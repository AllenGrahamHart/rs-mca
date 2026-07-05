# Amber premise-audit ledger

Date: 2026-07-05.
Worktree: `/home/u2470931/smooth-read-solomin/prize-amber-audit-20260705`.
Branch: `codex-amber-audit-20260705`.

This ledger follows the latest owner clarification: for an amber `A => B`, the
primary object under attack is the truth, scope, and interface of the premise
package `A`.  The implication itself is still flagged if a countermodel appears,
but premise falsification and premise weakening are the main target.

If an amber artifact is not naturally an implication packet, the assertion
itself is treated as the test object: equality/dictionary/counting claims are
attacked directly for falsifiers.

Proof-strategy lens: a finding matters here if it changes which red proposition
is worth proving for the two prize problems.  Stale files are recorded when they
can mis-state a consumer premise or send effort toward a false target; cosmetic
drift is secondary.

Setup read:

- `notes/EMPIRICAL_OBSERVATIONS.md`.
- `notes/CHAIN_COMPRESSION_POLICY.md`.

Replay helpers:

```bash
python3 experiments/amber_audit/inspect_amber_premises.py
timeout 20s python3 tools/verify_prize_dag.py
```

Weakenings applied in this audit clone:

- `adjacency_closing`: demoted direct req edges
  `acl_second_order`, `corridor_window_cleanup`, and `corridor_ext_crossing` to
  evidence, because `corridor_ledger` is the assembled corridor-eater predicate.
- `gap1_noneq_mass`: demoted direct req edges `tr_joint_telescope` and
  `tr_perleaf_list_ident` to evidence, because `gap1_product_model` packages
  that terminal-reserve chain for this parent.
- `ext_lift`: demoted direct req edges `ext_import` and `generating_escape` to
  evidence, because the pole/tower case packets carry those supports.

## 1. `mca_grand` (weight 137)

Implication as consumed:

- A: `s0_zero_open`, `mca_safe`, `mca_unsafe`, `mixed_radix_frontier`,
  `adjacency_closing`.
- B: for each admissible code row, exhibit adjacent integer agreements `a-1,a`
  with `B_C(a-1) > floor(q_line / 2^128) >= B_C(a)`.

Premise attack:

- `mca_safe` and `adjacency_closing` are the only open logical premises in the
  package; the others are green convention/unsafe/frontier inputs.
- The statement is full-family, but the migrated ledger also says the project
  pivot is clean-rate closure first and rate `1/2` as endgame.  This is harmless
  only if the full root continues to require a genuinely full
  `adjacency_closing` premise at rate `1/2`.
- The root implication is therefore only as sound as the child premise scopes:
  a clean-rate-only `mca_safe` or a bracket-grade-only rate-half premise cannot
  be silently consumed here.

Interface check:

- `mca_grand/conditional.md` is ledger prose rather than a crisp proof packet;
  it does not enumerate the exact predicates or the threshold-symbol bridge.
- No direct counterexample to the root implication was found: if `mca_safe`,
  `mca_unsafe`, and `adjacency_closing` are all interpreted in the strong full
  sense, the final root step is essentially threshold bookkeeping.

Verdict: `REPAIRABLE`.

Repair proposed:

- Make the packet explicit: full root consumes full-family `mca_safe` and
  full-family `adjacency_closing`.
- If the intended near-term object is clean-rate closure, split it into a
  separate partial node rather than letting the full root statement inherit
  clean-rate prose.

Replay command:

```bash
python3 experiments/amber_audit/inspect_amber_premises.py | sed -n '/## mca_grand/,/## mca_safe/p'
```

Wall time: `<1s` local.

## 2. `mca_safe` (weight 69)

Implication as consumed:

- A: `counting_frame`, `fm1`, `strip`, `paid_closure`, `ext_lift`,
  `safe_assembly_uniformity`, `r2_clean_rates`.
- B: `B_C(a_safe) <= B*` by the stratified sum
  `tan + quot + ap + ext`, first-match dedup, and R2 on the aperiodic stratum.

Premise attack:

- `r2_clean_rates` is explicitly scoped to clean rates `1/4`, `1/8`, and
  `1/16`; its statement excludes the rate-`1/2` battlefield and says rate
  `1/2` is reserved for separate globalness/composition machinery.
- `mca_safe` is marked `gate: all` and its statement does not restrict the claim
  to clean rates.
- No wired premise in `mca_safe` supplies the rate-`1/2` aperiodic safe-side
  obligation.  The rate-half band appears downstream under `adjacency_closing`,
  not as a safe-side input to `mca_safe`.
