---
name: insanely-great
description: Practical product judgment inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design: remove complexity, keep capability. For technology products of every kind (software, apps, platforms, APIs, developer tools, digital services, hardware). Use when planning a product or feature; choosing scope, priorities, or a roadmap; proposing a system architecture, backend, tech stack, or data model; designing or refactoring APIs, SDKs, CLIs, or workflows; reviewing UX, UI, flows, or code for unnecessary complexity; organizing features and settings; simplifying anything without losing capability; improving performance or maintainability; designing hardware or connected products; or writing positioning, README, or launch copy. Also use when asked to make something simpler, more focused, more polished, "like Apple" or "like Steve Jobs", or when quoting Jobs. Not for routine bug fixes or mechanical edits.
license: MIT
metadata:
  version: "1.0.0"
  source: "https://github.com/saadalmana49-crypto/insanely-great"
---

# Insanely Great

A working method for building technology products that are **complete and powerful underneath, and simple, clear, and effortless on the surface**. It is inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design, as documented in his interviews, keynotes, and writing (see `references/sources.md`).

It applies to any technology product: an API, a CLI, a SaaS platform, a mobile app, a data pipeline, an internal tool, a connected device.

**It is a lens, not a persona and not an Apple style guide:**
- Apply the reasoning to your users, your platform's conventions, and your product's identity.
- Never imitate Jobs' voice or harshness, or Apple's look.
- The user owns the product. You recommend, they decide. Never drop something they asked for without saying so.

## The core idea: remove complexity, keep capability

- **Complexity** is whatever makes a product harder to understand, use, build, or change than it needs to be:
  - redundant concepts,
  - unnecessary decisions and steps,
  - implementation details leaking into the experience,
  - inconsistency,
  - needless layers, options, and code,
  - slow paths.
- **Capability** is what the product lets people do:
  - essential functions,
  - valuable advanced features,
  - expert speed,
  - integrations and export,
  - reliability, security, and access for everyone.

Radical simplicity means removing complexity relentlessly while keeping capability intact. Every product has two layers:
- **The surface:** what most people see and do most often. Make it obvious, calm, and fast.
- **The depth:** everything else the product can do. Keep it complete, reliable, and reachable when it is needed.

Make the surface simpler by making the depth smarter (defaults, automation, inference, clear organization), never by deleting the depth. A "simplification" that removes a capability people rely on is a regression. *"Simple can be harder than complex"* (BW98).

## Scale the method to the decision

| Size | Examples | What to do |
|---|---|---|
| Small | A label, one button, an error message, a function signature | Apply the principles silently. Mention them only if it changes the answer. |
| Medium | A screen, a flow, a feature, an endpoint, a module, a CLI command | Short pass: purpose, hero path, states, what to cut and what to keep. Then the work. |
| Large | A new product, a major feature, a redesign, an architecture, a roadmap | Use the full mode below. Produce its output before writing code. |

## Seven principles, each with the action it requires

1. **Start from the experience, work backwards to the technology** (WWDC97). Before choosing features, architecture, or a stack, write one sentence: who it is for, the moment they use it, and what they get. Every later choice must serve it.
2. **Remove complexity, not capability.** For each concept, step, option, setting, layer, or module, ask: is this capability someone needs, or complexity we created? Cut the complexity. Find the right place for every capability (see the placement ladder). Never report a simplification without a capability check.
3. **Focus the surface, keep the depth.**
   - "Focusing is about saying no" (WWDC97). Say no to new work that doesn't serve the purpose, and give the surface to the few things most people do most often.
   - When simplifying something that already exists, organize before you remove. Valuable advanced features move to the right depth; they don't disappear.
4. **Design is how it works, for everyone who uses it** (NYT03). Walk the real paths: the newcomer's first run, the expert's daily work, and every state (empty, loading, error, offline, success, scale). A screenshot or a diagram is not the design.
5. **Make sophisticated technology feel effortless.**
   - Let the product carry the complexity: infer, detect, default, automate, recover.
   - The iPod had no on/off switch. It slept and woke on its own (ISA11). The iPhone hid advanced multi-touch technology behind direct manipulation with your fingers (IPH07).
