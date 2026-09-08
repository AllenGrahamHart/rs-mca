# Fiber Contraction And Quadratic Basis Bounds

Status: PROVED by the hand proof; external independent review remains due.
The degree, rank and size parameters D,E,K,r below are positive integers,
with r>=2 for contraction so that the annihilator has positive dimension.

Let V be an r-dimensional polynomial space of degree <K over any field,
evaluated at N=D+K distinct points H, with every evaluation nonzero.
Write B_r(V,H) for the number of independent ORDERED r-tuples of its
evaluation functionals. All dimensions and coordinates are actual.

## Exact Contraction

Partition H into projective evaluation fibers of sizes a_i. For each
fiber A_i let V_i be the annihilator of an evaluation in that fiber,
divided by its full locator. Then dim V_i=r-1, deg V_i<K-a_i,
and all N-a_i remaining evaluations are nonzero. Exactly

    B_r(V,H)=sum_i a_i B_(r-1)(V_i,H minus A_i).       (CONTRACT)

The gap D is unchanged. No receiver, field or slope is descended.

## Rank-Three Seed

For r=3 and 3<=K<=D,

    B_3(V,H)>=(D+1)(D+K)(D+(K+1)/2).                 (SEED)

## Quadratic Step

Fix 4<=r<=E<=D. Suppose the quadratic F(k)=A+B*k+C*k^2, with
C>=0 and B>=D*C, is a proved lower bound on B_(r-1) for EVERY
such nonzero-evaluation space of degree <k on D+k points, for all
integer r-1<=k<=E. No sign condition on A is needed. For r<=K<=E,

    B_r(V,H)>=min(S_r(K),U_r(K)),                    (STEP)
    S_r(K)=(K-r+1)F(r-1)+(D+r-1)F(K-1),
    U_r(K)=(D+K)F(((r-2)K+1)/(r-1)).

The argument of F in U_r may be fractional: this comes from a real
relaxation of the fiber partition, not a fractional-degree source.
The seed and step are hand-proved universal statements. They do not
follow from a finite collection of numerical carrier examples.

## Return To Selected MCA Slopes

For an actual dimension-s fixed affine explanation carrier, full-code-bad
size-m supports and empty universal carrier core, a raw<=T record has
at least m-T nonzero joint-core evaluations. If every such core subset
has at least B ordered bases, inserting one actual defect gives at least
(s+1)*B independent incidence tuples for that record. Distinct finite
slopes own disjoint tuples. LOW and HIGH consume one original tuple
budget; their separate quotient bounds combine by maximum, not addition.
This interface uses the required completed-basis resource. It does not
itself supply an original-source normalization or a prize-row conclusion.

The [method boundary](method_boundary.md) constructs actual raw-one
records showing why a uniform isolated-core charge with the coarse global
tuple budget cannot by itself pay all the remaining smaller-J rows.
This does not construct an unsafe line or a full original rank-twelve family.
