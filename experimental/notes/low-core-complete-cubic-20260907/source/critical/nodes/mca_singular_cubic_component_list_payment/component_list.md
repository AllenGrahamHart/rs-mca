# Uniform per-component list count

Use the polynomial model of `component_model.md` on one three-dimensional
component. Set a=J+66972 and n=1048576+J. Each represented LOW pair has
at least a original joint agreements. Write ell for its parameter degree
and g for its identical joint-agreement coordinates. The model proves

    2<=ell<=floor((J-1-h)/3),
    0<=g<=G=J-1-h-3ell,
    deg E<=J-1-2ell+h.

Remove the g IDENTICAL agreement coordinates from this count, subtracting
them from both domain and required agreement. Constant nonmatching fibers
have empty lists. The slot budget on the other original coordinates is

    S(g)=2n+J-1-2ell+h-3g, agreement a-g.                (1)

There are at most deg E-g exceptional three-lists because all g removed
coordinates are distinct roots of E. This is why the last term is -3g,
not merely -2g. Distinct parameter polynomials agree on at most ell
coordinates. No projection fiber is merged and no receiver descent occurs.

For M distinct represented nonsingular pairs, choose exactly a-g accepted
coordinates per pair. Slot incidences and Cauchy--Schwarz give

    M*(a-g)^2 <= S(g)*((a-g)+(M-1)*ell),
    M <= S(g)*(a-g-ell)/((a-g)^2-S(g)*ell),             (2)

when the denominator is positive. The original pair set is finite; the
same follows from agreement >ell and the finite permitted lists.

## Bound g without assuming it equals its maximum

Put u=a-g and b=S(0)-3a=1896235-2ell+h>0. The fraction in (2) is

    F(u)=(b+3u)*(u-ell)/(u^2-(b+3u)*ell).

On a positive denominator its derivative has numerator

    -(b+6ell)*u^2-4*b*ell*u-b^2*ell <0.               (3)

The denominator increases with u on the relevant range because
2u>3ell. Hence the largest g, namely G, gives the largest fraction
and smallest denominator. At g=G the budgets are

    u=66973+h+3ell,
    S=2097154+4h+7ell.                                (4)

For the remaining d=7 source, 1301<=h<=4327 and J<=8655, so ell<=2451.
Enlarge the slot budget using h<=4327 and lower the agreement using
h>=1301. These are legitimate Johnson relaxations: its fraction
increases with S and decreases with u when u>ell, S>=ell and the
denominator is positive. We obtain

    u_0=68274+3ell,
    S_0=2114462+7ell.                                 (5)

The numerator S_0*(u_0-ell) is positive and increasing with ell>=0.
Its denominator is

    68274^2-1704818*ell+2ell^2,

decreasing for 0<=ell<=2451, since -1704818+4ell<0. At ell=2451,

    u_0=75627, S_0=2131619,
    denominator=494844960>0,
    numerator=155983351944,
    floor(numerator/denominator)=315.                 (6)

Thus all the denominators used above are positive, and EVERY
three-dimensional component has at most 315 represented nonsingular
LOW pairs. This is one uniform analytic envelope, not a scan over h,J,
parameter coefficients or source words.
