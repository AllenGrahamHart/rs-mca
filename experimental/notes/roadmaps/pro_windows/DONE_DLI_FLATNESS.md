# proof: DLI-flatness EXACT reduction + resultant-survivor conditional (Pro, verified)

## Lemma 1 — EXACT counting identity (PROVED, orthogonality; VERIFIED)
rho_j(M) = q^{L_j} |Z_j(M)| / U_j(M), where Z_j(M) = { d in prod_y D_y : A d = 0 } is the
set of bounded-coefficient kernel skews (A = the L_j x |Y| odd-evaluation matrix). Proof:
B_j = q^{-L} sum_d sum_lambda psi(lambda . Ad); additive-character orthogonality collapses
the lambda-sum to 1_{Ad=0}, so B_j = |Z_j|. VERIFIED: ternary |Z_j|=81 (rho 3.568), signed
|Z_j|=16 (rho 18.06) -- exact match to the harness B-values. So DLI-flatness is EXACTLY a
bound on the kernel-skew count.

## The remaining obligation (RES, the conditional 'C')
For upper flatness (sufficient for the primitive-core <= 2^122), prove uniformly in the
central profile M:
    |R_j(M)| + 1_{0 in prod D_y}  <=  q^{kappa_j} * U_j(M)/q^{L_j},   sum_j kappa_j = o(t),
where R_j(M) is the RESULTANT-SURVIVOR set (proved to contain Z_j\{0}):
  d != 0 with support >= L_j+1 (Vandermonde), p | gcd_r Res(X^N+1, Q_{d,r}) (norm gate,
  every imposed odd r), not in the killed cyclotomic/coset class. Then rho_j <= q^{kappa_j},
  prod_j rho_j <= q^{o(t)}. (Absolute sup-version additionally needs the matching LOWER
  fibre estimate |Z_j| >= q^{-kappa_j} U_j/q^{L_j}.)

## SCOPE refinement (zero-atom, VERIFIED necessary)
The unconditional 'A' over "all central M" is LITERALLY FALSE if singleton-zero domains
D_y={0} are allowed: then U=1, rho_j = q^{L_j}, eta_j = L_j, sum = t (VERIFIED). Correct
rule = RANK CHARGING: zero atoms cost exactly L_j - rank(A_eff); a single zero atom costs
<= 1 (O(34) over levels = o(t)), but Omega(L_j) rank loss breaks flatness. So the central
measure must EXCLUDE/charge singleton-zero (and near-rank-deficient) profiles.

## Fixed-lambda refutation (VERIFIED)
|F_M(lambda)| <= 1 (normalized local char sum), so one nonzero lambda contributes <= 1 to
rho_j => log_q rho_j <= log_q 2 = O(1). An Omega(L_j) deviation CANNOT come from a fixed
lambda -- only from q^{Omega(L_j)} near-peak frequencies = aggregate kernel-skew mass. This
confirms the obstruction is the RES count, not any single frequency.

## Empirical support (this session): eta* flat, rho_j -> 1.0000 at scale (ternary + signed
0.019 at mu_32 decreasing) = exactly RES with tiny kappa_j. The remaining PROOF is the RES
counting bound.
