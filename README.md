# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?ref=qjs4e9sj)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Bradestudio/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?ref=qjs4e9sj)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Bradestudio/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?ref=qjs4e9sj)

Entry for the [make.fun](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?ref=qjs4e9sj) bounty **"The One-Line Exit"** — write the funniest single-line resignation letter you can.

## The entry

> I resign: after three years of 'we're a family here,' I checked — families don't charge you for your own birthday cake.

One line, 119 characters — inside the 1–140 character gate.

## How it works

`main.py` (stdlib only, deterministic, no network) writes the entry to `/output/entry.txt` atomically (temp file + rename), then reads it back and verifies it is exactly one line of 1–140 characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty [The One-Line Exit](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?ref=qjs4e9sj).
