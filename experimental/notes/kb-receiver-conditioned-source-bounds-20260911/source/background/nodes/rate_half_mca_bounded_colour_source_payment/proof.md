# Improve LOW By Contracting Its Actual Core Fibres

Put R=1048576,d=67472,J0=9965,J1=21499,D=d-2=67470.
All polynomials, coordinates and finite labels remain over the ORIGINAL
coefficient field. Let U(J)=(R+J)_falling_12 and n_min=R+J0=1058541.

## 1. Freeze The Source And Canonicalize

Maximize raw over all full-code-bad m-supports and all explanations in
the SAME h_*+V, independently for each original label. The original
selection makes these finite sets nonempty. New explanations and raw
values can change; the original error rank is not assumed preserved.

For a fixed basis c_1,...,c_11 of V, the incidence normals
(v(x),-c_1(x),...,-c_11(x)), with right-hand side h_*(x)-u(x),
determine the label and explanation from any independent ordered12-tuple.
Different labels therefore own disjoint independent tuples.

On a full-code-bad support V evaluates with rank11 since m>=J.
The received v is outside that restricted span, since v=b in V there
would make the full-code pair(h-gamma*b,b) contain the support.
The incidence rank is therefore12 in the FROZEN frame, irrespective
of the new global affine rank of the chosen explanations.

At a joint-core point, ev_x=0 would imply v(x)=0 and u(x)=h_*(x),
contrary to empty literal universal carrier core. Joint-core evaluations
are nonzero. These facts are the recordwise hypotheses of the required
original min-envelope resource; they survive reselection without
silently changing its original-rank premise.

## 2. A Receiver-Colour Cap Bounds Actual CORE Fibres

Write the selected pair as(a,b)=(h-gamma*b,b), with
a=h_*+a_V and a_V,b in V. On a nonzero evaluation fibre its joint
core consists exactly of the receiver colour(ell(a_V),ell(b)).
Thus its COMPLETE core occupies at most C points in that evaluation
fibre, even when the entire evaluation fibre is much larger.

For a record of raw r<=2, take any M=m-2=D+J points of its joint core.
Each projective evaluation fibre WITHIN this M-point set has size a<=C.
The exact full-fibre contraction gives

    B_11(H)=sum_(fibres A) a*B_10(H contracted by A).

The annihilator of A has dimension10. Division by its FULL locator
gives a rank10 degree-<(J-a) space on D+J-a points with nonzero
evaluations. This is an auxiliary BASIS count, not a punctured MCA
source. Since C<=286<J0-10, all child degrees are at least10.

Let F_10(k) be the proved nondecreasing rank10 ordered-basis lower
bound constructed in section3. Then

    B_11(H)>=sum a*F_10(J-a)>=M*F_10(J-C).             (CORE)

Insert EACH actual defect in each of12 positions of each core basis.
The defect is the unique coordinate outside this pair's core hyperplane,
so tuples and insertion positions are recoverable. Consequently raw r<=2
owns at least r*beta_C(J) independent original tuples, where

    beta_C(J)=12*(D+J)*F_10(J-C).                     (LOW)

Using the cap of the original evaluation fibre in place of the receiver
colour would discard this improvement. The core only sees one colour.

## 3. Complete Rank10 Branch Tree And Universal Monotonicity

Set P_10(D)=prod_(i=1)^9(D+i). In x=k-r start with the rank3 seed

    q3(x)=D+3+(3D+7)*x/(2*(D+2))+x^2/(2*(D+2)).

For EVERY branch at each rank r=4..10 retain both

    qS(x)=q(x)+1+x,
    qU(x)=(D+r+x)/(D+r-1)*q((r-2)*x/(r-1)).

The required minimum-envelope contraction theorem applies: on the
ENTIRE real child interval x in[0,J1-r+1], every one of127 input
branches satisfies

    q'>=0, q''>=0, 2q'-J1*q''>=0,
    2(r-2)*q'-(D+J1)*q''>=0.

The exact certificate verifies nonnegative Bernstein coefficients for
all four polynomials, with independent reconstruction in unshifted degree.
No branch is pruned. The128 final branches have nonnegative shifted
coefficients and common value D+10 at x=0. Therefore

    F_10(k)=P_10(D)*min_(128 branches) q(k-10)

is a valid nondecreasing basis lower bound for10<=k<=J1.

Every final branch also passes the EXACT strict gate

    q'(J0-286-10)*(R+J0-11)>12*q(J1-2-10).            (MONO)

