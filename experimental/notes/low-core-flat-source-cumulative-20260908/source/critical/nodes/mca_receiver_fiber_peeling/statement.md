# Peel Receiver Classes From One Projective Evaluation Fiber

Status: PROVED by the hand argument; independent external review remains due.

Let V have actual dimension s>=2 and degree <K over a finite field F,
h_* have degree <K, and D be n distinct points. Fix a received pair (u,v).
Every distinct finite gamma in Gamma has an explanation h_gamma in h_*+V
and a full-degree-<K-pair-code-bad scalar-agreeing support of size m=K+d,
where d>=1 and m<=n. Assume the universal carrier core is empty:

    {x:V(x)=0,v(x)=0,u(x)=h_*(x)}=empty.

Freeze a minimizing b_gamma in V on each selected support, and put
a_gamma=h_gamma-gamma*b_gamma. Its raw mismatch r_gamma is at least one.

Let A be one COMPLETE nonzero projective evaluation fiber of V on D,
of size a>=1. Choose ell in V* and f in V with ell(f)=1 so that
ev_x=f(x)*ell for x in A; f(x) is nonzero there. The actual receiver colors

    ((u(x)-h_*(x))/f(x), v(x)/f(x)) in F^2

partition A into classes C_(alpha,beta) of sizes t_(alpha,beta).
Each complete joint core for (a_gamma,b_gamma) meets A in precisely its
color class, or in the empty set if that color is absent.

## Heavy-Class Transport

For 0<theta<=1 call a color heavy when t>theta*a. There are at most
h=ceil(1/theta)-1 heavy colors. Assign each label by its frozen pair.

Let Q>=0 be a proved uniform cap for ALL selected full-code-bad families
of explanation affine dimension <=s-1 on degree K-a, agreement m-a,
length n-a rows over F, with arbitrary received values and distinct points.
No post-near or zero-core hypothesis may be required of this child cap.
Then the group assigned to a heavy color of size t has at most

    Q+(a-t)                                             (HEAVY)

labels. The transport keeps original finite slopes; at most a-t of them
are explicitly charged before dividing by the COMPLETE fiber locator.

## Remaining Labels Share One Basis Resource

Fix 1<=T<=d, put M=m-T, l=s-1, e=K-a-l>=0, c=M-K+1, and

    P_e(X)=X*prod_(i=1)^(l-1)(X-e-i),
    F_A(t)=P_e(M-t)*(s*t+max(c-t,0)),
    b_theta=min(F_A(0),F_A(theta*a),F_A(c) if c<=theta*a).

Let L>0 be a valid completed-weight floor for raw>T, in the normalization
of the required completed-basis resource, and P_d=prod_(i=1)^(s-1)(d+i).
The nonheavy labels satisfy the same-source bound

    |Gamma_light| <= floor(n_falling_(s+1) /
                         min((s+1)*b_theta,m*P_d*L)).    (LIGHT)

The heavy groups and light group are disjoint original labels, so

    |Gamma| <= h*(Q+a) + the right side of (LIGHT).       (PEEL)

This sum is justified by the actual receiver partition, not a free sum
of independently maximized child fibers. Inside LIGHT, LOW and HIGH
combine by maximum of their quotient bounds, not addition.

For theta<=1/s, F_A is nondecreasing on [0,theta*a], so b_theta=F_A(0).
No original near allowance is included here. Any original normalization,
near add-back, finite application and Prize conclusion belong to consumers.
