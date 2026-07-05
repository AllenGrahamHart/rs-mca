# Pro brief — the AQB c=2 amortization gain (closes rate-1/2 band)

*Self-contained. Construction+certification, or a refutation, both decisive.*

## Setting
Reed-Solomon, rate 1/2, evaluation domain mu_n subset F_q^*, n = 2^41,
k = 2^40, field size q < 2^256. Prior work (the scale-free quotient-remainder
floor) closed the clean-rate corridor for all rates EXCEPT a razor slice at
rate 1/2: the band is open only for log2 q in (255.900, 256). The crossing is
sigma* = 8,592,912,738.

## What is PROVED (take as given; all interval-certified)
At quotient scale c=2 the quotient order is N = n/2 = 2^40 and the base fiber
count is 2^39. With d extra fibers, m = 2^39 + d, the residual DEFICIT of the
plain (unaveraged) quotient-remainder floor at field exponent Q = log2 q is

```
    B_I(Q) = d*Q - 40 - log2 C(2^40, 2^39 + d).
```

At the campaign's chosen d = 4,296,456,369 this is affine-increasing in Q, so
the worst case is Q = 256, where (Robbins-Stirling interval-certified)

```
    B_I(256) = 429,645,546.77  bits   <   429,645,547.
```

So the plain floor falls short by < 429,645,547 bits across the whole open
slice. (q_crit = 255.90000002 where B_I = 0, independently cross-checked.)

## The AQB strategy (proved reduction)
Rather than exhibit one unsafe received word, take a finite FAMILY F of
quotient-box words. PROVED averaging transfer: if the family-average list
contribution exceeds the MCA trigger T at sigma*, then some member exceeds T
(pigeonhole) — an unsafe witness that closes the band. Reduction chain (all
proved): a family with certified net shared-entropy gain >= 429,645,547 bits
amortizes past the deficit and triggers the transfer.

So the ENTIRE remaining obligation is:

> **Construct the canonical c=2 averaged quotient-box family at sigma* and
> certify that its shared quotient structure lets the box charge be paid once
> (amortized) across the family, giving net entropy gain >= 429,645,547 bits
> after all box, overlap, multiplicity, and quotient/fiber normalization
> costs.**

The gain must come from box-charge SHARING: the plain floor charges the full
256-bit box per fiber; a c=2 family with common quotient/fiber coordinates
pays the box charge (near-)once, and the saving is the gain. Target saving is
~0.00039 bits per quotient-order fiber (429,645,547 / 2^40), or ~0.1 bits per
extra fiber d.

## The ask (choose your target)
- **(A) Construct + certify:** exhibit the canonical c=2 averaged family
  (member parametrization + shared quotient/fiber data + reusable box-charge
  datum + transfer maps) and a closed-form / interval-certified entropy ledger
  proving net gain >= 429,645,547 bits. A closed-form fiber-class ledger is
  required (the family has ~5.5e11 members; per-member enumeration is
  infeasible). This closes rate_half_band_closure and the last clean-rate
  corridor.
- **(B) Refute the route:** prove every admissible c=2 quotient-box family at
  sigma* decomposes into independent single-word boxes with no nontrivial
  shared quotient charge (so no amortization gain exists). Equally decisive: it
  kills the AQB route and redirects rate-1/2 to its siblings (safe-side push
  through sigma*, or averaged conversion at a different scale).
- **(C) Conditional:** the gain >= 429,645,547 bits modulo a clean stated
  hypothesis on the c=2 shared-charge structure.

## Admissibility guard (must hold)
The gain computation must NOT circularly consume the per-fiber counts it is
meant to establish (no circularity with the `perfiber` estimate). Keep the
amortization argument structural / self-contained in the quotient geometry.
