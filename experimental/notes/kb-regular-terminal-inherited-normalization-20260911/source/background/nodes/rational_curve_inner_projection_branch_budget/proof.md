# Low Degree Supplies The Needed Separability

Work over the algebraic closure to prove the geometric statement. Suppose
projection from a GENERAL curve point were nonbirational. The correspondence
of three distinct collinear normalization parameters a,b,c then has a
component dominating the (a,b) plane. Every pair projection of this component
is generically finite and dominant. Otherwise, fixing one general parameter
would leave only finitely many possibilities for the third and would put
the varying curve point on finitely many fixed lines; irreducibility would
put the curve in one line.

The degree of each pair projection is at most d-2 INCLUDING inseparability.
Over the function field of a general pair, choose a hyperplane containing
its secant line but not the curve. Its pullback to the normalization is a
degree-d divisor containing both known parameters. The residual collinear
parameter scheme has length at most d-2, so the degree of each component's
function field over that pair field has the same bound. This is a scheme
length bound, not merely a count of distinct points. Since d<p, these field
extensions are separable; in characteristic0 this is automatic.

In an affine chart write gamma(c)=u*gamma(a)+(1-u)*gamma(b), u not0,1.
Use local separating parameters on the rational normalization. Separability
of the (a,b), (a,c) and (b,c) projections implies both c_a and c_b are nonzero.
Differentiation gives

    gamma'(c)*c_a = u*gamma'(a)+u_a*(gamma(a)-gamma(b)),
    gamma'(c)*c_b = (1-u)*gamma'(b)+u_b*(gamma(a)-gamma(b)).

Modulo the secant direction, gamma'(a) and gamma'(b) are proportional.
Thus two general projective tangent lines are coplanar and intersect.
An irreducible family of pairwise intersecting lines is either planar or
concurrent: fix two lines meeting at o; any line meeting both lies in their
plane or passes through o, and irreducibility selects one of these loci.

The planar case puts C in a plane, contradicting nondegeneracy for r>=3.
In the concurrent case, projection from o is nonconstant but has zero
differential. In positive characteristic its function field lies in the
p-th powers on the rational normalization, so its degree is at least p.
But every nonconstant point projection of a degree-d curve has degree at
most d, by the full fixed-divisor degree identity.
This contradicts p>d. In characteristic0 zero differential is already
impossible. Therefore general inner projection is birational.

Its centre can be chosen smooth and outside any prescribed proper closed
subset. Its fixed divisor on the normalization has degree1, so its image
degree is d-1. This remains within the characteristic bound and permits
iteration while the ambient dimension is at least3.

The numerical branch budget and its original-coordinate conversion are
proved in branch_charges.md. No characteristic-zero theorem is transplanted
to the official field without the above separability argument.
