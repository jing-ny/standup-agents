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

## Grading a set

`/panel material/sets/<file>.md` judges the set *as a set* — opener choice,
callback graph across bits, energy ordering, closer type — not each bit again.
Same grade scale as bits, same `(untested)` rule. A set earns **S** only when
the whole thing has run in that order on a real stage with a show record to
prove it.

`_example-*` files are synthetic — delete when you start your own.
