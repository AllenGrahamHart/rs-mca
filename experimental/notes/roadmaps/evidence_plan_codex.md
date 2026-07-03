# Evidence-gathering plan — targeted falsifications and toy proofs (for Codex / any lane)

- **Status:** AUDIT / experiment campaign spec. Companion to
  `execution_queue.md`, `redteam_attack_plan.md`, `enumeration_routes.md`
  and the prize DAG.
- **Objective:** these tasks exist to move PRIORS, not to prove the prize:
  each targets a question where the roadmap-maker is genuinely unsure and
  the two outcomes lead to DIFFERENT route choices. Results feed DAG
  updates (gate reweighting, new grounded conjectures, or S9 ledger
  events). Tasks where both outcomes imply the same next action were
  deliberately excluded — they carry no decision information.
- **Pre-registration discipline (mandatory):** each packet states, BEFORE
  the run: the search space, pinned seeds, the acceptance computation, and
  the interpretation table below verbatim. Negative results are results —
  publish them identically. A falsification hit is a first-class
  COUNTEREXAMPLE contribution (S9 protocol; see redteam_attack_plan.md).
- **Deliverable format:** repo-standard packet (note + verifier + JSON
  artifacts + agents-log), one task per PR, citing the DAG node id and the
  E-number here. Outcome classification printed by the verifier itself.
- **NOTE:** PR #176 already supplies the SPI base-case evidence stream
  (deficiency-1 ladder / prediction P3) — not duplicated here; its outcome
  slots into the same update framework (P3 pass => SPI route prior UP;
  unpaid identically-valid pencil => R2-as-stated falsified).

## E1 — Zone-(b) Row-C sampling: WHICH END OF THE CORRIDOR IS REAL?

```text
TARGET    zone_b / e1_fullness (CRITICAL; four-way route gate)
QUESTION  are e1 value sets (1-o(1))-full or heavily collided for
          quotient orders 80 < N' < 512 at prize-scale p?
PRIOR     ~50/50 in-corridor — the single most information-dense
          unknown on the board
METHOD    numerical, birthday sampling: n = 2^10 row, log2 p ~ 250,
          N' restricted to DIVISORS of n (spec corrected per PR #180's
          compatibility finding: 96/192 invalid on 2-power rows);
          pilot done (#180): zero collisions at 2^18/cell, support
          >= 2^33.4. DECISIVE FOLLOW-UP: N'=64 full birthday run
          (~2^25-2^26 samples reaches the 2^49.7 class count); open
          in-corridor cells (N'=128+) exceed birthday scale — use
          structured-subfamily collision estimators or the
          collision_norm_criterion route instead
INTERPRET density -> 1:      e1_fullness prior UP strongly; corridor
                             lands at the quotient crossing; prioritize
                             norm/amplification extensions (QZ tier);
                             averaged_slope_conversion deprioritized
          heavy collisions   collided branch REAL: averaged_slope_
          at some N':        conversion becomes load-bearing (unsafe
                             side), collision structure gets a new
                             grounded conjecture node (what divides the
                             norms), R4 conspiracy search escalates
          mixed by N':       zone charts gain an interval structure —
                             new stratified conjecture, per-N' gates
```

## E2 — Toy XR inverse: DOES THE ENERGY ROUTE HAVE CLEAN CONTENT?

```text
TARGET    xr_inverse (the XR pipeline's core bet)
QUESTION  at toy scale, is every E_3-large pair structured
          (folded/equivariant or tangent), or do unstructured
          energy-large pairs exist?
PRIOR     ~60% clean — the E_3 functional is OUR invention; this is
          the cheapest kill-or-confirm on the whole XR route
METHOD    numerical + exact algebra: n = 16 (mu_16 in F_97) exhaustive
          over pair orbits; n = 32 sampled; compute the E_3 spectrum
          (definition per QX.1/xr_e3_calculus — build it first or
          co-develop), list top-decile pairs, classify each against
          the known structure taxonomy (verifier prints the residue)
INTERPRET all structured:    XR route prior UP strongly; invest
                             xr_gvn/QE.1 next; C_XR content conjecture
                             added to the DAG (grounded)
          unstructured pair  DECISIVE either way: (a) if it has unpaid
          found:             alignment mass -> fifth-mechanism preview
                             through the energy lens (S9-relevant!);
                             (b) if paid -> E_3 needs redefinition;
                             xr_gvn spec revises BEFORE anyone builds
                             the Cauchy-Schwarz chain
```

