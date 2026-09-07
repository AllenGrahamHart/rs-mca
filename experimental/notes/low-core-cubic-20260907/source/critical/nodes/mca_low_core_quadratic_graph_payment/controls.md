# An actual canonical parabola beyond thirteen pencils

Use E=F_787 and F=E(beta), beta^2=2. The prime 787 is 3 modulo 8,
so 2 is nonsquare; in particular beta is not in E. Put

    P=X+beta, V=span_F{P,P^2}, h_*=0, K=3, m=30, d=27, T=1.

Partition D={0,...,782} into 27 consecutive groups of 29 points.
On group j, 1<=j<=27, define the received pair to be

    f_j=(j*P,j^2*P^2).

The complete core of f_j is exactly its group: P(x)!=0 and the first
values j*P(x) are distinct. Every represented pair lies on b=a^2.

## Exact bad-label census, including all carrier explanations

For every point x in group j and every i!=j, the explanation
h_i=a_i+gamma*b_i has one extra agreement at x for

    gamma=-1/((i+j)*P(x)).                              (3)

All 783*26=20358 labels in (3) are distinct. Equality of denominators
(i+j)(x+beta)=(i'+j')(x'+beta) forces i+j=i'+j' and x=x', by
E-independence of 1,beta. Then j=j', hence i=i'. Every relevant sum
lies in 3,...,53 and is nonzero modulo 787.

For any fixed source-piece explanation h_i, agreement on another group
j requires precisely (3). Consequently it has either its 29-point
core or that core plus the unique extra point. At each printed label
only one source-piece explanation reaches 30 points.

Every other allowed explanation h=alpha*P+eta*P^2 agrees at most
once on each group: divide by the nonzero P(x), and the difference
from the group's explanation is a nonzero linear polynomial in P(x).
Such an h therefore has at most 27<30 agreements. This proves that
there are no further eligible explanations or bad labels with an
explanation in the fixed carrier V, for any finite gamma in F. It is
not a census allowing arbitrary explanations outside this carrier.

Each printed label has raw exactly one. The second polynomial b_i matches
29 core points and fails at the extra point. Any degree-<3 polynomial
containing the full support would have to equal b_i on its 29 core
points, then fail at the extra point. Thus the support is full-code-bad.
There is no larger complete scalar agreement or another eligible carrier
explanation, so the all-explanation maximum raw is one. The canonical
guard 2T<d holds, and all 27 pairs occur.

## Neither previous pencil cover applies

For three distinct parameters i,j,k, the affine determinant is a
nonzero Vandermonde scalar times P^3. Thus no three of the 27 pairs
are collinear over F(X), and at least fourteen lines are necessary.
Every two-pair secant has nonconstant component direction, proportional
to (1,(i+j)P); a constant-direction line contains at most one pair.
Thus neither thirteen nonconstant lines nor one constant plus one
nonconstant line covers the family.

The verifier checks the entire exact label encoding (3), field inverses,
all parameter triples, and the original core/defect equations. The proof
above supplies the all-explanation and no-other-label assertions; no
enumeration of F-codewords or large symbolic elimination is required.
This is a genuine small-scope source, not a deployed KoalaBear unsafe
witness or a claim that all nonlinear sources are parabolic.

## Guard on the geometric degree charge

A zero-dimensional variety of degree two can contain two scalar list
points. Over F_5, the two constant polynomials a=0 and a=1 form such
a variety; on a four-point received word (0,0,1,1), both agree twice.
Here K=1,A=2. Dropping Delta from Delta*Q^dimension would incorrectly
bound the list by one. Dimension alone is not the new counting theorem.

## Characteristic and dimension guards

The characteristic restriction is substantive. In characteristic two let
V=span{1,X,X^2,X^4}, of dimension four. Every
a=c_0+c_1*X+c_2*X^2 has a^2=c_0^2+c_1^2*X^2+c_2^2*X^4 in V.
This three-dimensional family violates floor((4+1)/2)=2. The theorem
therefore cannot be extended to characteristic two merely by omitting the
division by two in its tangent proof.

In odd characteristic the dimension estimate itself can be sharp: with
V=F[X]_(<11), every a of degree <=5 has a^2 in V, yielding dimension
six. This is an algebraic-carrier example, not an over-budget source.
