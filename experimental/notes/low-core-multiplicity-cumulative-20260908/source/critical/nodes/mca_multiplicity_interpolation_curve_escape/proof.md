# Proof

Write K=F(X), d=r*A, and let W(d) contain every polynomial of weighted
degree <d for weights (1,w,w). There are i+1 pair monomials of total
degree i, each with max(d-i*w,0) allowed X powers. Hence dim_F W(d)
is exactly Phi_w(d), including its strict endpoint and all truncated blocks.
Every element has pair degree <=ell=floor((d-1)/w).

## 1. Impose multiplicity in all three variables

At a received triple P_x=(x,u(x),v(x)), impose

    Q in (X-x,Y-u(x),Z-v(x))^r.

This imposes at most binom(r+2,3) linear conditions on W(d): expand
in the three translated variables and set all coefficients of total degree
<r to zero. These are Hasse coefficients, with no factorial division.
Use all n domain points; restricting to a complete core union would also
work, but is not needed. The resulting linear kernel E therefore has

    dim_F E >= Phi_w(d)-n*binom(r+2,3).                (1)

No independence of the conditions is assumed. No interpolation matrix
needs to be constructed. For r=2 there are four conditions, including
the formal X derivative. This does not differentiate the received word.

Let (a,b) be any counted pair. At each joint agreement x, substitution
Y=a(X), Z=b(X) sends all three generators of the displayed maximal
ideal into (X-x). Consequently Q(X,a(X),b(X)) is divisible by (X-x)^r.
Its degree is <r*A, because both substituted polynomials have degree
<=w. The A distinct agreement points supply at least r*A roots counted
with multiplicity. Thus

    Q(X,a,b)=0 in F[X] for EVERY Q in E.              (2)

This argument includes zeros of all coefficients of G and makes no
assumption about how a polynomial pair varies inside a coefficient family.

## 2. The whole kernel cannot consist of multiples of G

Gauss division over the UFD F[X] says that if primitive G divides Q
over K[Y,Z], then Q/G already belongs to F[X,Y,Z]. A negative content
valuation in the quotient would persist in the product, since G has
content valuation zero at every prime. Multiplication by G is injective.

Weighted degree is additive in a polynomial domain, and weighted_degree(G)
is at least g*w. Therefore the subspace of W(d) divisible by G has
dimension at most Phi_w(d-g*w). This bound needs no upper coefficient
height for G. Under (ESC), (1) strictly exceeds that dimension. There is
a nonzero Q in E not divisible by G.

## 3. Count function-field points, not coefficient components

Irreducibility of G and G not dividing Q imply that G,Q are coprime
in K[Y,Z]. The affine plane intersection degree bound gives at most
g*ell common K-points. It follows from the hypersurface degree argument
in the required supplier's algebraic_list_bound.md, applied to the
projective closures and then discarding infinity and multiplicities.
It does not require smoothness or separability of an individual
intersection point. A nonzero constant Q gives no points.

Each rich polynomial pair on G is one such K-point by (2), and distinct
polynomial pairs give distinct K-points. This proves (COUNT), including
singular curve points, every coefficient component and isolated solutions.
Passing to a geometric intersection for this upper bound changes neither
the actual field of the polynomial pairs nor any original MCA denominator.

The strict dimension inequality, the FULL three-variable multiplicity,
and strict weighted substitution degree are all essential proof interfaces.
