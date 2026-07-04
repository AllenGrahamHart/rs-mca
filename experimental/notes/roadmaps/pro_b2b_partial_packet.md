# Pro B2b partial packet (verified 17/17, toy + exact arithmetic)

Delivered by GPT Pro 2026-07-04; every lemma machine-verified
(tools/../nodes/b2_modp_giant_extras/notes/verify_pro_packet.py).

## The exact dyadic-descent suite (Lemmas 1-7) — PROVED
- L1 complement duality: sum over mu_n of x^r = 0 (r < n), so t-null
  transfers to the complement; locator form L_A L_{A^c} = X^n - 1.
- L2/L3 iterated descent: m_j(y) = #{x in A : x^{2^j} = y} has
  0 <= m_j <= 2^j and p_s(m_j) = p_{2^j s}(A); t-null A gives
  floor(t/2^j)-null multisets.
- L4 honest lift count: per fiber, l_j(a) = 2^j + 1 - |a - 2^j| raw
  splits (odd equations NOT included - lossy-but-honest).
- L5 odd equations retained exactly: fixing a square-root section,
  p_{2s+1}(m) = sum d(y) sigma(y) y^s with the skew d = m(sigma) -
  m(-sigma); even + odd = the full constraint set. The clean
  formalization form.
- L6 coset fixed points: mu_{2^j}-coset unions <=> m_j in {0, 2^j};
  quotient nullity transfers with floor(t/2^j).
- L7 boundary-scale REPAIR: at official t = 2^33 + 1 the subgroup
  scale is M_0 = 2^{floor log2 t} = 2^33 (R = 256 at rates 1/4, 1/8;
  M_0 = 2^32, R = 512 at 1/16), NOT M = t; the boundary class =
  mu_{M_0}-coset unions with p_1(C) = 0 on the quotient, after
  stripping antipodally-invariant patterns (which are mu_{2M_0}
  unions, already in the M > t dictionary).

## The near-tail interpolation bound (L8-9, Thm 10) — PROVED
- L8: N_{t+k} <= C(n,k)/C(t+k,k) by degree-(k-1) interpolation
  (at most one member of the flat X^b + F[X]_{<=k-1} vanishes on a
  given k-set).
- Thm 10 at n = 2^41, t = 2^33 + 1: both near-tails
  (min(|A|, n-|A|) in [t+1, t+15]) together contribute < 2^122
  (n/t < 2^8, so N_{t+k} < 2^{8k}; exact-fraction product bound
  verified at k = 1 and 15).

## Hazards (both accepted)
1. The b2 statement's "coset unions at scale M = t" was literally
   false at non-2-power t — repaired to the M_0 convention (matches
   QA.25).
2. Brief frame (c) is VACUOUS: p_r(gamma A) = gamma^r p_r(A), so
   scalar-conjugate domains give identical vanishing — the variance
   over gamma mu_n is identically zero. Falsification #14 (mine).

## What remains: the primitive core
#{t-null primitive B : t+16 <= |B| <= n/2} <= 2^122. The descent
reduces it to bounded-multiplicity multiset-null counting WITH the
odd skew equations; interpolation dies at k = 16 (2^128 > budget).
One structural input still needed.
