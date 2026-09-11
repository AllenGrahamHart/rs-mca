# Null Geometry Constrains The Union Of Line Trees

Use the polar bilinear form B. In a nondegenerate three-space, a totally
isotropic subspace has dimension at most1: W subset W-perp implies
2dim W<=3. Thus null vectors orthogonal to each other are proportional.

Edges from distinct affine lines cannot repeat. If three points are
pairwise null-separated, subtracting one point gives two null orthogonal
vectors, hence they are collinear. Any graph triangle would therefore lie
on a single null line. All its edges come from that line's single tree,
which is impossible. The graph is triangle-free.

For noncollinear centres a,b,c, a common neighbour x solves Q(x-a)=
Q(x-b)=Q(x-c)=0. Subtraction gives two independent affine linear equations
by nondegeneracy of B. Their solution set is an affine line. Its quadratic
restriction has at most2 roots unless the line lies in all three cones.
In that exceptional case its direction v is null and its displacement
from each centre is null and orthogonal to v. Each centre would lie on
that line, a contradiction. So at most2 common neighbours exist.

For three distinct collinear centres a+t_i*v, these same equations say a
quadratic in t has three roots. Its coefficients vanish: Q(v)=0,
B(x-a,v)=0 and Q(x-a)=0. Thus every common neighbour is on the same null
line. Two common neighbours would create a K_(3,2) cycle in its single
tree. There is therefore at most1 common neighbour in the collinear case.

## Edge Bound

For a triangle-free graph on s vertices with E edges and degrees d_v,
each edge uv has d_u+d_v<=s. Hence sum d_v^2<=sE; Cauchy gives
4E^2<=s^2*E and E<=floor(s^2/4). The number of independent triples is

    I3=binom(s,3)-E*(s-2)+sum_v binom(d_v,2).

Any triple with a common neighbour is independent. Counting such triples
with their common neighbours gives sum binom(d_v,3)<=2*I3. Rearrangement
using sum d_v=2E yields sum phi_s(d_v)<=2*binom(s,3).

For integer0<=d<=5, phi_s(d)-(s-4)d=d(d-4)(d-5)/6>=0. Above5 the
successive slopes of phi increase; the first slope is s-2>=s-4.
Thus psi is convex and below phi on all integer degrees0..s-1.
Jensen gives s*psi_s(2E/s)<=sum phi_s(d_v)<=2*binom(s,3), proving K_s.
No unproved graph extremal conjecture or incidence theorem is used.
