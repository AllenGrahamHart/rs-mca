# Guards And Small Controls

## Why maximal dimension is necessary in the proof

The root-ball argument initially gives finitely many affine cosets, not
one global parametrization. Their number could be very large. Dimension
four forces a whole four-dimensional coset and forces every valuation of
alpha to be divisible by three. Monicity then proves that the SAME model
covers all other nonsingular bounded pairs. Do not omit that final step
or apply the conclusion merely to a sampled finite family.

For valuation data summing to zero, `deg D=3+sum floor(a_v/3)` is
strictly below three unless all residues modulo three are zero.
The finite controls include negative valuations, where truncation toward
zero in place of floor would give a false dimension.

## Exceptional projective lists are real

Consider the nodal parametrization

    Phi=(z^2-1)*(z-T),
    Psi=(z^2-1)-T*Phi.

It has Delta=1. Every degree-three eta gives outputs of degree <=10.
At finite T, z=1 and z=-1 both map to the singular pair (0,0), so
one-element lists cannot be assumed. At infinity, the degree-ten
homogenized output is `(0,-z^3)`. Over F_7 it has a fiber of size three.
The homogeneous degree-five Delta vanishes at infinity, even though its
affine polynomial is constant. Ignoring infinity would lose this case.

The rational projection 1/X has its infinity fiber at the original finite
coordinate X=0. The difference section T^2-1, homogenized to degree
three, pulls back to `X-X^3`; its three zeros over F_17 include X=0.
Counting only affine T zeros would miss that collision coordinate.

## No received-word descent

Distinct original coordinates in one projection fiber may carry different
received pairs and different permitted lists. The proof sums their slots
separately. It only bounds the size of each projection fiber by h. q zeros
outside complete cores are assigned empty lists, not removed from the
original domain/defect budget. These scope restrictions are hand-audited,
not inferred from finite-field toy examples.

## Two exact interval budgets

The full strip's smallest joint agreement and largest height do NOT have
a positive Johnson denominator together. The two printed interval budgets
do. This failure is an arithmetic-envelope limitation, not an unsafe
source. The coefficient dimension <=3 branch uses the old weighted
bound; the new 1251 cap is claimed only for dimension four.
