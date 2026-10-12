# Compatibility

Insanely Great, an Agent Skill inspired by Steve Jobs' philosophy of simplicity, product excellence, and thoughtful design, is a single folder, `skills/insanely-great/`, in the open [Agent Skills](https://agentskills.io/specification) format:
- a `SKILL.md` with `name` and `description` frontmatter,
- plus plain Markdown references.

It has no scripts, no tool-specific fields, and no network access. Any agent that reads standard `SKILL.md` folders can use it as is.

The status column means one of three things:
- **Tested:** we ran the agent ourselves and saw it discover or use the skill. The version and the check are listed.
- **Documented:** the agent's official docs say it reads skills from these paths. We have not run it.
- **Fallback:** the agent doesn't support skills, so you point it at the file manually.

Last checked: October 2026.

| Agent | Status | Where it looks (user / project) | How to invoke explicitly |
|---|---|---|---|
| Claude Code | **Tested** (2.1.296) | `~/.claude/skills/` / `.claude/skills/`, or as a plugin | `/insanely-great` (plugin: `/insanely-great:insanely-great`) |
| OpenAI Codex | **Tested: discovery only** (CLI 0.162.1) | `~/.agents/skills/` / `.agents/skills/` | `$insanely-great`, or `/skills` |
| Gemini CLI | **Tested: install and discovery** (0.60.0) | `~/.gemini/skills/` or `~/.agents/skills/` / `.gemini/skills/` or `.agents/skills/` | Activated automatically through `activate_skill` |
| Cursor | Documented | `~/.cursor/skills/`, `~/.agents/skills/` / `.cursor/skills/`, `.agents/skills/` (also reads `.claude/skills/`) | `/insanely-great` in Agent chat |
| GitHub Copilot (VS Code, CLI, cloud agent) | Documented | `~/.copilot/skills/`, `~/.agents/skills/`, `~/.claude/skills/` / `.github/skills/`, `.agents/skills/`, `.claude/skills/` | Automatic |
| Windsurf / Devin Desktop (Cascade) | Documented | `~/.codeium/windsurf/skills/`, `~/.config/devin/skills/`, `~/.agents/skills/` / `.devin/skills/`, `.windsurf/skills/`, `.agents/skills/` | `@insanely-great` |
| Devin (cloud agent) | Documented | Repository: `.agents/skills/` (recommended), also `.devin/`, `.github/`, `.claude/`, `.windsurf/` | `@skills:insanely-great` |
| Cline | Documented | `~/.cline/skills/` / `.cline/skills/`, `.clinerules/skills/`, `.claude/skills/` | `/insanely-great` |
| OpenCode, Goose, Roo Code, Kiro, Amp, and others | Documented by the [skills CLI](https://github.com/vercel-labs/skills) and the [Agent Skills client list](https://agentskills.io/) | Installed for you by `npx skills add` | Varies by tool |
| Tools without skill support | Fallback | Add a pointer to `AGENTS.md` or your rules file (see below) | The agent reads the file when the rule applies |

## What "tested" covered

All checks ran on macOS on 11 October 2026, in throwaway directories so the maintainer's own settings were not involved.

- **Claude Code 2.1.296.**
  - Copied the skill into a project's `.claude/skills/`. Ran 42 headless sessions across 14 scenarios (see [`evals/`](../evals/)). Claude invoked the skill on its own in all 42.
  - Installed it as a plugin from this repository's marketplace: `claude plugin marketplace add`, then `claude plugin install insanely-great@insanely-great`. `claude plugin details` listed the skill, at about 240 tokens always-on and about 4.4k when invoked.
  - `claude plugin validate .` passes.
- **Codex CLI 0.162.1.**
  - With the skill in a repository's `.agents/skills/`, `codex debug prompt-input` showed it in the model-visible skill list, with its full description.
  - We could not run a Codex session that uses the skill, because the test account hit its usage limit. Behavior in Codex is therefore untested.
  - With about 125 other skills installed, Codex warned that it had exceeded its skills context budget and shortened every description, ours included, to a few characters. If you have many skills, invoke this one explicitly with `$insanely-great`.
- **Gemini CLI 0.60.0.**
  - `gemini skills install <repo> --path skills/insanely-great` installed the skill at user scope. `gemini skills list` showed it enabled.
  - A symlink in `~/.agents/skills/` was also discovered.
  - Workspace skills (`.gemini/skills/`, `.agents/skills/` in a project) are skipped unless the folder is trusted.
  - We did not run a Gemini session that uses the skill.
- **`npx skills` (Vercel's skills CLI).**
  - `npx skills add <repo> -g -a claude-code -a codex -a gemini-cli -a cursor -a cline` found the skill. It installed one copy in `~/.agents/skills/`, which the CLI treats as shared by Codex, Gemini CLI, Cursor, and Cline, and symlinked it for Claude Code.
- **Cline CLI 2.17.0** was installed but not signed in, so it was not tested.

If you test the skill in another agent, please open an issue or PR with the agent's version and what you checked. We will move it from Documented to Tested.

## Fallback for tools without skills

Clone the repository somewhere stable. Then add this to `AGENTS.md`, `.cursorrules`, `.windsurfrules`, or your tool's rules file:

```markdown
## Product decisions
When planning a product or feature, deciding scope or priorities, reviewing UX, simplifying
something complex, or writing launch copy, read and follow
`/absolute/path/to/insanely-great/skills/insanely-great/SKILL.md`.
Load files from its `references/` folder only when SKILL.md points you to them.
```

This keeps the full skill out of every conversation. The agent loads it only when the rule applies.

## Known differences between agents

- **Explicit invocation** differs: `/name` (Claude Code, Cursor, Cline), `$name` (Codex), `@name` (Windsurf/Devin Desktop), `@skills:name` (Devin).
- **Plugin namespacing.** As a Claude Code plugin, the skill is invoked as `/insanely-great:insanely-great`. Automatic activation works the same way.
- **One active skill.** Devin's docs say only one skill can be active at a time.
- **Trust prompts.** Gemini CLI asks for confirmation before activating a skill, and loads workspace skills only in trusted folders.
- **Description budgets.** Agents shorten descriptions when many skills are installed (seen in Codex). Explicit invocation always works.