- `safe_assembly_uniformity` asserts uniformity over the admissible family, but
  its proof relies on "the budget audit is exact at all six candidate rows",
  while the active R2 premise is only clean-rate scoped.  This is the classic
  producer/consumer scope mismatch: the uniform assembly premise is stronger
  than the wired R2 producer.

Toy/falsification model:

- Interpret `r2_clean_rates` literally as true only for clean rates and make no
  assumption about rate `1/2`.  Then A can hold as written on the clean-rate
  rows while leaving the rate-`1/2` aperiodic term unconstrained; B, if read over
  all admissible rows, does not follow.

Verdict: `REPAIRABLE`.

Repair proposed:

- Split the node into `mca_safe_clean_rates` and a separate rate-`1/2` safe-side
  premise, or add a wired rate-`1/2` R2/safe premise before keeping the
  full-family `mca_safe` statement.
- In either repair, make `safe_assembly_uniformity` consume the same scoped R2
  object that `mca_safe` consumes.

Replay command:

```bash
rg -n "rate 1/2|clean-rate|clean rate|admissible|mca_safe|safe side" \
  nodes/mca_safe nodes/safe_assembly_uniformity nodes/r2_clean_rates \
  nodes/rate_half_band_closure nodes/adjacency_closing -g '*.md'
```

Wall time: `<1s` local.

## 3. `adjacency_closing` (weight 21)

Implication as consumed:

- A after weakening: `crossing_localization`, `staircase_steepness`,
  `aperiodic_zero_at_crossing`, `knife_edge_census`, `corridor_ledger`,
  `rate_half_band_closure`.
- B: for each admissible row, the proved safe agreement `a` and proved unsafe
  agreement `a-1` are adjacent.

Premise attack:

- The premise `rate_half_band_closure` is the dangerous one.  Its statement is
  disjunctive: cover the rate-`1/2` band by a new mechanism, or accept that the
  rate-`1/2` determination is bracket-grade there.
- The consumer `adjacency_closing` needs the strong branch: the band must be
  closed for the full-family adjacency conclusion.  The bracket-grade branch is
  explicitly not enough for adjacency.
- `rate_half_band_closure/conditional.md` still presents the AQB-I averaged
  quotient-box proof, but the current statement/provenance says the AQB route
  was refuted and a genuinely new theorem is needed.  Because the node remains
  `TARGET`, this is not a false green premise, but it is a stale proof packet
  attached to a live premise.
- `aperiodic_zero_at_crossing` is also open and explicitly says the old
  integrality-zero statement was corrected; its premise package must be audited
  before adjacency can be trusted.

Toy/falsification model:

- Let the disjunctive `rate_half_band_closure` premise be satisfied by the
  bracket-grade branch.  Then A, read from the premise statement, can be true
  while B is false for the full-family conclusion.  This is a premise-interface
  countermodel, not a numerical counterexample to the mathematics.

Verdict: `REPAIRABLE`.

Repair proposed:

- Re-pose the rate-half input consumed by `adjacency_closing` as a strong
  `rate_half_band_closed_full` premise, with the bracket-grade alternative moved
  to a separate partial-result node.
- Retire or quarantine the stale AQB conditional packet so it cannot be read as
  an active conditional proof of the full rate-half premise.
- Applied weakening: the direct corridor-eater ingredients were demoted to
  evidence; `corridor_ledger` is now the only corridor-eater predicate consumed
  by this parent.

Replay command:

```bash
sed -n '1,80p' nodes/rate_half_band_closure/statement.md
sed -n '1,80p' nodes/rate_half_band_closure/conditional.md
sed -n '1,90p' nodes/adjacency_closing/conditional.md
```

Wall time: `<1s` local.

## 4. `strip` (weight 32)

Assertion/implication as exposed:

- A: `periodic_strata`, `q_recursion`, `confinement`, `isotypic`,
  `gap1_noneq_mass`, `gap2_seam`.
- B: "Strip-periodic: aperiodic stratum exact."

Premise/assertion attack:

- The premise package is visible in `dag.json`, but the claim is not stated at a
  falsifiable level in either `statement.md` or `conditional.md`.
- `conditional.md` says only "combinatorics PROVED; completeness rests on GAP-1
  pricing."  It does not define the exact aperiodic stratum, the stripped
  object, the endpoint convention, or the contribution being bounded.
- Because the assertion is underspecified, a direct falsification attempt would
  risk testing a proxy rather than the real object.

Verdict: `ILL-POSED`.

