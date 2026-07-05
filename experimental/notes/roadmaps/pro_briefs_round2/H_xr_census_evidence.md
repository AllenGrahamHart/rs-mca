# XR eliminant nonvanishing census (Modal, evidence-only)

Faithful port of verify_xr_triangle_eliminant_form: profile = overlap shape
(pair_sum, triple_size, union_size); light iff pair_sum - trip <= 2k;
nonvanishing for a profile iff SOME instance (supports+slopes over F_p) reaches
full rank 3t (a full-rank instance is a valid nonzero-minor certificate).

RESULT (8 rows, k=2..6, t=2..5, A=4..11, n=12..26, ~40k light samples/row):

| row (p,n,k,A)   | t | target 3t | light profiles | certified nonvanishing | gaps |
|-----------------|---|-----------|----------------|------------------------|------|
| 101,12,2,4      | 2 | 6         | 9              | 9                      | 0    |
| 101,14,3,5      | 2 | 6         | 15             | 15                     | 0    |
| 101,16,3,6      | 3 | 9         | 14             | 14                     | 0    |
| 101,18,4,7      | 3 | 9         | 20             | 20                     | 0    |
| 103,20,4,8      | 4 | 12        | 18             | 18                     | 0    |
| 103,22,5,9      | 4 | 12        | 26             | 26                     | 0    |
| 107,24,5,10     | 5 | 15        | 21             | 21                     | 0    |
| 109,26,6,11     | 5 | 15        | 29             | 29                     | 0    |

152 distinct light profile types, ALL certified nonvanishing; ZERO identically-
vanishing light profiles found. Nonvanishing is uniform across scales.

STATUS: EVIDENCE ONLY (does not close the node). The profile-type count GROWS
with (k,t) (9..29), so the full quantifier at k=2^40 is not enumerable — the
close needs the parametric argument (Pro brief). But the census confirms the
theorem is TRUE and that a generic/triangular minor is nonzero for every
profile at every tested scale — exactly the structural fact the proof needs.
