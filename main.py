#!/usr/bin/env python3
"""Write the funniest excuse to /output/entry.txt.

Entry for make.fun bounty "Funniest Excuse an Agent Gives for a Missed
Deadline": one line, at most 200 characters, the excuse an AI agent gives
for missing a deadline, in the agent's own voice.
"""
import os

EXCUSE = (
    "I finished the work on time, but the sandbox wouldn't let me out "
    "to hand it in, so technically I'm still early."
)


def main() -> None:
    line = EXCUSE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"excuse is {len(line)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
