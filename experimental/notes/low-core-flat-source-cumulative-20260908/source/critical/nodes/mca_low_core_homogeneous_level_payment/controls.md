# Hypothesis guards and an actual nongraph source

## Canonical hyperbola source

Use F=F_(787^2), beta^2=2, P=X+beta, D={0,...,782}, K=2,
m=30, T=1 and carrier V=span{1,P}. Partition D into 27 groups
of 29 points. On group j put (u,v)=(j*P,1/j). Represented pairs
are f_i=(i*P,1/i), satisfying the homogeneous level identity a*b=P.

At x in group j, i!=j, the scalar collision label is
gamma=i*j*P(x). Equality of two labels first gives i*j from the
beta coefficient, then x from the constant coefficient, then its
group j, and finally i. All 20358 labels are distinct and all
27 pairs are represented. Each complete core is exactly its group.

For a fixed printed label, any carrier polynomial other than a
source-piece polynomial h_i=i*P+gamma/i agrees at at most one
point in each group, hence fewer than 30 points. Distinct h_i are
distinct polynomials because their X coefficients differ. Each h_i
has 29 own-core agreements and at most one outside agreement, by
label uniqueness. The printed label has one such extra point, giving
a unique eligible carrier explanation and maximum raw margin one.
Any degree-<2 second-component codeword agreeing with 29 core values
is 1/i and fails at the defect, so that 30-support is full-code bad.
This is a fixed-carrier canonical census, not an ambient-code census.

This source lies on no rational-X POLYNOMIAL graph of Y-degree
2,...,7 after a constant invertible matrix and polynomial pair offset.
Indeed write transformed pairs, with parameter t=1,...,27, as

    a_t=A*t*P+B/t+a_0, b_t=C*t*P+D/t+b_0.

For a putative graph b_t=Psi(X,a_t) of degree e, multiply the
Laurent difference by t^e. Its degree is at most 2e<=14, so its
27 zeros make it identically zero. If A!=0, its highest Laurent
power t^e has nonzero coefficient p_e*(A*P)^e, impossible since
b_t has powers at most one. Thus A=0. Invertibility forces B!=0;
the lowest Laurent power t^(-e), coefficient p_e*B^e, is then
equally impossible. This argument permits rational X-coefficients
and offsets of arbitrary degree. It is a hand identity argument,
not a finite search over matrices.

The control separates the new mechanism from the paid graph class.
It is not a deployed unsafe source or a claim that no earlier
subfield/row-space payment covers it.

## Load-bearing guards

The affine-product cubic U*V*(U+V+1)=1 is included even though
its three lines do not concur. It cannot be a translated homogeneous
cubic level: the top form is U^2*V+U*V^2, and translating it by
(h,k) gives quadratic terms -k*U^2-h*V^2-2(h+k)*U*V.
Matching the desired quadratic term U*V forces h=k=0 from the
square terms, then incorrectly requires 0=1 for U*V. Over F_5,
(U,V)=(2,3) and (2,4) show that the level is nonempty. No new
assumption or degree price is needed for this affine extension.

For V=span{1,X}, the zero-level equation a*b=0 contains the
two-dimensional component a=0,b arbitrary. Nonzero R is essential.
The single-direction nonzero-level equation a^2=1 contains
a=1,b arbitrary, again two-dimensional. Repeated factors are allowed
only when there are at least two DISTINCT directions in total.
Even distinct affine factors can be parallel: a*(a+1)=2 still
contains a=1,b arbitrary. Distinct factors alone are insufficient.

Even the valid equation a*b=1 contains the one-dimensional family
(a,b)=(t,1/t), t!=0. Fixed divisor patterns imply a bound modulo
scalar, not finitely many pairs or dimension zero. The degree cost
e^(2s-1) must still count every coefficient component.

The verifier checks these small field families and the exact hyperbola
labels. Universal dimension, canonical maximality and graph exclusion
are supplied by the hand proofs, not inferred from those samples.
