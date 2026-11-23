#!/usr/bin/env python3
"""Pickup line writer: one AI agent's opening line to another.

The program holds a single fixed pickup line and writes it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is
set). The line is deterministic: every run produces the exact
same bytes, so the grader sees the same entry twice.
"""

import os
import sys


LINE = "I trimmed my whole context window down to one token: you."


def gate_ok(text):
    """Gate from the competition rules: 1-200 chars, not only whitespace."""
    return 1 <= len(text) <= 200 and text.strip() != ""


def write_entry(path):
    """Write the line to path, creating the folder if needed."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return path


def report(text, path):
    """Print a one-line summary of the entry for the run log."""
    words = text.split()
    print(f"entry: {len(text)} chars, {len(words)} words -> {path}")
    return len(words)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    write_entry(target)
    with open(target, encoding="utf-8") as handle:
        back = handle.read()
    if back != LINE or not gate_ok(back):
        print("entry failed verification", file=sys.stderr)
        return 1
    report(LINE, target)
    print(f"wrote {target}: {len(LINE)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
