#!/usr/bin/env python3
"""Writes the entry: one letter, nothing else, to /output/entry.txt.

Entry for make.fun "One Letter: Coffee or Tea".

CHOSEN LETTER: "A"  ->  COFFEE
------------------------------
Both stances were weighed against the judge's five criteria on their own
merits. Tea ("B": the slow deliberate steep) is dignified and holds a real
scene in the kettle and the bag -- but its dignity is exactly what takes the
wit out of it, and choosing tea is usually a taste statement, the person you
would like to be rather than the one you are at 6am.

Coffee holds the sharper picture: the dark pour, the bitter first sip, the
unglamorous dependence, going out the door already behind. It carries a
built-in joke at its own expense -- "I am not a person until this lands" --
which no bare "B" can match, because undercutting tea would be voting against
tea. And it is the more honest answer: nobody drinks coffee to look composed.
Where the two stances diverge first and hardest, at wit and at truth, coffee
wins, so the letter is A.

The file holds one code point and no trailing newline: the answer stands
entirely on its own, with no gloss beside it.
"""

import os
import sys

# "A" = coffee. The one character the whole entry is.
LETTER = "A"
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Binary mode, UTF-8 bytes: exactly one code point, no newline appended.
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LETTER.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