Repair proposed:

- Replace the one-line assertion with the exact stripped-count identity/inequality
  consumed by `mca_safe`, and enumerate which part is delivered by each req.
- In particular, identify the exact output of `gap1_noneq_mass` used at the strip
  boundary.

Replay command:

```bash
sed -n '1,80p' nodes/strip/statement.md
sed -n '1,80p' nodes/strip/conditional.md
python3 experiments/amber_audit/inspect_amber_premises.py | sed -n '/## strip/,/## imgfib/p'
```

Wall time: `<1s` local.

## 5. `imgfib` (weight 31)

Implication as consumed:

- A: `petal_growth`, `conj_f`, `l1_program_frontier`,
  `dyadic_profile_evaluation`, `payment_completeness`.
- B: for all received words `U`, `#ImgFib_U(k+sigma) <= n^B` once the printed
  reserve and quotient-profile budget hypotheses hold.

Premise attack:

- The dangerous premise is exactly exposed: `petal_growth` is a `TARGET`, and
  its retraction manifest says the old petal subtree was cut after repeated
  falsifications-as-stated.
- This is good wiring rather than a hidden amber: the consumer is no stronger
  than the live red premise if `petal_growth` is read literally as full-petal
  extras poly(n) uniformly in cofactor excess.
- I found no additional unwired premise in this pass, but the conditional packet
  is ledger-only and should be expanded if this node becomes a proof-facing
  submission artifact.

Verdict: `SOUND`.

Crux attacked:

- The old petal machinery is not silently consumed as green.  The current A
  package names the honest red premise that must be proved/falsified.

Replay command:

```bash
sed -n '1,80p' nodes/imgfib/statement.md
sed -n '1,80p' nodes/petal_growth/statement.md
sed -n '1,80p' nodes/petal_growth/RETRACTION_MANIFEST.md
```

Wall time: `<1s` local.

## 6. `gap1_noneq_mass` (weight 27)

Implication as consumed:

- A after weakening: `gap1_product_model`.
- B: the non-equivariant `K_M`-stable escape mass is `<= poly(n) * FM`.

Premise attack:

- The packet is crisp after weakening: `gap1_product_model` packages the
  product mechanism and the terminal-reserve chain needed by this parent.
- The previous direct edges to `tr_joint_telescope` and
  `tr_perleaf_list_ident` were redundant and have been demoted to evidence.
- No hidden sup/average or paid-citation mismatch appeared at this node itself;
  the real falsification surface is pushed to the two child assertions.

Verdict: `SOUND`.

Crux attacked:

- Cross-character amplification is not being dismissed by prose alone; the
  terminal-reserve chain is wired under `gap1_product_model`.

Replay command:

```bash
sed -n '1,120p' nodes/gap1_noneq_mass/conditional.md
python3 experiments/amber_audit/inspect_amber_premises.py | sed -n '/## gap1_noneq_mass/,/## tr_perleaf_list_ident/p'
```

Wall time: `<1s` local.

## 7. `tr_perleaf_list_ident` (weight 24)

Assertion/implication as consumed:

- A: `tr_joint_telescope`, `x4_exactlist_staircase_split`.
- B/assertion: each per-character TR set `A_r` is the same-rate quotient-row
  exact-list kernel, after lifted joint-stabilizer identity and
  degenerate-tower correction.

Direct assertion attack:

- This is a dictionary/equality assertion rather than a numerical bound.  The
  core map is `f(x)=x^r F(x^M)` and `pi(x)=x^M`; for `K_M`-stable supports,
  support, agreement, and exact disagreement descend and lift orbitwise.
- The likely failure mode is not the algebraic dictionary but whether the actual
  TR objects satisfy the stability/jointness hypotheses.  That is exactly what
  `tr_joint_telescope` is wired to supply, including the degenerate-tower
  correction column.
- No direct dictionary falsifier was found in this pass.

Verdict: `SOUND`.

Crux attacked:

- The equality was tested at the level of support transport: if support is not
  `K_M`-stable, the dictionary could fail, but that case is outside A and is
  assigned to `tr_joint_telescope`.

Replay command:

```bash
sed -n '1,120p' nodes/tr_perleaf_list_ident/conditional.md
```

Wall time: `<1s` local.

## 8. `x4_exactlist_staircase_split` (weight 23)

Implication as consumed:

- A: the wired req package headed by `u1_pullback_dichotomy`,
  `dli_prime_weighted_large_block_support`, `u2c_giant_tnull_dichotomy`,
  `moment_trade_staircase`, and the proved DLI/B2B/trace/syzygy side inputs.
