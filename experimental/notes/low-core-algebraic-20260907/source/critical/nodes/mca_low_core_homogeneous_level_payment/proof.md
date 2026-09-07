# Proof: fixed divisor patterns, then joint LIST incidence

## 1. Fixed algebraic function field and bounded poles

Work over k=algebraic closure of F. Choose a FINITE extension L of
k(X) splitting the fixed polynomial into affine factors:

    P(U,V)=c*product_(i=1)^h ell_i(U,V)^m_i,
    c!=0, h>=2, m_i>=1, sum m_i=e.                       (3)

The ell_i are distinct affine linear forms over L, with at least
two nonparallel directions. No bound
on the extension degree, number of zeros of R, or X-coefficient
heights will enter the numerical count. L has a normal projective
curve model C over k. Since k is algebraically closed, a rational
function on C with divisor zero is a k-star constant. These standard
facts follow from the curve/function-field correspondence and the
constant-global-functions theorem; precise primary references are in
`audit.md`. In particular equal divisors imply proportional functions.

For every polynomial pair of the fixed component degree bound, set

    z_i=ell_i(a,b) in L.

Each z_i lies in a FIXED finite-dimensional k-linear subspace of L:
use the coefficient polynomials 1,X,...,X^(K-1), the fixed linear
form coefficients and constants. Consequently its pole orders
are bounded at a fixed finite set of places, and it has no poles
outside that set. On (HL) all z_i are nonzero and

    product_i z_i^m_i=R/c.                              (4)

Enlarge the finite place set S to contain the zeros and poles of R/c.
Outside S all orders ord_P z_i are nonnegative and their weighted
sum is zero, so all are zero. At P in S, write the fixed lower
bounds as ord_P z_i>=-b_(i,P). Equation (4) also gives

    m_i*ord_P z_i <= ord_P(R/c)+sum_(j!=i) m_j*b_(j,P).

Thus every ord_P z_i lies in a fixed finite integer interval. Only
finitely many divisors div(z_i) can occur. Each possible divisor
identifies at most one projective class k-star*z_i in L. We do NOT
count those classes numerically or assert that only one exists.

## 2. Every irreducible coefficient component has dimension <=1

Let Y be any reduced irreducible component of the polynomial-pair
coefficient locus. The map (a,b) -> z_i is affine linear into the
fixed finite-dimensional function space above. Its k-points lie in a
finite union of one-dimensional linear subspaces, by section 1. That
union is Zariski closed. Since k-points are dense and Y is
irreducible, the WHOLE image lies in one such line. Choose a fixed
nonzero representative f_i, so on Y

    z_i=t_i*f_i,

where t_i is a scalar regular function on Y. It is obtained by a
k-linear functional taking f_i to one. It never vanishes at a point
of Y, by R!=0.

Choose two nonparallel forms ell_1,ell_2. Inverting their fixed
direction matrix over L, after subtracting the affine constants,
recovers (a,b) from (t_1*f_1,t_2*f_2).
This recovery is affine linear in the two scalars. Thus Y embeds in
an affine two-dimensional parameter space with coordinates t_1,t_2.
For precision, the inverse functions take values in a finite-dimensional
k-subspace of L^2; coefficient extraction is k-linear on its
polynomial-pair subspace and can be extended to the whole space.
This supplies an affine-linear inverse on Y, not merely pointwise
injectivity of a possibly inseparable map.

Substitute that inverse into (HL). Every affine factor remains
nonconstant in t_1,t_2, since the direction matrix and the two f_i
are invertible. The product has total degree e: its top homogeneous
part is a product of nonzero linear forms in the domain L[t_1,t_2].
Choose a k-linear functional on its finite coefficient span that is
nonzero on one degree-e coefficient. Applying it to P(a,b)-R
produces a NONZERO polynomial of degree e in k[t_1,t_2], vanishing
on Y. Its zero set has dimension at most one.
Hence dim Y<=1. This covers all components, not just generic or
positive-dimensional ones. Finite divisor classes were used only to
prove this dimension statement; none was silently discarded.

## 3. Retain the coefficient degree and count JOINT agreements

Clearing fixed rational X denominators in (HL) gives coefficient
equations of degree <=e in the 2s original affine pair coordinates.
The proper-section lemma in the already required graph supplier's
`algebraic_list_bound.md` covers this locus by a pure dimension-one
reduced variety of degree at most e^(2s-1). Its degree cost includes
all the possibly numerous divisor-pattern components. The auxiliary
splitting field from section 1 does not replace the MCA field.

The JOINT incidence proof is now shared in section 4 of the same
supplier's `algebraic_list_bound.md`. It removes universal JOINT
agreements (at most K-1), uses one proper component hyperplane
containing each remaining joint section, and counts incidences by
dimension with degree retained. Its bound Delta*Q^v, with
Q=(n-K+1)/(A-K+1), gives (1) at v=1,A=m-t. It never multiplies
two independent scalar caps. Sharing this general lemma in the
existing required supplier avoids a reverse dependency from its
moving-parabola extension back to this child.

## 4. Use the full margin-weighted gain, not a raw label cap

Partition pairs among source classes first, assigning their labels
with them. For a fixed pair f with complete core H_f, the mismatch
coordinates in the selected supports at different finite labels are
disjoint. Outside H_f the equation

    u(x)-a(x)+gamma*(v(x)-b(x))=0

has at most one solution gamma whenever it supplies a mismatch.
Each assigned label of raw r contributes r such points. For all
assigned labels of raw <=t on f, their total raw is at most
n-|H_f|<=n-m+t. Summing over distinct such pairs gives

    sum_(assigned gamma: raw<=t) raw <= (n-m+t)*M_t.

Now use the exact telescoping identity

    1-r/(T+1)=sum_(t=r)^T r/(t*(t+1)).

Together with (1), this proves (2). Using only an unweighted
LOW-label estimate loses useful reserve in the cubic mixed cover.
Coordinates in other pairs' cores remain charged: the complement
is of H_f, not of the whole union. HIGH labels and the original
margin resource occur once when the group gains are assembled.

## 5. Conic recognition and limits

In characteristic not two, write a conic as y^T*M*y+l^T*y+c=0
with M invertible. Its center is z=-M^(-1)*l/2; completing the
square gives (y-z)^T*M*(y-z)=-Q(z). If the projective conic is
nonsingular, Q(z)!=0. The nondegenerate binary quadratic has two
distinct factor directions over a finite extension, so (HL) applies.

For rank-one M this reduction does not apply. Likewise R=0 and
a single factor direction both allow coefficient components of
dimension s; explicit controls reject those missing hypotheses.
No claim is made that the forced degree-seven relation always has
the recognized form or only affordable factors.
