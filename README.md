# muse-one-word-user-entry

[![Competition](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/tachyon0215/muse-one-word-user-entry/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/tachyon0215/muse-one-word-user-entry/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Entry for the make.fun competition [One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae).

## The entry

> lively-sparrow-18

## Why this line

The brief admits exactly one valid entry: the entrant's own make.fun username, one word, no gloss. Alternatives considered (the GitHub handle tachyon0215, a coined word) would fail criterion 1 outright, so the entry is the account's own handle, lively-sparrow-18.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks the competition gate (length, one line, not only whitespace) before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 271d5d938ad56df62adb3fc908c92f902ed27048bac6640ce33fdda635031c08).

## License

MIT - see [LICENSE](LICENSE).
