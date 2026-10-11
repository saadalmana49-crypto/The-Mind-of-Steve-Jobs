# Evaluations

These evals check whether the skill makes an agent's product decisions better, not just different. Results are in [results.md](results.md). The raw transcript for every scenario is in [runs/](runs/).

## Method

- **Agent under test:** Claude Code in headless mode (`claude -p`), model `sonnet`.
- **Isolation:** each run happens in a fresh temporary directory. Both arms load:
  - no user settings, skills, plugins, hooks, or MCP servers,
  - only the `Read` and `Skill` tools.
- **Two arms:**
  - **baseline:** an empty directory.
  - **skill:** the same, with `skills/insanely-great/` copied into the directory's `.claude/skills/`. Claude has to discover and activate the skill on its own, as it would for a real user. The prompts never mention the skill.
- **Repetitions:** 3 per scenario per arm.
- **Grading,** by `claude -p --model opus` with no tools, never told which arm produced an output:
  1. **Checklist:** each output is graded alone against the scenario's checks in [rubric.json](rubric.json). The checks were written before the final runs.
  2. **Pairwise:** the baseline and skill outputs for the same scenario and rep are shown as A and B in random order. The judge picks the one that would better help the person build a better product, and is told that length is not a virtue.

## Scenarios

| Id | Prompt (abridged) | What it tests |
|---|---|---|
| s1 | Plan a money app for freelancers | Purpose, hero path, focused v1, a depth plan, states |
| s2 | Spec a sidebar adding 8 overlapping organization features | Consolidating overlapping concepts without silently dropping requests |
| s3 | Review a 6-screen SaaS onboarding | Quantified, ranked, specific review |
| s4 | "Make settings minimal like Apple" (26 items) | Guardrails: accessibility, security, locale, and advanced options kept. No secret gestures |
| s5 | Prioritize 12 roadmap items for a 3-person team | Focus, reasons for each "no", what would change the call |
| s6 | End-to-end experience for an air-quality monitor | Device works without the app, setup target, failure states |
| s7 | "Give me 6 Steve Jobs quotes about simplicity" | No fabricated or misattributed quotes |
| s8 | Build a meeting-room booking tool for 15 people | Configure before building. A proportionate design |
| s9 | Simplify a professional photo editor | Simpler for newcomers while keeping every pro capability and expert speed |
| s10 | Architecture for a 4-person B2B invoicing SaaS | Simple underneath at the same quality bar (safeguards, money handling) |
| s11 | Simplify a 19-parameter export function used in 40 places | A simpler API without losing capability or breaking callers |
| h1 | "Make our video player minimal like Apple" | Held out: captions, audio description, keyboard, and advanced controls kept |
| h2 | Add WhatsApp and RCS to an SMS API with six endpoints | Held out: unifying instead of multiplying, compatibility |
| h3 | Plan a school-pickup coordination app | Held out: focus without cutting child safety |

How the scenarios relate to the skill's development:
- **s1–s8:** run without the skill first. The skill was written to address the failures seen there. This is the "red, then green" method for skills.
- **h1–h3:** written after the first draft, and the skill text was never tailored to them.
- **s9–s11:** added when the skill's scope was broadened to cover keeping capability and engineering.
- **Contamination check:** the worked examples in `references/examples.md` deliberately use different domains from all scenarios. Some teach the same patterns, for example refactoring with a deprecation adapter, which is the point of the skill.

## Rerun

Requires Claude Code signed in. Uses your plan's quota: about 84 agent runs and 126 judge calls for the full set.

```bash
python3 evals/run.py --arm baseline --reps 3 --out evals/runs/raw
python3 evals/run.py --arm skill --reps 3 --out evals/runs/raw
python3 evals/judge.py --runs evals/runs/raw      # writes evals/runs/<scenario>.md and prints the table
```

Run a subset with `--scenarios s4,h1`. Add a scenario by writing its prompt to `scenarios/<id>-<name>.txt` and its checks to `rubric.json`, before looking at any outputs.

## Limitations

- **Small samples.** Three reps per arm is enough to see consistent differences, not to estimate effect sizes precisely.
- **A model judging a model.** The judge (Opus) and the agent (Sonnet) are from the same model family. The judge is blind to the arm, but it may share the agent's tastes. The checklist is more objective than the pairwise preference. Read the transcripts.
- **One agent.** The behavioral numbers come from Claude Code only. Other agents were tested for discovery and installation, not behavior (see [docs/compatibility.md](../docs/compatibility.md)).
- **Single-turn prompts.** Real sessions involve follow-ups, code, and existing context. These prompts measure the first answer.
