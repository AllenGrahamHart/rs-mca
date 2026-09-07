# High-height pencil with zero bounded row space

Use E=F_19 and F=E(beta), beta^6=2. Since beta^19=8*beta and
8 has order six in E, the defining root has degree six over E. Set

    K=4, d=3, m=7, T=1, ell=d-T=2,
    P=X^3+beta*X,       C'=span_F{1,P}.

On the three six-point groups 0..5, 6..11 and 12..17, let the
received pair be f_i=c_i*(P,1), where (c_0,c_1,c_2)=(0,1,beta).
Their complete pair cores are exactly these disjoint groups, since their
second components are distinct constants. The primitive pencil row is
(1,-P), of height THREE, strictly above ell=2. Both components of any
pair difference are F-linearly independent polynomials: this is a rational
pencil, not a constant component direction.

The polynomial P is injective on E: if P(x)=P(y) with x!=y, then
beta=-(x^3-y^3)/(x-y) would belong to E. Thus the rational-direction
set gamma=-P(x), x=0..17, has exactly eighteen finite labels.

At such a gamma the source-piece explanation c_i*(P+gamma) agrees
on its six-point core plus the unique root point when that point lies in
another group. Exactly two pieces therefore have complete agreement seven.
Any other carrier explanation alpha*P+eta agrees at most once per group,
by injectivity of P, hence at most three times. Outside the eighteen
printed directions no carrier explanation reaches seven agreements.

Every one of these eighteen labels has maximum raw one, even after
maximizing over ALL explanations and bad supports. At a source-piece
explanation the second constant c_i matches six points and misses the
root point. Any degree-<4 containing polynomial is pinned to c_i by
the six core points, contradicting that defect. The strict canonical
guard 2T<d holds. Assign the label from group j to the pair in group
j+1 modulo three so that all three pairs are represented.

All eighteen bad labels are preferred rational-direction labels. Thus the
generic cost |E_i|<=|U_i| can be attained, even by a canonical LOW
family. Omitting that charge would give zero when U_i is the entire domain.

## No bounded E-valued row, and no old exact relation

Let R=(R_0,R_1) have degree at most two, and allow an offset Q of
degree <K+ell=6 such that R*y-Q is E-valued on the eighteen-point
union. On the six points of the zero piece, Q takes E-values, so its
coefficients belong to E by interpolation. The other two pieces imply
that both W=R_0*P+R_1 and beta*W are E-coefficient polynomials:
their degrees are at most five and each is E-valued on six E-points.
Since beta is not in E, W=0 coefficientwise. But deg P=3 and
deg R_i<=2, so R_0*P+R_1=0 forces R_0=R_1=0.

Thus the FULL bounded E-row space is zero. In particular there is no
nonzero row with this degree bound and received remainder degree <6,
whereas the exact high-height row (1,-P) annihilates every represented
pair and the received source on the union. This shows that the new
pair-pencil premise is not equivalent to the old bounded-row premise.
It is a small source-class control, not a deployed-row counterexample.

The verifier checks all two-point-pinned carrier explanations at all
eighteen labels and a 60x36 matrix over E for the FULL bounded row
space. It does not enumerate degree-<4 codewords over F.

## A pencil-cover guard

Over F_101(X), the 27 pairs

    f_t=(t*X,t^2),       t=1,...,27,

belong to (<1,X>)^2. Any three are noncollinear: their determinant is
a nonzero scalar times X, with coefficient the product of their three
parameter differences. Thus each affine F(X)-line contains at most two
of them, and at least fourteen lines are required. Every secant has
nonconstant direction, because t+u is nonzero in F_101.

This polynomial-family example rejects inferring a thirteen-pencil cover
from affine dimension two or common carrier dimension alone. It is not
claimed to be a canonical over-budget MCA source on a deployed row.
