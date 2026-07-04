# X25: h=5 finite prime-window sweep

- **DAG node:** `x25_h5_prime_window`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite evidence.
- **Verifier:** `experimental/scripts/verify_x25_h5_prime_window.py`.
- **Certificate:**
  `experimental/data/certificates/x25-h5-prime-window/x25_h5_prime_window.json`.

## Scope

X24 proves that characteristic-zero dyadic trades are empty when `h` is not a
power of two.  The first campaign-relevant odd size is:

```text
h = 5.
```

X25 tests whether finite-characteristic reductions create h=5 same-top-four
collisions in the first full boundary windows:

```text
n=16: all primes p == 1 mod n with n^2 < p <= n^3
n=32: all primes p == 1 mod n with n^2 < p <= n^3
```

The scan is exact and low-memory.  It stops at `n=32`; a full `n=64` h=5
all-prime sweep is much heavier and should remain a separate task if needed.

## Result

No same-top-four h=5 collisions occur in either full window:

```text
family       primes swept       p range             collision rows
------------------------------------------------------------------
n=16             61             257..4049           0
n=32            212             1153..32609         0
```

Thus the h=5 characteristic-zero emptiness persists through the first two
finite boundary windows.

## Interpretation

This is finite evidence, not a theorem.  It supports the current terminal-node
split:

```text
power-of-two h:      finite-p reductions of cyclic full-fiber trades;
non-power h:         no reductions seen so far at h=5.
```

Together with X15, this says h=5 is raw-injective across the checked rows and
across the full `n=16,32` prime windows.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x25_h5_prime_window.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x25_h5_prime_window.py --write-certificate
```

Current replay: **9 PASS, 0 FAIL**.
