# Product thinking: find the real problem

Use this before designing or building anything bigger than a single screen. The result is a **Product brief** (the format is in SKILL.md). Write it before choosing features or a stack.

## Work backwards from the experience

Jobs' answer to a developer at WWDC 1997 was that you start with the customer experience and work backwards to the technology, not the other way round (WWDC97). In practice:

1. Write the **first-use story** before any feature list. Make it 5–8 sentences, in the present tense, from the user's side: where they are, what they need, what they do, what they get, and how long it takes.
2. Underline every capability the story needs. Those are the features.
3. Anything not in the story has to justify itself or go on the Not-now list.
4. Only then choose the technology that makes the story true with the least machinery.

The iPod shows this order. The promise was "1,000 songs in your pocket" (IPOD01). The promise set the requirements: enough storage, a pocket-sized body, and a sync that wouldn't take hours. Apple's launch materials said FireWire could load 1,000 songs in under ten minutes. The connector was chosen to serve the experience, not the other way round.

## The questions, in order

Answer each one in a line or two. If you can't, that is the work to do next. Don't start building.

1. **What is it for?** Write one sentence a non-expert can repeat.
   - Weak: "An all-in-one productivity platform for creators."
   - Strong: names a person, a moment, and a result the person would notice.
2. **Who, and in what moment?** Describe the situation of use, not demographics. "Between client calls, on a phone" says more than "freelancers aged 25–40".
3. **What is the real problem behind the request?** Keep asking "so that…?" until you reach a need the user would recognize in their own words. Stop before it turns abstract.
4. **What do they do today?** Name the current alternative: a spreadsheet, a group chat, a shared calendar, or nothing.
   - The new thing must beat that alternative *on the hero path*, not on the feature count.
   - Sometimes the honest answer is to configure what already exists instead of building.
5. **What must it be brilliant at?** Pick one to three things. Brilliant means better than anything the user has tried, not merely present.
6. **What lies beneath the surface?** List the capabilities the product needs beyond the hero path: advanced options, expert workflows, integrations, admin, export. Decide where each one lives on the placement ladder (simplicity.md). A focused product still needs depth.
7. **What is the hero path?** List the steps from arrival to first value, and count them. Then do the same for the most frequent repeat task.
   - Isaacson reports that the iPod team set a goal of reaching any song in three presses (ISA11).
   - Set your own budget, then design to it.
8. **Why would someone recommend it?** After the 1997 return, Jobs asked of Apple's sprawling Mac line, "Which ones do I tell my friends to buy?" (ISA11). If your answer to "why recommend it?" is a feature list, the purpose is not clear yet.

## Show, don't survey

"A lot of times, people don't know what they want until you show it to them" (BW98). This is about *how* to learn from people, not permission to ignore them:
- **Evidence that helps:** what people do with a prototype, workarounds they have built, support tickets, drop-off points, and how often the hero path is used.
- **Evidence that misleads when treated as a spec:** feature-request vote counts, "would you use X?" surveys, and competitors' feature lists. Treat requests as signals of a need, then design the answer yourself.
- **Make it concrete early.** Kocienda describes iPhone and iPad software decisions being made by trying working demos, often two alternatives side by side, rather than debating documents (KOC18).
  - For an agent, that means producing a clickable mock, a short CLI transcript, or two small variants.
  - Then choose by using them, with the criteria stated.

## Expect the idea to change

Jobs warned against thinking a great idea is most of the work. "There's just a tremendous amount of craftsmanship in between a great idea and a great product" (LI95).
- As you build, you discover tradeoffs the brief could not see.
- Revisit the brief after the first working version.
- Update the Not-now list. Don't quietly let it shrink.

## When to ask the user, and what

Ask only questions whose answers change the design. Ask at most three at a time, after showing what you would do by default:
- Who is it for, if two plausible audiences would lead to different products?
- What is the one thing it must do brilliantly, if the request lists many equal priorities?
- What hard constraint applies: platform, deadline, budget, regulation, or an existing system to fit?

Never ask about something you can decide with a sensible default and state.

## Anti-patterns

| Pattern | Why it fails | Instead |
|---|---|---|
| Starting with the tech stack | The technology starts shaping the product | Write the first-use story first |
| Copying a competitor's feature list | You inherit their complexity and none of their reasons | List what's broken in the category (innovation.md) |
| The "minimum" in MVP is applied to quality, not scope | A broad, mediocre v1 teaches users it's mediocre | Narrow scope, high quality |
| Personas made of demographics | Demographics don't decide design | Moments, needs, current alternatives |
| A setting for every disagreement | Pushes product decisions onto users | Decide, set a default, revisit with evidence |
| No Not-now list | Nothing was decided, so everything creeps back | Keep the list with reasons, and review it |

See `examples.md` for complete briefs.