- B: the corrected four-column exact-list split: quotient staircase,
  dihedral staircase analogue, moment-trade staircase, and primitive remainder
  `<= n^2` after the relevant strips.

Premise/packet attack:

- `conditional.md` says its hypotheses "match wiring", but the listed
  hypotheses omit wired reqs `moment_trade_staircase`,
  `xr_syzygy_support_lemma`, and `xr_scattered_syzygy_flattice`.
- The reduction packet also omits those three from the compressed-step
  hypothesis list, despite the statement's four-column amendment explicitly
  relying on the moment column.
- `u1_pullback_dichotomy` is `TARGET` in `dag.json` but its node files still say
  `CONDITIONAL`, even though `RETRACTION_MANIFEST.md` says the former
  conditional subtree was cut after hidden-red failures.
- `dli_prime_weighted_large_block_support` has no `statement.md`; its folder has
  a `proof.md` for an exact reduction and a stale pro brief still asking for the
  now-refuted sup formulation, while the `dag.json` statement correctly says the
  real obligation is weighted average.
- `u2c_giant_tnull_dichotomy` is a wired `TARGET` with no node folder, so the
  surfaced premise cannot currently be audited from local artifacts.

Verdict: `REPAIRABLE`.

Repair proposed:

- Align the packet with the actual wired A package: include all wired reqs, or
  demote cargo edges to evidence.
- Re-sync frontier artifacts: `u1` statement status, a real `statement.md` for
  DLI weighted support, and a node folder for `u2c_giant_tnull_dichotomy`.
- Remove/quarantine stale sup-form DLI prose from the active proof surface.

Replay command:

```bash
python3 experiments/amber_audit/inspect_amber_premises.py | sed -n '/## x4_exactlist_staircase_split/,/## ext_lift/p'
rg -n "moment_trade_staircase|xr_syzygy_support_lemma|xr_scattered_syzygy_flattice|Hypotheses|Reattached" nodes/x4_exactlist_staircase_split -g '*.md'
```

Wall time: `<1s` local.

## 9. `ext_lift` (weight 21)

Implication as consumed:

- A after weakening: `b_rational_lift`, `f1_classification`,
  `f1_case_pole`, `f1_case_tower`.
- B: every extension bad slope above reserve is covered by the B-rational,
  pole, or tower-confined pricing ledgers.

Premise attack:

- The local implication is credible if `f1_classification` is read strongly:
  partition into the three cases, then price each case.
- The artifact layer previously had cargo reqs: `ext_import` and
  `generating_escape` were wired directly but not used as separate local
  predicates.
- Those cargo reqs have now been demoted to evidence; the packet and DAG agree.
- This does not change the red target: the route still wants
  `f1_classification`/pole-list threshold, not a new extension mechanism.

Verdict: `SOUND`.

Weakening applied:

- `ext_import` and `generating_escape` are evidence/support for child case
  packets, not logical predicates of this assembly node.

Replay command:

```bash
python3 experiments/amber_audit/inspect_amber_premises.py | sed -n '/## ext_lift/,/## adjacency_closing/p'
sed -n '1,120p' nodes/ext_lift/conditional.md
```

Wall time: `<1s` local.

## 10. `f1_classification` (weight 16)

Implication/assertion as consumed:

- A: `b_rational_lift`, `f1_case_pole`, `f1_case_tower`,
  `f1_minimal_field_descent`, `f1_full_field_pole_forcing`.
- B: trichotomy of bad slopes into B-pencil-rational, pole-type, or
  intermediate-subfield/tower-confined.

Premise/direct attack:

- The field-theoretic split itself survived direct replay:
  `nodes/f1_minimal_field_descent/verify.py` passed.
- If `f1_full_field_pole_forcing` and `f1_case_pole` are granted, no fourth case
  is visible: minimal field gives B / proper intermediate / full F, and the
  full-F branch is forced into pole unless B-rational.
- Artifact risk is high: the node is `CONDITIONAL` in `dag.json`, but
  `statement.md` still says `CONJECTURE`; several child files also carry stale
  statuses (`f1_full_field_pole_forcing` file says `TARGET` while DAG says
  `PROVED`; `f1_case_tower` file says `TARGET` while DAG says `PROVED`).

Verdict: `REPAIRABLE`.

Repair proposed:

- Sync the F1 node-folder statuses with `dag.json`, or keep the red status if
  those promoted claims are not trusted.  The proof target is still the
  full-field pole forcing/pole threshold package, not a new case split.

