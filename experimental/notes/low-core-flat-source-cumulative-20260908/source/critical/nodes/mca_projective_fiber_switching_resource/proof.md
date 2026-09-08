# Proof By A Coordinate Switch

## 1. Count Switches Out Of Good Tuples

For an ordered distinct-fiber tuple v, choose a position i, another
coordinate y in the same fiber as v_i, and a position j!=i. Replace v_j
by y. Since all original fibers are distinct, y is not any coordinate
already in v. The resulting tuple b still has r DISTINCT coordinates
and has exactly one repeated fiber, at positions i,j. All other fibers
are represented once. The number of switches out of v is exactly
(r-1)*sum_(x in v)(a(x)-1). Summing gives(r-1)W_r switches.

## 2. Bound Switches Into Each One-Collision Tuple

Fix an ordered distinct-coordinate b whose only fiber repetition is one
pair. There are exactly two choices for which of the repeated positions
was i (retained) and which was j (replaced). The removed coordinate v_j
must lie outside EVERY fiber represented in b. Conversely every such
coordinate and either orientation recover exactly one good input switch.

If S_b is the union of represented fibers, incoming multiplicity is
EXACTLY2(n-|S_b|). Since b contains r distinct coordinates, |S_b|>=r.
Thus it is at most2(n-r). If B_1 counts these one-collision tuples,

    (r-1)W_r <=2(n-r)B_1.

The sets G_r and B_1 are disjoint subsets of all(n)_r ordered distinct-
coordinate tuples. Divide by2(n-r)>0 and add|G_r| to prove SWITCH.
No independence or probabilistic approximation of collision events enters.

## 3. Sharpness And Polynomial Realization

With one doubleton and all other fibers singleton, every nongood tuple
has exactly one collision, and every such tuple has |S_b|=r. Both
inequalities above are equalities. Explicitly,

    (n)_r-|G_r|=r(r-1)(n-2)_(r-2),
    W_r=2r(n-2)_(r-1)>0.

Their ratio is exactly(r-1)/(2(n-r)), so any larger uniform coefficient
fails. This is an exact finite extremizer of the resource inequality.

For s=r-1>=3 set g(X)=X(X-1) and

    V=span{1,g,Xg,...,X^(s-2)g}.

These s polynomials are linearly independent and have degree<=s<r.
On n>r distinct field points containing0,1 the evaluation map is injective
by root count, so actual rank is s. All evaluations are nonzero because
1 belongs to V. Points0,1 give the same projective row. On every other
point, the ratio of Xg to g recovers X, so no other two projective rows
are equal and none equals the0/1 row. This realizes the sharp partition.
It is not a received-word or bad-slope extremizer.

## 4. Original-Source Interface

Use the required secant theorem's one explicit set E. Every agreeing
independent tuple outside E uses distinct nonzero source fibers, and
different finite labels own disjoint tuples. Pad zeros by singleton fibers:
their weight is zero, and allowing them only enlarges the resource.
Nonnegative weighting preserves ownership, so SWITCH bounds the weighted
independent tuples by(n)_r. The exceptional label charge is unchanged.

For a degree/source box, n<=n1 makes(r-1)/(2(n1-r))<=lambda_*(n).
Fix that ONE lambda for every record. Weighted core-counting inequalities
can be reused because their cost proofs hold for any nonnegative lambda;
their preceding sufficient Bonferroni CREDIT condition was used only to
bound the resource, which SWITCH now supplies directly. No circular
assumption of the row payment, new quotient receiver or label loss occurs.

The result is a double-counting refinement of the already proved
distinct-fiber resource. No general literature novelty is claimed.
