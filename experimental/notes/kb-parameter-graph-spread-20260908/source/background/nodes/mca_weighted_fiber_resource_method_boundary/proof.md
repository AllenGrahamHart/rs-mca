# Proof With An Actual Raw-One Record

## 1. Construct The Carrier On Any Distinct Evaluation Domain

Fix any n-point domain D in the original field. Choose H0 subset D of
size m-1, A subset H0 of size a as in the statement, and x0 outside H0.
These sets exist since0<a<m-1<n. Let P_A be the full locator and set

    V=span{1,P_A,X*P_A,...,X^9*P_A}, h_*=0.

The eleven polynomials are independent: evaluating a proposed relation
on A first eliminates its constant, then polynomial multiplication by
P_A is injective. Their maximum degree is a+9<J. Evaluation on D and
H0 preserves rank by root count, since both lengths exceed J. The
constant1 makes every evaluation nonzero, so the universal core is empty.

Every A-point has projective row(1,0,...,0). Outside A the ratio XP_A/P_A
recovers X, so all other projective rows are distinct and none equals
the A-row. The complete source partition is EXACTLY one a-point fiber
and n-a singletons. This construction needs no domain enumeration or
field change; it works also on allowed punctured smooth domains.

## 2. An Eligible Record With No Secant Exceptions

Set the received pair to(0,0) on H0,(1,1) at x0, and(0,1) elsewhere.
At gamma=-1, the zero explanation agrees exactly on S=H0 union{x0},
which has size m. Both components vanish on at least J points of S but
are nonzero at x0, so neither can equal a degree-<J polynomial there.
In particular S is bad for the FULL degree-<J polynomial pair code.

The zero second polynomial lies in V and misses v on S only at x0.
A zero-mismatch second polynomial is impossible by the same root argument.
Thus the selected raw mismatch is exactly one and H0 is the COMPLETE
joint core of the selected polynomial pair(0,0).

On A the normalized received pair is identically(0,0); singleton fibers
produce no secants and there are no carrier zeros. The secant supplier's
exception set is therefore empty. In particular this record survives it.

For14000<=J<=17000 the largest fiber is J-2001<J-2000. Below14000
the degree-2000 theorem has no stated scope. The degree-6000 and arc
theorems begin above17000. Thus none of these previously paid source
alternatives disposes of this construction in the printed interval.

## 3. Canonical Raw One And Exactly Two Bad Slopes

For ANY finite gamma, the received scalar takes value0 on H0, valuegamma
on D minus S, and valuegamma+1 at x0. A nonconstant degree-<J explanation
has at most J-1 roots at each of its0 and gamma levels, plus at most x0.
It therefore agrees at most2J-1<m times, since J-1<67472. If gamma=0
the levels coalesce and this upper bound is merely looser. Thus only
constant explanations can have size-m supports.

For gamma not in{0,-1}, constant0 agrees only on H0, of size m-1.
Constantgamma agrees only on D minus S, where the polynomial pair(0,1)
explains BOTH received components. Constantgamma+1 agrees only at x0.
Every other constant has no agreements. Hence these labels are not bad.

At gamma=-1, only constant0 has a BAD size-m support: it agrees exactly
on S. Constant-1 has only the completely pair-explained complement. Thus
the zero explanation and S are the ONLY eligible choice, even in the full
degree-<J code, and maximal-raw selection at this label is forced to be one.

At gamma=0, zero agrees on D minus{x0}. Choose y in D minus S, which
exists because n>m, and use H0 union{y}. It is a full-code-bad size-m
support: v vanishes on at least J H0-points but equals1 at y. No other
constant has an eligible support. The bad-slope set is exactly{0,-1}.
Both selected explanations must be zero, and the error words u and u-v
have affine rank one since v is not identically zero. This explicitly
shows why the construction is not an original rank-twelve family.

## 4. Upper-Bound The Entire Record, Not A Chosen Subcollection

On H0 the incidence normals are(evaluation_V(x),0); only the x0 normal
has a nonzero last coordinate. Thus an independent twelve-tuple in S
must contain x0, and its other eleven coordinates form a core basis.
Conversely every core basis, with x0 inserted at any of twelve positions,
is such a tuple. Its weight is unchanged by x0, which is a singleton.

A core basis contains either no A-point or exactly one. With b=|H0-A|,
the two ordered counts are at most(b)_11 and11*a*(b)_10. Their tuple
weights are1 and1+lambda*(a-1), respectively. This proves the upper
bound H in(RATIO). It does not assume every permitted outside tuple is
independent. A weaker upper estimate only strengthens the validity of
the claimed impossibility for a universal lower charge.

On the FULL source, a distinct-fiber twelve-tuple has zero or one A-point.
Its exact counts are(N)_12 and12*a*(N)_11 with the same weights.
This proves U in(RATIO). Any recipe requiring beta as a lower bound
on all eligible record costs must have beta<=actual_cost<=H. Consequently
its resource quotient is at least U/H. The sharp switching supplier also
gives U<=(n)_12 for the allowed lambda, so the coarser resource is no help.

## 5. Monotonicity Reduces Both Intervals To Two Endpoints

For fixed c, N and b are constant. Apart from a positive constant U/H is

    R(X)=(N-11+12X)/(b-10+11X).

Its derivative has the sign of12(b-10)-11(N-11), which is negative
for both c=10 and c=2001. It is therefore decreasing in X. For a>1,
X_lambda increases with lambda, so the smallest ratio in the whole
allowed range is at lambda_*=11/(2(N+a-12)).

Let C=N-12>0. Then

    X_*(a)=a+(11/2)*a(a-1)/(C+a),
    d/da[a(a-1)/(C+a)]=[a^2+(2a-1)C]/(C+a)^2>0.

Thus the ratio also decreases with a, hence with J within each fixed-c
interval. It suffices to evaluate J=13999,c=10 and J=17000,c=2001.
There is no extrapolation from sampled J or field elements.

For exact integer arithmetic write L=2(N+a-12) and
Y=a*L+11*a(a-1). The endpoint ratio is

    (N)_11*((N-11)*L+12Y)
      /[12*(b)_10*((b-10)*L+11Y)].                 (INTEGER)

Euclidean division gives the two floors in the statement. The independent
integer checker reconstructs(INTEGER) and streams all7060 J-values as
a control of the analytic argument. The smaller floor already exceeds B*
by814732750522428, without near or any exceptional-label add-back.

## 6. Provenance And Nonclaims

The unweighted one-large-fiber/raw-one construction is credited to the
method boundary in mca_fiber_contraction_core_basis_resource. The uniform
coefficient and exception interface are the proved switching/secant suppliers.
This refinement uses the exact WEIGHTED source resource, the entire actual
record, source-gate-respecting fiber sizes, and two analytic interval bounds.

The canonical-label and exact two-slope conclusions sharpen that example.
Its complete family has rank one, not twelve. Additional complete-family
rank restrictions can exclude this source; actual tuple ownership can
drastically reduce the resource. Choosing lambda above the printed range
with a separately paid resource is also outside the theorem. No existing
payment is refuted, and no upper row bound or Prize threshold changes.
