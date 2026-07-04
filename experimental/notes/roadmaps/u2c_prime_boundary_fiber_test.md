# U2C-PRIME: boundary fiber-test falsifier

- **DAG:** `u2c_boundary_scale_column`.
- **Task:** U2C-PRIME.
- **Status:** toy falsifier negative for the X-8 boundary construction.
- **Verifier:** `experimental/scripts/verify_u2c_prime_boundary_fiber_test.py`.
- **Certificate:**
  `experimental/data/certificates/u2c-prime-boundary-fiber-test/u2c_prime_boundary_fiber_test.json`.

## Question

The original U2-C giant-regime dictionary charged full 2-power cosets only at
scales `M > t`.  X-8 found boundary examples at `M = t`: if `n=tR` and
`S` is an antipodal-free zero-sum subset of the quotient row `mu_R`, then

```text
B_S = { x in mu_n : x^t in S }
```

is `t`-null.  The old classifier calls this primitive because it is not a
union of any larger `M > t` cosets.  The repaired residual dichotomy should
classify it as charged because it is a union of `M=t` fibers.

This verifier tests exactly that classifier boundary.

## Toy Rows

Both rows are deliberately in the pigeonhole-visible regime:

```text
q < 2^(R/2).
```

The checked rows are:

```text
F_257 / mu_128,  t=M=4, R=32
F_257 / mu_256,  t=M=8, R=32
```

For each row, the verifier enumerates all `2^16` antipodal-free quotient
patterns, finds every zero-sum pattern, lifts it to `mu_n`, and checks:

```text
1. the lifted block is t-null by exact power sums r=1..t;
2. the old M>t fiber classifier rejects it;
3. the repaired M>=t classifier accepts it, with minimal M=t.
```

## Result

Both rows find exactly `256` zero-sum boundary patterns.

```text
row                    zero-sum patterns   old M>t hits   repaired minimal M
F257_mu128_t4_R32      256                 0              4
F257_mu256_t8_R32      256                 0              8
```

So the X-8 constructed family is not a primitive residue after the repair.  It
is exactly the boundary-scale column the DAG node names.

## Honest Residual

This does **not** prove U2-C' for arbitrary `t`-null blocks.  It only closes
the specific residual-dichotomy falsifier that the X-8 construction produced:

```text
old dictionary:      false negative at M=t;
repaired dictionary: charged at M=t.
```

The remaining structural statement is still:

```text
every t-null block is a union of mu_M-cosets for some M >= t, including the
boundary zero-sum clause, or else an actually primitive residue exists.
```

## Verification

Run:

```bash
python3 experimental/scripts/verify_u2c_prime_boundary_fiber_test.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_u2c_prime_boundary_fiber_test.py --write-certificate
```

Current replay: **27 PASS, 0 FAIL**; peak RSS under `/usr/bin/time -v` was
`24972 KB`, with no swaps.
