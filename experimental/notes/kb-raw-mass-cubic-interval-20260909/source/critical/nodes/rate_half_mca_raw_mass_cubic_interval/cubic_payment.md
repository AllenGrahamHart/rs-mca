# Every Irreducible Cubic At The Actual Double-Point Height

Assume the full-kernel gcd in proof.md is irreducible cubic. It occupies
the entire degree budget. At most256 represented raw<=50 pairs are
off it; its primitive weighted degree is <2*(J+67422).
Write base=12672029169970630 and L=981154 from basis_mass.md.

## Smooth, Multiple-Boundary And Infinity-Singular Types

The required finite relation consumer's cubic_tail_payment.md records
the general classification and its credited dimension theorems. Smooth
cubics and rational normalizations with at least two points over infinity
have LOW_500 pair count at most163774741769 on the unchanged row.
Irreducible but nongeometrically integral cubics have at most six rational
pairs. Their LOW_50 subsets obey the same bounds.

A unique-boundary cubic singular at infinity is a polynomial cubic in
its primitive linear projection. The ACTUAL <2A factor weight gives

    h<=floor((2*(J+67422)-1-3*(J-1))/3)
      =floor((134846-J)/3)<=41635<51391.

The credited height-51391 moving-projection pair cap223154201664 applies
even at LOW_500. After adding256 exceptions, each of these cases pays by
DIRECT; their largest total is231620667000586310<(C50).

## Affine-Singular One-Boundary Types

Let e be the projection-kernel dimension on V x V, not the degree gap d.
The required weighted theorem gives coefficient dimension r=ceil(e/3)
and the ALL-component pair cap

    M<=floor(2^e*3^(22-e-r)*((1048577-h)/(67423-h))^r). (WC)

The same carrier height theorem gives
h<=floor(9963/floor(10/(11-e))) for1<=e<11; e=11 has h=0.
The ratio increases with h and is >=3. For e=0 use3^22 directly.
For e outside{7,10}, DIRECT with256 exceptions has largest total
269761880886747862 at e=11, below(C50). This uses actual carrier
height, not an old factor-weight bound.

### e=7, Height At Most1550

At every nested depth1<=t<=50, the same theorem gives
M_t<=2^7*3^12*((1048577-h)/(67473-t-h))^3 for curve pairs.
The ratio increases with h. The same256 exceptions cover every nested
subset, so the complete-pair raw-sum bound in basis_mass.md allows

    S_t<=f(t)=(981104+t)
                 *(2^7*3^12*(1047027/(65923-t))^3+256).

Use CUM with all50 exact rational summands:

    floor(W/51+sum_(t=1)^50 f(t)/[t(t+1)])+134944
      =274861473951141154.                           (BIND)

The finite sum is a printed exact formula, not a fit or sample of sources.
Every selected defect, singular solution, off-curve pair and original near
allowance is included once. No chord approximation is needed.

### e=7, Height At Least1551

The generic component model, degree and list proofs in the required
component supplier apply with actual agreement a=J+67422. Let ell be
normalization parameter degree, g identical agreements. They give

    2<=ell<=floor((J-1-h)/3)<=2804,
    0<=g<=J-1-h-3ell,
    S(g)=2n+J-1-2ell+h-3g.

For u=a-g, the incidence fraction is S(g)*(u-ell)/(u^2-S(g)*ell).
Writing S(g)=3u+b, b=1894885-2ell+h>0, its derivative has numerator
-(b+6ell)u^2-4b*ell*u-b^2*ell<0. The denominator increases with u.
Thus largest g gives worst budgets

    u=67423+h+3ell, S=2097154+4h+7ell.

At fixed ell, S=4u+b' with b'=1827462-5ell>0. The derivative numerator
is -(b'+12ell)u^2-6b'*ell*u-b'^2*ell<0; the denominator increases
with u since2u>4ell. Relax h to1550. The resulting denominator is

    68973^2-1689516*ell+2ell^2,

decreasing through2804; its numerator increases. At that endpoint,

    u=77385, S=2122982, denominator=35596697>0,
    floor(S*(u-ell)/denominator)=4448.

Positivity at this worst point justifies all preceding relaxations.
There are at most3^16 top-dimensional components by the unchanged
normalization-degree proof. The weighted bound on the ENTIRE complement
of their union, at h<=4981, gives

    M_lower<=floor(2^7*3^13*(1043596/62442)^2)=57002969822.

Add one singular pair and256 exceptions. DIRECT gives
base+L*(4448*3^16+57002969822+257)=256464058457221028<(C50).
No purity or single-component premise is imposed.

### e=10

The required GP model and single_fiber_payment.md apply at actual
h<=996. Every pair has at least77363 original joint agreements.
The21h loss, including infinity and exceptional projection fibers, gives

    n_max=1058540, a1_min=56447, collision_max=2988,
    denominator=23346289>0,
    floor(n_max*(a1_min-collision_max)/denominator)=2423.

For coefficient dimension four add one singular pair. If the ENTIRE
coefficient locus has dimension at most three, the weighted theorem gives
floor(2^10*3^9*(1047581/66427)^3)=79053330393 pairs, already including
singular and isolated solutions. These are whole-locus alternatives;
take their maximum, not their sum. With256 off-curve pairs, DIRECT gives
90235520749559576<(C50).

These types exhaust irreducible cubics. Their whole-source bounds combine
by maximum, giving(BIND). The full-kernel cover and all reducible factors
are proved and charged separately in proof.md, without reverse dependency.
