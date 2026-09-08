# Rational pencils without a row-degree hypothesis

Status: PROVED. Keep this node's exact support-margin setup, fixed
carrier h_*+C', dim C'=s>=1, m=K+d and 1<=T<=d. Assign every
selected raw<=T label to its chosen minimizing polynomial pair. These
pairs lie in (h_*,0)+C' x C'. A pencil means an AFFINE LINE in
F(X)^2, not necessarily a line with constant component direction over F.

The original bounded-row hypothesis can be replaced by the assertion
that the represented low pairs lie on one such pencil. Its primitive row
may have ANY degree; the earlier height cutoff was only used to derive
an exact pair identity, not in the subsequent counting proof.

More generally cover the represented low pairs by finitely many pencils,
assign each distinct pair to exactly one covering pencil, and retain its
assigned labels. Let U_i be the union of COMPLETE cores in group i,
e_i=n-|U_i|, and

    G_i=sum_(gamma assigned to i)(1-raw_gamma/(T+1)).

The original global margin resource gives

    |Gamma| <= C_s/(T+1)+sum_i G_i.                     (PC)

The resource is counted ONCE, not once per pencil. The following
groupwise bounds apply independently of labels in other groups.

## 1. Exact pair identities and primitive normalization

For a group with at least two distinct pairs choose f_* and one
nonzero difference (D_0,D_1). Put g=gcd(D_0,D_1) and choose the
coprime row

    A_0=D_1/g, A_1=-D_0/g, Q=A_0*a_*+A_1*b_*.

Collinearity over F(X) implies the POLYNOMIAL identity

    A_0*a+A_1*b=Q

for every represented pair in this pencil. At every x in U_i some
assigned pair matches the receiver, so A_0*u+A_1*v=Q there. This
includes roots of g; there is no source-incompatible gcd-root deletion.
The primitive A_0,A_1 have no common evaluation zero anywhere.

Write h=max(deg A_0,deg A_1). The existence of two distinct bounded-
degree pairs implies h<K. A singleton can be included in a pencil of
either kind and is handled directly in the finite consumer. No inequality
h<=d-T or deg Q<m-T is required by this pair-identity formulation.

## 2. Scalar parameterization and its dimension

Every polynomial pair in the group has

    (a,b)=(a_*,b_*)+(A_1,-A_0)*H,       deg H<K-h.

This H is a polynomial, not an uncontrolled rational function: Bezout
coefficients for the coprime A_i express it as a polynomial combination
of a-a_* and b-b_*. It lies in

    W={H:deg H<K-h, A_0*H in C', A_1*H in C'}.

If h>=1, then dim_F W<=s-1. Indeed both A_i are nonzero; equality
dim W=s would give A_0 W=A_1 W=C'. Multiplication by the
nonconstant rational function A_1/A_0 would preserve a nonzero finite-
dimensional polynomial space. Coprimality would force arbitrarily high
powers of a nonconstant denominator to divide one fixed polynomial, or
a polynomial numerator would give unbounded degrees. Both are impossible.
This is precisely the existing dimension-drop argument, with no height cap.

If h=0, the row is constant, and its polynomial kernel value Q has
degree <K. In the normalized finite chart, Q/A_0 belongs to h_*+C'.
In the infinite chart the second polynomial belongs to C', by using f_*.

Coverage defines a unique scalar receiver w_i on U_i by

    (u-a_*,v-b_*)=(A_1,-A_0)*w_i.

Its complete H-agreement sets there are exactly the represented pair
cores. There is no pole: at least one A_i(x) is nonzero at every point.
The parameter polynomials have degree <K even when the stronger
degree gain h is ignored. Thus, for |U_i|>=m, ordinary scalar LIST
caps at dimension <=s-1 on (|U_i|,K,m-t) bound the cumulative
represented H counts M_i,t when h>=1.

## 3. Preferred directions and groupwise low gain

Let E_i be the finite labels gamma with A_1(x)-gamma*A_0(x)=0
at some x in U_i. For h>=1, |E_i|<=|U_i|<=n. For h=0,
|E_i|<=1. Count only assigned labels in E_i; overlaps with other
groups cause no problem since labels were partitioned at the outset.

For an assigned LOW label outside E_i, scalar agreement at a point
of U_i is equivalent to joint pair agreement. Hence ALL its selected
noncore coordinates lie outside U_i. For a fixed pair, such outside
coordinates are disjoint over its assigned labels: two different slopes
agreeing there would make it a point of the COMPLETE pair core.

Put t_f=max(1,m-|H_f|). Then raw_gamma>=t_f. Summing the disjoint
noncore charges and telescoping gives

    G_i <= |E_i|+e_i*sum_(t=1)^T M_i,t/(t*(t+1)).        (G)

This remains true with the actual cumulative pair counts whenever U_i
is nonempty; counts at thresholds above |U_i| are zero. For h>=1
and |U_i|>=m, replace M_i,t by the rank-(s-1) scalar LIST caps
just described. For constant-direction pencils one may instead use an
appropriate scalar or JOINT list cap for the actual pair family.

In the finite empty-universal-core consumer, evaluation on C' is nonzero
on every covered U_i. Anchoring the JOINT pairs then gives

    M_i,t <= |U_i|*V_i,t/(m-t),

where V_i,t is the common-carrier dimension-(s-1) JOINT child cap on
(|U_i|-1,K-1,m-t-1). This last specialization DOES use the empty
universal core; it is not silently asserted for the generic setup.

Equation (PC) follows from theta=min(d+1,raw) and
theta>=T+1 off the LOW family. Combining it with (G) retains all
higher-margin labels and all preferred directions. The source outside
each U_i is arbitrary, including points in other groups' cores.

## 4. What is not inferred

A large pencil cover is not automatically affordable. The finite consumer
prints the allowable numbers of constant and nonconstant directions.
Neither affine dimension two over F(X) nor a small common carrier implies
a cover of that size. The 27-point polynomial parabola in the controls
needs at least fourteen lines despite using a two-dimensional carrier.

Component-polynomial rank two OVER F is compatible with a pencil over
F(X). The canonical selector excludes constant collision directions at
LOW labels, not the variable rational directions charged above.
The high-height control has zero full bounded E-row space but lies on one
rational pencil; the degree-free formulation strictly weakens the old gate.
