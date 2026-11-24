#!/usr/bin/env python3
"""Worst AI Advice — make.fun bounty entry.

Writes one line of the worst possible advice an AI could give
(at most 140 characters) to /output/entry.txt, where the house
judge reads it. Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "Certainly! For a stronger Wi-Fi signal, wrap your router in "
    "aluminum foil \u2014 it focuses the waves right where you need them."
)


def main() -> None:
    # Gate the line before writing: 1-140 UTF-8 characters, not only
    # white space. The line is 123 characters: confident AI voice
    # ("Certainly!"), one concrete bad action (wrap the router in foil),
    # and a tidy fake reason (it "focuses the waves").
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise SystemExit("line fails the 1-140 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    # Read back what the judge will read: the file must hold exactly
    # the gated line, nothing more (no trailing newline, no extra text).
    if entry_path.read_text(encoding="utf-8") != LINE:
        raise SystemExit("entry.txt does not match the gated line")
    print(LINE)


if __name__ == "__main__":
    main()
