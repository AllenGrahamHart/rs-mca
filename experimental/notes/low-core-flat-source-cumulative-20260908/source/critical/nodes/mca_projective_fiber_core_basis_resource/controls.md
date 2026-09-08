# Small Source Controls

All fields here are F_13. These are controls for a hand proof, not
large-row numerical evidence or a claim of an exhaustive field search.

## Saturated Fiber And Distinct Slopes

Let G=X(X-1)(X-2), V=span{1,G,XG}, K=5. The fiber A={0,1,2}
has size a=3=K-s+1. Set u=v=0 on H={0,1,2,3,4,5}, put (u,v)=(0,1)
at 6 and (-1,1) at 7, and choose zero explanations for slopes 0 and 1
on H union their respective defect. Both supports have m=7 and raw=1.
They are bad in the FULL degree-<5 pair code: a second polynomial
vanishing on all six core points cannot also match the sole defect.

There are 60 ordered V-evaluation bases on H, hence 240 independent
ordered incidence tuples for each support. The two tuple sets are disjoint.
The generic lower core count is b(6)=54, not an equality assertion.

## Remaining Degree Excess Cannot Be Ignored

Let G=X(X-1), V=span{1,G,X^2G}, K=5. Now a=2 and e=1. On
H={0,2,3,4,9,10}, the outside restriction W/G is span{1,X^2}.
Its five outside points give 16 independent ordered pairs, exceeding
the correct P_e(5)=15 but below the unsupported e=0 count 20.

There are 48 ordered full bases with exactly one inside point and 60
with none, giving 108 core bases and 432 one-defect tuples. These two
classes are disjoint. This illustrates both the legitimate addition at
the CORE stage and the failure of a free outside-independence premise.

## Universal And Nonuniversal Carrier Zeros

Multiply the first V by X-12 and use K=6. With its original six-point
core H and sole defect at 12, the carrier-zero point is nonuniversally
agreeing: v(12)=1. It remains an actual independent defect. The source
still has 240 tuples; deleting the point would delete a real label.

Instead take H={0,1,2,3,4,12}, with u=v=0 there and sole defect at 6.
This violates g=0. Only 18 core bases and 72 completed tuples exist,
below the false g=0 lower count 4*b(6)=96. The hypothesis is necessary
for the printed formula and is not silently replaced by basepoint-freeness.

## Exact Scalar Controls

The primary checker tests 645 small parameter combinations, retaining
the interior kink in the minimum. The independent checker reconstructs
core counts by determinants rather than Gaussian rank. Finite floors are
checked using fractions and independent integer cross products; all eight
off-by-one endpoint mutations are rejected. All checks use explicit
exceptions and remain active under Python -O.

The analytic all-J derivative and convexity signs are checked exactly.
No raw-margin sample, finite fiber scan or endpoint-only extrapolation
is used to prove the universal assertions.
