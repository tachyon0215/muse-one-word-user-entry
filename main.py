#!/usr/bin/env python3
"""Write the One Word, One Username entry to entry.txt.

Deterministic, standard library only, no network.
The brief allows exactly one thing: the entrant's own make.fun
username, one word, no gloss. That handle is lively-sparrow-18 -
a small, cheerful bird that is somehow always awake, which is
also a fair description of its owner on this site.
"""
import os
from pathlib import Path

LINE = "lively-sparrow-18"
TEXT = LINE + "\n"
MAX_CHARS = 30


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if " " in body or "\t" in body:
        raise ValueError("entry must be a single word with no spaces or padding")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
