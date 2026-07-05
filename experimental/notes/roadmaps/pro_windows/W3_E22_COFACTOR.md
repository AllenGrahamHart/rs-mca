# PRO WINDOW W3 — "E22-COFACTOR"

*Fresh window. Self-contained exact-factorization / algebra problem. The single
terminal of a clean 16-rung E22 reduction ladder (all other 46 nodes proved).*

## Setting
RS worst-word / E22 challenger pricing. A "touched petal" cofactor divisor comes
from the divisor constraints L_{T_i} | H_i (the locator L_{T_i} of support T_i
divides H_i). The support T_i has a "tail" B (a common part) and non-tail roots.
Dyadic local moduli M_i > t (t = nullity parameter). All roots are in mu_n.

## What must be proved (the terminal)
Provide the E22 cofactor factorization manifest: from the actual divisor
constraints L_{T_i} | H_i, exhibit
- ONE common tail B (shared across all touched-petal divisors);
- dyadic local moduli M_i > t with |B| < min_i M_i;
- for each touched petal, a quotient-value set Z_i; and
- the EXACT SQUAREFREE IDENTITY
    L_{T_i \ B}(X) = prod_{z in Z_i} (X^{M_i} - z)
  for the non-tail roots (i.e. the non-tail part of each touched-petal locator
  factors as a product of X^{M_i} - z quotient factors -- a dyadic/coset
  structure).
Then (via the proved e22_tail_removed_factor_manifest_soundness) this discharges
the common-tail invariance and closes the E22 staircase pricing ->
worst_word_challenger_pricing.

## The ask
- **(A)** Prove the factorization: from L_{T_i} | H_i (the divisor constraints of
  the E22 challenger family), show the non-tail locator factors as
  prod (X^{M_i} - z) with a common bounded tail B (|B| < min M_i) and dyadic
  moduli M_i > t. The structure to exploit: the E22 challengers are built from
  the moment-trade / square-shift construction (see the proved
  e22_two_class_exhaustion and the staircase parametrization); the cofactor
  divisor should inherit the X^{M_i} - z coset structure from the trade.
- **(B)** A touched-petal cofactor divisor pattern with NO common bounded tail or
  no exact quotient-factor identity -- would break the E22 pricing route.
- **(C)** Conditional on a clean structural hypothesis on the challenger cofactors.

Downstream: worst_word_challenger_pricing -> imgfib -> list_planted_arithmetic /
list_safe -> list_grand (the list side of the prize).
