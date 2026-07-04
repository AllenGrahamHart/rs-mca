# X72: h=4 interval X+1 strip

- **DAG node:** `x72_h4_interval_xplus_strip`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved certifier reduction.
- **Verifier:** `experimental/scripts/verify_x72_h4_interval_xplus_strip.py`.
- **Certificate:**
  `experimental/data/certificates/x72-h4-interval-xplus-strip/x72_h4_interval_xplus_strip.json`.

## Statement

After X71, each normalized h=4 quotient has the form

```text
q(X) = 1 + eps * (X^a + X^(a+1) + ... + X^(a+ell-1)),
eps in {+1,-1}.
```

Then

```text
q(-1) = 0
```

if and only if

```text
ell is odd,        eps * (-1)^a = -1.
```

In that parity-matched case,

```text
q(X) = (X+1) h(X)
```

with `h in Z[X]`.  For every 2-power row `n >= 4`,

```text
Phi_n(-1) = 2.
```

Since all rows with `mu_n` have odd characteristic, the `X+1` factor is
prime-safe:

```text
p | Res(Phi_n, q)        iff        p | Res(Phi_n, h).
```

Thus the primitive h=4 sparse-resultant certifier can strip `X+1` from exactly
the parity-matched interval keys.

## Proof

Evaluate the X71 interval at `-1`.  The alternating sum of `ell` consecutive
signs is zero when `ell` is even.  When `ell` is odd, it is `(-1)^a`.  Hence

```text
q(-1) =
  1,                         ell even,
  1 + eps * (-1)^a,           ell odd.
```

This vanishes exactly when `ell` is odd and `eps*(-1)^a=-1`.

If `q(-1)=0`, then `X+1` divides `q` in `Z[X]`.  Resultants are
multiplicative, so

```text
Res(Phi_n, q) = +/- Res(Phi_n, X+1) Res(Phi_n, h).
```

For `n=2^s >= 4`,

```text
Phi_n(X) = X^(n/2) + 1,
```

and `n/2` is even, so

```text
Res(Phi_n, X+1) = +/- Phi_n(-1) = +/- 2.
```

Odd row characteristic cannot divide this factor.

The strip flag is constant on each X68 certifier key.  Indeed, X70 has

```text
f(X) = (X-1)q(X),
```

so `q(-1)=0` iff the original four-term word `f` vanishes at `-1`.  X66/X67
show that X68 key operations send `f` to a signed monomial multiple of
`f(X^u)` with `u` odd.  At `X=-1`, this only multiplies the value by a
nonzero sign, because `(-1)^u=-1`.  Vanishing at `-1` is therefore key
invariant.

## Replay

The verifier recomputes all X69 normalized representatives in the X60 replay
rows, applies the X71 interval formula, checks the parity criterion, divides
the parity-matched cases by `X+1`, and verifies that the strip flag is
constant on every X68 key.

```text
row                  stripped keys   total keys   stripped normalized reps
---------------------------------------------------------------------------
low_n16_p17          6               19           22
low_n64_p193         39              133          152
boundary_n64_p7937   8               23           28
boundary_n128_p17921 2               12           8
boundary_n256_p91393 6               22           24
```

This is not a row-count compression.  It is a certifier-degree reduction for
the subset of X68 keys whose interval quotient has the parity-matched
`X+1` factor.

## Consequence

The h=4 primitive certifier pipeline now has two quotient stages:

```text
X+X^r-X^s-1
  -> divide by X-1 universally
  -> write q = 1 +/- interval
  -> if ell odd and eps*(-1)^a=-1, divide q by X+1
  -> test the remaining residual against Phi_n.
```

Surviving certifier keys still expand by X65 row-count currency.  X72 only
shrinks the polynomial whose cyclotomic resultant is tested.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x72_h4_interval_xplus_strip.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x72_h4_interval_xplus_strip.py --write-certificate
```
