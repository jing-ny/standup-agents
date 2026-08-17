# Tutorial 00 — From zero: GitHub, Claude Code, and your first conversation

*For people who've never used a terminal-based AI tool or barely touched GitHub.
One-time setup, 20–30 minutes. If you already have Claude Code running and a
cloned repo, skip straight to tutorial 01.*

## What you need

- A **GitHub account** (free) — [github.com/signup](https://github.com/signup)
- A **Claude subscription** (Pro or above) — Claude Code runs on it
- A Mac, Windows, or Linux computer. Everything happens on your machine;
  your material lives in files you own.

## 1. Get your own copy of this repo

1. On this repo's GitHub page, click the green **Use this template** button →
   **Create a new repository**.
2. Name it whatever you like (`my-standup` works). Set visibility to
   **Private** — your material is your act.
3. That's it. You now have your own vault on GitHub; this template stays behind.

## 2. Install the tools

1. **Claude Code** — follow the install instructions at
   [claude.com/claude-code](https://claude.com/claude-code) for your OS.
2. **Git** — Macs have it preinstalled (open Terminal, type `git --version`;
   if it prompts to install developer tools, accept). On Windows, install
   [git-scm.com](https://git-scm.com) with default options.

## 3. Clone your repo (get it onto your computer)

Open Terminal (Mac: Spotlight → "Terminal") and run, replacing both names:

```
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

Git may pop a browser window to log in to GitHub the first time. If anything
goes wrong here, don't debug alone — finish step 4 first, then paste the error
message to Claude. Fixing git problems is genuinely one of the things it's best at.

## 4. Start your first conversation

Inside the repo folder, run:

```
claude
```

You're in. Claude Code automatically reads this vault's `CLAUDE.md` — the
constitution that tells it what it may and may not do with your material —
so it already knows the house rules before you say a word.

(Using Codex or another agent CLI instead? Same deal: those tools auto-read
`AGENTS.md`, which binds them to the same constitution. Everything in these
tutorials works — just say the slash commands in your own words.)

## 5. The mental model (read this twice)

**You talk. It types.** You don't need to create files, remember folder names,
or write the frontmatter headers you'll see in the other tutorials. Those
tutorials show manual paths so you know *where things live* — but in practice
you just say what you want:

> "I just got back from a mic. Here's my voice memo transcript: … File it as a
> raw dump."

> "Show me every bit I haven't performed yet."

> "Commit everything with a sensible message."

Three more things:

- **Slash commands are saved prompts.** `/organize` and `/panel` are shortcuts
  this template ships with (they live in `.claude/commands/` — plain text,
  go read them). Typing the request in your own words works too.
- **Everything is a file.** Nothing is hidden in an app. Open the folder in
  any editor and it's all just text you own.
- **Commits are save points.** Ask Claude to commit whenever you finish a
  session; ask it to push so GitHub has your backup. If you ever mess
  something up, tell Claude what happened — git means almost nothing is
  truly lost.

## 6. Try one round trip

Say to Claude:

> "Walk me through tutorial 01 with a dump I'll give you now."

…and rant for two minutes about something that annoyed you this week.
It will take it from there — filing verbatim, listing the seeds it hears,
and asking you which one to build. That's the loop. Welcome in.
