# Full-Fiber Scalar Incidences With Empty Universal Core

Status: PROVED by the hand argument; external independent review remains due.

Let n=R+K, m=d+K, R>=d>=1, 2<=s<=K, and let V be an actual
dimension-s polynomial space of degree <K on n distinct points over one
field. Fix a degree-<K polynomial h_* and a received pair (u,v). For a
finite set Gamma of distinct affine labels, fix h_gamma in h_*+V for each
gamma and an exact size-m scalar agreement
support that is pair-noncontained in the FULL degree-<K code. Assume

    {x: V(x)=0, u(x)=h_*(x), v(x)=0} is empty.

The selected explanations need not span V, be post-near, or have chosen
minimizing pairs. Partition the nonzero evaluations into COMPLETE projective
fibers A. Write a=|A| and z for the number of carrier-zero coordinates.
Choose f in V and ell in V* with ev_x=f(x)ell on A and f(x)!=0.
The actual receiver colors are

    ((u(x)-h_*(x))/f(x), v(x)/f(x)), x in A.

For a color C=(alpha,beta) of size t define the scalar-restriction family

    Gamma_(A,C)={gamma: ell(h_gamma-h_*)=alpha+gamma*beta}.

These families may overlap. Every selected incidence in C has its label
in Gamma_(A,C), even if a chosen minimizing pair has another restriction.

## Exact Child And Incidence Ledger

At most a-t labels E_(A,C) of this family agree at a point of A outside C.
All remaining labels admit a fixed same-field child, of degree K-a,
length n-a, actual carrier dimension s-1, and agreement m-t, with the
SAME labels, full-code badness and empty universal carrier core. If m-t
exceeds n-a there are no survivors. Otherwise exact bad subsets may reduce
the agreement to m-a, keeping the receiver and carrier fixed.

Let G(k) be any valid uniform upper bound for these empty-core families
with actual enclosing carrier dimension s-1 on (R+k,k,d+k), over the
same field, for every integer s-1<=k<=K-1. Then

    m|Gamma| <= sum_A a G(K-a)
                    +sum_A (a^2-sum_(C in A)|C|^2)+z.       (LEDGER)

The finer exceptional charge is sum_(A,C) |C| |E_(A,C)|; carrier-zero
incidences may likewise replace z by their actual count. Neither colors
nor fibers receive an independently spendable whole-family budget.

## A Two-Profile Upper Envelope

Suppose a twice continuously differentiable F on [s-1,K-1] is >=1,
nonincreasing and convex, and G(k)<=F(k) at every required integer k.
Put w=K-s+1 and b=(K-1)/(s-1). Then

    |Gamma| <= floor(max(S,U)/(d+K)),                        (PROFILE)
    S=w F(s-1)+(R+s-1)F(K-1)+w(w-1),
    U=(R+K)(F(K-b)+b-1).

For K=s only the single endpoint F(s-1) is used. Nonintegral b and
K-b are real partition relaxations, not new polynomial degrees. This
is a proved composition inequality with quantified proved cap inputs,
not a conjecture that a chosen recursive formula has the required shape.
It supplies no original near add-back or finite Prize-row payment itself.
