#!/usr/bin/env python3
"""Transcribe an audio file with the OpenAI Whisper API.

Usage:
    python3 scripts/transcribe.py path/to/recording.m4a

Setup (once):
    pip install openai
    export OPENAI_API_KEY=sk-...   # or put it in your shell profile

Prints the transcript to stdout. Typical use inside Claude Code:
    "Transcribe material/audio/mic-night.m4a and file it as a raw dump."

Notes:
- Audio files are gitignored on purpose: recordings of live rooms contain other
  comics' material and audience voices. The audio stays local; the verbatim
  transcript of YOUR words is what enters the vault.
- The transcript goes into material/raw/ exactly as transcribed — mishears and
  all. Flag suspected mishears in a note section; never silently "fix" them.
"""
import sys

try:
    from openai import OpenAI
except ImportError:
    sys.exit("Missing dependency: pip install openai")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/transcribe.py <audio-file>")
    with open(sys.argv[1], "rb") as f:
        result = OpenAI().audio.transcriptions.create(model="whisper-1", file=f)
    print(result.text)


if __name__ == "__main__":
    main()
