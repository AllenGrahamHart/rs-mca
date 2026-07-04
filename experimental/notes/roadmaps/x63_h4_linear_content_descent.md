# X63: h=4 linear content descent

- **DAG node:** `x63_h4_linear_content_descent`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved content split.
- **Verifier:** `experimental/scripts/verify_x63_h4_linear_content_descent.py`.
- **Certificate:**
  `experimental/data/certificates/x63-h4-linear-content-descent/x63_h4_linear_content_descent.json`.

## Statement

Let `n = 2^s`, let `zeta` be a primitive `n`-th root, and consider an X60
filtered finite-field solution

```text
zeta^a + zeta^b - zeta^c - 1 = 0.
```

Put

```text
d = gcd(n,a,b,c).
```

If `d > 1`, then the four-term word is a quotient pullback:

```text
X^a + X^b - X^c - 1 = G(X^d),
```

and the triple descends verbatim to the smaller row `mu_{n/d}`:

```text
beta^(a/d) + beta^(b/d) - beta^(c/d) - 1 = 0,
beta = zeta^d.
```

The X60 filtered conditions descend as well.  Therefore the post-quotient
primitive part of the X62 norm-gate residue is exactly the content-one
subfamily

```text
gcd(n,a,b,c) = 1.
```

## Proof

Since `d` divides `n,a,b,c`, write

```text
n = d n',        a = d a',        b = d b',        c = d c'.
```

Then

```text
X^a + X^b - X^c - 1
  = X^(d a') + X^(d b') - X^(d c') - 1
  = G(X^d),
```

where

```text
G(T)=T^a' + T^b' - T^c' - 1.
```

Because `zeta` has order `n`, the element

```text
beta = zeta^d
```

has order `n' = n/d`.  Evaluating `G` at `beta` gives the displayed quotient
equation.

The five X60 exclusions are congruence conditions:

```text
a = 0,        b = 0,        c = 0,        b = a,
b = a + n/2             (mod n).
```

Dividing by `d` gives exactly the corresponding exclusions modulo `n'`:

```text
a' = 0,       b' = 0,       c' = 0,       b' = a',
b' = a' + n'/2            (mod n').
```

So a filtered nonprimitive triple descends to a filtered quotient triple.  This
is precisely the quotient/pullback branch already handled by the strip; it is
not primitive top-level X62 mass.

## Consequence

X62 says every filtered h=4 linear triple is finite-p norm-gate mass.  X63
splits that mass into:

```text
content d > 1:      quotient-row pullback, recurse/charge at scale n/d;
content d = 1:      primitive four-term norm-gate residue.
```

Thus the next row-local certifier only needs to attack primitive words

```text
X^a + X^b - X^c - 1,
gcd(n,a,b,c)=1,
```

outside the X60 branches.  Nonprimitive words are not a new top-level
mechanism.

## Replay

The verifier replays all X60 finite rows.  In those rows the content split is:

```text
row                  primitive content  quotient-descended content
low_n16_p17          160                8
low_n64_p193         1072               104
boundary_n64_p7937   184                24
boundary_n128_p17921 96                 24
boundary_n256_p91393 176                48
```

All nonprimitive replayed words have `d=2` and descend to the `n/2` quotient
row; this last observation is evidence only, not part of the general theorem.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x63_h4_linear_content_descent.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x63_h4_linear_content_descent.py --write-certificate
```
