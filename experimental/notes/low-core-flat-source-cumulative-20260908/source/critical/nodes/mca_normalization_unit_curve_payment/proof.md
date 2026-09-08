# Proof: two integral functions bound both divisor directions

## 1. Fix the field and the normalization function

Work over k=algebraic closure of F. Fix the finite extension L/k(X)
in the statement, the normalized affine curve D over L, and its unit z.
The extension is fixed for the ENTIRE coefficient locus. The ring of
D is integral over L[U,V]/(Q). Consequently both z and z^(-1) satisfy
fixed monic equations with coefficients in this latter ring. Choose
polynomial representatives of those coefficients in L[U,V].

The normalization is birational. Represent z as a quotient of two
functions on Q=0, and exclude the finitely many curve points where
that expression or the normalization inverse is not defined. Such
points supply at most finitely many fixed polynomial pairs, hence
zero-dimensional coefficient loci. They are not discarded from the
eventual degree cover. On the remaining open curve, z(a,b) is a
well-defined nonzero element of L for every polynomial pair.

Let B be a normal projective k-curve with function field L. Its
existence and the constant-function facts are already sourced in the
required homogeneous-level supplier. We distinguish B, whose variable
is X, from the normalized PAIR curve D over L.

## 2. Integrality bounds the poles of z and its reciprocal

Fix the bounds on deg(a),deg(b). Each coefficient of either monic
equation, after evaluation at (a,b), belongs to a FIXED finite-dimensional
k-subspace of L. Its pole orders are bounded at a fixed finite set S
of places of B, and it has no poles outside S.

At a place P, consider an evaluated monic equation

    z^d + c_(d-1) z^(d-1) + ... + c_0 = 0.

Choose b_P>=0 with ord_P(c_i)>=-b_P for all coefficients and all
pairs. If ord_P(z)<-b_P, the monic leading term has strictly smaller
valuation than every other term, which is impossible in a vanishing
sum. Thus ord_P(z)>=-b_P. The monic equation for z^(-1) similarly
gives ord_P(z)<=b'_P. Outside S both bounds are zero. Hence div(z)
is supported on S, with every coefficient in a fixed finite integer
interval.

Only finitely many divisors can occur. On the normal projective curve B,
two nonzero functions with the same divisor differ by a k-star constant.
Choose representatives f_1,...,f_q in L-star for the occurring classes.
Every evaluated unit is thus lambda*f_i, for some lambda in k-star.
Neither q nor the sizes of the pole bounds are inserted into a point
count. They are used only for the following dimension argument.

## 3. The rational coefficient map has finite fibers over one scalar

Let Y be a positive-dimensional reduced irreducible coefficient component.
The finitely many exceptional pairs from section 1 do not contain Y.
Shrink to an open Y_0 where the unit expression is defined.

The pole bounds place all evaluated z in the vector space L(D_0)
for a fixed effective divisor D_0 on B. This space is finite-dimensional:
evaluation at deg(D_0)+1 distinct points outside its support is injective,
since a nonzero function with those poles has at most deg(D_0) zeros.
Choose such auxiliary evaluation points also avoiding the finitely many
fixed coefficient/X poles and the places where the denominator expression
is identically zero on Y_0.
This extra forbidden set is finite by expanding the generic denominator
in finitely many linearly independent coefficient functions on Y.
After shrinking Y_0, all those evaluations are rational, and then regular,
functions of its original polynomial coefficients.

The evaluation image lies in the finite union of the lines k*f_i
(in evaluation coordinates). This union is closed. Density of k-points
and irreducibility put the whole image in ONE of those lines. A nonzero
coordinate of f_i therefore defines a regular scalar function lambda
on a further nonempty open, with z=lambda*f_i.

For each fixed lambda in k, the nonconstant rational function z on
the normalized pair curve D has only finitely many geometric points
in that fiber. Thus only finitely many original pairs (a,b) can occur
with this lambda. The morphism Y_0->A^1_k has finite closed fibers;
the dimension-of-fibers theorem gives dim Y<=1. This needs no
separability or tangent-map injectivity. Finite fibers, not an assumed
birational unit coordinate, suffice.

Together with the exceptional zero-dimensional loci, this proves the
dimension bound for ALL coefficient components.

## 4. Two normalization points at infinity supply a unit

If the geometric projective normalization is P^1, choose a fixed finite
extension L over which that description and two distinct boundary
points P,Q are defined. A coordinate z with simple zero at P and
simple pole at Q has no zero or pole on the inverse image of the
affine curve. Both z and its inverse are regular there, hence integral
over the affine coordinate ring. The preceding argument applies.
Normalization finiteness and the genus-zero description are sourced in
`audit.md`. The function need not descend to a regular unit on the
singular affine curve itself.

## 5. Retain original degree and original LOW labels

Restrict to the original affine 2s-dimensional polynomial pair space.
Clearing fixed X-denominators from Q(a,b)=0 gives coefficient equations
of degree <=e. The general degree-cover lemma required through the
homogeneous-level supplier covers the dimension-<=1 locus, including
all exceptional points and all divisor classes, with degree e^(2s-1).
Its joint LIST induction gives the stated M_t bound.

The same supplier's complete-core raw-weighted proof then gives the
group gain. For a cubic on the normalized finite parameters it is

    3^21 * sum_(t=1)^500
      (981104+t)*1048577/((67473-t)*t*(t+1)),

whose exact ceiling is 159185671413625180, already independently
checked in the smooth-cubic supplier and recomputed by this verifier.
No pole-order bound, normalization parameter degree or splitting-field
size is used in that count. This node never changes the original field,
domain, complete cores or finite slope ownership.
