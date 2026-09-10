# Use The Common Annihilator Before Maximizing Individual Fibres

Choose a constant row rho annihilating delta. Then g=rho(z) is a
nonzero polynomial. Otherwise z=delta*h for a polynomial h in U, by
using any nonzero constant component of delta, contradicting the direct
sum. The original polynomial H_a*g has degree at most K-1.

Choose a quotient coordinate with kernel delta tensor U and value1 at z.
For a pair f apply it to(f-f_*)/H_a. Changing base or scaling this
coordinate merely affinely relabels the fibres, so they partition the
actual family independently of these choices. For c!=c', a point in
C_c intersect C_c' lies in the core of some pair in each fibre. Those
pairs both equal the receiver there; applying rho to their difference
gives(c-c')*H_a(x)*g(x)=0. Thus the unions are disjoint outside one
common root set of size h<=K-1.

With nu>=1 occupied fibres, sum_c |C_c|<=n+(nu-1)h. Subtracting
nu*(K-1) proves(PACK). Also each occupied union contains a core of
size>=A, so x_c>=A-K+1>0. Empty families have zero weight separately.

## Inject Each Fibre Into A Scalar LIST

Choose an actual pair f_c in its fibre and a constant row mu with
mu(delta)=1. Map f to h_f=mu(f-f_c)/H_a. This polynomial lies in U
and the map is injective: every fixed-c difference is H_a*delta times
a unique element of U. On C_c minus the a anchors use the scalar
receiver mu((u,v)-f_c)/H_a, defined pointwise. Every f has at least
A-a remaining joint agreements, each of which is a scalar agreement.
The length is |C_c|-a=x_c+K-1-a, degree bound K-a, and affine
dimension is the ACTUAL represented scalar span, not an ambient label count.

This is an auxiliary count over the same field. Only pair differences
are divisible by H_a; neither receiver nor base pair is asserted to be.
All pairs, original labels, weights and complete cores remain unchanged.

Every fibre is a constant-direction pencil with the same delta. By the
weighted-owner proof, each nonpreferred pair's original raw weight is at
most n-|C_c|, and all preferred labels together have weight at most t.
The preferred finite slope, if present, is the single solution of
delta_0+gamma*delta_1=0, common to all fibres. Hence the weight is
at most t+sum_c(n-K+1-x_c)*L(x_c). Divide each summand by the
positive x_c, apply its supremum, and use(PACK) once. This proves(OWNER).

The common mass inequality is essential. Replacing each fibre separately
by a largest possible list and then multiplying by a separately maximized
fibre count would discard the coupling that supplies this bound.
