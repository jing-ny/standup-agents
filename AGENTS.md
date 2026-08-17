# Entry point for Codex and other agent CLIs

This vault's constitution lives in [`CLAUDE.md`](CLAUDE.md). Read it in full
before touching anything. Its rules bind **every** AI agent working in this
repo, whatever the tool — the filename is a Claude Code convention, not a
scope limit.

The short version you must not violate:

1. You organize, lint, question, grade, and track. **You never write the jokes.**
2. `material/raw/` is verbatim and append-only. AI-drafted text carries a
   leading `🤖`; unmarked text is the performer's and is never edited in place.
3. Grades are hypotheses until the stage votes; real-room results override paper.
4. Changes land via issues, branches, and PRs — never silent, never force-pushed.

Tool notes:

- The `/organize`, `/panel`, and `/setlist` slash commands in
  `.claude/commands/` are plain saved prompts. On tools without slash-command
  support, open those files and follow them, or let the performer ask in their
  own words ("run the panel on the allen-key bit", "what could I take to a
  5-minute mic?") — same thing.
- Agent specs live in `agents/` (`organizer.md`, `panel.md`). They are the
  source of truth; this file and the commands only point at them.
