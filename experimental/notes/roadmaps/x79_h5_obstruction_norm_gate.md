# X79: h=5 obstruction norm gate

- **DAG node:** `x79_h5_obstruction_norm_gate`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved h=5 p-specific obstruction gate.
- **Verifier:** `experimental/scripts/verify_x79_h5_obstruction_norm_gate.py`.
- **Certificate:**
  `experimental/data/certificates/x79-h5-obstruction-norm-gate/x79_h5_obstruction_norm_gate.json`.

## Statement

Let `n=2^s`, `H=mu_n`, and let `R` be a 10-subset of `H`.  Write

```text
C_R(X) = prod_{r in R} (X-r).
```

There is at most one monic degree-five polynomial `S_R` whose square agrees
with `C_R` in degrees `10,9,...,5`.  It is obtained recursively from those
high coefficients.  Define the obstruction polynomial

```text
E_R(X) = S_R(X)^2 - C_R(X).
```

By construction,

```text
deg E_R <= 4.
```

For an odd row prime `p`, the support `R` can underlie a finite-field h=5
same-top-four trade only if the four low obstruction coefficients vanish in
the row field:

```text
[X^i]E_R = 0,        i=1,2,3,4,
```

and the constant coefficient `[X^0]E_R` is a nonzero square.  Equivalently,
the h=5 residue is gated by four simultaneous low-coefficient obstructions,
not merely by the first-sum norm gate.

After clearing the powers of two introduced by the recursive square-root
formula, the following p-specific norm statement holds.  If a row prime
`p == 1 mod n`, `p` odd, realizes `R` as an h=5 trade, then `p` divides the
cyclotomic norm of every nonzero cleared obstruction coefficient.

## Proof

Let

```text
C_R(X) = X^10 + c_9 X^9 + ... + c_0
```

and seek

```text
S_R(X) = X^5 + s_4 X^4 + ... + s_0.
```

Matching the coefficient of `X^9` gives

```text
2s_4 = c_9.
```

Then matching `X^8` determines `s_3`, matching `X^7` determines `s_2`, and so
on down to `X^5`, because at each step the new unknown appears linearly with
coefficient `2`.  Since row primes are odd, this recursion is valid in every
row field.  Over characteristic zero it is valid after adjoining powers of
`1/2`.

Once `S_R` is forced, the identity

```text
C_R + lambda = S_R^2
```

is equivalent to saying that the coefficients of `X^1,...,X^4` in
`E_R=S_R^2-C_R` vanish; then `lambda=[X^0]E_R`.

By X78, this square-shift condition with nonzero square `lambda` is equivalent
to a disjoint h=5 same-top-four split of `R`, unique up to swapping sides.
Thus the finite-field criterion follows.

For the norm gate, view `R` first over `K=Q(zeta_n)`.  The forced root
coefficients have only powers of two in their denominators.  In degree five,
the recursion gives `S_R` coefficients in `2^-9 O_K`, so squaring shows that
`2^18` safely clears the low obstruction coefficients:

```text
2^18 [X^i]E_R,        i=1,2,3,4
```

are cyclotomic integers.  If an odd row prime realizes the support, each
cleared obstruction maps to zero in the chosen prime of `O_K` over `p`.
Therefore `p` divides its field norm.  X24 rules out characteristic-zero h=5
trades, so not all four obstruction coefficients can vanish over `K`; every
finite h=5 trade is therefore genuinely p-specific.

## Consequence

X77 said h=5 finite trades are first-level p-specific sparse norm-gate events.
X79 sharpens the gate:

```text
first-sum norm gate
  -> square-shift support
  -> four simultaneous low-coefficient obstruction norms.
```

This is a better target for the terminal proof than raw h=5 pair enumeration.
It also exposes the next exact certifier shape: for each 10-support, compute
the forced high-coefficient square root once, clear denominators, and test the
gcd of the four obstruction norms against the official row prime.

## Replay

The verifier checks the algebra on constructed examples and then applies the
finite-field obstruction gate to small rows:

```text
F17 / mu16
F97 / mu16
F257 / mu16
```

All `8008` ten-supports in each sanity row are rejected by a nonzero low
obstruction coefficient; there are no square-lambda survivors.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x79_h5_obstruction_norm_gate.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x79_h5_obstruction_norm_gate.py --write-certificate
```