Replay command:

```bash
timeout 20s python3 nodes/f1_minimal_field_descent/verify.py
python3 experiments/amber_audit/inspect_amber_premises.py | sed -n '/## f1_classification/,/## r2_clean_rates/p'
```

Wall time: `<1s` local.

## 11. `r2_clean_rates` (weight 9)

Implication as consumed:

- A: `xr_globalness_from_ledger`, `xr_small_set_engine`,
  `xr_radius_arithmetic`, `xr_clean_residual_any_gate`.
- B: at clean-rate decision candidates, every pair satisfies
  `R_post(u,v; A) <= 16 n^3`, sufficient by exact integer budget arithmetic.

Premise attack:

- Scope is honest here: this is explicitly clean rates `1/4,1/8,1/16`.
- The exact arithmetic/reach machinery replayed locally:
  `nodes/xr_radius_arithmetic/verify.py` passed; `nodes/xr_ledger_qpower/verify.py`
  also passed its small-field checks.
- The serious issue is inherited from `xr_clean_residual_any_gate`: the child
  premise is advertised as a `poly(n)` spread bound, but this consumer needs the
  explicit `16 n^3` budget.  A generic `n^4` child theorem would satisfy the
  written word "polynomial" but would not prove this node.

Verdict: `REPAIRABLE`.

Repair proposed:

- Re-pose the child premise with an explicit exponent/constant compatible with
  `16 n^3`, or change this node to consume a separately named
  `xr_smallcore_spread_count_le_16n3` premise.

Replay command:

```bash
timeout 20s python3 nodes/xr_radius_arithmetic/verify.py
timeout 20s python3 nodes/xr_ledger_qpower/verify.py
rg -n "16 n\\^3|poly\\(n\\)|polynomial" nodes/r2_clean_rates nodes/xr_clean_residual_any_gate nodes/xr_smallcore_spread_count -g '*.md'
```

Wall time: `<16s` local total.

## 12. `list_grand` (weight 7)

Implication as consumed:

- A: `s0_zero_open`, `list_safe`, `list_unsafe`, `mixed_radix_frontier`,
  `list_adjacency_closing`.
- B: for each admissible code and constant `m`, exhibit adjacent list radii
  crossing `2^-128 |F|`.

Premise attack:

- As with `mca_grand`, the final implication is bookkeeping if child premises
  are interpreted strongly.
- The child `list_adjacency_closing` inherits the rate-half disjunctive-premise
  issue from `rate_half_band_closure`.
- The top-layer packet correctly keeps the list `m` quantifier visible via the
  closing/safe children; no new quantifier hole was found locally.

Verdict: `REPAIRABLE`.

Repair proposed:

- Same split as the MCA root: keep full list-grand consuming strong full-family
  closing, and create a separate clean-rate partial if that is the current
  near-term deliverable.

Replay command:

```bash
sed -n '1,80p' nodes/list_grand/statement.md
python3 experiments/amber_audit/inspect_amber_premises.py | sed -n '/## list_grand/,/## list_adjacency_closing/p'
```

Wall time: `<1s` local.

## 13. `list_adjacency_closing` (weight 6)

Implication as consumed:

- A: `list_crossing_localization`, `worst_word_planted`,
  `list_planted_arithmetic`, `rate_half_band_closure`,
  `list_corridor_ledger`.
- B: for each admissible row and constant `m`, the worst-word list count crosses
  the epsilon gate at adjacent agreement indices.

Premise attack:

- The clean-rate list corridor is numerically supported: `tools/verify_list_corridor_ledger.py`
  passed with positive margins `0.020286`, `0.023985`, and `0.046660`.
- The same rate-half premise problem appears here: `rate_half_band_closure`
  allows a bracket-grade branch, while this consumer needs full adjacency.
- `statement.md` still says `TARGET` while `dag.json` says `CONDITIONAL`.
- The child `worst_word_planted` correctly exposes the E15 challenger repair,
  so the list side is not silently using the false planted-only premise.

Verdict: `REPAIRABLE`.

Repair proposed:

- Split the strong rate-half closure premise from bracket-grade partials, and
  sync the node status file.  The clean-rate corridor itself looks worth
  trusting as a proof target after the verifier pass.

Replay command:

```bash
timeout 20s python3 tools/verify_list_corridor_ledger.py
sed -n '1,100p' nodes/list_adjacency_closing/conditional.md
```

Wall time: `1.1s` local.

## 14. `list_safe` (weight 4)

Implication as consumed:

