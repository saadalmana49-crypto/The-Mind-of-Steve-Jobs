# Engineering: simple underneath, without lowering the bar

Use this for architecture, APIs, SDKs, CLIs, data models, implementation, refactoring, performance, and maintainability. The goal is the same as everywhere else in this skill: remove complexity, keep capability. In engineering, capability includes quality: correctness, data integrity, security, reliability, and the ability to change the system safely.

Jobs' argument at WWDC 1997 applies directly: start with the customer experience and work backwards to the technology (WWDC97). Architecture is chosen to deliver an experience at a quality bar. It is not chosen first and then justified.

## 1. Derive the quality bar from the experience

Before choosing an architecture, write down what the experience requires:

| Requirement | Ask |
|---|---|
| Latency | How fast must the hero path feel? Which actions must be instant? |
| Correctness and integrity | What data must never be lost, duplicated, or corrupted? |
| Availability | What happens to users if this is down for a minute? An hour? |
| Security and privacy | Whose data is this? Who may see or change it? What does the law require? |
| Scale | Realistic load in the next 12 months, not the dream. What would force a change? |
| Change | Who will maintain it? How often will it change? |

These numbers decide the design. Anything they don't require is a candidate for removal.

## 2. Choose the fewest moving parts that meet the bar

- **Start with one deployable, one primary database, and proven technology.** Add a service, a queue, a cache, or a second datastore only when a requirement in step 1 needs it. Write that requirement down next to the component.
- **Keep one source of truth for each piece of data.** Derived copies (caches, search indexes, analytics) are rebuildable and labeled as such.
- **Own what determines the experience, rent the rest.** Jobs called Apple the company that made "the whole widget" (WW03). In software, the test is: if this part is mediocre, does the core experience suffer?
  - If yes, build or control it.
  - If no, use a managed service or a standard library: payments, email delivery, auth providers, observability, hosting.
- **Write down the triggers for more complexity** ("add a read replica above 500 queries/second"), so the simple design isn't replaced by guesswork later.

**Never simplified away**, whatever the size of the team:
- authentication and authorization, including tenant isolation in multi-tenant products,
- input validation,
- backups that have actually been restored in a test,
- reversible migrations,
- secrets management,
- structured logs and alerting on the hero path,
- error handling that never loses user data.

These are capability, not complexity.

## 3. APIs, SDKs, and CLIs: a simple surface over full power

An interface is good when the common case is obvious and the uncommon case is possible.

- **Few concepts, named in the domain's words.** One noun per concept, the same name everywhere: endpoint, SDK, docs, errors.
- **One obvious way for the common task,** with safe defaults. Required inputs are only what can't be defaulted or inferred.
- **Full power through optional parameters, flags, config, and escape hatches.** Advanced users keep every capability. They just don't pay for it on the common path.
- **Unify instead of multiplying.** Prefer one operation with a parameter over a family of near-duplicates. For example, `export --format csv|json|pdf` instead of `export-csv`, `export-json`, and `export-pdf`.
- **Errors say how to fix the call:** what was wrong, which field, an example of a valid value, and a link to the docs.
- **Never break callers silently.** Add before you remove:
  1. Introduce the simpler interface.
  2. Make the old one a thin adapter over it.
  3. Mark it deprecated, with a warning and a date.
  4. Measure usage.
  5. Remove it only after the stated period.
- **CLIs:**
  - a zero-configuration happy path (detect what you can),
  - flags for the exceptions,
  - no prompts in non-interactive mode,
  - output that says what happened and what to do next,
  - exit codes that scripts can trust.

## 4. Implementation: the back of the cabinet

"You're not going to use a piece of plywood on the back, even though it faces the wall and nobody will ever see it" (PB85). Code is the back of the cabinet. Users feel its quality through reliability and speed, and future teammates feel it directly.

