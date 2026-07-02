# Execution queue — hand-off items derived from the prize DAG

- **Status:** AUDIT / work queue. Derived mechanically from
  `experimental/data/prize-dag/prize_dag.json` (149 nodes @ this writing):
  the RIPE list (requirements met), the PROVABLE tier (routes pinned), the
  ready TEST nodes, and the named hard targets. Regenerate the source lists
  with `verify_prize_dag.py` as statuses flip.
- **Who this is for:** any agent/lane picking up tractable work. Each item
  is self-contained: what to do, inputs, acceptance test, size
  (S = a session, M = a few sessions, L = open-ended), and which DAG node
  flips on completion.
- **Claiming protocol:** one item (or one listed bundle) per PR (standing
  order 6); verify-first (the acceptance test must pass before commit);
  agents-log entry; CITE THE DAG NODE ID in the PR body so the map gets
  updated on integration. Honest labels; nothing here authorizes promoting
  SKETCH/CONJECTURE content.

## Tier 0 — lookups and gates (minutes to hours each)

```text
Q0.1 [field_cap_check] (S)  Read ePrint 2026/680; confirm or refute the
     working constants k <= 2^40 and |F| < 2^256 (absent from the live
     prize page). Acceptance: quotes + section refs recorded in the
     wp0_2-format freeze table. Flips: field_cap_check; unblocks exact
     B* statements in every dossier table.
Q0.2 [rules_freeze] (S)  Build prize_rules_freeze.md + the SHA-256 drift
     detector per wp_detail/wp0_2 §2. Acceptance: verifier green; all
     quote hashes pinned. Flips: rules_freeze; hardens S0 axes 8/9.
Q0.3 [replay_170_171] (M)  Execute the wp0_3 six-step replay protocol on
     PRs #170/#171 (pin SHAs; independent re-derivation of Phi and the
     rank-6 example — diff against the s3b_iii_2 factorization).
     Acceptance: divergence tables published. Flips: replay_170_171;
     UNBLOCKS alpha_front and beta_front scans; upgrades #173-adjacent
     statuses when its turn comes.
```

## Tier 1 — RIPE builds (all prerequisites proved; engineering + write-up)

```text
Q1.1 [bridge_ledger] (S)  Write experimental/notes/audits/bridge_ledger.md
     per wp5_2_wp6_2_wp6_3 §3 (rows already enumerated there) + the
     keyword checker. Acceptance: checker fails a doc using an unlisted
     bridge; passes current notes. Flips: bridge_ledger.
Q1.2 [paid_tan_fn + paid_quot_fn + paid_ext_fn -> paid_closure] (M, one
     bundle)  Implement Paid(A) per s2 §5: staircase formula; quotient
     zones with INTERVAL cells (point values stay conditional — print
     them as intervals, never numbers); the s6 extension import rule
     (0 if generating). Acceptance: deterministic regeneration; WP-0.4
     checker H2/H5 logic green on the emitted table for the pinned row
     (regression: tangent term reproduces 506/507). Flips: 4 nodes; the
     M4 table generator (wp2_4) becomes a formatting exercise.
Q1.3 [window_m5_charts] (M)  Per-point cleanup of the M3 window using the
     integrated lemma kit (m1_packet_transport, m1_rank_defect_nf): at
     each rank-drop Z of each bucket, decide kernel-contains-valid-
     locator; emit the per-A bucket log (wp2_5 §1). Acceptance: zero
     'unknown' leaves 385 <= A <= 426 OR named residuals with minimal
     reproductions. Flips: window_m5_charts; tests window_pred_aper0.
Q1.4 [dossier_partial] (M; do LAST in this tier)  Assemble v-PARTIAL per
     wp7_2_wp7_3_wp7_4 §3 from wp1_1's note spec + Q1.1/Q1.2 outputs +
     lean_tier1 (Q2.6). Acceptance: build script refuses if any gate
     fails; S0 conditioning language per wp1_1 §4. Flips: dossier_partial
     — the program's first submission-shaped artifact.
```

## Tier 2 — PROVABLE write-ups (routes pinned in the notes; execute them)

One-page lemma notes (S each):

```text
Q2.1 [fm1]  Write the exact-first-moment lemma (surjectivity + linearity;
     route in s2 §2) + commit the toy verifier (numbers already exactly
     verified: 0.017333 = 0.017333). Flips fm1 -> PROVED.
Q2.2 [gap2_seam]  The pullback => M | t_denom derivation (s4 §3) as a
     lemma note. Flips gap2_seam.
Q2.3 [spi_genericity]  Post-strip stratum carries no subgroup symmetry
     (from the PROVED strata combinatorics, s3b_ii §4). Flips
     spi_genericity.
Q2.4 [ext_import]  The N(L) crossing arithmetic + B-rational linearity
     argument (s6 §1-2) as a note + verifier. Flips ext_import.
```

Verifier-backed builds (S-M each):

```text
Q2.5 [displacement_uniform]  The three-field verifier ((F_13, mu_4),
     (F_17, mu_16), (F_49, mu_16)) deriving the #170 identities FROM the
     V^T D V factorization, with printed nonvanishing hypotheses
     (wp2_5_wp4_1 §2). Independent of mega-PR integration. Flips
     displacement_uniform; strengthens xr_wall's foundations.
Q2.6 [lean_tier1]  The gate addition certificates (witnesses computed and
     verified in wp1_1_wp1_2 §2), staircase arithmetic, endpoint Rat
     facts; lake build green, zero sorry, CERTIFICATION_MAP.md. Flips
     lean_tier1.
```

