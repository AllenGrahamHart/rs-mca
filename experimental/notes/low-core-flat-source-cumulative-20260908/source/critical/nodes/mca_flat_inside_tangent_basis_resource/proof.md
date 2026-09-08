# Proof By Coupling Calibrated Tangents Before Bounding Their Signs

## 1. Retain The Actual Inside Extension Identity

The required maximum-density theorem supplies the actual quotient basis
count P(M-t), including the complete flat locator and both inherited
degree and density bounds. Its proof section 2 counts disjoint classes
with exactly b inside points. Write E_b for the number of actual ordered
independent b-tuples inside the core; E_0=1 and E_1=t. For such a
tuple let y_b be the number of inside points outside its span. Then

    sum_(ordered independent b-tuples) y_b=E_(b+1).

The outside completion count for that tuple is at least
R_(j-b)(y_b)=prod_(i=0)^(j-b-1)(c+i-y_b). Here y_b<=t<=a<c, so
all factors are positive. The factor binom(11,b) comes from disjoint
interleavings. The construction and this identity do not require j<=5;
only the previous sign-discarding shortcut was rank-limited.

For k>=1, R_k(y)>=(c-y)^k. The latter function is convex on y<c.
Its tangent at ANY q<c gives, for the actual y>=0,

    R_k(y)>=p^k+k*p^(k-1)*(q-y)=L_k-D_k*y.

The k=0 identity uses L_0=1,D_0=0. Multiply by binom(11,b), sum
the b>=1 classes, and use the EXACT extension identity. The resulting
expression is

    11*L_(j-1)*t+sum_(b=2)^j C_b*E_b.

The b=0 class contributes R_j(t)>=(c-t)^j separately. This proves
the signed expression BEFORE any estimates on E_b are made.

## 2. Bound Each Coefficient In Its Correct Direction

After choosing i independent inside points, their span contains at most
i*h original coordinates by maximum density. It therefore contains at
most i*h points of the actual inside set. Greedy extension gives
E_b>=prod_(i=0)^(b-1)max(t-i*h,0). If a factor is nonpositive the
lower bound is simply zero; no false inside-rank assumption is made.
Trivially E_b<=t^b. Thus positive C_b use E_b^- and negative C_b
use E_b^+, proving (SIGNED). The calibration is a real inequality
parameter, not a fractional field or a realized polynomial degree.

For a box t0<=t<=t1<c and h<=h1, the same proof with q=t1 gives
the certified lower expression

    (c-t1)^j+11*L_(j-1)*t0
      +sum_(C_b>=0) C_b*prod_i max(t0-i*h1,0)
      +sum_(C_b<0) C_b*t1^b.                       (BOX)

Every L_k is positive because q>=0 and p>0. A consumer may multiply
this by a positive lower bound for P only after proving (BOX)>0.

## 3. Use The Complete Core Without Reselecting The Witness

Let H be the full joint agreement set of the already chosen pair.
The old witness has at least m-T=M joint-core points, so |H|>=M.
Its intersection with the flat is exactly t<=a<M. Choose all t inside
points and M-t points from H outside A. This is possible because
|H outside A|>=M-t. These extra core points need not belong to the
old selected size-m witness.

Every point in H still satisfies the ORIGINAL scalar equation for the
same h_gamma=a_gamma+gamma*b_gamma. The old witness supplies an actual
defect outside H, since full-code badness forces raw>=1. A core basis
plus that defect is independent in the original incidence representation.
Its unique defect position recovers the insertion, giving twelve distinct
ordered tuples per basis. Distinct original labels cannot share an
independent tuple. Nothing here changes the selected witness, its raw
margin, its minimizing pair or its projected-pair group.

Any valid basis lower count can be used, not only (SIGNED). In particular
the older j<=5 coupled count applies at the heavy group's full occupancy,
instead of minimizing over occupancies that the group cannot have.
HIGH records keep their separately proved completed-weight charge.

## 4. The Two-Cost Resource Inequality

Let H and L be the disjoint heavy and light label counts. Then
T_up>=beta_L*L+beta_H*H. If beta_H<=beta_L, rearranging and using
H<=Q_H proves (TWO-COST). If beta_H>beta_L, every record costs at
least beta_L and |Gamma|<=T_up/beta_L already. This explains the
positive-part coefficient and avoids inserting an upper cap into a
negative-coefficient term. No heavy group gives the same light-only bound.

The bound is on one original source and one counted label partition.
Different possible flats, parameter boxes or whole-source alternatives
combine by maximum, never by an uncharged sum of their upper bounds.
