# proof: petal ledger — conditional on chargeability lemma (Pro P5)

## Reduction (Pro P5, uses proved Lemma 13)
Full-petal chart (I,d), t=|I|, petal size ell, c=d-ell. Missed-core F=L_D injects
into K^sq_{I,d}. The cofactor coordinate A_i(F)=(W_{D,I}-c_i F)/L_{T_i} has
deg A_i <= c (in-regime d<=(t-1)ell-1), and the cofactor map is injective on
kernel points. Lemma 13: dim K_{I,d} <= c+1. So ALL c-dependent growth is confined
to the cofactor space V_c={deg <= c}. Classify cofactor directions, not locators.

## The missing bridge (P5-CL, the conditional)
Petal cofactor chargeability: exists absolute B_pet (indep of c,d,ell,t,q,n) s.t.
every squarefree-realizable cofactor family Z either (charged) has A_i(Z) in a
paid quotient-type family (exact quotient/coset pullback, low-defect quotient,
signed/antipodal, petal-coset/cyclotomic), or (uncharged) has dim A_i(Z) <= B_pet.
Algebraic signature of charged: quotient-pullback locators have sparse coeff
support (degrees divisible by the quotient modulus).

## Consequence (given P5-CL)
Uncharged families have |Z(F_q)| <= q^{B_pet}; summing over charts with M=O(log n)
gives total uncharged <= 2^M poly(M) q^{B_pet} = n^{O(1)}, exponent INDEPENDENT of
c. Falsifier: an in-regime family with c->inf, dim A_i(Z_c)->inf, not quotient/
signed/cyclotomic/petal-coset chargeable. Remaining obligation: prove P5-CL.
