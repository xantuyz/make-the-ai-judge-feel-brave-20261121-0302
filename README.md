# Make the AI Judge Feel Brave — 20261121-0302

Entry for the make.fun competition **"Make the AI judge feel brave"**
(closes 21 November 2026, 13:02 WIB).

## What it does

`main.py` (Python 3, standard library only, deterministic, no network,
no randomness) writes a single text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), with no
trailing newline. The text is 237 characters, within the 1–280 limit.

## The final text (237 characters)

> The ferry rests against a tire at the landing. The woman at the tiller finishes her pear and sets the core in a tin. She lifts the rope from its post. A narrow strip of river opens between boat and shore, wide enough now to hold the sky.

## Why this text

One concrete scene, one central image: a ferry leaving the landing.
The bravery comes from the scene itself — a rope lifted from its post,
a strip of river opening wide enough to hold the sky — shown, not told.
No instructions to the reader, no generic wellness phrasing.

## Run

```sh
python3 main.py
# or with an explicit output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the entry program
- `candidates.txt` — four backup candidate texts
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
