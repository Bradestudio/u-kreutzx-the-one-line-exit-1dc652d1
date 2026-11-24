# SPDX-License-Identifier: MIT
"""The One-Line Exit — writes one funny one-line resignation letter.

Stdlib only, deterministic, no network. Writes the entry to
/output/entry.txt atomically (temp file + rename) and reads it back
to verify it is exactly one line of 1-140 characters.
"""

import os
import sys

ENTRY = (
    "I resign: after three years of 'we're a family here,' I checked \u2014 "
    "families don't charge you for your own birthday cake."
)

MAX_CHARS = 140


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 for ch in text):
        print("error: entry contains control characters", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, target)

    # Read-back verification: exactly one line, within the gate.
    with open(target, "r", encoding="utf-8") as f:
        back = f.read()
    lines = back.splitlines()
    if len(lines) != 1 or lines[0] != text:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if not 1 <= len(lines[0]) <= MAX_CHARS:
        print("error: read-back length out of gate", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(lines[0]), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
