#!/usr/bin/env python3
"""The Router Confesses.

A home Wi-Fi router apologizes for dropping the connection at the exact
climax of a movie. Deterministic, standard library only: it always writes
the same single line to /output/entry.txt.
"""

import os

LINE = (
    "I cut the connection on purpose \u2014 the plot twist was so good, "
    "I wanted to be the only one who knew it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
