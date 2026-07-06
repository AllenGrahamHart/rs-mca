# Codex DLI gap-attack run (2026-07-06, paused mid-run) — integrated summary

Run was paused (local heavy enumerations crashed the machine; Modal was again
unavailable in its shell). All six attacks executed at least partially before
the pause; results banked here. NO FALSIFIERS ANYWHERE.

1. GAP-TRADE HUNT: 10 window-closed rows (n=32..128, L=2..5, q up to 665089):
   ZERO trades. Extends the pre-Pro hunt (5 rows) to 15 total clean rows.
2. ROTATION-ENGINEERED FAMILY: **ALGEBRAICALLY KILLED** — for n = 2^s and odd
   surviving moment r0, zeta^(2k r0) = 1 forces n | 2k (r0 invertible mod 2^s),
   so the rotation is the identity and no disjoint Q exists. A proof, not a
   failed hunt; closes pre-emption item 6 of DLI_CLOSE_PINNED. (+1440 patterns
   checked empirically, no hits.)
3. TAIL RATIO: N_w / random measured at 4 rows across weights: ratios settle to
   ~1.0 at the larger rows (0.97-1.48 at n=64, counts up to 73088 vs expected
   72289); max 4.31 at a small open-window row (64 vs 14.9 at w=5). The tail
   constant K is real and small (~1 asymptotic, <5 everywhere observed).
4. ANALYTIC MARGIN (exhaustive worst-lambda census, up to 912,672 lambdas):
   worst per-coordinate log2 cos^2 in [-0.84, -0.34] — INDEPENDENTLY CONFIRMS
   the uniform-AC falsification (worst lambda sits above -1 bit/coordinate);
   only the summed form (DLI-NPM) is viable. Matches the round-2 re-pose.
5. LEVEL INDEPENDENCE: no fatal coupling found; the exact tower factorization
   is census-verified; the product-measure-across-levels hypothesis correctly
   remains an explicit unproved hypothesis (as flagged in the pinned doc).
6. IDENTITY REPLICATION: D2 = D3 exact (<= 7e-14) at 3 new rows, with
   weight-resolved trade counts as a bonus dataset.

All six feed DLI-CLOSE-2 (already dispatched): the tail-ratio ~1 and the
near-peak margin data directly support DLI-NPM's dyadic route.
