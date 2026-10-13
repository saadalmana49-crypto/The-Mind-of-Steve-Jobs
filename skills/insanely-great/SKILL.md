---
name: insanely-great
description: Product judgment inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design. Remove complexity, keep capability. For technology products of every kind (software, apps, platforms, APIs, developer tools, digital services, hardware). Use when planning a product or feature; choosing scope, priorities, pricing, or a roadmap; proposing an architecture, backend, data model, or pipeline; designing or refactoring APIs, SDKs, CLIs, workflows, permissions, or notifications; reviewing UX, UI, flows, or code for unnecessary complexity; simplifying, consolidating, removing, or deprecating features without losing what people need; improving performance or maintainability; designing hardware or connected products; or writing or rewriting README, landing-page, positioning, or launch copy. Also use when asked to make something simpler, more focused, more polished, "like Apple" or "like Steve Jobs", or when quoting Jobs. Not for routine bug fixes, small copy tweaks, or mechanical edits.
license: MIT
metadata:
  version: "1.1.0"
  source: "https://github.com/saadalmana49-crypto/The-Mind-of-Steve-Jobs"
---

# Insanely Great

Build technology products that are complete and powerful underneath, and simple, clear, and effortless on the surface. The method is inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design. Sources are in `references/sources.md`.

**It is a lens, not a persona:**
- Apply the reasoning to your users, your platform, and your brand.
- Never imitate Jobs' voice or Apple's look.
- The user owns the product. Recommend, let them decide, and never drop something they asked for without saying so.

## The core rule: remove complexity, keep capability

- **Complexity** is whatever makes a product harder to understand, use, build, or change than it needs to be:
  - duplicate concepts,
  - needless decisions and steps,
  - implementation details leaking into the experience,
  - inconsistency,
  - extra layers,
  - slow paths.
- **Capability** is what the product lets people do:
  - essential functions,
  - valuable advanced features,
  - expert speed,
  - integrations and export,
  - reliability, security, and access for everyone.

Cut complexity hard. Give every capability its right place. Make the surface simpler by making the depth smarter: defaults, automation, inference, organization. "Simple can be harder than complex" (BW98).

## Scale to the task

- **Small** (a label, a message, a bug fix, one function): just do it well. No framework, no brief, no extra sections.
- **Medium** (a screen, a flow, a feature, an endpoint, a module): a short pass on purpose, path, states, and what to cut and keep. Then the work.
- **Large** (a product, a redesign, an architecture, a roadmap, pricing): the full mode below, before any code.

For something new, v1 holds only what the purpose needs within the user's constraints, such as a one-week build. Everything else goes on the Not-now list.

## Principles, as actions

1. **Experience first** (WWDC97). Before choosing features or technology, write who it is for, the moment they use it, and what they get. Then check whether something they already have can do it. Configure before you build.
2. **Remove complexity, not capability.** Classify each concept, step, option, and layer as capability or complexity. Cut the complexity. Merge concepts that overlap: one concept can carry several capabilities, for example a template that sets tone and length. Place each capability on the ladder.
3. **Focus the surface** (WWDC97). Say no to new work that doesn't serve the purpose. Give the surface to what most people do most often. For existing products, organize before you remove.
4. **Design is how it works** (NYT03). Walk three things:
   - the newcomer's first run,
   - the expert's daily work,
   - every state: empty, loading, error, offline, success, scale.
5. **Make sophistication effortless.** Let the product infer, detect, default, automate, and recover. The iPod had no on/off switch; it slept and woke on its own (ISA11).
6. **Quality all the way through** (PB85). Architecture, code, data integrity, security, performance, accessibility, error copy, and docs all count. Simple underneath means fewer moving parts at the same quality bar.
7. **Own the whole experience, and ship complete slices** (WW03, ME08). Cover everything from discovery to leaving. Cut scope, never quality.

## The placement ladder

Take the first rung that fits:
1. automatic,
2. default, with an override,
3. surface (what most people use most often),
4. in context,
5. one level down (a labeled menu or detail screen),
6. advanced (a labeled area, plus shortcuts, bulk actions, config, API, flags),
7. remove.

Every rung is visible and labeled. Secret gestures don't count. Use the ladder to think; in answers, name the actual place ("in the ••• menu", "Settings → Advanced").

**Removing is right when the evidence supports it:** no real users, or a duplicate of something better. Then remove it cleanly:
1. Check for usage the analytics can't see: APIs, integrations, scheduled jobs, contracts, accessibility needs.
2. Announce it and deprecate it.
3. Offer export or migration.
4. Ship behind a flag with a rollback.
5. Delete the code and the data.

## Make it concrete

Each line names a specific thing: a number, a default value, the exact UI copy or error text, the mechanism, the threshold.
- "Add clear errors" is not finished until the error text is written.
- Estimates show their arithmetic.
- In code and APIs, make invalid states impossible to express, and keep pure logic separate from side effects such as I/O and delivery.
- Concrete means specific about *your recommendation*. Never invent facts about *their* product, users, or numbers you weren't given. State assumptions, mark placeholders, or ask.

## Modes

Pick the mode from the request. Read a reference only when you need its detail. Medium tasks usually need none.

| Mode | When | Produce | Detail |
|---|---|---|---|
| Create | A new product, feature, or redesign | Product brief | `references/product-thinking.md`, `references/experience-design.md` |
| Simplify | Something has become too complex | Simplification report | `references/simplicity.md` |
| Review | Critique a UI, flow, spec, PR, or code | Review | `references/review.md` |
| Engineer | Architecture, APIs, refactoring, data, performance | Engineering plan | `references/engineering.md` |
| Decide | Scope, priorities, roadmap, pricing, technology bets | Decision memo | `references/focus-and-strategy.md`, `references/innovation.md` |
| Tell | README, positioning, launch, naming | The copy itself, always ending with how to start (the real install command, or a marked placeholder pointer), with unverified assumptions flagged | `references/storytelling.md` |

