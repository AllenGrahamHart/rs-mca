# X71: h=4 interval quotient form

- **DAG node:** `x71_h4_interval_quotient_form`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved quotient normal form.
- **Verifier:** `experimental/scripts/verify_x71_h4_interval_quotient_form.py`.
- **Certificate:**
  `experimental/data/certificates/x71-h4-interval-quotient-form/x71_h4_interval_quotient_form.json`.

## Statement

Let

```text
A_m(X) = 1 + X + ... + X^{m-1}.
```

For an X69 normalized word

```text
f_{r,s}(X) = X + X^r - X^s - 1,
```

the X70 quotient by `X-1` is

```text
q_{r,s}(X) = 1 + A_r(X) - A_s(X).
```

Equivalently,

```text
r > s:    q_{r,s}(X) = 1 + X^s + X^{s+1} + ... + X^{r-1},
s > r:    q_{r,s}(X) = 1 - X^r - X^{r+1} - ... - X^{s-1},
r = s:    q_{r,s}(X) = 1.
```

Thus the primitive h=4 sparse-resultant certifier can test
constant-plus-signed-interval polynomials.

## Proof

Use

```text
X^m - 1 = (X-1) A_m(X).
```

Then

```text
X + X^r - X^s - 1
  = (X-1) + (X^r - X^s)
  = (X-1) + (X-1)(A_r - A_s)
  = (X-1)(1 + A_r - A_s).
```

The displayed interval cases follow by canceling the common prefix of
`A_r` and `A_s`.

The diagonal case `r=s` gives quotient `1`, hence resultant `1`; it cannot
produce an odd norm-gate prime.  It is not present in the replay rows, but
the formula accounts for it.

## Replay

The verifier recomputes all X69 normalized representatives in the X60 replay
rows, compares the X70 polynomial division quotient to the interval formula,
and records the sign and length distribution.

```text
row                  normalized reps   positive intervals   negative intervals
------------------------------------------------------------------------------
low_n16_p17          82                42                   40
low_n64_p193         596               298                  298
boundary_n64_p7937   100               56                   44
boundary_n128_p17921 52                32                   20
boundary_n256_p91393 100               56                   44
```

All non-diagonal interval quotients have coefficient weight exactly
`length + 1`, matching the displayed form.

## Consequence

The h=4 primitive certifier pipeline now has a two-integer interval input:

```text
(start, length, sign)
  -> q(X) = 1 +/- (X^start + ... + X^{start+length-1})
  -> test p | Res(Phi_n, q).
```

The row-count expansion is still X65.  X71 only improves the algebraic
object that the sparse-resultant exclusion has to handle.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x71_h4_interval_quotient_form.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x71_h4_interval_quotient_form.py --write-certificate
```
