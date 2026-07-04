# Clean-rate MCA campaign — the falsification ledger

- **Status:** DRAFT / living. Sibling of `campaign_report_00_overview`
  (overview) and `campaign_report_01_terminal` (the terminal problem).
- **Audience:** the maintainer (przchojecki) and the community, as a record
  of method. Companion to `critical_path_status_2026_07_04.md`.
- **Scope:** the twelve statements this campaign **believed, then
  falsified, then repaired** into the current structure.

## Why this file exists

The campaign runs a **falsify-before-prove** discipline: every conjecture
is pre-registered with a wired falsifier, and the DAG validator forbids a
refuted node from being a requirement of anything. The result is a program
that overturns its own claims routinely and on the record. This is not an
errata sheet — the falsifications are the load-bearing work. Each one
deleted a false shortcut and, more usefully, told us the *true* shape of
the object underneath. Three of the twelve below are self-inflicted
corrections caught in the final week (entries 7, 10, 12); the rest are the
scaffolding of the whole reduction. The DAG carries ~10 REFUTED-and-repaired
nodes at any snapshot (`campaign_report_00_overview.md`); this ledger reads
them, plus the roadmap-note corrections, as one narrative.

Format per entry: **Believed** | **Falsifier** (with file refs) | **Repair
— and what structure it became**.

## The ledger

### 1. The no-slack MCA conjecture (the program's origin)

- **Believed.** The clean determination holds with *no slack*: the safe/
  unsafe boundary is exactly the MCA prediction, provable by a direct
  entropy-gap / single-scale argument.
- **Falsifier.** The original no-slack conjecture is **refuted** outright
  (`tex/RS_disproof_v3.tex`; DAG node `route_noslack`, REFUTED). The naive
  one-scale ambient-`q` entropy-gap prediction also fails
  (`route_one_scale`, REFUTED; `proof_sketch/s7_list_side.md#1`).
- **Repair.** The determination was recast as a **procedure/Reading-B
  obligation** compiled to one counting column `R_PTE <= n^3` per row
  (`campaign_report_00_overview.md`; the poly-forcing compiler). The whole
  subsequent chain exists because the direct route was killed here first.

### 2. X-4: the "monolithic list" staircase counterexample