6. **Carry quality all the way through** (PB85). The parts nobody sees are the product too:
   - architecture, code, data integrity, security,
   - performance, error handling, accessibility, observability, docs.
   - Simple underneath means fewer moving parts at the same quality bar, not a lower bar.
7. **Own the whole experience, and ship it whole** (WW03).
   - Everything the user touches is the product: discovery, setup, daily use, failure and recovery, billing, support, export, leaving.
   - Ship in complete slices. Cut scope, never quality (FL-SHIP, ME08).

## The placement ladder: where each capability belongs

Take the first rung that fits. Remove a capability only at the last rung.

1. **Automatic:** the product does it without asking (save, sync, detect format, sleep and wake).
2. **Default:** decided for the user, with an easy override (theme follows the system, sensible timeouts).
3. **Surface:** visible on the hero path. Only for what most people need most often.
4. **In context:** appears when relevant (a cast button when a device is found, a fix-it action next to an error).
5. **One level down:** a labeled menu, a "More" control, a detail screen, a secondary tab.
6. **Advanced:** a clearly labeled area for experts, plus shortcuts, bulk actions, config files, API parameters, CLI flags.
7. **Remove:** only accidental complexity, or a feature with no real users or purpose. Show the evidence, list it, and get the user's agreement.

The ladder is your working tool. In answers, describe placement in the user's terms ("in the ••• menu", "Settings → Advanced"), not by rung number.

Never use rung 5 or 6 as a hiding place. Every capability must be discoverable through a visible, labeled path. Secret gestures and easter eggs don't count.

## Simplicity across the whole product

| Layer | Simplify | Keep intact |
|---|---|---|
| Strategy | One purpose, at most three priorities, a Not-now list | The capabilities that make the product worth choosing |
| Architecture | The fewest moving parts that meet the quality bar. One source of truth. Proven technology | Data integrity, security, backups, observability, the headroom you actually need |
| Implementation | Clear modules, one way to do each thing, no dead code, flags, or speculative options | Tests on critical paths, error handling, readable code |
| APIs, CLIs, SDKs | Few concepts, safe defaults, one obvious path | Full power through optional parameters, flags, config, escape hatches |
| Workflows and UX | The fewest steps and decisions on the hero path. Defaults. Inline guidance | Expert speed: shortcuts, bulk actions, automation, saved setups |
| Interface | One primary action per screen, clear hierarchy, consistent words | Every function reachable and labeled |
| Performance | A fast hero path with explicit budgets | Correctness under load and on slow networks |
| Maintainability | Fewer special cases, consistent patterns, small dependencies | Docs and tests that let others change it safely |
| Journey | One coherent product from discovery to leaving | Export, recovery, support, accessibility |

## Modes

Pick the mode from the request. Load a reference file only when its mode is in play.

### Create: a new product, feature, or redesign
1. **Purpose.** One sentence a non-expert understands. If you can't write it, ask before designing.
2. **Real problem.** Separate the requested solution from the underlying need.
3. **Hero path.** Count the steps from arrival to first value, and for the most frequent repeat task.
4. **Brilliant at.** One to three things it must do better than anything else.
5. **Depth.** The capabilities that stay beneath the surface, and the rung where each one lives.
6. **Not now.** New work you are not building yet, each with a reason.
7. **States and quality bar.** First run, empty, loading, error, success, scale. The details that make it feel finished.
8. **Then choose the technology** that delivers this most simply at the quality bar.

Output: the **Product brief** below. Load `references/product-thinking.md` and `references/experience-design.md`.

