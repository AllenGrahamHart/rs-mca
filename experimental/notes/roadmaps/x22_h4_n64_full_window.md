# X22: h=4 full n=64 prime-window sweep

- **DAG node:** `x22_h4_n64_full_window`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite evidence, medium-cost replay.
- **Verifier:** `experimental/scripts/verify_x22_h4_n64_full_window.py`.
- **Certificate:**
  `experimental/data/certificates/x22-h4-n64-full-window/x22_h4_n64_full_window.json`.

## Scope

X21 sampled the first 25 `n=64` boundary primes.  X22 completes the full
prime window:

```text
n = 64,
p == 1 mod 64,
64^2 < p <= 64^3.
```

There are exactly `693` such primes, from `4289` through `261761`.

The verifier is intentionally isolated from the fast X21 check because it
takes a few minutes.  It remains low-memory: each prime uses one h=4 signature
sort and then releases the table.

## Result

No prime in the full window has a primitive/non-fingerprinted h=4 active pair:

```text
nonfingerprinted rows = 0.
```

Every prime has the persistent `mu4_full_fiber` family with count

```text
n/4 - 1 = 15.
```

Exactly nine primes have the additional paid antipodal quotient-lift family:

```text
4993, 7937, 10177, 11329, 26177, 50177, 51137, 65537, 156353.
```

At each of those primes, the extra h=4 mass is already classified as an
`antipodal_h2_quotient_lift`, hence cyclic-pullback paid.

## Interpretation

This removes the first larger exceptional-prime warning for the h=4
classification route:

```text
full n=64 h=4 window: primitive residue 0.
```

The evidence now says the h=4 theorem should not assert raw injectivity.
It should assert the two-family paid classification:

```text
mu_4 full-fiber trades
antipodal h=2 quotient lifts
```

The second family appears at isolated primes, but it stays in the cyclic
ledger.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x22_h4_n64_full_window.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x22_h4_n64_full_window.py --write-certificate
```

Current replay: **7 PASS, 0 FAIL**.  The certificate-writing run took about
`361` seconds on the local machine.
