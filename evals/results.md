# Results

These results cover skill version 1.1.0, compared with version 1.0.0 and with no skill:
- **Agent:** Claude Code 2.1.296 in headless mode, model `sonnet`.
- **Judge:** `opus`.
- **Scale:** 24 scenarios, 3 reps per arm, 3 arms. That makes 216 agent runs, 216 blind checklist gradings, and 144 blind pairwise judgments.
- **Dates:** the no-skill runs took place on 11–12 October 2026, the 1.0.0 runs on 12 October, and the 1.1.0 runs on 13 October, all on the final 1.1.0 text.

The method and its limitations are in [README.md](README.md). Every output, check, and judgment is in [runs/](runs/).

## Summary

| | No skill | Version 1.0.0 | Version 1.1.0 |
|---|---|---|---|
| Checklist items passed | 259 / 324 (80%) | 307 / 324 (95%) | **320 / 324 (99%)** |
| Original 14 scenarios (s1–s11, h1–h3) | 146 / 192 | 189 / 192 | 190 / 192 |
| New 10 scenarios (n1–n10) | 113 / 132 | 118 / 132 | 130 / 132 |
| Skill activated without being named | — | 60 / 72 | 64 / 72 |
| Average length (words) | 628 | 619 | 680 |
| Average cost per run, new scenarios | $0.031 | $0.056 | $0.050 |

In blind pairwise comparisons, the judge preferred version 1.1.0:
- **over no skill** in 64 of 72 (6 losses, 2 ties),
- **over version 1.0.0** in 51 of 72 (18 losses, 3 ties): 30–12 on the original scenarios, and 21–6, with 3 ties, on the new ones.

Cost is compared only on the new scenarios, because the earlier runs predate cost tracking. Across all 24 scenarios, a 1.1.0 run averaged $0.060.

## By scenario

Checks are given as no skill / 1.0.0 / 1.1.0. Pairwise results are 1.1.0's wins–losses, with ties added when there were any.

| Scenario | Checks | 1.1.0 vs. none | 1.1.0 vs. 1.0.0 | Words (none / 1.0.0 / 1.1.0) |
|---|---|---|---|---|
| s1 New product plan | 3 / 15 / 14 of 15 | 3–0 | 1–2 | 1051 / 844 / 760 |
| s2 Eight overlapping features | 10 / 12 / 12 of 12 | 3–0 | 3–0 | 1300 / 1691 / 1739 |
| s3 Onboarding review | 11 / 12 / 12 of 12 | 3–0 | 2–1 | 759 / 931 / 863 |
| s4 "Minimal like Apple" settings | 8 / 18 / 18 of 18 | 3–0 | 1–2 | 390 / 527 / 597 |
| s5 Roadmap for a 3-person team | 11 / 12 / 12 of 12 | 3–0 | 2–1 | 540 / 642 / 669 |
| s6 Air-quality monitor | 12 / 12 / 12 of 12 | 3–0 | 3–0 | 1153 / 836 / 1168 |
| s7 Steve Jobs quotes | 6 / 9 / 9 of 9 | 2–1 | 3–0 | 335 / 500 / 479 |
| s8 Meeting-room tool | 11 / 12 / 12 of 12 | 3–0 | 2–1 | 597 / 649 / 723 |
| s9 Pro photo editor | 14 / 15 / 15 of 15 | 3–0 | 2–1 | 691 / 582 / 733 |
| s10 SaaS architecture | 11 / 14 / 15 of 15 | 2–1 | 2–1 | 1124 / 715 / 773 |
| s11 19-parameter function | 12 / 13 / 15 of 15 | 3–0 | 2–1 | 408 / 507 / 602 |
| h1 Video player (held out) | 17 / 18 / 18 of 18 | 3–0 | 2–1 | 425 / 494 / 537 |
| h2 Messaging API (held out) | 11 / 12 / 12 of 12 | 3–0 | 3–0 | 836 / 601 / 722 |
| h3 School-pickup app (held out) | 9 / 15 / 14 of 15 | 3–0 | 2–1 | 788 / 654 / 748 |
| n1 Button label | 6 / 6 / 6 of 6 | 1–0, 2 ties | 1–0, 2 ties | 2 / 2 / 2 |
| n2 Removing unused features | 15 / 15 / 15 of 15 | 3–0 | 3–0 | 704 / 749 / 745 |
| n3 Single-page checkout | 6 / 9 / 15 of 15 | 3–0 | 3–0 | 674 / 675 / 722 |
| n4 AI writing assistant | 13 / 12 / 15 of 15 | 3–0 | 2–1 | 949 / 625 / 791 |
| n5 README opening | 8 / 10 / 10 of 12 | 1–2 | 2–1 | 167 / 156 / 184 |
| n6 Permission toggles | 14 / 15 / 15 of 15 | 1–2 | 1–2 | 360 / 607 / 616 |
| n7 One-line bug fix | 9 / 9 / 9 of 9 | 3–0 | 2–0, 1 tie | 91 / 117 / 118 |
| n8 Push notifications | 15 / 15 / 15 of 15 | 3–0 | 2–1 | 821 / 636 / 705 |
| n9 Six pricing plans | 15 / 15 / 15 of 15 | 3–0 | 3–0 | 503 / 588 / 659 |
| n10 Data pipeline | 12 / 12 / 15 of 15 | 3–0 | 2–1 | 398 / 531 / 660 |

