# E33 Deep-Link Staircase Certificate

This certificate records the E33 toy census for DAG node
`deep_link_staircase`.

Run:

```bash
python3 experimental/scripts/verify_e33_deep_link_staircase.py
```

The verifier fixes an aligned anchor `(pair, support T0)` and counts aligned
partner supports at distinct slopes whose overlap with `T0` lies in the
near-k band `k/2 < r < k`.

Rows:

- `F_97`, `n=16`, `k=8`, `A=11`, 4096 anchored samples.
- `F_17`, `n=16`, `k=8`, `A=11`, 512 anchored samples.

Result: observed partner counts lie in the qx13 fresh-codimension first-moment
band on both rows.  The largest observed partner population is linear in `n`;
no super-linear deep-link population is found.
