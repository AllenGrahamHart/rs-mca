# Count Eigen-Root Incidences By Actual Line And Plane Capacities

Status: PROVED locally; independent mathematical review remains due.

Let U be a three-dimensional F-space of polynomials of degree<=D, with
NO common evaluation zero on an n-point domain. Let T:U->U have
one-dimensional eigenspaces for each eigenvalue in F. Write e in{0,1,2,3}
for their number. Actual pairs have the affine form f_*+(y,T(y)), y in S,
against one fixed receiver; every complete joint core H_y has size>=A.

Suppose each affine line parallel to an F-eigenvector contains at most q1
points of S, each affine plane contains at most q2, and 2*q1<=q2.
These are ACTUAL pair counts, not owner weights or formal hull sizes.
Let E be the union of roots of one eigenpolynomial per F-eigenvalue.
For e=0, E is empty. Then the aggregate core incidence on E satisfies

    sum_(x in E) |{y in S:x in H_y}|
       <= D*c_e,   c_e=(0,q2,q2+q1,3*q2/2)_e.          (CAPACITY)

In particular c_e<=3*q2/2 for every e. Coordinates of E are not
charged as though every represented pair agrees there.

## Fixed-Cardinality Consequence

Fix M>=2. The same capacities hold for any M-element subset of S.
Set B=D*c_e and S0=M*A-B. Suppose S0>=n and

    S0^2-n*S0 > n*M*(M-1)*H.                          (ENERGY)

If every two distinct actual cores have at most H common coordinates
outside E, there cannot be M represented pairs. Thus |S|<=M-1.
By the required spectral-fibre theorem, a bound on all actual nonzero
projective evaluation fibres outside E suffices for that intersection bound.

Because non-eigenvector differences give two independent degree-<=D
polynomials, their common zeros number at most D-1. Eigenvector
differences have no common zeros outside E. Thus H may be replaced by
min(H,D-1) in ENERGY. No generic-degree assumption is used.

More generally, if I2 is the SUM of pairwise core-intersection sizes outside
E over the unordered pairs of an actual M-subset, then
2*I2>=S0^2/n-S0. Thus ENERGY forces I2>binom(M,2)*H even without a
uniform intersection cap. This statement is about actual pairs, not directions.

The common-zero exclusion, repeated-eigenvalue case and factor3/2 are
load-bearing. This theorem needs proved q1/q2 capacities; it does not
assert them for an arbitrary polynomial operator, or a universal MCA bound.
