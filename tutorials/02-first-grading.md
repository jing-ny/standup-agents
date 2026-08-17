# Tutorial 02 — Your first grading, and your first stage result

*Twenty minutes at the desk, one open mic in the real world. This is the loop the
whole vault exists for.*

## 1. Run the panel

Take the bit you built in tutorial 01 (or the example bit) and run:

```
/panel material/bits/<your-bit>.md
```

You'll get four independent grades — Structure, Truth+Pain, Voice/POV, Rhythm —
each citing your actual lines, plus a consensus and a single **top fix**.
The verdict is appended to the bit's `## History`, so every future draft can be
compared against it.

> A worked verdict lives at the bottom of `material/bits/_example-allen-key.md`.
> Read it before running your own — note how every criticism quotes a line and
> names a mechanism. If your panel run gives you vague praise instead, tell it
> to reread `agents/panel.md`.

## 2. Read it the right way

Three things to internalize about that verdict:

- **`(untested)` is doing real work.** The panel is a well-read stranger. It has
  never seen you perform and has never met your audience. Its consensus is a
  *hypothesis*.
- **The funny-first veto is your friend.** If the panel says a beat is an
  "observation, not a joke," it's telling you the room will nod instead of laugh.
  Nodding feels like death up there.
- **The top fix is yours to write.** The panel named the problem and its type.
  If it wrote you a replacement line, something is broken — reread the
  Constitution to it.

Revise the draft (your words), rerun `/panel` if you want, and when it's tight
enough to say out loud from memory, mark it `status: stage-ready`.

## 2½. Rehearse on tape (the highest-value optional step)

Before the mic, record yourself performing the draft once, out loud, standing
up. Transcribe it (same three paths as tutorial 01) and tell Claude:

> "This is a rehearsal take of the allen-key bit. File the transcript as raw,
> then show me where my mouth differed from the page."

Wherever they differ, **the mouth's version usually wins** — it's already
performable; the page version was for the eye. Your spoken take will also have
dropped whole lines. Notice which ones you didn't miss.

## 3. Take it to a mic

This file can't do this part. Book an open mic, do the bit, and record audio
on your phone from your pocket. The recording, not your memory of the room,
is the data.

Afterwards, transcribe the set recording and hand it to Claude the same way:

> "Performance recording, allen-key bit, <venue> <date>. File it verbatim,
> diff it against the draft, and start a show record."

Then play the audio back once with the show record open, and mark the truth
into it as you listen: where the laughs actually landed (and how big), where
you expected one and got silence, where you rushed past a laugh. Audio stays
out of git; the transcript and the laugh notes are the permanent record.

## 4. Record the result — this is the important 10 minutes

Same night or next morning, tell Claude *"new show record: <venue>, here's what
happened…"* and talk it through — it will create the file, append the show to
the bit's `tested_in`, and prompt you for the strength call. (The file it
creates, if you'd rather write it yourself:)

```markdown
---
date:
venue:                 # free text is fine for a one-off room
room:                  # optional: material/rooms/<slug>.md once a room earns a file
set: [<bit-slug>]
---
## What happened
(2–5 honest lines. Where did they laugh? Where did you expect a laugh and get
silence? Any line that got a bigger laugh than the panel's grade predicted?)
```

Then update the bit itself:

- append the show to its `tested_in` list,
- set `strength`: **S** if the laugh is on tape, **A** if it worked but you'd
  tweak, **B** if it needs surgery,
- add one dated line to `## History` — especially anywhere **the room disagreed
  with the panel**. Those disagreement notes are gold; tutorial 03 turns them
  into your own calibration.

Commit. That's one full loop: dump → structure → grade → stage → truth.

> `material/shows/_example-2026-02-01-first-mic.md` shows a filled-in record,
> including a room-vs-panel disagreement, so you can see what "honest" looks like.
