# Projective-flat occupancy strengthens the slope resource

Status: PROVED by the hand proof; external independent review due.

Use the exact selected-slope setup of the completed-basis supplier: a
degree-<K polynomial carrier V of dimension s>=1, affine explanations
h_*+V, size-m full-code-bad supports with m=K+d, and distinct finite
labels Gamma. The chosen supports need NOT maximize raw margins.
Let r_gamma>=1 be the minimum mismatch to b in V on the chosen support.

For a fixed basis of V let ell_x be evaluation at x. Fix a real h>=1.
Assume every j-dimensional linear subspace of V* contains the nonzero
evaluation vectors of at most j*h ORIGINAL coordinates, for 1<=j<s.
This is a bound on all low-dimensional subspaces, not merely on fibers.
The proof only multiplies positive lower bounds on integer choice counts;
integrality of h is unnecessary. This weakens the earlier integer-h scope.

A sufficient special case is a projective arc: every at most s distinct
projective evaluation classes are independent and each class has at most
h coordinates. The subspace-occupancy hypothesis is weaker and is the
only condition used by the proof.

Let z count zero incidence normals (v(x),-ell_x), and let g count those
also satisfying u(x)=h_*(x). Keep these coordinates; do not assume g=0.
Write P=prod_(i=1)^(s-1)(d+i) and w_s(r;g) for the required supplier's
completed normalized weight. Define

    beta(r)=(s+1)*r*prod_(j=0)^(s-1)(m-r-g-j*h)

when m-r-g>(s-1)h, and beta(r)=0 otherwise. Then

    sum_Gamma max((m-g)*P*w_s(r_gamma;g), beta(r_gamma))
          <= (n-z)_falling_(s+1).                    (FLAT)

Both counts consume the SAME independent tuples and combine by maximum.

If T>=1 and (s+1)T<m-g-(s-1)h, then beta(r)>=beta(1) for 1<=r<=T.
If w_s(r;g)>=L>0 for every raw r>T, (FLAT) gives

    |Gamma| <= floor((n-z)_falling_(s+1)
                      /min(beta(1),(m-g)*P*L)).      (MIN)

This is a complete source count, not an assertion that all LOW pairs
lie on a curve. Neither arbitrary V nor an arbitrary projective image
is assumed to satisfy the occupancy hypothesis. Finite row payment,
original near and source transport belong to the consumer.
