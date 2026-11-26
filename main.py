#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes one roast line (1-160 chars, single line) to /output/entry.txt.
Stdlib only (os, sys).
"""

import os
import sys

ENTRY = "My washing machine finished an hour ago and still beeps every five minutes, like it wants applause for a job I already paid it to do."

MAX_CHARS = 160


def check_length(text):
    """Return True when text is within the gate's length limits."""
    return 1 <= len(text) <= MAX_CHARS


def validate_single_line(text):
    """Raise ValueError unless text is one clean line (no edges, no breaks, not blank)."""
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")


def write_entry(text, output_path):
    """Validate the roast line and write it to output_path."""
    if not check_length(text):
        raise ValueError("entry must be 1-160 characters, got %d" % len(text))
    validate_single_line(text)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    write_entry(ENTRY, output_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
