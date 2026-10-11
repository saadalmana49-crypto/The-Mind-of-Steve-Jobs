# Focus and strategy: deciding what to build

"People think focus means saying yes to the thing you've got to focus on. But that's not what it means at all. It means saying no to the hundred other good ideas that there are. You have to pick carefully" (WWDC97).

## Ten to three

Isaacson describes a ritual at Apple's annual "Top 100" retreat. Jobs would ask for the ten things the company should do next, write them on a whiteboard, cross out the bottom seven, and say, "We can only do three" (ISA11). Use the same move for any roadmap, sprint, or feature list:

1. **List the candidates.** Merge duplicates and requests that serve the same need.
2. **Connect each one to the purpose** and to evidence: who needs it, how often, how much it hurts, what they do today.
3. **Keep at most three.** If you have more than three "must-haves", the purpose is not sharp enough yet.
4. **Write the Not-now list.** One line per item with the reason, plus the signal that would bring it back ("revisit if more than 20% of churned accounts cite it").
5. **Write down what would change your mind.**

## Focus for new work, organization for what exists

Focus decides what you build *next* and what earns the surface. It is not a reason to delete capabilities people already rely on.
- **For new work:** keep at most three items, and give everything else a reason on the Not-now list.
- **For an existing product that feels bloated:** simplify by organizing it. Merge duplicates, add defaults, automate, and move capabilities down the placement ladder (simplicity.md). Remove only what has no users or purpose, with evidence and the user's agreement.
- **For a roadmap:** prefer work that makes the existing product simpler *and* keeps its power. Faster core actions, clearer errors, and better defaults often beat new features.

## Choosing the three

There is no formula. These questions separate the strong candidates from the weak:
- **Does it improve the hero path for most users,** or a side path for a few?
- **Arithmetic:** time or pain saved × frequency × users (see experience-design.md).
- **Is it the reason the product exists** (what it's brilliant at), or table stakes? Table stakes only need to be good enough.
- **Does it simplify the product or add to it?** Prefer work that removes complexity: faster, fewer steps, fewer failures, clearer errors.
- **What does it cost forever,** not just to build? Count maintenance, support, docs, the test matrix, UI space, the concepts users must learn, and how it interacts with every other feature.
- **Can it be undone?** Reversible bets can be made quickly. Irreversible ones (data models, public APIs, pricing promises) need more care.
- **Does it make what you already have better?** Often the best item on the list is a fix: speed, reliability, error messages.

## The 2×2: one clear choice per need

Isaacson reports that after Jobs returned in 1997, he asked of the many Mac models, "Which ones do I tell my friends to buy?" Then he drew a grid with Consumer and Pro across the top and Desktop and Portable down the side, and said the job was to make four great products, one per square. Most of the line was cancelled (ISA11).

Use this for product lines, pricing tiers, editions, and configuration presets:
1. Find the **two axes customers actually use to sort themselves** (solo vs. team, personal vs. professional, small vs. large data).
2. Allow **at most one offering per square.** Leave a square empty if no one needs it.
3. **The test:** a customer can tell which square is theirs in seconds, and you can tell a friend which one to buy.

## The real cost of yes

Each feature adds:
- build and test time,
- documentation,
- support load,
- a concept to learn,
- space on the screen,
- combinations with every other feature,
- and future migration work.

Removing a feature later costs trust and needs a deprecation path. Saying yes is easy and unsaying it is hard, so the default answer to a new feature is "not now, and here is why".

## Saying no well

When a user, stakeholder, or teammate asks for something outside the focus:
1. Acknowledge the need behind it, in their words.
2. Explain the tradeoff: what it would displace or complicate.
3. Offer what serves that need inside the current focus, if anything does.
4. Record it on the Not-now list with the signal that would bring it back.

In agent work, the user is the decision-maker. Present the recommendation and the tradeoff, deliver the work with the recommended core first, and let the user confirm or override.

## Decide with working things

- Kocienda describes decisions at Apple being made by trying working demos, often two variants of the same idea, and choosing the one that felt right in use (KOC18).
- When opinions collide, build the smallest concrete version of each and compare them.
- Lashinsky reports Apple's practice of naming a Directly Responsible Individual (DRI) for every task (LAS11). Every decision should have one owner. In a user–agent session, that owner is the user.

## Process serves content

"People start to get confused that the process is the content" (LI95). Warning signs:
- A roadmap made of process milestones instead of user-visible outcomes.
- Specs reviewed more carefully than prototypes.
- Debates about frameworks instead of demos of the product.

Plan around what the user will experience.

## Ship: fixed date, flexible scope

- **Hold the date and cut the scope.** "Real artists ship" was a Mac-team slogan for exactly this (FL-SHIP).
- **Never ship the part that isn't ready.** In his own email, Jobs wrote that MobileMe "was simply not up to Apple's standards - it clearly needed more time and testing" (ME08).
- **Ship in slices, not as a monolith.** The same email says Apple should have launched over-the-air iPhone syncing first, then the web apps one at a time, about 30 days apart, each only if the previous one went well (ME08). Release the smallest piece that delivers value, watch it, then add the next.
- **Avoid stacked launches.** Jobs called launching MobileMe alongside iPhone 3G, iPhone 2.0 software, and the App Store "a mistake" (ME08). Give each risky change full attention and a clean rollback.

## Strong opinions, revised with evidence

In June 2007, Apple told developers that web apps were the "sweet solution" for iPhone software (WWDC07). Four months later, Jobs announced a native SDK (SDK07). A clear position helps a team move. Changing it when the evidence turns is part of the discipline, not a betrayal of it. Every decision memo should state what would change the recommendation.

## Decision memo

```
Recommendation:  <at most 3 items>
Why:             <each item → which part of the purpose it serves, with the evidence>
Not now:         <item: reason; signal to revisit>
Risks:           <what could go wrong; how we'll notice>
Would change if: <evidence that would flip the decision>
```
