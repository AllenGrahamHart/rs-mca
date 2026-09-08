# The same gap bounds the full multiplicity-kernel gcd

Current scope: the finite consumer and full-kernel child now price the
entire 9527..9821 tail in `double_point_cubic_tail.md`. The cover below
is an independent supplier; it does not depend on that later payment.
The factor-height and exception warnings remain essential interfaces.

Use the entire kernel E constructed in proof.md, not one selected
interpolant. Write d=r*A, ell=floor((d-1)/w). If for an integer g0>=1

    Phi_w(d)-Phi_w(d-g0*w)>n*binom(r+2,3),             (KESC)

then E is nonzero and its primitive gcd H over F(X)[Y,Z] has pair
degree h<g0. All counted rich pairs lie on H, except at most
(ell-h)^2<=ell^2 pairs. A constant gcd means all pairs are exceptions.
The gcd and each primitive factor have weighted degree <d.

Indeed the strict inequality gives dim E>Phi_w(d-g0*w)>=0. If h>=g0,
the Gauss/weighted-degree argument would place all of E in a space of
dimension at most Phi_w(d-h*w)<=Phi_w(d-g0*w), a contradiction.
This argument needs no irreducibility of the gcd.

Write a finite F-basis Q_i=H*R_i. The residual polynomials R_i have gcd
one and pair degrees <=ell-h. Any rich pair off H is a common zero
of all R_i, since every Q_i vanishes on it identically. If one R_i is
a nonzero constant, there are no exceptions. Otherwise fix a nonconstant
R_0 and choose an F(X)-linear combination R_1 of the residuals avoiding
each irreducible factor of R_0. Each avoidance condition is proper and
F(X) is infinite. Thus R_0,R_1 are coprime, and the same plane
intersection bound gives at most (ell-h)^2 common points. Singularity
and coefficient-component dimension are irrelevant to this finite count.

## KoalaBear tail consequence

For LOW_500, (n,w,A)=(1048576+J,J-1,J+66972), the finite consumer
prints the verified r=2,g0=4 gap through J=9821. Hence the FULL
double-point kernel has gcd degree <=3. It covers all LOW pairs except
at most 17^2=289 pairs on 8764..9821. On the subsequent tail
9527..9821, the bound can be sharpened to 16^2=256, since ell<=16.

The important changed interface is weighted_degree(H)<2*A, not <A.
The old simple-point cubic factor height bound is not inherited. No
affordability of the new cubic factor patterns is asserted without checking
their actual heights, exceptional counts and finite source payments.
This supplier proves a cover, not its affordability. The separately proved
consumer named above now pays that tail; neither prize is closed.
