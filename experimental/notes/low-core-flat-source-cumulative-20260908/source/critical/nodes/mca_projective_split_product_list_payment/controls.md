# Small exact controls and their limits

All polynomial controls use F_7, V=span{X}, J=2 and exponent 3.
They are not canonical rank-eleven MCA sources or prize witnesses.

1. x,y in V, x*y^3=X^4 has six pairs and ONE projective class.
   On all seven coordinates, choose the mu=1 pair on X=1,2,3 and
   the mu=2 pair on X=4,5,6; the received pair at zero is (0,0).
   Exactly two pairs have four joint agreements, saturating floor(Q)=2.
   This rejects charging one pair per class or forgetting the common zero.
2. x in 1+V,y in V, x*y^3=(1+X)*X^3 has THREE actual pairs
   in one projective class. The one fixed affine scale leaves three cube
   roots for the other. The factor m in this mixed case is necessary.
3. x in V,y in 1+V, x*y^3=X*(1+X)^3 has one pair. With both
   in 1+V and product (1+X)^4 there is again one pair.
4. x=1/X+aX,y=bX, x*y^3=X^4+X^2 has three original polynomial
   pairs (aX,bX). Clearing X gives (1+aX^2)*(bX)^3=X^5+X^3.
   The transformed pole at zero is not grounds for puncturing original
   coordinates; the all-pair affine count already includes these pairs.

`verify.py` uses polynomial coefficient multiplication. `verify_audit.py`
independently tests evaluations at all seven field points: degrees <=5
make these identity tests exact, not probabilistic. The audit also checks
the projective degree formula by finite differences of its Hilbert function,
using Pascal binomials, and independently reconstructs the finite ledger.
These checks are not proofs of finiteness, the embedding or its intersection
degree; those are hand arguments in `projective_fiber.md`.