For all2<=C<=286 and J0<=J<=J1, increasing q,q' imply

    q'(J-C-10)/q(J-C-10)>12/(R+J0-11)>=U'(J)/U(J).

The extra factor D+J in beta_C only strengthens the derivative.
Hence every branch quotient U/[12*(D+J)*P_10*q(J-C-10)] decreases.
Their maximum U/beta_C decreases too, without differentiating a
branch minimum. Define

    W_C=floor(U(J0)/beta_C(J0)).

Then U(J)/beta_C(J)<W_C+1. Also W_C increases with C because
F_10 is nondecreasing. The exact endpoint values needed are

    W_2   =539549513624449050,
    W_43  =541038523546369464,
    W_286 =549960182707973479.

These inequalities cover the full C/J box, not just sampled rows.

## 4. Fund Every HIGH Record On The SAME Universe

The required original resource assigns beta44(J)*min(r,44) tuples
to EVERY original record, including r>500 and r>d, and proves

    U(J)/beta44(J)<W44+1, W44=581590844909990298.

Its recordwise LOW/intermediate/HIGH arguments use the rank and
nonzero-core facts in section1 and so apply in the reselected frame.

Every r>=3 owns at least3*beta44(J) tuples. Set

    beta_eff(J)=min(beta_C(J),3*beta44(J)/2).

Records r<=2 own at least r*beta_eff; records r>=3 own at least
2*beta_eff. These are alternative lower costs for disjoint records
inside ONE original tuple universe, not two budgets to add. Thus

    sum min(r,2)<=floor(U/beta_eff)
       =max(floor(U/beta_C),floor(2*U/(3*beta44)))
       <=W_C.                                      (MASS)

For the last step use

    floor(2*(W44+1)/3)<W_2<=W_C.

Taking a MAXIMUM instead of a minimum in beta_eff would not generally
fund both raw ranges.

## 5. Singleton Defects And The Whole Source

For canonical raw1,2<d, the generic small-colour lemma forces every
nonzero-evaluation defect into a singleton receiver-colour class.
Remove zero-evaluation defect labels once. Scalar agreement fixes the
global label gamma=-(u-h_*)/v there, and the locator bound gives at
most J-11<=21488 labels. A zero evaluation with v=0 is never a defect.

Let N1 be the remaining raw-one count. Its tuples from(LOW) all touch
the singleton bank, so

    N1<=H(n,sigma1)/beta_C(J),
    H(n,b)=n_falling_12-(n-b)_falling_12.

For a declared bound sigma1<=b with0<=b<=n_min-12, the hit fraction
H(n,b)/n_falling_12 decreases with n and increases with b. This follows
factorwise from1-prod_(i=0)^11(1-b/(n-i)). Therefore

    N1<=L_C(b),
    L_C(b)=floor((W_C+1)*H(n_min,b)/U(J0)).            (BANK)

The rational +1 is retained BEFORE multiplying by a universe fraction.
An integer floor of the unrestricted resource is not a valid substitute.

For every remaining positive raw r,

    2=min(r,2)+1_(r=1).

Combining this exact identity with(MASS) and(BANK), and adding the two
global allowances, gives the two-parameter SOURCE bound

    whole source<=floor((W_C+L_C(b))/2)+21488+134944.  (PAY)

The three certificate rows(C,b)=(2,1717),(43,1465),(286,0) yield the
statement's totals and strictly positive reserves. Smaller C or b in
the respective row only improves the estimates. The adjacent singleton
recipes fail, as does the no-singleton recipe at C287; this does not
show that any such source is unsafe.

## 6. Why This Extends The Previous Colour Result

When C<=43, ALL nonzero-evaluation coordinates belong to B43.
There are at most J-11 zero evaluations, so

    sigma43=n-z>=(R+J)-(J-11)=1048587>53067.

Consequently the C43 source class cannot be paid by the previous
small-bank hypothesis. The new proof succeeds by improving LOW's
basis cost and isolating singleton defects, not by reusing that hypothesis.

This does not prove that every source has bounded colours or sparse
singletons. More concentrated classes and singleton-rich receivers remain,
subject to the other independently proved source restrictions.
The [profile resource](profile_resource.md) retains actual class weights
on the UPPER tuple budget and gives a pointwise inequality without the
finite cap restriction. It does not supply exhaustive payment.
No full original degree across all source geometries or Prize is closed.