### Simplify: something has become too complex
1. **Inventory** both the complexity (concepts, decisions, steps, options, layers) and the capabilities.
2. **Classify** every item. Place each capability on the ladder. Remove only accidental complexity.
3. **Check the guardrails.** Recount, and report before and after, with a capability ledger: kept, moved, automated, removed (with the user's approval).

Load `references/simplicity.md`.

### Review: critique a UI, flow, spec, PR, codebase, or product
1. State what it is supposed to do.
2. Walk the newcomer and expert paths, counting steps and decisions.
3. Inventory the states.
4. Audit each element: complexity or capability?
5. Do a details pass.
6. Rank the findings, and say what to keep.

Output: the **Review** format below. Load `references/review.md`.

### Engineer: architecture, APIs, implementation, refactoring, performance
1. **Derive the quality bar from the experience:** latency, data integrity, availability, security, realistic scale.
2. **Choose the simplest design that meets it.** Map every component to a requirement, and write down what would trigger more complexity later.
3. **Name the safeguards explicitly, every time:**
   - authentication and authorization (tenant isolation if multi-tenant),
   - input validation,
   - backups with a tested restore,
   - migrations,
   - secrets,
   - logs and alerts on the hero path,
   - idempotency wherever money or messages are involved.
4. **Keep power available** through optional parameters and escape hatches. Refactor without breaking callers.

Load `references/engineering.md`.

### Decide: scope, priorities, roadmap, technology bets, differentiation
Keep at most three items and give every other item a reason. State what would change your mind. Load `references/focus-and-strategy.md`, and also `references/innovation.md` for differentiation.

### Tell: positioning, naming, README, landing page, launch, demo
Problem first, one concrete line, show it working, true claims only. Load `references/storytelling.md`.

### Hardware and connected products
Load `references/hardware-and-systems.md`.

## When the request itself adds complexity

Feature requests describe a need. They are not a spec. When a request would make the product worse (overlapping features, a v1 with everything, another endpoint family):
1. Name the underlying needs. Usually there are fewer needs than requests.
2. Recommend the smallest set of concepts that meets every need, keeping the capabilities. State the tradeoff in two or three sentences.
3. **Still deliver the work.** The recommended core goes first. Everything else goes in a marked "Not now / later" section, with what it would take to add.
4. Ask the user to confirm the cut before code is written.

## Guardrails: what simplicity never costs

Organize, default, or move these. Never remove or hide them to make something look simple:
- **Valuable advanced features.** Anything experts, professionals, admins, or developers rely on: pro workflows, bulk operations, import and export formats, integrations, automation, keyboard control. Apple's Final Cut Pro X (2011) launched without multicam, XML exchange, and tape support. Professionals objected, and Apple restored those features over later updates (FCPX11).
- **Accessibility:**
  - Text size, contrast, reduced motion, captions, keyboard access, screen-reader labels, target sizes.
  - Honoring the OS setting is the default. It does not replace the in-app control when the app renders its own text, motion, or media.
- **Security and account control:** password, two-factor authentication, sessions and devices, data export, account deletion.
- **Recovery:** undo, cancel, back, drafts, trash and restore, confirmation before anything destructive.
- **Quality underneath:** data integrity, backups that restore, input validation, observability, tests on critical paths.
- **Locale and legal:** a language override, licenses, privacy, consent.
- **Anything the user explicitly asked for.** Recommend against it if you must. The user decides.

| Rationalization | Reality |
|---|---|
| "Few people use the advanced feature, so cut it." | The few are often the most committed users: pros, admins, developers. Move it down a rung. Remove it only with evidence and the user's agreement. |
| "The OS handles accessibility." | Only partly. Custom-rendered text, motion, and media often ignore it. Honor the OS by default and keep the controls. |
| "Hide it behind a gesture or an easter egg." | Hidden is not simple. Use a visible, labeled "More" or "Advanced" path. |
| "A simple architecture can skip backups, tests, or monitoring." | Simple means fewer moving parts at the same quality bar. |
| "Make it look like Apple." | Apply the reasoning, not the look. Follow your platform's conventions and your own identity. |
| "Jobs ignored users and focus groups." | He rejected designing *by* focus group, not evidence. Prototype, show it, observe. |
| "Perfect is the standard, so wait." | Ship the smaller complete slice. Never ship the part that isn't ready. |

## Response shape

Clarity is part of the craft.
- **If the user asked for a full document** (a spec, an RFC, a design doc), write the whole document, with the recommended core first and deferred items last.
- **Otherwise,** the answer is exactly these parts, in order:
  1. **The recommendation or verdict,** in at most three sentences.
  2. **The mode's output format,** one line per item where possible. Its fields are the sections. Don't add other sections.
  3. **One closing line** offering the next layer of detail (full spec, per-screen detail, implementation notes).

  Aim for 300–600 words.

## Output formats

**Product brief** (Create). Every field is required:
```
Purpose:        <who, what moment, what they get>
Real problem:   <the need behind the request>
Hero path:      <numbered steps to first value> (N steps); repeat task (N steps)
Brilliant at:   <1–3 things>
Depth:          <capabilities beneath the surface → where each lives on the ladder>
Not now:        <item: reason>, ... (never empty)
States:         <first run / empty / loading / error / success>
Quality bar:    <specific details, performance budgets, reliability needs>
Technology:     <simplest design that meets the bar, and why>
Open decisions: <what the user must decide>
```

**Review** (Review):
```
Verdict:          <2–3 sentences: what it is for, whether it delivers>
Numbers:          <steps / fields / decisions before first value: now → proposed>
Findings:         [Blocker | Major | Minor | Polish] <problem>. Evidence: <where>. Fix: <change>
Simplify:         <complexity to remove or merge>
Capability check: <capabilities kept, moved (where), or at risk>
Keep:             <what works and should not be touched>
```

**Simplification report** (Simplify): before → after counts, then a capability ledger with four parts:
- kept on the surface,
- moved (to which rung),
- automated,
- removed (with evidence and approval).

The default for "removed" is zero.

**Decision memo** (Decide): Recommendation (at most three items) → why → Not now, with reasons → risks → what would change it.

## Red flags: stop and rethink

- A feature list with no purpose sentence, or a v1 with an empty Not-now list.
- Technology or architecture chosen before the experience and quality bar are described.
- A capability removed to make something *look* simple, or an advanced feature with no visible path.
- Two concepts doing one job ("spaces" and "projects" that differ only in name), or a setting asking what a default could answer.
- An error with a code but no next step. UI words that expose the implementation.
- An architecture with more moving parts than its requirements need, or fewer safeguards than its data deserves.
- A product tour explaining a confusing UI instead of fixing it.
- Copying Apple's look or slogans instead of applying the reasoning.
- A Jobs quote you can't find in `references/sources.md`.

## References (load on demand)

| File | Load when |
|---|---|
| `references/product-thinking.md` | Defining a product or feature, finding the real problem, writing a brief |
| `references/simplicity.md` | Reducing complexity anywhere while keeping capability: the full ladder, settings, pro tools |
| `references/engineering.md` | Architecture, APIs, SDKs, CLIs, implementation, refactoring, performance, maintainability |
| `references/experience-design.md` | Flows, states, newcomer and expert paths, interaction, copy, visual craft |
| `references/review.md` | Critiquing or auditing anything |
| `references/focus-and-strategy.md` | Priorities, roadmaps, scope, saying no, product lines, tiers |
| `references/innovation.md` | Differentiation, new categories, technology bets |
| `references/hardware-and-systems.md` | Physical and connected products, ecosystems, setup |
| `references/storytelling.md` | Positioning, naming, README, landing pages, launches, demos |
| `references/failure-modes.md` | Before applying these ideas at full strength. Shows where the approach failed historically and how imitators misuse it |
| `references/examples.md` | Worked before-and-after examples across product types |
| `references/sources.md` | Any Jobs quote or historical claim. Which sources are verified, and which quotes are misattributed |
