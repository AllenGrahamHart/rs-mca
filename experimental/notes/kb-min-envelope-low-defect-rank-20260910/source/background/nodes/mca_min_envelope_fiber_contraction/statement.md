# Fiber Endpoints For A Minimum Of Smooth Branches

Status: PROVED. Independent mathematical review remains due.

Fix integers4<=r<=E<=D and a nonzero-evaluation rank-r degree-<K polynomial
space on N=D+K distinct points, r<=K<=E. Let F=min_i F_i on[r-1,E],
where the family is finite and nonempty and each F_i is twice continuously
differentiable. Suppose F is a valid ordered-basis LOWER bound for every
rank-(r-1) child of degree<k on D+k points, integer r-1<=k<=E.

Require, pointwise on the whole real child interval, for every branch:

    F_i'>=0, F_i''>=0,
    2F_i'>=E*F_i'',
    2(r-2)F_i'>=(D+E)*F_i''.                            (SHAPE)

Then the parent ordered-basis count satisfies

    B_r >= min(S_r(K),U_r(K)),
    S_r(K)=(K-r+1)*F(r-1)+(D+r-1)*F(K-1),
    U_r(K)=(D+K)*F(((r-2)*K+1)/(r-1)).                  (ENDPOINT)

The minimum F itself need NOT be convex or differentiable. No Jensen
inequality is applied to F. Branches need not separately bound actual
children; only their pointwise minimum must do so. Conditions(SHAPE)
are explicit analytic gates, verified by the finite consumer, not open
mathematical conjectures or a claim that every polynomial satisfies them.

The existing exact full-fiber contraction and rank-three seed are the
required inputs. All contractions concern actual local evaluation spaces;
no MCA receiver, original label, carrier or field is descended here.
