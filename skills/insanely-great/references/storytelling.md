# Storytelling: positioning, naming, and presentation

Use this for READMEs, landing pages, launch posts, release notes, pitches, demos, and product names. The test of the story is the same as the test of the product: it must be clear, specific, and true.

## One concrete line

The iPod was announced with "1,000 songs in your pocket" (IPOD01). That line works for three reasons:
- **Concrete:** you can picture it and count it.
- **A result, not a spec:** it doesn't say "5 GB hard drive", but it implies it.
- **Repeatable:** a customer can say it to a friend.

To write yours:
1. Write ten candidate lines. Strike every one that would fit a competitor equally well.
2. Prefer a measurable or visual result ("deploys in 30 seconds", "every receipt in one place") over an adjective ("powerful", "seamless", "next-generation").
3. Read it to someone outside the field. If they can't repeat it back, try again.

## Open with the problem

The iPhone presentation spent its opening on what was wrong with the smartphones people already carried, before showing anything new (IPH07). Use this structure for any launch, README, or demo:

1. **The problem.** One or two sentences the audience already feels.
2. **Why existing options fall short.** Be specific and fair, and never sneer.
3. **The one line.**
4. **Show it working.** A live demo, a short clip, a three-line quickstart, a before-and-after.
5. **The few things it does brilliantly.** Three, not twenty. Then point to the depth (advanced features, API, integrations) in a line, so experts know it's there.
6. **How to get it.** One step if possible.
7. **Honest limits.** What it doesn't do yet.

## Values and specifics

"To me, marketing is about values" (TD97). In that talk Jobs used Nike as his example: its ads honor athletes instead of describing air soles.

The lesson is to say what you stand for and who it's for. Don't drown the message in specifications. Two balances keep this from becoming vague:
- **For technical audiences, the right specs are benefits:** cold-start time, binary size, the number of steps. State them precisely and tie each one to the experience it improves.
- **Values must be visible in the product.** A claim of "simple" is checked by the reader's first five minutes.

## Demos

- **Demo the hero path, live where possible, at real speed.**
- **Rehearse the exact path.** Know where it can fail and keep a fallback.
- **Show the moment of value early.** Don't spend the first minutes on setup or settings.
- **One idea per demo segment.** Name it, show it, move on.
- **For written docs:** a screenshot or GIF of the result, then the shortest command or code that produces it.

## Naming

- One plain, memorable name per concept, used everywhere: UI, docs, API, support.
- Name the product for what people get or can picture. Avoid internal codenames and stacked jargon.
- Check the name for conflicts and trademarks, and for unwanted meanings in other languages and markets.
- Version names and numbers should tell users whether an update matters to them.

## README and landing page skeleton

```
# Name
One concrete line.

<image or 10-second demo of the result>

## Why
The problem in 2 sentences; what's wrong with the usual approach.

## Quickstart
The shortest path to first value (copy-paste).

## What it does well
Three things, each with a one-line example.

## Going further
The advanced capabilities, one line each, with links. Simple to start does not mean shallow.

## Limits
What it doesn't do (yet).

## Install / Docs / License
```

## Honesty

- **Every claim must be checkable.** Numbers need conditions ("on an M-series laptop, 10k files").
- **No "revolutionary", "the best", or "game-changing" without evidence.** Let the demo make the case.
- **Describe limits and known issues plainly.** Trust is part of the product.
- **When something goes wrong, say so and fix it for users.** Jobs opened the 2010 antenna press conference with "We're not perfect. Phones aren't perfect." Apple then gave every owner a free case (AG10). Defensive comparisons to competitors (also part of that event) persuade less than the fix does.

## Anti-patterns

| Pattern | Instead |
|---|---|
| Buzzword stacks ("AI-powered, cloud-native, seamless platform") | One concrete result |
| A feature dump as the first section | The problem, the line, then the demo |
| Claims without conditions | Numbers with their test setup |
| Hiding limits | A short, honest Limits section |
| Copying a famous brand's voice or slogans | Your product's own plain words |
