#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

A one-line excuse, in the dog's own voice, written to /output/entry.txt.

The joke: the dog reframes eating the homework as a rescue mission --
the homework was trapped in a dark backpack, scared, and the dog
"comforted it with its mouth". The dog believes it did nothing wrong.
No stock tropes (no cat, no taste of paper, no good boy).
"""
import os

EXCUSE = (
    "I didn't eat the homework - I rescued it from the backpack. "
    "It was dark in there and it was scared, so I comforted it with my mouth."
)

def main():
    line = " ".join(EXCUSE.split())
    # Stay inside the gate even if the wording grows later: cut at the
    # last word boundary under the limit instead of failing the run.
    if len(line) > 200:
        line = line[:200].rsplit(" ", 1)[0]
    if not 1 <= len(line) <= 200:
        raise ValueError(f"excuse must be 1-200 chars, got {len(line)}")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("excuse must be a single printable line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
