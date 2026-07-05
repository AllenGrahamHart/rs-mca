# Amber stress-test ledger

Date: 2026-07-06.
Worktree: `/home/u2470931/smooth-read-solomin/prize-amber-stress-20260706`.
Branch: `codex-amber-stress-20260706`.
Base: `prize` master `64ae80a`.

Goal: stress-test amber nodes with numerical and algebraic falsification
attempts.  For implication nodes, attack both the premise package and the
implication where feasible.  For direct assertions, attack the assertion.
Every experiment is capped at 60 seconds and must leave checkpoint output.

Initial current-state facts:

- `dag.json` has 29 `CONDITIONAL` nodes.
- `tools/verify_prize_dag.py` still reports pre-existing reachability failures
  in archived/cut branches.
- The same validator flags three amber nodes with no `statement` field:
  `a_regular_collapse`, `free_pool_ladder`, and `m_le3_route`.
- Modal is not installed in this environment (`modal: command not found`).
  The rate-half Modal scripts request `timeout=1800`, so this pass uses a local
  60-second-safe equivalent for the same arithmetic.

## Experiment batch 1: algebraic toy attacks

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 experiments/amber_stress/stress_harness.py --time-limit 55
```

Checkpoint:

```text
experiments/amber_stress/results.json
```

Targets:

- `tr_perleaf_list_ident`: test quotient/lift exact-list dictionary on small
  finite fields, plus a non-stable negative control.
- `x4_exactlist_staircase_split` / `moment_trade_staircase`: recompute the
  primitive moment-null witness from the statement and test that it is not
  quotient/dihedral symmetry.
- `worst_word_planted` / `worst_word_challenger_pricing`: rerun the local E22
  challenger gate and check for unclassified third-class challengers in the toy
  cell.

Result:

- PASS in `6.15s`.
- Checkpoint: `experiments/amber_stress/results.json`.

Findings:

- `tr_perleaf_list_ident`: resisted direct falsification on small fields
  `F_97, n=12, M=3` and `F_193, n=16, M=4`.  The harness checked `886,115`
  lifted polynomial agreement comparisons and found exact quotient/upstairs
  agreement scaling in every case.  Positive controls had nonempty list counts.
- TR negative control: breaking one point in a fiber was detected in all `10`
  non-stable controls.  This is important: the dictionary is not being tested
  vacuously; stability is a load-bearing hypothesis.
- `moment_trade_staircase` / `x4_exactlist_staircase_split`: recomputed the
  statement's primitive witness
  `{11^e : e in {0,1,2,4,16,45,50,60}}` in `mu_64(F_193)`.  Power sums vanish
  for `r=1,2,3`, the `r=4` sum is `18`, the top three subleading locator
  coefficients are zero, and the only rotation stabilizer is identity with no
  reflection stabilizer.  This supports the claim that the moment column is a
  real non-quotient/non-dihedral mechanism.
- `worst_word_planted` / `worst_word_challenger_pricing`: reproduced the E15
  local challenger.  At `n=16, sigma=1`, `k=2,4,8` beat the planted count via
  mixed/full-petal challengers; `UNCLASSIFIED=0` in all gate cells.  Sigma-2
  controls had no challengers.

Verdict impact:

- No falsifier found.
- Confidence increased for `tr_perleaf_list_ident`, `x4`'s moment-column
  inclusion, and the two-class E22 challenger repair.
- The TR stress confirms that any future proof must keep the stable-support
  hypothesis explicit; dropping it is false by the negative control.

## Experiment batch 2: targeted existing verifiers

Script:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Checkpoint:

```text
experiments/amber_stress/verifier_results.json
```

Result:

- PASS in `26.03s` total.
- Every selected command used a `60s` per-command cap; the slowest was
  `xr_ledger_qpower` at about `23.2s`.

Passed checks and covered amber surfaces:

- `list_adjacency_closing` / `list_grand`: list corridor widths and ledger
  arithmetic passed; clean-rate margins remain positive.
- `f1_classification` / `ext_lift`: minimal-field descent verifier passed,
  including concrete finite-field trichotomy partitions.
- `r2_clean_rates` / `xr_clean_residual_any_gate`: XR radius arithmetic,
  q-power ledger, and exponent reconciliation passed.
- `worst_word_planted` / `list_planted_arithmetic`: E22 two-class exhaustion
  sanity check and fixed-scale staircase injectivity passed.
- `strip`: `gap2_seam` verifier passed.
- `imgfib` / `list_safe`: `petal_fixed_excess` verifier passed, including
  top-defect controls.
- `x4_exactlist_staircase_split` / `tr_perleaf_list_ident`: dyadic profile
  evaluation passed.
- `mca_safe`: bounded-scale census verifier passed.
- `adjacency_closing` / `list_adjacency_closing`: local rate-half floor-depth
  and q-threshold arithmetic passed.  At `log2 q=256`, max floor depth is
  `2^33 = 8,589,934,592`, leaving gap `2,978,146` to `sigma*`.  Threshold
  `log2 q ~= 255.89999`, so the open slice is about `0.10001` bits.

Verdict impact:

- No falsifier found in this batch.
- The clean-rate list corridor, F1 trichotomy bookkeeping, XR arithmetic, E22
  two-class repair, strip seam, fixed-excess petal partial, dyadic profile, and
  bounded-scale census all resisted replay.
- Rate-half remains a genuine red premise: the local arithmetic confirms the
  residual top-slice gap instead of closing it.

## Current unresolved amber-stress items

- `a_regular_collapse`, `free_pool_ladder`, and `m_le3_route` are still
  unauditable as ambers because `dag.json` marks them `CONDITIONAL` but does
  not provide a statement field.
- This pass has not yet built fresh falsification harnesses for every one of
  the 29 amber nodes; it establishes a reusable checkpointed framework and
  covers the highest-leverage algebraic/numerical surfaces first.

## Premise weakening batch 1

Target:

- `list_grand`: amber implication from lower list-side predicates to the list
  grand challenge.
- `list_adjacency_closing`: amber implication from list crossing localization
  and priced columns to adjacent list crossing.
- `r2_clean_rates`: clean-rate R2 assembly at the compiled
  `R_post <= 16 n^3` target.

Weakening applied:

- Demoted `list_safe -> list_grand` and `list_unsafe -> list_grand` from
  `req` to `ev` in `dag.json`.
- Rewrote `nodes/list_grand/conditional.md` so the logical predicate set is
  exactly `s0_zero_open`, `mixed_radix_frontier`, and
  `list_adjacency_closing`.
- Demoted `worst_word_planted -> list_adjacency_closing` from `req` to `ev`.
  The transitive logical dependency remains through `list_planted_arithmetic`.
- Demoted `xr_globalness_from_ledger -> r2_clean_rates`,
  `xr_small_set_engine -> r2_clean_rates`, and
  `xr_radius_arithmetic -> r2_clean_rates` from `req` to `ev`.
  The sole logical premise of `r2_clean_rates` is now
  `xr_clean_residual_any_gate`.

Reason:

- The conclusion of `list_adjacency_closing` already contains the adjacent
  crossing inequality
  `sup_U |Lambda(U, delta - 1)| > eps*|F| >= sup_U |Lambda(U, delta)|`.
  Therefore the top-layer grand assembly does not need independent safe/unsafe
  premises.  The former children remain evidence/support edges for the
  lower-level route and for diagnostics.
- The child `list_planted_arithmetic` already consumes `worst_word_planted` and
  packages the exact planted-plus-challenger arithmetic.  A second direct
  `worst_word_planted` premise on `list_adjacency_closing` was redundant.
- The active `r2_clean_rates` statement is the compiled clean-rate residual
  bound `R_post(u,v; A) <= 16 n^3`.  The child
  `xr_clean_residual_any_gate` already includes the budget audit converting the
  safe-side obligation to that exact inequality, so the older KLLM/globalness
  route inputs are no longer direct premises of this assembly node.

Verdict impact:

- This is a genuine weakening of an amber premise package, not a proof of a red
  node.  It reduces the logical dependency surface of `list_grand` and
  `list_adjacency_closing` while preserving the same conclusions.
- For `r2_clean_rates`, this is also a route simplification, not a closure:
  `xr_clean_residual_any_gate` still needs a budget-compatible smallcore bound
  (`<= 16 n^3` scale), so the open critical premise is unchanged.

## Red-premise falsification cleanup: rate-half band

Target:

- `rate_half_band_closure`, consumed by `adjacency_closing`,
  `list_adjacency_closing`, and `mca_safe`.

Finding:

- The node folder was internally inconsistent.  `statement.md` and
  `P6_RATEHALF_SIBLING.md` say the AQB route is refuted and the band is open,
  but `conditional.md` still claimed AQB-I closes the band and `proof.md`
  claimed the P6 dihedral-sibling route gives a concrete covering mechanism.
- The repo already contains the refutation:
  `nodes/dihedral_sibling_window_certificate/proof.md` proves the P6 route
  fails the degree audit.  The proposed packet size is not a Chebyshev
  top-degree drop, true Dickson fibers are too small in the first band, and the
  endpoint fixed-point sibling also overflows.

Edit applied:

- Replaced `nodes/rate_half_band_closure/conditional.md` with the current open
  TARGET status and explicit notes that both AQB-I and P6 dihedral-sibling are
  refuted routes.
- Replaced `nodes/rate_half_band_closure/proof.md` with a proof-status notice
  rather than a stale positive proof.
- Re-posed `rate_half_band_closure` as the strong full-determination premise:
  it means "cover the band by a new priced mechanism."  A bracket-grade
  obstruction remains valuable but is a separate partial result, not a proof of
  this node as consumed by the full adjacency/safe parents.

Verdict impact:

- This does not close or repair the red node.  It prevents downstream amber
  consumers from accidentally reading a known-false route as a conditional
  proof of the rate-half premise, and prevents a bracket-grade partial from
  satisfying a full-determination premise by disjunction.

## Scope repair: aperiodic zero at crossing

Target:

- `aperiodic_zero_at_crossing`, consumed by `adjacency_closing`.

Finding:

- The node's file-level statement discussed all table rows, including the
  rate-`1/2` thin point, but its live R2 premise is `r2_clean_rates`, which is
  explicitly scoped to rates `1/4`, `1/8`, and `1/16`.
- This is a producer/consumer scope mismatch: the clean-rate R2 input cannot
  prove the rate-`1/2` margin statement.

Edit applied:

- Rewrote `nodes/aperiodic_zero_at_crossing/conditional.md` as a clean-rate
  proof packet from `fm1` and `r2_clean_rates`.
- Added the same rate-scope note to `statement.md`.
- Retitled the DAG node to "Clean-rate integrality: R2 + tiny FM pin the
  aperiodic zero threshold".
- Updated `adjacency_closing/conditional.md` so the rate-`1/2` thin point is
  explicitly supplied by `rate_half_band_closure`, not by the clean-rate
  aperiodic node.

Verdict impact:

- This weakens the assertion to the part actually supported by its premises.
  The full adjacency parent still has a route to all admissible rows only if the
  strong rate-half premise is eventually proved.

## Verification rerun after repairs

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 experiments/amber_stress/run_selected_verifiers.py 60
```