The deficiency-1 ladder (M as a bundle; = RESUME PR #172, task #13's
parked resume point; each rung is one loop turn per wp2_6):

```text
Q2.7 [u1_cramer, u2_nondegeneracy, u3_divisibility, u4_pseudoremainder,
      u5_dichotomy, acid_test, spi_dim1]  Execute rungs U1-U5 on the toy
     row, run the EXHAUSTIVE acid test (1820 supports x 97 slopes brute
     force == chart prediction), then the declared F_17^32 family packet.
     Acceptance per rung in wp2_6. Flips 7 nodes and tests prediction P3
     — the base case of the SPI mechanism.
```

Medium mathematics (M each; more thought, still route-pinned):

```text
Q2.8 [averaged_xr]  The Johnson-scheme second-moment computation (s3b_iii_2
     §5): variance of |A_{u,v}| over pairs, graded by intersection size,
     using the exact gap lam0 - lam1 = n. Acceptance: a toy-verified
     moment formula + the averaged-XR statement. Flips averaged_xr;
     upgrades the FM model to almost-all-pairs.
Q2.9 [petal_fixed_excess]  Enumerate/bound full-petal extras at fixed
     d-ell <= 3 on toy rows (CRT compression, L1 Lemmas 7/8, makes this
     finite). Acceptance: exact counts + a growth table vs d-ell.
     Flips petal_fixed_excess; first data on the petal escape route.
```

## Tier 3 — experiments ready to run

```text
Q3.1 [row_c_experiment] (M)  Build the Row-C birthday-sampling harness
     (wp3_1 §1: n = 2^10, log2 q ~ 250; e_1 value-set density at
     N' = 64..256; ~sqrt(V) samples; pinned seeds; confidence intervals).
     THE highest-information experiment on the board: it measures the
     zone-(b)/e1_fullness question that decides the corridor.
Q3.2 [alpha_front / beta_front] (M; blocked on Q0.3)  The full-grid alpha
     scan and the rank-6 Hankel-realizability search, on REPLAYED
     definitions, with P1a/b/c and P-beta outcome classification (s3a).
```

## Tier 4 — named hard targets (for strong sessions; standing order 8 applies)

```text
Q4.1 [exchange_ledger_gen_t]   generalize the #152 one-exchange residual
                               ledger past t = 2 (feeds xr_expansion;
                               small-t version targets the stripped A=265)
Q4.2 [acl_second_order]        explicit second-order term for Acl (makes
                               the S2 bracket's quotient end a number)
Q4.3 [norm_threshold_ext]      extend qfloor exactness past N' ~ 80
                               (each step narrows zone-(b) from the left)
Q4.4 [a_regularity_forcing]    force a-regularity or bound the irregular
                               stratum (REQUIRED for m >= 4 for-all lists)
Q4.5 [petal_mixed_amplification] the mixed-petal theorem (with Q2.9's
                               data as the guide)
Q4.6 [beta2_primitivity_trace] compute ONE integer, Tr(gamma|V) at z = -2,
                               by any route not yet foreclosed (the
                               elementary Lefschetz route is proven dead —
                               do not re-walk it; see beta2_dead_routes)
Q4.7 [xr_crystallization = spi_exceptional_class]  the shared core:
                               dense alignment => paid structure. The one
                               genuinely new idea the program needs;
                               odd-moment inputs (Q4.1, Hooley-Katz) are
                               the cheapest rigid information.
```

## Addendum — items from DAG depth passes 5-6 (2026-07-02)

```text
Q2.10 [stratification_partition_thm] (S)  Write the T0-T7 partition theorem
      (totality + first-match disjointness; true by construction) + the
      fuzz acceptance from wp2_3 §4. Load-bearing: the final theorem sums
      over these strata. Flips stratification_partition_thm; makes
      strat_tree's ripeness formal.
Q2.11 [dyadic_profile_evaluation] (S-M)  Compute Q_H(eta) exactly for
      2-power domains at the four official rates (pure divisor counting;
      verifier + note). Without it conj:B's profile hypothesis is
      unverifiable on official rows. Flips dyadic_profile_evaluation.
Q2.12 [averaged_slope_conversion] (M)  Second moment + paid-fiber
      exclusion => a many-SLOPE pair exists whenever the FM locator mean
      crosses B* (route: s2 fork F2). This is the unsafe side's needed
      tool in the COLLIDED branch of zone-(b). Flips
      averaged_slope_conversion; with e1_fullness it makes
      unsafe_at_crossing's any-gate exhaustive.
Q4.8  [amplification_range_ext] (L)  Extend the split-prime transfer
      (finite collisions = char-0 collisions) from p > exp(Cn log n/sigma)
      toward prize-scale p ~ 2^256. The proved foundation (thm:upstairs +
      Galois amplification) is fully in place — RIPE in the well-posed
      sense. Every range improvement is direct corridor progress.
NOTE  Q1.1 (bridge ledger) gains a MANDATORY row: the proved LD_sw vs
      ABF/GG separation (forward-only import; see ldsw_ld_separation).
```

## Sequencing notes

STRATEGIC OVERLAY: see `strategic_recommendations.md` (computed from the
DAG) before claiming Tier-4 items — several are ROUTE-INTERNAL (pay their
tolls only if that route is chosen) and two are SUPPORT-ONLY (Graver,
Hooley-Katz-as-target). The four walls are alternatives: pick one.

Q0.x first (they gate honesty everywhere); Q1.2 before Q1.4; Q2.7 is one
resumable loop; Q3.1 is independent of everything and maximally
informative; Tier 4 items are deliberately unscheduled — they are the
targets the tractable tiers exist to feed.
