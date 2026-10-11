# Contributing

Thanks for helping. Insanely Great is inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design. It is meant to be a practical, independent method for any technology product. It is not an Apple style guide or a tribute. Three standards matter more than anything else:
1. Every historical claim must be traceable to a source.
2. Every instruction must change what an agent actually does.
3. **Remove complexity, keep capability.** Guidance must never push agents to delete essential functions, valuable advanced features, accessibility, or quality in the name of simplicity.

## Scope

The skill covers technology products and projects of every kind:
- software, apps, and platforms,
- APIs, SDKs, CLIs, and developer tools,
- digital services and internal tools,
- physical and connected products.

It applies across:
- strategy, architecture, and engineering,
- user experience, interface, and workflows,
- feature organization, performance, and maintainability,
- the whole user journey.

Contributions that narrow it to one platform, one aesthetic, or one company's way of doing things will be asked to generalize.

## Contributions we want

- **Source corrections.** A misquote, a wrong date, a better primary source. Open a "Source correction" issue or a PR that edits `skills/insanely-great/references/sources.md`.
- **Behavior reports.** Cases where an agent using the skill made a worse decision than it should have: cutting something needed, getting verbose, missing a state. Include the prompt, the agent and version, and the output.
- **Compatibility reports.** You ran the skill in an agent we list as "Documented". Tell us the version and what you checked, and we'll mark it tested in [docs/compatibility.md](docs/compatibility.md).
- **New guidance or examples,** with evidence that they help (see "Testing changes" below).

## Source standards

- Use the grades in `sources.md`:
  - **A:** Jobs' own recorded words.
  - **B:** a first-hand account.
  - **C:** later interpretation.
- Quote only what you have checked against a transcript, an archived original, or a reproduction of the original text. Add new quotes to the "Verified quotes" list with their key.
- Paraphrase anything else, and attribute it ("Isaacson reports…").
- Cite sources by key in the skill files, for example `(WWDC97)`. `scripts/check.py` fails if a key is not defined in `sources.md`.
- Keep to technology products: design, engineering, product strategy, presentation. Leave out personal, spiritual, or unrelated material.

## Writing standards

- **Write for the agent's behavior.** Each instruction should change a decision or an output. Remove anything that only sounds wise.
- **Prefer recipes to prohibitions** for output shape ("lead with the recommendation"). Use explicit guardrails and rationalization tables only for judgment failures seen in testing.
- **Keep `SKILL.md` small:** under 500 lines and about 5,000 tokens. Detail goes in `references/`, linked directly from `SKILL.md` (one level deep).
- **Keep the skill portable.** Use only the open-standard frontmatter fields: `name`, `description`, `license`, `metadata`. Tool-specific behavior belongs in the docs, not in `SKILL.md`.
- **Don't use eval scenario domains in examples.** `references/examples.md` deliberately avoids the domains in `evals/scenarios/`, so the evals measure general behavior, not memorized answers.
- **Plain language, no hype.** Examples are labeled as illustrations, not history.

## Testing changes

```bash
python3 scripts/check.py                         # links, citations, versions, size budget
pip install "git+https://github.com/agentskills/agentskills.git#subdirectory=skills-ref"
skills-ref validate skills/insanely-great        # Agent Skills spec
```

For changes meant to alter agent behavior, run the evals before and after. They need Claude Code signed in, and they use your plan's quota:

```bash
python3 evals/run.py --arm baseline --reps 3 --out evals/runs/raw
python3 evals/run.py --arm skill --reps 3 --out evals/runs/raw
python3 evals/judge.py --runs evals/runs/raw
```

Put the before and after numbers in your PR. If you add a scenario, add its checks to `evals/rubric.json` before you look at any outputs.

## Versioning

The skill follows Semantic Versioning, interpreted for instructions rather than code:
- **Major:** changes that break expectations. Renaming the skill, removing a mode or an output format, or removing a reference file other tools or prompts may point to.
- **Minor:** new guidance, a new reference file, new examples, or broader triggers. Behavior changes that keep the existing contract.
- **Patch:** corrections to sources, wording, links, or typos that are not meant to change behavior.

To release:
1. Bump the version in `skills/insanely-great/SKILL.md` (`metadata.version`) and `.claude-plugin/plugin.json`, and add a `CHANGELOG.md` entry. `scripts/check.py` fails if these disagree.
2. Merge to `main`, then tag `vX.Y.Z` and publish a GitHub release with the changelog entry.

## Reviews and conduct

- PRs need one maintainer review.
- Changes to `SKILL.md` or the guardrails get the closest look. Skills run with the agent's permissions, so instruction changes are reviewed as carefully as code.
- Be direct about the work and respectful to people. Maintainers may edit, lock, or remove comments, issues, and PRs that are harassing or off-topic.
