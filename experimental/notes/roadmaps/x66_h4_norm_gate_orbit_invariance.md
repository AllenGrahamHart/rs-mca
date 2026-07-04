# X66: h=4 norm-gate orbit invariance

- **DAG node:** `x66_h4_norm_gate_orbit_invariance`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved orbit-invariance lemma for the sparse norm-gate
  certifier.
- **Verifier:** `experimental/scripts/verify_x66_h4_norm_gate_orbit_invariance.py`.
- **Certificate:**
  `experimental/data/certificates/x66-h4-norm-gate-orbit-invariance/x66_h4_norm_gate_orbit_invariance.json`.

## Statement

For an X60 filtered triple `(a,b,c)`, put

```text
f_(a,b,c)(X) = X^a + X^b - X^c - 1
```

in the group ring `Z[C_n] = Z[X]/(X^n - 1)`.  Each of the eight X64
chord-pair transforms sends `f_(a,b,c)` to a signed monomial multiple of the
original word:

```text
(a,b,c)                         +1
(b,a,c)                         +1
(a-c,b-c,-c)                    +X^{-c}
(b-c,a-c,-c)                    +X^{-c}
(c-a,-a,b-a)                    -X^{-a}
(-a,c-a,b-a)                    -X^{-a}
(c-b,-b,a-b)                    -X^{-b}
(-b,c-b,a-b)                    -X^{-b}
```

Consequently the primitive-root zero condition and the sparse cyclotomic
norm-gate test

```text
p | Res(Phi_n, X^a + X^b - X^c - 1)
```

are invariant on each X64 orbit.  The primitive content-one certifier may
therefore evaluate one canonical orbit representative without losing any
characteristic-`p` obstruction.

## Proof

The first two transforms only swap the positive pair and leave the word
unchanged.  For the negative-pair re-anchor,

```text
X^{-c} f_(a,b,c)
  = X^{a-c} + X^{b-c} - 1 - X^{-c}
  = f_(a-c,b-c,-c).
```

The swapped positive-pair version is identical.  For the side swap anchored
at the old `x = zeta^a`,

```text
-X^{-a} f_(a,b,c)
  = -1 - X^{b-a} + X^{c-a} + X^{-a}
  = f_(c-a,-a,b-a),
```

and the paired transform only swaps its first two positive exponents.  The
old-`y` anchor gives similarly

```text
-X^{-b} f_(a,b,c) = f_(c-b,-b,a-b),
```

again with the paired positive swap.

Let `zeta` be any primitive `n`-th root in a field where the row is defined.
The monomials `zeta^m` and the signs are units, so

```text
f_transform(zeta) = unit * f_(a,b,c)(zeta).
```

Thus one word vanishes at `zeta` if and only if every word in its X64 orbit
does.  Over `Z`, the class of `X` is also a unit in `Z[X]/(Phi_n)` because
`Phi_n(0)=1` for 2-power `n`.  Multiplication by `±X^m` has norm `±1`, so
the integer resultants in an X64 orbit agree up to sign.  Their prime
divisors are identical.

## Replay

The verifier recomputes the X60 filtered triples in every replay row and
checks, for every triple and every X64 transform, that the transformed sparse
word is exactly the signed shift above in `Z[C_n]`.

```text
row                  filtered triples   primitive orbit reps
------------------------------------------------------------
low_n16_p17          168                20
low_n64_p193         1176               134
boundary_n64_p7937   208                23
boundary_n128_p17921 120                12
boundary_n256_p91393 224                22
```

All replayed transforms match the X64 orbit transforms and all signed
monomial identities hold.

## Consequence

X65 fixed the remaining h=4 target in canonical orbit-budget currency.  X66
adds that the p-specific norm-gate predicate itself is constant on those
orbits:

```text
canonical orbit representative
    <=> entire eightfold sparse-resultant orbit.
```

This is the right input shape for the next row-local primitive norm-gate
certifier.  It avoids accidentally checking ordered triples after the orbit
budget has already divided by eight.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x66_h4_norm_gate_orbit_invariance.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x66_h4_norm_gate_orbit_invariance.py --write-certificate
```
