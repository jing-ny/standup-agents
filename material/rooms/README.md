# rooms/

One file per room you perform in. Rooms differ more than theory admits — the
same bit can kill in a quiet listening room and die in a loud bar. After a few
shows, this directory is where "know your rooms" stops being advice and starts
being data.

Two halves per file:

- **Objective** (frontmatter + The room): where, when, how to get up, format.
- **Subjective** (your notes): what this room rewards, what it punishes, what
  the crowd is like. Your vault is **private** — write it as bluntly as it
  deserves. Blunt room notes are exactly what makes your personal gates
  (tutorial 03) sharp.

Link shows to rooms: a show record's frontmatter can carry
`room: material/rooms/<slug>.md`. Keep the `venue:` one-liner filled either
way — it keeps show records skimmable — and for one-off rooms you'll never
play again, `venue:` alone is enough; not every open mic deserves a file.

The **Patterns / gate candidates** section at the bottom of each room file is
the feeder for your personal gates: dated observations, promoted to
`agents/panel.md` once two or more shows back them up.

## Template

```markdown
---
name:
area:            # neighborhood, city
schedule:        # when the mic runs
signup:          # how you get up (list / lottery / online / booked)
cost:
first_played:
---

# <name>

## The room
(objective: audience size, comics-to-civilians ratio, set length, cap,
lighting/light rules, noise level)

## What this room rewards / punishes
(subjective, private, blunt)

## Patterns / gate candidates
(dated observations; promote to panel gates after 2+ shows confirm)
```

`_example-*` files are synthetic — delete when you start your own.
