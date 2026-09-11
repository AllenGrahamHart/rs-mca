# Count Conic Pairs And Charge Off-Conic Agreement On The Exception Set

Put R=1048576,d=67472,J1=21499,T=43 and E0=276035. Fix the
ORIGINAL source and owner assignment from the statement. Its actual
minimizing pairs belong to(h_*+V) x V, dim V=11. No label or raw
value is reselected. Classify each represented pair f=(a,b) by the
POLYNOMIAL identity Q(X,a(X),b(X))=0. This classification is fixed
across all raw cutoffs.

## 1. Every Off-Conic Pair Must Agree Often On E

If f is off the conic, the substituted polynomial is nonzero of degree
at most2J, including all content and coefficient-root factors. On the
good receiver set D minus E, each joint agreement with f is a root
of that polynomial. There are at most2J such points.

A pair represented at cutoff t<=43 has complete original joint core
of size at least m-t. It consequently has at least

    A_off=m-t-2J=d-t-J

joint agreements on E. If E has fewer points, no such pair exists.
Otherwise enlarge E, if necessary, to any E0-point subset of the
original domain. The original received values are retained. Every
off-conic pair still has at least A_off agreements there.

This is an auxiliary joint LIST count only. It does NOT reapply an
MCA source theorem, remeasure a raw defect, or change a probability
denominator.

## 2. Shared-Carrier Joint LIST Pays Those Pairs

On the auxiliary domain the degree is still<J and the common polynomial
carrier dimension is at most11, NOT the pair-affine dimension up to22.
Set r=E0-J and w=d-t-2J. Throughout the printed interval w>=24431>0
and r>w. The same-field shared-carrier LIST supplier, iterating its
dimension bound(S) from U0=1, gives

    M_off,t <= floor(product_(i=1)^11(r+i)/(w+i))
             <= floor(((r+1)/(w+1))^11).

Floors at intermediate stages can only improve this bound. The common
carrier is injectively restricted since E0>=J; no polynomial is lost.

For fixed E0,t the ratio

    (E0-J+1)/(d-t-2J+1)

increases with J, because its derivative has positive numerator
2E0-d+t-1. Thus the ENTIRE original interval is bounded by

    O_t=floor((254537/(24475-t))^11).                  (OFF)

The auxiliary domain need not be smooth. The joint-LIST theorem works
on arbitrary distinct points in the SAME original field.

## 3. The Three Conic Types Have One Uniform Count

Write q_t=(R+1)/(d-t+1). Complete original cores have size at least m-t.
The proved conic suppliers give these original polynomial-pair counts:

- Rank-two quadratic part: at most floor(2^21*q_t), by the
  affine-product coefficient-dimension-one theorem.
- Rank-one part with constant quadratic direction: at most
  floor(2^5*q_t^6), by the rational-coefficient graph theorem.
- Rank-one part with moving quadratic direction: at most
  floor(2^17*q_t^5), by the tangent-equality dimension theorem and
  the original-coordinate joint algebraic LIST bound.

These exhaust nonsingular projective conics in the original odd
characteristic. Fixed rational coefficients or auxiliary parameters are
used for the geometric proof only, not to change the polynomial code.
Since2<=q_t<=4096, the third bound dominates the first two. Therefore

    I_t=floor(2^17*((1048577)/(67473-t))^5)             (ON)

bounds every on-conic pair family. The potentially large rational
parameter degree is never substituted into LIST.

## 4. One Original Resource And Once-Only Ownership

For one represented pair, selected defects from its different finite
labels are disjoint: outside the complete pair core the equation
(u-a)+gamma*(v-b)=0 determines at most one gamma whenever v-b!=0.
Thus its TOTAL original raw weight at cutoff t is at most

    n-|H_f|<=n-(m-t)=R-d+t=:c_t.

Summing over the two disjoint pair classes gives

    Omega_t=sum_(raw<=t) raw <=c_t*(I_t+O_t).

For every positive integer raw tau the EXACT identity is

    1=min(tau,44)/44
      +tau*sum_(t=tau)^43 1/(t*(t+1)),                (ID)

with an empty sum for tau>=44. The original min-envelope supplier pays
sum min(raw,44) by W44=581590844909990298 across this whole J interval.
Consequently all original labels plus near obey

    |Z_bad|<=floor(W44/44
             +sum_(t=1)^43 c_t*(I_t+O_t)/(t*(t+1)))+134944
            =274980278712737789.

The on/off counts do not receive separate copies of W44 or near.
All high raw values are covered by(ID). No source class is discarded
without paying it and no assumption on P1/P2 rank is introduced.

The exact certificate computes all43 cutoffs and their rational sum.
At E0+1 the SAME upper recipe is274986666760617051>B*. This only
locates this recipe's exception threshold; it is not an unsafe witness.

## 5. Transport A Degree-One Terminal Conic Back To The Source

Let q(A,B,C) be the homogeneous quadratic defining the parameter conic
in the corollary. Put v=(Y,Z)-f_*(X), and define

    Q(X,Y,Z)=q(adj(M(X))*v, F(X)*det M(X)).

For f=f_*+F M y, its three homogeneous arguments are F det(M)*(y,1),
so Q(X,f)=0. Since F det M is nonzero, the coordinate change is an
invertible affine change over F(X); the resulting projective conic is
nonsingular. No specialization at a root of F or det M is deleted.

For a generic pair of original degree<J, each of the first two
arguments has degree at most J, while the third has degree at most
deg F+2<=J. Hence Q has original weighted degree at most2J.
This can also be read directly from its coefficient degrees: linear
arguments have Y/Z coefficient degrees<=1 and constant degrees<=J.

On every COMPLETE original core in U the received pair equals its
represented f, so Q(x,u(x),v(x))=0. Thus |E|<=n-|U|<=276035, and
the preceding whole-source theorem applies.

This is an explicit sufficient original-source condition. It does not
show that the locally constructed obstruction admits such a source lift,
or that arbitrary conic-free/high-primitive-degree terminals are paid.
