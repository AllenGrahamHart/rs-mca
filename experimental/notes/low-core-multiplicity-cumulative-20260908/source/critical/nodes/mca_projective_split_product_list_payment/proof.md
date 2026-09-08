# Proof: recover affine scales and count joint agreements

Extend constants to k=algebraic closure of F for upper counting only.
The fixed GL_2(F) matrix maps V x V bijectively onto V x V. Thus the
factor values range independently over cosets x0+V and y0+V, where
x0=alpha*h_*+c0 and y0=gamma*h_*+c1. The k-linear span of each
coset has dimension s+eps, eps as in the statement. Membership of an
F-rational offset in V does not change on extension of constants.

Apply `projective_fiber.md` to these spans, with projective dimensions
a=s+eps_x-1 and b=s+eps_y-1. A point of its finite fiber represents
at most one class of factor pairs up to their two constant scales.
Choose nonzero representatives f,g with f*g^m=cR, c in k^*. Actual
factor values are x=lambda*f,y=mu*g with

    lambda*mu^m=c^(-1), lambda,mu nonzero.                (1)

The invertible affine transformation recovers the original pair uniquely
from these values. Overcounting geometric points can only bound F-pairs
from above, and does not change the finite MCA field or its labels.

## 1. Affine cosets not containing zero

A coset z0+V not containing zero meets a one-dimensional k-linear
space in at most one point: two different multiples would put the
direction in V, then z0 in V. Consequently:

- If eps_x=eps_y=1, both scales are unique. The class count is
  binom(2s,s)*m^s, with at most one actual pair per class.
- If eps_x=0,eps_y=1, mu is unique and (1) determines lambda.
  The bound is binom(2s-1,s-1)*m^s.
- If eps_x=1,eps_y=0, lambda is unique and (1) allows at most m
  distinct mu. Multiplying the class count binom(2s-1,s)*m^(s-1)
  by m gives the third bound. No separability is needed for an upper
  bound by the degree of a nonzero polynomial.

These bounds count all algebraic function-field solutions. They do not
evaluate c0 or c1 on D, so their poles cause no deleted coordinates
or unpriced exception set. In particular a projective class in the last
mixed case need not mean a single pair.

## 2. Both cosets contain zero

Now both factor values range in V. For a class meeting these cosets,
choose f,g in V, with g a nonzero polynomial of degree <J. Let z be
the number of its zeros in D; z<=J-1. Distinct actual pairs in the
class have distinct mu, since (1) uniquely determines lambda from mu.

At each coordinate where g is nonzero, original joint agreement forces
y to have the one prescribed value gamma*u+delta*v+c1. It therefore
pins mu uniquely. This evaluation is well-defined here: y0 in V and
h_* of degree <J imply c1=y0-gamma*h_* is a polynomial of degree <J;
the same holds for c0. We have not assumed rational offsets regular
in the other cases where no evaluation was used.

Each A-rich pair agrees at at least A-z of the n-z remaining original
coordinates, and those agreement sets are disjoint across distinct mu.
Thus the rich pairs in this class number at most

    floor((n-z)/(A-z)) <= floor((n-J+1)/(A-J+1))=floor(Q).

The inequality follows from n>=A and z<=J-1<A. Coordinates with
g=0 remain charged by z, even if they are common agreements for every
pair in the class; they are not deleted from the source. Multiply by
the projective class count binom(2s-2,s-1)*m^(s-1).

The two mixed bounds are half of binom(2s,s)*m^s, so taking the
maximum gives (SP). The proof uses the original degree bound only in
this last incidence argument. All zero-dimensional and positive-dimensional
affine scaling cases are included; no uncounted components remain.

## 3. Finite specialization

For s=11,m=3, Q=1048577/66973 has floor 15. The projective class
counts and scale factors give exactly the four numbers in the statement.
In particular the largest is 15*binom(20,10)*3^10=163644855660.
The consumer, not this abstract list lemma, owns conversion to full
LOW labels, HIGH resource, the off-curve allowance and original near.
