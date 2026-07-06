# PRO WINDOW — "DLI-CLOSE-3" (round 5; your round-4 refutation verified and integrated)

*Your DLI-NPM refutation was verified exactly (the 3^12 rational ledger reproduces
to the fraction). Our diagnostic went one step further: RANDOM 12-subsets of the
same half-section also fail (E = 4.1, 3.6, 3.7) — the cause is not the segment
structure but the volume ratio: N = 12, L = 2, q = 97 violates 2^N >= q^L
(4096 < 9409). Your own scope note is confirmed: the full 16-point half-section
at the same row gives E = 1.3477. The row class is now pinned for good.*

## The scoped row class R* (this is the real object — no remaining slack)

- q prime, q ≡ 1 (mod n'), n' = 2^s.
- X = c · (the FULL half-section of mu_{n'}), any c != 0; N = n'/2.
  (The production tower levels are exactly these: a dyadic residue class of the
  big section is a rotated full half-section of a smaller mu; kernels are
  rotation-invariant.)
- **2^N >= q^L** (balanced volume; automatic at production where N = 256L and
  q < 2^256).
- No antipodes / no full cosets in X (inherited, verified).

## THE TARGET (DLI-NPM*)

> For every row in R*:  sum_{lambda != 0} T(lambda) <= 3,
> T(lambda) = prod_{y=1}^{N} cos^2(pi a_y(lambda)/q),
> a_y(lambda) = sum_{l=1}^{L} lambda_l x_y^{2l-1}.

Equivalently (your round-4 exact form): the weighted kernel mass satisfies
W <= 4 * 2^N/q^L - 1 on R*.

Status of every refutation produced so far, against R*:
- round-2 witness (q=65537, N=256, L=1): in R* by volume (2^256 >> q); E = 1.000000
  there — SURVIVES (the W-blowup was balanced mass, display artifact).
- round-4 witness (N=12): violates 2^N >= q^L — outside R*.
- all verified R* rows: W = 0.348 (97,32,16), 0.751 (257,32,16), ~1e-6 (DPs),
  0.000000 (your 65537 row). Nothing has ever exceeded 3 inside R*.

## The ask

> **(A) Prove DLI-NPM\*** on R*. Your own two counted routes from round 4 are the
> suggested architecture (both summed — the guardrail holds):
>   - dyadic near-peak ledger: sum_j 2^{-j} |B_j| <= 3,
>     B_j = {lambda != 0 : j <= -log2 T(lambda) < j+1};
>   - half-circle census: T >= 2^{-j} forces lambda in
>     G_j = {lambda != 0 : #{y : ||a_y(lambda)/q|| > 1/4} <= j};
>     leaf: sum_{j>=1} 2^{-j} |G_j| <= 3.
>   The G_j count is a small-value concentration statement for the low-degree odd
>   polynomial P_lambda on the full half-section: lambda in G_j means P_lambda
>   lands in the quarter-arc at >= N - j of the N points. For j << N this is
>   massively overdetermined — the norm-gate/resultant route (each near-miss is a
>   divisibility) or a Weil-type bound on the quarter-arc indicator both apply,
>   and the target has the two-for-one margin (circle average -2 bits vs -1
>   needed).
> **(B) Refute**: a verified row IN R* with sum_{lambda != 0} T > 3. Note this
>   now requires the full half-section and the volume condition — every slack
>   dimension used in rounds 2 and 4 is closed. A genuine refutation would be a
>   discovery about odd-polynomial small-value concentration on half-sections.
> **(C) Conditional**: reduce to a single exact statement about |G_j| growth
>   (e.g. |G_j| <= C^j binomial-type), with constants that survive the
>   sum_j 2^{-j} weighting.

## Guardrails (five rounds of tennis)

sup-profiles -> weighted; W-display -> E-display; uniform-lambda -> summed;
unpinned N -> R*. Uniform quantifiers and unpinned parameters die; averages and
pinned classes survive. R* is the production object itself — if DLI-NPM* is
false on R*, the dli node is false and the campaign needs to know immediately;
if it is true, this is the last round.
