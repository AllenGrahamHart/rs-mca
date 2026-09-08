# Moving-axis parabolas: rule out the tangent equality case

Status: PROVED, 2026-09-07. Work in characteristic not two. Let
Q(U,V) over F(X) define a nonsingular projective conic with rank-one
quadratic homogeneous part. Its unique direction at infinity is called
its quadratic direction here, not a Euclidean metric axis. Suppose
this direction is NONCONSTANT in X. In affine translates of one
s-dimensional polynomial carrier, s>=2, the degree-<K pair locus
Q(a,b)=0 has every coefficient component of dimension at most

    r=floor(s/2).                                       (MPD)

For complete-core agreement >=m-t, K<=m-T and 1<=t<=T, its
distinct represented pairs consequently satisfy

    M_t<=floor(2^(2s-r)*((n-K+1)/(m-t-K+1))^r).          (MPL)

The count uses ORIGINAL polynomial pairs, not the higher-degree
rational parameter below. The dimension improvement is strict in
odd s; the constant-direction case can have dimension (s+1)/2.

## 1. Rational quadratic parameterization and coefficient transport

Put Kappa=F(X). A rank-one binary quadratic can be written c*ell^2
with c in Kappa-star and a nonzero linear form ell over Kappa.
No square root is needed: use a nonzero diagonal entry of its
rank-one symmetric matrix and its row. Choose an independent
linear form m. The conic becomes

    c*t^2+u*t+v*w+z=0, t=ell(a,b), w=m(a,b).

Nonsingularity forces v!=0; otherwise the equation is independent
of w and is geometrically a union of lines. Solving for w and
inverting the constant-in-(a,b) matrix gives

    a=A*t^2+B*t+C, b=D*t^2+E*t+F,                       (8)

with rational X-coefficients and A*E-B*D!=0. The direction (A:D)
is the unique direction at infinity. In the moving case A,D!=0
and D/A is nonconstant in X.

Because t is a fixed rational linear combination of degree-<K
polynomials, a fixed nonzero polynomial L(X) makes zeta=L*t a
polynomial of bounded degree. Its coefficient space is finite;
its degree need not be <K. Substitution in (8) is quadratic with
fixed rational X-coefficients. Requiring the two outputs to be
polynomials of degree <K and to belong to their prescribed affine
carriers gives finitely many closed coefficient equations after
clearing denominators. Conversely each such zeta gives exactly one
pair, and t=ell(a,b) recovers it. These maps are regular in the
coefficient coordinates: multiplication by fixed denominators and
coefficient extraction are linear, and the inverse substitution is
quadratic. Thus the pair locus and this parameter locus are isomorphic.

In particular irreducible components and their dimensions are preserved.
We will use this parameter only for dimension, NOT for a LIST degree
or agreement bound.

## 2. The one-output tangent bound needs no input carrier hypothesis

For dimension, base-change to k=algebraic closure of F. A rational
function nonconstant in X remains nonconstant in k(X).

Let Y be a positive-dimensional component in polynomial zeta space.
Choose zeta_* in Y and divide the gcd of all differences zeta-zeta_*
to obtain a normalized irreducible polynomial family H containing
zero with gcd one. It has the same dimension as Y. Both outputs
take the form

    a(h)=alpha*h^2+beta*h+gamma,
    b(h)=delta*h^2+epsilon*h+z,

with alpha,delta nonzero rational functions and delta/alpha=D/A
still nonconstant. Let D_0 be the maximum degree in H. If D_0=0,
dim H<=1, sufficient since s>=2.

For D_0>0 apply sections 1--3 of `rational_coefficient_graphs.md`
to the first output only. The dimension argument there uses bounded
polynomial variation, gcd-one normalization, and output membership
in an s-space. It does NOT require the input family to lie in that
space. Explicitly, write its derivative as c(X)R(X,h), primitive
in X, with R=r_1(X)h+r_0(X). Its generic degree is

    E_0=max(deg r_1+D_0,deg r_0)>=D_0.

Choose two full-degree coprime derivative values, as in that proof.
Their tangent images each have dimension >=dim H in c^(-1)V;
their intersection has dimension <=1. Thus dim H<=floor((s+1)/2).
For even s this is already (MPD). Suppose s=2r_0-1 is odd and
dim H=r_0>=2. If E_0>D_0 the two images are disjoint, impossible
in dimension 2r_0-1. Therefore E_0=D_0, r_1 is a nonzero
constant, and after absorbing it into c,

    R(X,h)=h+g(X), deg g<=D_0.                           (9)

## 3. Equality forces linear parameter variation

Fix one full-degree derivative value R_1=h_1+g. The set of h_2
with R_2=h_2+g full-degree and coprime to R_1 is nonempty open
in H by the gcd-one argument. At each such pair of points,

    R_1*T_1, R_2*T_2 subset c^(-1)V.

Each tangent dimension is at least r_0. Coprimality and degree D_0
bound the intersection by one, so both tangent dimensions must be
EXACTLY r_0 and their intersection exactly one. A nonzero equality
R_1*w_1=R_2*w_2 forces w_1 to be a nonzero constant multiple of
R_2, since deg w_1<=D_0=deg R_2. Hence h_2+g belongs to T_1
for EVERY h_2 in that open set. By closure H+g is contained in
the r_0-dimensional linear space T_1. Its dimension is r_0,
so H+g=T_1. Since 0 belongs to H, g belongs to T_1 and

    H=W=T_1 is a linear r_0-dimensional polynomial space. (10)

One can equivalently take the closure before this argument: the closed
quadratic output-membership equations still hold on it. Thus no
unjustified closed-image or smoothness assumption is being used.

## 4. The shared output carrier forces a constant quadratic direction

For every h in W, both h and -h lie in H. Subtract the fixed
output at zero and polarize. Since characteristic is not two,

    alpha*W^2 subset V, delta*W^2 subset V,              (11)

where W^2 is the linear span of all products of two elements of W.
Squares span this product space by polarization. If d_1<...<d_r0
are a leading-degree basis of W, the products with degrees

    d_1+d_1 < ... < d_1+d_r0 < d_2+d_r0 < ... < 2d_r0

are 2r_0-1 independent polynomials. Thus dim W^2>=2r_0-1=s.
Equation (11) forces equality and V=alpha*W^2. Therefore
(delta/alpha)*W^2 is contained in W^2. A nonconstant rational
function cannot preserve a nonzero finite-dimensional k-vector space
in k(X): Cayley--Hamilton applied to multiplication would make it
algebraic over the algebraically closed constant field k, hence
constant. This contradicts the moving direction. The equality case
is impossible, proving (MPD) for odd s also.

This step requires the SAME output carrier. Two unrelated spaces of
dimension s do not suffice; the controls exhibit the failure.

## 5. Return to the original pair coefficients for the count

Clear the fixed X denominators in Q(a,b)=0. Its coefficient
equations are quadratic in the original 2s pair coordinates, and
their locus has dimension <=r by (MPD). Section 3 of
`algebraic_list_bound.md` gives a pure r-dimensional cover with
degree <=2^(2s-r). Its joint version in section 4 gives (MPL).
No parameter degree or extra field degree appears in Q's LIST ratio.
Original slope ownership and global margin accounting are unchanged.

If the quadratic direction IS constant, a fixed GL_2(F) change
makes one component affine linear in t with nonzero coefficient.
Eliminating t gives a degree-two rational-X polynomial graph. This
case uses the earlier graph theorem, not the improved moving bound.
