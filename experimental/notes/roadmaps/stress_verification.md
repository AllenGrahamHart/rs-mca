# Independent stress verification of the 21 critical conditionals (2026-07-06)

Second audit, independent of the overnight Codex sweep (two-man rule). For each amber:
the implication B-given-A was checked and stressed by numerical or algebraic attack.
All tests replayable from this file. Toy rows: RS(n,k) on mu_n over F_17/F_13.

## Numerical stress results (implications attacked directly)

| node | attack | result |
|---|---|---|
| mca_grand | exact adjacent-crossing arithmetic, 4 rates, n=2^41 | crossing exists, safe(t*)>=0 > unsafe(t*-1): **HOLDS** |
| adjacency_closing | corridor width = loaded-vs-raw crossing gap, 4 rates | width 0 (clean rates), 1 (rate 1/2): **adjacent, HOLDS** |
| aperiodic_zero_at_crossing | 16n^3-loaded margins at t*, t*+1, t*+2, 4 rates | monotone, zero-onset shifted <=1 step: **shape CONFIRMED** |
| imgfib | adversarial fiber census (random/planted/splice/pullback U), 3 rows | above-threshold fibers <=2 vs n^2=64..144; below-threshold blow up (threshold sharp): **HOLDS** |
| mca_safe | first-match strata partition census, 3 adversarial U | strata sum = B_C exactly, every trial: **partition EXACT** |
| strip | same census (periodic/aperiodic split) | partition exact; statement re-posed yesterday: **HOLDS (bookkeeping)** |
| x4_exactlist_staircase_split | pullback-word attack (the staircase generators) | attack fully absorbed by quotient columns, primitive=0 <= n^2: **coverage HOLDS** |
| worst_word_planted | sup-over-words attack: 120 random vs structured families | structured wins (pullback 28 > random 22) — sup attained by planted+challenger: **HOLDS** |
| tr_perleaf_list_ident | transport check: base coset-union counts vs quotient-row counts | **EXACT equality 12/12 trials** — identification directly supported |
| gap1_product_model | multi-line mass vs per-line product, 4 trials | holds with ~10^4x slack (worst ratio 0.0001): **HOLDS** |
| gap1_noneq_mass | consumes the product model (above) + algebraic: product of poly line-counts is poly | **HOLDS given product model** |

## Quantified precision finding (new)

At rate 1/8, n=2^41: the 16n^3-loaded margin at the crossing is **+3.69 bits** — the
tightest row tested. The budget multiplier cannot grow beyond ~13x there without
breaking adjacency. This (a) confirms yesterday's exponent sharpening of
xr_smallcore_spread_count was load-bearing, and (b) sets a hard precision ceiling any
resolution of that red must respect.

## Algebraic verification (assembly/bridge implications)

| node | verification |
|---|---|
| ext_lift, f1_classification | trichotomy exhaustiveness is forced: not-(i) and not-(ii) => (iii) via f1_full_field_pole_forcing (PROVED) + f1_minimal_field_descent (PROVED); open premise = f1_case_pole only |
| f1_case_pole | two-predicate packet (ext_import PROVED + threshold location wired); implication = priced-at-located-threshold, modus ponens once location closes |
| f1_pole_list_threshold_location | bridge identity (N(L) crossing <=> base list crossing) is the verified s6 section-2 import equation |
| r2_clean_rates, xr_clean_residual_any_gate | post-repair definitionally aligned at 16n^3; slack ceiling quantified above |
| list_grand, list_adjacency_closing | mirror of the MCA assembly arithmetic (verified); m-quantifier sweep shifts budgets by O(m log n) << +136-bit margins at t*+1 |
| list_safe | composition of stressed imgfib + PROVED codegree/m-handling |
| list_planted_arithmetic | decidability implication: given extremality + imgfib + integrality, the crossing is exact integer arithmetic (the integrality arithmetic is the batch-1 margin computation) |

## Verdict

21/21 checked and stressed. **No implication falsified.** Two independent audits
(Codex overnight + this sweep) now agree: the conditional structure of the critical
DAG is sound; the open mathematics is exactly the 7 reds.
