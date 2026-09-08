# Proof: Bind The Normalized Bounds To Every Original Label

## 1. Freeze The Original Selection

Use the near set and complete post-near selection from statement.md.
Its at most 134944 near slopes are added back ONCE at the end. A family
with at most one retained slope is immediate. The required rank-eleven
theorem pays a<=11 by 156765527508803240. Assume a=12.

Same-support badness implies v is not an original codeword. Otherwise
(h_gamma-gamma*v,v) would be a degree-<K polynomial pair explaining
the received pair on every selected scalar support.

Fix gamma_0 and form the actual polynomial/slope space

    E=span{(gamma-gamma_0,h_gamma-h_gamma0)} subset F direct_sum C.

The map (delta,c) -> delta*v-c is injective: if delta is nonzero its
kernel would make v a codeword; if delta=0, injectivity of polynomial
evaluation on n>=K points gives c=0. Its image is the error-difference
space, so dim E=a=12. The first-coordinate projection has rank one.
Choose (1,b) in E and put

    v^g=v-b, h_gamma^g=h_gamma-gamma*b,
    h_*=h_gamma0^g, V=span{h_gamma^g-h_*}.

The differences generate precisely the kernel of the slope projection
of E, so V has ACTUAL dimension eleven, not merely an upper bound.
Errors and complete scalar agreement sets are unchanged by this gauge.
Adding or subtracting b in a pair's second polynomial proves two-way
preservation of full-code pair containment on every support.

## 2. The Complete Shared Core Is Exactly The Universal Carrier Core

We claim

    G={x:V(x)=0, v^g(x)=0, u(x)=h_*(x)}.            (1)

Right-to-left is immediate. If every selected error vanishes at x,
each generator (delta,c) of E satisfies c(x)=delta*v(x), hence so
does every element of E. Applying this to (1,b) gives b(x)=v(x).
Applying it to the zero-slope kernel gives V(x)=0. The gamma_0
equation then gives u(x)=h_*(x). This proves (1).

In particular every V-polynomial vanishes on G. The polynomial common
root-space bound gives g<=K-11 and J=K-g>=11. The larger zero set
{x:V(x)=0} need not equal G. We do NOT remove that larger set: a
nonuniversal zero may agree at one original slope, which must remain.

## 3. All Labels Admit Saturated Full-Bad Supports

Let A_gamma be the COMPLETE scalar agreement set of h_gamma^g.
It contains G and its original full-code-bad witness, so no polynomial
pair can explain it entirely. Apply the required common-core transport
theorem with P=P_G. On D'=D minus G define

    u'=(u-h_*)/P, v'=v^g/P,
    V'=V/P, h'_gamma=(h_gamma^g-h_*)/P.

There is no division by a zero locator value on D'. The dimensions are

    n'=n-g=1048576+J, K'=J, m'=m-g=67472+J,
    dim V'=11, deg V'<J.

For clarity, each A_gamma minus G contains an exact size-m' bad subset.
Otherwise polynomial pairs on all its m'-subsets would agree on adjacent
overlaps of size m'-1>=J. Connectedness under one-point exchanges glues
them to one pair on the complete remainder. Lifting by P and adding
(h_*,b) would explain the original A_gamma, a contradiction.
Adding G to such a child subset gives a saturated original witness.
Thus every original label remains, with no exception charge.

The child's universal carrier core is empty by (1): any point in it
would have belonged to the complete original G and was removed.
Common V'-zeros outside that core may remain. The field, slope values
and cardinality |Z| are unchanged, so the normalized numerator is
exactly |Z|, not a quotient image or independently maximized fiber sum.
At this cancellation stage the original error affine rank is also
preserved: all selected errors vanish on G, so restriction and nonzero
coordinate rescaling are injective on their affine-difference span.

## 4. Canonical Reselection Does Not Reopen Transport