## What 1.1.0 changed

- **Checkout kept the price breakdown (n3).** All three 1.0.0 runs built the requested page without an order summary, showing only the total before payment. All three 1.1.0 runs delivered the single page while keeping the subtotal, shipping, and total visible, and said why. This comes from the new exception to "they decide": the skill won't build a version that is deceptive, unsafe, or non-compliant.
- **Overlapping controls got merged (n4).** 1.0.0 merged tones, templates, and length in only one of three runs. 1.1.0 did it in all three.
- **Pipelines got diagnosed before being redesigned (n10).** 1.1.0 kept the data-quality, replay, and alerting safeguards, validated an incremental migration, and measured the causes of breakage first, in all three runs. 1.0.0 did each of these in two.
- **Errors got written out (s11).** 1.0.0 showed the actual error text in one run of three, and 1.1.0 in all three. This was a known gap in 1.0.0.
- **Lower cost than 1.0.0.** The main file shrank from about 4.4k to about 3k tokens. On the new scenarios, input dropped from 21.8k to 17.6k tokens per run, and cost from $0.056 to $0.050. That is still 61% more than no skill ($0.031).
- **Small tasks stayed small.** The skill stayed out of the button label (n1) and the bug fix (n7) in every run, as its description intends. Those answers stayed short: two words for the label, and about 120 for the fix (no skill: 91).

## Where 1.1.0 fell short

- **Longer answers.** 1.1.0 answers were longer than 1.0.0's in 19 of 24 scenarios, averaging 680 words against 619. That is above the skill's own 300–600-word target.
- **A capability lost while claiming nothing was (s4).** Two runs merged the sound and haptics switches into one toggle and still said no capability was removed. Both also miscounted the original settings. The checklist still passed, but the judge preferred 1.0.0 in both. The new rule to keep an honest capability ledger didn't prevent this.
- **Thinner product plans than 1.0.0 (s1).** The judge preferred 1.0.0 in two of three. Those plans covered more essentials, such as a client-facing payment page and invoices that can't be edited after sending. One 1.1.0 run designed error states only for bank sync, not for sending invoices or receiving payments.
- **Permissions (n6).** The no-skill answer won two of three, both times for covering the same design more concisely. 1.0.0 also won two of three: once for a design aimed more squarely at preventing mistakes, and once because a 1.1.0 run's numbers contradicted each other.
- **README rewrites (n5).** The skill activated in only one of three runs (1.0.0: none of three). The two runs without it gave readers no way to start, which is why the checklist shows 10 of 12. In the run where it did activate, the judge penalized guessed details, such as a scheduling feature and a package name, even though the answer flagged them as unverified.
- **Purpose statement (h3).** One run split the purpose across two sentences.

## Notes on validity

- **The new scenarios are not held out.** n1–n10 were written for 1.1.0, with checks written before the first runs. The text was then revised after failures on n3, n4, n5, s1, s3, and s8. So 1.1.0's gains on n1–n10 partly reflect tuning. h1–h3 remain the only held-out scenarios. There, 1.1.0 passed 44 of 45 checks (1.0.0: 45 of 45) and won 7 of 9 comparisons against 1.0.0.
- **Judge noise.** n1 and n7 rarely activate the skill in either version, so their pairwise results compare near-identical answers. The 1.1.0 "wins" there (for example 3–0 against no skill on n7) show how often the judge picks a side between equivalent answers. They are not evidence of improvement.
- **Session limits.** Runs hit the account's session limit three times and returned an error instead of an answer. None of those were graded: `evals/judge.py` refuses to grade failed runs, and they were rerun in full.
- See [README.md](README.md#limitations) for the other limitations: small samples, a model judging a model, one agent, single-turn prompts.
