# KoalaBear MCA: receiver-fiber classes and original rank-twelve bounds

~~~yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: an original line satisfying the rank/core gate or either rank-twelve receiver-fiber gate below has |Z_bad|<=274979661975561635
architecture: DIRECT
atom_or_cell: original received-line classes, not an active-v4 owner
quantifier: every original received line admitting such a complete selection
projection_and_unit: all original distinct finite bad affine slopes, counted once
claimed_bound: 274979661975561635
status: PROVED
impact: LOCAL_ONLY
falsifier: an original line satisfying the printed rank/core gate but exceeding the bound
replay: python3 -B experimental/notes/low-core-flat-source-cumulative-20260908/replay.py
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
`995577..1038635`. Here the core is the intersection of COMPLETE scalar
agreement sets, not selected size-m witnesses.

Equivalently, every over-budget original line must have, for EVERY such
selection, either:

- error affine rank at least thirteen; or
- error affine rank twelve and `J=1048576-g` in **9941..52999**.

For rank twelve, this extension additionally requires every complete
nonzero projective evaluation fiber of the normalized carrier to have
size at most `J-2001` when `J>=14000`, and at most `ceil(J/2)-1` when
`J>=45000`. These are necessary restrictions on an over-budget line,
not automatic facts about every carrier. The numerical J interval stays
unchanged: no new whole interval or rank closure is claimed.

The existing all-rank restriction `g<=1043775` also remains. This is a
necessary restriction on a possible unsafe line, not a claim that any
line in the remaining classes is unsafe or that those classes are empty.

## What Is New In This Extension

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
uniform isolated-core pricing. The unfinished higher-flat/shared-budget
extension is deliberately excluded from this snapshot.

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

Together with the earlier maximum-density theorem, coverage is now
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
| 878577..995576 | 53000..169999 | 274929007493481160 |
| **995577..1038635** | **9941..52999** | **OPEN** |
| 1038636..1043775 | 4801..9940 | 274979661975561635 |
| at least 1043776 | large-core theorem, all ranks | 100000000000134944 |

These are alternative WHOLE-source bounds for the one original g, not
owner charges to add. The last row also covers g>=k0 without a positive
child degree. The largest paid total is the displayed main bound.

## Review And Reproducibility

- [REVIEW.md](REVIEW.md): the new contraction argument and prior source bridge.
- [PROVENANCE.md](PROVENANCE.md): immutable inputs, attribution and dependency DAG.
- [VALIDATION.md](VALIDATION.md): bounded serial replay and its limits.
- [SOURCE_CONTRACT.md](SOURCE_CONTRACT.md): inherited, stronger contract for
  the older lower-strip arguments; the new high-interval statement is separate.
- [EARLIER_SOURCE_CLASSES.md](EARLIER_SOURCE_CLASSES.md): prior bounded-flat,
  progression, large-fiber and lower-strip results, with historical scope labels.

Relative to parent `47d527e5`, this extension adds 15 proof/control sources
and revises seven assembly files; 417 parent sources stay byte-identical.
There are 439 hashed sources and a 40-node acyclic requirement inventory,
locally PROVED at the used scopes. This is not a globally green-DAG claim.
The parent commit preserves the previous interval statement and inventory.
Historical supplier summaries retain their dated narrower ranges; the
linked receiver-fiber and original-source assembly statements are the
current authority. Source-local descriptions of the continuation as
"local" record its prepublication custody, not a conditional proof status.

Still open: rank twelve on **9941..52999**, higher original error ranks,
the unrestricted adjacent KoalaBear inequality, ordinary LIST and both
Prize problems. The direct theorem needs no v4 owner ledger, but inserting
it into that ledger would require its separate ownership contract.
No new compute request, Modal spending or unfinished receiver-flat
extension is included. To replay just the four new checks, use
`python3 -B replay.py --receiver-only` from this packet directory;
adding `-O` also optimizes those four explicitly guarded children.
The earlier `--contraction-only` mode remains available.
