# Moving-projection controls

## Input dimension and degree must change

For V=P_<=s-1, A=1, B=X^h with 0<=h<=s,

    dim(V+X^h V)=s+h, dim ker L=s-h.

Thus N+d=2s; replacing N by s is generally false. At h>=s the
two monomial ranges are disjoint and d=0. These are exact linear
space identities, not an inferred dimension of a nonlinear family.

There are actual admissible inputs outside V. Take V=span{1,X},
A=1, B=X and

    Phi(T)=T-T^3/X^4, Psi(T)=T^3/X^5.

Then Phi+X*Psi=T. The pair (0,X) lies in V x V and has input
T=X^2, outside V. Its component degrees are <2 but its input degree
is two. Although the displayed outputs have poles at X=0, their
rational identities yield genuine polynomial outputs, and T(0)=0
still gives the scalar agreement there. No domain point is removed.

## The coupled dimension can be attained

For V=P_<=10, A=1, B=X, put

    Phi(T)=T+X*T^3, Psi(T)=-T^3.

Here s=11,d=10,N=12,r=4. Every T of degree <=3 is admissible,
so the dimension-four bound is attained. The leading direction moves
with X; this is not being treated as a constant component change.

## Guards and residual cases

- The characteristic-three family T=c+dX, outputs (T,T^3) in
  V=span{1,X,X^3}, has dimension two. The predicted r=1 would be
  false if the p>=K output-space guard were dropped (here K=4).
- The identity A*Phi+B*Psi=T is essential. For outputs (T^2,T^3),
  no F(X)-linear combination has a T term. A quadratic normalization
  projection must not be substituted for this linear input.
- A finite singularity can use all eleven carrier directions even with
  a four-dimensional parameter family. Take (a,b)=(X^4*T^2,T^3),
  deg T<=3, in V=P_<=10. Polarization in characteristic >3 shows
  that the coordinate spans are X^4*P_<=6 and P_<=9, whose sum
  is all V. Their cusp equation is a^3=X^12*b^2. This rejects a
  naive carrier-dimension-drop argument; it is not a canonical unsafe
  source or an asserted error-rank-twelve construction.
- Primitive normalization of A,B is required for the coefficient-height
  inference. Multiplying both by an arbitrary polynomial does not
  produce a new forced height bound from the same primitive curve.
- h=51392 violates the Q_h<64 recipe by one in the cross-multiplied
  numerator. That is failure of this sufficient cap, not an unsafe row.

The small verifiers check these scalar/polynomial identities and the
finite arithmetic. The universal dimension and geometric recognition
proofs remain hand proofs.
