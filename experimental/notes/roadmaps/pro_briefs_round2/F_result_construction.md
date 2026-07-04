# Pro Brief F construction (verified toy 320; scale 2^65.7 / 2^130)
Antipodal zero-sum padding: B(s,T) = {z^s, z^{s+1}} u (N/4-1 antipodal pairs),
|B| = N/2. Each antipodal pair sums to 0, so e_1(B) = (1+z) z^s. Pairwise
differences = (1+z) z^t (z^k - 1), certified by G = {z, 1+z} u {z^k-1 : 1<=k<N},
|G| <= N+1 = O(N) bases. |F| = N * C(N/2-2, N/4-1): 2^65.691 (N=128), 2^130.183
(N=256). Admissibility respected: uses only mu_N cyclic structure + y+(-y)=0, NO
prefix-map fiber counts. Verified: antipodes, e_1 formula, every difference
factorization, base count (F_17 toy, all PASS).
