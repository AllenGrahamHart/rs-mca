# First Excess Core Flat Or Balanced Bases

Status: PROVED. Fix an actual rank-s polynomial space of degree <K on
N>K distinct nonzero evaluations H, s>=3. Set D=N-K and

    P_s(D,K)=product_(i=0)^(s-1)(D+K-i*(K-1)/(s-1)).

Either the ordered basis count is at least P_s, or there exists a
LOWEST rank t in 1..s-2 having a complete H-flat G of size b>N/(s-t).
The chosen G is spanned by its H-points, and

    b<=K-s+t,
    every rank-i H-flat has <=floor(N/(s-i)) coordinates for 1<=i<t.

These lower-rank coordinate caps may be intersected with any other proved
density or polynomial root caps. G need not maximize density. The two
alternatives can overlap. This selects a flat in the same actual core,
not a received-word quotient, original-label census or numerical heuristic.
