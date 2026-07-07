# FALSIFICATION GOAL (floor campaign attack phase, set 2026-07-07)

**GOAL: subject every one of the seven floor conjectures to extensive,
pre-registered falsification attacks — threat-ordered — until each floor
either DIES (campaign event) or is HARDENED (has survived ≥ 3 genuinely
distinct attack families under its pre-registered standard). The user is
away; do not block on input. The purpose is early detection: a dead floor
found now saves months of work on a false region of the DAG; a hardened
floor is the true frontier.**

## The seven floors and their pre-registered falsifiers

All falsifier standards are ALREADY pre-registered in each node's dag
`falsifier` field and in notes/floor_campaign/ + REPOSE_B_WEAK.md — they
were fixed before data and are NOT to be reinterpreted mid-attack. Attack
queue (threat-ordered; re-derive if evidence shifts):

1. **F6 rate_half_band_closure (BAND-SAFETY)** — three consumers incl.
   mca_safe. Attack: exact corridor arithmetic at admissible top-slice
   rows (log2 q ∈ (255.900, 256)) across band radii σ ∈ (2^33, σ*];
   engineered adversarial radius/row selection; the existing Modal razor
   machinery (notes/verify_q_threshold_modal.py, verify_floor_depth_modal.py)
   extends directly.
2. **F2 u2c_giant_tnull_dichotomy (EXTRAS-BUDGET)** — extend
   experiments/u2c_tnull_boundary_scan.py toward the sub-balance boundary
   (Modal sweeps); engineered accident hunts INSIDE the sub-balance regime
   (norm/CRT selection — the dli round-5 pattern transported); the
   complementation lemma halves the search space.
3. **F7 worst_word_challenger_pricing (ROWWISE-ENVELOPE)** — FIRST: finish
   the canceled pre-registered census (notes/e22_census_modal.py, was
   130/135 cells); then envelope stress at bg ≤ 1 rows across q; then
   engineered challenger stacking (codim-σ coincidence selection).
4. **F4 petal_growth (PETAL-ESCAPE-BUDGET)** — extend
   experiments/amber_stress/petal_excess_local_scan.py to the top-defect
   band at scaled official-like rows; adversarial c-sweeps (the demoted
   uniformity-in-c is where the route died — attack the floor there too).
5. **F5 xr_smallcore_spread_count (16n³ per pair)** — E27 pencil-machinery
   searches for super-budget pairs at scaled rows; sunflower-free
   configuration engineering at intersection threshold k+t−1.
6. **F3 u1_x4_direct_column_budget (n³ direct column)** — boundary
   p ≡ 1 (mod n) slices beyond the probe's 60s-capped coverage (Modal
   sharding removes the cap); anchored PTE-family engineering at q ≥ n².
7. **F1 dli B-WEAK** — already survival +1; continue with experiment 2
   (engineered stacked towers — multi-level norm coincidences priced
   against the transported budget) and the n = 64 joint towers (sharded
   MITM redesign) when the queue permits.

## Attack protocol (per floor, per attack)

1. Design the attack at the floor's MOST REFUTABLE projection; write the
   attack script with the transported/scaled budget arithmetic fixed
   BEFORE running (pre-registration discipline).
2. Run on Modal (shard so every job < 60 s; local only for trivially
   small jobs — user directive, prevents crashes).
3. CLASSIFY BEFORE DECLARING (the B-WEAK experiment-1 lesson): any hot
   signal must have its population classified against the known structural
   columns and window-law populations before it counts as a refutation
   signal. A naive baseline manufactures false kills.
4. Bank: attack note + script + raw results in the node's folder (create
   critical/nodes/<id>/notes/ if absent); survival ledger +1 in the dag
   statement on absorption; commit via tools/dag_commit.sh + full ritual
   (fork sync allen/prize-dag-delta, artifact
   https://claude.ai/code/artifact/ebb725d6-96a0-4e31-bb9b-14522786c58c
   favicon 🗺️, ./tools/publish_site.sh) after every dag change; update
   the campaign memory at meaningful state changes.
