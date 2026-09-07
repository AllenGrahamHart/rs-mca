# The remaining cubic has a finite singular point and a (2,3) parameter

Status: PROVED reduction, 2026-09-07. No payment of this last class is
claimed. Keep the exact source and N from `cubic_obstruction.md`.
The logical input is its one-place conclusion proved in sections 1--4,
before its final affine-singularity refinement. The argument below then
proves that refinement and the normal form, not conversely.

For 7117<=J<=8655, if N>B, the cubic in that theorem may now be
taken to have its unique singular point in the AFFINE plane. It is
defined over Kappa=F(X), not just an auxiliary field. There exist

    f_s in Kappa^2, lambda in Kappa,
    P,Q in Kappa^2 linearly independent over Kappa,

such that all but at most 65 represented LOW pairs have the form

    f(tau)=f_s+(tau^2-lambda)*(P+tau*Q),
    tau in Kappa, tau^2!=lambda.                       (NF)

All original pairs remain polynomial of component degree <J in the
SAME affine carrier. Their complete cores and original labels remain
unchanged. The displayed tau, f_s, P, Q and lambda are RATIONAL in X;
their heights or denominators are not assumed negligible. The extra
one exceptional pair is f_s if it is represented. The other <=64 are
off the cubic. Distinct nonsingular pairs have distinct tau.

## 1. Remove the singularity-at-infinity case

The required finite consumer inherits the moving-projection theorem
from the existing jet supplier. A one-place cubic singular at infinity
is polynomial in a linear projection x=A*a+B*b. Its primitive top
binary form is c*(A Y+B Z)^3. The full-kernel weighted bound forces
h=max(deg A,deg B)<=17580 on this interval. Its group gain is at
most 71875471818343284. With the single resource/near and <=64
off-curve pairs, the total is at most

    117918672306944736+64*981604
      =117918672369767392,

below the already paid alternative 255637082913634099. Thus N>B
rules this case out. The remaining geometric cubic has its singular
point finite and its unique point at infinity smooth.

## 2. Complete the square over the original function field

Choose Kappa-linear coordinates x,y with the point at infinity
[0:1:0]. The highest binary part is c*x^3, c!=0. Smoothness at
infinity makes the coefficient of y^2 nonzero, as in the jet supplier's
direct coefficient test. In characteristic >3, completing the square
in y gives

    y_1^2 = R(x), deg R=3.

An affine singularity is exactly a repeated root of R. Its repeated
root alpha is in Kappa: in the double-root case gcd(R,R') is linear,
and in the triple-root case alpha is recovered from the x^2 coefficient
by division by three times the leading coefficient. Write

    R(x)=a*(x-alpha)^2*(x-alpha+b), a!=0.

The singular point is (alpha,0), hence its original coordinates f_s
also lie in Kappa^2. Put z=x-alpha. Away from z=0, define

    tau=y_1/z.

Then tau^2=a*(z+b), so, writing lambda=a*b,

    z=(tau^2-lambda)/a,
    y_1=tau*(tau^2-lambda)/a.

The inverse affine coordinate change is f=f_s+u*z+v*y_1 for
independent u,v in Kappa^2. Taking P=u/a, Q=v/a proves (NF).
Conversely every tau with tau^2!=lambda gives a nonsingular point
and is recovered by the ratio above. At most the one singular pair
was excluded. If lambda!=0 it is nodal; lambda=0 is cuspidal.
No square root or extension of the challenge field is needed.

## 3. What remains to count

The normalization parameter is not a linear projection of the pair:
its two independent coordinate degrees are two and three. This is
precisely why the new moving-projection graph theorem does not close it.
One must count those rational tau for which (NF) lies in the original
bounded common carrier and has a large COMPLETE joint core. Applying
scalar LIST to tau as though it were a degree-<J polynomial would
discard unproved denominator and degree claims.

For example, even a harmless rescaling can introduce a parameter pole:
with f_s=0, lambda=0, P=(X^2,0), Q=(0,X^3), the rational
tau=1/X yields the polynomial pair (1,1). This does not prove an
intrinsic pole obstruction; it shows why a chosen parametrization
cannot be used without its actual degree contract.

This is a proved explicit reduction of the residual case. It is not
a conjecture that the case exists, a proof of its payment, a new
conditional node, or an extension of the paid 4801..7116 strip.
