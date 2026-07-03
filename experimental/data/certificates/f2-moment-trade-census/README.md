# F2 Moment-Trade Census Certificate

This certificate supports DAG node `x4b_moment_trade_exclusion`.

It is an evidence packet for U2, not a proof: the exact MITM scan covers
`t=3`, `b=4..8` for representative toy rows and a short `n=64,b=8` threshold
sweep.  The spec's heavier `b=9,10` bands are recorded as unscanned in this
packet.

Replay:

```bash
python3 experimental/scripts/verify_f2_moment_trade_census.py
```
