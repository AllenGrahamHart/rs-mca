# Pointwise Colour-Profile Resource Without A Small-Cap Premise

This is a proved generalization of the source counting inequality, not
a claim that its numerical value always fits the Prize budget.

Keep the same ORIGINAL normalized frame, J9965..21499. Canonicalize
inside it and peel the zero-evaluation labels as in proof.md. Let
w_1,...,w_l be the sizes of ALL nonzero-evaluation receiver-colour
classes and C=max w_i. The polynomial root-space bound gives
C<=J-10, so J-C>=10; the pointwise rank10 tree is valid even if C>286.
Only the finite uniform calibration in the main statement needs C<=286.

## 1. Count Tuples That Could Be Independent

No retained scalar agreement contains a zero evaluation: v!=0 would
force a peeled label, while v=0 would either give no agreement or an
excluded universal core point. All retained tuples therefore use the
nonzero colour classes.

Within one receiver-colour class, the incidence normals are

    lambda_x*(beta,-ell(c_1),...,-ell(c_11)),

where c_1,...,c_11 denotes a FIXED BASIS of V and beta is the
second receiver-colour entry. They are proportional. Hence an
independent ordered12-tuple uses at most one point of each class.

Let e_j(w) be the degree-j elementary symmetric polynomial in those
NONNEGATIVE INTEGER sizes. The number of ordered12-tuples using
distinct classes is exactly

    U_col=12!*e_12(w).

This is an UPPER bound for independent tuples, not a claim that all
distinct-class tuples are independent.

Delete singleton classes from the weight list to obtain w_non1.
The corresponding upper bound for such tuples that also touch a
singleton coordinate is

    V_col=12!*(e_12(w)-e_12(w_non1)).

These counts concern the same global tuple universe. Removing
singleton classes here counts misses; it does not remove source labels
or redefine a code.

## 2. Couple Pointwise LOW And HIGH Costs

Use the exact pointwise functions

    beta_C=12*(67470+J)*F_10(J-C),
    beta44=beta44(J),
    alpha=max(beta_C,beta44),
    eta=min(alpha,3*beta44/2).

The core-contraction proof gives r*beta_C for raw r<=2; the original
all-defect cutoff44 proof also gives r*beta44 there. Their MAXIMUM
is a valid lower count, so r*alpha is funded. For raw1 either chosen
construction consists entirely of tuples hitting the singleton bank.

Every raw>=3 owns at least3*beta44 tuples. Therefore ALL retained
records own at least eta*min(raw,2) tuples, with distinct labels
disjoint. In exact integer arithmetic,

    W_col=floor(U_col/eta),
    L_col=floor(V_col/alpha),
    source<=floor((W_col+min(W_col,L_col))/2)+(J-11)+134944. (PROFILE)

Here N1<=L_col by the singleton tuple universe, and N1<=W_col
because its raw-two resource weight is1. The last equation follows
from2*N=sum min(raw,2)+N1. The global zero-label bound is J-11,
rather than its uniform21488 relaxation.

No whole-J monotonicity in an unknown profile is claimed. All costs
and class sizes in(PROFILE) belong to the SAME actual source at its
actual J. In particular we do not extrapolate the named finite W_C
calibration beyond its C<=286 range.

## 3. Exact Evaluation And Remaining Obligation

The needed e_j for j<=12 can be computed in constant working space.
Start E_0=1,E_1=...=E_12=0. For each class weight w update, in
DESCENDING j,

    E_j <- E_j+w*E_(j-1).

The identity follows by separating products that contain the new class
from those that do not. Descending order prevents using one class
twice. This is an evaluation rule, not a request to enumerate an
original receiver or launch a large computation.

A small independent control counts distinct-class ordered tuples and
singleton hits directly. The proof of proportional normals is what
connects this elementary symmetric count to MCA.

The remaining research problem is to couple realizable colour profiles
with their actual complete-core basis costs strongly enough to make a
source bound universal. This appendix supplies a valid profile-sensitive
inequality but does not establish that coverage or close the target.
