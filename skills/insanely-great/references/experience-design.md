# Experience design: design is how it works

"It's not just what it looks like and feels like. Design is how it works" (NYT03). Judge a design by using it, path by path and state by state. A static mockup or a code diff is only part of it.

## Walk the whole journey

Everything the user touches is the product. For each stage, write down what the user sees, what they do, and what can go wrong:

| Stage | Often forgotten |
|---|---|
| Discover and evaluate | What the landing page or README promises, compared with what the product does |
| Get it | Install size, permissions requested, sign-up demands |
| Set up | Questions that could be defaults, import from the old tool |
| First value | The time it takes and the number of steps. The empty state |
| Repeat use | Speed of the frequent task, shortcuts, remembered context |
| Failure and recovery | Errors, offline, undo, lost work, support |
| Growth | Lots of data, more people, more devices |
| Change | Updates, migrations, price changes, deprecations |
| Leave | Export, cancel, delete, what happens to their data |

## State inventory

For every screen or flow on the hero path, decide what the user sees and can do in each state. Missing states are the most common defect in software built by agents.

| State | Check |
|---|---|
| First run | Does it teach the first action, or show an empty shell? |
| Empty | Does it explain what will appear here and how to make it appear? |
| Loading | Is progress shown without a layout jump, and is it cancellable when slow? |
| Partial | Some data, or some items failed. Shown honestly? |
| Success | Is the result confirmed, with the next step obvious? |
| Error: the user's mistake | Inline, specific, preserves input, says how to fix it |
| Error: the system's fault | Plain words, no blame, a retry, nothing lost |
| Offline or slow network | Is work queued or saved, with clear status? |
| Permission denied | Explains why it's needed, offers a path forward |
| Scale | 0, 1, many, too many. Long names. Huge files |
| Interrupted | App closed mid-flow, two tabs, two devices editing |

## Interaction quality

- **Act on the thing itself.** Jobs' case for the multi-touch iPhone was that fingers beat a stylus, the device you are "born with ten of" (IPH07). Prefer direct manipulation and visible objects to modes, menus, and indirection.
- **Respond immediately.** Every action gets visible acknowledgement right away. A common rule of thumb from HCI research is about 100 ms to feel instant and about 1 s to keep the user's flow. If work takes longer, show progress.
- **Be forgiving.** Undo beats "Are you sure?" for anything reversible. Keep confirmation for what can't be undone, and name the consequence: "Delete 3 projects and their files".
- **Default rather than ask.** Each question costs attention. Ask only what you can't infer.
- **Be consistent.** The same thing has the same name, the same place, and the same behavior everywhere: web, mobile, email, docs, API.
- **Borrow what people already understand.** Hertzfeld recalls Jobs walking Bill Atkinson around the neighborhood to point out that rounded rectangles were everywhere. They became a basic drawing primitive of the Mac (FL-RECT). Look at the conventions people already know, from the platform and from the physical world, before inventing new ones.

## Two paths: newcomers and experts

A product is simple when a newcomer succeeds on the first try *and* an expert works at full speed. Design and test both paths:

| | Newcomer | Expert |
|---|---|---|
| Needs | One obvious next step, plain words, safe defaults, no dead ends | Speed, density, control, automation, no repeated questions |
| Give them | A guided first run, an empty state that teaches, sensible defaults | Shortcuts, a command palette, bulk actions, saved setups, an API, configurable views |
| Don't | Show every option at once | Hide capabilities with no visible path, or force them through the newcomer's steps every time |

- **Progressive disclosure,** done properly, reveals depth as people need it: in context, one level down, or in a labeled Advanced area. Use the placement ladder in simplicity.md.
- **Advanced features follow the same rules** as everything else: consistent names, visible entry points, the same behavior everywhere.
- **Measure both paths:** steps to first value for a newcomer, and time on the most frequent task for an expert.

## Money moments

