# Tutorial 01 — Your first dump, organized

*Thirty minutes. By the end you'll have one raw dump filed forever and one
structured bit started — and you'll have seen exactly where the AI's job stops
and yours begins.*

## 1. Dump

Talk for two minutes about something that **annoyed, scared, confused, or
embarrassed you this week**. Not "something funny" — strong feeling first, funny
is downstream of it. Use your phone's voice memo and transcribe it, or just type
a rant. Don't edit. Typos, tangents, half-thoughts — all of it stays.

Save it as `material/raw/<date>-<two-word-slug>.md`:

```markdown
---
date: 2026-01-10
source: voice-memo
---
(your verbatim rant here)
```

> Peek at `material/raw/_example-2026-01-10-ikea-dump.md` to see what "unedited"
> really means. It's not pretty. That's the point.

## 2. Organize

In Claude Code, run:

```
/organize material/raw/<your-file>.md
```

The AI will list the comedic **seeds** it hears — each one a quote from *your own
words* plus a note on the emotion underneath. It will not polish anything.
It will probably find seeds you didn't notice you'd said. That's the whole
value of dumping before judging.

## 3. Pick one seed — you, not the AI

The organizer lists; you choose. Pick the seed that still has heat when you
reread it. Tell Claude to open a bit file for it, and it will scaffold
`material/bits/<slug>.md` with your phrasing carried over verbatim and
`🤖`-marked questions where structure is missing:

- What's the **premise** — the absurd truth this exposes?
- What does the audience expect (setup), and where does that expectation
  break (punch)?
- Which moment could be **acted out** instead of narrated?

## 4. Answer the questions in your own words

Type answers under the 🤖 questions. Delete the markers as you answer — unmarked
text means *yours*. If a question makes you write something that sounds like an
essay, say it out loud first, then type what you actually said.

When the file has a premise and a rough performable draft, change `status: idea`
to `status: working`. Commit:

```
git add material/ && git commit -m "First dump + first working bit"
```

## What just happened

You did the writing. The AI did the filing, the listening, and the questions.
Next: find out what a four-lens critic thinks — `tutorials/02-first-grading.md`.
