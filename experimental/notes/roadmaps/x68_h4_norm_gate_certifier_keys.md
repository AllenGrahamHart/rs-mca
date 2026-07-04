# X68: h=4 norm-gate certifier keys

- **DAG node:** `x68_h4_norm_gate_certifier_keys`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved certifier-key packaging.
- **Verifier:** `experimental/scripts/verify_x68_h4_norm_gate_certifier_keys.py`.
- **Certificate:**
  `experimental/data/certificates/x68-h4-norm-gate-certifier-keys/x68_h4_norm_gate_certifier_keys.json`.

## Statement

For a primitive content-one X60 word

```text
f_(a,b,c)(X) = X^a + X^b - X^c - 1,
```

define the **norm-gate certifier key**

```text
K(a,b,c) = min_lex { T(u a, u b, u c) :
                     u in (Z/nZ)^*, T one of the eight X64 transforms }.
```

Then every word with the same key has the same cyclotomic resultant prime
set.  More concretely, if `K(a,b,c) = K(a',b',c')`, then

```text
prime divisors of Res(Phi_n, f_(a,b,c))
  = prime divisors of Res(Phi_n, f_(a',b',c')).
```

The key is itself X60-filtered and content-one whenever the input is.

## Warning

This is only a sparse-resultant certifier key.

The raw key orbit usually contains exponent words that are not finite-field
solutions for the row's chosen generator.  Therefore X68 must not be used to
divide the actual row count.  It only reduces how many cyclotomic resultants
the primitive norm-gate certifier needs to compute.  If a key survives, its
finite-row contribution is still expanded in X65's primitive X64 row-count
currency.

## Proof

X66 proves that every X64 transform sends `f_(a,b,c)` to a signed monomial
multiple of the original word in `Z[C_n]`.  Signed monomial multiplication is
a unit operation modulo `Phi_n`; it preserves the primitive-root zero
condition and the resultant prime set.

X67 proves that unit exponent scaling

```text
(a,b,c) -> (u a, u b, u c)
```

sends

```text
f_(a,b,c)(X) -> f_(a,b,c)(X^u)
```

and hence only permutes the primitive-root factors of the cyclotomic norm.
It also preserves the X60 filter congruences and primitive content.

The generated relation is therefore a relation by operations that preserve:

```text
1. X60-filtered status,
2. content gcd(n,a,b,c),
3. the prime divisor set of Res(Phi_n, f).
```

Taking the lexicographically least member gives a canonical representative of
that relation.  Idempotence follows because taking the orbit of an orbit
minimum gives the same finite set.

## Replay

The verifier recomputes the primitive X64 canonical representatives from the
X60 replay rows, groups them by `K`, and checks that every raw certifier orbit
has one key.

```text
row                  primitive X64 reps   certifier keys   row reps merged
--------------------------------------------------------------------------
low_n16_p17          20                   19               1
low_n64_p193         134                  133              1
boundary_n64_p7937   23                   23               0
boundary_n128_p17921 12                   12               0
boundary_n256_p91393 22                   22               0
```

The observed replay compression is small, which is fine: the purpose of this
packet is not to improve the row budget.  Its purpose is to fix the exact
input currency for the primitive sparse-resultant certifier.

## Consequence

The h=4 centered primitive norm-gate certifier can now operate on:

```text
one resultant per X68 key,
with survivor mass expanded through X65 primitive X64 representatives.
```

This prevents two opposite errors:

- recomputing the same resultant across signed-monomial or Galois copies;
- undercounting row mass by treating Galois copies as finite-row symmetries.

The terminal h=4 residue is now ready for a row-local primitive norm-gate
exclusion/certification packet in this exact key currency.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x68_h4_norm_gate_certifier_keys.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x68_h4_norm_gate_certifier_keys.py --write-certificate
```
