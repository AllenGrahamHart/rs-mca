# Exclude Annihilators Of The Generic Projection Kernel

Extend scalars to F(z). The projection kernel is

    ker(pi_z|W)={(-z*g,g):g in U_z}, dim U_z=r-s.

Let E be the CONSTANT functionals in U_z^perp, a subspace of V*.
Linearly independent F-valued coefficient vectors remain independent
over F(z), so dim_F E<=s-(r-s)=c. Define B to contain precisely those
coordinates x whose evaluation ell_x annihilates U_z; this includes
zero evaluations. All their functionals lie in E. Their common
annihilator in V has dimension at least s-c=r-s>0 and vanishes on B.
The usual root-flat dimension count gives |B|<=K-s+dim E<=K+s-r.

## Every Retained Section Is Joint-Good And Regular

Fix x outside B. Evaluation on U_z is nonzero, hence onto F(z).
For any h in (V_x)_(F(z)), choose (a,b) in W_(F(z)) with a+z*b=h.
Choose g in U_z with g(x)=-b(x), and add (-z*g,g). The resulting
pair still projects to h, while both its components vanish at x.
This proves pi_z(W_x)=(V_x)_(F(z)).

Joint evaluation has rank two: kernel vectors (-z*g,g) yield a
nonzero evaluation in direction(-z,1), and an h with h(x)!=0 yields
a direction outside that line. Since the joint evaluation matrix has
entries in F, its rank over F is also two. Thus dim W_x=r-2 and
dim V_x=s-1. Scalar extension commutes with these constant linear
equations. Nonempty affine sections translate this same kernel.

For weights omega_f>=0, count good joint agreements with the ORIGINAL
weights. If b=|B| then (A-b)*sum omega_f <= (n-b)*L. The ratio
(n-b)/(A-b) increases for b<A because A<=n. Insert the proved bound
b<=K+s-r to get WEIGHT. No owner weight is reset or subdivided.

The strict r>s guard is essential: at r=s the projection kernel is
zero, so every coordinate belongs to B and this root-flat proof fails.
Such a terminal must be handled separately, not anchored by this lemma.

## A Square Regular Terminal Is An Operator Graph

When dim W=dim V=c, write pi_z in fixed bases. Its c-by-c matrix has
entries of degree<=1, and its determinant is a nonzero polynomial of
degree<=c. If |F|>c there is alpha in F with nonzero determinant.
Let y=pi_alpha(a,b). The inverse of pi_alpha identifies W with V;
define T(y)=b. Then (a,b)=(y-alpha*T(y),T(y)). Replacing the first
component by a+alpha*b gives the graph of T, over the ORIGINAL field.

For an original label gamma its projected value is
(I+(gamma-alpha)*T)y. This rewrites the same label, not a deletion or
reassignment. The case c=0 is the single zero direction. Neither
Jordan decomposition nor existence of eigenvalues in F is assumed.
