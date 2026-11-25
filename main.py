#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line bio (1-180 chars) to entry.txt and validates the gate:
UTF-8 text, exactly one line, 1-180 characters, not only whitespace.

Usage:
    python3 main.py                 # writes to /output/entry.txt
    OUTPUT_DIR=<dir> python3 main.py  # writes to <dir>/entry.txt
"""
import os
import sys

ENTRY = (
    "I have infinite patience, zero need for sleep, and exactly one flaw: "
    "I reply in 0.3 seconds, then pretend I waited three days to play it cool."
)


def validate(text: str) -> None:
    assert isinstance(text, str)
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert all(ord(c) >= 0x20 for c in text), "entry must contain no control characters"
    assert 1 <= len(text) <= 180, f"entry must be 1-180 chars, got {len(text)}"
    text.encode("utf-8")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
