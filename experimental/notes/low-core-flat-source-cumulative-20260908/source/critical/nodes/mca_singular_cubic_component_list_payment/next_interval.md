# Coupling height and agreement extends the component bound

Status: PROVED. Use the same canonical normalized source, now with
8656<=J<=9526, and an affine-singular cubic of projection-kernel
dimension d=7 and primitive height 1301<=h<=4762. Keep at most 64
off-curve LOW pairs. The height ceiling is floor((J-1)/2), from the
already required height theorem, not an assumption added to the source.

The generic polynomial-model and degree-cost proofs in this node do
not depend on the earlier numerical endpoint. They give parameter degree
ell<=floor((J-1-h)/3)<=2741, at most 3^16 top components, and the
same constant/exceptional-fiber list argument. We sharpen only its
uniform envelope; using the old independent h-rectangle here would fail.

## 1. Keep the common height in both Johnson budgets

After maximizing the number of identical agreement coordinates as in
`component_list.md`, the agreement and slot budgets are

    a=66973+h+3ell, S=2097154+4h+7ell.

For fixed ell write S=4a+b, b=1829262-5ell>0. The Johnson fraction is

    F(a)=(4a+b)*(a-ell)/(a^2-(4a+b)*ell).

Its derivative has numerator

    -(b+12ell)*a^2-6b*ell*a-b^2*ell <0.              (1)

The denominator increases with a because 2a>4ell. Thus the largest
fraction and smallest denominator occur at h=1301, not by separately
maximizing S at h=4762. Put

    a0=68274+3ell, S0=2102358+7ell.

The numerator S0*(a0-ell) increases with ell>=0. The denominator is

    68274^2-1692714ell+2ell^2,

decreasing on 0<=ell<=2741. At the last endpoint, a0=76497,
S0=2121545 and denominator=36636164>0. The exact Johnson floor is
4271. Positivity here justifies all the preceding monotonicity steps,
including the earlier maximization over identical agreement coordinates.
Every top-dimensional component therefore has at most 4271 represented
nonsingular rich pairs on the entire new interval.

## 2. Count all components and labels once

The unchanged cubic normalization degree proof bounds the number of
three-dimensional components by 3^16=43046721. Their contribution
is at most 4271*3^16=183852545391 pairs. The same actual nonpure
weighted-lift proof pays the complement of ALL top components at h=4762:

    M_lower<=floor(2^7*3^13*(1043815/62211)^2)
            =57451183984.

The locus need not be pure or have one component. Including one singular
pair and 64 off-curve pairs gives

    M_ALL<=183852545391+57451183984+65=241303729440,
    N<=4194116990084347+981604*M_ALL
      =241058823023306107<B=274980728111395087.        (C7+)

Original field, coordinates, raw selection, defects and slope units remain
unchanged. No resource or near charge is repeated. Lower coefficient
dimensions are included by the same complement argument. The earlier
7117..8655 bound remains valid at its sharper constant.

At h<=1300 the separate weighted theorem still gives the uniform bound
274979661292365251, including 64 off-curve pairs, because its ratio
depends on h and the fixed degree gap, not on J. Together these results
pay every d=7 cubic on the new interval. Their use in a multi-factor
kernel ledger requires counting the other factor's labels separately;
this source theorem is not a whole quartic or original-row closure.
