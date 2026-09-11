# Two Necessary Guards

## Singular Centre Count Is Not Coordinate Count

Use the F97 degree43 actual-anchor carrier in the required
[degree ledger](../polynomial_carrier_inner_projection_degree_ledger/controls.md).
After seven anchors, its image has degree36 in P3 and normalization degree1.
The next centre has b=12 branches and inner degree mu=12.
Its charge binom(23,2)=253 fits G=binom(34,2)=561.

The centre-count bound for mu>=12 is floor(561/binom(12,2))=8.
But10 ACTUAL coordinates remain over this one centre. Thus multiplying
the centre count by nu=1 would be a false coordinate bound. The proved
branch-weighted bound is floor(561/21)=26, which retains all10.
This is a shared-carrier obstruction to a transfer shortcut, not an
official high-agreement MCA counterexample.

## Characteristic Cannot Be Dropped

In characteristic3, the degree9 rational curve

    [1:X:X^3:X^9] in P3

is nondegenerate and smooth at every finite parameter. For ANY finite a
over the algebraic closure, the inner projection has sections
X-a, X^3-a^3, X^9-a^9. Put u=X-a and remove the full fixed factor u.
Frobenius gives the child system[1:u^2:u^8]. Its image field is Fbar(u^2),
so its normalization degree is2, not1. Every finite point is therefore
a nonbirational inner centre.

This infinite family contradicts a characteristic-free finiteness claim,
but not the proved p>d theorem: here p=3,d=9. The algebraic Frobenius
identity, not a finite sample of centres, establishes the control.