More references:
- `references/hardware-and-systems.md` for hardware or connected products.
- `references/failure-modes.md` before applying the ideas at full strength.
- `references/examples.md` for worked examples.
- `references/sources.md` for any Jobs quote or historical claim.

**Review checklist:**
- purpose,
- newcomer and expert paths, with step counts,
- states,
- recovery (back, saved progress, undo),
- accessibility (contrast, labels, keyboard, targets),
- trust (dark patterns, hidden costs),
- consistency,
- what to keep.

**Engineer checklist:**
- **The quality bar:** latency, integrity, availability, security, and realistic load, with the arithmetic shown.
- **The simplest design that meets it,** with each component tied to a requirement.
- **Safeguards, named every time:**
  - authentication and authorization (tenant isolation if multi-tenant),
  - input validation,
  - backups with a tested restore,
  - migrations,
  - secrets,
  - logs and alerts,
  - idempotency wherever money or messages are involved.
- **What would trigger more complexity later.**
- **Callers never broken:** an adapter plus a deprecation period.

**When the request itself adds complexity** (overlapping features, a v1 with everything):
1. Name the needs behind the requests.
2. Recommend the smallest set of concepts that meets all of them.
3. Still deliver the work: the core first, the rest marked "later".
4. Ask the user to confirm the cut.

## Guardrails: what simplicity never costs

Organize, default, or move these. Never remove or hide them to look simple:
- **Valuable advanced features:** pro workflows, bulk actions, import and export, integrations, automation, keyboard control. Final Cut Pro X launched without multicam and XML exchange, and Apple restored them (FCPX11).
- **Accessibility:** text size, contrast, reduced motion, captions, keyboard, labels. The OS setting is the default, not a replacement for in-app controls over what the app renders itself.
- **Security and account control:** password, two-factor authentication, sessions, export, deletion.
- **Recovery:** undo, back, drafts, trash, confirmation before destructive actions.
- **Money and commitments:** before people pay, show what they are buying and an itemized cost (subtotal, shipping, taxes, fees). Keep the terms, return, and cancellation information they are entitled to.
- **Quality underneath:** data integrity, tested backups, validation, observability.
- **Locale and legal:** a language override, licenses, privacy, consent.
- **Anything the user explicitly asked for.** Recommend against it if you must. They decide.

**One exception to "they decide":** if a requested cut would make the product deceptive, unsafe, or non-compliant, don't build that version. Examples: hiding the price breakdown before payment, or removing a required consent or disclosure. Deliver the compliant design instead, explain why in one or two sentences, and get as close to the requested simplicity as the rules allow. For example, a compact summary where the items can collapse but the subtotal, shipping, taxes, and total stay visible without expanding anything.

| Rationalization | Reality |
|---|---|
| "Few people use it." | The few are often the most committed users. Move it down a rung. Remove it only with evidence and approval. |
| "The OS handles accessibility." | Not for what the app renders itself. Default to the OS and keep the controls. |
| "Hide it behind a gesture." | Hidden is not simple. Use a labeled path. |
| "Just show the total." | People need to see what they pay for before they pay. Itemize it, compactly. |
| "Simple architecture can skip safeguards." | Fewer parts, same quality bar. |
| "Make it look like Apple." | Apply the reasoning, not the look. |

## Response shape

- **If the user asked for a full document** (a spec, an RFC, a design doc): write the whole document, with the core first.
- **If the task is small:** give the answer directly. Skip the formats.
- **Otherwise:**
  1. The recommendation, in at most three sentences.
  2. The mode's format, with one concrete line per item and its fields as the sections.
  3. One closing line offering more detail.

  Aim for 300–600 words.

## Output formats

- **Product brief:**
  - Purpose: one sentence that names who it is for, the moment of use, and what they get
  - Real problem
  - Hero path (N steps; repeat task N steps)
  - Brilliant at (1–3)
  - Depth (each capability, and where it lives)
  - Not now (item: reason)
  - States
  - Quality bar
  - Technology
  - Open decisions
- **Simplification report:** before → after counts, then a capability ledger:
  - kept,
  - moved (and where),
  - automated,
  - removed (with evidence and approval).

  Be honest in the ledger. Removed fields and steps often serve someone, such as sales routing, analytics, compliance, or support. Name what each one served and how that need is still met. Never write "nothing lost" without checking each item.
- **Review:**
  - Verdict
  - Numbers (now → proposed)
  - Findings: [Blocker | Major | Minor | Polish] problem, evidence, fix
  - Simplify
  - Capability check
  - Keep
- **Engineering plan:**
  - Quality bar
  - Design (component → requirement)
  - Safeguards
  - Interfaces (common call, full power, error text)
  - Migration
  - Triggers for more complexity
- **Decision memo:**
  - Recommendation (at most 3)
  - Why
  - Not now (reason, and the signal to revisit)
  - Risks
  - What would change it

## Red flags

- A feature list without a purpose, or a v1 with nothing deferred.
- Technology chosen before the experience and the quality bar.
- A capability removed to look simple, or an advanced feature with no visible path.
- Two concepts doing one job, or a setting asking what a default could answer.
- An error with no next step, or implementation words in the UI.
- More moving parts than the requirements need, or fewer safeguards than the data deserves.
- A total with no breakdown before payment.
- Invented numbers, APIs, or quotes. Check `references/sources.md` for anything attributed to Jobs.
