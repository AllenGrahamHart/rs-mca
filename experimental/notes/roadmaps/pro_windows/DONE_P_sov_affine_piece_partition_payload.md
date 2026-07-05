# proof: sov grid-sum — trace-flat gate required (Pro P3, verified). Route history:
# affine-piece REFUTED (P3 prior), grid-sum FALSE for trace char (this pass).

## Pro P3 finding (VERIFIED): grid-sum FALSE as stated for the canonical trace char
Official row F=F_{17^32}, H=mu_512, C=RS[F,H,256]. Canonical psi(x)=exp(2pi i
Tr_{F/F17}(x)/17). Frobenius/LTE pairing: Tr(zeta^j)=0 unless 32|j (j 17^i pairs
with +256 since v_2(j(17^t-1))=8 for t=2^{4-r}, zeta^256=-1). VERIFIED: exactly
496 of 512 grid points are trace-ZERO; the 16 nonzero are mu_16=F_17^* (j div 32).
So on Gamma=trace-zero (density 496/512), the cell Omega_Gamma(h) has
ψ(-sum x)=1 for ALL P, giving |sum| = C(496,h): at h=21 density 0.506 of the full
h-subset space (unconditioned S_21(1)/C(512,21)=0.485). NO cancellation — a
positive-density trace-flat family.

## The fix: a TRACE-FLAT / SUBFIELD-NORM paid gate
The paid ledger must include: exists a!=0 with x->Tr(ax) constant on a positive-
density free-root cell. This gate is NOT small (density 0.506 at h=21), so it must
be explicit — it is NOT covered by "quotient/dihedral/norm" as previously stated.

## Corrected target P3'
Prove the multiplicative-grid character-sum bound ONLY after removing trace-flat/
subfield-norm gates IN ADDITION to quotient/pullback/dihedral gates; then a Lane-1
power-sum bound |sum_{x in Gamma} psi(jax)| <= B (1<=j<=h, 17∤j) on the residual
cells gives |sum_{P subset Gamma}| <= [u^h](1-u)^{-B}(1-u^17)^{-(|Gamma|-B)/17}.
The a=1 trace-flat cell has B=|Gamma| (outside any cancellation regime) — hence it
MUST be a paid gate, not a cancellation remainder.
