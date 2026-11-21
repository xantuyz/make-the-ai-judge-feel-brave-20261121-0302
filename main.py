"""Entry for make.fun: Make the AI judge feel brave (2026-11-21).

Writes a single 237-character text to entry.txt in the output directory.
Deterministic, stdlib only, no network, no randomness.

The text is a single scene: a ferry leaving the landing. The bravery
comes from the scene itself -- a rope lifted, a strip of river opening --
not from any instruction to the reader.
"""

import os

SENTENCES = (
    "The ferry rests against a tire at the landing.",
    "The woman at the tiller finishes her pear and sets the core in a tin.",
    "She lifts the rope from its post.",
    "A narrow strip of river opens between boat and shore, "
    "wide enough now to hold the sky.",
)

TEXT = " ".join(SENTENCES)


def build_entry() -> str:
    """Return the entry text, enforcing the competition's length rule."""
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(TEXT)}")
    return TEXT


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
