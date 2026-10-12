# Publishing checklist

For maintainers. Everything here runs once, when a release is approved. The repository is ready on `main`. Nothing has been pushed.

## Before publishing

```bash
python3 scripts/check.py                       # links, citations, versions, size budget
skills-ref validate skills/insanely-great      # Agent Skills spec (pip install from agentskills/agentskills)
claude plugin validate .                       # Claude Code marketplace and plugin manifests
```

## Publish v1.0.0

Requires the GitHub CLI (`brew install gh`, then `gh auth login`).

```bash
# 1. Create the public repository and push main
gh repo create saadalmana49-crypto/insanely-great --public --source . --push \
  --description "Remove complexity, keep capability. An Agent Skill inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design."

# 2. Topics, for discovery
gh repo edit saadalmana49-crypto/insanely-great \
  --add-topic agent-skills --add-topic claude-code --add-topic codex --add-topic gemini-cli \
  --add-topic cursor --add-topic ai-agents --add-topic product-design --add-topic ux \
  --add-topic simplicity --add-topic steve-jobs

# 3. Tag the release and attach the zipped skill
git tag -a v1.0.0 -m "Insanely Great 1.0.0"
git push origin v1.0.0
git archive --format=zip --prefix=insanely-great/ -o insanely-great-1.0.0.zip v1.0.0:skills/insanely-great
gh release create v1.0.0 insanely-great-1.0.0.zip \
  --title "Insanely Great 1.0.0" --notes-file docs/release-notes/v1.0.0.md
```

## After publishing

Run these checks against the live repository. They could not be run before it existed:

```bash
npx skills add saadalmana49-crypto/insanely-great -g -a claude-code -y   # in a scratch HOME
gemini skills install https://github.com/saadalmana49-crypto/insanely-great.git --path skills/insanely-great
claude plugin marketplace add saadalmana49-crypto/insanely-great && claude plugin install insanely-great@insanely-great
```

Optional:
- Add a social preview image under Settings → General.
- Submit the plugin to Anthropic's directory (see the Claude Code docs, "Submit to Anthropic's directory").

## Later releases

1. Update `metadata.version` in `skills/insanely-great/SKILL.md` and `version` in `.claude-plugin/plugin.json`.
2. Add a `CHANGELOG.md` entry and `docs/release-notes/vX.Y.Z.md`.
3. For behavior changes, rerun the evals and update `evals/results.md`.
4. Run the three checks above, then repeat step 3 of "Publish" with the new version.
