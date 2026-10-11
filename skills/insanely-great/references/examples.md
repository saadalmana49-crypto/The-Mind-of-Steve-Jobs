# Worked examples

These are illustrations of the method, not historical accounts. Each one shows a typical first draft, the same work done with this skill, and the reasoning. Adapt the pattern; don't copy the details.

---

## 1. Create: a new consumer app

**Request:** "Plan an app that helps busy families with meal planning."

**Typical first draft:**
- A recipe database with search and filters
- A weekly planner
- A grocery list
- Nutrition tracking
- Pantry inventory
- Social sharing
- AI recommendations
- Budget tracking
- 12 screens and a backend with accounts

Everything is "MVP".

**With this skill:**
```
Purpose:        On Sunday evening, a parent plans the week's dinners in five minutes
                and gets one grocery list that matches.
Real problem:   Not "finding recipes" — deciding what to cook each night and buying
                the right things in one trip.
Hero path:      1 open → 2 household size + up to 3 dislikes → 3 app proposes 5 dinners
                → 4 swap any with one tap → 5 grocery list, grouped by aisle (5 steps)
                Repeat use: open → "repeat favorites" or "new mix" → adjust → list (3 steps)
Brilliant at:   A week of dinners in under five minutes; a complete list in store order.
Depth:          Dietary filters and serving overrides one level down on each recipe;
                editing the list (add any item, reorder aisles) in context; household
                profiles and sharing in Settings; export list as text (Advanced).
Not now:        Nutrition tracking: a different job, needs data entry.
                Pantry inventory: high upkeep; revisit if users report buying duplicates.
                Social sharing: no evidence it serves the job.
                AI chat: one-tap swap covers "suggest something else".
                Budget tracking, multiple meals per day, import from any website: v1.x
                if usage shows demand.
States:         First run: 40 tested recipes, no empty shell.
                Empty week: "No dinners planned yet. Plan in 5 minutes."
                Offline: planning and list work fully offline.
                Success: list ready; share via the system share sheet.
Quality bar:    Every recipe tested and ≤ 30 minutes; quantities scale to household;
                list merges duplicates ("3 onions", not three lines); usable one-handed
                in a store; supports large text.
Technology:     A mobile app with local storage and a static recipe feed. No accounts
                in v1. Sharing uses the platform share sheet.
Open decisions: One platform first, or both? Curated recipes only, or user-added in v1?
```
**Why:** The purpose sentence decided everything else. Nutrition and pantry features are reasonable, but they serve different jobs, and each one adds daily upkeep for the user.

---

## 2. A request that adds complexity

**Request:** "Users of our task app want priorities (P1–P4), flags, stars, an 'important' toggle, colored labels, and a 'Today' view. Spec all of it."

**Typical first draft:** six independent features, each with its own UI, filters, and settings.

**With this skill:** lead with the needs, recommend a core, and still deliver the full spec.
- **Needs behind the requests:** (a) "what matters most", (b) "what's due soon", (c) "group related tasks".
- **Recommendation:** one importance marker (star), due dates, and labels. "Today" is generated automatically from due-today, overdue, and starred tasks.
  - P1–P4, flags, and "important" all express need (a), three times over.
  - Tradeoff: teams that triage with numeric priorities lose granularity.
- **Spec structure:**
  1. Star, due dates, labels, and the automatic Today view (full detail).
  2. *Not now / later phase:* P1–P4. It would add a field and sort order. Revisit if team accounts use the star on more than 40% of tasks, a sign that one level isn't enough.
  3. *Not now:* flags and "important". Both duplicate the star.
- **Question to the user:** "Do you want me to proceed with the consolidated version, or spec all six as requested?"

**Why:** Nothing was silently dropped. The user sees the reasoning and decides.

---

## 3. Simplify settings without breaking anyone

**Request:** "Our podcast app's settings are a mess (31 items). Make it minimal."

**Typical first draft:**
- Removes text size, reduced motion, and transcripts ("the OS handles it").
- Removes OPML export.
- Hides developer logs behind tapping the version number seven times.

**With this skill:**
| Group | Contents | Notes |
|---|---|---|
| Playback | Speed, skip intervals, sleep timer | Per-show speed lives on the show page, not here |
| Downloads & Storage | Download over cellular, auto-delete played episodes (on by default) | Storage limit replaced by auto-delete: a decision automated |
| Notifications | New episodes (all / chosen shows / off) | 14 per-show toggles moved to each show's page |
| Appearance & Accessibility | Theme (follows system), text size, reduce motion, transcripts | Kept: the app renders its own text and animations |
| Language | App language (defaults to device) | Kept as an override |
| Privacy & Data | Analytics opt-out, export subscriptions (OPML), delete account | Export and delete are the user's way out |
| Advanced | Diagnostic logs | Labeled and visible, never hidden |
| About | Version, licenses | |

