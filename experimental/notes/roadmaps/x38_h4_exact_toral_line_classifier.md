# X38: h=4 exact toral-line classifier

- **DAG node:** `x38_h4_exact_toral_line_classifier`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved h=4 specialization.
- **Verifier:** `experimental/scripts/verify_x38_h4_exact_toral_line_classifier.py`.
- **Certificate:**
  `experimental/data/certificates/x38-h4-exact-toral-line-classifier/x38_h4_exact_toral_line_classifier.json`.

## Statement

Let

```text
psi(X)=X^4+a_3X^3+a_2X^2+a_1X+a_0
```

be a monic quartic over a field of odd characteristic.  If the polynomial
fiber product

```text
psi(X)-psi(Y)=0
```

has an exact toral line of scaling type

```text
X = lambda Y,        lambda != 1,
```

then `psi` is a cyclic pullback:

```text
psi(X)=Phi(X^2)      or      psi(X)=Phi(X^4).
```

The inverse toral line

```text
XY = c,        c != 0,
```

cannot occur for a nonconstant exact polynomial quartic.

Consequently, in the X37 h=4 two-fiber form, every exact toral-line quartic is
already paid by the cyclic strip.  Any remaining primitive quartic residue has
no exact toral line in its polynomial fiber product.

## Proof

For a scaling line `X=lambda Y`, the factor condition is exactly

```text
psi(lambda Y)=psi(Y).
```

Comparing coefficients gives

```text
(lambda^i-1)a_i = 0,        i=0,1,2,3,4,
```

where `a_4=1`.  The leading coefficient therefore forces

```text
lambda^4=1.
```

Because the characteristic is odd and `lambda != 1`, the order

```text
m = ord(lambda)
```

is either `2` or `4`.  For every nonzero coefficient `a_i`, the same
coefficient identity gives `lambda^i=1`, hence `m | i`.  Thus all nonzero
exponents are multiples of `m`, so

```text
psi(X) = Phi(X^m),        m in {2,4}.
```

This is exactly a cyclic pullback, hence paid.

For the inverse toral line, suppose `XY-c` divides `psi(X)-psi(Y)`.
Substituting `Y=c/X` gives the rational identity

```text
psi(X)-psi(c/X)=0.
```

Multiplying by `X^4`, the term from the monic leading coefficient contributes

```text
X^8
```

with coefficient `1`.  No term from `X^4 psi(c/X)` has degree `8`, so the
identity is impossible.  Therefore no exact inverse toral line occurs for a
nonconstant monic quartic.

## Relation To X37

X37 proves that disjoint h=4 trades are exactly two split fibers of the monic
quartic locator `L_P`.  This packet classifies the cheapest possible toral
symmetries of that quartic fiber product:

```text
exact scaling toral line   -> cyclic pullback paid,
exact inverse toral line   -> impossible.
```

It is intentionally narrower than the full tame Laurent/Ritt theorem.  It does
not classify higher-degree components or rational/Laurent tails.  It does
remove the exact line-level toral escape from the remaining h=4 primitive
branch.

## Checks

The verifier records:

- coefficient-level scaling checks in `F_97` and `F_4993`;
- the inverse-line obstruction for several nonzero `c`;
- the `mu_4` baseline as an order-4 cyclic pullback;
- the antipodal quotient extra as an order-2 cyclic pullback;
- the top-level first-sum-only nontrade as having no exact scaling toral line.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x38_h4_exact_toral_line_classifier.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x38_h4_exact_toral_line_classifier.py --write-certificate
```
