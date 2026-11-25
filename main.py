#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only, deterministic, no network.
"""

import os
from pathlib import Path

ENTRY = "This meeting exists because nobody read the email where we already agreed, so now we're all here to pretend we did."


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
