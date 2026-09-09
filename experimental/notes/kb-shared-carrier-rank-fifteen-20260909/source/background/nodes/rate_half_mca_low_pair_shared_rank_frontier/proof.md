# Use The Low-Pair Carrier Without Replacing The Source

Put R=1048576,d=67472,E=21499, near=134944 and
T=274138707278280353. The original V, source rank, complete shared
core and labels remain fixed throughout. All counts below concern P_2
or its complete-core threshold subsets S_t, t=1,2.

## 1. Intrinsic Directions And Legal Auxiliary Enlargements

Differences from any f_0 span the affine direction hull of P_2; changing
f_0 changes neither that hull nor the sum of its two component images.
Thus U and s are intrinsic. Both images lie in V, hence U subset V,
s<=11, and the pair direction hull has dimension r<=2s.

We may extend U to a chosen s_0-dimensional subspace U_0 of V whenever
s<=s_0<=11. If r<=r_0<=2s_0, extend the pair direction hull inside
U_0 x U_0 to dimension r_0. This enlarges only the auxiliary candidate
space f_0+W_0. It changes no original record, received value or source
gauge. Its components are in a_0+U_0 and b_0+U_0, with a shared
direction carrier; they need not be in h_*+U_0 and U_0 themselves.

Every subsequent good anchor lowers these AUXILIARY pair/shared ranks
by2/1. The shared-carrier theorem allows their common zeros, including
the earlier anchors. All counts retain original normalized degree J,
domain D and joint agreement threshold A_t=m-t.

## 2. Shared Dimension Nine Needs No Pencil Assumption

If s<=9 and P_2 is nonempty, choose U_0 of dimension9 and
W_0=U_0 x U_0 of dimension18. Apply the shared-carrier anchor
successively at pair/shared ranks

    (18,9),(16,8),...,(2,1).

At each stage r_0>s_0, so its bad-coordinate count is at most
J-c for c=9,8,...,1. The positive incidence factor is
(R+c)/(d-t+c). After nine good anchors the ambient space has
dimension zero and contains at most one pair. Therefore

    M_t=|S_t|<=product_(c=1)^9 (R+c)/(d-t+c).         (NINE)

The separate floors are52853517316 and52860567481. This argument
does not use dominant-pencil alternatives, height bands, an empty core
for U_0 or a rank-one/rank-two child assumption at equality: its final
space is simply zero-dimensional.

The original all-raw resource and owner proof from the required finite
chain give W3=613022127444579907 and
L_t=sum_(raw<=t)raw<=(R-d+t)*M_t. Hence

    |Gamma|+near
      <=floor(W3/3+sum_(t=1)^2 (R-d+t)*M_t/(t*(t+1)))+near
       =238911770855075395.                         (PAY9)

Empty P_2 is covered by the resource alone. All raw>=3 labels are still
paid. Since (NINE) is unconditional on the original source class s<=9,
(PAY9) is the actual full cap, not a branch that needs a larger maximum.

## 3. Shared Dimension Ten Reaches Pair Dimension Seventeen

Suppose s<=10 and r<=17. The already paid constant/Johnson and
height-band source classes have whole-source cap T, by the required
rank-fifteen chain. In their complement, the hereditary pencil bounds
on every affine subspace are

    C_t=528576/(67473-t) for constant directions,
    P_t=781095/(85474-t) in general.

They concern COMPLETE P_2 core unions on the original source, so they
remain valid in any smaller auxiliary carrier. There is no claim that
this carrier has the original V's empty universal core.

If P_2 is nonempty, choose s_0=10,r_0=17 in section1. Seven guarded
anchors at ranks17/10,15/9,13/8,11/7,9/6,7/5,5/4 cost

    product_(c=1)^7 (R+c)/(d-t+c).

The terminal child has pair/shared ranks3/3. A rank-one child must
be constant and has cap C_t^3. A rank-two child has cap H_t*P_t,
where H_t=1027079/(45975-t) is the worst-J determinant quotient.
The exact inequalities H_t<=P_t^2 and H_t*P_t<=C_t^3 pay both
types by C_t^3. Consequently

    M_t<=C_t^3*product_(c=1)^7 (R+c)/(d-t+c),         (TEN)
    pair floors105235509453 and105251107155.

The same all-raw ledger gives branch273174666855895812. Its maximum
with the already paid source classes is T. This proves the s<=10,r<=17
claim. All lower actual ranks are covered by auxiliary enlargement, not
by asserting they have rank17 or remeasuring the original error rank.

## 4. State The Remaining Alternatives Precisely

The required rank-fifteen theorem also pays r<=15 without lowering s.
Thus an over-budget source has s>=10. If s=10, it must have r>=18,
and r<=2s=20. If s=11, it must have r>=16, with r<=22. These
disjoint alternatives exhaust the possible intrinsic ranks, proving
(SURVIVOR) under every valid assignment.

The possible pair-space codimensions2s-r are therefore0..2 in the
s=10 branch and0..6 in the s=11 branch. This is a proved restriction,
not a payment of those spaces or an assertion that their pair sets are
dense in their affine hulls. Original error ranks>=13 and both full
Prize problems remain open.
