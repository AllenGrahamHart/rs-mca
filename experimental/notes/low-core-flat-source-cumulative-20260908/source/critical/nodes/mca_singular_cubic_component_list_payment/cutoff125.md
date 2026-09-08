# The d=7 high-height class at cutoff 125

Status: PROVED pair bound. Keep the canonical normalized source with
9822<=J<=9940, but count only its raw<=125 pairs. Suppose the cubic
has projection-kernel dimension seven and h>=1551. Then its nonsingular
three-dimensional components and entire smaller-dimensional complement
together contain at most

    M7=4225*3^16+57119482443+1                        (C125)

rich pairs. The final one is the possible singular pair. Off-curve pairs,
source resource and original near remain the finite consumer's charges.

The generic component model is unchanged. Write ell for parameter degree.
Every counted pair has a=J+67347 joint agreements, and

    2<=ell<=floor((J-1-h)/3)<=2796,
    0<=g<=J-1-h-3ell.

The slot expression before optimizing identical agreements is still
S(g)=2n+J-1-2ell+h-3g. The proof in component_list.md applies with
the stronger actual a. Its derivative is negative since
S(0)-3a=1895110-2ell+h>0. At the largest allowed g the budgets become

    u=67348+h+3ell, S=2097154+4h+7ell.

For fixed ell, S=4u+b with b=1827762-5ell>0. The derivative argument
of next_interval.md again shows that the count decreases with h.
Relax h to 1550. Then

    u0=68898+3ell, S0=2103354+7ell,
    u0^2-S0*ell=68898^2-1689966ell+2ell^2.

The denominator decreases and the numerator S0*(u0-ell) increases through
ell=2796. At that endpoint,

    u0=77286, S0=2122926,
    denominator=37424700>0,
    floor(S0*(u0-ell)/denominator)=4225.

Positivity at this worst point justifies the derivative and incidence
steps throughout the rectangle. The existing degree budget allows
at most 3^16 top components; it does not depend on this cutoff.

The carrier height bound is h<=floor((J-1)/2)<=4969. The weighted
incidence estimate on the ENTIRE complement of all top components,
at agreement J+67347 and actual input degree <J+h, gives

    M_lower<=floor(2^7*3^13*(1043608/62379)^2)
            =57119482443.

The singular point and every component are retained. No purity assumption,
receiver descent or source-coordinate deletion is made. This proves (C125);
the finite consumer separately handles h<=1550.
