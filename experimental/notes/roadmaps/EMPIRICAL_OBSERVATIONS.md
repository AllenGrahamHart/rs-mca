# Empirical observations log (evidence-first: probe -> confidence -> prove)

Rule: keep Modal/local runs < 60s; stress-test each RED node AND the AMBER it flows
into; record every observation so the eventual conjecture is consistent with ALL data.
Only dispatch a Pro proof (10-25 min) once empirically confident. Confidence: LOW /
MEDIUM / HIGH / REFUTED.

## dli_prime_weighted_large_block_support  (deepest leaf)  — confidence: HIGH
Conjecture: the odd-eval residue partition puts o(L_j) mass on small (non-cancelling) blocks.
Observations (local, seconds):
- max_lambda |mu_hat_S| ~ 2.5/sqrt(|S|) for the odd-eval phase psi(lambda*P(sigma(y))).
  ROBUST across random AND structured (consecutive-index) subsets — no adversarial block
  cancels worse (section is mult-structured => additively spread). [P=x,x^3,x^5; n=16..256]
- Non-cancelling blocks are ONLY small ones: |S| <= ~C^2 ~ 9 (below the sqrt threshold).
- Near-peak FREQUENCY count VANISHES with scale: n=32 ~212 freqs |mu|>0.3; n=128: 0;
  n=256+: none |mu|>0.2. So near-peak mass DECREASES with scale (repo's "~129" is a
  small-scale artifact). max|mu| ~ 2.5/sqrt(n) throughout.
Not yet tested: the EXACT D-thread degree-preimage block partition (needs its definition);
the multi-level (per-L_j) weighting. Upstream amber (ejm->pcf->b2b): budget arithmetic
verified earlier (34 levels, sum L_j=t, o(t) closes at 2^122). 

## sov_gridsum_residual  — confidence: MEDIUM-HIGH
Conjecture: after paid trace-flat + quotient/dihedral + large_power_sum(Bohr) classes,
residual cells cancel (Lane-1). Equivalent test: small value-set => large power sum.
Observations (local + C, thousands of cells, 8 cell types incl arcs/APs/geometric/
cosets/sumsets/Bohr/random):
- CLEAN dichotomy: every small-value-set cell has max additive power-sum ratio >= 0.90;
  ZERO unexplained (small value-set + small power sums). Supports the decomposition.
- BUG caught in 2s: an incomplete-frequency check false-flagged APs (Bohr at freq d^-1) —
  fixed by sweeping all frequencies. (This was the wrong-conjecture failure mode in miniature.)
Not yet tested at scale on Modal (local signal already strong). Upstream amber
(single_obstruction_valueset via sov_hminus1_fiber_fourier_duality) not yet stress-tested.

## petal (Gate D / petal_quotient_descent_step)  — confidence: LOW (needs redesign)
Conjecture: power-sum window m >= theta*2^r => coset-union at scale r; theta=5.
Observations (L1 dyadic toy F_17[z]/(z^32-3), |H|=512):
- Coset-unions at scale r have window exactly 2^{r+1}-1 = 2*2^r - 1, well BELOW theta*2^r=5*2^r
  => theta=5 is conservative (~2.5x margin above a bare scale-r coset-union).
- Random supports essentially NEVER have a power-sum window (p_1=0 is codim-32) => windows
  are rare/structured, consistent with Gate N.
Flaw in first design: tested the wrong direction; need to CONSTRUCT long-window non-coset
supports to measure the tight theta. Redesign pending.

## m720_conductor_compression (the gate: no primitive non-toral survivor) — confidence: MEDIUM (test vacuous)
Observations (local, exhaustive small n): random anchored 2h-supports over char-0 (aux prime
P0=1e9) have ZERO char-0 survivors (all obstructions O_j!=0) at n=8,16 / h=3,4. So the gate
holds GENERICALLY (random supports never survive). BUT the test is VACUOUS for the real
question: it found no survivors at all, so cannot classify the STRUCTURED (X79 square-shift)
survivors as toral vs primitive. Need the exact square-shift survivor family to stress-test
the X24 char-0-toral classification. My O_j setup (S_R^2-C_R, top-h match) may not capture the
actual survivor condition. Prior modal_m720 census: 0 survivors where complete (consistent).
CAVEAT to record: no strong empirical handle on the PRIMITIVE-survivor exclusion yet.