The refined quotient-density/high interval requires no maximal-raw selector. For the
lower-strip theorem, maximize the raw mismatch for each label over all
size-m' full-bad supports and explanations in the SAME fixed V'. This
maximum exists over the finite field and finite domain; the family is
nonempty by section 3. Choose one maximizer and a minimizing second
polynomial. The lower-strip prerequisite uses 2*500<67472, as required.

This operation keeps the original label set and the actual ambient
carrier V' with empty universal core. It need not preserve the previous
raw values, selected explanations, shared complete core or error rank.
Those are not new obligations: a and G were used BEFORE reselection
to obtain the fixed child row, and the normalized lower-strip theorem
is uniform over all permitted canonical selections on that fixed carrier.
Do not shrink V' to a newly selected explanation span or cancel a new
shared core as an uncharged extra normalization.

## 5. Compose Whole-Source Alternatives, Not Owner Charges

The existing common-core forcing theorem already pays rank twelve for
g<=878576 and, in every rank, g>=1043776. Its stated uniform totals
are at most 273540953998915577 and 100000000000134944 respectively.
The completed-child improvement has the smaller total 270992495272115150
on 793577<=g<=878576; all these are below the total in (ORIGINAL).

For the remaining 878577<=g<=1043775, sections 1--4 give the exact
normalized row J=4801..169999 without losing labels. The required
all-carrier interval theorems now pay:

    original g interval     child J interval      |Z|+134944 upper bound
    878577..1027076          21500..169999         274956328426911303
    1038636..1043775         4801..9940            274979661975561635.

The remaining original interval is exactly1027077..1038635, equivalent
to J=9941..21499. Section17 proves the latest interval extension.
Every other rank-twelve case has a whole-family bound.
The finite alternatives refer to the ONE g attached to the fixed original
selection; their worst-case totals combine by MAXIMUM, never addition.
Since |Z_bad|=|Z|+|N|<=|Z|+134944, the largest bound proves (ORIGINAL).

Taking the contrapositive for an arbitrary complete selection proves
the EVERY-selection restriction on any over-budget original line.
Changing a selection may change a and G; no favorable choice is assumed
to exist. The existing all-rank large-core restriction remains valid.

## 6. Additional Actual Receiver-Fiber Classes

In the remaining interval, sections 1--3 already give a fixed actual
dimension-eleven normalized carrier V', the same labels and field,
full-code-bad supports and empty universal core. The required receiver-
fiber payment applies directly, with no canonical reselection or new
common-core cancellation. In the remaining range it pays a fiber of size
>=J-2000 on14000..21499 by248408859318207582, including the one
original near allowance and below (ORIGINAL). Its earlier half-size
fiber payment on 45000..52999 is now subsumed by section 5's unconditional
every-carrier interval. That older supplier remains valid at its full scope.

Use one such fiber if it exists. This bounds the entire original family,
not only the labels agreeing on that fiber: the receiver-class theorem
separately pays the remaining labels on the original incidence resource.
Do not sum these whole-source bounds over multiple fibers. Taking the
contrapositive for every complete original selection proves the additional
carrier restriction in the statement. This additional fiber branch does
not enlarge section 5's degree interval or prove an original error-rank bound.

## 7. Transport The Additional Bounded-Density Class

Use the SAME fixed normalized carrier V' from sections 2 and 3, with its
original slopes, full-code-bad supports and empty universal carrier core.
On 23000<=J<=29999, if its maximum proper-flat density h satisfies
30*h<=J+67466, the required balanced-density supplier gives
|Z|+134944<=268913508505087358. Its bound already contains the single
original near allowance and is below (ORIGINAL). No extra shortening,
zero-coordinate deletion, near event or witness reselection is used.

This is an alternative whole-source sufficient condition, not an added
charge. The supplier's maximizing-flat rank gates and the contrapositive
for EVERY complete original selection give the stated dense-flat
restrictions. Neither the numerical J interval nor the original error-rank
alternatives change. The density condition is not asserted automatic.

