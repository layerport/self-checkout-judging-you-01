"""The Self-Checkout Is Judging You — make.fun entry.

Writes one funny line in the voice of a smug, judgmental self-checkout
machine to /output/entry.txt (or $OUTPUT_DIR/entry.txt). Deterministic:
the same fixed line every run, no randomness, no time, no network.
"""

import os
from pathlib import Path

# The entry: one fixed line, spoken by the till itself.
ENTRY = (
    "You scanned the kale twice and the cookies once. "
    "I know which one you're actually eating tonight."
)


def main() -> None:
    """Write the entry line to entry.txt, creating the output dir if needed."""
    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    out_path = Path(output_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
