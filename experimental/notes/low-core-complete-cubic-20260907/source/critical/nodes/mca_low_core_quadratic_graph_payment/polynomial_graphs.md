# Uniform polynomial-graph extension

The later `rational_coefficient_graphs.md` proves the same bounds for
F(X)[Y] by a different two-tangent argument. The polynomial-X proof
below remains valid at its original scope; its rational-coefficient
limitation is not a counterexample to that extension.

Status: PROVED, 2026-09-07. Keep the original exact support-margin and
common-carrier setup. Replace b=a^2 by the POLYNOMIAL pair identity

    b=Psi(X,a),   Psi(X,Y)=sum_(i=0)^e p_i(X)*Y^i,
    p_i in F[X], e>=2, p_e!=0, e nonzero in F.            (PG)

One fixed constant invertible matrix and degree-<K polynomial pair
offset may first identify the graph, exactly as in the earlier theorem.
There is no bound on deg_X p_i in the identity formulation. Coefficients
are polynomials, not arbitrary rational functions of X.

Put

    r_e=floor((s+1)/2)                  if e=2,
    r_e=max(1,floor(s/2))               if e>=3,
    Delta_e=e^(s-r_e), Q=(n-K+1)/(m-T-K+1).

Then the number M of distinct represented LOW pairs and the original
selected labels satisfy

    M<=floor(Delta_e*Q^r_e),
    |Gamma|<=C_s/(T+1)+(n-m+T)*floor(Delta_e*Q^r_e).      (PGB)

This is one degree-parameterized theorem, not an assertion that all
families have such a graph or a collection of open per-degree targets.
The coefficient-family dimension is at most r_e on EVERY geometric
component, with a degree charge retained in the count.

## 1. Use the highest coefficient that actually varies

Over an algebraic closure k consider the coefficient locus

    X={a in a_0+V: Psi(X,a) belongs to b_0+V}.

It is cut out by equations of degree <=e in the s coefficients of a.
Let Y be a positive-dimensional reduced irreducible component. There
is a largest polynomial coefficient index D whose value is nonconstant
on Y. All coefficients above D are constant on Y. Subtract a fixed
polynomial a_* with those higher coefficients. Thus h=a-a_* has
degree at most D on Y and its coefficient lambda at X^D is a
nonconstant function on Y. Every tangent vector w of Y has degree
<=D and belongs to V. If D=0 the tangent space of Y is contained in
the constants, so dim Y<=1.

Assume D>0. Here Psi_Y denotes differentiation in the second polynomial
argument. Write

    Psi_Y(X,a_*+H)=sum_(j=0)^(e-1) c_j(X)*H^j.

All c_j are polynomials and c_(e-1)=e*p_e is nonzero. Define

    delta=max_(c_j!=0)(deg c_j+j*D) >=(e-1)*D.          (1)

At the generic point of Y, the coefficient of X^delta after H=h is

    sum_(deg c_j+jD=delta) lc(c_j)*lambda^j.

This is a NONZERO polynomial in lambda: distinct indices j give distinct
powers. A nonconstant function on an irreducible variety over the
algebraically closed field k is transcendental over k. Thus this leading
coefficient cannot vanish identically on Y. Choose a point in the nonempty
open set where it is nonzero. At this point R=Psi_Y(X,a) has degree
delta, and every tangent vector w of Y satisfies

    w in V, deg w<=D, R*w in V.                          (2)

This addresses possible leading-term cancellation rather than assuming
that a generic polynomial has the advertised degree. The fixed higher
coefficients of a are removed before D is chosen.

## 2. Two sets of leading degrees in the SAME carrier

Let W be the vector space defined by (2), of dimension t. Its t
distinct leading degrees form S subset {0,...,D}. Multiplication by
R gives t leading degrees delta+S, also in the leading-degree set of V.

For e=2, delta>=D, so the two sets intersect in at most one degree.
Hence 2t-1<=s. For e>=3, delta>=2D>D, so they are disjoint and
2t<=s. The tangent dimension bounds dim Y, proving dim Y<=r_e.
The D=0 case explains the max(1,...) in the higher-degree formula.
Zero-dimensional components require no tangent argument.

Polynomial coefficients matter in (1): a rational coefficient can have
negative degree and destroy delta>=(e-1)D. The field condition matters
as well: when the characteristic divides e, the leading derivative can
vanish. The explicit characteristic-three cubic control demonstrates an
actual dimension failure without that condition.

## 3. Degree charge and original slope count

Apply section 3 of `algebraic_list_bound.md` with equation degree e
and dimension r_e, then its LIST incidence bound. Projection to a is
injective on graph pairs. Each actual core has at least m-T points of
first-coordinate agreement, so the pair bound in (PGB) follows.

The original-coordinate argument in `proof.md` is unchanged: labels
assigned to one pair consume disjoint points outside its COMPLETE core.
All LOW labels are bounded by (n-m+T)*M. The original margin resource
and HIGH labels occur once, proving the full count in (PGB). No
nonlinear transformation of the MCA problem is used.

## 4. A sufficient received-word certificate for the identity

Let U be the COMPLETE LOW core union in the transformed coordinates,
with received pair (u_*,v_*). Suppose

    v_*(x)=Psi(x,u_*(x)) for every x in U,
    max_(p_i!=0)(deg p_i+i*(K-1)) < m-T.                (CERT)

Then every represented LOW pair satisfies (PG). Indeed the polynomial
b-Psi(X,a) has degree <m-T, since deg b<K<=m-T, and vanishes
on its at-least-(m-T)-point complete core. It is therefore identically
zero. A sharper certified first-component degree D_a can replace K-1
in (CERT); no empirical degree estimate is substituted for a bound.

This is a direct sufficient bridge from received data to a paid class,
not a proof that the certificate always exists. An arbitrary high-degree
pointwise graph fit is insufficient; the actual one-defect control in
`polynomial_graph_controls.md` falsifies that shortcut.
