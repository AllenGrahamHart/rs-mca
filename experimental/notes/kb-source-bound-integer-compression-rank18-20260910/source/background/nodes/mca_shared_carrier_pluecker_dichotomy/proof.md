# The Exterior Product Detects The Entire Child

At good x the two component covectors a_x,b_x are independent and
K_x=ker a_x intersect ker b_x. Choose a basis of W* beginning with
a_x,b_x. A two-form vanishes on Lambda^2 K_x exactly when each of its
terms contains a_x or b_x, equivalently its wedge with a_x wedge b_x
is zero. Thus the child has function-field rank one precisely when

    p_y wedge p_x=0 identically as a polynomial in y.

Division by Y-x changes its two-by-two determinants by the common factor
(Y-x)^2 and does not change whether they vanish identically. The child
dimension equals dim U_x=s-1, so the required full-carrier rigidity makes
each rank-one child constant-direction.

Each coordinate of p_x is a determinant of two degree-<K polynomials,
hence has degree at most2K-2 in x. Expand p_y wedge p_x in y and in
an exterior basis. If one coefficient is nonzero, all good rank-one-child
coordinates are its roots. This proves the sparse alternative, without
chart denominators, deleted roots or a nonzero-field-value inference.

## The Identity Alternative

Suppose instead the full bivariate exterior product is zero. For good
x let L_x=span(a_x,b_x) in W*. These two-planes are pairwise intersecting.
They either share a line or all lie in one three-dimensional subspace.
To see this, choose distinct planes with intersection line L. A third
plane not containing L lies in their three-dimensional sum, since it
meets both along distinct lines. Every other plane must then lie in that
sum: a plane outside it meeting both first planes contains L and cannot
meet the third. If no such third plane exists, all planes contain L.
Identical planes also fall under the common-line alternative.

The three-space case is impossible. The common annihilator has dimension
at least(s+1)-3=s-2>0. Its polynomial components vanish at every good
coordinate. The shared-carrier bound gives at most K-1 bad coordinates,
so there are at least N-K+1>K-1 good ones. Root count forces both
components of each annihilator vector to vanish identically, a contradiction.

Consequently some nonzero lambda in W* lies in every L_x. Its kernel H
has dimension s. At every good x, the evaluation of H has rank<=1.
Every determinant of two members of H has degree<=2K-2 and vanishes
at more than that many good coordinates. Therefore all such determinants
vanish as polynomials: H has function-field rank one. Equality rigidity
at dim H=dim U=s gives H=delta tensor U with delta constant over F.
Choose z outside H to obtain W=(delta tensor U) direct_sum F z.

Conversely, in such a decomposition at a good coordinate the evaluation
of z is independent of delta. A vector in the joint kernel must have
zero z coefficient, and that kernel is delta tensor ker(ev_x on U).
Every good child is therefore constant. All constructions are over the
original field and work in every characteristic; no division by2 occurs.
The coefficient polynomials in x have degree<=2K-2, so vanishing on all
good x also gives the full bivariate exterior identity in this converse.