## E3 — Spread-regime designs: TRY TO KILL THE CRYSTALLIZATION RESIDUE

```text
TARGET    spread_regime_bound (the open half of crystallization;
          DATA-FIRST by standing decision)
QUESTION  can combinatorial designs (pairwise support intersections
          < k) realize super-poly many aligned slopes?
PRIOR     ~75% true — but with essentially NO evidence in the
          all-small-intersections regime; the two-slope lemma provably
          cannot see it
METHOD    algebraic + numerical: n = 16..64; build co-support families
          from packings/Steiner-like systems; solve the alignment
          linear systems for (u,v); record max #slopes vs family size
          and n; adversarially optimize (this is R5 with growth
          tracking added)
INTERPRET max slopes O(n^c), pattern documents WHICH designs saturate:
          small c stable:    spread_regime prior UP strongly; the c
                             value becomes the conjectured exponent
                             (new grounded statement); XR/SPI
                             classification stages inherit the bound
          growing trend:     falsification track: minimal reproduction,
                             COUNTEREXAMPLE packet; r2_rigidity
                             restates (paid taxonomy gains the design
                             mechanism); corridor arithmetic recomputes
```

## E4 — Auxiliary-list wide regime: THE MIXED-PETAL RESIDUE, MEASURED DIRECTLY

```text
TARGET    pma_wide_residual (single-point-of-failure chain for the
          list challenge)
QUESTION  in the many-petal, sub-Johnson regime, do the auxiliary
          pieced-word lists stay poly (correlated-target structure
          working) or grow?
PRIOR     ~80% poly — but the wide regime is exactly where no data
          exists; the aux-word reduction (QP.1) makes this experiment
          CLEAN for the first time
METHOD    numerical: toy sunflowers (n = 32..128), petal count M swept
          ACROSS the Johnson threshold (d+sigma)^2/(d(sigma+1));
          directly enumerate degree-<=d polynomials near the pieced
          word U* = c_i L_D on T_i; plot list size vs M
INTERPRET bounded/poly:      pma_wide_residual prior UP; the M-scaling
                             data selects between correlated-GS and
                             descent (attack angles a vs b) — the
                             winning angle gets the next decomposition
          super-poly growth: imgfib in danger AS STATED: escalate R3
                             (structured vs unstructured hit); if
                             unstructured, the list-side threshold
                             conjectures revise (major S9-list event)
```

## E5 — Multi-scale resonance: FIRST EVIDENCE IN THE HIDING ROOM

```text
TARGET    payment_completeness (CRITICAL; the 3-strikes hypothesis)
QUESTION  can phase-locked structure across MANY dyadic scales create
          unpaid alignment mass invisible to per-scale ledgers?
PRIOR     ~65-70% no fifth mechanism — the least-tested load-bearing
          assumption (all prior failures of its class were found by
          construction)
METHOD    numerical construction search (R1): n = 2^10..2^12 (8-10
          nested scales, no toy analogue); words assembled from
          isotypic components across several K_M simultaneously,
          phases locked so each single-scale ledger sees
          sub-threshold mass; measure unpaid alignment vs FM baseline;
          structured search space PRINTED (no silent caps)
INTERPRET nothing above FM   payment_completeness prior UP — the first
          by poly factors:   evidence that touches the actual hiding
                             room; red-team pressure shifts elsewhere
          super-FM mass:     FIFTH MECHANISM candidate: minimal
                             reproduction, S9 protocol (ledger node,
                             taxonomy version bump, corridor moves)
```

## E6 — GAP-1 amplification: PUMP THE KNOWN CRACK