- A: `imgfib`, `codegree`, `m_sweep`, `m_handling`.
- B: `#Lambda(C^{==m}, delta) <= 2^-128 |F|` above the list window.

Premise attack:

- The official `m` convention and range are wired, and the conversion through
  `codegree` is explicitly stated.
- The only substantive open premise is `imgfib`, which was already judged a
  sound assembly over the honest red `petal_growth`.
- The refuted `route_one_scale` appears only as a refuted alternative route; it
  is not consumed by the local proof.

Verdict: `SOUND`.

Replay command:

```bash
sed -n '1,120p' nodes/list_safe/conditional.md
```

Wall time: `<1s` local.

## 15. `xr_clean_residual_any_gate` (weight 2)

Implication as consumed:

- A: `xr_target_budget_audit`, `xr_pencil_cascade`,
  `xr_smallcore_spread_count`.
- B: the clean-rate post-strip residual bound `R_post(u,v; A) <= 16 n^3`.

Premise attack:

- This is the clearest premise-strength mismatch in the audit.
- `xr_smallcore_spread_count` is `TARGET` in `dag.json`, but its statement file
  still says `CONDITIONAL` and claims only `<= poly(n)`.
- The consumer conclusion needs the explicit exponent budget `16 n^3`.  A
  hypothetical proof of `Remainder <= n^4` would satisfy the written
  smallcore premise but falsify this implication as used by `r2_clean_rates`.

Verdict: `REPAIRABLE`.

Repair proposed:

- Re-pose the red as an explicit budget-compatible statement, e.g.
  `smallcore_spread <= c n^3` with `c <= 16` after cascade/dihedral accounting,
  or introduce a compiler node that converts a named polynomial exponent into
  the exact budget.

Replay command:

```bash
sed -n '1,80p' nodes/xr_clean_residual_any_gate/conditional.md
sed -n '1,80p' nodes/xr_smallcore_spread_count/statement.md
```

Wall time: `<1s` local.

## 16. `f1_case_pole` (weight 1)

Implication as consumed:

- A: `ext_import`, `f1_pole_list_threshold_location`.
- B: pole-type slopes are priced by the imported list term.

Premise attack:

- The old prose-only second condition has been surfaced as
  `f1_pole_list_threshold_location`, which is the important repair.
- The local `conditional.md` is still ledger-only and does not enumerate the
  predicate nodes, so the assertion is not referee-clean.
- No independent fourth pole-pricing condition was found beyond the list
  threshold child.

Verdict: `REPAIRABLE`.

Repair proposed:

- Replace the ledger-only conditional with the two-predicate proof packet:
  `ext_import` gives the bridge and `f1_pole_list_threshold_location` gives the
  base-list crossing location.

Replay command:

```bash
sed -n '1,80p' nodes/f1_case_pole/statement.md
sed -n '1,100p' nodes/f1_pole_list_threshold_location/conditional.md
```

Wall time: `<1s` local.

## 17. `aperiodic_zero_at_crossing` (weight 0)

Assertion/implication as consumed:

- A: `fm1`, `r2_clean_rates`.
- B: integrality zero begins only at `A*+2`; `A*` and `A*+1` have live
  aperiodic terms and must be decided with the R2 constant.

Premise attack:

- The corrected assertion is strategically important: it prevents the false
  "zero at A*+1" route.
- Scope mismatch remains: the statement discusses all ten table rows and the
  rate-`1/2` thin point, but its R2 input is `r2_clean_rates`, explicitly scoped
  to clean rates.
- Thus the clean-rate conclusion can be trusted only as far as
  `r2_clean_rates` reaches; the rate-`1/2` margin point needs a separate R2 or
  band premise.

Verdict: `REPAIRABLE`.

Repair proposed:

- Split into `aperiodic_zero_clean_rates` and `aperiodic_zero_rate_half_margin`,
  or wire a rate-half R2 premise before using the all-ten-row wording.

Replay command:

```bash
sed -n '1,100p' nodes/aperiodic_zero_at_crossing/statement.md
sed -n '1,80p' nodes/r2_clean_rates/statement.md
```

Wall time: `<1s` local.

## 18. `worst_word_planted` (weight 0)

Implication as consumed:

- A: `imgfib`, `worst_word_challenger_pricing`.
- B: at crossing radii, the worst received words are exhausted by planted
  sunflower words plus the structured E15 challenger class.

Premise/direct attack:

- The false planted-only form is not being used: the E15 counterexample is in
  the statement, and `worst_word_challenger_pricing` is wired.
