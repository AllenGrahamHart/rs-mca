# X21: h=4 prime sweep

- **DAG node:** `x21_h4_prime_sweep`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite evidence.
- **Verifier:** `experimental/scripts/verify_x21_h4_prime_sweep.py`.
- **Certificate:**
  `experimental/data/certificates/x21-h4-prime-sweep/x21_h4_prime_sweep.json`.

## Scope

X20 identified two h=4 cyclic fingerprints:

```text
mu4_full_fiber
antipodal_h2_quotient_lift
```

This packet tests whether exceptional-prime behavior creates any h=4
primitive residue when the prime varies.

The sweep covers:

```text
n=16: all primes p == 1 mod n with n^2 < p <= n^3
n=32: all primes p == 1 mod n with n^2 < p <= n^3
n=64: first 25 primes p == 1 mod n above n^2
```

The `n=64` row is intentionally bounded: it is only a boundary sample, not an
exhaustive window.  It is included because it is the first size where the
antipodal quotient-lift exception appears in the prime sweep.

## Result

No swept row has a non-fingerprinted h=4 active pair.

```text
family        primes swept      antipodal primes        primitive/other rows
---------------------------------------------------------------------------
n=16              61            none                    0
n=32             212            none                    0
n=64              25            4993, 7937, 10177       0
```

Every swept prime has the persistent `mu4_full_fiber` family:

```text
count = n/4 - 1
```

The `n=64` exceptional primes add twelve paid antipodal quotient lifts each.
Thus the boundary-prime phenomenon is real, but it remains in the cyclic
pullback ledger.

## Interpretation

This strengthens the h=4 terminal picture:

```text
h=4 primitive residue observed so far: 0
h=4 exceptional-prime residue observed so far: paid antipodal h=2 quotient lift
```

So the useful uniform statement is not "h=4 is always empty".  The correct
classification target is:

```text
Every h=4 active pair is either a mu_4 full-fiber trade or an antipodal
h=2 quotient lift, hence cyclic-pullback paid.
```

X21 does not prove that statement.  It rules out a cheap exceptional-prime
falsifier at the small exact windows above and gives the proof route a more
accurate second family.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x21_h4_prime_sweep.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x21_h4_prime_sweep.py --write-certificate
```

Current replay: **19 PASS, 0 FAIL**.
