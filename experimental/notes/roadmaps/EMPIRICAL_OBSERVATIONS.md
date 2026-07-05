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
