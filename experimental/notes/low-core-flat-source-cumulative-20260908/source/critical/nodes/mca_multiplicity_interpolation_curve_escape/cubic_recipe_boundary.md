# Exact boundary of the degree-three full-kernel recipe

Status: PROVED limitation of the sufficient dimension criterion, not a
counterexample to a source bound. Put n=1048576+J, w=J-1 and
A=J+67472-T. For EVERY integer

    9981<=J<=169999, T>=1 with A>=1, r>=1,

the degree threshold g0=4 fails this node's strict criterion:

    Phi_w(r*A)-Phi_w(r*A-4*w)-n*binom(r+2,3)<=0.       (FENCE)

Thus varying multiplicity or the positive raw cutoff cannot make THIS
whole-kernel dimension argument force gcd degree <=3 on this interval.
Other interpolation spaces, sharper condition-rank bounds, additional
source structure and higher-degree covers are not excluded.

## 1. A convex shell count

Reindex the second sum in the definition of Phi. Exactly,

    Phi_w(d)-Phi_w(d-4w)
      =sum_(i>=0) min(i+1,4)*max(d-i*w,0).             (1)

It increases with d. Therefore T=1 is the most favorable permitted
cutoff; failure there implies failure at any larger T.

Fix r and set A=J+67471. Each summand in (1) is a nonnegative multiple
of the maximum of an affine function of J and zero. Only finitely many
summands can be nonzero on the closed interval. Subtracting
(1048576+J)*binom(r+2,3) leaves a convex function of J.
Its maximum is consequently bounded by its endpoint maximum.

## 2. Four small multiplicities

At T=1, the exact gaps at the two endpoints are:

    r       J=9981           J=169999
    1       -122645          -846161
    2       -276             -3384644
    3       -651530          -8331938
    4       -3134964         -16793548.

They are strictly negative. Equation (1) or direct monomial counting
gives this finite integer table; convexity covers every intermediate J.

## 3. All larger multiplicities at once

For the decreasing nonnegative function max(d-w*x,0), its sum at positive
integer x is bounded by its integral from zero. Hence (1) is at most

    4*d+2*d^2/w.

Divide by r^2 and write d=rA. It suffices to prove

    2*A^2/w+4*A/r < n*(r+3+2/r)/6.                   (2)

The left side decreases with r; the right side increases for r>=5.
At r=5, after multiplication by 5w, (2) is equivalent to

    7*n*w-10*A^2-4*A*w>0.

Its endpoint values are 10870785140 and 724689480710 respectively.
Therefore every r>=5 has negative gap at both endpoints. Applying
the fixed-r convexity from section 1 proves (FENCE) for all those r,
without enumerating multiplicities or source words.

## 4. Sharpness as a recipe boundary

At J=9980,T=1,r=2 the gap is 88>0; at J=9981 it is -276.
Thus 9981 is a genuine boundary for this criterion in the printed range,
not just the end of a bounded scan over r. The resource cost and factor
payments at T=1 are NOT thereby affordable at 9980.

At T=125,r=2 the gap is 3618424-364J on 9822..9941.
It is 264 at 9940 and -100 at 9941. The finite consumer now supplies
a complete source payment through 9940, separately from this method fence.

Neither a negative dimension lower bound nor failure to escape a curve
proves that an unsafe MCA source exists. Both prizes remain open.
