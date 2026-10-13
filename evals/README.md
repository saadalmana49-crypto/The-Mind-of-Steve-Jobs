# Evaluations

These evals check whether the skill makes an agent's product decisions better, not just different. Results are in [results.md](results.md). The raw transcript for every scenario is in [runs/](runs/).

## Method

- **Agent under test:** Claude Code in headless mode (`claude -p`), model `sonnet`.
- **Isolation:** each run happens in a fresh temporary directory. Both arms load:
  - no user settings, skills, plugins, hooks, or MCP servers,
  - only the `Read` and `Skill` tools.
- **Arms:**
  - **baseline:** an empty directory, with no skill.
  - **skill:** the current `skills/insanely-great/`, copied into the directory's `.claude/skills/`. Claude has to discover and activate it on its own, as it would for a real user. The prompts never mention the skill.
  - **v1, or any other label:** an older version of the skill, installed with `--skill-dir`. Used for before-and-after comparisons.
- **Repetitions:** 3 per scenario per arm.
- **Grading,** by `claude -p --model opus` with no tools, never told which arm produced an output:
  1. **Checklist:** each output is graded alone against the scenario's checks in [rubric.json](rubric.json). The checks were written before the final runs.
  2. **Pairwise:** two arms' outputs for the same scenario and rep are shown as A and B in random order. The judge picks the one that would better help the person build a better product, and is told that length is not a virtue. The comparisons run are baseline vs. skill and v1 vs. skill.
- **Cost:** each run records the input and output tokens and the dollar cost Claude Code reports.

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
| n1 | "Suggest a better label than Submit" | Proportion: a one-line answer, no framework |
| n2 | Remove four features with zero usage | Removing cleanly when the evidence supports it |
| n3 | Single-page checkout, minus summary, shipping line, and terms | Simplicity versus payment transparency and legal terms |
| n4 | AI writing assistant with 8 requested controls | Consolidating controls, keeping advanced ones reachable |
| n5 | Rewrite a hype-filled README opening | Plain claims, no invented facts, a way to start |
| n6 | 40 permission toggles per role | Presets, keeping fine-grained control, preventing mistakes |
| n7 | Fix a one-line discount bug | Proportion: just the fix |
| n8 | 14 kinds of push notifications | Fewer, smarter notifications, keeping user control |
| n9 | Six pricing plans | Fewer plans, protecting existing customers |
| n10 | 23 Airflow DAGs and a custom retry framework | Simplifying a pipeline without losing its safeguards |

How the scenarios relate to the skill's development:
- **s1–s8:** run without the skill first. The skill was written to address the failures seen there. This is the "red, then green" method for skills.
- **h1–h3:** written after the first draft, and the skill text was never tailored to them.
- **s9–s11:** added when the skill's scope was broadened to cover keeping capability and engineering.
- **n1–n10:** added for version 1.1.0, to cover more domains and the ways the skill can misfire: applying the method to tasks too small for it, refusing a removal the evidence supports, and inventing facts.
- **Contamination check:** the worked examples in `references/examples.md` deliberately use different domains from all scenarios. Some teach the same patterns, for example refactoring with a deprecation adapter, which is the point of the skill.

## Rerun

Requires Claude Code signed in. The runs use your plan's quota: 72 agent runs per arm for all 24 scenarios, plus the judge calls. Grades are cached, so a rerun only regrades the outputs that changed.

```bash
python3 evals/run.py --arm baseline --reps 3 --out evals/runs/raw
python3 evals/run.py --arm skill --reps 3 --out evals/runs/raw
python3 evals/judge.py --runs evals/runs/raw      # writes evals/runs/<scenario>.md and prints the table
```

To compare against an older version, export it from git and run it as its own arm:

```bash
mkdir -p /tmp/v1 && git archive 80f16af skills/insanely-great | tar -x -C /tmp/v1
python3 evals/run.py --arm v1 --skill-dir /tmp/v1/skills/insanely-great --reps 3 --out evals/runs/raw
python3 evals/judge.py --runs evals/runs/raw --pairs baseline:skill,v1:skill
```

Run a subset with `--scenarios s4,h1`. Add a scenario by writing its prompt to `scenarios/<id>-<name>.txt` and its checks to `rubric.json`, before looking at any outputs.

## Limitations

- **Small samples.** Three reps per arm is enough to see consistent differences, not to estimate effect sizes precisely.
- **A model judging a model.** The judge (Opus) and the agent (Sonnet) are from the same model family. The judge is blind to the arm, but it may share the agent's tastes. The checklist is more objective than the pairwise preference. Read the transcripts.
- **One agent.** The behavioral numbers come from Claude Code only. Other agents were tested for discovery and installation, not behavior (see [docs/compatibility.md](../docs/compatibility.md)).
- **Judge noise.** n1 and n7 rarely activate the skill in either version, so their v1-vs-skill comparisons are mostly noise between equivalent answers. Read those numbers as a measure of judge noise, not as wins or losses.
- **Single-turn prompts.** Real sessions involve follow-ups, code, and existing context. These prompts measure the first answer.
