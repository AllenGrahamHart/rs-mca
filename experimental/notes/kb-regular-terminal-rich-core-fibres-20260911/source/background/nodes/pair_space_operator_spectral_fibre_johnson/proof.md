# Separate Eigenvector Differences Before Counting Intersections

For x off the anchors, differences between two represented pairs vanish
jointly exactly when y(x)=T(y)(x)=0, where y is their nonzero parameter
difference. The constant change (p,q)->(p+alpha*q,q) is invertible, and
H_a(x)!=0. All coefficients and eigenspaces remain over F.

If y is an eigenvector, its polynomial is a nonzero multiple of the
chosen y_lambda. Its roots were deleted, so such a pair of cores has
no common point in Omega. Otherwise y and T(y) are F-linearly independent.
Their simultaneous annihilator in U* is one-dimensional. Every nonzero
evaluation where they both vanish therefore represents the SAME projective
point. The two cores intersect Omega in at most H common coordinates.
This argument does not require joint evaluation to have rank two.

## The Removed Set

Distinct eigenvalues number at most three, since det(zI-T) has degree
three. The eigenspace hypothesis permits one polynomial per eigenvalue;
each has degree<=D. For e>0 the union of these roots has size<=e*D
and includes every common evaluation zero of U. Adding anchors gives b_e.

If e=0 and U vanishes on z nonanchor coordinates, their locator divides
every polynomial of U. Division injects U into polynomials of degree<=D-z,
a space of dimension D-z+1. Thus z<=D-2. This gives b_0. Multiplicities
and overlaps can only decrease the number of deleted coordinates.

## Exact Intersection Bound

Let b be the actual number deleted, N_b=n-b and A_b=A-b. Choose exactly
A_b remaining core coordinates for each of M represented pairs; this
loses no pair. Their pairwise intersections have size<=H. If c_x is the
incidence multiplicity, Cauchy--Schwarz and double counting give

    M^2*A_b^2/N_b <= sum c_x^2
                   <= M*A_b+M*(M-1)*H.

For M>0 and positive denominator, this yields
M<=N_b*(A_b-H)/(A_b^2-N_b*H). Empty families cost zero.

For the passage to b_e, put c=n-A>=0, x=A-b and
Delta=x^2-(x+c)*H. The quotient is 1+c*x/Delta. On Delta>0 its derivative
in x is -c*(x^2+c*H)/Delta^2<=0. Delta is positive for all x>=A-b_e:
the stated positive gate implies x>H, and its derivative 2x-H is positive.
Since b<=b_e, replacing b by b_e only increases the quotient.
This proves COUNT with its stated gates, including the case n=A.

The required original-owner theorem bounds each pair's raw weight by
n-|H_f|<=n-A. Multiply by the pair count; retain all its original
assigned labels and weights, including defects at deleted auxiliary
coordinates. This is not a refund or a shortened-source raw value.
