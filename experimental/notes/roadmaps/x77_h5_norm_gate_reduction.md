# X77: h=5 norm-gate reduction

- **DAG node:** `x77_h5_norm_gate_reduction`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved reduction plus finite evidence.
- **Verifier:** `experimental/scripts/verify_x77_h5_norm_gate_reduction.py`.
- **Certificate:**
  `experimental/data/certificates/x77-h5-norm-gate-reduction/x77_h5_norm_gate_reduction.json`.

## Statement

For h=5 on a 2-power row, any finite-field same-top-four trade is a
first-level p-specific sparse norm-gate event.

In the checked h=5 scopes, no such events occur:

```text
n=16,32: all primes p == 1 mod n with n^2 < p <= n^3;
n=32,64: selected first-prime rows from alpha=2 through alpha=3.
```

## Proof

X24 proves the characteristic-zero dyadic classification:

```text
if h is not a power of two, no characteristic-zero trade exists.
```

In particular, characteristic-zero h=5 trades are empty.

X30 proves the finite-p dichotomy for the signed first-sum word:

```text
finite-p trade = dyadic descent branch or p-specific norm gate.
```

The descent branch requires both supports to be antipodal unions.  This is
impossible for h=5 because an antipodal union has even cardinality.  Therefore
every finite h=5 trade must trigger the top-level sparse norm gate:

```text
p | Res(Phi_n, f),
```

where

```text
f(X) = sum_{a in P} X^a - sum_{b in Q} X^b
```

is the signed `5+5` first-sum word.

This is a reduction, not a uniform exclusion theorem.  The landed finite
evidence then says the reduced object is empty in the checked scopes.

## Replay

The verifier checks:

- X30 records h=5 as non-antipodal;
- X25 has no collision rows in the full `n=16,32` prime windows;
- X15 has no collision rows in the selected `n=32,64` rows through
  `alpha=3`.

```text
full window      primes swept       p range        collision rows
-----------------------------------------------------------------
n=16             61                 257..4049      0
n=32             212                1153..32609    0

selected rows    n=32,64 through alpha=3           0
```

## Consequence

The h=5 terminal branch has no descent/paid ambiguity: it is either empty or
first-level p-specific norm-gate mass.  Existing exact finite windows are
empty.  A uniform proof still needs to exclude or bound these signed `5+5`
norm-gate events; this packet only fixes the branch shape and records the
checked emptiness.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x77_h5_norm_gate_reduction.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x77_h5_norm_gate_reduction.py --write-certificate
```