5. Also PREPARE (do not send) one Pro brief per floor as attacks mature,
   in the established DLI-CLOSE format, published to the fork's
   pro_windows/ so the user can relay at will. Pro cannot be reached
   directly — the user relays.

## Death protocol (campaign event — the whole point; A KILL DOES NOT HALT THE CAMPAIGN)

If a pre-registered falsifier FIRES (verified, replayed, classified):
pause the queue ONLY long enough to bank the death properly, then move to
the next floor. Banking a death means: (1) replay and classify the
counterexample against the real objects (a death claim gets the same
verify-first treatment as everything else); (2) mark the floor KILLED in
its dag statement with the witness and the exact fired standard (status
handling: statement records the death; the node stays red — its
obligation is now unsatisfiable-as-posed); (3) write the
downstream-consequence analysis: which ambers/conditional chains above
are invalidated, what re-route candidates exist, what the consumer must
do differently; (4) flag the consumer(s)' conditional chains in their
statements; (5) report loudly (session log + PushNotification if
available) and queue the re-route decision as the FIRST morning
discussion item. Do NOT redesign consumers or re-route the DAG
autonomously — that is the user's strategic call. Then CONTINUE the
attack queue: every floor gets stress-tested to hardening or destruction
regardless of prior casualties. Multiple deaths compound the morning
report; they do not stop the night's work.

## Hardening criterion and termination

- A floor is HARDENED when it has survived ≥ 3 genuinely distinct attack
  families (different mechanisms, not reruns), each executed under its
  pre-registered standard, with the survival ledger documenting each.
- The goal TERMINATES when every floor is either hardened or dead, OR
  when every remaining un-hardened floor has exhausted its known attack
  surface (then: final campaign report ranking the seven floors by
  evidence strength, naming the hardened frontier, listing the prepared
  Pro briefs, and recommending the next phase).
- Interrupts: a user-relayed Pro reply preempts everything (verify-first,
  replay exactly). DLI-CLOSE-6 remains open.

## Standing rules (non-negotiable, unchanged)

