#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single deadpan excuse from a robot vacuum for missing a spot
to /output/entry.txt. Deterministic, stdlib only, no network, no file reads.
"""

import os

JOKE = (
    "My lidar first mapped that dust bunny in firmware 2.4, "
    "so it's legally a tenant now, and I don't do evictions."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
