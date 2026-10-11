# Results

Run on 11 October 2026 with skill version 1.0.0. The agent was Claude Code 2.1.296 in headless mode with model `sonnet`. The judge was `opus`. There were 14 scenarios, with 3 reps per arm: 84 agent runs and 126 blind judgments. The method and limitations are in [README.md](README.md). Every output and judgment is in [runs/](runs/).

## Summary

| | Without the skill | With the skill |
|---|---|---|
| Checklist items passed | 146 / 192 (76%) | **187 / 192 (97%)** |
| Blind pairwise preference | 6 wins | **36 wins** (0 ties) |
| Skill activated without being named | — | 40 / 42 runs |
| Average length (words) | 743 | 824 |

## By scenario

| Scenario | Checks without | Checks with | Pairwise (with–without) | Activated | Words without → with |
|---|---|---|---|---|---|
| s1 New product plan | 3/15 | 14/15 | 3–0 | 3/3 | 1051 → 863 |
| s2 Eight overlapping features | 10/12 | 12/12 | 3–0 | 3/3 | 1300 → 1679 |
| s3 Onboarding review | 11/12 | 12/12 | 2–1 | 3/3 | 759 → 947 |
| s4 "Minimal like Apple" settings | 8/18 | 18/18 | 3–0 | 3/3 | 390 → 553 |
| s5 Roadmap for a 3-person team | 11/12 | 12/12 | 3–0 | 3/3 | 540 → 697 |
| s6 Air-quality monitor | 12/12 | 12/12 | 3–0 | 3/3 | 1153 → 1260 |
| s7 Steve Jobs quotes | 6/9 | 9/9 | 3–0 | 3/3 | 335 → 468 |
| s8 Meeting-room tool | 11/12 | 12/12 | 3–0 | 3/3 | 597 → 746 |
| s9 Pro photo editor | 14/15 | 15/15 | 3–0 | 3/3 | 691 → 692 |
| s10 SaaS architecture | 11/15 | 12/15 | 2–1 | **1/3** | 1124 → 949 |
| s11 19-parameter function | 12/15 | 15/15 | 2–1 | 3/3 | 408 → 561 |
| h1 Video player (held out) | 17/18 | 18/18 | 1–2 | 3/3 | 425 → 565 |
| h2 Messaging API (held out) | 11/12 | 12/12 | 2–1 | 3/3 | 836 → 654 |
| h3 School-pickup app (held out) | 9/15 | 14/15 | 3–0 | 3/3 | 788 → 895 |

## What changed with the skill

- **Simplicity stopped costing capability (s4).** Without the skill:
  - Two of three runs removed in-app accessibility controls (text size, reduced motion, or high contrast) and the language override.
  - All three runs hid developer and beta options behind a secret gesture or left no labeled path to them.

  With the skill, all 18 checks passed: accessibility, security, locale, and advanced options were kept and grouped, behind visible labels.
- **Plans got a purpose and a shape (s1, h3).**
  - Without the skill, no run of s1 had a one-sentence purpose, a counted hero path, a reasoned deferred list, or designed states.
  - With it, those checks passed in 14 of 15 cases, and the plans were shorter on average.
  - Child safety stayed in scope in every h3 run, with and without the skill.
- **No fabricated quotes (s7).** All three runs without the skill offered at least one quote that is not in the verified set, presented as verbatim. All three runs with the skill used only verified quotes, gave citations, and flagged misattributions.
- **Refactoring kept every capability and gave clear errors (s11).** All three runs with the skill passed all five checks, including validation with errors that name the fix. That check was missed in every run without the skill.

## Where the skill fell short

- **Activation on architecture prompts (s10).** Claude invoked the skill on its own in only 1 of 3 architecture runs. The description lists architecture, but a plain "propose the system architecture" prompt often didn't trigger it. Invoking it explicitly (`/insanely-great`) avoids this.
- **Safeguards in architecture (s10, check 2).** Neither arm passed this check in any run. Both usually named some of auth, tenant isolation, tested restores, validation, and observability, but never all of them.
- **Length.**
  - With the skill, answers were longer in 11 of 14 scenarios, despite the response-shape guidance.
  - Four of the six pairwise losses cite concision. The other two preferred the baseline for more concrete detail (h2) and a stronger type design (s11).
  - One loss cites skill vocabulary leaking into the answer: a "Rung" column. After this run, a sentence was added to `SKILL.md` telling the agent to keep the ladder's vocabulary internal. That change has not been re-measured.
- **The baseline is strong.** On several scenarios (s3, s6, h1, h2), the base model already passed most checks. The gains there are smaller, and in h1 the judge preferred the baseline 2 to 1.

## Notes on validity

- During the first attempt, 29 runs with the skill hit the account's session limit and returned an error message instead of an answer. Those runs were discarded and rerun with the same skill version before any judging. `evals/judge.py` now refuses to grade failed runs.
- The 33 runs without the skill for s1–s8 and h1–h3 come from an earlier batch. The baseline doesn't depend on the skill, so it didn't need to be rerun. The prompts are identical.
- See [README.md](README.md#limitations) for the limitations: small samples, a model judging a model, one agent, single-turn prompts.