```text
TARGET    gap1_noneq_mass (CRITICAL; strip's conditionality)
QUESTION  does non-equivariant periodic mass grow poly or can the
          isolated witnesses be amplified into families?
PRIOR     ~80% poly — but the witnesses exist and nobody has tried to
          amplify them (Q3.3 measurement + R2 construction combined)
METHOD    exact enumeration at F_13/F_97 toys (all K_M-stable supports,
          count multi-isotypic aligned pairs) + constructive
          amplification attempts at n = 64..256; fit growth in n
INTERPRET poly fit:          gap1 prior UP; strip conditionality
                             quantified (the fitted exponent becomes
                             the conjectured constant — grounded)
          super-poly:        GAP-1 ledger required: strip pricing
                             incomplete; paid_closure gains a column;
                             mca_safe assembly restates
```

## E7 — Conjecture F at dimension 2: THE UNAVOIDABLE CONJECTURE'S FIRST OPEN INSTANCE

```text
TARGET    f_primitive_case (dim 1 is PROVABLE at n/j; dim 2 is the
          first unknown)
QUESTION  what is the actual max count of gcd-trivial aperiodic D_j
          points on PAIR-GENERATED planes (kernel/fiber planes — the
          planes the proof actually consumes)?
PRIOR     ~85% poly with small exponent; the VALUE of B_F is unknown
          and matters for every budget downstream
METHOD    exhaustive at n = 16 over pair-generated kernel planes
          (finite: pairs -> planes -> count D_j points, classify
          against paid shapes); sampled at n = 32; tabulate the top
          offenders and their structure
INTERPRET max bounded small: F prior UP + FIRST EXPONENT ESTIMATE
                             (B_F conjecture becomes a number — new
                             grounded node); budget_b3 cross-checked
          a rich plane       INSPECT ITS SHAPE: if it matches a known
          found:             paid stratum, the classifier was
                             incomplete (fix); if genuinely new -> the
                             conj_f statement itself revises — the
                             most consequential possible outcome of
                             this whole campaign
```

## E8 — Mixed-radix toy row: OFF THE 2-POWER CHAIN FOR THE FIRST TIME

```text
TARGET    mixed_radix_frontier (NEW: the family-uniformity gap)
QUESTION  does the base machinery survive when quotient scales form a
          lattice (incomparable M) instead of a chain? EVERY existing
          artifact is a 2-power row; the prize family quantifier is not.
PRIOR     ~90% VACUOUS: the standard FRI/STARK reading of 'smooth' is
          2-power, which the Q0.1 ePrint check confirms; and wp0_2's
          conservativity sketch says 2-power is the quotient-richest
          (hardest) case anyway. Run this ONLY if the rules freeze
          lands on a broader definition.
METHOD    F_97 supports n = 48 = 2^4 * 3. Rerun: FM exact means;
          periodic strata counts over the full divisor lattice
          (including incomparable 2^a*3^b); dedup totality/disjointness
          fuzz; coset-move dynamics. Name every invariant that fails
          to reproduce.
INTERPRET all reproduce:     uniformity prior UP; the frontier's
                             attack surface narrows to the zone-cell /
                             corridor arithmetic on lattices
          named breakage:    the single most valuable negative result
                             available — it localizes exactly which
                             statements silently assumed chain
                             structure, BEFORE the rules freeze
                             potentially makes mixed radix official
NOTE      cheap (toy scale) and high-information in BOTH directions;
          also previews the lattice-forced analogue of E5's resonance.
```

## Suggested order (expected information per unit cost)

```text
1. E1 (corridor decider — highest single-number information)
2. E2 (kill-or-confirm on a whole route, cheap)
3. E3 (the falsifiable core; no evidence exists either way)
4. E7 (data on the one unavoidable conjecture + an exponent)
5. E4 (single-point-of-failure chain, newly measurable)
6. E6 (known crack, cheap enumeration first)
7. E5 (low hit-prior but program-level impact; run in background)
8. E8 CANCELED PERMANENTLY (2026-07-03): blueprint line 102 defines
   smooth as power-of-two order, definitively. Do not run.
```

The roadmap-maker lane commits to processing every completed packet into
the DAG within one maintenance pass: gate reweighting notes, grounded
conjecture nodes (with the measured constants), or S9 events — with the
packet cited as the evidence edge.

# WAVE 3 (2026-07-03) — evidence for the morning decompositions

Same discipline: pre-registered tables, one PR per task, negative
results publish identically. Ranked by expected information.

