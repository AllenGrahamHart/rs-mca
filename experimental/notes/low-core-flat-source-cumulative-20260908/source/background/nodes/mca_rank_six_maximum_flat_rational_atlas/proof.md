# Proof By Proper-Join Exclusion And Polynomial Cross Determinants

Everything below uses elementary linear algebra, polynomial division and
the distinct-root bound. No unproved basis-envelope curvature or list census
is imported. The existing maximum-density and complete-flat counting nodes
are antecedents for the geometry, not additional unproved premises.

## 1. Root Capacity And Proper-Join Exclusion

If an evaluation flat has rank r<11 and contains b distinct H-points,
its polynomial annihilator has dimension11-r. Division by the full locator
embeds that space into degree<K-b polynomials. Thus

    b<=K-11+r.                                        (ROOT)

The maximum h may be taken over complete flats spanned by their points.
For ANY subspace of rank r, its contained H-points number at most rh:
replace the subspace by the span of those points if necessary.

Take two distinct maximizing rank-six flats A,B. If their join has proper
rank u, then7<=u<=10 and their subspace intersection has rank12-u.
Their coordinate union therefore has size at least

    12h-(12-u)h=u*h.

Applying ROOT to the join gives u(h-1)<=K-11. But h>(K-4)/7
implies7(h-1)>K-11, and u>=7, a contradiction. Thus their join
has rank11, intersection rank1, and coordinate intersection at most h.
Annihilator dimension and pairwise zero intersection follow by duality.

The same ROOT bound shows that under this h gate no maximizing proper
flat can have rank>=7. This does not exclude ranks1..5.

## 2. A Per-Core Packing Bound

Write L for the number of maximizing rank-six flats. For x in H, let
t_x count how many members contain x. Each has a=6h points, so
sum_x t_x=La. Pairwise coordinate intersections are at most h, hence

    sum_x t_x^2 <= La+L(L-1)h.

Cauchy gives (La)^2<=M*sum_x t_x^2. For L>0, cancel L and obtain

    L*(a^2-Mh)<=M*(a-h).

When36h>M, substitute a=6h>0 and divide by the POSITIVE coefficient.
This proves PACK. The L=0 case is immediate. No analogous division is
permitted if36h<=M; in particular M must not silently become the whole
original evaluation-domain length.

## 3. Three Actual Annihilators Give One Rational Direction

We first prove the general three-flat version. Pairwise full joins give
dim W_A=dim W_B=dim W_C=5 and pairwise zero intersections. Consequently
U=W_A+W_B is a direct sum of dimension10. The space W_C intersect U
has dimension d_C in{4,5}. Every w there has a UNIQUE representation

    w=P_A*f+P_B*g, f in U_A, g in U_B,
    deg f<k_A, deg g<k_B.

Neither component of a nonzero w can vanish: otherwise w would lie in
W_C intersect W_A or W_C intersect W_B. For two represented vectors
(f_1,g_1),(f_2,g_2), every x in C outside A union B satisfies

    P_A(x)*f_i(x)+P_B(x)*g_i(x)=0,

with P_A(x),P_B(x) nonzero. Hence f_1*g_2-f_2*g_1 vanishes at all
those points. Its degree is at most k_A+k_B-2. Under the printed strict
root-count hypothesis it is identically zero, for EVERY such pair.

Choose a nonzero pair and divide its polynomial gcd to get coprime
nonzero (f_C,g_C). Every represented pair has zero cross determinant
with this one. Coprimality in F[X] then forces it to be
(f_C*t,g_C*t) for a UNIQUE polynomial t. These t form a d_C-dimensional
F-space T_C. The direction is unique up to a nonzero F-scalar.
The polynomial R_C=P_A*f_C+P_B*g_C is nonzero: otherwise any nonzero
t in T_C would give a zero represented vector in the direct sum.

