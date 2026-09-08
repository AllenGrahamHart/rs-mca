# Finite projective product fibers, with their degree cost

Work over an algebraically closed field k, in any characteristic. Let
U,W be nonzero finite-dimensional k-subspaces of k(X), of dimensions
a+1,b+1, and let R!=0 in k(X), m>=1. Then

    Z={([f],[g]) in P(U) x P(W): f*g^m belongs to k^* R}

is finite and has at most binom(a+b,a)*m^b geometric points. Empty
fibers are allowed. The bound counts all divisor patterns, not just one.

## 1. Finiteness

Use the fixed-divisor argument of the required affine-product supplier,
here directly on P^1_k. A basis of U or W bounds poles at a fixed finite
set of places. Enlarge it to S by the zeros and poles of R. Outside S,
ord f and ord g are nonnegative, and ord f+m*ord g=ord R=0, so both
are zero. At each place of S their fixed lower bounds, combined with
that equality, give fixed upper bounds as well. Thus each function has
only finitely many possible divisors. Equal divisors on P^1 imply a
constant nonzero ratio. There are finitely many pairs of projective
classes. This argument does not estimate their number from pole heights.

## 2. A closed embedding and its exact degree

Choose coefficient coordinates F_0,...,F_a and G_0,...,G_b. Embed
P^a x P^b using ALL monomials F_i*G^I with |I|=m. This is the
degree-m Veronese map on the second factor followed by the Segre map.
For completeness, on F_i*G_j^m!=0 the coordinate ratios include

    (F_l*G_j^m)/(F_i*G_j^m)=F_l/F_i,
    (F_i*G_j^(m-1)*G_l)/(F_i*G_j^m)=G_l/G_j.

They generate the affine chart ring, so these chart maps are closed
immersions. The map is proper, since its source is projective, and
these charts cover the source; hence it is a closed immersion globally.
In particular, this uses all monomials, not the possibly inseparable
map retaining only pure mth powers in positive characteristic.

Its homogeneous coordinate ring in grade t has basis all monomials of
bidegree (t,mt). Every such monomial factors into t monomials of
bidegree (1,m), and distinct monomials in the polynomial ring are
linearly independent. Its Hilbert function is therefore

    H(t)=binom(t+a,a)*binom(mt+b,b).

The variety has dimension a+b. Multiplying the leading coefficient
m^b/(a!*b!) by (a+b)! gives degree binom(a+b,a)*m^b. This computation
is characteristic-free and includes a=0 or b=0.

## 3. The fiber is a linear section in that embedding

Expand f*g^m in a fixed finite-dimensional function space containing
all these products and R. Its coefficients are forms of bidegree
(1,m), hence linear combinations of the embedding coordinates. The
product never vanishes for nonzero f,g in a field, so this coefficient
system has no basepoint. The condition that the product lie in kR is
given by linear equations; no zero product is accidentally included.

We have already proved that their common zero set on the embedded
variety is finite. Starting with its irreducible image, at every positive
dimension choose a linear combination of the fiber equations nonzero
on every current component. Such a combination exists over infinite k:
no positive-dimensional component can lie in the finite common zero set.
Intersect, reduce, and continue. Proper hyperplane sections lower pure
dimension by one and do not increase total component degree, by the
required supplier's hypersurface degree lemma. After a+b steps, the
result is zero-dimensional, contains Z, and has total degree at most
binom(a+b,a)*m^b. Multiplicities can only increase the upper bound on
distinct points. Dimension zero initially needs no cuts.

This proves the lemma without computing roots, divisor classes, a
Groebner basis, or a large coefficient matrix. A dimension-one bound
in the original affine coefficient space alone would not give this price.
