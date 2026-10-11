# Simplicity: remove complexity, keep capability

"Simple can be harder than complex: You have to work hard to get your thinking clean to make it simple" (BW98). Simplicity is what a product feels like when someone has done the hard work of understanding it well enough to organize everything it can do.
- It is not a visual style.
- It is not a smaller feature list.

Isaacson quotes Jony Ive on the same point: to be truly simple, you have to go really deep (ISA11).

The test of a simplification is two numbers moving in opposite directions:
- **Complexity goes down:** concepts, decisions, steps, options, layers, special cases.
- **Capability stays the same:** everything people rely on still works and can still be found.

## Complexity vs. capability

| Complexity: remove it | Capability: keep it, and place it well |
|---|---|
| Two concepts that do one job | Each distinct job people need done |
| A question the product could answer itself | The override for when its answer is wrong |
| Steps that exist because of how it was built | Steps that protect data, money, or safety |
| Words that expose the implementation | Precise terms experts rely on, in expert areas |
| Inconsistent names, places, and behaviors | Variety that reflects real differences |
| Options nobody changes | Options a real group changes for real reasons |
| Layers, services, and abstractions no requirement needs | The safeguards the data and users deserve |
| Dead code, stale flags, duplicate paths | Every behavior with a caller or a user |

## Where complexity lives

Simplify from the top of this list down. Shrinking the surface while leaving the concepts untouched only hides complexity.

| Layer | What to count | Example of excess |
|---|---|---|
| **Concepts** | Things the user must understand: objects, modes, terms, rules | Spaces, projects, boards, and lists all group tasks |
| **Decisions** | Choices the user must make to proceed | Choosing a template before seeing an empty document |
| **Steps** | Actions to finish the hero task | Ten form fields before first value |
| **Surface** | Screens, settings, buttons, options | 40 settings, 15 notification toggles, all on one level |
| **Variants** | Plans, editions, configurations, platforms | Five editions that each differ by one feature |
| **Exceptions** | Special cases users must remember | "Works everywhere except shared folders" |
| **Machinery** | Services, layers, dependencies, code paths | Three services and a queue for a form with ten users a day |

## The procedure

1. **Inventory both lists:**
   - the complexity (concepts, decisions, steps, options, layers, exceptions),
   - the capabilities (every job the product does, including advanced ones).
   Count both.
2. **Gather evidence for each capability.** Who uses it, how often, what breaks without it, and what they would do instead. Usage data and support tickets beat guesses. If there is no data, say so.
3. **Classify each item:**
   - **Essential:** the core job fails without it.
   - **Valuable:** an advanced, occasional, or expert capability with a real purpose.
   - **Accidental:** exists only because of how the product was built or how it grew.
   - **Ornamental:** decoration with no job.
4. **Place every capability on the ladder** (below). Remove only accidental and ornamental items, and features with no users.
5. **Check the guardrails** in SKILL.md: valuable advanced features, accessibility, security, recovery, quality underneath, locale and legal, anything the user asked for.
6. **Recount and report.** Show before and after counts, plus the capability ledger.
7. **Walk two paths again.**
   - The newcomer's hero path must be shorter.
   - The expert's frequent path must be at least as fast: shortcuts, bulk actions, saved setups, the API.

## The placement ladder in detail

| Rung | Use it when | Examples |
|---|---|---|
| 1. Automatic | The right action is knowable and safe to take | Autosave. Detect file encoding. Sleep and wake: Isaacson reports the iPod had no on/off switch (ISA11). Clean up played episodes |
| 2. Default | Most people want the same value, but some need another | Theme follows the system. Locale from the device. Sensible retry and timeout values |
| 3. Surface | Most people need it most of the time | The primary action. The core content. The one status that matters |
| 4. In context | It matters only in certain moments | "Skip intro" during the intro. A "Retry" next to a failed upload. Cast when a device is found |
| 5. One level down | Some people need it some of the time | Secondary settings. A "More" menu. A details panel. Per-item options on the item's page |
| 6. Advanced | Experts need it, and need it to be fast | Keyboard shortcuts, bulk edit, custom rules, scripting and API, raw config, developer options, pro panels |
| 7. Remove | It is accidental complexity, ornamental, or has no users | A duplicate concept. An option nobody changes. A dead flag. Report each, with evidence, for approval |