- **Believed.** The list target is a single monolithic agreement bound.
- **Falsifier.** X-4 exhibited a verified **staircase counterexample**: the
  extremal list configuration splits, so the monolithic target is
  unattainable (git `eb529b80`, "X-4 verdict banked (verified): the
  staircase counterexample — list target corrected to the split form").
- **Repair.** The target became the **split-pair / active-core form** —
  agreement pairs at agreement `A`, differing by a constant on the top `t`
  (`sp_census_split_pair_census.md`; `campaign_report_00_overview.md`
  item 3). This split framing is what makes the star-PTE reduction and the
  `R_PTE` column possible at all.

### 3. X-4b: the four-mechanism taxonomy was complete

- **Believed.** The charged (symmetry-paid) classes are exactly four:
  multiplicative, dihedral, affine, moment-block — a closed dictionary.
- **Falsifier.** X-4b found a **fifth mechanism**, verified: primitive
  moment-trade staircases — chargeable families the four-column split
  omitted (git `f7926c15`, "THE FIFTH MECHANISM (X-4b verdict, witness
  verified)"; `f2_moment_trade_census.md`).
- **Repair.** The dictionary gained an explicit **MomentTradeStaircase
  column** with exact counting rules, and the grammar was **frozen as v1**
  to make "charged" decidable and countable
  (`w3_chargeable_dictionary_grammar.md`; `xr_budget_audit.md`). The
  taxonomy is now symmetry-complete against the frozen grammar.

### 4. U2: primitive moment trades are universally excluded (the 234-bit witness)

- **Believed.** At official rows no primitive `t`-moment-null block exists —
  a *universal* large-prime theorem (first-moment count `~ n^b p^{-t}`
  dwarfed by hundreds of bits), closable by Weil/character sums.
- **Falsifier.** X-6 produced a **verified witness**: a 234-bit prime,
  sparse relation `1 + a + a^2 + a^4 = 0` with `ord(a) = 1024`, giving a
  3-moment-null non-quotient non-dihedral block `{+-1, +-b, +-b^2, +-b^4}`
  in `mu_2048` over `F_{p^2}` (git `bfbd4f60`, "U2 refuted as universal";
  `f2_moment_trade_census.md`). Universal exclusion is **false**.
- **Repair.** Two structural gains. (a) The witness is *inadmissible*
  (`q = 2^468 > 2^256` field cap) — a scope, not a threat. (b) The
  mechanism is **resultant-divisibility**: sparse-relation blocks exist
  exactly at the finitely many primes dividing `Res(relation, Phi_n)`. The
  lane became **certification** (`u2_per_row_moment_certifier` — divisibility
  checks per row), and the companion **char-0 lifting theorem** was proved
  (`u2_large_characteristic_lift`, PROVED). The "exceptional primes" the
  `q`-sweep kept seeing are exactly these resultant factors — the seed of
  the good-reduction lemma A3.

### 5. U2-C: giant `t`-null blocks are coset unions with `M > t` only

- **Believed.** Every giant `t`-null block is a disjoint union of full
  2-power cosets `mu_M` with `M > t` (the dictionary's `M > t` fence);
  the giant regime is fully charged by the quotient staircase.
- **Falsifier.** X-8 built a verified **boundary-scale counterexample**
  (with a Pocklington primality certificate): at the first boundary scale
  `M = t` there are primitive **zero-sum quotient** blocks — coset unions
  the `M > t` fence excludes (git `1e0dd858`, "U2-C refuted at the
  dictionary's boundary scale"; `qa25_boundary_scale_column.md`;
  `u2c_giant_block_statement.md`). The node `u2c_giant_block_dichotomy` is
  REFUTED.
- **Repair.** A new **boundary-scale (`M = t`) zero-sum column**, exactly
  characterisable and exactly countable (subset-sum collision counts),
  joins the charged classes (`u2c_boundary_scale_column`; the U2-C-prime
  residual dichotomy). Verified nearly-immune at the six campaign
  candidates (`~2^6` blocks at worst); the QA.25 crossover arithmetic
  locates the danger row exactly.

### 6. The `K^2` fiber-count (quadratic) estimate

- **Believed.** The abundance/fiber count in the deep-link staircase grows
  quadratically, `~ K^2 t^2 / 2` incidences (`u1_proof_skeleton_ritt_route.md`
  step 3(i)'s fiber-product heuristic).
- **Falsifier.** The E33 deep-link staircase census measured the growth as
  **linear**, not quadratic (git `dd627ba0`, "staircase-linear";
  `e33_deep_link_staircase.md`, the `E_r = (q-1) C(A,r) C(n-A,A-r)/q^t`
  count).
- **Repair.** The staircase budget column uses the **linear** count. The
  correction tightened the descent lattices (fixed-`d` bound slack — good
  for descent) rather than widening them.

### 7. h = 3 as a campaign (certification) row

- **Believed.** `h = 3` is one of the campaign rows to be certified — a
  first-class entry in the budget/staircase tables.
- **Falsifier.** The clean `t = 3` lane's **smallest actual trade size is
  `h = t + 1 = 4`**, not 3; `h = 3` is a base case, not a row to certify
  (`x14_h4_charged_sweep.md`: "the first real terminal size rather than
  another h=3 base-case row").
- **Repair.** `h = 3` was reframed as the **terminal estimate's proved base
  case** — the cubic cap `# active pairs < n^3` via the degree-`2n` root
  bound on `N_x^n - D^n` (`campaign_report_01_terminal.md`, "What is
  proved"; git `3049a213`). The certification lanes start at `h = 4`.

### 8. Elementary rigidity closes the kernel (R1-R4)

- **Believed.** A rigidity argument (few points determine the whole
  configuration) yields the terminal bound directly — the Rigidity Kernel
  as one schema four problems consume, attackable elementarily along axes
  R1-R4 (`rigidity_kernel.md`; `redteam_attack_plan.md`).
- **Falsifier.** X-12 killed the **elementary** rigidity route (git
  `6dc865fd`, "elementary rigidity dead; h=2 split off"); the rigidity
  sub-routes are recorded dead — Katz CE circular, Hall Legendre-only,
  rigidity needs `13 > 3` points, elementary Lefschetz trace insufficient
  (`beta2_dead_routes`, REFUTED; `experimental/notes/m1/m1_beta2_conditional_close.md`).
- **Repair.** `h = 2` split off to its own proved rung (Corvaja-Zannier,
  `A_2 <= 6 n^{5/3}`), and the "one statement" role passed to the
  **arithmetic-geometry dichotomy** (universal obstruction gate + char-0
  classification + good reduction). The R1-R7 red-team probes survive as
  the empirical **preview/falsifier** layer, not as a proof route
  (`redteam_attack_plan.md`).

### 9. The naive `worst_word_planted` (planted-only extremal)

- **Believed.** At the list-decoding crossing radii the extremal (worst)
  word is exactly the **planted sunflower family** — planted-only.
- **Falsifier.** The E15 adversarial search (#197) found a structured
  **low-slack non-planted challenger** at `sigma = 1` in the toy cell that
  the planted-only form misses (DAG node `worst_word_planted`, CONJECTURE
  "REVISED per the E15 COUNTEREXAMPLE"; `proof_sketch/s7_list_side.md`;
  `evidence_plan_codex.md`).
- **Repair.** The statement became **planted-family OR E15 structured
  challenger class**, and `list_planted_arithmetic` must price *both*
  exactly. The challenger is structured (not a fifth-mechanism signal), so
  the endgame arithmetic gained one classified column, not a new
  mechanism (`xr_smallcore_rungs_2a_2b.md`).

### 10. The h-only, n-uniform good-reduction target

- **Believed.** The good-reduction exceptional set can be `h`-only: a
  single integer `D(h)` such that for **all** `n` and all `p` coprime to
  `D(h)`, no extra trades appear at `(n, h)`.
- **Falsifier.** This is **false as a target shape**: as `n` grows through
  2-powers, new anchored non-candidates appear whose obstruction values are
  new cyclotomic integers with new prime divisors; nothing bounds their
  prime support uniformly in `n` (the verified `q`-sweep exceptional primes
  at increasing `n` demonstrate it) (`a3_good_reduction_lemma.md` sec 6,
  "why naive n-uniformity is false").
- **Repair.** The lemma proves the correct **per-pair** form `A3(n, h)`: a
  computable exceptional integer `D(n, h)`, row-independent within a row
  class, consumed by per-row GCD certification (`a3_good_reduction_lemma.md`;
  `verify_c2_gcd_harness.py` self-test recovers `{7, 17, 97}` at `(16,3)`).
  The `h`-only uniform bad-prime statement is a named open gap (G4), *not
  needed* for closure at official rows.

### 11. The four-levels-of-descent claim (delta-saturation)

- **Believed.** The C1b descent-injection certificate reaches the
  censusable domain `n = 64` in **4 levels** (`log2(1024/64)`), covering the
  whole window by descent to a brute-forceable bottom.
- **Falsifier.** The `delta`-recursion `delta' = floor((h + delta)/2)` hits
  the vacuous `h - 1` after only `~log2(h)` levels, retaining `h/2^k`
  coefficients of information per level — the descent **saturates** long
  before 4 levels (git `d8106f0f`, "the band budget saturates"; the C1b
  node correction in `experimental/data/prize-dag/prize_dag.json`).
- **Repair.** The corrected coverage map: C1a (direct MITM) covers
  `h = 4(-5)`; C1b (descent) covers `h <= ~8-10`; **`h >= ~16` needs a
  separate large-h emptiness lemma** as a third piece. This correction
  forced blocker 3 (mid/large `h`) onto the critical path explicitly
  (`critical_path_status_2026_07_04.md`), and is recorded, not hidden.

### 12. The `2 log2 n` window cap

- **Believed.** The consumer trades are capped at `h <= 2 log2 n = 20`
  (the `H_max` in `a_closure_assembly.md`).
- **Falsifier.** The h-window audit found the `2 log2 n` cap corresponds to
  **no banked object** and sits below every Row-C agreement number
  (`20 < 67 <= A`), so it bounds nothing; even the real banked cap
  `(log2 n)^2 = 100` is definitional (a frozen grammar choice) and lies
  below `A` at rates 1/4, 1/8 (`h_window_derivation_audit.md` sec 2, T1c/T1b).
- **Repair.** The true a-priori envelope is `H_max = A` (Row-C: 261/133/67),
  pinned by the star-PTE support micro-lemma `t < h <= A`
  (`star_pte_support_bound.md`; the trade support `2h` splits across two
  agreement sets, so the `2h <= A` reading is wrong). Repointing
  `H_max := A` **widened** the declared gap to `(100, A]` (git `f2bd806a`) —
  an honest enlargement of the open region, and the value-set partner cap
  (`<= n` partners per anchored core, all `h`) was proved as the harvestable
  companion.

## Further corrections (honorable mentions)

Beyond the twelve, smaller falsify-and-repair events kept the budget
columns honest: the **dihedral-parity clause** (E30: even-`j` dihedral
words are anti-reciprocal at odd `j`, which the clean-rate candidates sit
at — the budget's dihedral column must use the corrected form; git
`9c15152e`); the **`k`-multiplier reduction** (its residue matrix is a
rank-1 outer product mod `p`, so the Green-Tao-favorable counting
presupposed an independence that never holds — `multi_multiplier_reduction`
REFUTED; `qa16_multiplier_impossibility.md`); and the **measured
infeasibility** of the brute-force certificate at `n = 1024` (elimination
dies at `n = 32`), which forced the descent/certification blockers and is
recorded rather than papered over (`critical_path_status_2026_07_04.md`).

## The takeaway

None of the twelve is an embarrassment; each is a load-bearing beam. The
program's guarantee is not "we were right the first time" — it is "every
claim that could be false has a wired falsifier, and the ones that were
false are on this ledger with their repairs." The current structure —
compiler, symmetry-complete taxonomy, proved dichotomy, five enumerated
certification blockers (`critical_path_status_2026_07_04.md`) — is exactly
what survived this attrition.