## E17 — Hankel-kernel support patterns (gates f_termination_hankel)

```text
TARGET    f_termination_hankel / f_descent_termination
QUESTION  are sparse-dual-word supports of Hankel-kernel flats always
          COSET UNIONS (the displacement-structure prediction)?
PRIOR     ~80% yes — E7's kernel twins were exactly coset pairs
METHOD    E9-style census RESTRICTED to Hankel-pencil kernel flats
          (n = 16, j <= 5; the #183 kernel-sample machinery reruns);
          record every sparse word's support against the coset lattice
INTERPRET all coset unions => the lattice bound (QF.14) proceeds on
          the divisor poset; ONE non-coset support => the prediction
          dies and termination needs the general lattice argument
```

## E18 — Full pair-orbit E_3 scanner (the c_xr_content kill-switch)

```text
TARGET    c_xr_content / xr_inverse
QUESTION  E11 scanned a candidate DICTIONARY; do actual A_{u,v}
          pair-orbit alignment sets, post-strip, have top E_3 only at
          fixed-core/fixed-hole structures?
PRIOR     ~75% clean (dictionary + k=1 dictators both agree)
METHOD    exhaustive pair orbits at n = 16 (mu_16 in F_97), sampled at
          n = 32; strip quotient strata; compute E_3 of the true
          alignment sets; classify every top-decile set
INTERPRET clean => c_xr_content grounded at the object level; the KMS
          route proceeds with confidence | an unstructured top set =>
          C_XR needs a new member BEFORE the import note is written
```

## E19 — Globalness measurement (previews the XR shortcut)

```text
TARGET    xr_globalness_from_ledger
QUESTION  do post-strip alignment sets have link densities BELOW the
          KLLM globalness threshold at every core size r?
PRIOR     ~70% yes (the tangent ledger should enforce it; never measured)
METHOD    same pair-orbit data as E18: for each alignment set, tabulate
          density on every fixed-core link (r = 1..4) vs the paid
          tangent bound and vs the KLLM threshold formula
INTERPRET below threshold everywhere => the globalness certificate is
          real; QX.11 becomes a write-up | a leak at some r => either
          an unpaid tangent leak (R2-relevant — report loudly) or the
          strip is incomplete at that scale
```

## E20 — KMS/KLLM loss-exponent tables (statement arithmetic, no compute)

```text
TARGET    xr_kms_parameter_matching
QUESTION  do the published quantitative forms (KMS Johnson, DKKMS
          Grassmann, KLLM global hypercontractivity) survive FM-scale
          measure mu ~ q^{1-t}?
PRIOR     raw KMS ~25%; KLLM route ~65%
METHOD    literature statement extraction ONLY: tabulate each theorem's
          loss exponents; per rate, compare against the available FM
          gap; no experiments
INTERPRET KLLM survives => the import (QX.12) proceeds | both fail =>
          the XR wall needs a strengthened small-set theorem — named,
          honest, and known before anyone writes bridge notes
```

## E21 — Circuit census growth (calibrates the syzygy branch)

```text
TARGET    spread_syzygy_circuit_bound / circuit_locus_density
QUESTION  how does the minimal-circuit count grow in n (E13: 71 at
          n = 32, first 16 blocks)?
PRIOR     q-suppressed poly growth (~75%) per the determinantal-locus
          prediction
METHOD    extend the E13 census across n = 16..64, full block ranges,
          two field sizes (to see the q-dependence directly);
          also settle the flagged caveat: do the two identities
          involve (u,v) or locator data only
INTERPRET growth matches deg/q^c => QS.4's density argument is
          calibrated | faster growth => the locus argument misses
          circuit families — the branch needs its own taxonomy
```

## E22 — Challenger-class census (completes the E15 repair)

```text
TARGET    worst_word_planted (revised) / list_planted_arithmetic
QUESTION  does planted + the E15 structured challenger class EXHAUST
          the extremal words, and what is the challenger's exact count
          formula?
PRIOR     ~70% two classes suffice
METHOD    extend the E15 search at sigma = 1..3, n = 16..64: enumerate
          all words beating 0.9 x planted list; classify against the
          two known classes; extract the challenger count formula
INTERPRET two classes exhaust => QL.5's two-column arithmetic closes
          the repair | a THIRD class => iterate the E15 protocol
          (enlarge, price, re-census) — the endgame absorbs it
```

