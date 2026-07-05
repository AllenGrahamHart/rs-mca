# proof: q_cofactor_normal_form — PROVED (Pro T2, verified)

The SHARED TERMINAL algebra of e22 + petal (a mild generalization of the proved
kernel-invariance/fiber machinery to the character-twisted case e != 0).

## The normal form (VERIFIED)
D=mu_n, M|n, char∤n. Projectors Pi_{M,e}f(X)=(1/M) sum_{eta in mu_M} eta^{-e} f(eta X)
are orthogonal + complete. EQUIVALENT (VERIFIED F_37, mu_12, M=4):
  f(eta x)=eta^e f(x) for all eta in mu_M  <=>  Pi_{M,e}f=f  <=>  all coeffs deg ≡ e mod M
  <=>  f(X)=X^e G(X^M).
Off a bounded tail B: the retained zero set is mu_M-invariant => union of full
x->x^M fibers => L_{T\B}(X)=prod_{z in Z}(X^M - z), squarefree (char∤n). This is
the terminal both e22 (factor manifest) and petal (paid quotient ledger) consume.

## The naive sharing is REFUTED (VERIFIED)
"large dimension + quotient-compatible constraints => scalar pullback X^e G(X^M)"
is FALSE. Counterexample F=P(X^M)(A(X^M)+X^r B(X^M)) (1<=r<M, A,B != 0): it IS
full-fiber divisible (prod(X^M - z_j) | F), dimension grows with deg A,B, BUT its
coefficient support lies in TWO residue classes mod M (0 and r) — NOT one X^e
G(X^M). VERIFIED (F_37: (X^M-z1)|F, support classes {0,1}). Quotient-compatible
constraints PRESERVE the isotypic decomposition; they do NOT SELECT a single
character. Character selection is additional SOURCE data.

## Adjudication: shared terminal, SEPARATE sources
- E22 is a POINTWISE covariance-extraction problem: the sunflower must supply
  E22-COV(i): H_i(eta x)=eta^{e_i}H_i(x) off B. Then the normal form gives the
  factorization.
- P5 is a FAMILY-LEVEL chargeability problem: after subtracting paid isotypic
  templates, the primitive projection of each squarefree-realizable family has
  dim <= B_pet. Then charged templates convert via the normal form.
These are NOT the same source lemma. Do NOT merge the two open leaves.
