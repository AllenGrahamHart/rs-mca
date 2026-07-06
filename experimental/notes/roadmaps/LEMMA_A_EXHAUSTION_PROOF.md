# Lemma A: two-class exhaustion PROVED (with sharp scope) — 2026-07-06

## Statement
In a planted sunflower cell (core = k-1 points with word value 0; M petals of size
ell = sigma+1, petal p carrying scalar_p * L_core; background = the remaining
points, value 0) with **background <= 1 point** (the max-fill convention of the
official cells): every non-planted list word g (deg < k, agreement >= s = k+sigma,
sigma >= 1) touches at least TWO petals — i.e. lies in the E15 challenger class
(mixed_petal or full_petal). Together with the planted family this EXHAUSTS the
list: no third class.

## Proof
Let g be a non-planted list word with agreement composition a (core) + b_j (petal
j's points) + c (background), a + sum_j b_j + c >= s. Note the word equals f_j :=
scalar_j * L_core on petal j, and equals 0 on core and background; each planted
f_j also vanishes on the core.
- If g touches NO petal: agreement <= (k-1) + c <= (k-1) + 1 = k < k + sigma = s.
  Contradiction.
- If g touches exactly ONE petal j: agreement at core points means g = 0 = f_j
  there; agreement at petal-j points means g = f_j there. So g agrees with the
  polynomial f_j at a + b_j = s - c >= (k + sigma) - 1 >= k points (sigma >= 1,
  c <= 1). Two polynomials of degree < k agreeing at k points are equal, so
  g = f_j — planted. Contradiction.
Hence g touches >= 2 petals. QED.

## Sharpness (verified numerically — the hypothesis is load-bearing)
With larger background the conclusion FAILS, with explicit witnesses:
- bg=5 (q=97, k=4, sigma=1, M=4): the ZERO polynomial is a non-planted list word
  of class BG/CORE_ONLY (agreement = core 3 + bg 5 = 8 >= s = 5).
- bg=9 (M=2): three ONE_PETAL non-planted list words + one BG/CORE_ONLY.
- bg=1 (max-fill, M=6): none, at every tested (q, sigma) — matching the lemma.

## Scope notes
- The official e22_core cells use petal_count = max-fill, so bg <= 1 always:
  Lemma A covers every cell of the existing censuses (219 + 77 + gate cells) and
  EXPLAINS their UNCLASSIFIED = 0 outcome as a theorem, not an observation.
- At official crossing radii the same argument gives the analogous exclusion
  whenever c <= sigma - 1 + (s - k - sigma) slack; the max-fill convention or a
  crossing-radius margin supplies it. Receivers outside the sunflower family are
  worst_word_planted's obligation, not this node's.

## The verified pricing law (the envelope's quantitative shape)
Challenger counts obey the campaign's universal WINDOW LAW (third verified
instance, after u2c accidents and dli trades): a challenger is a codim-sigma
coincidence (s = k + sigma agreement points overdetermine a deg<k polynomial by
exactly sigma conditions), so
    E[#challengers] ~ K_cell / q^sigma,
verified: 1/q scaling at sigma=1 (count*q ~ 2000 stable across q = 97..449 at
n=16, k=3); sigma=2 window OPENS at q=17 (7 challengers, all >= 2-petal) and
closes by q=97; sigma=2,3 empty at all official-scale toy cells.
