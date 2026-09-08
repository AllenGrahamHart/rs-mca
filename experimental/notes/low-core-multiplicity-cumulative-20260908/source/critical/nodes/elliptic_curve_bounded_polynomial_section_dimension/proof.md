# Proof using families of sections

Write B=P^1_k and K=k(X). All coefficient loci below are reduced.

## 1. The surface and its section normal bundles

If the coefficient locus is empty there is nothing to prove. Otherwise
it has a k-point, hence C has a K-point O. A smooth projective genus-one
curve with this origin is an elliptic curve E over K. This is an
isomorphism of abstract curves, not an assertion that an arbitrary O
is a flex or that a linear plane transformation gives Weierstrass form.

Take its smooth projective relatively minimal elliptic surface
pi:S->B, with section O. We use the classical Kodaira--Neron model,
canonical-bundle formula and Euler-characteristic formula specified in
`audit.md`. When pi has a singular fiber, they give, for EVERY section P,

    deg N_(P/S) = P^2 = -chi(O_S) < 0.                 (1)

For example, adjunction gives
-2=P^2+K_S.P=P^2+(-2+chi(O_S)), and positivity of chi follows
from the singular-fiber Euler contributions. Characteristic >3 excludes
the wild small-characteristic cases; no separability of the j-map is
assumed.

Handle the all-smooth case separately; do not apply a strict positivity
statement whose source assumes a singular fiber. The global minimal
Weierstrass model over B has coefficients of weights 4n and 6n and
discriminant of degree 12n, with n>=0. A nowhere-zero discriminant on
P^1 has degree zero, so n=0. The coefficients are constant, and S is
the product B x E_0. Along any section, the vertical tangent bundle is
the pullback of T_(E_0), which is trivial by an invariant vector field.
Since a section splits d pi, its normal bundle is this vertical bundle.
Thus in this case

    N_(P/S) is trivial, and h^0(B,N_(P/S))=1.           (2)

Combining (1) and (2), the space of global normal sections has dimension
at most one, and zero if pi has a singular fiber. Also, if pi is smooth
everywhere its j-invariant is regular on B and hence constant. A
nonconstant j therefore implies the zero-dimensional alternative.

## 2. Spread an ACTUAL family before taking its tangent

Let Y be an irreducible coefficient component and let eta be its
generic point. Its generic polynomial pair defines a point of
C(k(Y)(X)), hence of E(k(Y)(X)). Properness of S over B extends this
point to a section over P^1_(k(Y)): apply the valuative criterion at
each missing point of this regular curve. The extensions are unique
and glue. A field extension of k preserves smoothness of S.

This section spreads to a morphism

    sigma: B x Y_0 -> S

for some nonempty open Y_0 of Y, with pi sigma equal to the first
projection. Here one can shrink an affine open of Y through principal
opens: their products with B have affine transition maps, are
quasi-compact and quasi-separated, and have limit P^1_(k(Y)). The
finite-presentation limit theorem cited in `audit.md` spreads both
the morphism and its section identity. Shrink again so that the
generic-fiber identification with the original polynomial pair holds.
Concretely, this last identity involves finitely many rational
coordinate functions and can be spread by clearing their denominators.

This step is essential. We are NOT claiming that every formal
first-order perturbation of rational coordinates extends to a section
at all singular fibers. We first extend and spread an actual family,
then differentiate only that family.

## 3. Inject coefficient tangents into global normal sections

Choose a smooth k-point y of Y_0, possible since k is perfect. Write
P=sigma_y. For v in T_yY, differentiating sigma in the Y-direction
gives a global section of P^*T_S whose image under d pi is zero.
The section identity gives d pi dP=id. Thus pi is smooth along P,
and its vertical tangent along P identifies with N_(P/S). We obtain

    T_yY -> H^0(B,N_(P/S)).                            (3)

This map is injective. If the normal variation is zero, its vertical
tangent representative is zero because the section splits d pi.
On the generic fiber the isomorphism E=C then forces the variations
of the original affine coordinates a,b to be zero. Equality of
polynomials over k[epsilon]/(epsilon^2) forces every coefficient
variation to be zero. Y is a coefficient subvariety, so v=0.
An isogeny or Frobenius substitution would not justify this argument;
we used an actual curve isomorphism and the original coefficient
embedding.

Since y is smooth, dim Y=dim T_yY. Equations (1)--(3) prove
dim Y<=1, and dim Y=0 when pi has a singular fiber. The result holds
for each component and for all finite polynomial degree bounds.
Intersecting with affine coefficient subspaces can only decrease
dimension. Nonconstant j supplies the stated sufficient test.

No count of sections, Mordell--Weil rank computation, height estimate,
domain genericity, or finite-field sampling is used.