## E23 — The A=425 unsafe side (the strongest unclaimed item, now with compute)

```text
TARGET    second_pin_a426
QUESTION  is LD_sw(RS[F_p, D, 256], 425) > 87 at the #204 budget-prime
          row?
PRIOR     ~85% yes (the staircase steps by q-factors; 425 sits one
          step below a count that EQUALS B*)
METHOD    exact computation in the #204 framework one grid step down:
          the two-core structural numerator at A = 425, specialized to
          the budget prime; if exact evaluation is heavy, a certified
          witness family (qfloor at the active scale) suffices for >
INTERPRET > 87 => THE SECOND PIN IS COMPLETE — a window-edge
          threshold-pinned row, the strongest partial of the program;
          <= 87 => the crossing sits deeper: relocate the budget prime
          per the staircase table and re-run (the framework makes this
          a parameter change, not new mathematics)
```

## E24 — LLL/BKZ collision hunt: DECIDE the cells sampling cannot reach

```text
TARGET    zone_b open cells / kernel_lattice_reframing /
          lattice_cone_certificate
QUESTION  does the kernel lattice K_p = {v : sum v_x zeta^x = 0 mod p}
          contain sparse ternary vectors (support <= 2l') beyond the
          cyclotomic relations, at N' = 128 and 256, for Row-C-class
          primes?
PRIOR     ~85% no (matches typicality + Gaussian heuristic ~2^-50)
METHOD    build K_p explicitly (rank N', index p; p = 1 mod N' so zeta
          in F_p — pure linear algebra); run LLL then BKZ with
          increasing block size; record the reduced basis profile and
          every short vector found; test each for ternary-sparsity;
          quotient out the known cyclotomic relation sublattice first
INTERPRET no sparse ternary vector at practical block sizes + healthy
          basis profile => the open cells gain their first DIRECT
          evidence (beyond all sampling reach); the profile data feeds
          the cone-certificate design | a sparse ternary vector FOUND
          => AN ACTUAL COLLISION at an open cell: the collided branch
          is real, zone-(b) verdict changes, averaged_slope_conversion
          promotes — the single most consequential possible finding
          on the unsafe side
NOTE      this instrument reaches exactly where birthday sampling was
          proven infeasible; either outcome is decisive-grade.
```

## E25 — THE DIHEDRAL AUDIT (urgent; decides whether we found the fifth mechanism)

```text
TARGET    payment_completeness / dihedral_quotient_stratum / zone_b
QUESTION  do inversion-symmetric (palindromic/reciprocal) configurations
          generate UNPAID MCA bad slopes on multiplicative prize rows,
          or are they absorbed by existing ledgers?
PRIOR     ~55% absorbed — the zone-(b) antipodal-class machinery already
          quotients by a related symmetry, and v12's Chebyshev cap-side
          machinery treats the class; but the red team NEVER searched
          dihedral structure (E5/R1 were multiplicative-only)
METHOD    exact toys first (F_17, mu_16; F_97): build palindromic
          locator families l_I (inverse-pair quadratic products), solve
          the alignment systems for words (u,v) with dihedral symmetry
          (u(x^{-1}) = x^{-deg} u(x)-type); count bad slopes vs the
          tangent/quotient/antipodal charges; then the M5 chart
          machinery at A = 384-426 restricted to palindromic supports
INTERPRET absorbed => taxonomy completion: add the dihedral ledger
          (v12-Chebyshev machinery imports), restate the strip, DONE at
          bookkeeping cost | UNPAID slopes found => THE FIFTH MECHANISM:
          full S9 (new ledger, corridor arithmetic recomputes, caps may
          SHARPEN — a dihedral floor would be a new unsafe construction
          and a paper-grade discovery in its own right)
NOTE      either outcome is major; this is the highest-information
          single probe since E1.
```

## E26 — Dihedral window arithmetic vs the rate-1/2 coverage gap

