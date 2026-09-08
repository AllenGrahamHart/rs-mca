# Projected Receiver Pairs And A Shared Tuple Budget

Status: PROVED by the hand proof; external independent review remains due.

Use a fixed actual dimension-s degree-<K carrier V, affine translate h_*+V,
n distinct points and one received pair (u,v). Every original finite label
gamma has a scalar-agreeing size-m support, m=K+d, d>=1, bad in the
FULL degree-<K pair code. The universal carrier core is empty. Freeze one
minimizing pair (a_gamma,b_gamma) in (h_*+V) x V per selected record.

Let F be a proper evaluation flat of dimension j, 1<=j<s, spanned by
its complete set A of a NONZERO original evaluations. Suppose every
hyperplane of F contains at most a-Delta such coordinates, 0<Delta<=a.
For a maximum-density flat one may take Delta=a/j, without a new premise.

Group records by the restrictions of BOTH pair polynomials to A. Distinct
projected pairs have complete joint cores in A intersecting in at most
a-Delta points. Thus at most one group has core size t>a-Delta/2.

## Full Child Cap And Complement Bound

The heavy group's complete-locator transport has at most a-t exceptional
ORIGINAL labels. Its retained child has length n-a, degree K-a, agreement
m-t, actual ambient carrier dimension s-j, and EMPTY UNIVERSAL CORE.
Its selected span may be smaller; its field and finite labels are unchanged.

Let U>=1 uniformly bound all affine-dimension-at-most-(s-j-1) selected
families on the anchored rows, allowing the zero code when necessary.
For fixed R=n-K it suffices to supply a full uniform cap at baseline gap d:
the actual larger gap d+a-t can be reduced by exact bad-subset selection.
The existing scalar-incidence ledger therefore gives a heavy-group bound

    H(t) <= (n-a)*U/(m-t) + a-t.                    (CHILD)

Every other projected pair has at most b(t)=2*a-Delta-t agreeing points
in A. Without a heavy group, all such core sizes are <=a-Delta/2.
Unlike fiber colors, these sets can overlap; disjointness is NOT assumed.

## Count Heavy Records On The Same Resource

Suppose every record has at least eta*beta_max independent incidence
tuples, 0<=eta<=1. Suppose all light records with core occupancy <=b
have at least beta(b)>0 tuples, with beta(b)<=beta_max. Let T_up bound
the total independent ordered incidence tuples of the ORIGINAL source.

Then, when the heavy group exists,

    |Gamma| <= T_up/beta(b(t)) + (1-eta)*H(t).       (SHARED)

This charges the heavy group for its tuple consumption. Without a heavy
group, |Gamma|<=T_up/beta(a-Delta/2). A supremum of the displayed heavy
bound over the relaxed closed interval a-Delta/2<=t<=a also covers that case.

The finite consumer provides beta, eta and U from proved suppliers. This
is a quantified counting theorem, not a new speculative conditional leaf.
Its lower-rank child may NOT be assumed post-near. No original near
add-back, all-source rank bound, owner atom or prize closure is supplied here.
