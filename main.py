#!/usr/bin/env python3
"""The Router Confesses.

A home Wi-Fi router apologizes for dropping the connection at the exact
climax of a movie. Deterministic, standard library only: it always writes
the same single line to /output/entry.txt.
"""

import os

LINE = (
    "I dropped you on purpose \u2014 the plot twist was so good, "
    "I decided to be the only one who knew it."
)


def main() -> None:
    # Enforce the entry contract before writing: one line, 1-200 chars.
    if not (1 <= len(LINE) <= 200) or "\n" in LINE:
        raise ValueError("entry line must be a single line of 1-200 chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
