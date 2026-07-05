# PRO THREAD T8 — "DIHEDRAL-CERT" (fresh window)

*Self-contained. The rate-1/2 covering certificate. The mechanism + entropy are
verified; the remaining work is a degree/distinctness certificate, NOT numerical.*

## Setting
Prize grand challenge at rate 1/2, razor slice log2 q in (255.900, 256). n=2^41,
k=2^40. MCA/list is PROVED clean at rates 1/4,1/8,1/16. At rate 1/2 the residual
band is 2^33 < sigma <= sigma* = 8,592,912,738 (size 2,978,147), the shadow of the
2-power quotient-core floor cap n/256 = 2^33.

## What is proved / verified (black boxes)
- **AQB route REFUTED:** family-averaging cancels the box-sharing gain (convex
  combination); do NOT retry averaged/box-charge mechanisms.
- **Dihedral mechanism + entropy VERIFIED:** the inversion/Chebyshev quotient
  x -> x + x^{-1} has twin-pair fibers {x, x^{-1}}, giving FINE-GRAINED scales d (not
  just 2-powers). Strict window: scale d covers sigma < d, count C(2^40, 2^32+1),
  log2 ~ 4.05e10 >> trigger B* < 2^128 (margin 3e8x). Even scales cover
  [2^33, sigma*-1] (1,489,073 scales); the inversion fixed points +-1 give an
  endpoint sibling d=sigma*+1 covering sigma=sigma*. NON-AQB (single-family
  witnesses), non-giant-M.

## The ask (target: dihedral_sibling_window_certificate)
> For every sigma in [2^33, sigma*], certify a dihedral/Chebyshev quotient-core
> family (twin fibers x+x^{-1}, plus one inversion fixed point at the endpoint) whose
> members are valid degree<k=2^40 RS codewords giving > floor(q_line/2^128) bad
> witnesses at agreement k+sigma, uniformly for log2 q in (255.900, 256).

Concrete obligations:
- **(1) Chebyshev degree audit:** the locator/codeword shapes built from x+x^{-1}
  (and, at the endpoint, one fixed singleton) stay within degree < k.
- **(2) Distinctness / noncontainment audit:** the dihedral witnesses are distinct
  after evaluation on D and are NOT silently the old 2-power quotient-core witnesses
  already counted.
- **(3) Strict-window endpoint audit:** confirm the exact condition sigma < d; use
  d = sigma+1 for each target sigma, with the fixed-point sibling supplying the
  top-endpoint parity d = sigma*+1.
- **(4) Priced count certificate:** trivial once certified — log2 C(2^40,2^32+1) ~
  4.05e10 >> 128 (VERIFIED).
- **(B) Fallback:** a sigma in the band where every dihedral twin/fixed-point family
  overflows degree k, collapses to the old qcore count, or fails noncontainment ->
  then rate-1/2 is bracket-grade.

Supported by: E26 dihedral plan, floor-depth verdict (cap n/256), B2b no-
concentration scan (39/39, max excess 2^4.18). Downstream: rate_half_band_closure ->
the rate-1/2 grand-challenge determination (the last rate).
