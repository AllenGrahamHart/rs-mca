# Multiplicity interpolation escapes a prescribed polynomial curve

The [all-multiplicity boundary](cubic_recipe_boundary.md) proves failure
of the degree-three full-kernel dimension criterion on 9981..169999
for EVERY multiplicity and positive cutoff. This is a proved limitation
of one recipe, not a source counterexample. The convex shell and analytic
r>=5 argument are upstream of any finite consumer; no new req is added.
Earlier escape and cover statements retain their printed scopes.

Status: PROVED by the hand argument in proof.md; external review due.

Let F be any field, D a set of n distinct field elements, and (u,v) an
arbitrary received pair on D. Fix integers w>=1, 1<=A<=n, r>=1. Count
polynomial pairs (a,b) over F of component degrees <=w with at least A
JOINT agreements. Let G be an irreducible nonconstant curve in F(X)[Y,Z]
of total pair degree g. Choose its primitive F[X,Y,Z] representative.

For an integer d, define the full weighted polynomial-space dimension

    Phi_w(d)=sum_(i>=0) (i+1)*max(d-i*w,0),
    Phi_w(d)=0 if d<=0.

The sum is finite. If

    Phi_w(r*A)-Phi_w(r*A-g*w) > n*binom(r+2,3),        (ESC)

then the number of these rich polynomial pairs on G is at most

    g*floor((r*A-1)/w).                               (COUNT)

No common finite-dimensional carrier, curve smoothness, normalization,
coefficient height, chosen component dimension or numerical family coverage
is assumed. Singular points and isolated coefficient solutions are counted.
The actual rich pairs need not exhaust the curve's function-field points.
No code coordinate or original slope is removed. The theorem counts pairs;
MCA label/resource/near conversion belongs to its finite consumer.

The r=2 specialization imposes FOUR conditions at each received triple:
Q=Q_X=Q_Y=Q_Z=0. Imposing only the two pair derivatives is insufficient.
General r uses Hasse jets and is characteristic-free.

The proved companion `kernel_corollary.md` uses the SAME inequality
with a degree threshold g0 to force the entire multiplicity kernel's
gcd to have degree <g0, with at most ell^2 off-gcd rich pairs. Its
factors have weighted degree <r*A, not the old simple-point bound <A.
For normalized 9527..9821 it gives degree<=3 and <=256 exceptions.
The finite consumer and full-kernel child now supply that interval's
factor accounting separately in `double_point_cubic_tail.md`.
