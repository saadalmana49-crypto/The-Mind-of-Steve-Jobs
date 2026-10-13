# Insanely Great

**Remove complexity, keep capability.** An Agent Skill inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-black.svg)](https://agentskills.io/specification) [![Version](https://img.shields.io/badge/version-1.1.0-green.svg)](CHANGELOG.md)

Insanely Great gives AI coding agents the product judgment to build things that are powerful underneath and easy to use on top. It works on any technology product:
- an API, a CLI, or a SaaS platform,
- a mobile app,
- an internal tool,
- a connected device.

It is plain Markdown in the open [Agent Skills](https://agentskills.io) format, so it runs in Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, Windsurf, Devin, Cline, and other agents that read `SKILL.md` folders.

## Why it exists

Coding agents tend to fail at product work in two opposite ways.

Ask one to plan a product and it lists every feature it can think of. Ask it to simplify and it starts deleting. In our baseline runs, a strong model asked to make a settings screen "minimal, like Apple would" removed in-app text size and contrast controls in two of three runs, and in every run left developer options without a labeled path. Asked for Steve Jobs quotes, it presented unverified lines as his exact words.

Insanely Great gives the agent a better default, and a method to go with it.

## Remove complexity, keep capability

Most products have two layers:
- **The surface** is what most people do most of the time. It should be obvious, calm, and fast.
- **The depth** is everything else the product can do: expert workflows, integrations, exports, admin tools, reliability, security, accessibility. It should be complete, and reachable when someone needs it.

The skill teaches agents to make the surface simpler by making the depth smarter, not by deleting it:
- **Defaults** replace questions.
- **Automation** replaces chores.
- **Inference** replaces configuration.
- **Clear organization** replaces a wall of options.

A simplification that removes something people rely on is treated as a regression, not progress.

Every capability gets a deliberate place on what the skill calls the placement ladder:
1. automatic,
2. default,
3. on the surface,
4. in context,
5. one level down,
6. advanced,
7. removed.

Removal is the last rung. It needs evidence that nobody uses the feature, plus your approval. Hidden gestures and easter eggs don't count as a place.

The same idea applies below the interface:
- In architecture, it means the fewest moving parts that still meet the quality bar. Backups, auth, and monitoring are never the thing you "simplify away".
- In an API, it means a short common call with the full power still available through optional parameters.
- In a refactor, it means a cleaner interface with every old caller still working.

On top of that, the skill gives the agent:
- seven principles, each tied to an action,
- six modes for the work it is asked to do: Create, Simplify, Review, Engineer, Decide, Tell,
- an output format for each mode, so answers lead with a decision and stay short,
- guardrails for advanced features, accessibility, security, recovery, and engineering quality.

## What it looks like in practice

These examples come from the evaluation runs in [`evals/`](evals/). The transcripts are in [`evals/runs/`](evals/runs/).

**"Make our settings minimal, like Apple would."** Without the skill, the agent cut accessibility controls and hid developer options. With it, in all three runs, the 26 settings became seven or eight labeled groups:
- text size, contrast, and reduced motion stayed, following the system by default,
- export and account deletion stayed under Data & Privacy,
- developer options went to a visible Advanced section.

The report ended with the number of capabilities lost: zero.

**"New users find our pro photo editor overwhelming. Make it simpler."** With the skill, the agent:
- gave newcomers a calmer default workspace and a guided start,
- kept every professional tool, from RAW processing to tethered shooting and plugins,
- kept the experts' shortcuts and custom layouts intact.

**"This 19-parameter function is misused in 40 places. Simplify it."** With the skill, the agent:
- grouped the parameters into a few concepts (format, per-format options, delivery), so contradictory combinations can't be written,
- kept every behavior,
- kept the old signature as a deprecated adapter, so none of the 40 callers broke.

## Inspired by Steve Jobs, built for your product

The principles come from Jobs' own recorded words and from people who worked with him:
- the 1983 Aspen design talk,
- the WWDC 1997 Q&A,
- *BusinessWeek* in 1998,
- the iPod and iPhone launches,
- the "Thoughts on Flash" letter,
- Andy Hertzfeld's accounts of the Macintosh team,
- Ken Kocienda's *Creative Selection*,
- Walter Isaacson's authorized biography.

Every quote in the skill was checked against a transcript or the original, and is cited. Popular misattributions are flagged, including "Simplicity is the ultimate sophistication", which came from a 1977 Apple brochure, not from Jobs. The full evidence base is in [`references/sources.md`](skills/insanely-great/references/sources.md).

What the skill takes from Jobs is the reasoning:
- start from the experience,
- focus,
- care about the parts nobody sees,
- own the whole product,
- ship.

It does not ask agents to copy Apple's look, imitate Jobs' voice, or repeat his management style. It also records where the approach went wrong (the G4 Cube, MobileMe, the iPhone 4 antenna, and Final Cut Pro X launching without features professionals needed), because knowing the limits is part of using the ideas well.

The name is Jobs' phrase for the standard the Macintosh team aimed for. Steven Levy later used it as the title of his 1994 history of the Mac.

## Install

**Any agent, with the [skills CLI](https://github.com/vercel-labs/skills):**

```bash
npx skills add saadalmana49-crypto/The-Mind-of-Steve-Jobs
```

It asks which agents to set up. It installs one copy in `~/.agents/skills/`, which Codex, Gemini CLI, Cursor, and others read, and links it for Claude Code. Add `-g -y` to install globally without prompts.

**Claude Code, as a plugin:**

```text
/plugin marketplace add saadalmana49-crypto/The-Mind-of-Steve-Jobs
/plugin install insanely-great@insanely-great
```

**Gemini CLI:**

```bash
gemini skills install https://github.com/saadalmana49-crypto/The-Mind-of-Steve-Jobs.git --path skills/insanely-great
```

**Codex:** ask the built-in installer:

```text
$skill-installer install https://github.com/saadalmana49-crypto/The-Mind-of-Steve-Jobs/tree/main/skills/insanely-great
```

**Any agent, by hand:** clone once and symlink, so `git pull` keeps it current:

```bash
git clone https://github.com/saadalmana49-crypto/The-Mind-of-Steve-Jobs.git ~/insanely-great
mkdir -p ~/.agents/skills ~/.claude/skills
ln -s ~/insanely-great/skills/insanely-great ~/.agents/skills/insanely-great   # Codex, Gemini CLI, Cursor, Copilot, Windsurf
ln -s ~/insanely-great/skills/insanely-great ~/.claude/skills/insanely-great   # Claude Code
```

For Cline, link the folder into `~/.cline/skills/` instead. For Devin, commit it to `.agents/skills/insanely-great/` in a connected repository. Each agent's paths, version, and test status are listed in [docs/compatibility.md](docs/compatibility.md).

## Use

The agent loads the skill on its own when a task fits:
- planning a product,
- scoping a feature,
- reviewing a flow,
- organizing settings,
- designing an architecture or an API,
- writing launch copy.

To call it directly, use:
- `/insanely-great` in Claude Code, Cursor, and Cline,
- `$insanely-great` in Codex,
- `@insanely-great` in Windsurf,
- `@skills:insanely-great` in Devin.


```text
/insanely-great plan an app that helps night-shift nurses track their sleep
/insanely-great review this onboarding flow: <screens, a URL, or code>
Simplify our admin console without losing anything our power users rely on.
Propose the architecture for our three-person team's booking platform.
Which five of these twelve roadmap items should we do next quarter?
```

## What's inside

```
skills/insanely-great/
├── SKILL.md              principles, placement ladder, modes, guardrails, output formats
└── references/           loaded only when a task needs them
    ├── product-thinking.md    finding the real problem, the product brief
    ├── simplicity.md          the full ladder, settings, professional tools
    ├── engineering.md         architecture, APIs, refactoring, performance, maintainability
    ├── experience-design.md   states, newcomer and expert paths, copy, visual craft
    ├── review.md              how to critique anything, with severity levels
    ├── focus-and-strategy.md  priorities, roadmaps, saying no
    ├── innovation.md          differentiation and technology bets
    ├── hardware-and-systems.md  devices, setup, ecosystems
    ├── storytelling.md        positioning, READMEs, launches
    ├── failure-modes.md       where this approach went wrong, and how it gets misused
    ├── examples.md            worked before-and-after examples
    └── sources.md             graded sources, verified quotes, misattributions
```

The skill itself is only Markdown, following the [Agent Skills specification](https://agentskills.io/specification): no scripts and no network calls. The Python files elsewhere in the repository (`evals/` and `scripts/`) are test and CI tooling. They are never installed with the skill. The agent always carries only the name and description, about 260 tokens. The main file (about 3k tokens) loads when the skill is used, and each reference loads only when its topic comes up.

## Evaluation

[`evals/`](evals/) holds 24 realistic scenarios. Each was run in Claude Code (model `sonnet`) 3 times without the skill, with version 1.0.0, and with version 1.1.0. A separate judge (`opus`) graded every answer blind, against checks written in advance.

| | No skill | Version 1.0.0 | Version 1.1.0 |
|---|---|---|---|
| Checklist items passed | 259 / 324 (80%) | 307 / 324 (95%) | 320 / 324 (99%) |
| Skill activated on its own | — | 60 / 72 runs | 64 / 72 runs |
| Average answer length | 628 words | 619 words | 680 words |

In blind head-to-head comparisons, the judge preferred version 1.1.0 over no skill in 64 of 72, and over version 1.0.0 in 51 of 72.

Across versions, the largest gains came from:
- keeping accessibility and advanced options when asked for "minimal",
- giving product plans a purpose, a hero path, and designed states,
- not presenting unsourced quotes,
- in 1.1.0, keeping the price breakdown in a simplified checkout, merging overlapping controls, and writing out error text.

The weak spots:
- 1.1.0 answers are about 10% longer than 1.0.0's.
- 1.1.0 lost to 1.0.0 in two of three runs on product planning, settings, and permissions.
- The skill often doesn't activate for short README rewrites.
- The ten scenarios added for 1.1.0 were also used to revise it, so its gains there are partly tuning.

All of it is in [evals/results.md](evals/results.md), with every transcript in [evals/runs/](evals/runs/) and the method and limitations in [evals/README.md](evals/README.md). These numbers measure Claude Code. Other agents were checked for installation and discovery only.

## Updating

| Installed with | Update with |
|---|---|
| skills CLI | `npx skills update` |
| Claude Code plugin | `/plugin marketplace update insanely-great` |
| Clone and symlink | `git pull` in the clone |
| Gemini CLI | Run the install command again |

Releases follow Semantic Versioning, adapted for instructions:
- a major version changes the skill's contract (its name, modes, or output formats),
- a minor version adds guidance,
- a patch fixes wording or sources.

See [CHANGELOG.md](CHANGELOG.md) and [CONTRIBUTING.md](CONTRIBUTING.md#versioning).

## Contributing

The most useful contributions are:
- corrections backed by a primary source,
- reports of an agent making a worse decision with the skill than it should have,
- test reports from agents we haven't tested yet.

Changes that alter behavior come with before-and-after eval numbers. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).

Insanely Great is an independent project. It is not affiliated with or endorsed by Apple Inc. or the estate of Steve Jobs. Apple, Macintosh, iPod, iPhone, iPad, and Final Cut Pro are trademarks of Apple Inc. Quotations are short excerpts used for commentary and are attributed to their sources.