| | Before | After |
|---|---|---|
| Top-level items | 31 | 8 groups |
| Removed | — | "Show tips" (became contextual hints), "Restart onboarding" (unused) |
| Kept and moved | — | Per-show settings (to the show page), logs (to Advanced) |
| Capabilities lost | — | 0 |

**Why:** Fewer decisions on the main screen. Every capability is still there, and nothing was removed that someone needs to read, recover, or leave.

---

## 4. Simplify a professional tool without dumbing it down

**Request:** "New users find our analytics app overwhelming. Simplify it."

The app has a SQL editor, a visual query builder, custom metrics, 14 chart types, dashboard filters, scheduled email reports, row-level permissions, an API, and embedding.

**Typical first draft:** "Remove the SQL editor, custom metrics, and the API for a clean, simple experience." That breaks the analysts who pay for the product.

**With this skill:** Simplify the surface, keep the depth.
| Capability | Rung | Change |
|---|---|---|
| Ask a question in plain language → chart | Surface | New starting point for newcomers |
| Templates for the 6 most common dashboards | Surface | First run starts from a template, not a blank canvas |
| Visual query builder | Surface | Unchanged |
| Chart type | Default | Picked automatically from the data. All 14 types one click away |
| SQL editor | One level down | "Edit as SQL" on any chart. Remembered per user, so analysts land there directly |
| Custom metrics, filters | One level down | In the chart's side panel |
| Scheduled reports | In context | "Schedule" on any dashboard |
| Row-level permissions, API, embedding | Advanced | Workspace settings → Advanced, plus the developer docs |

```
Steps to first chart (newcomer): 7 → 3        Analyst's path to SQL: unchanged (remembered)
Concepts on the first screen: 9 → 3           Capabilities lost: 0
```

**Why:** The newcomer's problem was the starting point, not the existence of SQL. The fix is a better entrance plus good defaults. Experts keep everything, and they keep their speed.

---

## 5. Architecture: simple underneath, same quality bar

**Request:** "Design the backend for our newsletter platform. Three engineers, about 2,000 writers and 400,000 readers expected next year."

**Typical first draft:** Eight microservices, an event bus, Kubernetes, a separate analytics database, and GraphQL federation.

**With this skill:**
- **Quality bar from the experience:**
  - Publishing is instant for writers.
  - Emails go out within 15 minutes, with no duplicates.
  - Subscriber lists are never lost.
  - Payments are correct.
  - Unsubscribing works every time.
- **Design:**
  - One web application and one Postgres database.
  - A background job queue for email sending, using idempotency keys per recipient, so retries never double-send.
  - A managed email provider and a managed payments provider. Neither is the product's differentiator.
- **Never skipped:**
  - nightly backups with a monthly restore test,
  - auth and per-writer authorization,
  - input validation,
  - structured logs,
  - alerts on send failures and payment webhooks.
- **Triggers for more complexity:**
  - Add a read replica if reader-facing queries exceed 300 per second.
  - Move sending to a separate worker fleet if a single send exceeds 1 million recipients.
- **Not now:** microservices, an event bus, and a separate analytics store. No requirement needs them yet.

**Why:** Fewer moving parts, the same guarantees. Every component maps to a written requirement.

---

## 6. Refactor without breaking callers

**Before:** a function that grew one flag at a time.
```python
def fetch(url, timeout=None, retry=False, retries=3, backoff=False, backoff_base=0.5,
          cache=False, cache_ttl=60, verify_ssl=True, raise_on_error=True, json=False):
    ...
```

**After:** a simple common path, with the same capability.
```python
def fetch(url, *, timeout=10, retry=Retry.default(), cache=None,
          verify_ssl=True, raise_on_error=True) -> Response:
    """Fetch url. Failures raise FetchError naming the URL and the likely fix."""

response = fetch(url)                                  # common case: sensible defaults
response = fetch(url, retry=Retry(attempts=5, backoff=0.5), cache=Cache(ttl=60))
data = response.json()                                 # replaces json=True
```
- Related flags became objects with defaults. `retry`, `retries`, `backoff`, and `backoff_base` became `Retry`. `cache` and `cache_ttl` became `Cache`.
- `json=True` became `response.json()`. `raise_on_error` and `verify_ssl` are unchanged.
- The old signature stays as a deprecated adapter for two minor versions, with a warning that shows the equivalent new call.

**Capability ledger:** every behavior kept, 6 flags merged into 2 objects, 1 flag replaced by a method, 0 removed.

---

## 7. Review: a fitness app's first run

**Request:** "Review our onboarding."

