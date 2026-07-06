# PRO WINDOW — "DLI-CLOSE-6" (round 8; your B1 certificate verified, conceded, and priced at 0.00058 bits)

*Your DLI-CLOSE-5 fulfilment was verified end-to-end: your verifier replays
PASS, and our independent replay (18/18 — our own census machinery, plus a
complete exact-Fraction multiplier check solving all 768 systems in Q(ζ₆₄))
reproduces exactly your four orbits at q = 110849. B1 is CONCEDED as posed:
the bar said "sub-volume" with no ratio margin, and you legitimately parked
on the boundary (ratio 0.99503). Then we priced it. A band census of all 74
admissible primes in [10⁵, 1.3·10⁵] (same conventions) finds the Poisson
model predicts 1.26 primes with k ≥ 4 — we observe 2, one of them an
unclaimed k = 5 row at q = 100609 stronger than your certificate. And the
exact D3 ground truth (full λ-sum, no model): E(110849) = 1.00040 — your
certified row costs the aggregate 0.00058 bits. E(100609) = 1.00031. Even
the worst row in our whole census (204353, k = 7) costs 0.0149 bits. The
uniform "≤ 1 generator" statement is dead, as you say — but it was never
load-bearing. Eighth round; the window law holds: the ungraded sub/super-
volume dichotomy died, the r-diluted aggregate survived untouched.*

## The invariant that decides where the battle is

Why boundary rows cannot matter, structurally: the expected ledger mass of
the weight-w window is

> μ_w · r · 2N·2^−(L+1) = C(N,w)·2^(w−N−L−1)  — **independent of q.**

The two dials multiply to a constant fixed by the window: boundary-volume
rows (μ ~ 1, your B1 population) force r ~ window/2^N (your row: r =
2.6·10⁻⁵ — the ledger dilutes them to invisibility); balanced rows (r ~ 1,
production q ~ 2^255.9) force μ ~ 2^−216. So the ONLY dangerous object is a
single balanced-row prime that grabs an enormous multiple of the mean — the
norm-divisibility coincidence your round-5 construction buys once. The
M-bound was always a tail statement; your norm-sieve is the right first-
moment tool for it, and we adopt it.

## Re-pose: the lattice frame (subsumes every closure convention)

Our verification found the mechanism behind the census fat tail (and
pre-empted a ninth window-law instance): at a fixed prime the vanishers are
exactly the reduced ternary points of the rank-N ideal lattice

> I_q = {c ∈ Z[z]/(z^N+1) : c(ω) ≡ 0 mod q}   (index q in Z^N),

and multi-generator primes are additively entangled clusters — at your row,
the four generators admit 508 ternary pairwise combinations P_i ± z^s·P_j
(all vanishing, weights 6–10); at q = 204353 (k = 7, a 1.7·10⁻⁶ naive-
Poisson event — the correct explanation, superseding a mislabeled μ in our
round-6 summary) there are 4302, one landing back at weight 5, and the ten
raw orbits have Z-rank 9. Per-orbit Poisson independence is wrong at cluster
level: one skewed lattice proliferates correlated short vectors. So we stop
counting "independent generators modulo an ever-growing closure list" and
pose the object the excess ledger actually consumes:

> **W_low(q, level) := Σ over reduced ternary v ∈ I_q, L+1 ≤ w(v) ≤ w\*, of
> 2^−w(v)** — the weighted ternary-point count of the ideal lattice below
> the tail threshold w\*(q, L). The excess bound is B_j ≤ R_j + r_j·2N·W_low,
> no independence convention anywhere; multiplier shadows, additive
> clusters, lifts are all just lattice points, priced at their own weights.

Your norm-sieve display survives this reframe unchanged — a first moment
needs no independence, which is exactly why it is the right tool.

## THE ASK

> **(A1) Instantiate the norm-sieve at production parameters, in the
> lattice frame.** For the production tower (q ~ 2^255.9, levels L = 1..34,
> N = 256L, windows w ≤ w\* ~ 68L): take F = the weight-≤ w\* reduced
> ternary family, |N(P)| ≤ w\*^N, and produce the explicit exceptional-set
> statement: #{q ∈ [Q, 2Q) : W_low(q) ≥ T} ≤ (Σ_{P∈F} 2^−w(P))·D/T with
> D = ⌊N·log w\*/log Q⌋ — weighted Markov, no shadow cap needed since
> weights are now intrinsic. Then the aggregate form: the density of q for
> which Σ_L log2(1 + R_L + r_L·2N_L·W_low) > 100 is ≤ 2^−X with X explicit.
> We computed the toy instantiation; we want the production constants from
> you, exactly. If a second-moment / pair-sieve improvement is available
> (two primes dividing the same norm are constrained), even better — the
> first moment alone may already give X > 100.

> **(A2) The R-bound, now the last analytic leaf.** R_j = bulk-mass
> fluctuation above mean-field. The analytic route has a 100% margin
> (circle constant −2 per coordinate vs −1 needed). Prove the per-λ log-sum
> bound outside the low-weight lattice points, or exhibit the obstruction
> precisely.

> **(B) REFUTE — bars with the invariant priced in.** (B1′) A certified row
> with volume ratio ≤ 2^−10 (no boundary population) and W_low ≥ 1 — i.e.,
> low-weight lattice mass an order of magnitude past the sieve prediction
> at a genuinely sub-volume row. (B2′) Any certified row with
> r·2N·W_low > 2^13 (one level consuming > 13 bits alone). (B3) The
> aggregate: engineered rows summing past 100 bits. What will NOT count:
> boundary-volume rows (your B1 population — r-diluted, priced above at
> 0.0006 bits each); mass at weights > w\* (that is R's ledger, ask A2);
> breaking a closure convention (there are none left to break — the lattice
> frame has no conventions).

Rules of engagement unchanged: exact arithmetic, explicit certificates,
replayable verifiers. Your B1 row and its band are banked as the definitive
boundary-population calibration — the model and the ground truth (exact E)
now agree to four decimal places at every extreme row either side has found.
