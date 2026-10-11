#!/usr/bin/env python3
"""Run the eval scenarios through Claude Code in headless mode.

Each run happens in a fresh temporary directory. In the `skill` arm the skill is
copied into that directory's `.claude/skills/`, so Claude Code has to discover
and activate it on its own, the same way it would for a real user. In the
`baseline` arm the directory is empty.

Both arms load no user settings, no user skills, no plugins, no hooks and no MCP
servers, and only the Read and Skill tools are available.

Usage:
  python3 evals/run.py --arm baseline --out evals/runs/raw
  python3 evals/run.py --arm skill --reps 2 --model sonnet --scenarios s1,s4

Requires: Claude Code (`claude`) signed in. Standard library only.
"""

import argparse
import concurrent.futures
import json
import pathlib
import shutil
import subprocess
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "insanely-great"
SCENARIO_DIR = ROOT / "evals" / "scenarios"


def run_one(scenario: pathlib.Path, arm: str, rep: int, model: str, out: pathlib.Path) -> dict:
    prompt = scenario.read_text().strip()
    work = pathlib.Path(tempfile.mkdtemp(prefix=f"ig-{scenario.stem}-{arm}-"))
    if arm == "skill":
        shutil.copytree(SKILL_DIR, work / ".claude" / "skills" / SKILL_DIR.name)
    cmd = [
        "claude", "-p", prompt,
        "--setting-sources", "project",
        "--strict-mcp-config",
        "--tools", "Read,Skill",
        "--no-session-persistence",
        "--model", model,
        "--output-format", "stream-json",
        "--verbose",
    ]
    started = time.time()
    proc = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=900)
    record = {
        "scenario": scenario.stem,
        "arm": arm,
        "rep": rep,
        "model": model,
        "skill_invoked": False,
        "reads": [],
        "result": "",
        "seconds": round(time.time() - started, 1),
        "exit_code": proc.returncode,
    }
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "assistant":
            for block in event.get("message", {}).get("content", []):
                if block.get("type") != "tool_use":
                    continue
                if block.get("name") == "Skill" and "insanely-great" in json.dumps(block.get("input", {})):
                    record["skill_invoked"] = True
                if block.get("name") == "Read":
                    path = block.get("input", {}).get("file_path", "")
                    record["reads"].append(path.split(".claude/skills/")[-1])
        elif event.get("type") == "result":
            record["result"] = event.get("result", "")
    if not record["result"]:
        record["stderr"] = proc.stderr[-2000:]
    shutil.rmtree(work, ignore_errors=True)
    name = f"{scenario.stem}__{arm}__r{rep}.json"
    (out / name).write_text(json.dumps(record, indent=2, ensure_ascii=False))
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--arm", choices=["baseline", "skill"], required=True)
    parser.add_argument("--reps", type=int, default=1)
    parser.add_argument("--model", default="sonnet")
    parser.add_argument("--scenarios", default="", help="comma-separated ids, e.g. s1,s4 (default: all)")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--out", default=str(ROOT / "evals" / "runs" / "raw"))
    args = parser.parse_args()

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    wanted = {s.strip() for s in args.scenarios.split(",") if s.strip()}
    scenarios = [p for p in sorted(SCENARIO_DIR.glob("*.txt")) if not wanted or p.stem.split("-")[0] in wanted]
    jobs = [(s, rep) for s in scenarios for rep in range(1, args.reps + 1)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(run_one, s, args.arm, rep, args.model, out) for s, rep in jobs]
        for future in concurrent.futures.as_completed(futures):
            r = future.result()
            status = "skill" if r["skill_invoked"] else "-"
            print(f"{r['scenario']:<24} {r['arm']:<8} r{r['rep']}  {r['seconds']:>6}s  {status}  exit={r['exit_code']}")


if __name__ == "__main__":
    main()