Result:

- PASS in about `22.05s` total.
- All selected existing verifiers still pass after the premise weakenings and
  rate-scope repairs.
- The local rate-half arithmetic still reports `max_depth = 2^33` at
  `log2 q = 256`, `sigma* = 8,592,912,738`, and the residual gap
  `2,978,146`.  This supports the strong-rate-half repair: the old floor
  mechanism does not close the band.

## Assertion repair: strip

Target:

- `strip`, consumed by `mca_safe`.

Finding:

- The node files only said "Strip-periodic: aperiodic stratum exact" and did
  not state the object or inequality being consumed.  That made direct
  falsification ill-posed.

Edit applied:

- Rewrote `nodes/strip/statement.md` and `nodes/strip/conditional.md` as the
  exact decomposition implied by the wired premises:
  `rate-preserving quotient columns + O(poly(n) * FM)`.
- The proof now enumerates the roles of `periodic_strata`, `q_recursion`,
  `confinement`, `isotypic`, `gap1_noneq_mass`, and `gap2_seam`.
- Updated the DAG title to
  "Strip-periodic decomposition: quotient columns plus GAP-1 residual".

Verdict impact:

- This does not close a new node; it turns a terse amber into a falsifiable
  implication.  The only live pricing premise remains `gap1_noneq_mass`.

