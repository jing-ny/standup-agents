# Tutorial 03 — Grow your own panel

*Do this after you have 2–3 real show records. This is the tutorial that makes
the template worth more than a notes app — and it cannot be done for you.*

## Why the stock panel is wrong about you

The panel ships knowing comedy theory: structure, truth+pain, economy. What it
doesn't know is *you* — your voice, your language, your scene, and above all
**your rooms**. Every comic eventually learns rules that are true for them and
nobody else: material that kills at a bar mic dies in a theater; a persona detail
that charms one crowd reads as bragging to another; a kind of opener that theory
loves but your mouth can't deliver.

The stock panel can't know these. Your show records do.

## 1. Mine your disagreements

Open every file in `material/shows/`. You're hunting for exactly two patterns:

- **Paper said yes, room said no.** Bits or beats the panel graded well that got
  silence. What do they have in common? (Too clever? Too much setup? A persona
  the room couldn't place? Vocabulary that works on the page but not in your
  mouth?)
- **Paper said meh, room said yes.** Lines that outperformed their grade. What's
  the shared engine? (A physical act-out? A specific kind of self-reveal? The
  moment you drop into another voice?)

Ask Claude to sweep the records with you — it's good at spotting repetition
across files. The *interpretation* is yours: you were in the room; it wasn't.

## 2. Write your first gate

A **gate** is a veto rule the panel applies on top of its four lenses. It has
three parts: a name, the evidence, and what it does to a grade. Append it to the
bottom of `agents/panel.md` under "Personal gates":

```markdown
1. **<short name>.** <What to flag.> Evidence: <show record(s) and what
   happened>. Effect: <caps the grade at X / demands a named fix / direction
   note only>.
```

Rules of thumb for good gates:

- **One gate = one real pattern**, backed by at least two performances. A single
  bad night is noise; twice is a lane marker.
- Gates about **your rooms** are usually the most valuable. Rooms differ more
  than theory admits — a quiet listening room and a loud bar room punish
  opposite things. If your scene has distinct room types, name them and note
  which material belongs where.
- Gates can be positive: "reward X, it has outperformed its paper grade twice."
- Date every gate. You will retire some later, and that's healthy.

## 3. Recalibrate and re-run

With gates in place, re-run `/panel` on your active bits. Grades will move —
some down (a gate tripped), some up (a positive gate recognized an engine the
theory lenses undervalued). Every moved grade should trace to a gate, and every
gate to a show record. Nothing in your vault is now an opinion without a chain
of custody back to a real audience.

## 4. Keep the flywheel turning

From here the loop is: perform → record the result → note disagreements → every
few shows, revisit the gates. Retire gates that stop matching; sharpen ones that
keep firing. Twice a year, reread the oldest gates — the performer who wrote
them was a worse comic than you are now.

That's the whole system. The template gave you an empty instrument;
your audience just tuned it.
