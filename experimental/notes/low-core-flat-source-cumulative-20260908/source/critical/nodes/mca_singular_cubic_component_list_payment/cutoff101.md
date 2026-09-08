# A component bound for LOW cutoff 101

Status: PROVED. Keep the actual common eleven-dimensional degree-<J
carrier and the same geometrically integral affine-singular one-boundary
cubic, with primitive projection-kernel dimension d=7. Now suppose

    8656<=J<=8763, 601<=h<=4381,
    joint agreement >=A=J+67371.

Every such jointly rich pair on the cubic, over the original field, is
included in the bound

    M_cubic<=255040048958.                             (C101)

The height ceiling is floor((J-1)/2)<=4381 by the required height
theorem. This is a pair count, not a source-cover assertion or a complete
MCA label/resource payment. The finite consumer owns the latter.

## 1. The polynomial models and degree cost are unchanged

The proofs in `component_model.md` and `component_degree.md` apply
without the old numerical cutoff. On each three-dimensional coefficient
component, the polynomial parameter has degree

    2<=ell<=floor((J-1-h)/3)<=2720,
    g<=G=J-1-h-3ell,

where g is the number of identical joint-agreement coordinates. There
are at most 3^16=43046721 such components. This counts all geometric
components and preserves their original polynomial-pair degree.

The list slots after paying g identical agreements are, as before,

    S(g)=2n+J-1-2ell+h-3g, u=A-g,
    M<=S(g)*(u-ell)/(u^2-S(g)*ell).                    (1)

The denominator is proved positive below. The rational parameter change
does not discard original coordinates, constant maps or exceptional fibers.

## 2. Keep g and h coupled

At fixed ell,h, write S(g)=3u+b with
b=1895038-2ell+h>0. The derivative numerator of the fraction in (1)
with respect to u is

    -(b+6ell)*u^2-4*b*ell*u-b^2*ell <0.

Also the denominator increases with u since 2u>3ell. Thus the worst
g is its maximum G. At g=G,

    u=67372+h+3ell, S=2097154+4h+7ell.                (2)

Write S=4u+b1, b1=1827666-5ell>0. Its derivative numerator is

    -(b1+12ell)*u^2-6*b1*ell*u-b1^2*ell <0.

The denominator again increases with u since 2u>4ell. Therefore the
worst h is 601, giving

    u0=67973+3ell, S0=2099558+7ell,
    u0^2-S0*ell=67973^2-1691720*ell+2ell^2.

The numerator S0*(u0-ell) increases with ell>=0. The denominator
decreases on 0<=ell<=2720. At the endpoint,

    u0=76133, S0=2118598,
    denominator=33647129>0, numerator=155532634974,
    floor(numerator/denominator)=4622.

This proves positivity for all preceding relaxations and a uniform
4622-pair cap per top component. It is not a scan over component models.

## 3. Include the entire smaller-dimensional complement

The actual nonpure weighted-lift budget in the required supplier applies
to the complement of the UNION of all top components. Its maximum height
is 4381 and the agreement gap is 67372. Thus this complement has at most

    floor(2^7*3^13*(1044196/62991)^2)=56078104495

rich pairs. This is not a dimension-two assertion about the whole locus.
Adding one possible singular pair, harmless even if already included,
gives

    4622*43046721+56078104495+1=255040048958.

All original labels and any off-curve pairs remain for the consumer to
count. The old cutoff-500 theorems and their stronger constants on their
own scopes are unchanged. No reverse dependency on the full-kernel node
is used in this component proof.
