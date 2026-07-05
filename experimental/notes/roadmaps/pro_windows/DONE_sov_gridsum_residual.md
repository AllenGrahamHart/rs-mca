# proof: sov_gridsum_residual — Lane-1 PROVED; a 2nd paid gate needed (Pro T4, verified)

## Counterexample (VERIFIED): trace-flat gate ALONE is insufficient
F_65537, H=mu_65536, h=21, Gamma={1,...,1024} (an additive ARC). The cell has
|S_h(Gamma)|/binom(1024,21) >= sinc(pi/64)^21 > 0.9916 (actual 0.99177, VERIFIED) —
near-MAXIMAL bias, NO cancellation. It is prime-field (not trace-flat), non-subfield,
non-quotient (not negation-invariant), non-dihedral, and density 2^-126.3 > 2^-128
(not negligible). So "non-trace-flat => cancels" is FALSE: an additive Bohr arc is
far from trace-flat yet almost maximally biased. Non-constant trace != cancellation.

## Lane-1 theorem (PROVED, VERIFIED)
If the residual cell Gamma (size M) satisfies the power-sum bound
max_{1<=j<=r, p0∤j} |sum_{x in Gamma} psi(-jax)| <= B for every nonzero a, then
|sum_{P subset Gamma,|P|=r} psi(-a sum P)| <= [u^r](1-u)^{-B}(1-u^{p0})^{-(M-B)/p0}
(Euler product + Newton power sums; VERIFIED F_101). Fourier-duality handoff:
|O(Omega)| >= q/(1 + (sum_a CharBudget^2)/|Omega|^2), so the value-set conclusion
follows once sum_a CharBudget^2 = o(|Omega|^2).

## Corrected obligation (this node)
sov_gridsum_residual = (a) a NEW paid class large_power_sum/Bohr-flat (remove
additive-arc / Fourier-biased cells — the general condition subsuming trace-flat is
"small power sums P_j for all j,a") + (b) the residual power-sum bound
sum_a CharBudget^2 = o(|Omega|^2) via the proved Lane-1 engine. The affine-arc cells
are the new paid class; the truly Bohr-flat residual cancels by Lane-1.
