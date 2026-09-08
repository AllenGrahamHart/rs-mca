# KoalaBear MCA: bounded-density payment and necessary dense-core mass

~~~yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: an original line satisfying the rank/core, receiver-fiber or bounded-density gate below has |Z_bad|<=274979661975561635; over-budget rank-twelve lines on J=23000..29999 require the printed dense-core label mass
architecture: DIRECT
atom_or_cell: original received-line classes, not an active-v4 owner
quantifier: every original received line admitting such a complete selection
projection_and_unit: all original distinct finite bad affine slopes, counted once
claimed_bound: 274979661975561635
status: PROVED
impact: LOCAL_ONLY
falsifier: an original line satisfying the printed rank/core gate but exceeding the bound
replay: use the three bounded modes in Review And Reproducibility below
~~~

Agent: Codex acting for AllenGrahamHart, 2026-09-08. Complete local proofs
submitted for independent mathematical review, not external acceptance.
This grouped extension stays on the established companion branch to
[#1175](https://github.com/przchojecki/rs-mca/pull/1175). It does not edit
Hughes's branch, claim his earlier rank/near results as new, or bank a
Grande Finale v4 atom. Neither Prize problem is resolved.

## Main Result: A Restriction On Original Over-Budget Lines

The [original-source theorem](source/critical/nodes/rate_half_mca_rank_twelve_paid_interval_assembly/statement.md)
and its [proof](source/critical/nodes/rate_half_mca_rank_twelve_paid_interval_assembly/proof.md)
give, on the original KoalaBear row, a whole-line bound

~~~text
|Z_bad| <= 274979661975561635 < B*=274980728111395087,
reserve >= 1066135833452,
~~~

whenever ONE complete post-near selection has error affine rank at most
eleven, or rank twelve with complete shared core outside
`1018577..1038635`. Here the core is the intersection of COMPLETE scalar
agreement sets, not selected size-m witnesses.

Equivalently, every over-budget original line must have, for EVERY such
selection, either:

- error affine rank at least thirteen; or
- error affine rank twelve and `J=1048576-g` in **9941..29999**.

For rank twelve, this extension additionally requires every complete
nonzero projective evaluation fiber of the normalized carrier to have
size at most `J-2001` when `J>=14000`. This is a necessary restriction
on an over-budget line, not an automatic fact about every carrier. The
previous half-size gate on 45000..52999 is subsumed by the new interval.

The existing all-rank restriction `g<=1043775` also remains. This is a
necessary restriction on a possible unsafe line, not a claim that any
line in the remaining classes is unsafe or that those classes are empty.

## What Is New In This Extension

Relative to public parent `88f4cf81`, four proved suppliers strengthen the
remaining **23000..29999** region. They pay a source class and constrain
all survivors; they remove no whole degree interval. The overall residual
remains **9941..29999**, with **20059** integer degrees.

### 1. Bounded Proper-Flat Density Pays The Source

The [generic basis theorem](source/critical/nodes/mca_balanced_basis_under_flat_density/proof.md)
proves the full balanced ordered-basis product for a rank-s, degree-<K
polynomial space on N=D+K nonzero evaluation coordinates when every
proper rank-j flat contains at most j*h coordinates and
`floor(s^2/4)*h<=N`. A joint second-moment bound survives every actual
complete-fiber contraction; convexity then closes the product induction.

Its [finite consumer](source/critical/nodes/rate_half_mca_balanced_density_payment/statement.md)
pays every normalized dimension-eleven KoalaBear source with
`30*h<=J+67466`, uniformly on **23000..29999**, by

~~~text
|Gamma|+134944 <= 268913508505087358,
reserve = 6067219606307729.
~~~

Here h is maximum proper-flat COORDINATE density of the whole nonzero
carrier evaluation set, not just the number of projective directions.
The original-source assembly transports this to original slopes with one
near add-back. Every maximizing flat on an over-budget source has rank at
most seven on 23000..24537, eight on 24538..28916, and nine on 28917..29999.

**The unqualified product is false.** The generic proof gives an actual
polynomial large-fiber construction at rank eleven and K=25000 violating
it even when K<D. This is not an unsafe received-line construction; the
density guard must not be dropped from this payment theorem.

### 2. Without A Density Premise, Many Labels Need Dense-Core Flags

The [basis-or-flag theorem](source/critical/nodes/mca_balanced_basis_or_dense_core_flag/proof.md)
follows an actual deficient contraction until its second moment fails.
It yields a nested complete-flat flag inside the SAME fixed core. It does
not assume the preceding density guard; the two alternatives may overlap.

For every fixed minimizing pair after normalization and every chosen
M=J+67466 point core of each LOW record (raw<=6), let e count once each
original label whose chosen core contains a flag of ranks t-1,t, sizes a,b,
with `(11-t)*b-(10-t)*a>M`. Set d=67472, D=67466, R=1048576 and

~~~text
P(J) = product_(i=0)^10 (D+J-i*(J-1)/10),
P_d = product_(i=1)^10 (d+i),
U(J) = (R+J)_falling_12,
beta(J) = min(12*P(J), (d+J)*P_d*10488/125),
G(J) = 134944 + floor(U(J)/beta(J)).
~~~

The [mass theorem](source/critical/nodes/rate_half_mca_dense_core_flag_mass/proof.md)
retains at least one eighth of the good tuple cost for each exceptional
label, on the SAME global resource. Thus

~~~text
|Gamma| <= U(J)/beta(J) + (7/8)*e,
|Gamma|+134944>B* implies e>=floor(8*(B*-G(J))/7)+1.
~~~

**G(J) is a good-record comparison, NOT an unconditional MCA upper bound.**
An original over-budget line has the same necessary consequence through
`|Z_bad|<=|Gamma|+134944`. The strict final +1 is essential.

| J | G(J) | Necessary distinct exceptional labels |
| ---: | ---: | ---: |
| 23000 | 268913508505087358 | 6933965264351691 |
| 25000 | 241182907136195749 | 38626081114513530 |
| 28000 | 205624578023526844 | 79264171528992278 |
| 29999 | 185335366473228672 | 102451841872190189 |

The first mass is also an analytically proved uniform lower bound over
23000..29999, not an inference from four sampled evaluations. Every flag
has **t<=7 throughout this interval**. These are pair-core flags, distinct
from the preceding whole-source maximizing flats. Rank seven yields an
auxiliary dimension-four polynomial annihilator quotient of degree <=5628.
It does NOT give free received-word descent or discarded exceptional labels.

There is **no upper census for e** in this packet. That census, retaining
actual source multiplicities and existing tuple charges, is the concrete
remaining geometric task. Lower J, original ranks >=13, ordinary LIST,
the unrestricted adjacent endpoint and both Prize problems remain open.

## Previous Refined-Interval And Scalar-Ledger Extension Retained

Relative to public parent `b69a8b0b`, there are two separate proved results.

### 1. Every-Carrier Coverage Starts At 30000

The [refined interval theorem](source/critical/nodes/rate_half_mca_quotient_density_refined_interval/statement.md)
and [scope-extension proof](source/critical/nodes/rate_half_mca_quotient_density_refined_interval/proof.md)
pay EVERY normalized carrier on **30000..31999** by
**274471852330442343**, including ONE original near allowance, with reserve
**508875780952744** below B*. Three smaller consecutive degree blocks
retain the parent's proved geometry and shared resource. No additional
source premise or new geometric counting theorem is claimed.

The union **30000..169999** retains **274929007493481160**. Through the
existing original-source bridge, another **2000 integer degrees** are
removed, leaving **20059** in the original rank-twelve interval. The
whole-line assembly maximum is unchanged. Independent exact engines agree
on all 84480 record-cost and 10560 source boxes; analytic full coverage,
not successful sampling, justifies the universal statement.

### 2. A Separate Full-Fiber Scalar-Incidence Theorem

The [scalar ledger](source/background/nodes/mca_empty_core_full_fiber_scalar_census/statement.md)
and [hand proof](source/background/nodes/mca_empty_core_full_fiber_scalar_census/proof.md)
count all original labels satisfying a receiver color's scalar restriction,
not just labels whose minimizing pair belongs to that color. At most
`a-t` original exceptional labels are removed before full-fiber division
gives a same-field, full-code-bad, empty-core child of dimension one lower.
For any proved uniform child cap G, the exact incidence accounting gives

~~~text
m |Gamma| <= sum_A |A| G(K-|A|)
             + sum_A (|A|^2 - sum_(C in A) |C|^2) + z.
~~~

Here A is a complete nonzero projective evaluation fiber, C an actual
normalized receiver color inside it, and z counts carrier-zero coordinates.
These are coordinate-incidence charges; overlapping scalar-label families
are not treated as disjoint whole-source families. A separate two-profile
corollary requires a proved >=1, nonincreasing convex C2 child-cap majorant.
Those shape conditions are not asserted for an arbitrary recursive formula.

**This lemma gives no new finite-row payment and is NOT a dependency of
the interval theorem.** Its nine-node proof inventory is recorded separately
from the 47-node original-source assembly. A preliminary numerical iteration
did not reach the budget and lacked its shape proof; that exploratory script
is not exported or represented as a certified bound or impossibility result.

## Previous Quotient-Density Extension Retained

The [density-aware completion proof](source/critical/nodes/mca_density_aware_flat_completion_resource/proof.md)
keeps maximum flat density in the supplementary outside extensions and
permits any proved quotient-basis lower count. Signed tangent coefficients
are eliminated backwards through actual inside-extension ratios; negative
coefficients use upper ratios, never lower ones.

The [finite quotient-density theorem](source/critical/nodes/rate_half_mca_quotient_density_interval/proof.md)
uses the earlier full-fiber contraction to supply stronger quotient counts.
Exact downward-rounded quadratic certificates hold uniformly over their
entire child-degree intervals. Gap lowering uses a smaller nonzero
evaluation subset, not presumed monotonicity of an empirical optimizer.

Together these two new proved suppliers pay EVERY normalized carrier on
**32000..39999** by **261925431454675420**, including ONE original near
allowance. The reserve below B* is **13055296656719667**. All proper
flat ranks 1..10 and all integer sizes and record occupancies are covered;
the separately paid near-full rank-one fiber class is included in the maximum.
There is no additional structural carrier premise.

With the earlier intervals, the union is **32000..169999**, retaining
**274929007493481160**. Relative to parent `a16bd73b`, this removes
**8000 integer degrees**, leaving **22059** in the original rank-twelve
interval. The whole-line assembly maximum is unchanged. Record bins use
one resource; source alternatives combine by maximum, not sum.

Two independent integer implementations check 112640 record-cost boxes
and 14080 source boxes. Analytic coverage is proved in the linked text;
matching output hashes do not certify that proof. The current assembly
transports the extension with the unchanged field, original slopes,
full-code badness, complete shared core and one near add-back.

## Previous Complete-Core Extension Retained

Two successive, fully discharged interval theorems pay EVERY normalized
dimension-eleven carrier, without an additional structural premise:

| New J interval | Original slopes, including ONE near allowance |
| --- | ---: |
| [45000..52999](source/critical/nodes/rate_half_mca_receiver_flat_interval/statement.md) | 272429083415036159 |
| [40000..44999](source/critical/nodes/rate_half_mca_complete_core_refund_interval/statement.md) | 264060029243645954 |

With the earlier high interval the union is **40000..169999**, at the
unchanged bound **274929007493481160**. Relative to parent `4d665ca9`,
this removes **13000 integer degrees** from the original rank-twelve
residual, leaving **30059**. The whole-line bound above is unchanged.

The [projected receiver-pair proof](source/critical/nodes/mca_receiver_flat_refunded_resource/proof.md)
uses maximum flat density to separate pair restrictions. There is at most
one heavy projected pair. Its child retains actual agreement m-t and
empty universal core; at most a-t exceptional ORIGINAL labels are charged.
The heavy group itself consumes the original tuple resource. Accounting
for that cost reduces the amount of its child bound that must be added.

The [complete-core counting proof](source/critical/nodes/mca_flat_inside_tangent_basis_resource/proof.md)
then uses the FULL pair-core occupancy even when the selected witness
omits some flat points. It changes counted tuples, not the original
witness, raw margin, minimizing pair or slope. The two-cost bound is

~~~text
N <= T_up/beta_L + max(0,1-beta_H/beta_L)*Q_H.
~~~

Rank five has a [signed-coefficient supplement](source/critical/nodes/mca_maximum_density_flat_core_basis_resource/rank_five_extension.md).
Rank six instead uses calibrated convex tangents: couple actual inside
extension counts FIRST, then use upper counts for negative coefficients
and lower counts for positive ones. Positivity is checked before a
lower product bound is multiplied in. The failed rank-six sign-discarding
shortcut is not reused or assumed true.

The [finite complete-core proof](source/critical/nodes/rate_half_mca_complete_core_refund_interval/proof.md)
covers 6400 source-parameter boxes and 2560 rank-six record-occupancy
boxes analytically. Exact rational and independent integer-scaled
certificates check every box. Rank-six occupancies vary per record:
take one uniform minimum charge on ONE resource, never sum box budgets.
The earlier 45000 interval uses 80 exact analytic profiles. These are
universal bounds plus exact certificates, not extrapolation from samples.

The existing original-source bridge transports both results with the same
field, full-code badness and one near add-back. This pays whole source
classes, not active-v4 owners. Independent mathematical review is requested.

## Earlier Receiver-Fiber Classes Retained

The [receiver-fiber theorem](source/critical/nodes/mca_receiver_fiber_peeling/statement.md)
and [finite payment](source/critical/nodes/rate_half_mca_receiver_fiber_payment/statement.md)
pay two additional WHOLE-source classes inside the remaining interval.
For one complete nonzero evaluation fiber of size b:

| Normalized degree J | Fiber gate | Bound on original slopes, including near |
| --- | --- | ---: |
| 14000..52999 | b >= J-2000 | 248408859318207582 |
| 45000..52999 | b >= ceil(J/2) | 272112051300507362 |

The existing [original-source assembly](source/critical/nodes/rate_half_mca_rank_twelve_paid_interval_assembly/proof.md)
transports both results below the unchanged main bound. Either gate
suffices; these are alternative whole-line bounds, not payments to sum
over fibers. The exact normalized source hypotheses remain full-code
badness and empty universal carrier core, with actual dimension eleven.
No maximal-raw selector or child post-near property is required.

The new information is the fixed receiver: normalize BOTH received
values along one fiber. A frozen pair's complete joint core meets it
in one actual value class. There are at most ten classes larger than
b/11, or one larger than b/2. For each such class of size t, charge
at most b-t exceptional ORIGINAL labels before dividing by the COMPLETE
fiber locator. Same-field full child caps pay the remaining labels.
The light records still share one original incidence-tuple resource;
LOW and HIGH combine by maximum. Only disjoint, explicitly counted
heavy classes can be added. The original near allowance occurs once.

This pays the earlier isolated-core method-boundary carrier at J=25000
for every allowed receiver, but not at J=10000. It does not refute that
boundary: the new proof uses collective receiver information absent from
uniform isolated-core pricing. The higher-flat/shared-budget continuation
is now proved and included above.

## Earlier Interval Results Retained

### 1. Fiber Contraction Extends Coverage To 53000

The [contraction theorem](source/critical/nodes/mca_fiber_contraction_core_basis_resource/statement.md)
and [hand proof](source/critical/nodes/mca_fiber_contraction_core_basis_resource/proof.md)
count ordered polynomial-evaluation bases by contracting the COMPLETE
projective fiber in the counted core. Locator division reduces actual
rank and degree together. A quadratic child bound needs only two fiber
profiles; the proof retains the cubic moment rather than bounding it away.

The [finite proof](source/critical/nodes/rate_half_mca_fiber_contraction_interval/proof.md)
uses eight fixed quadratic certificates, with independent exact checks,
to pay EVERY normalized carrier on **53000..65000**:

~~~text
|Gamma|+134944 <= 274171207928811099.
~~~

Together with the earlier maximum-density theorem, this parent stage gave
**53000..169999**, with unchanged union bound **274929007493481160**.
This removes 12000 integer J values from the unpaid interval. No carrier
classification, maximal-raw selection or additional source premise is added.
The original-source bridge and single near add-back are unchanged.

The [method limitation](source/critical/nodes/mca_fiber_contraction_core_basis_resource/method_boundary.md)
constructs actual raw-one records for which a uniform isolated-core charge
with the coarse global tuple budget cannot pay J=10000 or 25000. It is
NOT an unsafe received line or a full original rank-twelve family. Further
progress needs collective source information or a stronger global resource;
this extension does not claim the recurrence alone will close the gap.

### 2. Earlier Every-Carrier High Interval

The [maximum-density theorem](source/critical/nodes/rate_half_mca_maximum_density_high_interval/statement.md)
pays EVERY normalized dimension-eleven source on **65000..169999**:

~~~text
|Gamma|+134944 <= 274929007493481160,
reserve >= 51720617913927.
~~~

There is no extra flat-rank, fiber-size, curve-cover, field-drop or
receiver-descent premise. The exact normalized hypotheses are in the
linked statement; unlike the older curve arguments, it does not require
maximal-raw selection. Universal carrier core zero does NOT mean that
every carrier evaluation is nonzero.

The [generic basis proof](source/critical/nodes/mca_maximum_density_flat_core_basis_resource/proof.md)
combines actual maximum flat density with polynomial common-root bounds.
For a maximizing flat, its annihilator retains the degree excess after
locator division. Independent inside-tuple classes satisfy the exact
identity `sum y_b=E_(b+1)`. This cancels negative tangent terms before
nonnegative terms are discarded, including when the inside core has
rank smaller than the flat.

Low density is paid directly; otherwise root bounds force maximizing
rank 1..4. Log-concavity and derivative bounds reduce ALL cardinalities
and ALL J to 91 indexed rational endpoints. This is not extrapolation
from a grid. LOW raw<=6 and HIGH raw>=7 consume ONE incidence-tuple
resource, so the resulting source bounds combine by maximum, not sum.

### 3. Exact Transport And Interval Assembly

An actual error-rank-twelve gauge gives a dimension-eleven polynomial
carrier. Its universal core is exactly the complete original shared core.
Cancel ONLY that core; retain nonuniversal carrier zeros and their labels.
The saturated-support exchange argument keeps every original finite slope,
full-code badness, the same field and the same denominator.

Canonical reselection for the older lower strip occurs after the child
carrier is fixed. It need not preserve old raw values, selected error
rank or a newly selected common core. The proof does not silently impose
those extra conditions. The original near allowance is added only once.

Together with earlier proved suppliers, the whole-line alternatives are:

| Original rank-twelve core g | Child J, when used | Original slope bound |
| --- | --- | ---: |
| 0..793576 | at least 255000 | 273540953998915577 |
| 793577..878576 | 170000..254999 | 270992495272115150 |
| 878577..1018576 | 30000..169999 | 274929007493481160 |
| **1018577..1038635** | **9941..29999** | **OPEN** |
| 1038636..1043775 | 4801..9940 | 274979661975561635 |
| at least 1043776 | large-core theorem, all ranks | 100000000000134944 |

These are alternative WHOLE-source bounds for the one original g, not
owner charges to add. The last row also covers g>=k0 without a positive
child degree. The largest paid total is the displayed main bound.

## Review And Reproducibility

- [REVIEW.md](REVIEW.md): density, flag mass, source transport and prior proof checks.
- [PROVENANCE.md](PROVENANCE.md): immutable inputs, attribution and dependency DAG.
- [VALIDATION.md](VALIDATION.md): bounded serial replay and its limits.
- [SOURCE_CONTRACT.md](SOURCE_CONTRACT.md): inherited, stronger contract for
  the older lower-strip arguments; the new high-interval statement is separate.
- [EARLIER_SOURCE_CLASSES.md](EARLIER_SOURCE_CLASSES.md): prior bounded-flat,
  progression, large-fiber and lower-strip results, with historical scope labels.

Relative to parent `88f4cf81`, this extension adds 30 proof/control sources
and revises seven assembly sources; 494 parent sources stay byte-identical.
There are 531 hashed sources, a 51-node assembly and a separate nine-node
scalar-lemma requirement inventory, both acyclic and
locally PROVED at the used scopes. This is not a globally green-DAG claim.
The parent commit preserves the previous interval statement and inventory.
Historical supplier summaries retain their dated narrower ranges; the
linked density, flag-mass, scalar-ledger and original-source assembly statements are the
current authority. Source-local descriptions of the continuation as
"local" record its prepublication custody, not a conditional proof status.

Still open: rank twelve on **9941..29999**, higher original error ranks,
the unrestricted adjacent KoalaBear inequality, ordinary LIST and both
Prize problems. The direct theorem needs no v4 owner ledger, but inserting
it into that ledger would require its separate ownership contract.
From this packet directory, these four serial commands cover all 104
distinct checks while keeping each invocation short:

~~~sh
python3 -B replay.py --inherited-only
python3 -B replay.py --quotient-only
python3 -B replay.py --extension-only
python3 -B replay.py --density-only
~~~

For just this update, `python3 -B replay.py --density-only` runs its six
new checkers and the revised assembly in about two seconds. It also supports
`python3 -B -O replay.py --density-only`, propagating -O to all seven children.
The extension mode supports `python3 -B -O replay.py --extension-only`;
optimization is explicitly propagated to all four selected children. For
shorter runs use `--start J0`: quotient mode accepts 32000,34000,36000,38000;
extension mode accepts 30000,30200,30800. All blocks of a chosen interval
are needed for its complete replay. Every invocation validates the entire
source inventory and rejects fourteen manifest mutations, but reports its limited
arithmetic replay scope. The no-flag 104-check run may exceed 60 seconds;
use the split modes under a 60-second process-tree limit.
The earlier `--flat-only`, `--receiver-only` and `--contraction-only`
modes remain available. No flag runs a numerical search.

## Compute Requests

None. Serial standard-library checks suffice; no Modal spending, large-memory
computation or exploratory script is included.