- Local replay of `nodes/worst_word_challenger_pricing/notes/e22_gate_local.py`
  reproduced the E15 toy challenger at `n=16, sigma=1`: `k=2,4,8` beat planted
  via mixed/full-petal challengers, with `UNCLASSIFIED=0`; sigma-2 controls
  collapsed back to planted.
- This is evidence for the red premise, not proof.  The retraction manifest
  correctly says the full challenger-pricing branch remains an honest TARGET.

Verdict: `SOUND`.

Replay command:

```bash
timeout 20s python3 nodes/worst_word_challenger_pricing/notes/e22_gate_local.py
sed -n '1,80p' nodes/worst_word_planted/statement.md
```

Wall time: `~16s` local.

## 19. `gap1_product_model` (weight 0)

Implication as consumed:

- A: `tr_joint_telescope`, `tr_perleaf_list_ident`.
- B: the tower product model removes cross-character amplification and reduces
  the terminal reserve to the quotient-row per-leaf list supply.

Premise/direct attack:

- The packet is crisp and matches the intended proof strategy: jointness avoids
  the `q^{M-1}` over-aggregation, and the leaf count is delegated to the
  quotient-row exact-list split.
- No new falsifier to the product/dictionary reduction was found.  Any failure
  would be in `tr_perleaf_list_ident`/`x4`, already recorded.

Verdict: `SOUND`.

Replay command:

```bash
sed -n '1,120p' nodes/gap1_product_model/conditional.md
```

Wall time: `<1s` local.

## 20. `f1_pole_list_threshold_location` (weight 0)

Implication as consumed:

- A: `list_adjacency_closing`, `ext_import`.
- B: the base-row list crossing is located below the extension-pole threshold
  needed by the pole ledger.

Premise attack:

- Locally sound: `ext_import` supplies the pole/list bridge, while
  `list_adjacency_closing` supplies the base-list crossing location.
- All strategic risk is inherited from `list_adjacency_closing` and the
  rate-half/list-challenger premises; no separate F-lane red is hiding here.

Verdict: `SOUND`.

Replay command:

```bash
sed -n '1,120p' nodes/f1_pole_list_threshold_location/conditional.md
```

Wall time: `<1s` local.

## 21. `list_planted_arithmetic` (weight 0)

Implication/assertion as consumed:

- A: `worst_word_planted`, `worst_word_challenger_pricing`, `imgfib`.
- B: once extremal classes and image-fiber safety are supplied, list crossing is
  decided by exact integer arithmetic on planted and challenger columns.

Premise/direct attack:

- This is an arithmetic reduction, not the source of the extremality theorem.
- The E15 toy replay supports the need for the challenger column and found no
  unclassified third class in the local gate.
- No MCA-style zone-(b) collision column is being silently imported; the node
  correctly says all live list columns are explicit counts after predicates.

Verdict: `SOUND`.

Replay command:

```bash
sed -n '1,120p' nodes/list_planted_arithmetic/conditional.md
timeout 20s python3 nodes/worst_word_challenger_pricing/notes/e22_gate_local.py
```

Wall time: `~16s` local.

## Morning report table

