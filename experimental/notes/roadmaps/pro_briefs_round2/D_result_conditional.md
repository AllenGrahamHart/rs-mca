# conditional: b2b_primitive_core (Pro Brief D, route C — verified algebra)

## Predicate node
- `pcf_norm_gate_flatness`

## Claim
The primitive-core count #{primitive t-null B : t+16 <= |B| <= n/2} <= 2^122
follows from the single per-level norm-gate flatness estimate PCF.

## Proof (Pro Brief D; the chain is elementary and verified)
G_j(M) = {zero skew} u {nonzero bounded-coeff skews, support >= L_j+1, whose
folded resultants all carry the fixed prime q}. Proved inputs give
{valid skews} subset G_j(M) (Vandermonde threshold + simultaneous norm gate).
ASSUME PCF: |G_j(M)| <= q^{-L_j+eta_j} U_j(M) for every central profile.
Then B_j(M) <= |G_j(M)| <= q^{-L_j+eta_j} U_j(M), so rho_j = B_j/(q^{-L_j}U_j)
<= q^{eta_j}; prod_j rho_j <= q^H, H = sum eta_j; hence
C_central <= q^{-t+H} W_cen. With sum_j L_j = t and W_cen <= 2^n, the crude
sufficient budget is H <= (122 - n + t log2 q)/log2 q = 122/256 at the prize
row. So the core reduces to the ONE estimate PCF.