Checkout, upgrades, and cancellations are where simplification most often turns into a trust problem.
- **Fewer steps is good. Less information is not.** Before people pay, show what they are buying and the itemized cost: subtotal, shipping, taxes, fees.
- **Keep the terms, return, and cancellation information people are entitled to,** one tap away. Where the law requires explicit consent, keep it explicit.
- **Make the price people see the price they pay.** No surprises on the last step.

## Speed is part of the design

Hertzfeld recounts Jobs pressing the engineer working on the Mac's boot time. Multiplied across millions of users, ten seconds saved per boot added up to lifetimes ("Saving Lives", FL-SAVE). Use the same arithmetic to decide what to optimize:

```
seconds saved × times per day × users = time returned to people per day
```

Examples:
- A search that takes 3 seconds, used 20 times a day by 50,000 people, costs about 830 hours a day.
- Making it feel instant returns almost all of that.

Set budgets for the hero path, and measure on realistic devices and networks:
- launch or first render,
- the core action,
- search,
- save.

## Words are interface

- Use the user's vocabulary, not the implementation's. "Couldn't save. You're offline. We'll retry when you're back," not "Sync error 0x8004".
- A good error says what happened, what to do now, and whether anything was lost. Add a code only for support, after the plain words.
- Buttons name the outcome: "Send invoice", not "Submit". "Delete 3 notes", not "OK".
- Empty states name the first action: "No invoices yet. Create your first one."
- Use one name per concept throughout.

## Visual craft

- **The content is the hero.** Isaacson reports that late in the original iPhone's development, Jobs told Ive he didn't love the design, because the case competed with the display. The team reworked it (ISA11). If the frame, chrome, or decoration competes with the content, take it away.
- **One primary action per screen.** Secondary actions look secondary.
- **Hierarchy through type and space first,** color second. Keep the type scale small and the spacing consistent, and align everything to a grid.
- **Use color with restraint.** Reserve accent color for meaning (primary action, state, selection). Never use color as the only signal.
- **Motion explains change.** Use it to show where something came from or went. Respect reduced-motion settings.
- **Follow the platform's conventions for behavior,** and the product's identity for look. Consistency across platforms means the same model and voice, not identical pixels.

## Carry quality through to the parts nobody sees

The carpenter "not going to use a piece of plywood on the back" (PB85). The Mac team signing the inside of the case (FL-SIGN). In software, the back of the cabinet is:
- Error, empty, edge, and offline states.
- The accessibility tree:
  - labels, roles, focus order,
  - visible focus,
  - keyboard operation.
- Reduced motion, contrast, dynamic text sizes.
- Localization: text expansion, plurals, right-to-left layouts, date and number formats.
- Transactional email, receipts, notifications. Their copy, timing, and how to unsubscribe.
- API error bodies, logs, diagnostics, support tooling.
- Uninstall, cleanup, data export.
- Docs and examples that actually run.
- The code itself: readable, tested, fast on the hero path.

## Accessibility is part of how it works

Treat these as requirements, not polish:
- Text contrast of at least 4.5:1 (3:1 for large text), per WCAG 2.x AA.
- Touch targets around 44×44 pt (iOS) or 48×48 dp (Android). WCAG 2.2 sets a 24×24 CSS px minimum.
- Every control has an accessible name. Icon-only buttons have labels.
- Never convey meaning by color alone.
- Captions or transcripts for media.
- Full keyboard operation with visible focus.
- Respect dynamic type and text scaling without clipping.
- Honor reduced-motion and contrast preferences. Keep in-app controls where the app renders its own text or motion.

## Polish pass: before calling it done

- [ ] Hero path walked from a clean state, with the step count recorded.
- [ ] Expert path walked: every advanced capability is reachable through a labeled path, and the frequent tasks are fast.
- [ ] Every state in the inventory has a designed response.
- [ ] Copy read aloud: plain words, consistent names, no implementation jargon.
- [ ] One primary action per screen. Alignment and spacing consistent.
- [ ] Measured against the speed budget on a realistic device or network.
- [ ] Accessibility checks above pass.
- [ ] Destructive actions are confirmed or undoable. No input is lost on error.
- [ ] Touchpoints outside the app (email, docs, billing) match the product.
