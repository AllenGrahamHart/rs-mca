# PRO THREAD T7 — "PETAL-CHARGE" (fresh window)

*Self-contained. The P5 source. Distinct from E22 (verified): a FAMILY-level
chargeability theorem, not a pointwise covariance. The shared terminal is proved.*

## Setting
L1 coset-chart full-petal residue bridge. Missed-core defect d, petal size ell,
excess c=d-ell. The residue-line kernel K_{I,d}=ker(pi_{>d} R_{I,d}); PROVED
(Lemma 13, in-regime d<=(t-1)ell-1): dim K_{I,d}<=c+1. Cofactor coordinate
A_i(F)=(W_{D,I}-c_i F)/L_{T_i}, deg A_i<=c; the cofactor map is injective on kernel
points, so ALL c-dependent growth is confined to V_c={deg<=c}.

## What is proved (black boxes)
- **q_cofactor_normal_form (T2, PROVED):** a mu_M-isotypic (X^e G(X^M)) cofactor
  converts to a full-fiber (paid quotient) locator. So charged templates finish
  automatically.
- **Lemma 13:** dim K_{I,d}<=c+1 (in-regime).

## What is NOT enough (verified — do not retry)
Dimension-excess ALONE forces nothing: the affine family A_c={1+X+sum_{k>=2} a_k X^k}
has dim c-1 (unbounded) but no member is mu_M-covariant off a bounded tail (support
in classes 0 AND 1 mod M). So "large dim => quotient pullback" is FALSE. The
chargeability must use squarefree-realizability + the residue-kernel equations.

## The ask (target: petal_cofactor_chargeability / P5-CL)
> Prove: for every squarefree-realizable cofactor family Z in the residue-kernel
> chart, EITHER (charged) A_i(Z) lies — after bounded tail ops — in a paid
> quotient/coset/signed/antipodal/cyclotomic/low-defect template X^e G(X^M) (which
> q_cofactor_normal_form then finishes), OR (uncharged) the PRIMITIVE PROJECTION has
> bounded dimension: dim Pi_primitive A_i(Z) <= B_pet, with B_pet ABSOLUTE
> (independent of c,d,ell,t,q,n).

Then uncharged families have <= q^{B_pet} points; summing over charts (M=O(log n))
keeps the exponent c-INDEPENDENT: total uncharged <= 2^M poly(M) q^{B_pet}=n^{O(1)}.

- **(A)** Prove the chargeability decomposition. Lever: the residue-kernel equations
  (not just dimension) constrain the realizable families; sparse-coefficient
  (quotient-pullback) directions are charged, the rest have bounded primitive rank.
- **(B)** an in-regime family with c->inf and dim Pi_primitive A_i(Z_c)->inf, not
  quotient/signed/cyclotomic chargeable — refutes the c-independent ledger.
- **(C)** conditional on a clean bound on the primitive residue-kernel directions.

Downstream: petal ledger -> petal_excess_induction -> worst_word / list pricing.
