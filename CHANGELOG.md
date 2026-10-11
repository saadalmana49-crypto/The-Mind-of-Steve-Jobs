# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/) as described in [CONTRIBUTING.md](CONTRIBUTING.md#versioning).

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
