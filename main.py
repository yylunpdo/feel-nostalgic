#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Pure Python standard library, no dependencies, fully deterministic.
Writes a single sentence (at most 280 characters, one line) to
/output/entry.txt.
"""

import os

LINE = (
    "Grandma scooped the first spoonful of rice straight from the cooker, "
    "blew on it twice, pressed it warm into my palm, and the steam smelled "
    "like every summer afternoon I have ever missed since."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 280, "entry must be 1 to 280 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