```text
TARGET    rate_half_coverage_gap / dihedral_quotient_stratum
QUESTION  do dihedral/Chebyshev quotient windows (twin-coset fibers,
          d = m*ell degree arithmetic) provide unsafe coverage at
          effective scales inside [2^33, sigma*] at prize-max rate 1/2
          — i.e., does the new mechanism family fill the 2,978,147-
          radius granularity deficit?
PRIOR     ~50% — the scales are genuinely new (twin cosets, pair
          fibers) but whether their arithmetic interpolates into the
          deficit is pure computation
METHOD    window arithmetic only (no search): enumerate achievable
          dihedral and mixed dihedral-multiplicative window scales and
          their unsafe-count formulas at prize-max rate 1/2; compare
          against the deficit interval; exact analogues at the pinned
          row and Row C as calibration
INTERPRET coverage found => blocker (a) of rate 1/2 FALLS — the
          endgame there reduces to the tight composition + the thin
          margin point; also strong evidence the dihedral ledger is
          load-bearing on multiplicative rows (feeds E25)
          no coverage => the gap needs non-2-power quotient extension
          or bracket sharpening (as previously listed)
NOTE      pairs naturally with E25 (the dihedral audit): E25 asks
          whether the class is a paid stratum; E26 asks whether it is
          a USEFUL WEAPON. Run both.
```

# WAVE 4 (GATED) — the Rigidity Kernel probes, one per axis

Launch condition: after xr_target_budget_audit + E25 report (their
outcomes parametrize the tables below). Purpose: produce the OBSERVED
structure along which RK's decomposition will be written — per the
program's standing rule that classifications decompose after their
data, not before.

## E27 [axis Q — THE CENTRAL ONE] Exceptional-pair census
```text
Exhaustive at toy rows (n = 16, F_97; n = 32 sampled): for every pair
(u,v) with >= 1 unpaid aperiodic deep bad slope at the toy corridor
point, record the multiplicity spectrum (how many pairs have 1, 2, 3+
unpaid slopes) and CLASSIFY each exceptional pair's structure against
the 4-branch taxonomy + the trivial construction (u := c - z0 v on T).
INTERPRET: multiplicity-1 pairs abundant but multiplicity-(s+1) pairs
all structured => the forcing form of face 4 is TRUE at toy scale and
its decomposition = the observed forcing chain; an unstructured
multi-slope pair => RK's axis-Q core has a genuinely new exceptional
class (name it, S9).
```
## E28 [axis R] The empirical band map
```text
At toy rows, scan radii from w/3 (deep-mca proved) to the corridor:
at each radius, classify ALL pairs with bad slopes. Deliverable: the
radius at which each mechanism (tangent forcing, quotient, dihedral,
unstructured) first appears — the toy-scale map of the band. This
locates where deep-mca's dichotomy actually degrades vs where it is
merely unproved.
```
## E29 [axis J] Jointness measurement for Conjecture TR
```text
At F_13/F_97 (the #212 toy parameters): measure the joint
per-character product vs the per-leaf FM bounds across all active
sets — how many bits does jointness buy empirically, and does the
joint bound track n^B x FM? Calibrates TR's exponent before anyone
attempts its proof.
```
## E30 [axis D] Dimension-3 flat census with the dihedral branch
```text
Extend E7/E10 to dim-3 flats at n = 16 (sampled if needed): classify
sparse-dual structure with the ENLARGED taxonomy (multiplicative +
dihedral + tangent + descent); record whether any fifth shape appears
and the closed-set growth vs the fixed-d n^{O(d)} bound.
```
## E31 [axis T] (= #199 ladder reach, already in flight — consume its
result as the axis-T data; no new task.)

Assignment guidance: E27/E30 are light censuses (Fleet A-shaped);
E28/E29 are compute-heavier (Codex-shaped; serialize with anything
heavy per the RAM rule).

# WAVE 5 — the consolidated kernel gate slate (post faces-1-3 decomposition)

The derivation frontier is exhausted; these probes price everything
that remains. One PR each; tools exist for all of them.