## Orphan amber auditability repair

Targets:

- `a_regular_collapse`
- `free_pool_ladder`
- `m_le3_route`

Finding:

- These three nodes were marked `CONDITIONAL` in `dag.json` but had no
  `statement` field, so the DAG checker reported them as unauditable
  implications.  They are historical/orphan routes with no current root-path
  consumers, but they still need a statement while their status is amber.

Edit applied:

- Added concise DAG statements for all three.
- Marked `a_regular_collapse` as orphan/historical in the notes; it is retained
  for the for-all-`m` boundary but is not active under the official
  per-constant-`m` reading.

Verdict impact:

- No proof status changed and no root path was altered.  This is an
  auditability repair.

## Packet alignment: x4 exact-list staircase split

Target:

- `x4_exactlist_staircase_split`

Finding:

- The DAG wires `moment_trade_staircase`, `xr_syzygy_support_lemma`, and
  `xr_scattered_syzygy_flattice` as required inputs of the x4 split, but
  `conditional.md` omitted them from the displayed hypothesis package.  The
  reduction packet listed `moment_trade_staircase` as a wired hypothesis but
  still omitted the two XR syzygy side inputs.

Edit applied:

- Added all three omitted required inputs to
  `nodes/x4_exactlist_staircase_split/conditional.md`.
- Added the two proved XR syzygy inputs to the packet's reattached side-input
  list.

Verdict impact:

- No status or edge changed.  This keeps the amber implication honest about
  the actual premise package consumed by the DAG.  The XR inputs look like real
  transported-residue dictionary support, not obviously removable cargo, so no
  weakening was applied here.