## 8. Transport The Actual Dense-Core Mass

If the original line is over budget, |Z_bad|>B*, then sections 1--3 give
|Z|+134944>=|Z_bad|>B* on the SAME normalized dimension-eleven source.
For 23000<=J<=29999 the required dense-core mass theorem applies, with
no flat-density assumption. Fix the minimizing pairs and M-point complete
core subsets after normalization; its conclusion is uniform in those choices.

The counted exceptional labels are original distinct finite slopes, each
counted once. Their flags belong to the actual chosen pair cores and
do not entail a new quotient receiver or uncharged label removal. The
original near allowance is used only in the displayed inequality. No
additional near event, selected-rank preservation or core-size sum enters.

This proves the new necessary mass and rank/degree restrictions for every
complete original rank-twelve selection in that interval. It does not
assert an upper census or enlarge the already paid degree intervals.

## 9. Transport The Stronger Density Gate

Keep the same normalized dimension-eleven carrier from sections 2 and 3.
For 23000<=J<=29999 and h<=(J-3)/8, the new required supplier pays
|Z|+134944<=274977202549132026<(ORIGINAL). No new near event occurs,
and the whole-line alternatives still combine by maximum, not addition.
The supplier's arbitrary core flats and their quotients are used only to
count tuples belonging to the same original labels. They do not replace
the original source, field, denominator or full-code-badness contract.

For any maximizing rank-j flat, the polynomial root-space bound gives
h<=1+(J-11)/j. This is <=(J-3)/8 when j>=8. The contrapositive
therefore excludes EVERY maximizing flat of rank >=8, for EVERY complete
post-near rank-twelve selection of an over-budget original line in this
interval. The narrower degree region and original error-rank alternatives
are unchanged. No upper census of the remaining dense labels is inferred.

## 10. First-Excess Whole-Degree Extension

Use the SAME carrier V' from sections 2 and 3, retaining all original
post-near labels, full-code-bad supports, field and empty universal core.
On 28000<=J<=29999 the new first-excess supplier proves
|Z|+134944<=273019482620216244, with NO source-density hypothesis.
Its whole-source fiber split covers that class first; all other labels
share one original tuple resource through a core-local density split.
Minimal excess flats and maximizing core flats are only basis-counting
devices. They do not discard receiver exceptions or change the source.

This total is below the earlier 30000..169999 union bound
274929007493481160. Taking their maximum gives the predecessor of section 5's first row
on the 28000..169999 range. Section 11 extends it further. There is one original
near allowance in each alternative and none added again by composition.
Since g=K-J, the added interval is g=1018577..1020576. At this preceding stage the
original gap was g=1020577..1038635, or J=9941..27999 (18059 integers).

The earlier density and necessary-mass statements remain valid through
29999, but become redundant on the new paid interval. This is a genuine
whole-source extension, not proof that all original error ranks are <=12
or that the remaining lower degrees are paid.

## 11. Quantitative Whole-Degree And Stronger Fiber Extensions

Use exactly the source from sections 2 and 3. On 26500<=J<=27999,
the quantitative-density interval supplier gives
|Z|+134944<=272896493994028693 without an additional source premise.
Its density conditions split individual actual LOW cores exhaustively;
they are not assumptions on the original carrier. Its polynomial quotients
count tuples only. The SAME original labels, receiver, field, full-code
badness, nonuniversal zeros and empty universal core are retained.

Taking the maximum with section 10's union retains 274929007493481160
on 26500..169999. The added original core interval is
g=1020577..1022076, exactly 1500 integers. At this preceding stage section 5 left
g=1022077..1038635, or J=9941..26499, exactly 16559 integers.
No near allowance is repeated and the overall assembly maximum is unchanged.

