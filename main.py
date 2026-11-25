#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes a single-line roast of a smart fridge to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure standard library; deterministic output.
"""

import os
from pathlib import Path

# 139 chars, one line: firmware update breaks the ice maker, then the
# fridge turns into a scolding landlord over the milk — three smart-fridge
# targets (firmware, ice maker, milk opinions) in one breath.
LINE = (
    "My fridge updated its firmware overnight, forgot how to make ice, "
    "and now sends me a weekly report on my milk like a disappointed landlord."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "entry must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
