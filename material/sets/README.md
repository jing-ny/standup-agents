# sets/

Assembled setlists: an ordered run of bits with timing, transitions, and a
plan for when things go wrong. A set file references bits; it doesn't copy
their text — one source of truth per joke.

## The one hard rule

**Transitions and save lines are performable content.** They come out of your
mouth on stage, which puts them under the same constitutional protection as
punchlines: these two sections hold **the performer's words only**. The AI may
tell you "bit 2 → bit 3 has no bridge" or "nothing protects the risky opener" —
it may never draft the line that fixes it. (Cutting and reordering bits, by
contrast, is structure — the AI can and should propose those.)

## Template

```markdown
---
title:
target_minutes: 5
room:                 # optional: material/rooms/<slug>.md you're building this for
status: assembling    # assembling / stage-ready / retired
tested_in: []
---

# <title>

## Running order
| # | bit | est. time | why here |
|---|-----|-----------|----------|
| 1 | material/bits/<slug>.md | 2:30 | strongest opener, fast first laugh |

## Transitions
(performer's words only — how you get from each bit to the next)

## Save lines
(performer's words only — what you say when a planned laugh doesn't come)

## Emergency cuts
(ordered: if you're running long, what goes first, second, third —
cuts and reorders are fair game for AI proposals)

## History
(assembly decisions, rehearsal timings, and panel verdicts — append, never
overwrite)
```

## Timing

Estimating `est. time` per bit before you've performed it:

- **English:** spoken standup runs ~130–150 words per minute. Word count ÷ 140
  is a fine first guess. This is a *starting point* — your first recording
  replaces it with your real rate.
- **Other languages:** the wpm rule is English-specific (Chinese counts
  characters per minute, and every language paces differently). Record
  yourself performing one bit, divide, and that's your personal baseline.
  See `CUSTOMIZE.md` on languages.
- **Rehearsal beats arithmetic:** time the full set out loud three times and
  **keep the slowest run**. Then leave room for laughs — a set that fills the
  slot exactly in a silent bedroom runs over in a laughing room. The light
  doesn't care that you were doing well.

**Off-book standard** — a set (or bit) is stage-ready when all three hold:

1. Three clean runs out loud without looking at the page.
2. You can drop a line, notice, and keep going without restarting.
3. The spoken version is *shorter* than the page version (your mouth has
   already made its cuts — see tutorial 02 on rehearse-on-tape).

## Grading a set

`/panel material/sets/<file>.md` judges the set *as a set* — opener choice,
callback graph across bits, energy ordering, closer type — not each bit again.
Same grade scale as bits, same `(untested)` rule. A set earns **S** only when
the whole thing has run in that order on a real stage with a show record to
prove it.

`_example-*` files are synthetic — delete when you start your own.
