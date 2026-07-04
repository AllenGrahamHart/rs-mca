# Pro brief H (Brief-F thread, round 2) — close the 23-bit gap at N' = 128
*Your antipodal-padding construction was verified and banked (every claim
replayed: e_1 formula, difference factorization, base count, |F| exact). It
PASSES the budget at N' = 256 (+41 bits) and is SHORT 23.3 bits at N' = 128:
|F| = 2^65.69 vs required B*/2^33 = 2^89 (B* = 2^122).*

## THE MAP AROUND YOU
generator_economy is now amber CONDITIONAL on exactly this numeric gap. The
gap is at ONE of the two open cells. Anything that closes 23 bits at N'=128
finishes the node. Partial progress is banked proportionally (a 2^80 family
= most of the distance). If you PROVE the gap unclosable for zero-sum-padding
designs, say so — the node then needs either per-row budget refinement
(B* is a global cap; the row-local budget may be smaller — we can pin that
on our side) or a different certificate structure; an impossibility theorem
redirects us correctly and fast.

## The obvious enlargement to try first
Your construction pads with antipodal PAIRS (the mu_2-coset zero sums). At
N' = 128, mu_4-cosets {x, ix, -x, -ix} (i = zeta^{N'/4}) also sum to zero,
as do all mu_{2^m}-cosets. Mixed-block designs (choose a zero-sum block
partition from pairs AND quartets AND octets, plus the two-point core) give
far more selectable configurations at the same e_1 value. Count: does the
mixed-block family reach 2^89 at N' = 128 with the same O(N') cyclotomic
base certificate (block differences still factor through zeta^k - 1 and
1 + zeta powers)? Careful: blocks must avoid the core; distinct (s, padding)
with equal e_1 need the same nonzero-difference convention as before.
Also valid: multi-core variants (cores of size 4 with e_1 = c' zeta^s for a
new unit c'), or ANY other certified family — the requirement is only:
size >= 2^89, differences in a poly(N')-generated semigroup, no fiber-count
circularity.

## Deliverables: (A) a verified family >= 2^89 at N'=128 (give the exact
count formula + the base set; we machine-verify at the F_17 toy analogue);
(B) impossibility for a natural design class (state the class precisely);
(C) the best achievable size with proof (partial win, banked).
