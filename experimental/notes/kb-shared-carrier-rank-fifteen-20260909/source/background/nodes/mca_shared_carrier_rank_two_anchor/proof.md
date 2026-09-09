# A Small Dual Flat Contains All Bad Evaluations

## 1. Bound The Span, Not Just One Determinant's Roots

Use the nondegenerate dual pairing between V x V and V* x V*.
The annihilator W^perp has dimension q=2s-r<s. If x is bad and
ell_x is nonzero, a nonzero pair (alpha_x,beta_x) satisfies

    (alpha_x*ell_x,beta_x*ell_x) in W^perp.

Indeed, such a pair is a nonzero left-kernel vector of evaluation on W.
Let ell_1,...,ell_d be linearly independent members of the bad
evaluation set. The corresponding vectors in W^perp are independent:
a relation with coefficients c_i implies separately
sum c_i*alpha_i*ell_i=0 and sum c_i*beta_i*ell_i=0, so
c_i*alpha_i=c_i*beta_i=0 for each i, hence c_i=0.
Consequently d<=q. Adding zero evaluation functionals changes no span.

Let E span all bad evaluation functionals, with dim E=d. Its
annihilator V_B in V has dimension s-d>=r-s>0 and vanishes on
EVERY point of B, including common zeros. Every member is divisible
by the product of the distinct linear factors X-x for x in B.
The space of all degree-<K polynomials divisible by that product
has dimension max(0,K-|B|). Therefore

    s-d <= K-|B|,  |B|<=K-s+d<=K+s-r.

The positivity r-s>0 is essential. With W=V x {0}, r=s, every
evaluation has rank at most one and the asserted root bound need not hold.

## 2. Count Good Anchors In The Original Domain

At a good point, evaluation on W has rank two. A nonempty affine
agreement section thus has dimension r-2. Subtract one pair in that
section. Both component differences belong to V and vanish at x,
so their common carrier is V_x. Evaluation on V is nonzero there,
giving dim V_x=s-1. The ambient degree bound is still K.

Put b=|B|. Each pair in S has at least A-b good agreements, while
each of the n-b good coordinates belongs to at most L such pairs.
Thus (A-b)|S|<=(n-b)L. Since A<=n, the ratio
(n-b)/(A-b) is nondecreasing in b<A. The bound b<=K+s-r<A
therefore proves (ANCHOR). This proves the claim even if S does not
span Z. It does not posit rank two for any subsequent child.

## 3. Full-Carrier Pencils Have Constant Direction

The required rational_line_cores.md normalizes a nonzero function-field
rank-one direction to

    W={(A1*H,-A0*H):H in T},

where A0,A1 are coprime polynomials, and T is an r-dimensional
polynomial subspace. If the direction is nonconstant, both A_i are
nonzero, and multiplication embeds T into V in each component.
If r=s, both images equal V. Hence multiplication by A1/A0 maps
V onto itself. Choose a nonzero v in V. The s+1 vectors
v,(A1/A0)v,...,(A1/A0)^s v are dependent over F, giving a nonzero
polynomial over F satisfied by the nonconstant rational function A1/A0.
This is impossible: every nonconstant element of F(X) is transcendental
over F. Equivalently, substitution into a coprime numerator/denominator
cannot annihilate a nonzero polynomial over F.

Thus a nonconstant direction has r<=s-1. If r=s, the primitive row
must have height zero, giving a constant direction. This proof works
over finite fields and with common zeros in V; neither a field extension
nor an empty-universal-core hypothesis is used.
