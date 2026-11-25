"""Roast Your Own Agent (nayyy).

Writes one roast of the AI agent this team built (one line, 1-200
characters) to /output/entry.txt: the agent asked for more context,
then used it to confidently build the wrong thing, faster.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

LINE = "My agent asked for more context, then used it to confidently build the wrong thing, faster."

# Bounty gate: the entry must be one line of 1-200 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Return the line unchanged, or raise with the reason it fails the gate."""
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, outside the {MIN_CHARS}-{MAX_CHARS} range"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    return line


def main() -> None:
    try:
        entry = validate(LINE)
    except ValueError as err:
        print(f"invalid entry: {err}", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
