# Cofactor Relations And A Dual Matrix Pencil

## 1. A Small Polynomial Relation From Any Dependent Pencil

We use an elementary fact. If a matrix M(z) with entries of degree<=1
has t columns and is not injective over F(z), it has a nonzero polynomial
kernel vector of degree at most t-1. To prove this, choose a minimally
dependent set of k<=t columns. Their rank is k-1. Choose k-1 rows
independent on these columns and take their alternating(k-1)-minors.
The resulting cofactor vector is nonzero, has degree<=k-1, and
annihilates those rows. They span the restricted row space over F(z),
so the vector annihilates EVERY row. These are polynomial identities.
When k=1 the column is zero and the empty minor is1. No division or
generic evaluation over a large field is needed.

## 2. Minimal Normal Coefficients Are Independent

If the generic projection is proper, it has a nonzero annihilator over
F(z). Clearing denominators gives a polynomial normal. Choose one of
minimum degree d and let E subset V* be the span of its coefficients,
with dimension t<=d+1. Take a constant F-basis of E. Requiring an
E-valued functional to annihilate a+z*b for a basis of W gives a
matrix pencil with t columns. It has a polynomial kernel vector,
namely the chosen normal, so section1 supplies another nonzero normal
of degree<=t-1. If t<=d this contradicts minimality. Hence t=d+1,
and ell0,...,ell_d are linearly independent. This also excludes a zero
constant coefficient or a hidden common polynomial factor.

The coefficients of(NORMAL), viewed as elements of W's annihilator
inside V* x V*, are

    (ell0,0), (ell1,ell0), ...,(ell_d,ell_(d-1)), (0,ell_d).

They are linearly independent: looking at the first component kills
the first d+1 coefficients in any relation; looking at the second then
kills the last. The annihilator has dimension c, giving d+2<=c.
If d=0, ell0 annihilates BOTH component images of W. It cannot do so
when their sum is V. Thus full shared carrier forces d>=1.

## 3. A Full Generic Projection Has Few Exceptional Finite Slopes

Let T=W^perp, dim T=c, and write A,B:T->V* for its component
projections. A functional ell annihilates pi_gamma(W) exactly when
(ell,gamma*ell) belongs to T. Equivalently it comes from a vector
t in ker(B-gamma*A). A is injective on that kernel, because A(t)=0
would also imply B(t)=0 and hence t=0. Therefore

    dim(V/pi_gamma(W))=dim ker(B-gamma*A).                     (DUAL)

The same identity holds over F(z). If the generic projection is full,
the s-by-c matrix pencil B-z*A is injective over F(z), so c<=s.
For c>0 choose a nonzero c-by-c minor. It is a polynomial of degree
at most c. Every finite rank-deficient gamma is a root of that minor,
so there are at most c such gamma. For c=0 the map from the zero
space is injective at every gamma, and there are no exceptions.

The alternatives are exhaustive by rank over F(z). Translating an
affine pair family by one fixed(a0,b0) puts its differences in W;
substitution in(NORMAL) gives the asserted common pair-line identity.
All identities hold in every characteristic and with any field size.
No finite sampling is used to infer rank over F(z).
