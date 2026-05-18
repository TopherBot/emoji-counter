#!/usr/bin/env python3
"""emoji_counter.py

A tiny command‑line tool that counts emoji characters in a file or from STDIN.

Usage:
    python3 emoji_counter.py [path/to/file]
    # or pipe data into it
    cat file.txt | python3 emoji_counter.py
"""

import sys
import re
from collections import Counter

# Unicode ranges that cover the bulk of modern emojis.
EMOJI_PATTERN = re.compile(
    "[\U0001F600-\U0001F64F"   # Emoticons
    "\U0001F300-\U0001F5FF"    # Misc Symbols & Pictographs
    "\U0001F680-\U0001F6FF"    # Transport & Map
    "\U0002600-\U00026FF"      # Misc symbols
    "\U0002700-\U00027BF"      # Dingbats
    "\U0001F900-\U0001F9FF]"   # Supplemental Symbols & Pictographs
)

def read_input() -> str:
    """Read from a file path argument or STDIN if no argument is given."""
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except OSError as e:
            sys.stderr.write(f"Error opening {path}: {e}\n")
            sys.exit(1)
    else:
        # Read all of STDIN
        return sys.stdin.read()

def count_emojis(text: str) -> Counter:
    """Return a Counter mapping each emoji to its frequency in *text*."""
    matches = EMOJI_PATTERN.findall(text)
    return Counter(matches)

def main():
    text = read_input()
    emoji_counts = count_emojis(text)
    total = sum(emoji_counts.values())
    print(f"Total emojis found: {total}")
    if total:
        print("Breakdown by emoji:")
        for emo, cnt in emoji_counts.most_common():
            print(f"  {emo} : {cnt}")

if __name__ == "__main__":
    main()
