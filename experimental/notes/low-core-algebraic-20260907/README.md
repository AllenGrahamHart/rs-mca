# KoalaBear low-core algebraic bounds and a full-kernel strip

```yaml
workboard_item: K3
row: KoalaBear MCA, F of size 2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: every printed normalized source with 4801<=J<=7116 has N_selected+134944<=272837082962714299
architecture: DIRECT
atom_or_cell: normalized rank-twelve source class, not a v4 owner
quantifier: uniform over every received pair, domain and carrier satisfying SOURCE_CONTRACT.md
projection_and_unit: distinct original finite bad slopes, not pairs or supports
claimed_bound: 272837082962714299
status: PROVED
impact: LOCAL_ONLY
falsifier: a source satisfying the exact contract whose selected slope count exceeds 272837082962579355
replay: python3 -B experimental/notes/low-core-algebraic-20260907/replay.py
```

**Review submission, not an accepted row theorem.** This is a grouped
companion to [PR #1175](https://github.com/przchojecki/rs-mca/pull/1175),
not a replacement for Scott Hughes's branch. The proof is local and complete
at its printed scope; independent external hand review remains due. No
active-v4 atom, unrestricted adjacent endpoint, or prize is closed.

## Start with the interval theorem

The [new theorem](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/statement.md)
and [proof](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/proof.md)
cover ALL canonical normalized sources with 4801<=J<=7116. No graph,
pencil, or conic description is assumed. The reserve is 2143645148680788.

The mechanism is short enough to review separately from the finite ledger:

1. The full weighted degree-ten interpolation kernel vanishes on every
   represented LOW pair. A common factor of pair-degree >=3 would leave
   too few polynomial multiples to contain the kernel:
   `D_10-n-D_mult3=960748-135J>0` throughout this strip.
2. The gcd therefore has pair-degree <=2. Two coprime residual equations
   leave at most 100 polynomial pairs off this common curve.
3. Every quadratic factor pattern is paid. The last missing pattern,
   nonparallel constant-direction lines, puts one group on at most half
   the received domain. A direct Johnson argument bounds it by 43 pairs.
4. Partition the original labels, charge the resource and original near
   contribution once, and add at most `100*981604` for exceptional pairs.

At J=7117 the kernel dimension difference is -47. This is only failure of
this sufficient test, not an unsafe construction. Within the prior direct
rank-twelve normalization program, the remaining interval is now
7117..169999, subject to the same upstream normalization hypotheses.
Higher original error ranks remain open.

## Reusable results included

| Result | Source | Exact scope |
|---|---|---|
| Degree-weighted scalar and joint incidence | [algebraic LIST lemma](source/critical/nodes/mca_low_core_quadratic_graph_payment/algebraic_list_bound.md) | Algebraic family of dimension r and degree Delta: at most Delta*((n-K+1)/(A-K+1))^r points with A agreements; includes the degree-cover proof. |
| Rational-X graph dimension bounds | [two-tangent proof](source/critical/nodes/mca_low_core_quadratic_graph_payment/rational_coefficient_graphs.md) | Common s-carrier; quadratic dimension <=ceil(s/2), higher graph degree dimension <=max(1,floor(s/2)); characteristic and denominator guards retained. |
| Moving-direction parabola bound | [equality exclusion](source/critical/nodes/mca_low_core_quadratic_graph_payment/moving_parabolas.md) | Common s-carrier, odd characteristic, nonconstant quadratic direction: dimension <=floor(s/2); count back in the ORIGINAL pair coordinates. |
| Affine-product level dimension bound | [fixed-divisor proof](source/critical/nodes/mca_low_core_homogeneous_level_payment/proof.md) | Fixed nonzero level, at least two nonparallel geometric factor directions: coefficient dimension <=1, with the full degree charge retained. |
| Rational-pencil cover and original gain ledger | [pencil proof](source/background/nodes/mca_low_core_polynomial_relation_payment/rational_line_cores.md) | No old row-height cutoff; constant/nonconstant directions and preferred labels priced separately. |
| Every individual nonsingular conic | [finite conic assembly](source/background/nodes/rate_half_mca_cancelled_low_core_relation_payment/all_conic_payment.md) | On 4801..169999, one conic gives whole original total <=170738199574037868. Arbitrary multi-conic covers are NOT free. |
| Automatic interpolation and parallel fibers | [interpolation proof](source/background/nodes/rate_half_mca_cancelled_low_core_relation_payment/automatic_graph_interpolation.md) | A complete-core union criterion forces a paid graph or up to seven parallel fibers; no assumed nonzero output coefficient. |
| Mixed factors | [affine-product ledger](source/background/nodes/rate_half_mca_cancelled_low_core_relation_payment/homogeneous_level_factor_payment.md), [conic ledger](source/background/nodes/rate_half_mca_cancelled_low_core_relation_payment/all_conic_payment.md) | Printed degree-seven covers with ONE priced exceptional cubic or moving conic; these alternatives cannot be combined without paying both. |

The source files retain their historical node IDs and dated intermediate
nonclaims. The new strip theorem supersedes earlier sentences saying that
all of 4801..169999 remains open; it does not widen their individual bounds.
This package contains no speculative conditional children.

## Dependencies, novelty and integration

Read [SOURCE_CONTRACT.md](SOURCE_CONTRACT.md) before using an integer.
[PROVENANCE.md](PROVENANCE.md) separates reconstructed upstream foundations
from new results, records the live PR/main pins, and supplies a compact
dependency graph. The nonuniform support resource is credited to Hughes's
#1168/#1174 work, not claimed as new here. The elementary padded scalar/joint
LIST proofs, canonical selection, transport, and group ledger are included
so the new curve prices do not depend on unexported numerical MCA caps.

K3 is the primary upstream interface; K4 can use the normalized-source
elimination. No equality with the older 405 conic cases or any first-match
owner is claimed. A bankable active-v4 atom still needs its exhaustive
source-bound owner bridge and inherited charges. A direct uniform proof
would instead have to cover all the remaining source ranks and intervals.

These algebraic LIST tools are NOT an unrestricted ordinary post-Johnson
LIST result. Their output is restricted algebraic-family points; the finite
MCA application additionally uses the explicit slope ownership ledger.

## Replay and review limits

Python standard library only; no downloads, Sage, Modal, CAS or matrix
allocation. Run from the repository root:

```bash
python3 -B experimental/notes/low-core-algebraic-20260907/replay.py
python3 -O -B experimental/notes/low-core-algebraic-20260907/replay.py
```

The wrapper verifies every frozen source hash and runs checks serially, each
with a 15-second timeout. It deliberately starts assert-enabled children
even when the wrapper is optimized: the inherited checks use assertions.
The independent checkers rederive integer transitions, monomial counts and
rounded envelopes; hostile mutations check the printed arithmetic guards.
Finite-field controls test actual source mechanisms and necessary guards.
They do not establish the universal hand proofs. See [AUDIT.md](AUDIT.md).

`SOURCE_MANIFEST.json` binds byte-identical local source files. The origin
worktree was dirty: its HEAD is provenance, NOT the version of these new
proofs. The per-file hashes and this outbound commit pin the actual text.

## Compute requests

None. The contribution is analytic with small exact checks. No large
experiment is needed to review it; no Modal run or expenditure is requested.
