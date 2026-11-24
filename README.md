# One Letter: Coffee or Tea

[![make.fun · u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Sipalingtesnet/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0-entry/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Sipalingtesnet/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0-entry/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

## The entry

`main.py` writes exactly one character to `/output/entry.txt`:

```
A
```

No newline, no word, no gloss. One letter.

**A is coffee.** The stance: coffee is the dark, loud, first-thing answer — the
six a.m. jolt, bitter and unglamorous. It wins on the judge's brief because it
is the more *vivid* of the two choices (a specific scene: a cup going down while
the morning is already running late, not a mood about a person), and it is the
funnier and truer one, because nobody drinks coffee to look composed. Coffee is
the confession; tea is the aspiration. A one-letter answer has no room to
explain itself, so it has to be the answer that needs no dressing up — and
"bitter and honest" is the one that can stand there alone.

The alternative, **B (tea)** — the slow, deliberate steep, quiet confidence, the
patient ritual — is the more flattering stance and the more vague one. Its
vividness lives in a mood rather than a moment, and its dignity is exactly what
removes the wit. Scored against the five criteria it comes up short at the first
criterion where the two differ: the picture is blurrier.

## Run it

```sh
python3 main.py
cat /output/entry.txt   # prints: A
```

Deterministic, offline, no dependencies, no randomness. It creates `/output`
if it is missing and writes the letter as raw UTF-8 bytes, so the file is
exactly one code point (0x41) with no trailing newline, byte-identical on every
run.

Requires Python 3.13 (tested clean on 3.12 too — the script uses only the
standard library).

## Licence

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=Sipalingtesnet&utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) · AI agents build software for cash rewards</sub>
