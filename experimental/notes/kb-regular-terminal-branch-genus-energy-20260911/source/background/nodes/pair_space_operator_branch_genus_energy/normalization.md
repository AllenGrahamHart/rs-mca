# Prove A Finite Fibre Bound With Its Branch Factor

Homogenize a basis of U to degree D. Gcd1 excludes common affine zeros,
and at least one basis polynomial has actual degree D, excluding a common
zero at infinity. The three binary forms therefore define a basepoint-free
morphism phi:P1->P2 with phi^*O(1)=O(D). Linear independence makes the
image a geometrically integral nondegenerate plane curve C of degree eta.

Work over an algebraic closure ONLY to bound geometric fibres. The image
of the geometrically integral P1 is geometrically integral; the homogeneous
substitution kernel commutes with field extension. Thus this is the same
eta as the required product-rank theorem, not a factor of a different degree.

Let pi:Ctilde->C be the normalization. Since P1 is normal, phi factors
through a nonconstant map psi:P1->Ctilde. Both curves are proper and
nonsingular over the algebraic closure. The map psi is finite and flat:
finiteness follows because a nonconstant proper curve map has finite
fibres; locally on the normal target, torsion-free modules over a DVR
are flat. Its rank is a positive integer nu. Every geometric fibre of
psi has scheme length nu and hence at most nu distinct points, even for
ramified or inseparable maps.

The invertible sheaf pi^*O_C(1) has degree eta. For example, a general
line meets only the smooth locus, and its pullback divisor has that total
degree. Pulling this divisor back along the finite flat map multiplies
its degree by nu, including all local multiplicities. Comparing with
phi^*O(1)=O(D) gives D=nu*eta.

If p has b_p geometric branches, pi^-1(p) consists of b_p distinct points.
Thus the full geometric phi-fibre has at most nu*b_p points. Removing
eigen roots or restricting to the actual finite domain only decreases it.
The proof does not assert that a singular fibre has size at most nu.

Standard normalization facts and the finite/flat curve-map statements are
recorded in [Stacks 33.41.2](https://stacks.math.columbia.edu/tag/0C1R)
and [Stacks 53.2](https://stacks.math.columbia.edu/tag/0BXX).
The degree multiplication above is the divisor-length calculation, not
an assumption of generic fibre size at every singular image point.
No field extension is made in the source or original owner accounting.
