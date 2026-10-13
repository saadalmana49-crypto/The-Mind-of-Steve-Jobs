# Publishing checklist

For maintainers. The repository is public at https://github.com/saadalmana49-crypto/The-Mind-of-Steve-Jobs.

## Before each release

```bash
python3 scripts/check.py                       # links, citations, versions, size budget, YAML
skills-ref validate skills/insanely-great      # Agent Skills spec (pip install from agentskills/agentskills)
claude plugin validate .                       # Claude Code marketplace and plugin manifests
```

## Repository "About" box

GitHub keeps the description, website, and topics as repository settings, not as files, so no commit can fill them in. Set them once.

**In the browser:** on the repository page, click the gear icon next to "About", then fill in:
- **Description:** `Insanely Great: remove complexity, keep capability. An Agent Skill inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design.`
- **Website:** leave empty, or use `https://agentskills.io` if you want to point to the format.
- **Topics:**
  - `agent-skills`
  - `claude-code`
  - `codex`
  - `gemini-cli`
  - `cursor`
  - `ai-agents`
  - `product-design`
  - `ux`
  - `simplicity`
  - `steve-jobs`
- Leave **Releases** and **Packages** ticked.

**Or with the GitHub CLI** (`brew install gh`, then `gh auth login`):

```bash
gh repo edit saadalmana49-crypto/The-Mind-of-Steve-Jobs \
  --description "Insanely Great: remove complexity, keep capability. An Agent Skill inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design." \
  --add-topic agent-skills --add-topic claude-code --add-topic codex --add-topic gemini-cli \
  --add-topic cursor --add-topic ai-agents --add-topic product-design --add-topic ux \
  --add-topic simplicity --add-topic steve-jobs
```

## Release a version

```bash
V=1.1.0   # the version being released
git push origin main
git tag -a "v$V" -m "Insanely Great $V"
git push origin "v$V"
git archive --format=zip --prefix=insanely-great/ -o "insanely-great-$V.zip" "v$V:skills/insanely-great"
gh release create "v$V" "insanely-great-$V.zip" \
  --title "Insanely Great $V" --notes-file "docs/release-notes/v$V.md"
```

## After pushing

Check the public install paths:

```bash
npx skills add saadalmana49-crypto/The-Mind-of-Steve-Jobs
gemini skills install https://github.com/saadalmana49-crypto/The-Mind-of-Steve-Jobs.git --path skills/insanely-great
claude plugin marketplace add saadalmana49-crypto/The-Mind-of-Steve-Jobs && claude plugin install insanely-great@insanely-great
```

The language bar should show mostly Markdown. `.gitattributes` makes GitHub count Markdown and leaves generated eval transcripts out of the count.

## Later releases

1. Update `metadata.version` in `skills/insanely-great/SKILL.md` and `version` in `.claude-plugin/plugin.json`.
2. Add a `CHANGELOG.md` entry and `docs/release-notes/vX.Y.Z.md`.
3. For behavior changes, rerun the evals and update `evals/results.md`.
4. Run the checks above, then tag and release as shown, with `V` set to the new version.
