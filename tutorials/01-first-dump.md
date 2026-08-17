# Tutorial 01 — Your first dump, organized

*Thirty minutes. By the end you'll have one raw dump filed forever and one
structured bit started — and you'll have seen exactly where the AI's job stops
and yours begins.*

> **You don't have to do any of the file operations below by hand.** Everything —
> creating files, writing frontmatter, changing statuses, committing — can be
> done by telling Claude what you want in plain English ("file this as a raw
> dump", "mark the allen key bit stage-ready", "commit"). The manual paths are
> shown so you know where things live and can check its work. New to Claude Code
> entirely? Start at `tutorials/00-setup.md`.

## 1. Dump

Talk for two minutes about something that **annoyed, scared, confused, or
embarrassed you this week**. Not "something funny" — strong feeling first, funny
is downstream of it. Don't edit. Typos, tangents, half-thoughts — all of it stays.

**Voice first, if you can.** Spoken dumps are looser and funnier than typed ones —
your mouth doesn't self-censor the way your fingers do. Three ways to get the
transcript:

- **Your phone already does it.** Recent iPhones and Androids transcribe voice
  memos automatically — record, copy the transcript out, paste it to Claude.
- **Type the rant** if recording isn't your thing. Still don't edit.
- **`scripts/transcribe.py`** (optional, needs an OpenAI API key) — drop the
  audio file in the repo folder and say *"transcribe this and file it as a raw
  dump."* Audio itself never enters git (see `.gitignore`); only the verbatim
  transcript does — mishears flagged, never silently fixed.

Easiest path: paste the transcript into Claude Code and say **"file this as a
raw dump."** It will create `material/raw/<date>-<two-word-slug>.md` with the
right frontmatter and your text untouched. (Doing it by hand? The shape is:)

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

When the file has a premise and a rough performable draft, tell Claude to mark
it `working` and commit — or do it yourself:

```
git add material/ && git commit -m "First dump + first working bit"
```

## What just happened

You did the writing. The AI did the filing, the listening, and the questions.
Next: find out what a four-lens critic thinks — `tutorials/02-first-grading.md`.
