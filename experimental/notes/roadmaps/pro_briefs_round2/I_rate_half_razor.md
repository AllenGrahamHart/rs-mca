# Pro brief I — the rate-1/2 razor slice (fresh window; self-contained)

## THE MAP AROUND YOU
Rate 1/2 is the last rate with an open determination band, and the band is
now PROVEN razor-thin: the scale-free quotient-remainder floor (the proved
unsafe mechanism) reaches agreement-excess n/log2(q), which covers the
crossing sigma* = 8,592,912,738 for ALL admissible fields with log2 q <=
255.900. The band survives ONLY for q in the top 0.100 bits of the allowed
range (q in (2^255.9, 2^256)), where the floor tops out at 2^33 =
sigma* - 2,978,146. Three routes are open; ONE suffices. Equally valuable:
a matching SAFE-side theorem showing the band is genuinely undecidable-by-
these-mechanisms would land rate-1/2-at-max-q as honest bracket-grade — the
campaign accepts that outcome if it is proven, so a tightness construction
is a real deliverable, not a consolation.

## Setup (self-contained)
RS over mu_n, n = 2^41, k = 2^40 (rate 1/2), q prime in (2^255.9, 2^256),
q = 1 mod n. Agreement excess sigma = A - k. UNSAFE side proved up to
sigma <= 2^33 via: pick c | n, N = n/c, m = k/c + d; the received word with
syndrome supported on one quotient fiber gives list size >= C(N, m)/q^{d-1}
(the quotient-remainder floor); trigger: list > (q-n)/k => MCA failure at
radius 1 - (k + dc)/n. Depth d*c caps at ~n/log2 q ~= 2^33 (entropy 1 bit
per fiber point vs log2 q bits per box charge — proven exactly). SAFE side
proved for sigma > sigma* (half-distance/pincer machinery). The band:
sigma in (2^33, sigma*], width 2,978,146, ~2^21.5 wide.

## The three routes (any one closes the node)
1. AVERAGED CONVERSION AT GIANT M: the floor uses ONE received word; an
   averaged/multi-word variant (a family of syndromes sharing quotient
   structure, list mass averaged over the family) could beat the single-word
   entropy-vs-box tradeoff — the box charge amortizes if the words share
   ambient structure. Does an L-word average push depth by the missing
   factor 1 + 2,978,146/2^33 ~= 1.00035 (only 0.0005 bits/fiber needed!)?
2. B2b-STYLE BALANCE: the band's counting problem in the dual language —
   bound |{t-null-ish configurations}| in the band window directly (the
   norm-gate machinery from the B2b program transfers; a PCF-style estimate
   in this window is 2^21.5-narrow, far easier than the general case).
3. SAFE-SIDE PUSH: lower sigma* itself for q near the cap — the crossing
   constant came from the generic pincer; at maximal q the pincer's slack
   terms are at their weakest and a refined constant may cross 2^33.
4. (Tightness) OR: prove a list-size upper bound at sigma in the band
   matching the floor — the band is then genuinely open-by-necessity and
   the determination is bracket-grade AT THE CAP ONLY, proven.

## Deliverables: (A) any route closing the band; (B) the tightness theorem;
(C) conditional on one named estimate. The margin needed is measured in
TEN-THOUSANDTHS of a bit per fiber — state clearly which inequality you
attack and by how much it must move.
