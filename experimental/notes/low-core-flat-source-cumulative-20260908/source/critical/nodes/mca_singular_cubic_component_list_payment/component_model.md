# A polynomial model on one irreducible coefficient component

Work over the algebraically closed constant field k, characteristic zero
or >3. The original source's larger p>=J guard is retained separately.
Let Y be a positive-dimensional irreducible component of bounded original
polynomial pairs on the affine-singular cubic. The required weighted
supplier gives the birational normalization

    f(sigma)=f_s+(sigma^2-lambda)*(P+sigma*Q),
    P,Q in k(X)^2 independent, (A,B)*Q=0,
    (A,B)*P!=0.                                        (1)

It also bounds all admissible rational sigma in one fixed finite-dimensional
rational-function space. Its proof uses the equation for sigma^2 and
original degree ceilings; no small parameter height is assumed there.
The singular pair f_s is the only exceptional pair for the inverse formula.

Take the inverse image of Y away from f_s and its closure Z in that
parameter space. It is irreducible, has the same dimension as Y, and all
its outputs remain in the original affine carrier: those coefficient
conditions are closed polynomial equations. Choose sigma_0 in Z and a
common denominator D for the differences sigma-sigma_0. Let q be the
gcd of the nonzero polynomials in their k-linear span after multiplication
by D. Put

    sigma=sigma_0+(q/D)*z.                              (2)

The actual z form an irreducible polynomial coefficient family containing
zero. Let ell be their maximum degree. Their linear span has gcd one.
Consequently at EVERY finite x the value z(x) is nonconstant on this
family: some member is nonzero there and the zero member is present.
Likewise the coefficient of X^ell varies. These nonconstant functions
have infinite images over k, even in positive characteristic. No
surjectivity or full affine-space assertion is needed.

## All transformed output coefficients are polynomial

After (2) write the two output polynomials in the parameter z as

    Phi(X,z)=sum_(i=0)^3 P_i(X)*z^i,
    Psi(X,z)=sum_(i=0)^3 Q_i(X)*z^i,                    (3)

initially with rational X-coefficients. If, at a finite x, some coefficient
of Phi had a pole, take the largest pole order M. The coefficient of
(X-x)^(-M) in Phi(X,z(X)) is a NONZERO polynomial of degree <=3 in
z(x), formed from the leading pole coefficients. But every output in
the family is a polynomial, so it vanishes for the infinitely many z(x)
values of the family. This is impossible. The same argument applies to
Psi. Thus all P_i,Q_i belong to k[X].

At infinity, if max_i(deg P_i+i*ell)>J-1, its leading output coefficient
is a nonzero polynomial in the varying leading coefficient of z. It
cannot vanish on the whole family. Hence

    deg P_i, deg Q_i <=J-1-i*ell.                       (4)

Zero coefficients have degree minus infinity. The argument includes
ell=0: then the varying value is the constant coefficient of z.
For a dimension-three family necessarily ell>=2.

## The constant and exceptional fibers have degree budgets

The cubic leading vector stays in the primitive projection kernel:

    (P_3,Q_3)=gamma(X)*(B,-A).

It is nonzero over k(X). Both entries are polynomials and gcd(A,B)=1,
so gamma is a nonzero polynomial. By (4),

    deg gamma+h+3ell<=J-1.                             (5)

At a finite x, the map z -> (Phi(x,z),Psi(x,z)) can be constant only
if gamma(x)=0, since A(x),B(x) cannot both vanish. Let g count the
constant-map coordinates whose constant value equals the received pair.
They are exactly the identical joint agreements of Y, because z(x)
varies. Thus g<=deg gamma. Constant maps with a different received value
have empty lists, not unrestricted parameter values.

The projected output A*Phi+B*Psi has degree exactly two in z by (1).
Its quadratic coefficient

    E(X)=A*P_2+B*Q_2 !=0,
    deg E<=J-1-2ell+h.                                (6)

At E(x)!=0, a prescribed joint received value allows at most two z-values.
At E(x)=0, a nonconstant map allows at most three. Each of the g
identical-agreement coordinates is a root of E. There are consequently
at most deg E-g three-list exceptions among the other coordinates.

The rational change (2) deletes no original coordinates, including zeros
of D or q. Its transformed output coefficients are regular there by the
proof, so the original polynomial identities extend there. This is a
componentwise change of parameter, not a receiver descent or a change of
original finite slope. Different components may need different models;
their number is explicitly charged in `component_degree.md`.
