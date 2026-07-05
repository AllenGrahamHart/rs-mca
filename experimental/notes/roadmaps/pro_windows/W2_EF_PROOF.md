# proof: interleaved_floor_import (Pro W2, verified) — the Paper D floor is Weil-functorial

The singleton multiplication-slice interleaved witness IS forced onto the
extension-pole divisor; the Paper D simple-pole/list-window floor survives Weil
restriction. No S9 class exists within the essential-image (multiplication-slice,
common-support) hypotheses — which Pro's prior round already PROVED the witness
satisfies.

## Construction (verified)
D subset B, |D|>=2; K in {E,F}, C_K = RS[K,D,kappa]. For a witness in the
multiplication-slice essential image (P in K[X]_{<kappa+1}, U:D->K, support S,
|S|=a>kappa, P=U on S) and any pole alpha in K\B:
  f_alpha(x) = U(x)/(x-alpha),  g_alpha(x) = -1/(x-alpha),  z = P(alpha).
Then on S,  f_alpha + z g_alpha = (P(x)-P(alpha))/(x-alpha) = Q_alpha(x), deg < kappa
(VERIFIED numerically over F_101^2): the line is C_K-explained on S (CA/MCA-bad
at a). Noncontainment: H(X)=(X-alpha)G(X)+1 has deg<=kappa and H(alpha)=1!=0, so
g_alpha is not explained on >kappa points. Because D subset B, coordinate
expansion is exact (Phi(C_K)=C_B^e) and preserves containment/noncontainment
support-wise, so the SAME holds for the interleaved image Phi(f)+M_z Phi(g).

## The pole floor
alpha in K\B is a genuine extension pole; Paper D's extension-pole corollary
(Omega_0 = F\B, |D|>=2) at L=1 gives numerator ceil((|K|-|B|)/(|K|-|B|+kappa)) = 1
for |K|>|B| (verified). So the singleton meets the extension-pole divisor D_E.

## Scope check (the only Paper D step needing it)
The collision-count step P_i(alpha)=P_j(alpha) (<= kappa roots) is unchanged
under Weil restriction (Phi(P_i(alpha))=Phi(P_j(alpha)) iff P_i(alpha)=P_j(alpha)),
and is VACUOUS for the singleton (no pairs i!=j). The proof uses only the support
diagonal + the proved multiplication identity Phi(zg)=M_z Phi(g). QED.

Discharges interleaved_floor_import => ef_pole_free_cycle_exclusion =>
ef_full_orbit_pole_forcing => ef_ru => f1_full_field_pole_forcing.
