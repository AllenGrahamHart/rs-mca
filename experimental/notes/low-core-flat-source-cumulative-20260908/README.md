# KoalaBear MCA: maximum-density bases and original rank-twelve intervals

~~~yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: an original line with a complete post-near selection of error rank <=11, or rank twelve and complete shared core g outside 983577..1038635, has |Z_bad|<=274979661975561635
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
`983577..1038635`. Here the core is the intersection of COMPLETE scalar
agreement sets, not selected size-m witnesses.

Equivalently, every over-budget original line must have, for EVERY such
selection, either:

- error affine rank at least thirteen; or
- error affine rank twelve and `J=1048576-g` in **9941..64999**.

The existing all-rank restriction `g<=1043775` also remains. This is a
necessary restriction on a possible unsafe line, not a claim that any
line in the remaining classes is unsafe or that those classes are empty.

## What Is New In This Extension

### 1. Every Carrier On The High Interval

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

### 2. Exact Transport And Interval Assembly

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
| 878577..983576 | 65000..169999 | 274929007493481160 |
| **983577..1038635** | **9941..64999** | **OPEN** |
| 1038636..1043775 | 4801..9940 | 274979661975561635 |
| at least 1043776 | large-core theorem, all ranks | 100000000000134944 |

These are alternative WHOLE-source bounds for the one original g, not
owner charges to add. The last row also covers g>=k0 without a positive
child degree. The largest paid total is the displayed main bound.

## Review And Reproducibility

- [REVIEW.md](REVIEW.md): the three short proofs and their main risk points.
- [PROVENANCE.md](PROVENANCE.md): immutable inputs, attribution and dependency DAG.
- [VALIDATION.md](VALIDATION.md): bounded serial replay and its limits.
- [SOURCE_CONTRACT.md](SOURCE_CONTRACT.md): inherited, stronger contract for
  the older lower-strip arguments; the new high-interval statement is separate.
- [EARLIER_SOURCE_CLASSES.md](EARLIER_SOURCE_CLASSES.md): prior bounded-flat,
  progression, large-fiber and lower-strip results, with historical scope labels.

The extension retains all 241 previously published source files unchanged
and adds 165 proof/control sources, including earlier source-transport
dependencies. The 36-node requirement inventory is acyclic and locally
PROVED at the used scopes; this is not a claim that the entire Prize DAG
is green. Review the three new arguments first, then their cited suppliers.

Still open: rank twelve on **9941..64999**, higher original error ranks,
the unrestricted adjacent KoalaBear inequality, ordinary LIST and both
Prize problems. The direct theorem needs no v4 owner ledger, but inserting
it into that ledger would require its separate ownership contract.
No new compute request, Modal spending or speculative contraction result
is included.
