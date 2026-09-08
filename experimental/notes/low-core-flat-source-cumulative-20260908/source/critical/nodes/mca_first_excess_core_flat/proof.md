# Proof

The required basis-or-dense-flag theorem says that a deficient ordered-basis
count yields actual nested flats of ranks r-1,r and sizes a,b with
(s-r)b-(s-r-1)a>N, where 1<=r<=s-2 and a>=0.
In particular b>N/(s-r), so at least one excess flat exists.

Choose the least rank t with an excess flat, and choose any such complete
flat G. Minimality gives the displayed integer caps for EVERY smaller
rank. If its H-points spanned rank j<t, their complete span would have at
least b>N/(s-t)>N/(s-j) points. Nonzero evaluations give j>=1.
This would be a smaller-rank excess flat, a contradiction. Hence G is
spanned by its contained evaluations.

Its polynomial annihilator has dimension s-t. The full locator of its
b distinct roots divides that space, so K-b>=s-t, proving root capacity.
Only these actual H coordinates are used; no receiver or label is changed.

Equivalently, if no proper flat of rank <=s-2 exceeds its threshold,
the basis count is at least P_s. The presence of an excess flat need
not imply deficiency. Counts through the selected flat must still use
a proved counting lemma; minimality is a structural input, not a census.
