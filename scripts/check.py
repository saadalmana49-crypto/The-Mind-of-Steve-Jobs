#!/usr/bin/env python3
"""Repository checks that the Agent Skills validator does not cover.

- SKILL.md stays within the progressive-disclosure budget (<500 lines, ~5k tokens).
- Every reference file is linked from SKILL.md, and every link resolves.
- Every citation key used in the skill, like (WWDC97), is defined in sources.md.
- The version matches across SKILL.md, plugin.json, and CHANGELOG.md.
- The Claude Code marketplace entry and plugin manifest agree.

Usage: python3 scripts/check.py   (standard library only; exits 1 on failure)
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "insanely-great"
errors = []


def fail(msg: str) -> None:
    errors.append(msg)


skill_md = (SKILL / "SKILL.md").read_text()
lines = skill_md.count("\n")
if lines >= 500:
    fail(f"SKILL.md has {lines} lines; keep it under 500.")
if len(skill_md) / 4 > 5000:
    fail(f"SKILL.md is about {len(skill_md) // 4} tokens; keep it under 5000.")

desc_line = next(l for l in skill_md.splitlines() if l.startswith("description:"))
desc_value = desc_line.split(":", 1)[1].strip()
if not desc_value.startswith(("'", '"')) and ": " in desc_value:
    fail("SKILL.md description contains ': ' without quotes, which is invalid YAML for strict parsers.")

for ref in sorted((SKILL / "references").glob("*.md")):
    if f"references/{ref.name}" not in skill_md:
        fail(f"{ref.name} is not referenced from SKILL.md, so agents will never load it.")

link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
for md in sorted(ROOT.rglob("*.md")):
    if "evals/runs" in md.as_posix() or "node_modules" in md.parts:
        continue
    text = re.sub(r"```.*?```", "", md.read_text(), flags=re.S)
    for target in link.findall(text):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        path = (md.parent / target.split("#")[0]).resolve()
        if not path.exists():
            fail(f"{md.relative_to(ROOT)}: broken link -> {target}")

sources = (SKILL / "references" / "sources.md").read_text()
defined = set(re.findall(r"^\| ([A-Z][A-Z0-9-]+) \|", sources, flags=re.M))
cite = re.compile(r"\(([A-Z][A-Z0-9]*(?:-[A-Z]+)?\d*)\)")
for md in [SKILL / "SKILL.md", *sorted((SKILL / "references").glob("*.md"))]:
    for key in cite.findall(md.read_text()):
        looks_like_key = any(c.isdigit() for c in key) or key.startswith("FL-")
        if looks_like_key and key not in defined:
            fail(f"{md.relative_to(ROOT)}: citation ({key}) is not defined in sources.md")

skill_version = re.search(r'version:\s*"([^"]+)"', skill_md).group(1)
plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
changelog = re.search(r"^## \[?(\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(), flags=re.M).group(1)
if not skill_version == plugin["version"] == changelog:
    fail(f"Version mismatch: SKILL.md {skill_version}, plugin.json {plugin['version']}, CHANGELOG {changelog}")

market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
if not market.get("owner", {}).get("name"):
    fail("marketplace.json needs owner.name")
entries = {p["name"]: p for p in market.get("plugins", [])}
if plugin["name"] not in entries:
    fail("marketplace.json has no entry matching plugin.json's name")

if errors:
    print("\n".join(f"FAIL {e}" for e in errors))
    sys.exit(1)
print(f"OK: SKILL.md {lines} lines, {len(defined)} sources, version {skill_version}")
