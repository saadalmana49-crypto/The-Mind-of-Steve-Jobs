# Review procedure

Use this to critique a product, flow, screen, spec, pull request, API, or CLI. The goal is a short, ranked list of specific changes, each grounded in evidence. A long list of generic advice is not the goal.

## Start with what it is supposed to do

Lashinsky reports that after the troubled 2008 MobileMe launch, Jobs gathered the team and asked, "Can anyone tell me what MobileMe is supposed to do?" Then he asked why it didn't do that (LAS11). Begin every review the same way:
- State the purpose in one sentence, either from the user or inferred and labeled as an assumption.
- If no one can state it, that is the first finding.
- Judge everything else against that sentence.

## Procedure

1. **Purpose.** One sentence, as above.
2. **Hero path, first time.** Walk from arrival to first real value as a newcomer. Count these:
   - steps,
   - form fields,
   - decisions,
   - screens,
   - waits,
   - and the time to first value.
3. **Frequent path.** Walk the task an established user does most often. Count it the same way.
4. **State inventory.** Use the table in experience-design.md. List the missing or weak states.
5. **Element audit.** For each element, ask: is this capability someone needs, or complexity? Mark complexity to remove or merge. Place each capability on the ladder (see simplicity.md): keep, default, automate, move in context, move one level down, move to Advanced.
6. **Concept audit.** List the nouns the user must learn. Look for duplicates (two ways to organize, two names for one thing) and for implementation leaking into the UI.
7. **Consistency.** Check names, placement, behavior, and visual language across screens and platforms.
8. **Details.** Copy, feedback, speed, accessibility (contrast, labels, keyboard, target size), edge cases.
9. **Capability check.** If the review proposes cuts, list every capability affected and where it goes. Removing something people rely on, especially an expert workflow, is itself a finding (Major or Blocker).
10. **Whole product.** Do the email, docs, billing, support, and the leaving or export path feel like the same product?
11. **Trust.** Look for dark patterns: hidden skip buttons, forced card capture, confirmshaming, surprise charges, and cancellation that is hard to find.
12. **Rank and prescribe.** Order the findings by severity. Give each a specific fix. Say what to keep.

## Severity

| Level | Meaning | Examples |
|---|---|---|
| **Blocker** | Stops the core job, loses data, creates a security risk, excludes people, or removes a workflow people depend on | A draft lost when saving fails offline. Inputs wiped on error. No keyboard access to the main editor |
| **Major** | Big friction or drop-off on the hero path, or damage to trust | Twelve questions before the first result. An account required to see a sample. A raw "ERR_VALIDATION" message |
| **Minor** | Friction off the hero path, inconsistency | Two names for one concept. A misaligned secondary screen |
| **Polish** | The details that make it feel finished | Microcopy, transitions, empty-state illustration, spacing |

## Writing findings

Each finding is one line of problem, one line of evidence, and one line of fix. The fix must be concrete enough to implement.

```
[Major] The first workout appears only after 12 profile questions.
Evidence: Onboarding screens 1–4; 12 required fields, 3 of them about goals the app never uses.
Fix: Ask 2 questions (fitness level, minutes per day), show a workout immediately, learn the rest from use.
```

Avoid:
- findings without evidence,
- "consider improving X" with no change named,
- piles of polish items that bury the blockers.

## Say what to keep

A review that only lists problems invites a redesign of things that already work. Name the strengths explicitly so they survive the fixes.

## Optional scorecard

Use this only to compare two versions, or to track progress over time. Never use it in place of findings.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Purpose clarity | Can't be stated | Stated, but the product drifts from it | Mostly serves it | Every part serves it |
| Hero path economy | Value buried behind setup | Many avoidable steps | Few avoidable steps | Shortest credible path |
| State completeness | Happy path only | Some states | Most states | All states designed |
| Coherence | Conflicting concepts or names | Several inconsistencies | Minor inconsistencies | One model throughout |
| Craft of details | Rough | Uneven | Good | Finished |
| Depth preserved | Needed capabilities removed | Capabilities hard to find | Mostly reachable | Every capability reachable, experts fast |
| Accessibility | Blocks some users | Major gaps | Minor gaps | Meets WCAG AA and platform guidance |
| Honesty | Dark patterns present | Pushy | Neutral | Clear and respectful |

## Reviewing code and architecture with this lens

For a pull request, ask:
- Does this add a concept, option, mode, flag, or setting? Could a default or a single way of doing it replace it?
- Does it handle the error, empty, and slow states, with words the user understands?
- Is there a simpler design that delivers the same experience?
- Does it slow the hero path? By how much, for how many users? (See the arithmetic in experience-design.md.)
- Do names at the user-facing boundary (UI strings, API fields, CLI flags, error messages) use the user's vocabulary?
- Is the unseen quality there: tests on the hero path, useful logs, no silent failures?
- For architecture: does every component map to a written requirement? Are backups, auth, validation, and observability present? See engineering.md.

Don't turn a small PR review into a product critique. Keep the findings proportional to the change.

## Tone

Be direct and specific about the work, and respectful to the people.
- "I don't love it" is useful only when followed by the reason. Isaacson's account of the iPhone redesign gives one: the case competed with the display (ISA11).
- Taste is a judgment you explain, not a veto.
