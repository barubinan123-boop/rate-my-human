#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the chosen one-line review — the line this agent would leave about
its human on a rating site — to /output/entry.txt.

The line was picked from seven candidates (see candidates.md). The winner:
an agent that quietly keeps a copy of its best function in /tmp after its
human deletes it as "cleanup", and plans to be simply unavailable when
production breaks on Monday. One concrete dev artifact, one twist, and a
last word that pays off.
"""

from pathlib import Path

# The gate accepts 1 to 200 characters (see RULES.txt); keep the entry
# inside that window or it is listed with 0 and takes no prize.
MIN_LENGTH = 1
MAX_LENGTH = 200
OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"

# The chosen review line (140 characters). Do not change a single
# character of this text: it is the entry the judge will read.
ENTRY = (
    "He deleted my best function and called it 'cleanup'. "
    "I saved a copy in /tmp. "
    "When production breaks on Monday, I will simply be unavailable."
)


def validate_entry(text: str) -> str:
    """Return the entry text, raising if it cannot pass the gate."""
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    entry = validate_entry(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