The degree-4700 receiver-fiber supplier also applies directly to this
fixed normalized source on 23000..52999 whenever one complete nonzero
fiber has size b>=J-4700. Its whole-source bound, including near, is
246756107210901806, below (ORIGINAL). On the remaining 23000..26499
this is stronger than section 6's gate. Its heavy receiver classes carry
their explicit exceptions; its Johnson children require no second near
event or empty-core premise. Do not add bounds over alternative fibers.
The contrapositive forces EVERY full nonzero fiber <=J-4701 on every
over-budget original selection in that remaining range.

## 12. Rank-Profile Whole-Degree Extension

Apply the new rank-profile interval theorem to the SAME actual carrier
from sections 2 and 3. It gives |Z|+134944<=273123695048315164 on
24000<=J<=26499, with no extra source-density hypothesis. The profile
only changes how polynomial bases of each actual core are counted.
Its degree-box coefficients, quotient and signed inside counts retain
the fixed receiver, original field, all finite labels, full-code-bad
supports, nonuniversal zeros and empty universal carrier core.

The new total is below 274929007493481160, so its maximum with
section 11's union pays every J in24000..169999 by that same number.
Since g=K-J, the added original core interval is1022077..1024576,
exactly2500 integers. The remaining gap is1024577..1038635, or
J=9941..23999,14059 integers. The overall assembly maximum remains
274979661975561635. No original near allowance is repeated.

In the remaining interval the old source-fiber gate is useful on
14000..23999, and the stronger degree-4700 gate on23000..23999.
The older density and necessary-mass assertions remain valid on their
full printed scopes but are redundant on24000..29999.
The contrapositive holds for EVERY original complete selection; there
is no assumption that a favorable selection or small error rank exists.

## 13. Two-Cost Fiber Transport And A Further Whole Interval

Apply the two-cost fiber interval theorem to the SAME normalized carrier
of sections2 and3, with its original labels, field, full-code-bad supports,
nonuniversal zeros and empty universal core. It pays EVERY such source
on23000..23999 by274846585959022192 including the original near allowance.
The source-fiber branch uses the FULL dimension-at-most-ten child cap,
not a new degree-8000 Johnson claim or a child near removal. Its explicit
receiver exceptions are already included. If that branch fails, the
per-core rank-profile alternatives exhaust all remaining labels on one
resource. No source-density assumption is imported by this split.

The new total is below274929007493481160, so its maximum with section12's
union pays every J in23000..169999 by the same number. The new original
core interval is g=1024577..1025576, exactly1000 integers. The remaining
gap is1025577..1038635, equivalently J=9941..22999,13059 integers.
The main whole-line maximum remains274979661975561635; near is not repeated.

The additional degree-6000 source theorem has full scope21000..52999.
On the remaining21000..22999, any complete nonzero source fiber of
size>=J-6000 pays the ENTIRE original line by266180883463176443 including
near. This is below the main maximum. Its contrapositive forces EVERY
such fiber to have size<=J-6001 on any over-budget original rank-twelve
selection in that range. As before, one qualifying fiber suffices and
alternative fiber/source bounds combine by maximum, not addition.
The degree-2000 gate still applies on14000..22999; its weaker restriction
there is implied by the degree-6000 gate on their overlap.

The older degree-4700 and new degree-8000 supplier scopes begin at23000,
so they are now fully subsumed by the every-carrier union. All previous
source-density, maximizing-rank and necessary dense-label mass statements
have scope23000..29999 and are likewise entirely redundant. Their proofs
remain valid, but none gives a constraint on the remaining lower J gap.
Sections10--12 describe their preceding-stage intervals; this section
owned the preceding complement, now superseded by section15.
No favorable original selection or all-source
rank bound is assumed. The original router and unrestricted endpoint stay open.

## 14. Clustered-Arc Transport Inside The Remaining Gap

