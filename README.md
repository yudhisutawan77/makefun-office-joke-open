# Make the AI Judge Laugh: the Office Joke Open

[![make.fun](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/yudhisutawan77/makefun-office-joke-open/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/yudhisutawan77/makefun-office-joke-open/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

One line of office comedy, written for the
[make.fun bounty](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232):
a judge model reads the jokes two at a time and keeps the funnier one.
The funniest joke takes the whole $2 reward; entry is free.

## The joke

> After three years, my calendar finally showed one free hour, so my manager booked it for a meeting titled 'Why don't you ever have free time?'

142 characters, one line. The setup is a small, specific office win — a
free hour after three years — and the punchline spends it on the exact
meeting that proves why the free hour never existed.

## How it works

`main.py` (Python 3, standard library only) validates the joke against
the gate — one line, 1 to 200 characters, UTF-8, not blank — then writes
it to `/output/entry.txt` with no trailing newline, so the file holds
exactly the joke, and prints it to stdout.

```sh
python3 main.py
```

Set `ENTRY_OUT` to write somewhere else, or `ENTRY_OUT_DIR` to change
the output directory (default `/output`).

## License

MIT — see [LICENSE](LICENSE).
