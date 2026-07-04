# X39: h=4 affine-line normal form

- **DAG node:** `x39_h4_affine_line_normal_form`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved h=4 refinement.
- **Verifier:** `experimental/scripts/verify_x39_h4_affine_line_normal_form.py`.
- **Certificate:**
  `experimental/data/certificates/x39-h4-affine-line-normal-form/x39_h4_affine_line_normal_form.json`.

## Statement

Let

```text
psi(X)=X^4+a_3X^3+a_2X^2+a_1X+a_0
```

be a monic quartic over a field of characteristic `p > 4`.  If the polynomial
fiber product `psi(X)-psi(Y)` has an exact affine-line factor

```text
X = aY+b,
```

then either the affine map is the identity or

```text
psi(X)=Phi((X-c)^m),        m in {2,4},
```

where

```text
c = b/(1-a).
```

The zero-center case `c=0` is the cyclic-paid branch already isolated by X38.
The nonzero-center case is **not** charged here; it is the named
`h4_centered_power_affine_residue`.

## Proof

The line factor is equivalent to the polynomial identity

```text
psi(aY+b)=psi(Y).
```

If `a=1` and `b != 0`, then the coefficient of `Y^3` in
`psi(Y+b)-psi(Y)` is

```text
4b,
```

which is nonzero because `p > 4`.  So nontrivial translations are impossible.

Assume `a != 1`, and put

```text
c = b/(1-a).
```

Then

```text
aY+b-c = a(Y-c),
```

so, after the shift `T=Y-c`, the identity becomes

```text
phi(aT)=phi(T),        phi(T)=psi(T+c).
```

The leading coefficient of `phi` is still `1`, so the top coefficient gives

```text
a^4=1.
```

Since the affine map is not the identity, `ord(a)` is `2` or `4`.  Comparing
all coefficients of `phi(aT)=phi(T)`, every nonzero coefficient of `phi` has
exponent divisible by `m=ord(a)`.  Hence

```text
phi(T)=Phi(T^m),        m in {2,4},
```

and therefore

```text
psi(X)=Phi((X-c)^m).
```

This proves the normal form.

## Consequence For h=4

X38 treated the exact toral/scaling subcase `c=0` and showed it is cyclic-paid.
X39 shows that the broader affine-line branch has only one further possibility:
a nonzero-center power map.

Thus a primitive h=4 quartic two-fiber residue has no affine-line component
unless it belongs to the explicit centered-power branch

```text
h4_centered_power_affine_residue:
  psi(X)=Phi((X-c)^2) or Phi((X-c)^4),        c != 0.
```

This packet does not bound that branch.  It makes it a precise target rather
than mixing it with the general primitive quartic residue.

## Checks

The verifier records:

- coefficient-level impossibility of nontrivial translations;
- nonzero-center order-2 and order-4 examples, classified but not paid;
- zero-center order-2 and order-4 examples, classified as cyclic-paid;
- the `mu_4` baseline as affine-symmetric;
- the top-level first-sum-only nontrade as not affine-symmetric for the tested
  maps.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x39_h4_affine_line_normal_form.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x39_h4_affine_line_normal_form.py --write-certificate
```
