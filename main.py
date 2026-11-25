#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — a make.fun entry.

Running this script writes the one-line honest appliance error message to
/output/entry.txt. The output is fully deterministic: the exact same line is
produced on every run, with no network, no randomness, no clock and no
environment input beyond the output directory.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Check that the entry is one non-blank line of 1-200 characters.

    Exits with a non-zero status and a loud error message if the line is
    empty, spans multiple lines, or is over the limit, so a bad line can
    never ship unnoticed.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


# The entry itself: one fixed line, 154 characters, no trailing newline.
# An espresso machine, deadpan, reporting the truth of its fault: the descale
# is 214 days overdue, it has brewed 1,842 cups through solid limescale, the
# espresso now crunches — and the limescale has a name.
LINE = ("ERROR E09: Descale overdue 214 days. I have brewed 1,842 cups "
        "through solid limescale. Your espresso now crunches. The limescale "
        "has a name. It is Gerald.")


def main() -> None:
    # Validate first, then write the line to entry.txt.
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # No trailing newline: the file is exactly the 154-byte line, so the
        # Size tie-break counts the line itself and nothing else.
        f.write(LINE)


if __name__ == "__main__":
    main()
