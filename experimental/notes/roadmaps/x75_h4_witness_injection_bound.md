# X75: h=4 witness-injection bound

- **DAG node:** `x75_h4_witness_injection_bound`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved h=4 strengthening.
- **Verifier:** `experimental/scripts/verify_x75_h4_witness_injection_bound.py`.
- **Certificate:**
  `experimental/data/certificates/x75-h4-witness-injection-bound/x75_h4_witness_injection_bound.json`.

## Statement

The primitive h=4 norm-gate residue in X65 canonical-orbit currency satisfies

```text
# primitive h=4 canonical row orbits
  <= 2 phi(n)(n-1)
  = n(n-1)
  < n^2.
```

This strengthens X74 by removing the extra key-to-row `phi(n)` loss.

## Proof

Let `(a,b,c)` be a primitive X64 canonical row orbit representative satisfying
the h=4 linear norm-gate equation

```text
zeta^a + zeta^b - zeta^c - 1 = 0.
```

Since the content is one and `n` is a power of two, some X64 transform of the
orbit has odd first coordinate.  Choose a deterministic one, say the
lexicographically first transform

```text
(d,e,g)
```

with `d` odd.  Let `u=d^{-1} mod n` and normalize:

```text
(1,r,s) = (u d, u e, u g).
```

The normalized word

```text
X + X^r - X^s - 1
```

vanishes at the primitive root `zeta^d`, because

```text
(zeta^d) + (zeta^d)^r - (zeta^d)^s - 1
  = zeta^d + zeta^e - zeta^g - 1.
```

By X71, after the universal `X-1` strip the quotient is

```text
q(X) = 1 + eps * (X^A + X^(A+1) + ... + X^(A+ell-1)).
```

For a fixed primitive-root exponent `d`, sign `eps`, and length `ell`,
the equation `q(zeta^d)=0` forces the interval start `A` if it exists:

```text
(zeta^d)^A
  = - (1-zeta^d) / (eps * (1-(zeta^d)^ell)).
```

The denominator is nonzero because `1 <= ell <= n-1` and `zeta^d` is
primitive.  Hence there is at most one normalized interval for each witness

```text
(d, eps, ell).
```

There are `phi(n)` choices for `d`, two choices for `eps`, and at most `n-1`
choices for `ell`.

Finally, the deterministic normalization is injective on X64 canonical row
orbits.  Given `(d, eps, ell)`, the forced start reconstructs the normalized
pair `(1,r,s)`.  Multiplying exponents by `d` reconstructs the transformed
triple `(d,e,g)`, and its X64 canonical orbit is unique.

Therefore

```text
# primitive h=4 canonical row orbits <= 2 phi(n)(n-1).
```

For `n=2^s`, `phi(n)=n/2`, so this is `n(n-1)<n^2`.

## Replay

The verifier constructs the deterministic witness for every replay primitive
X64 canonical row orbit, checks that the witness is realized in the row, and
checks injectivity.

```text
row                  primitive orbits   witness bound   n^2
-------------------------------------------------------------
low_n16_p17          20                 240             256
low_n64_p193         134                4032            4096
boundary_n64_p7937   23                 4032            4096
boundary_n128_p17921 12                 16256           16384
boundary_n256_p91393 22                 65280           65536
```

The replay rows are much smaller than the bound, but the proof is uniform.

## Consequence

The h=4 primitive finite-p norm-gate branch now has an `O(n^2)` bound in X65
canonical-orbit currency, improving X74's `O(n^3)` key-count route.  This is
still h=4-specific; the full terminal node remains open for larger trade
sizes and for the final split-pair assembly.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x75_h4_witness_injection_bound.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x75_h4_witness_injection_bound.py --write-certificate
```
