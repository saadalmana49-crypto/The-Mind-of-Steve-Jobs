# Insanely Great

**An Agent Skill inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design.**

Insanely Great helps AI coding agents build technology products that are powerful and complete underneath, and simple, clear, and effortless for the people who use them. It works for software, apps, platforms, APIs, developer tools, digital services, and hardware. It runs in Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, Windsurf, Devin, Cline, and other agents that read the open [Agent Skills](https://agentskills.io) format.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-black.svg)](https://agentskills.io/specification) ![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

## Why it exists

AI agents are good at adding things. Ask one to plan a product and it lists every feature. Ask it to simplify and it often deletes what people need.

In our baseline tests, a strong model asked to make a settings screen "minimal like Apple":
- removed the in-app text size, reduced motion, and high-contrast controls,
- removed the language override,
- hid developer options behind tapping the version number.

Insanely Great gives the agent a different default: **remove complexity, keep capability.**

## The idea

Steve Jobs put it this way in 1998: "Simple can be harder than complex: You have to work hard to get your thinking clean to make it simple." The skill turns that into working steps.

Every product has two layers:
- **The surface:** what most people do most often. Make it obvious and fast.
- **The depth:** everything else the product can do. Keep it complete and reachable.

The surface gets simpler when the depth gets smarter (defaults, automation, inference, clear organization), not when capabilities are deleted.

The skill gives the agent:
- **Seven principles,** each tied to an action. Start from the experience and work backwards to the technology. Remove complexity, not capability. Focus the surface, keep the depth. Design is how it works, for newcomers and experts. Make sophisticated technology feel effortless. Carry quality all the way through. Own the whole experience, and ship it whole.
- **A placement ladder** for every capability: automatic, default, surface, in context, one level down, advanced, and removal only as the last rung, with evidence and your approval.
- **Six modes,** each with its own output format: Create (a product brief), Simplify (a report with a capability ledger), Review (ranked findings), Engineer (architecture, APIs, refactoring), Decide (a decision memo), Tell (positioning and launch copy).
- **Guardrails.** Advanced features, accessibility, security, recovery, and engineering quality are never removed to make something look simple.

## Inspired by Steve Jobs, built for your product

The principles come from what Jobs said and did:
- the 1983 Aspen design talk,
- WWDC 1997,
- *BusinessWeek* in 1998,
- the iPod and iPhone launches,
- "Thoughts on Flash",
- first-hand accounts from people who worked with him: Andy Hertzfeld, Ken Kocienda, and Walter Isaacson's authorized biography.

Every quote in the skill was checked against a transcript or original and is cited with its source. Common misattributions are flagged, including "Simplicity is the ultimate sophistication", which was a 1977 Apple brochure line. See [`references/sources.md`](skills/insanely-great/references/sources.md).

It is not an Apple style guide, and it doesn't ask the agent to imitate Jobs. It applies the reasoning to your users, your platform's conventions, and your brand. It also documents where the approach failed, for example the G4 Cube, MobileMe, and Final Cut Pro X's launch without the professional features its users needed, so the agent learns the limits too.

The name comes from Jobs' own phrase for the standard the Macintosh team aimed for, which Steven Levy used as the title of his 1994 history of the Mac.

## Install

The quickest way, for most agents:

```bash
npx skills add saadalmana49-crypto/insanely-great
```

This uses Vercel's [skills CLI](https://github.com/vercel-labs/skills). It installs to `~/.agents/skills/` (read by Codex, Gemini CLI, Cursor, and others) and links it for Claude Code. Add `-g` for a global install, or `-a <agent>` to choose agents.

| Agent | Install |
|---|---|
| Claude Code | `/plugin marketplace add saadalmana49-crypto/insanely-great`, then `/plugin install insanely-great@insanely-great` |
| Codex | Ask `$skill-installer` to install `https://github.com/saadalmana49-crypto/insanely-great/tree/main/skills/insanely-great`, or copy the folder into `~/.agents/skills/` |
| Gemini CLI | `gemini skills install https://github.com/saadalmana49-crypto/insanely-great.git --path skills/insanely-great` |
| Cursor, Copilot, Windsurf / Devin Desktop | Copy or symlink the folder into `~/.agents/skills/`, or into the project's `.agents/skills/` |
| Devin (cloud) | Commit the folder to `.agents/skills/insanely-great/` in a connected repository |
| Cline | Copy the folder into `~/.cline/skills/` or the project's `.cline/skills/` |

To keep one copy that updates with `git pull`:

```bash
git clone https://github.com/saadalmana49-crypto/insanely-great.git ~/insanely-great
mkdir -p ~/.agents/skills ~/.claude/skills
ln -s ~/insanely-great/skills/insanely-great ~/.agents/skills/insanely-great
ln -s ~/insanely-great/skills/insanely-great ~/.claude/skills/insanely-great
```

For paths, versions, and exactly what we tested, see [docs/compatibility.md](docs/compatibility.md).

## Use

Agents load the skill on their own when a task fits: planning a product, scoping a feature, reviewing a flow, simplifying settings, designing an API or architecture, or writing launch copy. To call it directly, use `/insanely-great` in Claude Code, Cursor, or Cline, `$insanely-great` in Codex, `@insanely-great` in Windsurf, or `@skills:insanely-great` in Devin. Some prompts that work well:

```text
/insanely-great plan a habit-tracking app for night-shift nurses
/insanely-great review this onboarding flow (paste screens or a URL)
Simplify our admin dashboard without losing anything our power users rely on.
Design the architecture for our 3-person team's booking platform.
Which of these 9 roadmap items should we do next quarter?
```

## What's inside

```
skills/insanely-great/
├── SKILL.md                    principles, ladder, modes, guardrails, formats (~4.4k tokens)
└── references/                 loaded only when a task needs them
    ├── product-thinking.md     ├── review.md              ├── storytelling.md
    ├── simplicity.md           ├── focus-and-strategy.md  ├── failure-modes.md
    ├── engineering.md          ├── innovation.md          ├── examples.md
    ├── experience-design.md    ├── hardware-and-systems.md└── sources.md
```

The skill is Markdown only. It has no scripts and needs no network access. Its always-on cost is the name and description, about 190 tokens.

## Evaluation

[`evals/`](evals/) holds 14 realistic scenarios. Each was run in Claude Code (model `sonnet`) with and without the skill, 3 reps each, and graded blind by a separate judge (`opus`) against checks written in advance.

| | Without the skill | With the skill |
|---|---|---|
| Checklist items passed | 146 / 192 (76%) | 187 / 192 (97%) |
| Blind pairwise preference | 6 wins | 36 wins |

The biggest differences were:
- keeping accessibility and advanced options when asked for "minimal like Apple",
- giving product plans a purpose, a hero path, and designed states,
- not fabricating Jobs quotes.

The weak spots are just as real:
- Answers with the skill ran about 10% longer.
- The skill activated on its own in only 1 of 3 architecture prompts. Use `/insanely-great` there.
- On several scenarios, the base model was already strong.

All of it is in [evals/results.md](evals/results.md), with every transcript in [evals/runs/](evals/runs/) and the limitations (small samples, a model judging a model, one agent) in [evals/README.md](evals/README.md).

## Updating and versioning

- **Plugin:** `/plugin marketplace update insanely-great`
- **skills CLI:** `npx skills update`
- **Symlinked clone:** `git pull`
- **Gemini CLI:** reinstall with the same command.

Versions follow Semantic Versioning, adapted for instructions. See [CONTRIBUTING.md](CONTRIBUTING.md#versioning) and [CHANGELOG.md](CHANGELOG.md).

## Contributing

Source corrections, behavior reports, and compatibility reports are the most useful contributions. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and disclaimer

MIT. See [LICENSE](LICENSE).

Insanely Great is an independent project. It is not affiliated with or endorsed by Apple Inc. or the estate of Steve Jobs. Apple, Macintosh, iPod, iPhone, iPad, and Final Cut Pro are trademarks of Apple Inc. Quotations are short excerpts used for commentary and attributed to their sources.
