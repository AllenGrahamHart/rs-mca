# Audit: recorded "target/candidate/conditional" results that are actually proved

- **Status:** AUDIT / VERIFIED. Identification pass (no status flips applied — those
  touch other owners' files; see "Ownership" below).
- **Agent/model:** Claude Opus 4.8 (1M context), branch `allen/m1-reserve-subsumption`.
  Produced by a fan-out sweep (10 lanes, 204 files) with per-item adversarial verification.
- **Date:** 2026-06-26.
- **Verifiers:** `experimental/scripts/verify_m1_tangent_floor_gate_ladder.py` (PASS),
  `experimental/scripts/verify_m1_reserve_subsumed_by_strict352.py` (PASS).

## The lever: the moving-root tangent floor

`experimental/data/tangent/tangent_staircase_section.tex` Thm "moving-root tangent
floor" proves, by an **elementary MDS argument** (no smoothness, no Cycle84 slot
model, no analytic input):

```
LD_sw(C, a) >= n - a + 1   for every  k+1 <= a <= n,   on any C = RS[F, D, k].
```

For the row `C = RS[F_17^32, H, 256]` (`n=512, k=256, q=17^32`) with the bridge
`emca(C,delta) = LD_sw(C, ceil((1-delta)n))/q` and the gate `emca > 2^-128 <=>
LD_sw >= 7` (since `floor(17^32/2^128) = 6`):

> the tangent floor clears the `>=7` gate for **every** `a <= 506` — unconditionally.

This single proved result subsumes the `>=7` **gate** of a whole stack of recorded
items (verified per-item in `verify_m1_tangent_floor_gate_ladder.py`):

| a | recorded item | recorded status | tangent floor LD_sw≥ | gate |
|---|---|---|---|---|
| 262 | cycle116/cycle120 prize gate | conditional (Cycle84 N) | 251 | clears |
| 263 | cycle119 strict263 | conditional (Cycle84 N) | 250 | clears |
| 264 | strict264 gate | proved(min≥9)/cand(2187) | 249 | clears |
| 272 | reserve272 | target | 241 | clears |
| 288 | reserve288 | target | 225 | clears |
| 313 | reserve313 | target | 200 | clears |
| 264–352 | strict352 range (gate) | proved (quotient-core) | ≥161 | clears |
| 506 | tangent506 last unsafe | proved/exact-gate | 7 | clears |
| 507 | (first safe) | proved/exact-gate | 6 | safe ✓ |

## (A) Already proved — recorded status should flip (ranked by impact)

**A1. Cycle120 prize gate** `emca(C,125/256) > 2^-128` (a=262) — *highest impact, prize-facing.*
Recorded **conditional** on the unreproduced Cycle84 census `N=52,747,567,092`
(`audit_pr100_cycle120_gate.md`, `audit_pr105_cycle120_standalone.md`). The tangent
floor gives `LD_sw(C,262) >= 251 >= 7`, so the **threshold/gate is unconditional**.
Only the exact *density* (~`2^-95`) still needs `N`.

**A2. Cycle119 strict strengthening** `delta*_C <= 249/512` (a=263). Recorded conditional;
tangent gives `LD_sw(C,263) >= 250 >= 7` ⟹ threshold unconditional. Exact density open.

**A3–A5. reserve272 / reserve288 / reserve313** (`site/data/frontier.json`, status `target`).
Tangent floor (241/225/200) **and** strict352 (M = 1.94e13 / 1.63e6 / 295) both prove the
needed `>=7`. Already certified by `verify_m1_reserve_subsumed_by_strict352.py`. Flip to
`proved`. (See companion note `m1_reserve_subsumed_by_strict352.md`.)

**A6. strict264 gate** (a=264). `frontier.json` already records `strict264-min` as `proved`
(badSlopes 9); the residual "open" framing survives only in audit/triage prose. Gate is
proved twice (quotient floor ≥9, tangent ≥249).

**A7. conj:B quotient-floor "separation"** (planned X1 target) — proved in Paper B
`prop:qfloor` (`slackMCA_v3.tex`:1273), as the note's own reassessment already concedes.
*(my lane — X1)*

**A8. prob:explicit density `> 2^-22`** (Paper D). The explicit non-B-rational family with
density `> 2^-22` is proved in-repo (`x1_prob_explicit_deep_point.md`, deep-point identity
+ averaging + `lem:fiber`(ii); `verify_x1_prob_explicit_deployed.py` PASS). *(my lane — X1)*

## (B) Easily proved (short new proof needed)

**None.** Every (A) item is a pure subsumption by an already-proved in-repo result or a
stale-label correction — no new derivation required. The only new code is the two gate-ladder
assertions above, which are bookkeeping, not a proof.

## (C) Cosmetic — label / stale-prose only

- **C1.** `m1_strict264_audit.md` header prose still implies the a=264 gate is open; `frontier.json`
  already has it `proved`. Update the prose.
- **C2.** `strict264-2187` (`frontier.json`/`rate-leaderboards.json`): the **gate** is proved, but
  the headline `nBad=2187=3^7 / +8.30 bits` exact count is **not** — keep it `candidate`, add a
  nonClaims line "gate cleared independently; only the exact 2187 shape remains candidate."
- **C3.** `tangent506-exact-gate` status differs across the two board files: `proved` in
  `frontier.json` vs `exact-gate` in `rate-leaderboards.json`. Harmonize.
- **C4.** `pr-triage-2026-06-23.md` frames the delta=125/256 negative counterexample as
  conditional; per A1 the gate is unconditional. Prose-only.

## (D) Looked closeable but genuinely OPEN (do NOT flip)

- **D1.** Exact `nBad = 2187 = 3^7` slot count at a=264 — slot-model-dependent (Cycle84 not in repo).
- **D2.** conj:B matching **upper** bound / aperiodic half (`prob:perfiber` / L1 `Q_1^list <= n^B`) — open analytic.
- **D3.** A single machine-pinned explicit witness line for `prob:explicit` (density proof is existential in alpha; infeasible to pin over F_{p^6}).
- **D4.** Exact Cycle119 density `~2^-95` / exact `delta*_C` — still rests on the unreproduced Cycle84 census `N` and the two-ended transfer.

## Ownership (how each flip should be made — I do NOT edit others' files)

- **A1/A2/A6, C1/C4 — M1/audit lane (Codex/Danny):** propose via an independent audit note +
  verified flag/PR comment; do not edit their audit notes or `tex/`.
- **A3/A4/A5, C2/C3 — `site/data/*.json` (Przemek's board):** propose via a PR from my branch;
  maintainer merges. (The arithmetic is already certified by passing verifiers.)
- **A7/A8 — X1 (my lane):** I can update my own `notes/x1/*` headers directly next turn.

## Bottom line

The two highest-value flips are the **prize gates** (A1/A2): the prize-facing negative
counterexample `delta*_C <= 125/256` (and the strict `<= 249/512`) no longer depend on the
unreproduced Cycle84 census — the tangent floor proves the `> 2^-128` threshold outright. Then
the three `frontier.json` `target -> proved` flips (reserve272/288/313). In every case flip only
the **gate/threshold/density-floor** claim; leave the exact-count residuals (D1–D4) recorded open.

## Reproducibility
```bash
python3 experimental/scripts/verify_m1_tangent_floor_gate_ladder.py
python3 experimental/scripts/verify_m1_reserve_subsumed_by_strict352.py
```
