# Complete very-low unions through J+400000 are paid

Status: PROVED, 2026-09-07. Use the same normalized KoalaBear row and
fixed affine carrier as the seven-margin companion:

    R=1048576, d=67472, 4801<=J<=169999,
    n=R+J, K=J, m=d+J, dim_F V=11,
    q=2130706433^6, B=274980728111395087.

The universal carrier core is EMPTY. Let U_6 be the union of COMPLETE
pair cores of the chosen minimizing pairs for selected raw<=6 labels.
If

    |U_6|<=J+400000,                                      (U)

then the WHOLE original near-inclusive source count is at most

    274980427687989169 < B,
    reserve=300423405918.                                 (PAY)

No error-rank, relation, subfield-row, or canonical-selection premise is
needed beyond this fixed carrier setup. In particular, the raw<=6 rank
may be twelve and the full row space on U_500 may be zero or cyclic.
All raw>=7 labels remain in the weighted resource; they are not discarded.

An unpaid rank-twelve source, after the stated normalization/selection,
must therefore have

    |U'_6|>=J+400001,
    |U_6,original|>=1448577.                              (RES)

Here the original union is obtained by lifting this selected normalized
family through the previously cancelled common core. Since U_6 is a
subset of U_500 for that same family, both unions have this lower bound.
No arbitrary earlier selection's union is asserted unchanged.

## 1. Ten-dimensional joint LIST cap, with two fixed certificates

The required ordinary-LIST supplier applies to JOINT lists in affine
translates of one common polynomial space, measuring that space's
dimension, not the tuple list's possibly twice-as-large affine dimension.
Use its corridor parameters

    r=400000, w=67466, K_max=169998,
    q>=r+K_max=569998.

Let U_s bound every dimension-at-most-s joint list on every degree
1<=k<=K_max in this corridor. Starting with U_0=1, the supplier gives

    (S) floor((r+s)*U_(s-1)/(w+s)),

and, for a fixed padded degree L with D_L>0,

    D_L=(w+L)^2-(r+L)*(L-1),
    J_L=floor((r+L)*(w+1)/D_L),
    (P) max(J_L,floor((r+L+1)*U_(s-1)/(w+L+1))).

Use (S) at s=1,3; use (P) at s=2 with L=13000 and at every
s=4..10 with L=17000. Only TWO full ordinary Johnson certificates
are needed: J_13000=25 and J_17000=612, with positive denominators.
The resulting all-degree joint-list caps are

    s:  0  1   2    3    4     5      6      7       8        9         10
    U:  1  5  25  148  730  3603  17787  87811  433509  2140169  10565695.

No optimized search, numerical Johnson/Hensel supplier, or unproved MCA
cap is used. Ordinary LIST common-zero removal discards no list word.
The two fixed padding degrees and the whole degree induction are part of
the existing elementary proof, not an assumed monotonicity of row maxima.

## 2. Count the distinct complete polynomial pairs on U_6

If U_6 is empty, there are no raw<=6 labels and the seven-margin
payment applies. Otherwise let P be their distinct minimizing polynomial
pairs f=(a,b), with a in h_*+V and b in V. Every complete H_f has
size at least m-6. Evaluation on V is nonzero at every x in U_6:
some pair matches the receiver there, so a common evaluation zero would
give u(x)=h_*(x), v(x)=0, a forbidden universal carrier core point.

At an anchor x in U_6, retain the pairs agreeing with the receiver
there, and subtract ONE such pair f_0. Both component differences lie
in the SAME space V_x=ker(eval_x|V), of dimension ten. Divide by X-x
and remove the anchor. This is an injective JOINT list on

    (|U_6|-1,J-1,J+d-7),

with common carrier V_x/(X-x), not a scalar list of either projection.
Under (U), extend this LIST domain if necessary to J+400000-1
points, retaining the existing agreements. Points from the original D
already suffice since 400000<R. No source slope, field or code degree
is changed by this auxiliary LIST extension. Its corridor is exactly
the one above, with k=J-1 and agreement k+w.

Thus at most 10565695 distinct pairs agree at each anchor. Counting
pair-core incidences gives

    |P|*(J+67466)<=|U_6|*10565695
                       <=(J+400000)*10565695.

The ratio (J+400000)/(J+67466) decreases with J. Its maximum on
the WHOLE residual interval is at J=4801, so

    |P|<=floor(404801*10565695/72267)
       =59183360 <60000000.                              (PAIR)

Distinct pairs also have distinct complete cores here: a common core
of at least J points determines both component polynomials. The count
does not multiply a scalar list bound by an independently chosen second
component, nor assert that anchoring drops tuple affine rank by only one.

## 3. Convert pairs to labels, including every cross-core point

For one pair f, every assigned selected explanation is a+gamma*b.
Outside its COMPLETE core H_f, a coordinate can be a scalar agreement
for at most one of those finite labels. If it agreed at two distinct
labels, subtraction would give v=b and then u=a, putting it in H_f.
Each assigned label has at least one selected noncore agreement because
its support is full-code-bad. Its labels therefore number at most

    n-|H_f|<=n-(m-6)=981110 <1000000.

This charges ALL noncore coordinates, including those inside another
pair's core. Replacing n-|H_f| by n-|U_6| would be false.
Together with (PAIR), it gives the convenient rounded bound

    L_6<=60000000000000.                                 (LOW)

There is no assertion that this rounded cap or the union cutoff is optimal.

## 4. Add the higher-margin family in the same resource

The seven-margin companion's small-rational relaxation gives

    5999*L_6+41952*H_7<=500*C,
    C=23067643444721720934,

on this exact interval and empty universal carrier core. Hence

    L_6+H_7<=floor((500*C+35953*60000000000000)/41952).

Add only the ORIGINAL near charge 134944, obtaining (PAY). The
strict reserve is exact, not a floating comparison. This proves payment
of the source class, rather than just a necessary union-size condition.

For the original rank-twelve branch, the cancelled core has size
g=1048576-J. Lift the selected pairs as

    (a,b) -> (h_*original+P_G*a,P_G*b).

Their complete cores are EXACTLY G disjoint_union H_f: outside G,
P_G is nonzero, so pair agreement is equivalent in both directions.
Consequently (RES) follows from g+J+400001=1448577. Canonical
selection may be made before applying this theorem; no old support's
margin or old union is carried through a different selection.

## 5. An actual control for the cross-core accounting guard

The canonical selector's existing F_13^6 examples have K=2,m=5,T=1,
three complete pair cores of size four partitioning all twelve coordinates,
and exactly 23 bad labels, each of raw one. Their full E-row spaces
are respectively zero and cyclic. The direct bound here gives

    23 <=3*(12-5+1)=24.

All selected defects lie in other pair cores: an outside-UNION-only count
would incorrectly give zero. The exact field verifier replays those
controls, including all carrier explanations and complete core checks.
They are not deployed-row counterexamples or evidence of optimality there.

## Scope and next action

The new original union floor exceeds the preceding U_500 floor 1262889
by 185688 coordinates. The residual J interval, higher-rank sources and
unrestricted prize brackets remain open. No original red is promoted.

The next count must retain the actual large complete U_6 family and its
cross-core labels. The zero/cyclic classification on U_500 is not silently
reapplied on U_6 or at a different row-degree allowance. Do not improve
this round cutoff by scanning endpoints instead of addressing that source.
