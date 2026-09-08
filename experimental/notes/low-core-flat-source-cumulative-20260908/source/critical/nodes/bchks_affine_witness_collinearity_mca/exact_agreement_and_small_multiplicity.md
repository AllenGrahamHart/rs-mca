# Exact agreement gate and multiplicities one and two

Status: PROVED by hand, 2026-09-06. This strengthens the existing
rounded theorem; it does not import the sketched sharp MCA constant.

Keep n,d=k-1,r=n-a and t=m+1/2, but allow every integer m>=1.
Set

```text
X=t*sqrt(n*d), Y=t*sqrt(n/d),
Z=max(Y,t^2*n/(3*d)), L=ceil(X),
H=2*L*Y^2*Z+(r+1)*Y+Z.
```

The sufficient agreement gate is EXACTLY

```text
0<=a<=n,       4*m^2*a^2 >= (2*m+1)^2*n*d.          (G')
```

Under these hypotheses the conclusion of proof.md holds unchanged:
the full original finite-slope MCA numerator is <=min(|F|,floor(H)).
Here are the two required replacements in that proof. All other
factor, denominator, Frobenius and chosen-witness arguments are retained.

## 1. Interpolant existence at every positive multiplicity

BCHKS Lemma 3.1's following paragraph, printed page 23, explicitly
permits smaller m by replacing its Z bound with the maximum of Y
and the old Z bound. This is a proved interpolation construction,
not the later sketched MCA theorem. Its count can also be checked
directly at the boundary values m=1,2.

Write rho=d/n and x=sqrt(rho). The source's sufficient strict
variables-versus-equations inequality simplifies to

```text
(t*x+1/4)*ceil(Z)
  > t^3/(3*x) - (t*x+m^3-m)/3.                     (1)
```

Our Z>=t^2/(3*x^2) makes the left side strictly greater than
t^3/(3*x), whereas the right side is strictly smaller, for every
m>=1. The counting prerequisites X=dY, Z>=Y and Y>=m-1
are all satisfied. Thus the strict monomial count and nonzero
interpolant apply at m=1,2 as well. No characteristic restriction
or genericity assumption is introduced.

Gate (G') is precisely X<=m*a, since both sides are nonnegative.
That is all the selected-witness substitution uses: its degree is
<X, while its zeros have total multiplicity at least m*a.
The old (m+1)*sqrt(n*d) agreement requirement was sufficient but
not necessary for this step.

## 2. Chosen-witness collinearity still follows

In proof.md section 4 put

```text
alpha=(a-d)/(n-d)>0.
```

The (d+1)-st largest agreement load is at least alpha*|T'|.
The needed inequality is

```text
alpha*(2*L-1)>2*d+1.                               (2)
```

This must be checked, not inferred merely from interpolant existence.
From (G'), a/n>=(t/m)*x and a<=n, hence x<=m/t. Also

```text
alpha >= x*((t/m)-x)/(1-x^2),
2*L-1 >= (2*m+1)*n*x-1.
```

For m=1, x<=2/3 and

```text
((3/2)-x)/(1-x^2) > 13/10,
13*x^2-10*x+2 = 13*(x-5/13)^2+1/13 > 0.
```

Consequently alpha*(2L-1)>(13/10)*(3d-x), which exceeds
2d+1 by at least 1/30, using d>=1 and x<=2/3.

For m=2, x<=4/5 and
((5/4)-x)/(1-x^2)>=1, since its numerator minus its denominator
is (x-1/2)^2. Thus alpha*(2L-1)>=5d-x>=5d-4/5>2d+1.

For m>=3, a/n>=x gives alpha>=x/(1+x), and the original
argument applies:

```text
alpha*(2L-1) >= (7d-x)/(1+x)>2d+1,
5d-1>2x(d+1)       for d>=1, 0<x<1.
```

This proves (2) at every multiplicity. The norm-zero argument then
forces d+1 coordinate identities in the function field, recovering
the same affine codeword line and its at-most-r+1 chosen bad witnesses.
Class weights and exceptional-content charges are unchanged.

The common Hensel starting-point argument also remains valid:
Y>1 and Z>=Y give H>=2L*Y^2*Z>2XY, the requisite resultant
degree threshold. If |F|<=H the bound is trivial as before.

## 3. When the original integer affordability formula applies

Z=t^2*n/(3d) exactly when

```text
36*d <= (2*m+1)^2*n.                               (3)
```

This always holds for m>=2 under (G'): x<=m/t and t^2>=3m.
At m=1 it is the extra condition 4d<=n. Otherwise use Z=Y in
the displayed real bound; do not reuse the old Z-specific integer
formula. The finite KoalaBear endpoint uses m=146, so (3) holds.

## Scope

These are sufficient upper certificates for arbitrary fields, distinct
domains and received pairs, including full agreement tails. No rank
restriction, correction census, same-support replacement, or exhaustive
MCA computation is required. Failure of the gate or affordability test
does not prove actual unsafety. Independent external review of the
underlying Hensel assembly remains due.

Primary interpolation source: [BCHKS, ECCC TR25-169, Lemma 3.1 and
the following paragraph](https://eccc.weizmann.ac.il/report/2025/169/download/).
The smaller-m extension is credited to that paragraph. The local work
checks it against the rounded, preselected-bad-witness assembly and
proves (2) with the relaxed gate.