## sov upstream amber single_obstruction_valueset (grid-sum => small fibers) — confidence: MEDIUM-HIGH
Observation: in the sov_adv census, NON-structured (random) cells have value-set fraction
vf ~ 1.0 (O takes ~all field values => small fibers), while only the additively-structured
(Bohr) cells have small vf. So after removing the Bohr/large_power_sum class, residual cells
DO have (1-o(1))q value-set. Supports the amber (single_obstruction_valueset) for residual
cells. Not yet tested: the exact Fourier-duality constant / anchored-cell version.

## corridor_ledger / adjacency_closing (clean-rate corridors) — confidence: MEDIUM-HIGH (computed)
STRESS-TEST of the amber (and correction of my own stale strategic claim):
- fourth_mechanism_rate8 is legitimately PROVED (gate:any on cap_end_sharpening, PROVED):
  the quotient-remainder floor at c=2^28 delivers 0.0625 grid steps = 8.8x the 0.00707 wedge.
  Its statement.md said "TARGET" — STALE; dag.json PROVED is justified. (Fixed the .md.)
- Acl anchors VERIFIED exactly: Acl_tot=(3^{N'/2}+1)/2, log2 = 49.72/100.44/201.88 for
  N'=64/128/256 (rho=1/2 antipodal class count). Arithmetic sound.
- Rate-1/8 eater ledger delivers +0.0164 (acl) +0.099 (window) +0 (ext guard) +0.0625 (cap_end)
  = 0.178 grid steps; corridor row CLOSES at the computed level.
=> CORRECTION: the "rate-1/8 ~0.9-bit wedge" I proposed as the top target is ALREADY CLOSED.
   The clean-rate (1/4,1/8,1/16) corridors close (corridor_ledger PROVED, computed/verifier level).
   The ONLY remaining adjacency blocker is rate_half (rate 1/2, bracket-grade).
CAVEAT: the eaters are "COMPUTED (agent verifier PASS)" — arithmetically verified here, but the
rigorous-proof vs high-confidence-computation status is the general fidelity question, not re-audited.
Strategic update: remaining prize gaps = (a) the 8 mca_safe leaves, (b) rate_half adjacency (rate 1/2).

## dli REAL-OBJECT CORRECTION (supersedes the proxy evidence above) — confidence: MEDIUM (was HIGH)
- Block partition PINNED: B_j(M)=q^{-L_j} sum_lambda prod_y mu_hat_y(lambda), mu_hat_y(lambda)=sum_d psi(d lambda v_y),
  v_y=zeta_n^{(2s+1)i}. CONFIRMED by verify_level2_tower.py (TEST 1 = exact mu_32 census match).
- My earlier max|mu_hat|~2.5/sqrt(n) was the WHOLE-SECTION average = a PROXY, NOT prod_y mu_hat_y. Superseded.
- Real excess rho=skewcount*q/2^|G| SCALES WITH q; eta_j=log_q rho_j. VANDERMONDE: nonzero skew needs support
  >= L_j+1, so meaningful regime is LARGE support (my |G|=3-6 test = below-threshold toy artifacts).
- Calibration eta*/L=3.6e-7 => eta_j=3.6e-7 L_j (linear, tiny coeff): Sum_j eta_j=3.6e-7 t=o(t) via the SMALL
  COEFFICIENT, not bounded excess. This is the correct hypothesis shape.
- NEXT TEST: reproduce eta_j = log_q(B_j/balanced_mean) at the actual calibration params (need the U_j/balanced
  normalization + the level structure), confirm eta_j/L_j ~ 3.6e-7 and characterize which profiles are the sup.
- Task (b) chain-tangle: dli subtree ~15 nodes, two Deligne branches converge on ejm; reduced_phase_manifest
  statement stale (Deligne route) but is one node in the tangle; full reconciliation pending a careful trace.

## dli REAL-OBJECT CONFIRMATION (resolves the correction above) — confidence: HIGH (on the true object)
Using the Fourier form (rho_j = sum_{lam in F_p^L} prod_y (1/|D|) sum_u psi(a_y u)) — the REAL object, reaching
large N without 3^N enumeration:
- eta* = log_q rho_j is FLAT: rho_j -> 1.0000 (eta* -> 0) as N grows, BOTH ternary and signed. [n=32..256, N up to 128]
- CALIBRATION REPRODUCED: signed midpoint eta*=0.019 at mu_32,N=16 (EXACT match to dli_dirichlet_log_integral
  record); decreasing with N. ternary flat ~0. This is the node's own calibration, replayed on the real object.
=> Sum_j eta_j = o(t) holds; the leaf is CORRECT as stated. The earlier proxy reached the right conclusion by the
   wrong route; the real-object test confirms it properly. dli is now empirically PROMOTION-READY (HIGH).
Small-N artifacts noted: at large-p/small-N, B collapses to the trivial vector (expected count <<1) giving
spurious large rho -- NOT the meaningful regime. The Fourier form at large N is the correct test.

## dli CHAIN RECONCILIATION (task b) — OUTCOME: chain is SOUND (spot-check + endpoint)
Full upward trace: the leaf reaches ejm through ONE connected chain (~17 nodes); the two
"branches" (polar_obstruction / pole_majorant) RECONVERGE at odd_phase_reduced_pole_budget.
Spot-check of the 3 critical joints:
- reduced_phase_manifest: reqs = {phase_pole_conductor_manifest [PROVED], harmonic_conductor_ledger
  [weakened]}. CONSISTENT = proved Deligne pole + weakened harmonic total. NOT stale (my earlier read
  was wrong: the pole parts are PROVED, only the harmonic-sum part is the weakened open route).
- odd_phase_reduced_pole_budget: needs "not AS-trivial" + "polar divisor harmonic total o(t)" -- the
  SAME o(t) threading back to harmonic_conductor_ledger -> bohr -> block_conductor -> leaf.
- dli_dirichlet_log_integral: the geometric-mean DLI, fed by the chain.
ENDPOINT CHECK: my calibration measured rho_j = sum_lambda F_M(lambda) DIRECTLY = the pcf/b2b endpoint;
it is flat. So the leaf's flatness gives the ejm/pcf input at the endpoint regardless of the Deligne
detour. Wired path and direct measurement AGREE.
=> A proved leaf propagates cleanly to ejm. No rewiring/hacking needed.
CAVEAT: spot-check of 3 joints + endpoint, NOT a full 17-node per-implication audit. The one residual
item worth a Pro glance: confirm the T3 "near-peak mass / harmonic total o(t)" output EXACTLY matches
the Deligne route's "reduced polar divisor harmonic total o(t)" input (same quantity, different language).

## dli PRO CONDITIONAL CLOSURE (DLI-FLATNESS) — exact reduction PROVED, leaf = RES count
- Lemma 1 (PROVED, orthogonality, VERIFIED): rho_j(M) = q^{L_j} |Z_j(M)| / U_j, Z_j = kernel skews
  {d in prod D_y : A d = 0}. |Z_j|=81(ternary)/16(signed) match the harness B exactly. So dli-flatness
  is EXACTLY a kernel-skew count.
- Remaining leaf (RES): |R_j(M)| + 1_{0} <= q^{kappa_j} U_j/q^{L_j}, sum kappa_j=o(t); R_j (proved to
  contain Z_j\{0}) = large-support(>=L_j+1) + norm-gated + not killed-cyclotomic. A sharp COUNTING stmt.
- ZERO-ATOM (verified): unconditional-A FALSE if singleton-zero domains allowed (rho_j=q^{L_j}). Fix =
  RANK CHARGING (zero atoms cost L_j - rank; central measure must exclude/charge them).
- FIXED-LAMBDA refuted (|F_M|<=1): obstruction is aggregate kernel-skew mass, not any single lambda.
- Empirical eta* flat (rho_j->1) = RES with kappa_j ~ 0 already supported. Remaining = the rigorous
  RES/resultant-sieve count. dli confidence HIGH; exact reduction now PROVEN.

## dli MAJOR CORRECTION (supersedes the HIGH-confidence + "phrasing artifact" entries above)
Pro's SHARPER counterexample (verified): a low-mass profile with L active ternary coords + rest zero
has U_j=3^L, |Z_j|=1 (Vandermonde), so rho_j=(q/3)^L => log_q rho_j ~ 0.994 L_j = Omega(L_j). This is
FORCED BY MASS (log_q U_j=0.006 L_j << L_j), independent of resultants. NOT the trivial {0} case; the
active-coord/full-rank scoping does NOT exclude it. So:
- The SUP obligation (my brief) is FALSE. It was only a SUFFICIENT condition for the b2b U-WEIGHTED
  AVERAGE of prod_j rho_j = q^{o(t)}; sup false => that route is DEAD.
- The real obligation = the weighted average directly (low-mass profiles U-suppressed by q^{1.58L} but
  number C(256L,L); whether suppression beats count is the OPEN primitive-core content).
- My eta*-flat calibration ONLY tested the FULL-MASS profile => HIGH confidence was OVERSTATED.
- Lemma 1 (exact reduction rho_j=q^{L_j}|Z_j|/U_j) still holds.
LESSON: the calibration was necessary but not sufficient -- it covered one profile family, not the sup/
weighted-average over ALL profiles. Adversarial Pro pressure caught the overclaim. This is the
"leaf-is-incorrect -> reassess" scenario. REASSESSMENT NEEDED: does pcf/ejm/b2b use the per-profile
sup (broken) or the weighted average (correct)? The chain must be re-checked against the weighted-average form.

## sov WORST-CASE CENSUS (dli-lesson-corrected) — MECHANISM SURVIVES (opposite of dli)
Modal thorough run (1064 cells, primes to 32003, 9 families incl. DEGENERATE small-support + subgroup-confined):
- value-set measured RELATIVE TO ACHIEVABLE MASS min(C(m,h),p) -- the dli-lesson fix (distinguishes genuine
  COLLISIONS from mass-deficiency). 950 mass-sufficient cells.
- 521 collision-heavy cells (vf<0.6 rel. mass); of those 521/521 = 100% Bohr-caught (maxpow>=0.15). ZERO
  counterexamples (no small-value-set cell evades the Bohr paid class), including the degenerate families that
  are the analog of the low-mass profile that KILLED dli.
=> sov's CORE MECHANISM (genuine collision => Bohr-detectable => paid) survives a worst-case adversarial census.
   Strong positive evidence, the OPPOSITE of the dli outcome.
CAVEATS (dli lesson: don't over-generalize the census): (1) tests the collision=>Bohr MECHANISM, not the FULL
obligation (quotient/dihedral exhaustion + the Lane-1 power-sum residual bound + the exact anchored-core
quantifier); (2) moderate primes (structural claim, scale-invariant, but not prize-scale); (3) maxpow has a
small-sample bias at tiny m (handled: REAL_CE category is mass-sufficient where maxpow is reliable).
CONFIDENCE: mechanism HIGH; full sov leaf MEDIUM-HIGH (untested parts remain).

## sov LANE-1 RESIDUAL probe (quantitative, dli-lesson-applied) — Lane-1 ROBUST; pricing crux identified
Quantitative (B=maxpow, value-set deficit) census + a gap probe (diluted-Bohr cells, Bohr fraction 0..1):
- 0 Lane-1 violations across 328 mass-sufficient cells. Fourier-uniform cells have deficit~0 (FULL value-set).
- Sharp transition: deficit~0 up to B~0.93; only PURE Bohr/interval (B->1) collapses (deficit 0.99). A 10%
  random admixture already rescues the value-set. So the Bohr class that TRULY collapses is very narrow.
- KEY SUBTLETY for the pricing obligation: a cell can have high char-sum B AND full value-set (random part
  rescues). The Bohr GATE (B>threshold) thus OVER-includes cells Lane-1 would close. Threshold placement:
  low => Bohr class large/expensive to price; near B=1 => narrow/cheap, BUT only if the Euler-product bound
  is TIGHT enough to close cells up to B~1. Empirically deficit=0 up to B~0.93.
  => THE CRUX of the pricing obligation = tightness of the Lane-1 Euler-product bound near B=1 (the gap between
     "Lane-1 proves closure" and "Bohr gate must price"). This is the sharp question for a Pro round / proof.
- CONFIDENCE: Lane-1 Euler-product theorem empirically ROBUST (stress-tested, survives). The open pricing
  obligation is well-characterized (narrow Bohr class) but its difficulty hinges on the bound's tightness.
  Moderate primes (structural). Overall sov: mechanism HIGH, Lane-1 HIGH, pricing obligation OPEN-but-narrowed.

## CODEX FALSIFICATION PASS (prize-rednode-falsification-20260705) — assessed + replayed 2026-07-05
Codex attacked all 8 leaves (numeric + algebraic, Modal <60s each). NONE deleted; all survive as TARGET.
CROSS-VALIDATION of my work: sov (0 falsifiers, remaining=Bohr pricing -- matches me exactly); dli (zero-atom/
rank falsifier reproduced; large-support scans FLATTEN -> positive for the weighted-average obligation).
CLEAN SURVIVORS (4): sov (Bohr pricing), rate_half (new mechanism, 2.98M gap, 0.1 vs 91.85 bits guardrail),
  e22 (source construction), m720 (survivor descent / D-GCD; shortcut 'h>=7 enough' killed).
PETAL CLUSTER = THE WEAK LINK (3 gates need repair):
  - Gate D (petal_quotient_descent_step): naive strategy FALSIFIED (verified witness M=36,p=37); scope/window/paid.
  - Gate L (petal_low_defect_quotient_charge): CITATION GAP (charging without a paid citation; sheets grow); SOUNDNESS.
  - Gate N (petal_newton_window): SCOPE GAP (no definition/verifier; naive shortcut refuted).
The petal gates feed BOTH list_grand AND (via the pole/list bridge) mca_safe -> the fragility touches both
grand challenges. Gate L's citation gap is the most concerning (a charged-but-uncited class = latent soundness hole).

## Gate L CITATION-GAP TRACE (petal_low_defect_quotient_charge) — bridgeable, SHARED ROOT with Gates N & D
- Gate L asserts low-defect quotient sheets are PAID; consumer PRK_pet peels them assuming paid; NO node justifies it.
- VERIFIED: the sheets = EXACTLY C(M,delta) (choices of the delta removed points B): 560=C(16,3), 4960=C(32,3),
  41664=C(64,3), 341376=C(128,3). So poly(n)-MANY structured quotient-coordinate families (fixed defect delta<=theta-1)
  -- exactly the TYPE petal_fixed_excess (poly count at fixed excess) handles. NOT unbounded.
- The gap = no node PROVES the C(M,delta) sheets are a paid class. TWO missing links:
  (a) defect delta <-> excess e=d-ell (reparametrization to fixed_excess);
  (b) quotient-coordinate <-> ambient full-petal coordinate.
- LINK (b) IS THE SAME primitive-coordinate bridge Gate N needs (naive K-membership shortcut refuted) and Gate D
  needs (D proof must visibly use the residue-kernel/primitive coordinate). => THE PETAL CLUSTER HAS A COMMON ROOT:
  one primitive/quotient-coordinate bridge would feed Gates L, N, D simultaneously. Highest-leverage petal move.
- Gate L is therefore NOT a dead soundness hole: it's bridgeable (poly(n) sheets), pending the shared coordinate bridge.

## Gate D STABILITY STRESS (petal_quotient_descent_step) — NOT yet stable; scoping is load-bearing + untested
C/Modal exhaustive MITM (M<=44): bare-mechanism counterexample window L*(M) [max window with a non-coarser,
non-antipodal, first-L-power-sums-zero subset]:
  M= 28 32 36 40 42 44  ->  L*= 4  4  5  6  6  5   (arithmetic-dependent; prime p matters strongly).
- L* EXCEEDS the toy theta=5 at M=40,42 (bare counterexamples at window 6). So NO small fixed window threshold
  makes the bare mechanism safe. (My first read of "unbounded ~M/logM" was an over-interpretation of 4 points;
  the Modal sweep shows fluctuation in 4-6, not clean growth -- corrected.)
- => Gate D's stability RESTS ENTIRELY on the squarefree-realizable scoping doing real work, which is UNVERIFIED
  and shares the primitive-coordinate definition gap with Gate N.
CONCLUSION (answers the "are red nodes stable before decomposing?" question for Gate D): NO, not yet. Do not
introduce a foundation node beneath the petal cluster until the squarefree-realizable scoping is pinned + tested.
The stress test did its job: it caught that Gate D's stability is contingent on an untested hypothesis.

## Gate D SCOPING VERIFIED (squarefree-realizable pinned + tested) — realizability caps the window
Pinned: squarefree-realizable = a split-squarefree kernel point of K_{I,d}=ker(pi_{>d} R_{I,d}) (executable).
Modal test + scaling:
- initial (t,ell<=4, d<=~11, q<=53): 2.05M candidates, 19211 realizable, max naive window = 3.
- scaled (t,ell<=6, d<=~20, q<=101): 1.36M candidates, 4276 realizable, max naive window = 2.
=> realizability FUNDAMENTALLY caps the naive-coordinate moment window at ~2-3 (does NOT grow with size). ZERO
   realizable points reach window>=5, vs arbitrary subsets where L*=5,6 exist. The bare Gate-D counterexamples
   are NOT realizable. The squarefree-realizable scoping is VERIFIED to do real work.
- So the workflow: bare mechanism UNSTABLE (L* stress) -> scoping VERIFIED to cap the window -> Gate D substantially
  more stable. This is the scoping earning its place, not assumed.
CAVEAT / REMAINING: naive root-coordinate window; Gate D's actual object is the QUOTIENT-coordinate window
Sum_x x^{Qt} (part 2, the primitive-coordinate definition). Confirm the cap holds there too before full confidence.

## PRIMITIVE COORDINATE — confirmed load-bearing + candidate definition (Gate N's core gap)
Modal test over realizable kernel points (K_{I,d} split-squarefree):
- naive (Q=1) moment window: capped at 2-3 (from prior test).
- MAX quotient-coordinate window (over x->x^Q): reaches 5. Witness: F_37, roots {4,5,10,12,17,29}, Q=6, window=5.
=> The primitive coordinate is REAL and load-bearing: the window small in the naive coordinate becomes large in a
   quotient coordinate. CANDIDATE DEFINITION: primitive coord = argmax_Q window(sum_x x^{Qt}). Window 5 > excess 1
   (consistent with Gate N ≥ c-kappa_N). This resolves the naive-vs-primitive contradiction Codex flagged.
- STATUS of the petal-cluster bottleneck: the coordinate is no longer a total unknown -- a concrete, testable
  candidate exists. REMAINING (Pro DEFINITION task): tie it to the petal/locator structure (vs generic x^Q) +
  verify the window grows with excess c across realizable families. This is a definition/proof task, not numerical.
STRESS-BEFORE-DECOMPOSE verdict: the shared coordinate is now empirically grounded (not vacuous, not undefined-in-
principle). Once the definition is tied to the petal structure + c-scaling verified, the petal cluster can be
decomposed on solid ground. Until then, do not add the foundation node.

## GATE N EXTRACTION REFUTED (Pro PETAL-PRIMITIVE-COORDINATE, verified) — petal descent broken
Pro answered Part A (canonical coordinate = petal quotient X->X^M + mu_M-character projectors Pi_{M,r}) but
REFUTED Part B (the extraction). Explicit counterexample (VERIFIED, M=3,t=6,q=127):
  F = X^{M-1}P(X^M)+Q(X^M), P=Y^{t-2}+omega_{t-1}Y^{t-3}, Q=const -- a TWO-CHARACTER family.
  * F in K_{I,d}: deg CRT(c_i F mod L_i)=14 <= d=14, G≡c_i F mod L_i for all petals. YES (realizable).
  * squarefree: gcd(F,F')=const. YES.
  * excess c=(t-2)M-1=11 (grows with t).  quotient moment window = 0 (s_M=90=-M*omega_{t-1}!=0).
=> Gate N's pointwise 'window>=c-kappa_N' is FALSE. The N->D->L descent (which needs N's window) is BROKEN.
ROOT CAUSE: quotient compatibility => isotypic mu_M-character decomposition, but does NOT select one character.
The unbounded-excess obstruction lives in MULTI-CHARACTER kernel directions. Same obstruction as
q_cofactor_normal_form (character selection = source data, not a divisibility consequence).
CORRECT REPLACEMENT (Pro): a FAMILY-LEVEL PRK-type statement -- multi-character squarefree-realizable residue
directions are paid separately OR bounded after peeling. NOT a pointwise Newton-window extraction.
IMPLICATION: the petal cluster needs RE-ARCHITECTING around the multi-character obstruction. The stress-first
discipline caught this BEFORE we built a foundation node on the false extraction -- exactly as intended.

## PRK TRUTH STRESS (petal_primitive_residue_kernel_rank) — the AMBER ITSELF is at risk
Question: is PRK's conclusion (dim Pi_prim <= B_pet ABSOLUTE after peeling) even TRUE? Never stress-tested until now.
Measurement (M=3, growing t): dim K_{I,d} ~ c+1 (grows with excess). The MULTI-CHARACTER residual (dim K minus
single largest character block) grows LINEARLY: c=5->4, c=17->12, c=29->20 (~2c/M). Single-character quotient
paid class covers only ~c/M. Pro's two-character counterexamples are squarefree-realizable and grow with c.
=> PRK requires the GROWING multi-character bulk to be PAID by a new mechanism (Pro's 'paid separately') or
   COLLAPSED by Pi_prim. NEITHER established. PRK is NOT confirmed true; its truth = the multi-character
   paid-or-bounded question (same as its proof).
CONSEQUENCE: we cannot separate 'is PRK true' from 'can we prove PRK'. If the multi-character bulk is unpayable,
PRK is FALSE -> the 24 downstream petal->list/mca conditionals need fundamental rethinking. This is now the
decisive petal-branch question. Do NOT invest in re-architecting PRK's proof until its TRUTH is resolved.
LESSON: the amber we were trying to flip had never itself been adversarially tested -- exactly the gap the
user flagged. The gates' refutation was the surface; the amber's truth is the real question.

## PRK FALSIFIED AS STATED (petal_primitive_residue_kernel_rank) — the amber is FALSE with the current paid menu
Attack (Modal, bug-fixed): generic multi-character kernel families (all mu_M-character blocks active, B_r in ker lambda):
- ESCAPE every existing paid class (mu_k quotient/coset, antipodal, cyclotomic; low-defect is single-char-based too)
  -- 25/25 across M=3,5,7, q=127..337, growing c. (First run's q-dependent catches were a z=1 bug in the mu_k
  primitive-root computation -- g could be a k-th power => z=1 => spurious pass. Fixed => uniform escape.)
- dimension GROWS ~ (M-1)c/M with excess c.
=> after peeling the current menu, an UNBOUNDED residual survives => dim Pi_prim <= B_pet (absolute) is FALSE.
   PRK is NOT true as stated.
FIXABILITY (encouraging): the multi-character families are STRUCTURED -- a bounded number (2^M-M-1, c-independent)
of product-of-kernel types. So PRK is likely FIXABLE by adding multi-character paid classes -- but that is a NEW
chargeability obligation (each must fit a ledger budget), which does not exist yet.
ANSWER to 'is the amber true / stress-tested?': NO -- and stress-testing FALSIFIED it as stated. The petal branch
needs an expanded paid menu + multi-character chargeability. The 24 downstream conditionals hinge on this repair.

## CONSUMER-PREMISE ATTACKS (the 5 ambers accepting the 5 reds) — 3 findings, 1 pruning
Per the falsification-pruning protocol, attacked the premises A of the consumer ambers directly:
1. petal_cofactor_chargeability: FALSIFIED AS STATED by the same multi-char families that killed PRK --
   escape paid menu (25/25) AND dim Pi_prim grows ~2c/M (measured 8..24 for c=11..35); tail ops O(1) can't
   rescue. => PRK PRUNED (salvage non-trivial, consumer falls to same object); frontier moved UP to
   chargeability (demoted to red, re-posed). Petal chain trimmed one level toward the prize.
2. dli_prime_block_conductor_mass (+bohr_flatness_prime): INTERFACE MISMATCH -- leaf re-posed to weighted
   average but consumers still sup/uniform-form; plus structural falsifier-candidate (minimal-support profile
   => all singleton blocks => exceptional mass ~L_j, not o(L_j)). Recommend re-posing the T3 intermediate
   chain to weighted form (the second-moment reduction likely needs only the average). No status flip (scope caveat).
3. m720_official_norm_gate_case_manifest_payload: COMPRESSION ROUTE EMPIRICALLY DEAD -- the h=7 (official
   band edge) survivor has FULL degree 32=phi(64), 291*32=9312 >> 250 (fails ~37x); all measured survivors
   full-degree. Live premise narrows to the C2/D-GCD certificate route (data acquisition).
Also: e22 consumer's premise (certificate CF) is exactly what Codex found unachievable (0/85 challengers) --
if Modal-confirmed, the manifest's coverage is vacuous for structured challengers; interface scope must say
which challengers need CF vs are routed elsewhere.

## dli CHAIN RE-POSE + COHERENCE AUDIT (sup -> weighted, full chain) — chain now coherent
- dli_prime_block_conductor_mass + dli_bohr_flatness_prime RE-POSED from sup_M to U-WEIGHTED form
  (E_U[C_j+X_j]=o(L_j); E_U[S_{j,lambda}]=o(L_j) + Markov + trivial eta_j<=L_j => E_U[q^{eta_j}]=q^{o(L_j)}).
  The proved pointwise T3 reduction (S<=C_j+X_j, Deligne + exceptional split) is unchanged, applied inside the average.
- SAFETY MARGIN VERIFIED: low-mass profiles (all-singleton blocks, X_j~L_j) falsify the sup but self-kill under
  the weight: weight fraction 2^{-501L_j} vs penalty q^{L_j}=2^{256L_j} => net 2^{-245L_j}. Independently matches
  Codex's alpha=256 envelope (-0.9639 ~ -245/256) and its exact weighted DPs (rho=1.000000 flat).
- AUDIT UP THE CHAIN: 9 more nodes had per-profile language. Pole/conductor nodes (polar_obstruction,
  pole_majorant, reduced_pole_budget, noncollapse, reduced_phase_manifest, harmonic ledger) are MASS-INSENSITIVE
  (pole orders/conductors don't depend on profile mass) -- left uniform. The 4 mass-SENSITIVE nodes
  (exponential_sum_bound, peak_mass_discrepancy, odd_evaluation_discrepancy, log_integral_equidistribution)
  CANNOT hold for low-mass profiles (inactive coords contribute 0 to the log-integral; the bound needs ~256L_j
  coords x 2log2) -- SCOPED to full-mass profiles; the low-mass tail is absorbed by the weighted ledger below.
=> The dli chain is now COHERENT end-to-end: leaf (weighted/RES) -> ledger (weighted) -> 2nd moment (weighted)
   -> full-mass-scoped Deligne branch -> ejm -> pcf -> b2b (weighted). The re-pose propagation debt from the
   leaf correction is PAID.
