# PRO THREAD T2 — "QUOTIENT-COFACTOR-GATE" (candidate SHARED: e22 + petal)

*Self-contained. A HYPOTHESIS that two open leaves are the same lemma. First task:
confirm or refute the sharing; then prove the shared statement (or each separately).*

## The two obligations that look identical
Both are about a COFACTOR polynomial on a multiplicative domain D=mu_n whose
"excess" structure is forced to factor through a power quotient x -> x^M.

**(E22) e22_mixed_petal_covariance.** For E22 mixed-petal sunflower challengers with
cofactor divisibility L_{T_i}|H_i (H_i = U L_{Z\C} - a_i L_{C\Z}), the sunflower
supplies, off one bounded tail B (|B|<min M_i), the mu_{M_i}-COVARIANCE
    H_i(eta x) = eta^{e_i} H_i(x)  for eta in mu_{M_i},
i.e. H_i(X) = X^{e_i} G_i(X^{M_i}) on the petal coordinate. (Divisor constraints
ALONE are insufficient — verified interpolation counterexample; a covariance/degree
property is load-bearing.)

**(PETAL) petal_cofactor_chargeability (P5-CL).** For the L1 coset-chart residue-line
kernel K_{I,d} (c=d-ell, dim <= c+1), every squarefree-realizable cofactor family
A_i(Z) subset V_c of dimension EXCEEDING an absolute B_pet is contained in a
QUOTIENT/coset/cyclotomic-pullback family (sparse-coefficient signature: coeffs only
in degrees divisible by the quotient modulus); the bounded-dim remainder is the
uncharged residual.

## The shared statement (the hypothesis to test)
> **Q-COFACTOR:** a cofactor polynomial on D=mu_n whose structure exceeds a bounded
> budget (covariance-forced, resp. dimension > B_pet) FACTORS THROUGH a power
> quotient x -> x^M (M | n, M > t): it is mu_M-covariant / a pullback G(X^M) off a
> bounded tail. The proved fiber machinery (fiber_locator_saturation:
> X^M - z | L_R iff the full fiber is in R; kernel_invariance_full_fiber_criterion:
> mu_M-invariance iff union of full fibers) then converts this to full-fiber
> (paid quotient) structure in BOTH settings.

## The ask
- **(0) Adjudicate the sharing:** are E22-covariance and P5-CL genuinely the same
  Q-COFACTOR lemma (a cofactor with excess structure is a mu_M-pullback), or do the
  two constructions (moment-trade sunflower vs coset-chart residue kernel) differ in
  a way that blocks a common proof? Be concrete about what, if anything, differs.
- **(A) If shared:** prove Q-COFACTOR uniformly (excess structure => mu_M-pullback
  off a bounded tail), so it discharges BOTH e22 and petal. The lever in both: a
  bounded-degree / bounded-dimension object satisfying "too many" quotient-compatible
  constraints must be a quotient pullback (a rigidity/completion argument), else its
  count/dimension would exceed the budget.
- **(B) If not shared:** give the obstruction, and prove each separately (E22
  covariance from the sunflower model; P5-CL from the coset-chart kernel).

If (A) succeeds it is a second shared gate (like the subfield-trace gate); I will
then encode Q-COFACTOR as one node feeding e22 + petal.