| node | verdict | one-line reason | replay command |
| --- | --- | --- | --- |
| `mca_grand` | `REPAIRABLE` | root step is bookkeeping if child premises are strong, but full-vs-clean scope must be explicit | `python3 experiments/amber_audit/inspect_amber_premises.py` |
| `mca_safe` | `REPAIRABLE` | full-family safe claim consumes a clean-rate-only R2 premise | `rg -n "rate 1/2|clean-rate|clean rate" nodes/mca_safe nodes/r2_clean_rates nodes/safe_assembly_uniformity -g '*.md'` |
| `strip` | `ILL-POSED` | assertion is too terse to falsify without proxy risk | `sed -n '1,80p' nodes/strip/statement.md` |
| `imgfib` | `SOUND` | suspicious petal premise is honestly wired as red, not hidden amber | `sed -n '1,80p' nodes/petal_growth/RETRACTION_MANIFEST.md` |
| `gap1_noneq_mass` | `SOUND` | weakened to consume only `gap1_product_model`; terminal chain sits under that node | `sed -n '1,120p' nodes/gap1_noneq_mass/conditional.md` |
| `tr_perleaf_list_ident` | `SOUND` | dictionary assertion survives direct stable-support transport check | `sed -n '1,120p' nodes/tr_perleaf_list_ident/conditional.md` |
| `x4_exactlist_staircase_split` | `REPAIRABLE` | reduction packet does not match wired premise package; frontier artifacts stale/missing | `python3 experiments/amber_audit/inspect_amber_premises.py` |
| `ext_lift` | `SOUND` | weakened cargo reqs to evidence; assembly now matches F1 case predicates | `python3 experiments/amber_audit/inspect_amber_premises.py` |
| `adjacency_closing` | `REPAIRABLE` | weakened corridor cargo reqs, but still consumes disjunctive rate-half premise | `sed -n '1,80p' nodes/rate_half_band_closure/statement.md` |
| `f1_classification` | `REPAIRABLE` | case split verifies locally, but status artifacts are stale around promoted F1 children | `timeout 20s python3 nodes/f1_minimal_field_descent/verify.py` |
| `r2_clean_rates` | `REPAIRABLE` | child says generic `poly(n)` but consumer needs explicit `<=16 n^3` | `rg -n "16 n\\^3|poly\\(n\\)" nodes/r2_clean_rates nodes/xr_clean_residual_any_gate nodes/xr_smallcore_spread_count -g '*.md'` |
| `list_grand` | `REPAIRABLE` | final step is bookkeeping, but inherits full-vs-clean/rate-half scope issue | `sed -n '1,80p' nodes/list_grand/statement.md` |
| `list_adjacency_closing` | `REPAIRABLE` | clean-rate list ledger verifies, but rate-half premise is disjunctive | `timeout 20s python3 tools/verify_list_corridor_ledger.py` |
| `list_safe` | `SOUND` | official `m` handling and codegree conversion are wired; open work is honest `imgfib` | `sed -n '1,120p' nodes/list_safe/conditional.md` |
| `xr_clean_residual_any_gate` | `REPAIRABLE` | same exponent mismatch: `poly(n)` child is too weak for `16 n^3` conclusion | `sed -n '1,80p' nodes/xr_clean_residual_any_gate/conditional.md` |
| `f1_case_pole` | `REPAIRABLE` | old prose-only list threshold is wired, but packet remains ledger-only | `sed -n '1,80p' nodes/f1_case_pole/statement.md` |
| `aperiodic_zero_at_crossing` | `REPAIRABLE` | all-ten-row wording consumes clean-rate-only R2 for rate-half margin claims | `sed -n '1,100p' nodes/aperiodic_zero_at_crossing/statement.md` |
| `worst_word_planted` | `SOUND` | false planted-only premise is repaired; E22 toy replay supports two-class route | `timeout 20s python3 nodes/worst_word_challenger_pricing/notes/e22_gate_local.py` |
| `gap1_product_model` | `SOUND` | product-model assertion cleanly delegates terminal reserve to TR/list lane | `sed -n '1,120p' nodes/gap1_product_model/conditional.md` |
| `f1_pole_list_threshold_location` | `SOUND` | local bridge follows from list adjacency plus ext import | `sed -n '1,120p' nodes/f1_pole_list_threshold_location/conditional.md` |
| `list_planted_arithmetic` | `SOUND` | after extremality/pricing predicates, list side is exact integer arithmetic | `sed -n '1,120p' nodes/list_planted_arithmetic/conditional.md` |

FATAL-CANDIDATES: none yet.

REPAIRABLE so far:

- `mca_grand`: split/clarify full root versus clean-rate partial.
- `mca_safe`: split clean-rate safe side from rate-`1/2` safe side, or wire a
  genuine rate-`1/2` safe premise.
- `x4_exactlist_staircase_split`: align packet hypotheses with wired reqs and
  repair stale/missing frontier artifacts.
- `adjacency_closing`: split strong band closure from bracket-grade partial and
  quarantine stale AQB proof prose; corridor cargo reqs already weakened.
- `f1_classification`: sync F1 status artifacts around promoted children.
- `r2_clean_rates` / `xr_clean_residual_any_gate`: re-pose the smallcore spread
  premise with an explicit `<=16 n^3` compatible bound.
- `list_grand` / `list_adjacency_closing`: same strong rate-half closure split
  as the MCA side.
- `f1_case_pole`: replace ledger-only prose with the two-predicate proof packet.
- `aperiodic_zero_at_crossing`: split clean-rate and rate-half margin wording.

ILL-POSED so far:

- `strip`: write the exact stripped assertion before treating it as audited.

SOUND so far:

- `imgfib`.
- `gap1_noneq_mass`.
- `tr_perleaf_list_ident`.
- `ext_lift`.
- `list_safe`.
- `worst_word_planted`.
- `gap1_product_model`.
- `f1_pole_list_threshold_location`.
- `list_planted_arithmetic`.
