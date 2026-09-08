# The quartic multiplier space controls height, exceptions and core density

Current scope: the entire 8764..9526 interval is now paid by
`quartic_strip_payment.md`. The independent restrictions below remain
proved at their stated hypotheses, but no longer describe an unpaid
interval. The new closure does not require these stronger restrictions.

Status: PROVED. Use the same canonical normalized source and LOW_500
kernel as `quartic_obstruction.md`, now on the unpaid 8764..9526 range.
Suppose its gcd has degree four. In the unpaid alternative it is exactly
the single geometrically integral quartic, not just a proper factor of a
larger gcd. Let G be its primitive F[X,Y,Z] representative. Put

    A=J+66972, w=J-1, n=1048576+J,
    weighted_degree(G)=4w+H, H>=0,
    S=A-4w-H,
    L=1965404-196J,
    D(H)=sum_(i=0)^4 (i+1)*max(S-i*w,0).

Then the following are necessary for the quartic alternative:

    H <= floor((111J-960724)/15),  8764<=J<=9099;
    H <= floor((146J-1295624)/10), 9100<=J<=9526.       (Height)

The number of represented LOW pairs off G is at most

    0 on 8764..9014;
    1 on 9015..9276;
    2 on 9277..9444;
    3 on 9445..9524;
    4 on 9525..9526.                                  (Off)

Writing U for the COMPLETE LOW core union, there is also the bound

    n-|U| <= D(H)-L <=111J-960724,
    |U|>=2009300-110J.                                (Union)

When no LOW pair is off G, every received pair on U lies on G and the
full kernel is exactly G times the full multiplier space counted by D(H).
These are universal restrictions, not a count proving that the quartic
source is affordable. The LOW-101 interval through 8763 remains closed.

## 1. Keep the true multiplier degree

The full W8 kernel E has dim_F E>=D8-|U|>=D8-n=L>0.
Gauss division, already proved in this node, writes every Q in E
uniquely as G*R with R in F[X,Y,Z]. Its pair degree is <=4 and its
weighted degree is <S. Multiplication is injective. Hence S>0 and

    dim E<=D(H), L<=D(H).

The maximum signs in D(H) are essential: the last multiplier block
can disappear on the upper part of the interval. In particular the
untruncated linear expression is not a valid upper bound everywhere.

Set S0=A-4w=66976-3J. If S<=3w, then D(H)<=10w. But

    L-10w=1965414-206J>=3058>0

through 9526. Thus S>3w, and only the last block can be absent:

    D(H)=max(15S-40w, 10S-20w).

Subtract L in the two cases to get

    D(H)-L=max(111J-960724-15H, 146J-1295624-10H).

Consequently H is at most the larger of the two displayed quotient
floors. Their real-valued order changes between 9099 and 9100,
since their difference has the sign of 216J-1965424. This proves
(Height), including the truncated-block transition. Examples of the
ceilings are 805 at 8764, 6130 at 9294 and 9517 at 9526.

This bounds the coefficients of the TOP binary quartic by degree H.
A lower pair-degree i coefficient can have degree up to (4-i)w+H;
it is false to call H a bound on every X-coefficient of G.

## 2. Distinct off-curve pairs consume separate multiplier blocks

Suppose t distinct represented pairs f_j=(a_j,b_j) lie off G, with
1<=t<=5. Every multiplier R of an element of E vanishes identically
on each f_j: G(f_j)!=0 and Q(f_j)=0 in the polynomial domain.

Choose c in F such that z_j=a_j+c*b_j are distinct polynomials.
Each pair of indices forbids at most one constant c, so more than
binom(t,2) field elements suffice; the actual field easily has this size.
Define the Newton polynomials

    P_0=1,
    P_i=product_(j=1)^i (Y+c*Z-z_j(X)), 1<=i<t.

Each has pair degree i and weighted degree <=i*w. Multiply P_i by
every X-polynomial of degree <S-i*w, using the zero space when this
bound is nonpositive. Their images under evaluation at the t pairs
are linearly independent blockwise: at f_1 only the first block survives;
then at f_2 the first remaining block is a nonzero polynomial multiple;
continue triangularly. No division at a code coordinate is involved.

Thus the evaluation map from the full multiplier space has rank at least

    R_t(H)=sum_(i=0)^(t-1) max(S-i*w,0),

and necessarily

    L<=dim E<=D(H)-R_t(H).                            (N_t)

Every coefficient in D(H)-R_t(H), as a sum of positive-part blocks,
is nonnegative. It therefore decreases with H>=0, so it is at most
D(0)-R_t(0). All five blocks at H=0 are positive through 9526.
Direct subtraction gives L-(D(0)-R_t(0)) as follows:

    t=1: 1027700-114J, positive through 9014;
    t=2: 1094677-118J, positive through 9276;
    t=3: 1161655-123J, positive through 9444;
    t=4: 1228634-129J, positive through 9524;
    t=5: 1295614-136J, positive through 9526.

Strict positivity contradicts (N_t), proving (Off). This is stronger
than even the direct 16-point Bezout bound at gcd degree four. The
actual-H test L>D(H)-R_t(H) can give a still smaller exception count.

The inequality must be strict. As an abstract multiplier control, take
w=1,S=3 and pair degree <=1, so D=7. At the pair (0,0), evaluation
has rank exactly 3 and kernel span{Y,XY,Z,XZ} of dimension D-S=4.
Multiplying that kernel by G=Y-1 preserves an off-G zero pair and
has gcd G. This is a sharp algebraic rank control, not a canonical
MCA source or a counterexample to the source theorem.

## 3. Density and exact received-curve coverage

Combining D8-|U|<=dim E<=D(H) gives (Union). Since D(H)<=D(0),
its coarser last bound follows from D(0)-L=111J-960724. At J=8764
it gives |U|>=1045260 of n=1057340 points; at 9526 it gives
|U|>=961440. No previous arbitrary upper bound on U is assumed.

If every represented LOW pair lies on G, each x in U belongs to one
of their complete joint cores. Polynomial identities then give
G(x,u(x),v(x))=0, even at zeros of leading coefficients. Every allowed
multiple G*R therefore vanishes on U and belongs to E. The reverse
inclusion is Gauss division, so E is the full multiplier space times G.
This conclusion holds in particular throughout 8764..9014.

## 4. Projection heights and an off-curve agreement exclusion

If the top binary quartic contains a primitive linear factor
A0*Y+B0*Z of multiplicity m0, its coefficient height h satisfies
m0*h<=H. Gauss division makes the remaining binary factor polynomial,
and X-degree is additive in its product with that linear power.

In particular, a quartic polynomial projection graph has top binary form
c(X)*(A0*Y+B0*Z)^4, so h<=floor(H/4). Hence h<=2379 throughout
this interval, and h<=1532 through 9294. The next height ceiling at
9295 is 6144, so that latter implication is not extended for free.

If f is an off-G LOW pair, then G(X,f) is a nonzero polynomial of
degree <=4w+H. On at least A-(4w+H)=S points of f's complete core,
the received pair is therefore OFF G. No on-G pair can agree jointly
there. The height bound gives S>=28881 on the entire interval, with
the minimum envelope at J=9526. Such points remove possible agreements
from an auxiliary on-G LIST count only: all original scalar defects,
HIGH records and off-curve pair labels remain in the source accounting.

The finite consumer uses these proved height/agreement facts in
`quartic_projection_graph_payment.md`. It is not assumed here that the
general integral quartic is a projection graph or has a rational normalization.
