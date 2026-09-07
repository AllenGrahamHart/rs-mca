# Moving-parabola controls

## Actual canonical source beyond the old mixed-factor cover

Let F=F_(787^2), beta^2=2, D={0,...,782}, K=2, m=30, T=1,
and V=span{1,X}. Split D into 27 groups of size 29. On group j
put (u,v)=(j^2,X*j^2+beta*j). Represented pairs are

    f_i=(i^2,X*i^2+beta*i),
    (b-X*a)^2=2*a.                                    (MC)

This is a nonsingular conic over F(X), with moving quadratic
direction (1:X). Each complete core is exactly the pair's own group.
At x in group j, i!=j, the collision label is

    gamma=-1/(x+beta/(i+j)).

Equality of labels identifies x and i+j by their base-field and
beta coefficients, then j from the group, then i. All 20358 labels
are distinct and all 27 pairs occur. At any fixed printed label,
source-piece polynomials h_i have distinct X coefficients gamma*i^2.
Any other carrier polynomial agrees at at most one point per group,
so at fewer than 30 points. A piece h_i agrees at its 29-point
core and at most one outside coordinate, by label uniqueness.
The printed label has that one extra coordinate, giving a unique
eligible carrier explanation and maximum raw margin one. The core
pins its degree-<2 second component, which fails at the defect;
the 30-support is full-code bad. This is a fixed-carrier census.

No prior total-degree-seven affordable factor cover contains all
27 pairs. Work with the parameter t over F(X). Every nonzero
affine line evaluates to a nonzero polynomial of degree <=2 on
(t^2,X*t^2+beta*t); it cannot vanish identically because its t
coefficient first forces its second row entry zero, then its first.

After any constant invertible matrix and polynomial offset, a first
component has t^2 coefficient A+B*X, nonzero for a nonzero row.
A rational-X polynomial graph of degree e>=2 therefore gives a
NONZERO substituted polynomial of degree <=2e: its top t^(2e)
coefficient cannot cancel against the second component's degree <=2.
It covers at most 2e of the 27 parameter values.

For an affine-product level P(a,b)=R!=0 of degree e, each affine
factor evaluates to a nonconstant polynomial in t (even over a
splitting function field). Their product cannot be the constant R.
Thus this too is a nonzero polynomial of degree <=2e and covers
at most 2e values. These arguments include the prior level-cubic
exception. A cover whose degrees sum to <=7 therefore contains at
most 14 parameter values, not 27. This separates the new mechanism
from that mixed-factor test, not from every earlier paid source class
or a deployed unsafe threshold.

## Necessary gates and tangent arithmetic

Dropping the moving-direction gate fails. Let W=span{1,X},
V=span{1,X,X^2}. The pairs (h^2,h^2+h), h in W, satisfy
(b-a)^2=a and have two free coefficients, exceeding floor(3/2).
Their quadratic direction (1:1) is constant. The old ceil bound
is necessary in that case.

The common-carrier gate is also essential. The moving pairs
(h^2,X*(h^2+h)), h in W, lie in DIFFERENT three-dimensional
carriers V_a=span{1,X,X^2}, V_b=span{X,X^2,X^3}; they still
have dimension two, exceeding floor(3/2). Their common containing
carrier instead has dimension four, consistent with the theorem.

For the odd s=11 equality test, W=span{1,...,X^5} has product
space span{1,...,X^10} of dimension eleven. Multiplication by X
does not preserve it, since X*X^10 is outside. This checks the
simple model behind the full rational-function invariance argument.
The earlier characteristic-two control remains a necessary guard.

The verifier checks the exact field census and finite parameter
encodings. Dimension, maximality and universal curve-cover exclusion
are hand proofs, not consequences of a sample surviving a search.