- **Deep modules:** a simple interface over a rich implementation. This matches the product philosophy at the code level. The idea is described by John Ousterhout in *A Philosophy of Software Design*; it is related reading, not a Jobs source.
- **One way to do each thing** in the codebase. Remove parallel helpers, duplicate abstractions, and competing patterns.
- **Delete what nothing uses:** dead code, stale feature flags, unused options, speculative extension points. Keep anything with a caller or a user. Check before deleting.
- **Name things in the domain's vocabulary,** especially at user-facing boundaries: API fields, CLI flags, error messages, log events.
- **Make failure paths first-class:** timeouts, retries with backoff where they're safe, idempotency keys for operations that must not run twice, clear error types.
- **Test what the experience depends on:** the hero path, the failure paths, and the data invariants. Test the behavior, not the implementation.

## Concrete, not aspirational

- **Write the error text.** "Clear errors" means the exact message, for example: `ExportError: pdf options given with format="csv". Use PdfOptions with format="pdf", or remove the options.`
- **Show the arithmetic for every estimate,** for example: 5,000 users × 20 uploads a day = 100,000 a day, or about 1.2 a second on average. Then size for the peak hour, not the average.
- **Make invalid states impossible to express.** If options belong to a format, let the options type select the format, instead of checking a separate string. If two settings must be set together, make them one object.
- **Keep pure logic apart from side effects.** Rendering, calculation, and validation should be pure functions. Delivery, storage, and network calls go at the edges, where they can be retried and tested separately.
- **Never invent facts.** Don't make up APIs, numbers, or library behavior you weren't given. Mark placeholders, or ask.

## 5. Configuration

Every configuration option is a decision handed to someone else:
- Default everything you can, and validate configuration at startup with errors that name the fix.
- Offer presets for common setups, with full configuration underneath for experts.
- Remove an option only when it has no users. Otherwise, keep it and give it a good default.

## 6. Performance is part of the experience

Hertzfeld recounts Jobs pushing the Mac team to cut boot time by arguing that seconds multiplied by millions of users added up to lifetimes (FL-SAVE). Use the arithmetic to choose what to optimize:

```
seconds saved × uses per day × users = time returned per day
```

- Set budgets for the hero path (first render, the core action, search, save) and measure them on realistic devices and networks.
- Optimize where the arithmetic is largest. Don't add caches, layers, or concurrency where it isn't.
- Perceived performance counts: immediate feedback, optimistic updates where they are safe, progress for long work.

## 7. Maintainability

- **Fewer special cases.** Every `if customer == "acme"` is complexity someone will pay for later.
- **Small, deliberate dependencies.** Each one is code you now maintain, update, and secure.
- **Observability that answers questions:** can you tell, in minutes, whether the hero path is working for users right now?
- **Docs that run:** quickstarts and examples are tested in CI.
- **Consistent patterns** across the codebase, so a change in one place looks like a change in any other.

## Refactoring for simplicity, without losing capability

1. **Write down the current capabilities and contracts:** public API, CLI flags, config, file formats, behaviors users rely on.
2. **Pin them with tests** before changing anything.
3. **Simplify the internals:** merge duplicates, delete dead paths, deepen modules.
4. **Simplify the surface additively:** new defaults, presets, and unified entry points, with the old paths kept as adapters.
5. **Report a capability ledger:** kept, moved, deprecated (with a timeline), removed (with evidence of no usage and the user's approval).

## Engineering checklist

- [ ] The quality bar is written down and derived from the experience.
- [ ] Every component maps to a requirement. No component exists "for the future".
- [ ] Auth, validation, tested backups, migrations, secrets, logs and alerts are present.
- [ ] Interfaces: the common path takes the fewest inputs, the full power stays optional, errors name the fix.
- [ ] No caller breaks without a deprecation path.
- [ ] Hero-path performance budgets are set and measured.
- [ ] Dead code, stale flags, and unused options are removed. Everything with a user is kept.
- [ ] Tests cover the hero path, the failure paths, and the data invariants.
