# X67: h=4 Galois norm-gate compression

- **DAG node:** `x67_h4_galois_norm_gate_compression`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved certifier compression.
- **Verifier:** `experimental/scripts/verify_x67_h4_galois_norm_gate_compression.py`.
- **Certificate:**
  `experimental/data/certificates/x67-h4-galois-norm-gate-compression/x67_h4_galois_norm_gate_compression.json`.

## Statement

Let

```text
f_(a,b,c)(X) = X^a + X^b - X^c - 1
```

be a primitive content-one X60 word.  For every unit
`u in (Z/nZ)^*`,

```text
f_(ua,ub,uc)(X) = f_(a,b,c)(X^u).
```

Since `zeta -> zeta^u` permutes the primitive `n`-th roots, the cyclotomic
norm and resultant are unchanged up to sign:

```text
Res(Phi_n, f_(ua,ub,uc)) = +/- Res(Phi_n, f_(a,b,c)).
```

Thus the prime set in the p-specific norm-gate predicate

```text
p | Res(Phi_n, X^a + X^b - X^c - 1)
```

is constant on unit exponent orbits.  Unit scaling also preserves the X60
filter congruences and the primitive content condition.

## Warning

This is a certifier compression, not a finite-row counting symmetry.

Unit exponent scaling is a Galois relabeling of primitive roots in the
cyclotomic norm.  It is not an additive symmetry of the fixed finite-field
equation

```text
zeta^a + zeta^b - zeta^c = 1
```

for one chosen generator `zeta`.  Therefore row counts should not be divided
by `phi(n)` using this lemma.  It only says that a sparse-resultant certifier
may compute one norm per unit orbit of exponent words.

## Proof

The identity

```text
f_(ua,ub,uc)(X) = f_(a,b,c)(X^u)
```

is immediate from the definition of `f`.  For primitive roots,

```text
{ zeta^v : v in (Z/nZ)^* }
```

is the complete Galois orbit.  Multiplication by `u` permutes the unit group,
so the factor multiset

```text
{ f_(ua,ub,uc)(zeta^v) : v in (Z/nZ)^* }
  = { f_(a,b,c)(zeta^{uv}) : v in (Z/nZ)^* }
```

equals

```text
{ f_(a,b,c)(zeta^w) : w in (Z/nZ)^* }.
```

Their product, the norm of the image in `Z[zeta]`, is the same.  Equivalently
the resultant with the monic cyclotomic polynomial `Phi_n` is unchanged up to
the harmless global sign convention for resultants.

For the filters, `u` is odd because `n` is a power of two.  Hence it preserves

```text
a = 0, b = 0, c = 0, b = a, b = a + n/2      (mod n),
```

since `u*n/2 = n/2 mod n`.  It also preserves

```text
gcd(n,a,b,c),
```

because multiplication by a unit is invertible modulo every divisor of `n`.
Thus content-one words stay content-one.

## Replay

The verifier recomputes the primitive canonical X64 representatives from the
X60 replay rows.  For every representative and every unit `u`, it checks:

- the X60 filter congruences are preserved;
- primitive content remains `1`;
- the Galois factor multiset indexed by `(Z/nZ)^*` is unchanged.

```text
row                  primitive reps   units   factor checks
-----------------------------------------------------------
low_n16_p17          20               8       160
low_n64_p193         134              32      4288
boundary_n64_p7937   23               32      736
boundary_n128_p17921 12               64      768
boundary_n256_p91393 22               128     2816
```

The raw unit action on content-one exponent triples is free in every replayed
row, as expected from `gcd(n,a,b,c)=1`.

## Consequence

Together, X65-X67 put the h=4 centered residue into the correct certifier
currency:

```text
canonical X64 orbit representative
  -> one sparse word modulo signed monomial transforms (X66)
  -> one cyclotomic norm modulo Galois/unit relabeling (X67).
```

The next primitive norm-gate certifier can enumerate canonical X64
representatives and then group those by unit action for resultant
computations, while still expanding any surviving row-count contribution in
the correct finite-field currency.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x67_h4_galois_norm_gate_compression.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x67_h4_galois_norm_gate_compression.py --write-certificate
```