## E32-MERGED [faces 3+4 jointly — supersedes E32-ext]
```text
The stagnation + exception census, one run, two consumers: (i) hunt
rank-stagnating far-spread triples (stacked-rank column on E27's
machinery); (ii) exhaustively enumerate light configurations at n=16
and evaluate the eliminant (evaluator: verify_xr_triangle_eliminant_
form.py); (iii) classify every identically-vanishing configuration;
(iv) restate E13's exception classes (AG/net, v-degenerate, syzygy
circuits) in the eliminant normal form — same objects, one language.
INTERPRET: all vanishing configs paid-patterned => beta-3b AND
face 3's classification write themselves | unpaid class => S9.
```
## E33 [face 4] deep-link staircase count
```text
As pre-registered: near-k-overlap aligned partners of a fixed
(pair, support) at toys. Linear => transfer-argument lemma;
super-linear => the derived-pencil recursion is load-bearing.
```
## E34 [face 1] the telescoping check (mechanical, cheap)
```text
At the F_13 toy (M4's verifier data): does the joint per-character
product equal/undershoot the single joint-stabilizer-scale instance?
YES => TR's jointness is structural (tower statement); E29 demotes
to constants calibration. NO => measure the excess; the joint
analytic content is real and E29 decides its size.
```
## E35 [face 2] weight-2 abundance column
```text
On E30's census machinery: per flat, count minimal weight-2 supports
vs symmetry-stratum membership (both dihedral parities). Deliverable:
the abundance threshold at which weight-2 count forces symmetry
(calibrates f_weight2_inverse's constant; falsifier = an abundant
asymmetric flat).
```
## E36 [face 2 keystone] exotic-stabilizer finite check
```text
For prize-class toy domains (2-power n | q-1, both parities of the
coset): enumerate the full PGL_2(F_q) set-stabilizer of the domain;
verify it equals Dih_n (or classify the exceptions). Closes
f_dih_subgroup_completeness's residual caveat.
```
## Non-evidence follow-ups (write-up lane)
```text
W1: pencil-cascade packet (last provable face-4 rung).
W2: the 2b graded tangent ledger design (consume the proved forcing
    map; charge cells by depth d = t - s).
```
Still queued from earlier waves: E28 (band map — now also feeds the
cascade-radius question), E29 (post-E34 role), C-1, C-5.

## E37 — THE MOMENT-BLOCK CENSUS (urgent; the fifth mechanism's per-row existence)

```text
TARGET    moment_trade_staircase / x4b_moment_trade_exclusion
QUESTION  do primitive (non-quotient, non-dihedral) t-moment-null
          blocks exist at official-row-like parameters? The verified
          witness lives at small p relative to n (F_193, mu_64, t=3,
          b=8); official rows have p ~ 2^128-256 with n <= 2^41 —
          Weil-type intuition suggests large p may FORBID small
          primitive blocks. Decide empirically.
METHOD    per (n, p, t): exhaustive/MITM search for 0/1 dual words of
          weight b in (t, 2t+4] with t leading zero syndromes, minus
          symmetric ones. Toy scan: n in {16, 32, 64}, p in several
          sizes from n+1-ish up to 2^61-ish; the p-size dependence is
          THE deliverable (existence threshold in log p / log n).
          Reuse the C-4 MITM machinery. SOLO if heavy.
INTERPRET large-p vanishing => the exclusion theorem is plausibly
          provable via Weil/character sums (route selected) and
          official rows are safe | blocks persist at large p =>
          the moment column is REAL at official rows: charge it
          (exact binomials) and re-run QA.22 with the fourth column.
```

## F4 — characteristic-p switch nets (X-5's residual red-team template)
```text
TARGET    u1_pullback_dichotomy (narrow/compression form)
QUESTION  do tame-row domains admit many DISJOINT gadgets with
          IDENTICAL moment defects Delta(r), r <= t? (p-fold switches
          then cancel: C(R, p) same-top-t locators from switch nets —
          not obviously shared-map-fiber-structured.)
METHOD    toy hunt at small p rows (the danger regime): enumerate
          gadget pairs (P_i, Q_i) by defect vector; count disjoint
          identical-defect families; test the survivors against the
          fiber dictionary. Include prime-power q rows.
INTERPRET none found at tame rows => the template is empty and the
          compression dictionary needs no switch-net clause | found
          => test chargeability; unchargeable switch nets = the
          compression conjecture's true adversary (name it loudly).
```
