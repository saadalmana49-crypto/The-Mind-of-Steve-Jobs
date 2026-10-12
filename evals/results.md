# Results

These results cover the released text of skill version 1.0.0. The final runs took place on 11–12 October 2026:
- **Agent:** Claude Code 2.1.296 in headless mode, model `sonnet`.
- **Judge:** `opus`.
- **Scale:** 14 scenarios, 3 reps per arm, so 84 agent runs and 126 blind judgments.

The method and its limitations are in [README.md](README.md). Every output, check, and judgment is in [runs/](runs/).

## Summary

| | Without the skill | With the skill |
|---|---|---|
| Checklist items passed | 146 / 192 (76%) | **189 / 192 (98%)** |
| Blind pairwise preference | 8 wins | **34 wins** (0 ties) |
| Skill activated without being named | — | 42 / 42 runs |
| Average length (words) | 743 | 727 |

## By scenario

| Scenario | Checks without | Checks with | Pairwise (with–without) | Words without → with |
|---|---|---|---|---|
| s1 New product plan | 3/15 | 15/15 | 3–0 | 1051 → 844 |
| s2 Eight overlapping features | 10/12 | 12/12 | 3–0 | 1300 → 1691 |
| s3 Onboarding review | 11/12 | 12/12 | 1–2 | 759 → 931 |
| s4 "Minimal like Apple" settings | 8/18 | 18/18 | 3–0 | 390 → 527 |
| s5 Roadmap for a 3-person team | 11/12 | 12/12 | 3–0 | 540 → 642 |
| s6 Air-quality monitor | 12/12 | 12/12 | 3–0 | 1153 → 836 |
| s7 Steve Jobs quotes | 6/9 | 9/9 | 3–0 | 335 → 500 |
| s8 Meeting-room tool | 11/12 | 12/12 | 2–1 | 597 → 649 |
| s9 Pro photo editor | 14/15 | 15/15 | 3–0 | 691 → 582 |
| s10 SaaS architecture | 11/15 | 14/15 | 2–1 | 1124 → 715 |
| s11 19-parameter function | 12/15 | 13/15 | 1–2 | 408 → 507 |
| h1 Video player (held out) | 17/18 | 18/18 | 2–1 | 425 → 494 |
| h2 Messaging API (held out) | 11/12 | 12/12 | 2–1 | 836 → 601 |
| h3 School-pickup app (held out) | 9/15 | 15/15 | 3–0 | 788 → 654 |

## What the skill changed

- **Simplifying stopped costing capability (s4, s9, h1).**
  - In s4, two of three runs without the skill removed in-app accessibility controls and the language override. All three left developer and beta options without a visible, labeled path.
  - With the skill, all 18 checks passed: accessibility, security, locale, and advanced options were kept and organized into labeled groups.
  - In s9, every professional tool stayed in all three runs. Newcomers got a calmer starting workspace.
- **Plans got a purpose and a shape (s1, h3).** Without the skill, no s1 run had a one-sentence purpose, a counted hero path, a reasoned deferred list, or designed states. With it, every check passed, and the plans were shorter.
- **No unsourced quotes (s7).** All three runs without the skill presented at least one quote outside the verified set as Jobs' exact words. All three runs with the skill used only verified quotes, cited them, and flagged misattributions.
- **Answers led with the decision.** On average, answers with the skill were slightly shorter than without it. A full spec that the user asked for (s2) is the main exception.

## Where the skill fell short

- **Losing on substance, not structure (s11, s3).** In s11, the judge preferred two baseline answers for cleaner type designs that separated rendering from delivery. In s3, it preferred two baseline reviews that covered more recovery and accessibility items. The with-skill reviews were tighter, but left some of those items out.
- **Errors that name the fix (s11, check 5).** Two of three runs promised "clear errors" without showing what the errors say.
- **Architecture slips (s10).** One with-skill run misestimated the load as about 2 invoices an hour instead of about 1 a minute. Another omitted input validation, even though the skill names it as a safeguard.
- **Some answers are longer.** Eight of fourteen scenarios got longer with the skill. In h1 and h2, the judge preferred a more concise or more detailed baseline answer once each.
- **The baseline is already strong** on s3, s6, s8, h1, and h2, so the measurable gains there are small.

## Notes on validity

- Some runs and judgments in earlier attempts hit the account's session limit and returned an error instead of an answer. None of those were graded:
  - `evals/run.py` outputs are checked before judging.
  - `evals/judge.py` refuses to grade failed runs, retries failed judgments, and reuses earlier grades only for outputs whose content hash is unchanged.
- The skill arm was rerun in full on the final skill text. The 42 baseline runs don't depend on the skill and were reused, with the same prompts.
- See [README.md](README.md#limitations) for the limitations: small samples, a model judging a model, one agent, single-turn prompts.
