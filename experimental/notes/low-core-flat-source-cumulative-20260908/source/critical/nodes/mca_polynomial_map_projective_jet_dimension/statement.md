# Projective jets bound polynomial-map families

## Moving linear projection extension

The [coupled theorem](moving_projection_graphs.md) also handles inputs
z=A*a+B*b with primitive polynomial A,B of height h, provided
(a,b)=(Phi(z),Psi(z)), max degree e>=2, and A*Phi+B*Psi=Z exactly.
If d is the kernel dimension of this projection on V x V, its input
space has dimension N=2s-d while the coefficient family has dimension
r<=ceil(d/e). The degree charge is e^(N-r), and the scalar LIST
degree is K+h, not K. No evaluation points are deleted.

On the normalized KoalaBear source, moving cubic projection graphs
with h<=51391 pay whole-source total <=265092257458790508.
For a primitive weighted kernel cubic on 7117..8655, the forced
h<=17580 improves this to <=117918672306944736. A one-place
cubic singular at infinity has exactly this projection-graph form.
Weighted unique-infinity conics similarly get gain <=18684190437980288,
less than two ordinary factor units. Arbitrary-height moving conics and
quadratic normalization projections do not receive these new prices.

The earlier general theorem and constant-coordinate graph bounds follow.

Status: PROVED. Let k be an algebraically closed field of characteristic
zero or characteristic p>=K. Let V be an s-dimensional subspace of
k[X] of degree <K, with s>=1. Let H be ANY finite-dimensional polynomial
parameter space, and Phi(X,Y) in k(X)[Y] have degree e>=1 and nonzero
leading coefficient alpha(X). For a fixed rational function b_0, every
irreducible coefficient family

    Z subset {h in H: Phi(X,h) belongs to b_0+V}

has dimension at most

    r=ceil(s/e).                                         (JD)

The parameter degree may exceed K. No input-carrier equality, generic
domain, bound on the X-coefficient heights, or nonzero derivative in Y
is assumed. The output degree/characteristic guard is essential.

If two outputs of the SAME degree e belong to affine translates of the
SAME V, with leading-coefficient ratio nonconstant in X, and s>=2,
the stronger bound is

    dim Z <= ceil((s-1)/e).                             (J2)

For a graph b=Phi(X,a) with a in a_0+V and b in b_0+V, both of
degree <K, the old algebraic degree-cover and LIST proof consequently gives

    M_LOW <= floor(e^(s-r)*Q^r),
    Q=(n-K+1)/(m-T-K+1), r=ceil(s/e).                   (JL)

This is an algebraic coefficient-family bound, not an arbitrary-word
post-Johnson theorem. Its MCA application keeps canonical complete cores,
original finite labels, and the original margin ledger.

On the canonical normalized KoalaBear source of the finite supplier,
4801<=J<=169999 and graph degrees 2<=e<=9 are all paid with

    |Gamma|+134944 <=140379757249624860,
    reserve=134600970861770227.                          (JF)

No arbitrary source is asserted to admit such a graph. The unrestricted
remaining J interval, higher ranks and both prizes remain open. The proof
uses the general projective dimension theorem, with a primary reference in
proof.md; the Wronskian and multiplicity arguments are proved here.
