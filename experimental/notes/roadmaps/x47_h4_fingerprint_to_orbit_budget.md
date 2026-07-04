# X47: h=4 fingerprint sweeps in orbit-budget currency

- **DAG node:** `x47_h4_fingerprint_to_orbit_budget`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved bridge plus certificate replay.
- **Verifier:** `experimental/scripts/verify_x47_h4_fingerprint_to_orbit_budget.py`.
- **Certificate:**
  `experimental/data/certificates/x47-h4-fingerprint-to-orbit-budget/x47_h4_fingerprint_to_orbit_budget.json`.

## Statement

For a fixed h=4 row, suppose every anchored active pair is one of the paid
fingerprints:

```text
mu_4 full fiber,
antipodal h=2 quotient lift.
```

Then the row has no positive canonical non-descended h=4 top-level orbit.
Consequently the h=4 top-level branch is zero in X46's orbit-budget currency,
and hence is safely inside the rewired terminal `n^3` column.

## Proof

X32 splits h=4 active pairs into:

```text
paid antipodal quotient branch
or
top-level non-descended sparse norm-gate branch.
```

The `mu_4` full-fiber family and the antipodal h=2 quotient-lift family are
paid.  Therefore any top-level non-descended pair is non-fingerprinted.

Conversely, if a positive canonical non-descended orbit existed, X33 gives a
Galois scaling of that exponent pattern whose h=4 common-gcd gate is positive,
so it is an actual top-three h=4 trade.  A common exponent translation anchors
one positive support element at `1`; translation preserves top-three equality
and paid/non-descended status.  Thus the orbit would produce an anchored
non-fingerprinted active pair.

So:

```text
zero non-fingerprinted active pairs
  => zero positive canonical non-descended h=4 orbits.
```

X46 then gives top-level mass

```text
n^2 * 0 = 0 <= n^3.
```

## Certificate Replay

The verifier replays the landed finite h=4 certificates in this new currency:

- X21: exact full windows for `n=16` and `n=32`;
- X22: exact full window for `n=64`;
- X20: selected `n=32,64,128` power rows.

Every row has zero non-fingerprinted active pairs, so every row has zero
positive canonical non-descended top-level orbits.

This does not prove the uniform h=4 theorem for all `n,p`.  It converts the
existing finite evidence into the stronger X46 target and validates that the
new orbit-budget formulation agrees with the earlier fingerprint formulation.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x47_h4_fingerprint_to_orbit_budget.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x47_h4_fingerprint_to_orbit_budget.py --write-certificate
```
