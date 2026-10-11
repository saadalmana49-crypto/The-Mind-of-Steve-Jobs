# Failure modes: where the approach went wrong, and how imitators misuse it

Read this before applying the principles at full strength. Jobs' record includes clear failures, and many imitators copy his style instead of his reasoning. Both teach as much as the successes.

## Historical cases

Each case: what happened → the lesson → the guardrail it supports.

1. **Power Mac G4 Cube (2000–2001).** A striking, compact, nearly silent computer. Apple suspended it after a year, saying most customers bought the Power Mac G4 tower instead (CUBE01).
   → Design must fit the real buyer's job and price. Beauty does not override expandability or value for the people buying.
   → *Guardrail:* validate the design against what the target customer actually needs.

2. **The 1984 Macintosh keyboard with no arrow keys.** The arrow keys were left out on purpose, to push users and developers toward the mouse. Later Mac keyboards restored them.
   → Forcing a new paradigm by removing the familiar path has real costs, especially for people who rely on the keyboard.
   → *Guardrail:* keep escape hatches. Never remove an accessibility path to force behavior.

3. **The 1998 iMac's round mouse.** Visually consistent with the iMac, but widely criticized as hard to orient and hold. Replaced in 2000.
   → Visual unity cannot come at the expense of ergonomics.
   → *Guardrail:* test physical and interactive design in real use, with real hands.

4. **NeXT Computer (1988).** Exquisitely built and priced far beyond much of its market. NeXT left hardware in 1993. Its software survived and became the base of Mac OS X.
   → Perfectionism has to serve the customer's job and budget. Separate the lasting idea (the software) from the unsustainable package.
   → *Guardrail:* quality bar ≠ cost-is-no-object.

5. **MobileMe (2008).** Launched alongside the iPhone 3G, iPhone 2.0 software, and the App Store. Jobs' own email said it "was simply not up to Apple's standards", that it should have launched piece by piece, and that launching it all together was a mistake (ME08). Lashinsky reports his question to the team: what is MobileMe supposed to do (LAS11)?
   → Ship less rather than ship broken. Don't stack big launches.
   → *Guardrail:* never ship the part that isn't ready.

6. **iPhone 4 antenna (2010).** The exterior band was the antenna, and some grips reduced signal. Apple gave every owner a free case (AG10).
   → Industrial design that touches function must be tested in realistic use. When you're wrong, fix it for users.
   → *Guardrail:* validate form against function. Own mistakes plainly.

7. **Third-party iPhone apps (2007).** In June, Apple pitched web apps as the "sweet solution" (WWDC07). In October, Jobs announced a native SDK (SDK07). The App Store that followed became central to the iPhone.
   → A strong initial position can be wrong. Reversing it quickly was the right call.
   → *Guardrail:* state what evidence would change the decision, and act on it.

8. **Music subscriptions (2003).** Jobs told *Rolling Stone* that subscription services had failed and that people did not want to rent their music (RS03). The market later moved heavily to streaming, and Apple launched its own subscription service in 2015.
   → Confident predictions about user behavior are hypotheses with a shelf life.
   → *Guardrail:* revisit core assumptions as conditions change.

9. **Final Cut Pro X (2011).** Apple rebuilt its professional video editor from scratch. It launched without multicam editing, XML exchange with other tools, and tape workflows that professionals depended on, and the previous version was pulled from sale. Apple restored XML in September 2011 and multicam in January 2012, and for a time sold the previous version again (FCPX11).
   → A cleaner, more modern product still fails its users if it drops the workflows they depend on.
   → *Guardrail:* remove complexity, not capability. Keep professional workflows, interchange formats, and a migration path.

10. **iMovie '08 (2007).** A simpler redesign dropped the classic timeline, most effects, and plug-ins. Apple offered the previous version as a free download (IMOVIE07).
    → Even consumer users notice when depth disappears.
    → *Guardrail:* simplify the surface. Keep the depth reachable, or keep the old path available until the new one covers it.

11. **Management style.** Isaacson and others document harshness toward colleagues (ISA11).
   → This is not part of the method, and nothing in it depends on it.
   → *Guardrail:* direct about the work, respectful to people.

## How imitators misuse the ideas

| Misuse | What it looks like | Do instead |
|---|---|---|
| **Minimalism as removal** | Cutting features people need so the screen looks clean | Simplify concepts and decisions. Keep needed function reachable and labeled |
| **Dumbing down** | Turning a capable product into a basic one. Expert workflows, formats, and integrations disappear | Keep the depth. Move it down the ladder, and give experts fast paths |
| **Burying the depth** | Advanced features exist but nobody can find them: no labels, no search, many clicks | Visible, labeled entry points. A command palette or search. Shortcuts |
| **Simple architecture by skipping safeguards** | "We kept it simple" means no backups, auth checks, or monitoring | Fewer moving parts at the same quality bar (engineering.md) |
| **Looks over function** | Light-gray text on white, tiny targets, icon-only controls, no visible affordances | Meet contrast and target-size requirements. Label icons. Make controls look like controls |
| **Secret UI** | Hidden gestures, long-press menus, easter-egg settings | A visible, labeled "More" or "Advanced" area |
| **Removing without a migration path** | Dropping a port, format, or API with no adapter, export, or overlap period | Announce early, provide the bridge, then remove |
| **"Users don't know what they want"** | Ignoring evidence, support tickets, and usability problems | Prototype, show it, observe behavior, then decide |
| **Reality distortion** | Overpromising dates, capabilities, or performance | Commit only to what you can show. State the conditions |
| **Perfectionism without shipping** | Endless polish, launch slips with no end | Fixed date, flexible scope. Ship the ready subset |
| **Taste as a veto** | "I don't like it" with no reason | Say what the design gets wrong, and offer an alternative |
| **Copying Apple's look** | Imitating aesthetics, slogans, and keynote theatrics, or applying iOS patterns to every platform | Copy the reasoning: purpose, focus, the whole experience, details. Follow your own platform's conventions and your own identity |
| **One person decides everything** | A bottleneck; experts overruled without reasons | One owner per decision, informed by the people closest to the work |
| **Harshness** | Belittling people as "high standards" | Hold a high bar for the work and treat the people with respect |

## Before going all in

- [ ] Is the cut serving users, or only the look?
- [ ] Did any capability people rely on get removed, especially an expert workflow, an export format, or an integration?
- [ ] Did any accessibility, security, recovery, or legal function get removed?
- [ ] Is there evidence for the bold call, or only conviction? What would change it?
- [ ] Does the design fit the actual buyer's job, budget, and context?
- [ ] Is the scope small enough to ship at high quality on the planned date?
- [ ] Has it been tested in real use, not only reviewed in mockups?