The ladder has rules:
- **Every rung must be reachable and labeled.** "One level down" and "Advanced" are visible places with clear names. They are never secret gestures, unlabeled icons, or easter eggs.
- **Experts shouldn't pay a speed tax.** If a capability moves down for newcomers, give experts a faster path: a shortcut, a pinned tool, a remembered workspace, a command palette, or an API.
- **Moving is reversible, removing is not.** When unsure between rung 6 and rung 7, choose 6 and measure.

## One good way, and when two are justified

Kocienda recounts showing Jobs an iPad keyboard demo with two input modes. Jobs concluded they didn't need both, and one was kept (KOC18).
- Extra modes multiply testing, documentation, support, and the user's uncertainty.
- Keep one excellent way for each job.
- Keep a second way only when distinct groups truly need different things, for example a guided mode for newcomers and a direct mode for professionals. Make the relationship between the two clear.

## Let the product carry the complexity

Some complexity is inherent to the problem. Larry Tesler, who worked at Xerox PARC and later Apple, described this as the conservation of complexity. The design choice is *who* absorbs it.

Prefer the product:
- infer instead of asking,
- detect instead of configuring,
- recover instead of erroring,
- explain at the moment of need instead of in a manual.

That is how sophisticated technology comes to feel effortless.

## Professional and expert tools

Expert tools (video and audio editing, design, analytics, IDEs, admin consoles, trading) are where careless simplification does the most damage:
- In 2011, Apple's Final Cut Pro X launched without multicam editing, XML exchange, and tape workflows that professionals relied on. Apple restored them in later updates, and for a time resumed selling the previous version (FCPX11).
- iMovie '08 dropped the classic timeline and most effects. Apple offered the previous iMovie as a free download (IMOVIE07).

For expert tools:
- **Simplify the learning path,** not the power: templates, guided first runs, smart defaults, contextual help.
- **Keep dense views available.** Density is a feature for experts. Offer a calmer default layout if newcomers need one, and let experts switch.
- **Preserve interchange:** import and export formats, project compatibility, automation hooks. Professionals live in pipelines.
- **Never remove a professional workflow without a migration path,** and say what is changing before it ships.

## Settings screens

1. **Group by user intent:**
   - Account
   - Privacy & Security
   - Notifications
   - Appearance & Accessibility
   - Language & Region
   - Data (export, delete)
   - Advanced
   - About
2. **Follow the OS by default and allow an override:** theme, language, text size, reduced motion, contrast.
3. **Collapse long lists of toggles into a few meaningful groups,** with per-item control one level down.
4. **Move things that aren't settings to where they belong:**
   - per-item options to the item's page,
   - reference material (keyboard shortcuts) to Help,
   - one-time tips to contextual hints.
5. **Put destructive actions last.** Label them plainly and confirm them.
6. **Keep developer and beta options in a labeled Advanced section.**

## When not to simplify

- **Safety-critical steps:** confirmations, warnings, irreversible actions.
- **Regulated disclosures and consents.**
- **Established conventions people rely on.** A "simpler" pattern that breaks the platform's standard behavior is not simpler for its users.
- **When you lack evidence about who uses a capability.** Move it, measure, then decide.

## Report the change

| | Before | After |
|---|---|---|
| Concepts to learn | 7 | 3 |
| Steps to first value | 9 | 3 |
| Top-level settings | 40 | 8 groups |

Capability ledger:
- **Kept on the surface:** 6
- **Moved:** 11 (8 one level down, 3 to Advanced, each listed with its new location)
- **Automated:** 2
- **Removed:** 1. A duplicate "Projects" view, merged into "Spaces". Approved by the user.
- **Capabilities lost:** 0
