# T-TOY: toral classification sanity scan

- **DAG node:** `u1_tame_toral_fiberproduct_classification`.
- **Task:** T-TOY.
- **Status:** TOY SANITY PASS.  No exception was found in the exact
  polynomial bidegree-`(1,1)` scan.
- **Verifier:** `experimental/scripts/verify_ttoy_toral_classification_scan.py`.
- **Certificate:**
  `experimental/data/certificates/ttoy-toral-classification-scan/ttoy_toral_classification_scan.json`.

## Scope

The scan covers tame toy rows with `deg psi in (t,20]` and `deg psi < p`:

```text
F_97 / mu_32,    t=3, degrees 4..20
F_193 / mu_64,   t=3, degrees 4..20
F_257 / mu_256,  t=5, degrees 6..20
```

It targets the first factorization case: bidegree-`(1,1)` factors of
`psi(X)-psi(Y)`.  A factor `X-(aY+b)` is equivalent to the affine symmetry

```text
psi(aY+b) = psi(Y).
```

The exact toral line `X=aY` is the `b=0` subcase.  The verifier also checks
the inverse toral shape `XY=c`.

## Classification Checked

For `deg psi < p`, translation symmetries cannot occur for nonconstant maps:
the leading coefficient of `psi(Y+b)-psi(Y)` is `d*b*a_d`, nonzero when
`b != 0`.

For `a != 1`, the affine map has fixed point

```text
c = b/(1-a).
```

After translating `X` by `c`, the symmetry is a scaling.  If `m=ord(a)`, every
invariant map has the normal form

```text
psi(X) = phi((X-c)^m).
```

Thus every exact bidegree-`(1,1)` affine/toral factor found by the scan is
chargeable as a power pullback after linear conjugacy and coset scaling.

The inverse toral factor `XY=c` is impossible for nonconstant exact
polynomial `psi`: in `Y^d(psi(c/Y)-psi(Y))`, each nonconstant coefficient
appears in two distinct Laurent degrees `d-i` and `d+i`.

## Dickson Sanity

Dickson polynomials do not create a new exact polynomial toral-line class in
this scan.  Odd degrees have no exact line factor.  Even degrees have the
expected `X -> -X` symmetry and reduce to the power-pullback form `phi(X^2)`.

This matches the X-8 correction: Dickson/Chebyshev belongs to the
Laurent/rational branch of T, not to exact polynomial toral components.

## Verdict

No exception was found:

```text
unclassified bidegree-(1,1) cases: 0
```

This does not prove the full T input.  It removes the cheap falsifier at the
first factorization rung and leaves the load-bearing T work exactly where the
DAG says it is:

```text
positive-characteristic Laurent/Ritt classification,
the corrected n^2/p threshold,
bounded-tail robustness.
```

## Verification

Run:

```bash
python3 experimental/scripts/verify_ttoy_toral_classification_scan.py
```
