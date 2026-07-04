# X46: h=4 top-level orbit budget

- **DAG node:** `x46_h4_top_level_orbit_budget`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved budget consequence of X45.
- **Verifier:** `experimental/scripts/verify_x46_h4_top_level_orbit_budget.py`.
- **Certificate:**
  `experimental/data/certificates/x46-h4-top-level-orbit-budget/x46_h4_top_level_orbit_budget.json`.

## Statement

Let `n=2^s`, `p == 1 mod n`, and consider ordered signed h=4 exponent pairs
`(P,Q)`.  Let the affine-swap group act by

```text
a -> u a + d,        u in (Z/nZ)^*, d in Z/nZ,
(P,Q) -> (Q,P).
```

This group has size

```text
2 n phi(n) = n^2.
```

By X45, the h=4 common-gcd degree is constant on each orbit.  The
`Phi_n`-descended paid status is invariant on the same orbits.  Therefore

```text
# top-level non-descended h=4 survivors
  <= n^2 * (# positive canonical non-descended affine orbits).
```

Consequently, if a row has at most `n` positive canonical non-descended h=4
orbits, then the entire h=4 top-level branch fits the rewired terminal column
`n^3`.  If it has none, the branch is empty.

## Proof

For `n=2^s`, `phi(n)=n/2`, so the affine-swap group has size

```text
2 * n * phi(n) = n^2.
```

X45 proves common-gcd invariance:

- translation multiplies each `E_r` by a monomial;
- unit dilation composes each `E_r` with `X^u` and permutes primitive roots;
- side swap multiplies each `E_r` by `-1`.

The same argument preserves the descended/paid branch from X32.  Translation
multiplies the first-sum signed word by a monomial, unit dilation applies a
cyclotomic automorphism, and side swap negates the word.  Thus
`Phi_n | f` is invariant.

Hence the h=4 top-level survivor property

```text
deg gcd(Phi_n,E_1,E_2,E_3) > 0
and Phi_n not dividing the first-sum word
```

is constant on affine-swap orbits.  Each canonical positive non-descended
orbit expands to at most the full group size, `n^2`, ordered signed pairs.
Summing over such orbits proves the displayed bound.

## Terminal Consequence

The terminal L3 column after W4 accepts `n^3` row-wise split-pair mass.  X46
turns the h=4 top-level branch into a canonical-orbit target:

```text
# positive canonical non-descended h=4 orbits <= n.
```

This is weaker than proving the branch empty, but strong enough for the
terminal budget.  Existing finite evidence is sharper: the checked h=4 rows
have zero primitive/non-fingerprinted residue after paid classes are removed.

## Replay

The verifier checks:

- `2 n phi(n) = n^2` for representative powers of two;
- descended/paid status invariance on h=4 examples;
- exact full anchored-pair accounting at `F_257 / mu_16`;
- sample `F_4993 / mu_32` canonical-orbit budgets without a full n=32 orbit
  census.

At `n=16`, the exact positive non-descended canonical-orbit count is zero, so
the expanded top-level mass is zero.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x46_h4_top_level_orbit_budget.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x46_h4_top_level_orbit_budget.py --write-certificate
```
