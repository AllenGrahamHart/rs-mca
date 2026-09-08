# Descend the curve, not the received word

The required weighted supplier proves that d=s-1=10 forces

    V=q*span_F{B^10,A*B^9,...,A^10},
    gcd(A,B)=1, h=max(deg A,deg B)>=1, deg q+10h<J.

Write rho=A/B=T. Every original pair in `(h_*+V) x V` is uniquely

    a=h_*+q*B^10*P(T), b=q*B^10*Q(T), deg P,Q<=10.   (1)

This is an identity over the function field; at B=0 use the corresponding
homogeneous polynomials, not division by B at that coordinate.
The map from coefficient vectors to (P,Q) is a linear affine isomorphism.

The original cubic becomes a geometrically integral cubic G(P,Q) over
F(X), with top binary form proportional to `(T P+Q)^3`. The affine
change of coordinates preserves its unique smooth infinity point and
affine singularity. Suppose its coefficient locus has dimension four.
In particular it contains infinitely many polynomial pairs over k[T],
where k is the algebraic closure of F.

## Coefficient descent

The polynomial `A(Z)-T*B(Z)` is irreducible over k(T): in k[Z,T] a
factorization, being linear in T, would have a T-independent factor
dividing both A and B. Primitivity in Z over k[T] then gives the claim
over k(T). Its Z-degree is h. Thus `1,X,...,X^(h-1)` form a basis of
both F(X)/F(T) and k(X)/k(T). No linear independence is lost on extending
the constant field. Expand

    G = sum_(i=0)^(h-1) X^i*G_i, G_i in F(T)[P,Q], deg G_i<=3.

Every polynomial pair over k[T] solving G=0 therefore solves every G_i=0.
Fix a nonzero G_i. If it is not a scalar multiple of G over k(X), it is
coprime to G, since G is geometrically integral and deg G_i<=3.
Bezout bounds their common geometric points by nine. This contradicts
the infinitely many distinct polynomial pairs, considered as points over
k(X). Hence G is a scalar multiple of a cubic H over F(T).

The geometric properties descend under the field extension, and the
polynomial-pair coefficient locus is unchanged. We may apply the generic
maximal-family theorem to H over k(T).

This proof only descends the defining curve. Neither u nor v nor h_* is
asserted to be a function of T. All those data remain at the original
X-coordinates. The original field size, slopes and near allowance stay
unchanged; extending constants for the geometry is an upper-bound device.

## Constant extensions are not required for a hidden source premise

The source contract supplies the actual algebraic coefficient locus, not
the finite Zariski closure of selected F-pairs. Its dimension four is
the only infinitude used here. If dimension is at most three, the old
weighted count already pays and this descent is unnecessary.
No sampled family is promoted to a positive-dimensional family.