Let e=max deg(t) over nonzero t in T_C. A d_C-dimensional polynomial
space requires e>=d_C-1. Degree addition in F[X] gives

    deg f_C+e<=k_A-1, deg g_C+e<=k_B-1.

This proves the component degree bounds. Since each R_C*t vanishes at
every point of C, its full squarefree locator divides their polynomial
gcd R_C*G_C, up to a nonzero scalar. Dividing T_C by G_C leaves the
same dimension d_C, so deg G_C<=e-d_C+1. The displayed bounds on e
give LOCATOR. This retains roots of G_C and of both components.

## 4. The Density Gate Supplies The Strict Root Count

For three maximizing rank-six flats, all sizes are a=6h, and both
intersections with C have at most h coordinates. Thus

    |C outside (A union B)|>=a-2h=4h.

The required comparison is4h>2(K-a)-2, equivalently16h>2K-2.
For K>=26, the density hypothesis implies

    16h >16(K-4)/7 >2K-2,

the last strict inequality being equivalent to2K-50>0. Section3
therefore applies uniformly. Completeness is with respect to this H;
no whole-source locator is substituted for its locator.

## 5. Distinct Flats Give Distinct Rational Directions

Fix A,B. For any coprime nonzero direction (f,g), the pairs

    (f*t,g*t) in U_A direct_sum U_B

form a space of dimension at most5: projection to the first component
is injective into U_A. Its image in U has the same dimension. If two
different C,D gave this direction, both W_C intersect U and W_D intersect U
would be subspaces of that at-most-five-space of dimension at least4.
They would intersect nontrivially, contradicting W_C intersect W_D=0.
This proves the claimed injectivity. It counts atlas directions for this
one core; it does not identify different cores or finite slope labels.

## 6. Retain A Quantified Band Below The Maximum

Let b satisfy the near-maximum statement, and put e=6h-b>=0. Two distinct
rank-six flats of size>=b with a proper rank-u join have coordinate union
at least2b-(12-u)h=u*h-2e. ROOT would give

    u(h-1)<=K-11+2e.

But u>=7 and7(h-1)>K-11+2e is exactly the stated2b-5h>K-4.
Thus all such joins are full. For any three, C outside A union B has
at least b-2h points, while k_A+k_B-2<=2K-2b-2. The strict root
comparison follows from

    3b-2h=16h-3e
           >16(K-4)/7+11e/7 >2K-2,

using7h-2e>K-4 and K>=26. Sections3 and5 give the rational atlas,
without asserting equality of flat sizes. To pack the family, choose any
b coordinates in each member. These subsets still have pairwise
intersections<=h. Apply section2 with a=b, dividing only if b^2>Mh.
This proves the robust bound without counting unqualified near-dense flats.

## 7. Exact LOW-Core Constants

Put D=67466, M=D+J, K=J. The density gate gives

    5M/(36h-M) < 35(D+J)/(29J-7D-144),               (BOUND)

whenever the latter denominator is positive. On20481..22999 it is.
The right side is strictly decreasing: differentiating leaves numerator
-35*(36D+144) divided by a positive square. At J=20481 it is
3078145/121543, strictly between25 and26. At J=22500 it is
3148810/180094, strictly between17 and18. Integer L consequently has
the two claimed uniform caps. The independently written arithmetic check
also proves these interval inequalities directly by affine endpoint guards.

Since a=6h>6(J-4)/7, k=J-a<(J+24)/7. For J<=22999, k<3289,
so k<=3288. Because d_C>=4, both component degrees are at most3284.
These are actual polynomial degrees, over the unchanged original field.

For the MCA interface, fix the same raw<=6 record and its minimizing pair.
Its joint core has at least J+67466 coordinates. Empty universal carrier
core makes all those joint-core evaluations nonzero. Choose the fixed
M-point core used by the prior basis count, then apply this theorem.
No receiver descent, new explanation, label removal, near add-back or
bad-slope payment is performed. The original remaining gap is unchanged.
