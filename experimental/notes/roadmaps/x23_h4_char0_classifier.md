# X23: h=4 characteristic-zero classifier

- **DAG node:** `x23_h4_char0_classifier`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved over characteristic zero.
- **Verifier:** `experimental/scripts/verify_x23_h4_char0_classifier.py`.
- **Certificate:**
  `experimental/data/certificates/x23-h4-char0-classifier/x23_h4_char0_classifier.json`.

## Statement

Let `n=2^s`, `s >= 2`, and let `H = mu_n(C)`.  If `P,Q` are disjoint
4-subsets of `H` with the same first three elementary symmetric sums, then
`P` and `Q` are full `mu_4` fibers:

```text
P = a mu_4,        Q = b mu_4,        a^4 != b^4.
```

Thus, in characteristic zero, the h=4 terminal residue is entirely cyclic-paid.
The finite-field antipodal quotient-lift exceptions seen in X20-X22 are
p-specific reductions, not characteristic-zero trades.

## Proof

Write `H = <zeta>` and encode the two supports by the signed word

```text
f(X) = sum_{zeta^i in P} X^i - sum_{zeta^j in Q} X^j,
```

with exponents represented in `[0,n)`.  Equality of the first elementary
symmetric sum gives

```text
f(zeta) = 0.
```

Since `n` is a power of two,

```text
Phi_n(X) = X^(n/2) + 1.
```

The polynomial `f` has degree `< n`, so `Phi_n | f` is equivalent to

```text
coeff_i(f) = coeff_{i+n/2}(f)       for 0 <= i < n/2.
```

The coefficients are in `{ -1, 0, 1 }` because `P` and `Q` are disjoint.
Therefore each nonzero coefficient occurs with the same sign at the antipodal
exponent.  Hence both `P` and `Q` are unions of two antipodal pairs:

```text
P = {a,-a,b,-b},       Q = {c,-c,d,-d}.
```

For such a support,

```text
L_P(X) = (X^2-a^2)(X^2-b^2)
       = X^4 - (a^2+b^2)X^2 + a^2b^2.
```

So `e_1=e_3=0`, and equality of `e_2` is exactly

```text
a^2 + b^2 = c^2 + d^2
```

inside `mu_{n/2}(C)`.

It remains to classify two-point sum collisions on the complex unit circle.
If `u+v = r+s` with all four points on the unit circle, then the common sum is
twice the midpoint of both chords.  A nonzero midpoint determines a unique
chord of the unit circle, hence `{u,v}={r,s}`.  Since `P` and `Q` are disjoint,
the quotient pairs must therefore have zero sum.  Thus each quotient pair is
antipodal:

```text
b^2 = -a^2,       d^2 = -c^2.
```

Lifting back to `mu_n`, this says

```text
P = a mu_4,       Q = c mu_4.
```

This proves the classification.

## Relation to finite-field data

Over finite fields, `f(zeta)=0` at one chosen primitive `n`-th root does not
force the integral divisibility `Phi_n | f`.  This is exactly where the
exceptional-prime behavior enters.

X20-X22 observed finite h=4 exceptions, but all of them are still paid:

```text
antipodal_h2_quotient_lift.
```

So the h=4 proof route splits cleanly:

```text
characteristic-zero part:  proved, only mu_4 fibers;
finite p-specific part:    certify/charge antipodal quotient lifts.
```

## Verification

Run:

```bash
python3 experimental/scripts/verify_x23_h4_char0_classifier.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x23_h4_char0_classifier.py --write-certificate
```

Current replay: **12 PASS, 0 FAIL**.
