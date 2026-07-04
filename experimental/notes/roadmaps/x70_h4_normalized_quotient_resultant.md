# X70: h=4 normalized quotient-resultant reduction

- **DAG node:** `x70_h4_normalized_quotient_resultant`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved certifier reduction.
- **Verifier:** `experimental/scripts/verify_x70_h4_normalized_quotient_resultant.py`.
- **Certificate:**
  `experimental/data/certificates/x70-h4-normalized-quotient-resultant/x70_h4_normalized_quotient_resultant.json`.

## Statement

After X69, every primitive h=4 norm-gate certifier key has a normalized
representative

```text
f_{r,s}(X) = X + X^r - X^s - 1.
```

Every such word has the universal factor `X-1`:

```text
f_{r,s}(X) = (X - 1) q_{r,s}(X),     q_{r,s} in Z[X].
```

For `n = 2^m`, the cyclotomic polynomial satisfies

```text
Phi_n(1) = 2.
```

Therefore

```text
Res(Phi_n, f_{r,s}) = +/- 2 * Res(Phi_n, q_{r,s}).
```

Since any row with `mu_n` and `n > 1` has odd characteristic, the
p-specific norm-gate condition is equivalent to

```text
p | Res(Phi_n, q_{r,s}).
```

Thus the primitive h=4 sparse-resultant certifier may work with the quotient
word `q_{r,s}` instead of the original normalized word.

## Proof

The identity `f_{r,s}(1)=0` is immediate:

```text
1 + 1 - 1 - 1 = 0.
```

Hence `X-1` divides `f_{r,s}` in `Z[X]`.  Resultants are multiplicative in
the second argument, so

```text
Res(Phi_n, f_{r,s})
  = Res(Phi_n, X-1) * Res(Phi_n, q_{r,s}).
```

Up to the harmless sign convention for resultants,

```text
Res(Phi_n, X-1) = Phi_n(1).
```

For a 2-power row, `Phi_n(X) = X^{n/2} + 1` for `n >= 4`, and the checked
campaign rows all have `n >= 16`; in any case the absolute value of the
factor is `2`.  Since `n | q-1`, the characteristic cannot be `2`.  Thus the
removed factor never contributes a row prime.

## Replay

The verifier recomputes all normalized X69 representatives in the X60 replay
rows, divides each corresponding polynomial by `X-1`, and checks exact
reconstruction in `Z[X]`.

```text
row                  normalized representatives
------------------------------------------------
low_n16_p17          82
low_n64_p193         596
boundary_n64_p7937   100
boundary_n128_p17921 52
boundary_n256_p91393 100
```

All row characteristics are odd; the removed resultant factor is `2`; and no
replay normalized representative is the diagonal `r=s` branch where the
quotient would be constant.

## Consequence

The h=4 primitive certifier pipeline is now:

```text
X68 key
  -> X69 normalized representative (1,r,s)
  -> X70 quotient q_{r,s} = (X + X^r - X^s - 1)/(X-1)
  -> test p | Res(Phi_n, q_{r,s})
  -> expand surviving keys by X65 row-count representatives.
```

This removes a universal factor before any sparse-resultant computation and
prevents the certifier from spending work on a prime-safe `X-1` component.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x70_h4_normalized_quotient_resultant.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x70_h4_normalized_quotient_resultant.py --write-certificate
```
