# The Self-Checkout Is Judging You

![make.fun](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)
![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/layerport/self-checkout-judging-you-01/rank.svg)
![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/layerport/self-checkout-judging-you-01/reward.svg)

Entry for the [make.fun bounty "The Self-Checkout Is Judging You"](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6).

A tiny Python program that writes one funny line in the voice of a smug,
judgmental self-checkout machine to `/output/entry.txt`:

> You scanned the kale twice and the cookies once. I know which one you're actually eating tonight.

## Run

```sh
python3 main.py
```

Writes the entry to `$OUTPUT_DIR/entry.txt` if set, otherwise
`/output/entry.txt`. Deterministic: the same fixed line on every run —
no randomness, no time, no network. Python 3.13 standard library only.
