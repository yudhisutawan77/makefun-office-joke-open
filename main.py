#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one line of office comedy (at most 200 characters) to
/output/entry.txt, or to the path named by ENTRY_OUT. Nothing else
is built or run: the writing is the whole contest.
"""

import os
import sys
from pathlib import Path

LIMIT = 200

JOKE = (
    "After three years, my calendar finally showed one free hour, "
    "so my manager booked it for a meeting titled "
    "'Why don't you ever have free time?'"
)


def checked(text):
    """Refuse anything the sealed gate would refuse, before writing."""
    problems = []
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if not text.strip():
        problems.append("entry must not be blank")
    if not 1 <= len(text) <= LIMIT:
        problems.append(f"entry is {len(text)} chars, limit is {LIMIT}")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry must be UTF-8 text")
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        raise SystemExit(1)
    return text


def output_path():
    """ENTRY_OUT wins; otherwise ENTRY_OUT_DIR/entry.txt, default /output."""
    direct = os.environ.get("ENTRY_OUT")
    if direct:
        return Path(direct)
    return Path(os.environ.get("ENTRY_OUT_DIR", "/output")) / "entry.txt"


def main():
    text = checked(JOKE.strip())
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