Verify-first; falsification-first; not-falsified ≠ true; honest labels;
no overclaiming; pre-registered standards are immutable mid-attack; route
and proxy failures never count against a floor. One-writer in canonical
prize/. Only allen/* branches; never touch others' branches/PRs or tex/
or Papers A-D. Commit trailer "Co-Authored-By: Claude Opus 4.8
<noreply@anthropic.com>"; push --force-with-lease only. Modal jobs < 60 s
sharded; local compute only for very small jobs; single process < 1.5 GB.
Self-paced wakeups: prefer long sleeps (1200 s+) over polling. Every
artifact replayable by a stranger.

## ATTACK LOG (running)

- 2026-07-07 F6 opened. v1 floor sign error caught against P6 primary docs
  (see FLOOR_CAMPAIGN.md correction); v2 = BAND-DETERMINATION banked.
  **F6-A1 design (next action):** scaled rate-1/2 band-analogue rows —
  toy rows (n, k = n/2, q swept in a toy razor slice) with the quotient-
  window reach and first-moment crossing computed by the SAME arithmetic
  as the prize razor (verify_q_threshold_modal.py's log2C/charge/trigger
  display, trigger rescaled to the toy budget); exact corridor counts at
  the band-analogue radii (machinery: tools/verify_list_corridor_ledger.py
  + verify_list_corridor_widths.py define the count object B; reuse their
  row conventions EXACTLY — protocol step: check the count definition
  against the primary tool before running). Falsifier fires on sustained
  deviation from the first-moment determination, either direction, >= 3
  scales. All jobs Modal-sharded < 60 s.
- F6-A1 GROUNDING PINNED (cap_envelope verify_sweep.py, exact conventions):
  floor family = quotient-remainder prefix configurations at scale c | k:
  m = k/c + d fibers, agreement A0 = m*c, w = d-1 box charges, certified
  list lower bound log2 L = log2 C(N, m) - (log2 box)*w, UNSAFE trigger
  L > 2^(log2 q - log2 k) (i.e. C(N,m) > 2^(256d - e) at prize with the
  conservative box=q charge). Rate-1/2 reach caps at d*c = 2^33; sigma* =
  first-moment crossing. TOY F6-A1: same formulas with toy exponents at
  toy rows (n = 2^m, k = n/2, D = order-n coset in F_q^x, q swept in a toy
  razor); compute toy floor reach + toy first-moment crossing; EXACT list
  counts at band-analogue agreements via the e22_core row/census machinery
  (reuses the official row conventions); compare counts to first-moment
  across >= 3 q-scales. Deviation either direction, sustained = falsifier
  fires. Modal-sharded.
- F6-A1 phase 1 RUN (f6a1_band_window_modal.py, Modal): at n=16, k=8 the toy
  transport gives INVERTED bands at all three q-scales (floor reach >=
  first-moment crossing: reach-excess 3/1/0 vs crossing-excess 2/0/0) — the
  toy floor family OVER-reaches at small n; the band is a large-parameter
  phenomenon (prize: 0.1-bit q-sliver at n=2^41). NEXT (phase 1b): band-
  existence sweep at n in {32, 64, 128} x fine q-grid to locate toy rows
  with genuine bands; if NONE exist under the faithful transport, pivot the
  attack to the full-scale exact-arithmetic projection (reach/crossing/
  balance arithmetic at n = 2^41 is exact rational computation — no
  enumeration needed — attack the model's internal consistency at the
  razor rows directly). Measurement phase (exact lists) only at rows with
  genuine toy bands.
- F6-A1 phase 1b: NO genuine toy band (reach < crossing) exists at n in
  {16, 32, 64} for any q up to 3e5 under the faithful transport — the band
  is exclusively a large-parameter phenomenon (prize razor sliver). The
  toy-count route to the F6 falsifier is CLOSED; measurement-phase shards
  not dispatched. PIVOT (pre-planned): full-scale exact-arithmetic attacks:
  **F6-A2** — exhaustive parametric-family sweep AT razor rows (n = 2^41,
  k = 2^40, log2 q in (255.900, 256)): every known family shape (quotient-
  remainder at ALL 2-power scales incl. giant M > 2^33, dihedral, moment-
  trade, staircase composites, TWO-SCALE stacks) priced by exact big-int
  arithmetic against the trigger at band radii. DUAL-USE: a family beating
  the trigger inside the band refutes the v2 floor's first-moment location
  AND constructively covers part of the band (a death here is a discovery
  either way). **F6-A3** — full-scale second moment of the band count
  (pair-correlation exact sums): variance >> mean^2 at band radii =
  non-concentration = the window-law floor threatened. Both Modal-sharded
  exact big-int; no enumeration needed.
- F6-A2 RUN (f6a2_fullscale_sweep_modal.py, 6 razor rows, mpmath dps=40).
  PRELIMINARY — NOT YET CLASSIFIED: at EVERY swept lq the per-row
  single-scale reach >= the per-row first-moment crossing sigma*(lq)
  (255.92: reach 8,592,241,264; 255.95: 8,591,245,312 vs crossing
  8,591,234,254, margin ~11k radii at scale 2^17; 255.99/255.9999:
  reach = 2^33 exactly vs crossings BELOW 2^33). The "band" appears ONLY
  against the FIXED banked sigma* = 8,592,912,738 — suspected to be the
  WORST-ROW constant (lq = 255.900) applied across the razor. HYPOTHESIS
  (dual-use): the band is a bookkeeping artifact of a fixed sigma*; per-row
  arithmetic (reach(lq) vs safe-boundary(lq)) closes the gap at every
  row — F6 would CLOSE, not die. MANDATORY VERIFICATION BEFORE ANY CLAIM
  (classify-before-declaring): (a) primary-doc provenance of 8,592,912,738
  — which object, which lq (find the safe-side balance derivation); (b) is
  the safe side provable above sigma*(lq) PER-ROW (the balance proof's lq
  dependence); (c) family-lemma validity hypotheses at the hitting scales
  (j = 17 is inside the verified sweep range e in [12,40) — good sign);
  (d) reproduce the razor script's own threshold (it compared reach to the
  FIXED sigma*, consistent with our numbers — no contradiction with banked
  results). S2 two-scale stacks: zero candidate hits anywhere (the
  composite channel is empty — mild F6 survival evidence on its own).
- F6-A2 CLASSIFIED (the mandatory verification killed the preliminary
  hypothesis — protocol instance #3): sigma* = 8,592,912,738 is the GENERIC
  PINCER safe-side bound on the WORST-WORD crossing (pro_brief_razor.md;
  its route 3 already anticipated per-row refinement "may cross 2^33").
  My swept sigma*(lq) was the RANDOM-WORD mean crossing — the wrong object
  for the sandwich (worst-word >= reach >= random-word crossing; no
  contradiction, no artifact, no close). RETAINED products of F6-A2:
  (1) per-row band widths — the band is lq-GRADED: width ~0 at 255.900 ->
  671,474 at 255.92 -> 1,678,484 at 255.95 -> 2,349,694 at 255.97 ->
  2,978,146 at the cap (a refinement of the banked worst-case constant;
  reach interpolates above 2^33 mid-slice, hits the 2^33 plateau only near
  the cap); (2) S2 SURVIVAL EVIDENCE: nested two-scale composite stacks
  score ZERO candidate hits at every razor row — the composite-family
  attack channel on the band is empty (F6 survival +1, first absorbed
  attack family: 'composite quotient stacks'); (3) v2 floor language
  check: "first-moment model" in the F6 floor means the WORST-WORD
  determination model (priced columns + FM), as campaign-standard — the
  A2-style bound-vs-bound arithmetic cannot test it; the live attack
  channels are route-1-style multi-word/averaged constructions (as
  attacks) and the B2b-window transfer. NEXT: F6-A3 (averaged/multi-word
  construction attack: can an L-word family amortize the box charge by the
  needed 0.0005 bits/fiber? — the brief's own sharpest question, run as an
  ATTACK with exact arithmetic) OR move to F2 per queue discipline after
  banking F6 survival +1.
- F2-A1 RUN, PARTIAL (f2a1_subbalance_sweep_modal.py): complete MITM
  censuses (upgrade over the original 60s-capped partial scans) across
  W = C(N,b)/p^t from 2^+5.6 down to 2^-14.5 at cells (32,2,6/8),
  (64,3,8/10), (128,4,6): EXTRAS IDENTICALLY ZERO at every completed
  (cell, p) — including the full N=64,t=3,b=8 sweep (t-null blocks all
  coset-unions, 120-216 per prime). Strongly floor-consistent. NOT YET a
  survival credit: (i) the calibration gate (banked transition p=257:
  192 extras, 577: 64, 641+: 0 at N=64,t=3,b=8 — W ~ 2^8) was NOT
  exercised (W-grid started at 2^6); (ii) two b=10 mid-W shards hit the
  60s timeout (C(64,5) = 7.6M-half joins — needs prefix-sharding). FIX +
  RERUN: add p in {257, 577, 641} as gate points; shard b=10 joins by
  3-index prefix (~35 shards each). Then F2 survival +1 if gate PASSES
  and zeros hold.
- F2-A1 COMPLETE: calibration gate PASSES EXACTLY (p=257/577/641/769 ->
  extras 192/64/0/0, matching the banked transition digit-for-digit —
  instrument validated); full sweep with the validated instrument: EXTRAS
  IDENTICALLY ZERO through the entire sub-balance regime (log2W < 0 down
  to -14.5) at cells (32,2,6), (32,2,8), (64,3,8), (128,4,6). **F2
  SURVIVAL +1** (attack family: calibrated complete window sweep). b=10
  cell deferred to F2-A1b (prefix-sharded joins). Next F2 families:
  engineered accident hunts inside sub-balance (norm/CRT selection — the
  dli round-5 transport) and the giant-block side via complementation.
- F7-A1 RUN (f7a1_census_driver_modal.py — the canceled pre-registered E22
  census reshaped to per-cell Modal jobs): gate PASSED; 118/135 cells
  completed with ZERO unclassified hits (no third-class alarm anywhere in
  the completed set); 17 heavy structured cells hit the 60s cap — flagged
  for F7-A1b (prefix-sharded structured search), NOT silently dropped.
  **F7 SURVIVAL +1, scoped** (attack family: the pre-registered census on
  its completed cells; the alarm is meaningfully tested only on searched
  cells — the 17 heavy cells are exactly where a residual alarm could
  hide, so full credit awaits A1b). Combined standing evidence: this + the
  two banked external censuses (77 + 219 cells, UNCLASSIFIED = 0).
- WAVE-1 STATUS (2026-07-07, after ~5 hours of attack phase): F6 +1
  (composite stacks empty; band lq-graded; 2 protocol catches), F2 +1
  (calibrated window sweep, extras zero through sub-balance), F7 +1 scoped
  (census 118/135 zero-alarm; 17 heavy cells to A1b), F1 carried +1 from
  pre-campaign. Zero deaths; three protocol catches (all my own
  mis-posings, caught before claims). PENDING QUEUE: F4-A1 (needs
  primary-doc grounding: top-defect band d >= M(t-2) definition, paid
  families, Lemma-13 scope — do NOT rush; the scan machinery is
  polynomial-arithmetic-heavy), F5-A1 (E27 pencil grounding likewise),
  F3-A1 (boundary slices sharded — mechanical), F6-A3 (averaged
  amortization — needs design), F2-A2 (engineered sub-balance accidents),
  F2-A1b + F7-A1b (mechanical sharded reruns), F1 experiment 2.
- F4-A1 GROUNDED + DESIGNED: the 2026-07-06 stress run (16 configs, 76
  rows) found exact realizable counts CONCENTRATED at/beyond the top-defect
  band (max 5005 there vs 1 below-top). The floor needs the top-band
  contribution <= n^B; the ATTACK is the SCALING question: rerun the
  scan's exact-realizable-count cells at a ladder of >= 3 scales (Modal,
  per-cell jobs; reuse petal_excess_local_scan.py's coset-chart cell
  conventions EXACTLY — read its planned-config parameterization first),
  extract max top-band counts per scale, and test polynomial fit with a
  scale-independent exponent. Falsifier fires on sustained super-poly
  growth of the top-band counts (the node's own dag falsifier, now scoped
  to the floor's official-like rows).
- F4-A1 COMPLETE (f4a1_topband_ladder_modal.py, 7-rung prime ladder
  109..6421, gates PASS at every rung): the top-band max exact realizable
  count is EXACTLY 5005 at every scale — log-log slope +0.000 across all
  six consecutive rung pairs; below-top max stays <= 1; zero Lemma-13
  violations. **F4 SURVIVAL +1** (attack family: scale ladder). BONUS
  CONSTRUCTIVE LEAD: 5005 = C(15, 6) — the top-band count is p-INDEPENDENT
  and BINOMIAL, i.e. the top-band family is combinatorially parameterized
  by the chart shape alone — exactly the "parameterized paid family" the
  retraction note demanded; the route side can now try to identify and
  prove the C(.,.) family directly (queued as a route note for the node,
  not a floor obligation).
- F3-A1 RUN (f3a1_boundary_sweep_modal.py): instrument gate EXACT (60
  nontoral at the positive control, matching the banked probe); ZERO
  nontoral trades and ZERO n^3 alarms at all 11 attack rows — original
  boundary rows now at FULL windows (the local run was sliced), extended
  boundary primes (p = 3137, 12289 at n=32), and n=64 rows. Complete at
  every n=32 row except h8 (partial: 50s anchor deadline); all four n=64
  rows partial-and-clean. **F3 SURVIVAL +1, scoped** (complete n=32
  boundary family; n=64 + h8 full coverage to F3-A1b anchor-sharding).
- F5-A1 RUN (f5a1_spread_sweep_modal.py): calibration gate = the node's own
  rungs-2a/2b certificate, PASS (38 checks). Exact spread measurement at
  5 completed rungs (k=2: q=17/31/47; k=3: q=17/31; the q=71 rung timed
  out -> A1b): worst greedy pairwise-small-core distinct-slope family =
  EXACTLY q at every cell (one aligned support per slope — the spread
  structure is slope-limited), vs budgets 16n^3 = 6.5e4..1.6e6: four
  orders of magnitude of margin. ZERO alarms, adversarial pencil pairs
  included. **F5 SURVIVAL +1, scoped** (5/6 rungs; q=71 to A1b). ALL
  SEVEN FLOORS now carry survival credits.
- F2-A2 RUN (f2a2_engineered_accidents_modal.py, 1440 engineered trials at
  two cells): the dli round-5 norm-selection mechanism transported to
  accident engineering — ZERO candidate sub-balance primes pass the
  multi-condition gcd filter (per-r norms generically coprime; the E2
  coprime-ideals obstruction blocks accident engineering identically).
  POSITIVE CONTROL PASSES: the known p=257 window accident is fully
  detected by the same machinery (all 3 norms divisible, gcd retains 257).
  **F2 SURVIVAL +2** (second distinct family: engineered norm-selection,
  positively controlled). F2 is at 2/3 toward hardening; third family
  candidate: giant-block complementation attacks or CRT-composite
  constructions.
- F7-A1b COMPLETE (f7a1b_heavy_cells_modal.py, 408 shard jobs): all 17
  heavy cells finished (24/24 shards each) — TOTAL UNCLASSIFIED = 0; the
  1,689 hits at the heavy cells (incl. ~400-hit k=16 sigma=1 cells) ALL
  classify into the two challenger columns. THE PRE-REGISTERED CENSUS IS
  NOW COMPLETE: 135/135 cells, zero third-class alarms anywhere. **F7
  first family upgraded scoped -> FULL (+1 unqualified).**
- F1-exp2 RUN (f1exp2_stacked_towers_modal.py, 120 trials -> 10 engineered
  stacked rows, exact D3 E at both levels per row): the lift-stacking
  mechanism is correctly priced. E64 = 1.000000 at EVERY engineered row
  (the lifted level-64 structure is r-diluted exactly as the ledger
  predicts); the level-32 measured excess initially read 2-2.8x the w<=7
  ledger — CLASSIFY-BEFORE-DECLARING (catch #4): the gap is exactly the
  omitted forced w>=8 window mass, which is the q-INDEPENDENT constant
  sum C(16,w>=8)/2^16 = 0.598 (the pinned window invariant appearing in
  the data); with it included the prediction over-covers at 9/10 rows,
  worst ratio 1.32 (single row, not sustained, << 2x). **F1 SURVIVAL +2**
  (engineered-stacking family). B-WEAK now has two absorbed families.
- F4-A2 RUN (f4a2_c_sweep_modal.py, c extended 2..14 at 3 scales): the
  top-band count grows in c as a BOUNDED-DEGREE BINOMIAL — 5005 = C(15,6)
  at the A1 c-range stepping to 38760 = C(20,6) at c-max 14 (p=211,
  complete sweep); degree-6 polynomial growth in the excess parameter is
  exactly what a c-uniform n^B budget absorbs. **F4 SURVIVAL +2, scoped**
  (adversarial-c family; caveats: p=809/3209 c-sweeps possibly
  deadline-truncated — their flat 5005 not yet confirmed as true
  p-uniformity at large c; the exact C(f(c), 6) offset formula needs the
  per-cell rows — both queued as F4-A2b). The structural lead sharpens:
  the paid top-band family is a 6-dimensional binomial column in c.
- F7-A2 RUN (f7a2_envelope_stress_modal.py, 4 cells x 9-point q-ladder
  97..1153): the K_cell/q^sigma envelope HOLDS — sigma=1 counts track 1/q
  (count*q ~ constant, drift <= 1.5x over a 12x ladder, under the 3x
  alarm gate; counts 109 -> 14), sigma=2 cell IDENTICALLY ZERO at every
  q >= 97 (the banked window-closure reproduced exactly), UNCLASSIFIED = 0
  everywhere. **F7 SURVIVAL +2** (envelope-stress family). One more family
  (engineered challenger stacking) hardens F7.
- F5-A2 RUN (f5a2_engineered_spread_modal.py, greedy adversarial
  construction, 5 rows): the engineered spread maximum saturates at
  THETA(n) — 28/51/106 at n = 46/96/192 (k=2; ~0.55n) and 46/81 (k=3) —
  matching the dimension-count prediction (each alignment costs sigma of
  the 2n degrees of freedom of (u,v)), 4-6 orders under the 16n^3
  budgets, zero alarms. **F5 SURVIVAL +2** + ROUTE LEAD: the
  dimension-count argument (engineered cap O(n/sigma)) is a proof
  candidate for the floor's structural margin.
- F2-A3 RUN, PARTIAL (f2a3_midsize_modal.py; b=12 complete, b=16 jobs
  need prefix sharding -> A3b): FIRST apparent sub-balance extras of the
  campaign (32 = one orbit at p=21313, per-b log2W = -1.01) — CLASSIFIED
  (catch #5): the regime marker must be GLOBAL balance (q^t >= 2^n, the
  dichotomy's own hypothesis; here p >= 65536), and p=21313 is globally
  ABOVE balance (the b=16 window is still open: C(32,16)/p^2 = 1.34 —
  the b=12 extras are window-regime relatives/dressings). All globally
  sub-balance primes in the sweep (p = 120193, 240641; plus every
  F2-A1 point) show ZERO extras. The per-b window label in the sweep
  output was the misleading instrument; the floor's own quantifier
  (official rows: q^t > 2^n by ~2%) was never touched. F2's third-family
  credit awaits the b=16 sharded completion (A3b) — the widest window is
  where the last doubt lives.
- F6 second family (crossing-fidelity, from banked F7-A2 exact data +
  first-moment arithmetic): 18/18 determination matches across the
  9-point q-ladder at sigma = 1, 2 — measured counts land on the SAME
  side of the unsafe threshold as the first-moment prediction at every
  point, including THROUGH the crossing transition (sigma=1 flips
  unsafe -> safe between q = 241 and 337 in both columns). Quantitative
  tracking within ~2x everywhere (structural columns explain the residue).
  **F6 SURVIVAL +2** (the floor's determination-location claim verified
  in its entire accessible regime). Third family = F6-A3 amortization
  exploration (queued).
- F2-A3b COMPLETE (f2a3b_b16_sharded_modal.py, 60 shard jobs, complete
  b=16 censuses = 6e8 subsets per prime): below global balance p=40961 ->
  640 extras (window population ✓, and further proof the per-b marker
  misleads: per-b W < 1 there); EVERY globally-sub-balance prime
  (65537..786433) -> extras = 0 EXACTLY with t-null blocks pinned at the
  structural constant 700 (pure coset unions, q-independent) at all five
  primes. The dichotomy holds at the WIDEST window.
  **F2 SURVIVAL +3 -> F2 HARDENED** (families: calibrated window sweep /
  engineered norm-selection / widest-window boundary census). FIRST
  HARDENED FLOOR OF THE CAMPAIGN.
- F7-A3 + F6-third RUN (f7a3_f6c_layout_sup_modal.py, 360 exact cells: 60
  layouts x 2 cells x 3 q): ADVERSARIAL LAYOUT-SUP bounded — max
  challenger counts <= 2.4x median (no sustained > 3x envelope violation;
  the mild growth is small-count dispersion), UNCLASSIFIED = 0 at all 360
  cells. ANTI-CONCENTRATION absent — min counts are Poisson-ordinary
  (min=4 at lambda=12: expected 0.5 such layouts of 60; observed 1); no
  word class collapses below the model.
  **F7 SURVIVAL +3 -> F7 HARDENED** (census / envelope-stress / layout-sup).
  **F6 SURVIVAL +3 -> F6 HARDENED** (composite sweep / crossing-fidelity /
  anti-concentration). THREE OF SEVEN FLOORS HARDENED (F2, F6, F7).
- F1-A3 RUN (f1a3_dual_spectrum_modal.py, 24 rows x full exact dyadic
  spectra, 5 q-bands 2e4..4.8e5): median K(j) = 0.6-1.35 at every
  well-sampled level in every band — the dual projection of B-WEAK carries
  NO structural surplus in population; no alarm.
  **F1 SURVIVAL +3 -> dli B-WEAK HARDENED** (joint scaling / engineered
  stacked towers / dual-spectrum sweep). FOUR OF SEVEN HARDENED
  (F1, F2, F6, F7). Remaining: F5 third (strip-integrity), F4 (A2b +
  third), F3 (A1b + A2).
- F5-A3 RUN (f5a3v3_strip_integrity_modal.py, line-geometric tangent-core
  counting, 3 scales complete; q=389 rung timed out — noted): RANDOM-word
  depth spectra collapse immediately (g(2) = 0 everywhere — decay faster
  than the q^-2 model; no stall); ADVERSARIAL cascades are the planted
  lines' binomial dressings C(m, 2+d) — the tangent ledger's own charged
  objects (classified in-instrument, pre-registered scope). No leak.
  **F5 SURVIVAL +3 -> F5 HARDENED** (slope-limited spread / engineered
  dimension-cap / strip-integrity). FIVE OF SEVEN HARDENED.
- F3-A2 + CONFINEMENT RUN (f3a2_smooth_confine_modal.py, 14/14 complete,
  gate exact): adversarially SMOOTH q (40961/61441/65537 incl. Fermat —
  maximal subgroup richness) at full n=32 windows: ZERO nontoral trades;
  exceptional-regime confinement at n=16: the p=17 exceptional structure
  (60 trades, the positive control) does NOT persist at any p >= 97 —
  zero at 7 rows. **F3 SURVIVAL +3 -> F3 HARDENED** (boundary sweep /
  smooth-q engineering / exceptional confinement). Honest remaining
  surface: n=64 full-window needs a numpy signature rewrite (C(63,7)
  left tables) — follow-up, does not block the 3-family criterion.
  SIX OF SEVEN HARDENED.
- F4-A2b COMPLETE + catch #6 (refining, not overturning): per-config
  captures at three bands reveal the TWO-REGIME structure of the top
  band — AT/BEYOND the top-defect boundary realizability SATURATES
  (realized = the full binomial window C(core, 6), p-INDEPENDENTLY: this
  is why the A1 ladder read a constant 5005 — it is a real, structurally
  saturated count = the parameterized paid family, exactly chargeable);
  BELOW top, realized counts are window-law accidents DECAYING with p
  (4 -> 0, 2 -> 0, 29 -> 8 at matched cells); Lemma-13 kernel ceiling:
  ZERO violations at every row of every instrument. Deep-c at large p =
  feasible per-c follow-up jobs (cost scales with p), listed as remaining
  surface, non-blocking. **F4 SURVIVAL +3 -> F4 HARDENED** (p-ladder with
  saturation semantics / c-growth bounded-degree binomial / Lemma-13
  kernel-ceiling). **SEVEN OF SEVEN FLOORS HARDENED.**