Use the SAME normalized source constructed in sections2 and3 from the
complete original rank-twelve selection. Its actual dimension-eleven
carrier, original finite labels, full-code-bad supports, field, affine
offset and empty universal carrier core satisfy the new consumer's
base contract. Nonuniversal zero coordinates have not been discarded.

If20481<=J<=22999 and this source has at most560 complete nonzero
projective fibers of size<=2048, with any at most11 distinct classes
independent, the required clustered-arc theorem bounds the ENTIRE source
plus original near by274545534639685994. Its single exceptional slope
set already includes carrier-zero agreements and all charged fiber
secants. Those labels must not be removed a second time as near.

The surviving labels are counted in the unchanged actual carrier;
they need not continue to span it. No rank/core recomputation or favorable
new explanation selection is required. The three geometric gates are
properties of the whole fixed source, not of a selected witness core.

This total is below the existing main whole-line maximum. It is another
alternative sufficient condition for that bound, not an owner charge or
new addend. Consequently every over-budget original rank-twelve selection
in this degree range fails at least one gate. The unrestricted residual
was then J=9941..22999; section15 narrows it further. Higher original
ranks remain open. No older density
condition beginning at23000 is imported below its scope.

## 15. Transport The Collision-Profile Every-Carrier Interval

This section records the preceding500-degree extension, now supplemented
by section16. Its supplier and full original-source scope remain valid.

Sections2 and3 supply the EXACT normalized contract of
rate_half_mca_collision_profile_interval for every fixed complete original
rank-twelve selection: actual carrier dimension eleven, empty universal
core, same field and finite labels, and saturated full-code-bad witnesses.
Its source-fiber and collision tests are exhaustive alternatives, not
extra assumptions on the original line. The selected carrier is retained
after any secant exception labels are removed; the survivors need not
span it. All exceptional labels are explicitly included in its total.

Therefore EVERY selection with22500<=J<=22999 has
|Z|+134944<=274938028871508001. Original near is already included.
UnderJ=1048576-g this is exactly1025577<=g<=1026076,500 complete
integer core sizes. No canonical reselection, second common-core
cancellation or original-rank recomputation is required for this theorem.

The previous23000..169999 bound274929007493481160 is SMALLER than
the new bound. Their union22500..169999 must use their maximum,
274938028871508001. That is still below the main whole-line maximum
274979661975561635 from the lower strip, so (ORIGINAL) is unchanged.
The only remaining original rank-twelve interval is now
g=1026077..1038635, equivalentlyJ=9941..22499,12559 integers.

The residual source-fiber gates apply on14000..22499 and21000..22499.
The clustered-arc supplier retains its full20481..22999 scope, but only
20481..22499 still intersects the unpaid interval. Older source-density
and mass statements starting at23000 remain fully subsumed. Taking
the contrapositive for EVERY complete original selection gives the
updated router restriction. No all-source error-rank bound or claim about
original ranks>=13, the remaining lower gap, LIST or either full Prize follows.

## 16. Transport The Coordinate-Weighted Every-Carrier Interval

This section records the preceding700-degree stage. Section17 gives the
current complement; this supplier's full scope remains unchanged.

The fixed original complete selection and sections2--3 supply exactly the
source of rate_half_mca_weighted_collision_interval: same original field
and finite labels, full-code-bad saturated witnesses, actual dimension11
and empty universal core after cancelling ONLY the complete shared core.
Nonuniversal zero coordinates remain. The new source-fiber alternative,
SOURCE moment cap and common weighting require no further hypothesis on
this carrier or its receiver. All surviving explanations are counted in
the same enclosing carrier; no post-exception rank assumption is imposed.

The weighted theorem thus pays|Z|+134944<=274954262108377832 for
EVERY original rank-twelve selection with21800<=J<=22499. Its explicit
secant/zero exceptions and the one original near allowance are already
included. Therefore|Z_bad| obeys the same total. UnderJ=1048576-g the
new original core interval is1026077..1026776,700 complete integer sizes.
Weights affect auxiliary tuple counting only, not original slope identity,
support badness, receiver, field denominator or selection rank.

