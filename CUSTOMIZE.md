# Making it yours

The template is deliberately generic. Everything valuable about your version
will come from three customizations — do them in this order, as they come up
naturally (don't do them on day one).

## 1. Your voice spec (after ~5 bits)

Once `material/bits/` has a handful of files, ask Claude to draft
`agents/voice.md` from your own material: how you actually talk, what you joke
about, what you never do. Mark it as a living document. The Voice/POV lens then
grades against *your* spec instead of "sounds like a comedian." Two rules:

- Build it from performed material, not from who you'd like to be on stage.
- Revisit after every 5–10 shows; early voice specs age fast.

## 2. Your personal gates (after 2–3 shows)

Covered in `tutorials/03-your-own-panel.md`. This is the highest-value
customization in the whole system — do not skip it.

## 3. Your language(s) and rooms

- **Language:** everything here works in any language. If you perform in more
  than one, note per bit which language it lives in — translation between
  comedy languages is re-anchoring (same premise, different cultural anchors),
  not word swapping, and deserves its own bit file.
- **Rooms:** if your scene has distinct room types (quiet listening rooms vs
  loud bar rooms, themed shows, language-specific mics), give recurring rooms a
  file in `material/rooms/` and link show records to them via the `room:` field.
  After a few entries, patterns of "this material belongs in that room type"
  appear — encode them as gates.

## Optional extras (only when the pain is real)

- **A lint script** that checks frontmatter consistency, once hand-checking
  annoys you. Keep it under `scripts/` and out of Claude's creative loop.
- **More agents** — a rehearsal timer, a set assembler, a mic-schedule tracker.
  One rule: every new agent obeys the Constitution. The AI never writes the joke.
- **Slash commands** for whatever you find yourself typing repeatedly —
  `.claude/commands/` files are just prompts; copy the two existing ones.

## What not to customize

The three rules in the README (verbatim sacred / AI never writes the joke /
grades are hypotheses) are load-bearing. Every failure mode this template
protects against — polished-but-dead material, AI-flavored voice, trusting
paper over rooms — comes back the moment one of them bends.
