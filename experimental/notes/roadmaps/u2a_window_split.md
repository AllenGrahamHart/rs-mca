# U2-A: moment/PTE window split

- **DAG nodes:** `x4b_moment_trade_exclusion`, `u2_per_row_certifier`.
- **Task:** U2-A.
- **Status:** PROVED arithmetic / window packet.
- **Verifier:** `experimental/scripts/verify_u2a_window_split.py`.
- **Certificate:**
  `experimental/data/certificates/u2a-window-split/u2a_window_split.json`.

## Convention

The dangerous small-block window is the frozen W3 v1 grammar window:

```text
t < b <= floor(log2 n)^2.
```

The older F2 empirical window

```text
t < b <= 2t + 4
```

is carried only as a comparison column.  P-B found toy residuals beyond
`2t+4`, so U2-B should consume the full grammar window.

## Base-Row Windows

For the three Row-C-class rows (`n=1024`, `floor(log2 n)^2 = 100`), U2-B's
base-row cells are:

```text
RowC rate 1/4:  t=5,  b=6..100   (95 cells)
RowC rate 1/8:  t=5,  b=6..100   (95 cells)
RowC rate 1/16: t=3,  b=4..100   (97 cells)
```

The older F2 windows are:

```text
t=5: b=6..14
t=3: b=4..10
```

So the full grammar adds `86`, `86`, and `90` extra Row-C cells beyond the
old F2 cap.

For all three prize rows, `n=2^41` and `floor(log2 n)^2 = 1681`, while

```text
t = 2^33 + 1   at rates 1/4 and 1/8,
t = 2^32 + 1   at rate 1/16.
```

Thus the prize base-row small window is empty.

## Giant-Regime Parameters

The prize rows enter U2-C directly:

```text
prize 1/4:  b_min = 8589934594, max disjoint (t+1)-blocks = 255,
            first charged coset M = 2^34, scale n/M = 128
prize 1/8:  same as prize 1/4
prize 1/16: b_min = 4294967298, max disjoint (t+1)-blocks = 511,
            first charged coset M = 2^33, scale n/M = 256
```

Complement duality reduces the block-size range to `b <= n/2` in all three
rows.

## Transported Quotient Rows

The verifier emits TR/per-leaf windows for the QA.22 transported quotient-row
table.  For transported rows, the U2 depth is the inherited `tail_b`, while the
quotient-local

```text
t_q = floor(A/M) - floor(k/M)
```

is recorded separately and is usually zero in the staircase table.

Live inherited-tail transported cells occur only on Row-C-class rows:

```text
RowC 1/4, t=5:  N=128 b=6..49; N=64 b=6..36; N=32 b=6..25;
                N=16 b=6..16; N=8 b=6..9
RowC 1/8, t=5:  same transported windows as RowC 1/4
RowC 1/16,t=3:  N=256 b=4..64; N=128 b=4..49; N=64 b=4..36;
                N=32 b=4..25; N=16 b=4..16
```

All prize transported inherited-tail windows are empty, because the inherited
tail depth is still much larger than `floor(log2 N)^2`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_u2a_window_split.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_u2a_window_split.py --write-certificate
```
