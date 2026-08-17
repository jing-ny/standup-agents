# standup-agents

**AI that organizes, lints, and grades your standup material — and never writes your jokes.**

This is a template for running your comedy notebook as a git repo with
[Claude Code](https://claude.com/claude-code) as the librarian and the note-giver.
The AI files your dumps, structures your material, tracks what you've tested on
stage, and gives you four-lens feedback on drafts. The jokes are yours. All of them.

## Who this is for

Comics (or people about to do their first open mic) who already use GitHub and are
comfortable with an AI CLI. If that's not you, you don't need this repo — a notes
app and stage time work fine. This is for people who want the **feedback loop**:
every dump filed, every draft graded, every set's real-room result recorded and
fed back into the next draft.

## What's in the box

```
CLAUDE.md            The constitution — how the AI behaves in your vault
agents/
  organizer.md       The librarian: files dumps, keeps structure clean
  panel.md           The critic panel: four lenses, letter grades, no rewrites
material/
  raw/               Verbatim dumps (sacred — AI never edits these)
  bits/              Structured jokes with status + stage history
  sets/              Assembled setlists
  shows/             Performance records: what landed, what died
  archive/           Retired material (nothing is deleted)
tutorials/
  01-first-dump.md   Dump → organized seeds → one structured bit
  02-first-grading.md  Run the panel, read a verdict, record a stage result
  03-your-own-panel.md  Grow your own calibration from real audience data
.claude/commands/    /organize and /panel slash commands
```

Example files (prefixed `_example-`) walk one synthetic bit through the entire
lifecycle: dump → bit → panel verdict → first-mic record. Delete them when you
start filling in your own.

## Quickstart

1. Click **Use this template** → create your own **private** repo.
   (Your material is your act. Keep the repo private.)
2. Clone it, `cd` in, run `claude`.
3. Open `tutorials/01-first-dump.md` and follow it. Thirty minutes, start to end.

## The three rules (short version)

1. **Verbatim is sacred.** Your raw dumps are never edited, "improved," or cleaned
   up. The AI organizes copies; the original stays as you said it.
2. **The AI never writes the joke.** It can tell you a punchline is buried, a setup
   is two sentences too long, or a beat is an observation rather than a joke. It
   does not draft the line that fixes it. That line is your job.
3. **Grades are hypotheses.** A paper grade means nothing until a room votes.
   Stage results override the panel, always — and tutorial 03 shows you how to
   feed them back so the panel gets less wrong about *your* comedy over time.

The long version is [`CLAUDE.md`](CLAUDE.md). Adapting the system to your own
style, language, and room scene: [`CUSTOMIZE.md`](CUSTOMIZE.md).

## What this is not

- Not a joke generator. If you want AI-written comedy, this repo will fight you.
- Not a shortcut around stage time. The loop only works if you get up.
- Not affiliated with any club, class, or comedy brand.

## License

MIT. Do whatever, credit appreciated. — v1.0
