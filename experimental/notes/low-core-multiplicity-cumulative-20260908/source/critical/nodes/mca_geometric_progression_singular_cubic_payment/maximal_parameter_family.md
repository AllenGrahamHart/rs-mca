# Four dimensions force the full degree-three parameter space

Work over k(T), k algebraically closed, char k zero or >3. The cubic H
has the geometry in the statement and top binary form `(T P+Q)^3`.
Set x=T*P+Q, y=P. Smoothness at its unique infinity point gives an
equation with nonzero x^3 and y^2 coefficients. Completing the square
in y and dividing by the repeated root of the resulting cubic in x,
as in the required weighted supplier, gives a birational parametrization

    P=Phi(T,sigma), Q=Psi(T,sigma), deg_sigma Phi=deg_sigma Psi=3,
    lead_sigma Phi=alpha(T), lead_sigma Psi=-T*alpha(T), alpha!=0. (1)

Every nonsingular rational pair has a unique sigma in k(T). Both maps
are polynomials in sigma; their coefficients may initially have arbitrary
poles. The affine singular pair is one exception to the inverse formula.

## 1. Finitely many affine parameter spaces, each of dimension at most four

Call sigma admissible when Phi(sigma),Psi(sigma) are polynomials of
degree <=10. Write a_v=ord_v(alpha) at each place of the T-line,
including infinity; these integers have finite support and sum zero.

At a finite place, factor Phi(T,Z)=alpha*product_(i=1)^3(Z-r_i) over
a splitting field equipped with an extension of ord_v. For admissible
sigma, the sum of ord_v(sigma-r_i) is at least -a_v. Therefore at
least one of these three valuations is >=-a_v/3. If Phi(sigma)=0,
one distance is infinite and the same conclusion holds.

At infinity apply this to Psi instead. Its leading coefficient has
valuation a_infinity-1, while admissibility requires ord_infinity Psi
at least -10. Thus one distance to a root of Psi is at least
(-9-a_infinity)/3. Only finitely many finite places are exceptional:
outside the zeros of alpha and the poles of the coefficients of Phi,
a negative valuation of sigma would make the cubic term uniquely lowest,
contradicting integral Phi(sigma). Thus sigma is integral there.

Choose one qualifying root at each exceptional place and at infinity.
There are finitely many assignments, with no estimate of their number
needed. Within one nonempty class choose an admissible sigma_0. The
ultrametric inequality and integer valuations of rational differences give

    ord_v(sigma-sigma_0)>=-floor(a_v/3),       v finite,
    ord_infinity(sigma-sigma_0)>=-3-floor(a_infinity/3).             (2)

Consequently all admissible parameters lie in finitely many cosets of

    W=L(D), D=sum_v floor(a_v/3)[v]+3[infinity].                   (3)

The elementary divisor-space dimension on P^1 is
`dim L(D)=max(deg D+1,0)`. Indeed multiply by the product of the finite
linear factors with the required valuations to reduce the conditions
to being a polynomial of degree <=deg D. Since sum a_v=0,

    deg D=3-(1/3)*sum_v (a_v-3*floor(a_v/3))<=3.                  (4)

Every summand in parentheses is 0,1 or 2, also for negative a_v.
Thus dim W<=4. This is a finite-union dimension argument, not a bound
that discards or fails to charge a potentially large number of branches.

For the standard valuation input, a valuation on k(T) extends to a finite
splitting field by a valuation ring dominating its local ring; restricting
back recovers the original valuation ring. See [Stacks, valuation rings](https://stacks.math.columbia.edu/tag/00I8),
Lemmas 10.50.2 and 10.50.7, and [finite extensions](https://stacks.math.columbia.edu/tag/0ASF),
Lemma 15.125.2. Normalize the extension to agree with ord_v; its values
may be fractional, but rational differences in (2) have integer values.
No series expansion or numerical root calculation is needed.

## 2. One entire coset is admissible

In each fixed coset sigma_0+W, the condition that both outputs are
polynomials of degree <=10 is a CLOSED algebraic condition on the finite
coefficient vector: clear their fixed common T-denominator and equate
the unwanted coefficients. The maps to the two output coefficient
vectors are polynomial on that closed set.

These finitely many images cover all nonsingular bounded pairs. If their
coefficient locus has dimension four, one closed admissible subset has
dimension at least four. Since dim W<=4, it equals its entire affine
coset. Equation (4) forces deg D=3, so every a_v is divisible by three.
Choose r(T) with ord_v r=-a_v/3 for all v. It exists by the explicit
product of finite linear factors, since the valuations sum zero.
Then alpha*r^3=c in k*, and W=r*k[T]_(<=3).

For one center sigma_0, EVERY sigma=sigma_0+r*eta with deg eta<=3
is admissible. Make this fixed affine change of normalization parameter.
The output cubics become

    Phi=c*eta^3+p(T)*eta^2+u(T)*eta+v(T),
    Psi=-c*T*eta^3+b(T)*eta^2+w(T)*eta+j(T).                      (5)

Vary constant eta over four distinct k-values. Vandermonde inversion
shows that each coefficient in (5) is polynomial of degree <=10.
Next vary eta=lambda*T^3 over four distinct lambda. The same inversion
shows that the coefficient of eta^i has degree <=10-3i.
Thus deg(p,b)<=4, deg(u,w)<=7, deg(v,j)<=10 as claimed.

## 3. The same model covers ALL nonsingular bounded pairs

This last step is essential: the full-coset conclusion alone need not
describe other components. For any other nonsingular bounded pair, its
original unique sigma is rational, hence eta=(sigma-sigma_0)/r is rational.
The first equation (5), with c a constant unit, is monic in eta after
division by c. Because its coefficients and its output are polynomials,
eta is integral over k[T], hence a polynomial. Equivalently a pole would
make c*eta^3 uniquely lowest in valuation.

If L=deg eta>=4, the second cubic term has degree 1+3L. Its competitors
have degrees at most 4+2L, 7+L and 10, all strictly smaller. Therefore
Psi has degree >10, impossible. Thus every such eta has degree <=3.
Uniqueness follows from the birational inverse away from the singular pair.
No extra component or root-choice class is left to count.

Finally Delta=T*p+b is nonzero. Otherwise x=T*Phi+Psi has parameter
degree <=1, while P has degree three. In the cubic equation in (x,P),
the nonzero P^2 term then has parameter degree six, greater than every
other term, a contradiction. Its degree is at most five by (5).
This completes the maximal-family theorem, independently of any received
word, field enumeration or finite-row numerical bound.
