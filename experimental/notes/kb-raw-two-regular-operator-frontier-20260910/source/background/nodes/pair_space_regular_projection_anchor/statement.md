# Shared Anchors Can Preserve Full Generic Projection At The Same Cost

Status: PROVED locally; independent mathematical review remains due.

Let D be n distinct field points, V subset F[X]_<K have dimension s,
and W subset V x V have dimension r with s<r<=2s. Assume the formal
projection pi_z(a,b)=a+z*b is onto V over F(z). Write c=2s-r.

There is a coordinate set B whose evaluation functionals span a space
of dimension at most c, with |B|<=K+s-r, such that every x outside B
has joint evaluation rank two on W and

    dim V_x=s-1, dim W_x=r-2,
    pi_z(W_x)=(V_x)_(F(z)).                         (REGULAR)

Here V_x consists of polynomials vanishing at x and W_x consists of
pairs whose components both vanish there. A nonempty affine joint
agreement section has this same direction space. An actual subfamily
need not span its enclosure, and its image need not exhaust that hull.

For nonnegative fixed owner weights, if every object has at least A
joint agreements, K+s-r<A<=n, and every retained child has weight<=L,

    total weight <= (n-K-s+r)/(A-K-s+r)*L.        (WEIGHT)

Thus full generic projection can be preserved at the same worst-case
anchor cost as the usual joint-rank lemma. Joint rank two ALONE does
not suffice for preservation; the verifier gives a strict small example.

If a terminal pair space has r=s=c and full generic projection, and
|F|>c, some finite alpha makes pi_alpha invertible. Under this auxiliary
coordinate choice it is the graph {(y,T*y):y in V} of an F-linear
operator T:V->V, after replacing the first component by a+alpha*b.
No diagonalization, splitting field or change of original labels is used.
