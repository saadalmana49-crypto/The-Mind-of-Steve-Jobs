# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/) as described in [CONTRIBUTING.md](CONTRIBUTING.md#versioning).

## [1.1.0] - 2026-10-13

### Changed
- `SKILL.md` was rewritten to be shorter and more direct. It loads at about 3k tokens, down from about 4.4k, and keeps the seven principles, the placement ladder, the six modes, the guardrails, and the output formats.
- The description now also covers pricing, pipelines, permissions, notifications, and removing or deprecating features. It excludes small copy tweaks.
- **Guardrails:**
  - Before people pay, show an itemized cost and keep the terms, return, and cancellation information they are entitled to.
  - A new exception to "they decide": if a requested cut would make the product deceptive, unsafe, or non-compliant, deliver the closest compliant design instead and say why.
- **Principles:**
  - Check whether something the user already has can do the job ("configure before you build").
  - Merge concepts that overlap.
  - Keep a v1 within the user's constraints.
- **Output formats:**
  - The purpose is one sentence naming who it is for, the moment of use, and what they get.
  - A simplification ledger names what each removed item served and how that need is still met.
  - Copy ends with how to start, and flags unverified assumptions.

### Added
- **A "Make it concrete" section in `SKILL.md`:**
  - write the exact error text,
  - show the arithmetic behind estimates,
  - make invalid states impossible to express,
  - never invent facts about the user's product.
- **Reference additions:**
  - "Removing cleanly" in `simplicity.md`, a five-step process for removing a feature when the evidence supports it.
  - "Concrete, not aspirational" in `engineering.md`.
  - "Money moments" in `experience-design.md`, covering checkout, upgrades, and cancellations.
  - A details checklist (recovery, accessibility, copy) in `review.md`.
  - How-to-start guidance in `storytelling.md`.
- **Ten eval scenarios (n1–n10).** They cover more domains, and the ways the skill can misfire: tasks too small for the method, removals the evidence supports, checkout, AI controls, README copy, permissions, notifications, pricing, and data pipelines.
- **Eval harness:**
  - version arms (`--arm v1 --skill-dir`) for before-and-after comparisons,
  - several judging pairs per run (`--pairs baseline:skill,v1:skill`),
  - tokens and cost recorded for each run.
- `.gitattributes`, so GitHub counts the Markdown and treats eval transcripts as generated.

### Fixed
- Repository links in `.claude-plugin/plugin.json` and the docs now point to `The-Mind-of-Steve-Jobs`.
- The eval summary now averages cost only over runs that recorded it. Before, runs without cost data counted as $0.

## [1.0.0] - 2026-10-11

### Added
- The `insanely-great` Agent Skill, inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design. Its central rule is to remove complexity and keep capability, so products stay powerful underneath and effortless on the surface.
  - `SKILL.md` contains:
    - seven principles,
    - the placement ladder for organizing capabilities,
    - a layer-by-layer table covering strategy, architecture, implementation, APIs, workflows, interface, performance, maintainability, and the user journey,
    - six modes: Create, Simplify, Review, Engineer, Decide, Tell,
    - guardrails that protect advanced features, accessibility, security, recovery, and quality,
    - a response shape and output formats.
  - Twelve reference files, loaded on demand: product thinking, simplicity, engineering, experience design, review, focus and strategy, innovation, hardware and systems, storytelling, failure modes, worked examples, and graded sources.
- An evidence base that traces every principle to a source graded primary, first-hand, reported event, or interpretation. It includes 23 verified quotes and a list of common misattributions.
- A Claude Code plugin marketplace manifest, for one-command install.
- An eval harness (`evals/run.py`, `evals/judge.py`) with 14 scenarios, a rubric written before the final runs, and published results with raw transcripts.
- CI that validates the skill with `skills-ref` and the repository checks in `scripts/check.py`.
