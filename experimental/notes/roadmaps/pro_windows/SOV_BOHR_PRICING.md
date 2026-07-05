# PRO WINDOW — "SOV-BOHR-PRICING" (fresh window)

*Self-contained. The last open obligation of the sov branch (grid-sum residual).
The decomposition is settled and the mechanism is verified; what remains is ONE
pricing question with a rich empirical contract attached. Prime-field only.*

## Setting
F_p (p prime; toy p up to 65537, prize-scale p ~ 2^250+). A residual "cell" is a
set Gamma subset F_p^* of size m (root sets surviving the earlier paid gates).
For h <= m, the object is the h-fold distinct-subset-sum VALUE SET
    V_h(Gamma) = { sum_{x in S} x : S subset Gamma, |S| = h },
and the obstruction count is controlled iff |V_h| is large relative to the
achievable mass min(C(m,h), p). The adversarial statistic is the normalized
power sum / additive Fourier coefficient
    B(Gamma) = max_{a != 0, small j, char∤j} |sum_{x in Gamma} psi(j a x)| / m,
(sweep ALL frequencies a — an incomplete sweep provably misses AP/Bohr cells).

## What is proved (black boxes)
- **T1 subfield/trace gate (PROVED):** trace-flat / subfield-norm cells are paid
  or base-reduce. Removed before this question starts.
- **Quotient / pullback / dihedral gates (paid):** likewise removed.
- **Lane-1 Euler-product theorem (PROVED):** if the power-sum bound B holds
  (all normalized power sums <= B), then the count of h-subsets in any fixed
  fiber obeys |S_r| <= [u^r] (1-u)^{-Bm} (1-u^{p0})^{-(m-Bm)/p0}
  (p0 = smallest prime > relevant scale) — i.e. LOW B forces a LARGE value set.
- **T4B refutation (VERIFIED, the reason this class exists):** the arbitrary-cell
  claim is FALSE — additive Bohr/interval cells Gamma = {1..(p-1)/R} are
  non-trace-flat, non-quotient, non-dihedral, positive density R^{-r}, yet
  |V_h| <= (r/R)p. Concrete: F_65537, R=64, h=21: value set 0.321p, char ratio
  0.9996, density 2^{-126.3}. So a NEW paid class (the Bohr/large-power-sum
  gate) is provably necessary; the question is its PRICE.

## Empirical contract (verified this campaign — your answer must match)
1. **Dichotomy (mechanism, exhaustive-style census, 1064 cells, 9 families incl.
   degenerate):** every collision-heavy cell (small value set relative to
   min(C(m,h),p)) is Bohr-caught: 521/521 with B >= 0.15. Zero cells evade.
2. **Sharp phase transition (quantitative Lane-1 probe, 328 mass-sufficient
   cells + a dilution sweep):** value-set deficit ~ 0 for ALL cells with
   B <= ~0.93; only near-pure Bohr cells (B -> 1) collapse (deficit 0.99).
   A 10% random admixture into a pure interval already RESCUES the value set
   (B drops ~0.93, deficit -> 0).
3. **Over-inclusion of naive gates (toy row (p,m,h)=(29,7,4), sampled 150k):**
   gate at B*=0.50 includes 92.88% of cells; at 0.70 includes 11.55%; at 0.93
   leaves 2163/150000 low-value-set cells BELOW the gate (worst observed:
   B=0.9087 with value fraction 0.4483 — toy-scale, small-sample caveat).
   So: gate too low => class far too big to price; gate too high => cells
   Lane-1 must close but currently doesn't (toy) slip under.
4. **The stressor family sits AT the budget scale:** collapsing interval rows
   appear for R >= 48 with densities log2 C(m,h)/C(p-1,h) =
   -117.5, -126.3, -138.8, -147.6 at R = 48, 64, 96, 128 (p=65537, h=21).
   The ledger scale is 2^{-128}: the R=48,64 rows are ABOVE budget scale and
   MUST be handled by the gate; R >= 96 rows are below. The pricing has ~2-10
   bits of room, not orders of magnitude. This family is the calibration test
   any proposed price must pass.

## The ask
> **Price the Bohr/large-power-sum paid class.** Exhibit a threshold B* (or a
> threshold FUNCTION of (m,h,p)) and prove BOTH:
> (i) **Lane-1 closure below the gate:** every residual cell with B(Gamma) <= B*
>     has |V_h| >= the ledger requirement (e.g. (1-o(1)) min(C(m,h),p), or the
>     precise downstream bound) — a sharpened Euler-product/Lane-1 estimate
>     valid up to B*. Empirics say the truth extends to B* ~ 0.93+.
> (ii) **Bounded mass above the gate:** the total density/count of residual
>     cells with B(Gamma) > B* is within the ledger budget — a structured
>     description (e.g. all near-pure Bohr sets = intervals/APs up to bounded
>     perturbation, via an inverse/stability theorem for large power sums) plus
>     a count. The R=48,64 interval rows (densities 2^{-117.5}, 2^{-126.3})
>     must be inside the priced class.
> - **(B) Refute:** show (i)+(ii) cannot meet — e.g. a positive-density-scale
>   family in the gap (0.93 < B < 1) with collapsed value set and mass above
>   any affordable budget. This would kill the current sov decomposition and
>   force a different residual mechanism.
> - **(C) Conditional:** reduce to a clean inverse theorem ("normalized power
>   sum > B* forces bounded-perturbation Bohr structure") + a count, each
>   attackable separately.

## Notes for the proof
- The natural shape for (ii) is an inverse theorem: |sum psi(ax)| > B*m with
  B* near 1 forces Gamma to be a bounded-symmetric-difference perturbation of
  a Bohr set/interval/AP union; those are countable (choices of frequency,
  length, perturbation) and their density sums geometrically — the R-table
  above suggests the count is dominated by the coarsest admissible R.
- The dilution empiric (10% admixture rescues) says the inverse theorem's
  perturbation tolerance and Lane-1's reach MEET — there should be no gap,
  but proving the meeting point is the content.
- Downstream: closes sov_gridsum_residual -> sov_affine_piece_partition_payload
  (re-posed P3') -> midlarge/anchored chain -> mca_safe. Together with the
  proved Lane-1 theorem this ends the sov branch.
- Executable predicates exist for every object here (value-set via subset-sum
  bitset DP; B via full-frequency sweep); any candidate B* or inverse-theorem
  perturbation bound can be validated numerically in seconds.
