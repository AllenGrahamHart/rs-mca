# Plane Multiplicities Bound Arithmetic Genus In Every Characteristic

Let Gamma be an integral plane curve of degree q over an algebraically
closed field, with multiplicities a_i at finitely many distinct points.
Blow up those points in P2. The surface S is smooth, its exceptional
curves E_i are disjoint P1's with O(E_i)|E_i=O_P1(-1), and the strict
transform is the integral Cartier divisor

    Gamma'=qH-sum a_i E_i.

Here a_i is the lowest total degree of the local equation. Substituting
y=xt in a blowup chart removes exactly x^a_i; this gives the displayed
strict-transform class without an ordinary-singularity assumption.

The blowup pi has pi_*O_S=O_P2 and higher direct images zero. Locally at
one centre this is the elementary two-chart Cech calculation with rings
k[x,t], k[t^-1,xt] and intersection k[x,t,t^-1]. Every intersection
monomial x^u t^v lies in the first chart if v>=0, and otherwise equals
(xt)^u*(t^-1)^(u-v) in the second. H1 is zero. The intersection of the
two chart rings is k[x,xt]=k[x,y]. Localization gives the same sheaf
calculation, and disjoint centres do not interfere.

Consequently pullback preserves the Euler characteristic of an invertible
sheaf. For L=O_S(-qH), the exact sequences adding jE_i have quotient
O_Ei(-j) and Euler-characteristic increment1-j. Summing gives

    chi(O_S(-Gamma'))=chi(O_P2(-q))-sum binom(a_i,2).

The divisor equation sequence yields

    p_a(Gamma')=binom(q-1,2)-sum binom(a_i,2).

Since Gamma' is integral and projective, H0(O_Gamma')=k and
p_a(Gamma')=dim H1(O_Gamma')>=0. Therefore

    sum binom(a_i,2)<=binom(q-1,2).                 (MULTIPLICITY)

This is the one-blowup genus calculation, not a characteristic-zero
resolution theorem. The exceptional-divisor Euler-characteristic method
can be compared with [Stacks 55.12.2](https://stacks.math.columbia.edu/tag/0CEF);
the needed local calculation and all increments are explicit here.