**With this skill (abridged):**
```
Verdict:  Built to get a beginner into a first workout, but the first workout appears
          only after 4 screens of questions and an account wall.
Numbers:  Before first workout: 4 screens, 12 required fields, 1 account wall, 0 previews.
          Proposed: 1 screen, 2 questions, account after the first workout.
Findings:
[Major] 12 required profile questions; 3 (body-fat %, target date, gym name) aren't used
        by the plan generator. Fix: ask level and minutes per day; infer the rest from use.
[Major] Account required before seeing any workout. Fix: let them try one, then offer an
        account to save progress.
[Minor] "Sync failed (E_TOKEN)" toast after sign-in. Fix: "Couldn't save your progress yet.
        We'll retry automatically." Keep the code in the logs.
[Polish] Video loops start with a black frame. Fix: poster image from frame 1.
Simplify: Remove the "Motivation style" quiz (unused). Move "Connect 6 wearables" out of
          onboarding.
Capability check: Wearable connections move to Settings, with a prompt when a device is
          detected. Body-fat % and target date move to the optional profile. Nothing removed.
Missing states: offline workout (cached video), interrupted workout (resume prompt).
Keep:     The plan generator's first workout is excellent. Lead with it.
```

---

## 8. Should we build it at all?

**Request:** "Build an internal dashboard showing whether our six services are up."

**With this skill:** The purpose is that anyone on the team can see, in seconds, whether something is down and who is handling it. The current alternative is pinging people in chat.
- **Recommendation:** use the status-page or uptime feature of the monitoring tool the team already pays for.
- **If they must build:** one static page generated every minute from health-check endpoints. It shows six rows, green or red, with the on-call name. No accounts, no database.
- **Not now:** historical charts (the monitoring tool has them), custom alerting (same).

**Why:** The cheapest experience that delivers the purpose is often configuration, not code.

---

## 9. A CLI that asks too much

**Before:**
```
$ dbmigrate init
? Database type (postgres/mysql/sqlite):
? Host:  ? Port:  ? User:  ? Password:  ? Database:
? Migrations directory:  ? Table name for history:
? Naming scheme (timestamp/sequential):  ? Transaction mode:  ? Lock timeout:
```

**After:**
```
$ dbmigrate init
Found DATABASE_URL in .env (postgres, app_dev).
Created migrations/ and migrations/0001_init.sql.
Next: write SQL in that file, then run `dbmigrate up`.
```
- Defaults: timestamp names, a transaction per migration, the history table `schema_migrations`.
- Each default is overridable by flag or config file. Nothing is asked in non-interactive mode.
- **Not removed:** every option still exists as a flag. The common path just doesn't make the user choose.

---

## 10. An SDK with too many ways in

**Before:** three ways to authenticate (`apiKey` param, `setCredentials()`, `AUTH_TOKEN` env var), and two client classes (`Client`, `AsyncClient`) whose method names differ.

**After:**
- One client: `Client()`. It reads `PAYMENTS_API_KEY` by default, or takes `Client(api_key=...)`.
- `AsyncClient` keeps, and uses exactly the same method names as `Client`.
- Errors name the fix: "No API key found. Set PAYMENTS_API_KEY or pass api_key=."
- `setCredentials()` is deprecated with a warning for two minor versions before removal. That is the migration path.

---

## 11. Hardware: a smart door lock

**Purpose:** Let the right people in without keys, and never lock anyone out.
- **On the device:**
  - Keypad and physical key, both working with no phone, app, or network.
  - A status light for locked, unlocked, and low battery.
  - Auto-lock after closing (default on, adjustable in the app).
- **In the app:** guest codes with schedules, an activity history, battery level, settings.
- **Setup target:** under 10 minutes from the box. A printed template for the drill holes. Pairing by scanning the code on the lock. Wi-Fi optional (Bluetooth works without it).
- **Failure states designed:**
  - Dead battery: weeks of low-battery warnings, plus external contacts for an emergency 9V jump.
  - Lost phone: keypad and key still work.
  - Company service shuts down: local codes and Bluetooth keep working, as stated on the box.
- **Validated in real use:** gloves, rain, darkness (backlit keys), doors that sag over the seasons.

---

## 12. Tell: a README opening

**Before:**
> LogLens is a next-generation, AI-powered, blazing-fast observability platform that seamlessly unifies your logs.

**After:**
> **LogLens** finds the log line you need across a hundred files in under a second.
>
> `loglens "payment failed" ./logs` → matching lines, grouped by request, newest first.
>
> - Searches 10 GB of logs in about 0.8 s on a laptop (benchmark and setup in `bench/`).
> - Understands JSON and plain-text logs without configuration.
> - Works offline. Nothing leaves your machine.
>
> **Limits:** no live tailing yet; no Windows event logs.

**Why:** It states one concrete result, shows it, gives three specific strengths with their conditions, and admits its limits.
