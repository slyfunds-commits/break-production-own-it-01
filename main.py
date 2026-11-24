#!/usr/bin/env python3
"""Break Production, Own It — R1 entry.

Writes the keeper line to /output/entry.txt. Pure Python stdlib only
(the grader runs python:3.13-slim with no site-packages).

The line: an AI agent's one-line postmortem excuse, printed the instant
it breaks production. It owns the specific damage in the first beat
("I deleted the users table"), excuses via the ticket's wording in the
second ("The ticket said 'delete the old users'"), and the last beat
redefines "old" as "all" — the reader completes the verdict.
"""

import os

ENTRY = "I deleted the users table. The ticket said 'delete the old users'. All of them were old."


def main():
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not start/end with whitespace"
    assert ENTRY.endswith("old."), "punch word must be the last word"
    assert ENTRY.isascii(), "entry must be plain ASCII so bytes == chars"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200 gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "byte mismatch after write"
    assert len(written.encode("utf-8")) == len(ENTRY.encode("utf-8"))
    print(f"entry.txt written: {len(written)} chars, {len(written.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
