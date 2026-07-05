# proof: m720 norm-gate — structural height discharge, conditional (Pro P4, verified)

## Theorem P4-HB (Pro P4)
K=Q(zeta_n), O=Z[zeta_n], row F_q, q=p or p^2, n|q-1. For an anchored 2h-support
R, C_R=prod(X-x); S_R = monic deg-h matching the top h coeffs; E_R=S_R^2-C_R;
O_j(R)=[X^j]E_R; cleared integers A_j(R)=2^{4h-2}O_j(R) in O (banked x83). Then:
a non-toral survivor => all A_j(R) ≡ 0 mod P (P|p). If all A_j=0 in K, the char-0
classification (X24) says R is full-fiber/toral/paid (contradiction). Else some
A=A_j != 0 with p | N_{L/Q}(A); if the height bound |N(A)| <= B^{[L:Q]} < p holds,
a nonzero integer < p can't be divisible by p — contradiction. So NO anchored
non-toral survivor. Equivalently p ∤ D_pt(n,h) (or the conservative D(n,h)).

## Verified height constant
Crude archimedean bound (recurrence T_r): log2 B_h — h=7: 71.9, h=13: 167.3,
h=20: 290.7 (VERIFIED, < 291 as Pro states). So the gate closes any official case
where the nonzero obstruction lies in a field L with 291*[L:Q] < log2 p.

## Remaining obligation
The full cyclotomic degree [K:Q]=phi(n) is FAR too large for the crude bound. The
missing input is a DEGREE/CONDUCTOR COMPRESSION lemma: every non-toral anchored
obstruction relevant to h<=20 lives in a much smaller field L (or has much
smaller norm). ALTERNATIVELY: the C2 per-row GCD certificates gcd(p, D(n,h))=1
for the official p-values. Either discharges m720 without census.