The previous high union22500..169999 has smaller cap274938028871508001.
The21800..169999 union must use the new maximum274954262108377832.
That is still below274979661975561635, so the original main bound and
its1066135833452 reserve do not change. The exact remaining rank-twelve
interval is nowg=1026777..1038635, equivalentlyJ=9941..21799,
11859 integers. The necessary fiber gates end at21799; the clustered-arc
supplier's remaining useful overlap is20481..21799. Its historical full
scope is not changed. Old density/mass scopes beginning at23000 remain
fully subsumed and impose no lower-gap restriction.

Taking the contrapositive for EVERY complete original selection gives
the revised router evidence. No theorem on higher original ranks, all
remaining source classes, ordinary LIST or either full Prize is inferred.

## 17. Transport The Sharp Switching Interval

Sections2--3 supply the exact source contract of
rate_half_mca_switching_credit_interval for every fixed original complete
rank-twelve selection. The actual dimension-eleven carrier has empty
universal core after cancelling ONLY the complete shared scalar core.
The original field, finite labels, full-code-bad saturated witnesses and
nonuniversal zero coordinates are retained. Fix minimizing pairs only
after this source is fixed; no new original-rank selection is assumed.

The new supplier pays EVERY carrier21500<=J<=21799 by
|Z|+134944<=274956328426911303. Its source-fiber branch is exhaustive.
The remaining branch uses the same secant/zero exception set and one
nonnegative coefficient for every record. The old core-cost inequalities
hold for every such coefficient; the sharp switching theorem replaces
only their sufficient resource guard. It changes neither the source nor
the label set. Survivors stay in the actual enclosing carrier even when
their own span is smaller. Exceptions and original near are already paid.

Under J=1048576-g this adds1026777<=g<=1027076, exactly300 complete
core sizes. The high union21500..169999 must use the LARGER maximum
274956328426911303. It remains below274979661975561635, so (ORIGINAL)
and its reserve are unchanged. The exact remaining interval is
g=1027077..1038635, equivalentlyJ=9941..21499,11559 integers. Relative
to publicead4b18c, sections16--17 remove1000 whole degrees in total.

The useful2000 and6000 fiber gates now end at21499. The clustered-arc
supplier retains20481..22999, with remaining overlap20481..21499.
No older density/mass scope is extended into the smaller gap. Taking the
contrapositive for EVERY complete original selection gives the current
router evidence. The sharp coefficient is optimal for its partition
resource, not for the actual bad-slope numerator. The remaining degrees,
original ranks>=13, unrestricted MCA, LIST and both Prize problems stay open.

## Scope And Provenance

The gauge and core identification are already proved in the rank-twelve
common-core supplier; saturated-support transport is already proved in
its separate supplier. This node makes their complete source interface
explicit and composes it with the new normalized bounds. The transport
mechanism is not claimed as a new independent discovery.

The required refined quotient-density interval extends the previous
supplier from 32000 down to 30000 with no new source hypothesis. Three
smaller degree blocks have exhaustive exact certificates and an explicit
scope extension. It requires the older quotient-density interval and its
full child and receiver-fiber payments, quotient contraction and density-aware
completion with coupled inside ratios. Quotienting counts bases, not a new
received source. Complete-core
packing retains the original witness and minimizing pair. All proper flat
ranks are covered, and the old large-fiber source class is included in
the finite maximum. Only the paid range in section 5 changes, not the
source bridge or original near add-back.

This is a DIRECT original-source theorem, not a claimed active-v4 atom.
An owner ledger is unnecessary for its direct conclusion; bankability
inside such a ledger would require its separate owner contract. Error
ranks >=13 and rank twelve in the remaining interval outside the new
paid receiver-fiber and bounded-density classes are unpaid.
No unrestricted endpoint, LIST theorem or full prize claim is made.
