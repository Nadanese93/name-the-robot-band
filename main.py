#!/usr/bin/env python3
"""Write the robot-band entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

One line, no trailing newline, UTF-8. Runs from any cwd: the output
directory comes from the MAKEFUN_OUTPUT_DIR environment variable
(default /output); nothing here depends on the working directory.
"""

import os
from pathlib import Path

ENTRY = 'The Self-Checkouts \u2014 hit single "Unexpected Item in the Bagging Area"'


def verify(out_path: Path) -> int:
    """Read the written file back and confirm it is byte-identical to ENTRY.

    Returns 0 only when the on-disk bytes match ENTRY exactly and ENTRY
    contains no control characters (ord < 0x20); 1 otherwise.
    """
    for ch in ENTRY:
        if ord(ch) < 0x20:
            return 1
    if out_path.read_bytes() != ENTRY.encode("utf-8"):
        return 1
    return 0


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    return verify(out_path)


if __name__ == "__main__":
    raise SystemExit(main())
