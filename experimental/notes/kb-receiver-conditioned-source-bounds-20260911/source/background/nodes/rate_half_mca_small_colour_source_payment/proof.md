# Fixed-Frame Reselection And The Restricted Tuple Resource

Put R=1048576, d=67472, s=11 and W=581590844909990298.
We keep the original normalized receiver, domain, carrier, degree J
and finite post-near labels throughout.

## 1. Reselect Without Reasserting The Original Rank

For each original label gamma, maximize raw over ALL full-code-bad
m-supports and ALL scalar explanations in h_*+V. The original assignment
ensures this finite set is nonempty. Choose a minimizing b in V for
the resulting record.

This can change the explanations, their actual error rank and the
raw values. None is claimed preserved. What is preserved is the fixed
11-dimensional V, the literal empty universal carrier core, receiver,
degree and original labels. The colour partition depends only on that
fixed data and is unchanged. We therefore transfer the RECORDWISE
proof of the required min-envelope theorem, rather than transplanting
a conclusion after changing its rank premise.

For a fixed basis c_1,...,c_11 of V the incidence normal at x is

    nu_x=(v(x),-c_1(x),...,-c_11(x)),

with right-hand side h_*(x)-u(x). Every independent ordered12-tuple
determines gamma and the eleven coefficients of h-h_* uniquely.
Consequently distinct original labels own disjoint independent tuples.

On every chosen m-support the V-evaluations have rank11: m>=J, so
a degree<J polynomial vanishing there is zero. Moreover v restricted
to the support is not in that evaluation span. If it were the evaluation
of b in V, the full-code pair (h-gamma*b,b) would contain the support,
contrary to full-code badness. Thus the normals have rank12 regardless
of the NEW global affine rank of the selected explanations.

The literal universal carrier core consists of coordinates where
ev_x=0, v(x)=0 and u(x)=h_*(x); it is empty. At any point of a joint
core, ev_x=0 would imply b(x)=0=v(x) and a(x)=h_*(x)=u(x),
which is impossible. Hence evaluations on every selected joint core
are nonzero. These are precisely the fixed-frame conditions used in
the basis lower bounds, including the all-HIGH argument.

## 2. Transfer Both LOW And HIGH Costs In That Frame

The required min-envelope proof constructs beta44(J) from all256
branches for bases on m-44 core points. Every selected record of raw
r<=44 has at least m-r joint-core points in its support. Select m-44
of them. The evaluation basis lower bound is beta44(J)/12.
Insert each of the r actual defects in each of12 positions.
These tuples are independent and distinct, since the defect is the
unique coordinate outside this pair's joint-core hyperplane. This
gives r*beta44(J) tuples.

For44<r<=150 the required branchwise transfer gives
44*beta44<=(45)*beta150, and all-defect insertion at cutoff150 gives
at least r*beta150>=44*beta44 tuples. For r>=151 the required
completed-basis bound gives

    11*151*m*prod_(i=1)^10(d+i)
       >=47*beta150>=44*beta44.

Its proof is recordwise in the same normals and fixed carrier. It
includes raw>500 and raw>d; no changed source-rank test is used.
These are alternative lower bounds on a record's tuples, not additive
resources. Thus on the canonically reselected ORIGINAL labels,

    sum min(r,44)<=floor(U(J)/beta44(J))<=W,       (MASS)
    U(J)=(R+J)_falling_12.

The required branch proof establishes U/beta44 decreasing throughout
9941..21499 and floor(U(9941)/beta44(9941))=W. In particular

    U(J)/beta44(J)<W+1.                           (RATIONAL)

The weaker W+1 bound is intentional. Multiplying the integer floor W
by a fraction of the tuple universe would not be justified.

## 3. Canonical Defects Restrict The LOW Tuple Universe

Since2*43<d, the generic canonical-colour supplier shows that a
selected raw r<=43 has exactly r defects on its COMPLETE scalar
agreement set. All nonzero-evaluation defects lie in colour classes
of size<=r, hence in B43.

At a zero evaluation with v(x)!=0, scalar agreement fixes the ONE
finite label gamma=-(u(x)-h_*(x))/v(x). Remove this set of labels once.
If v(x)=0, the coordinate is never a defect. The locator bound on V
gives at most J-11<=21488 such labels globally, NOT per pair.

Every remaining LOW tuple from section2 touches B43. Core entries may
also be in B43; we never require a unique bank entry. The available
ordered tuple count is exactly

    H(n,sigma)=n_falling_12-(n-sigma)_falling_12.

For S=sum_(remaining r<=43) r the generic lemma and(RATIONAL) give

    S<=H(n,sigma43)/beta44(J)
      <(W+1)*H(n,sigma43)/U(J).                    (BANK)

On our allowed sigma range, every factor below is positive. For fixed
sigma, the fraction

    H(n,sigma)/n_falling_12
      =1-prod_(i=0)^11(1-sigma/(n-i))

decreases with n, since each product factor increases. It increases
with sigma. Put n_min=R+9965=1058541. Then

    S<=L(sigma43),
    L(sigma)=floor((W+1)*H(n_min,sigma)/n_min_falling_12).

We may weaken the strict inequality to this floor, even when the
right-hand rational happens to be an integer.

## 4. One Shared Source Budget

Let N_LOW and N_HIGH count the remaining labels of raw<=43 and>=44.
All remaining raw is positive by full-code badness. From(MASS),

    S+44*N_HIGH<=W, N_LOW<=S,
    N_LOW+N_HIGH<=floor((W+43*S)/44)
                  <=floor((W+43*L(sigma43))/44).

This does not independently maximize and add LOW and HIGH budgets.
Add the global zero-label allowance and the ORIGINAL near allowance:

    whole source<=floor((W+43*L(sigma43))/44)+21488+134944. (PAY)

At sigma43=53067 the exact L value is267847831961870445 and(PAY) is
274978354983575055, below B* by2373127820032.
Monotonicity proves the same bound for every smaller sigma43 and all
11535 original degree integers. At53068 the recipe is274982014302343237.
Its failure proves nothing about a source being unsafe.

## 5. Scope Of The New Condition

No arbitrary source is assumed to satisfy the colour-mass hypothesis.
For example V=span{1,X,...,X^10} has distinct projective evaluations
on every distinct domain point, so every receiver-colour class is a
singleton and sigma43=n for any receiver. This observation concerns the
fixed-frame hypothesis, not an excessive original rank12 source.
Other proved source theorems can cover configurations excluded here.

The proof uses no exhaustive original-source computation. The generic
statement has a hand proof; exact finite checks audit the rational
constants, complete recurrence gates and the two original-source
accounting steps. External mathematical review remains due.
