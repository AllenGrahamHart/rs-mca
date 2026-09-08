# Proof: Eight Fixed Quadratic Certificates

## 1. Universal Core-Basis Ladder

Put D=67466, E=65000, X=5000 and P_r=prod_(i=1)^(r-1)(D+i).
The required contraction theorem applies to nonzero polynomial evaluations
on D+K points, rank r and degree <K, whenever r<=K<=E<=D.
We prove a universal lower bound P_r*q_r(K), with

    q_r(K)=a_r+b_r*K+c*K^2, c=1/[2(D+2)].

The rank-three seed gives

    a_3=D(2D+1)c, b_3=(3D+1)c.

For r=4,...,11 let a=a_(r-1), b=b_(r-1), H=D+r-1,
alpha=(r-2)/(r-1), beta=1/(r-1), and f=q_(r-1)(r-1).
The contraction theorem's two profiles, after division by P_r, are

    S(K)=s_0+s_1*K+c*K^2,
    s_1=b-2c+f/H, s_0=a-b+c-(r-1)f/H,
    U(K)=(D+K)*q_(r-1)(alpha*K+beta)/H.

Write U=u_0+u_1*K+u_2*K^2+u_3*K^3. Explicitly,

    u_3=c*alpha^2/H,
    u_2=(b*alpha+2c*alpha*beta+D*c*alpha^2)/H,
    u_1=(a+b*beta+c*beta^2+D*(b*alpha+2c*alpha*beta))/H,
    u_0=D*(a+b*beta+c*beta^2)/H.

In all eight steps the exact certificates give b>=D*c and u_2>=c.
Hence U-c*K^2 is convex on K>=0. Its tangent at the SAME fixed X is

    T(K)=t_0+t_1*K,
    t_1=u_1+2(u_2-c)X+3u_3 X^2,
    t_0=u_0-(u_2-c)X^2-2u_3 X^3.

Define the nonnegative shift

    eta=max(0,T(r)-s_0-s_1*r,T(E)-s_0-s_1*E),
    a_r=t_0-eta, b_r=t_1.

Then q_r<=S on the WHOLE interval [r,E], because their difference
is affine and nonnegative at both endpoints. Moreover

    U(K)-q_r(K)
      =eta+(K-X)^2*((u_2-c)+u_3*(K+2X))>=0 for K>=0.

The exact next-stage gate b_r>=D*c holds in every step. This proves
the universal bound by induction; no hull search, selected source model
or unchecked interpolation between numerical J samples is used.

For orientation, the certificate's (floor a_r,floor b_r) pairs are
(67182,2), (66657,2), (65876,3), (64820,4), (63467,5), (61794,6),
(54204,7), (39186,8). These rounded values are NOT used as bounds.
The shift vanishes at ranks 4..9 and is positive at ranks 10 and 11.
The printed rational recurrence fixes every coefficient exactly.

## 2. LOW Records On The Entire New Interval

Set T=6. For every raw<=6 record, choose a fixed m-6=J+D subset
of its complete joint core. Empty universal carrier core makes all its
V-evaluations nonzero. The preceding bound at r=11 and K=J applies.
Insert one of its nonzero number of actual defects. The contraction
supplier's incidence interface gives at least 12*P_11*q_11(J) tuples.

Put L=53000, q=q_11 and U_0(J)=(1048576+J)_falling_12. The exact
certificate gives q(L)>0, b_11>=D*c>=0, and

    (b_11+2cL)*(1048576+L-11) > 12*q(E).

For L<=J<=E, q is positive increasing, and

    (log q)' >= (b_11+2cL)/q(E)
       >12/(1048576+L-11) >= (log U_0)'.

Thus U_0(J)/(12*P_11*q(J)) is decreasing throughout this real interval.
Its exact floor at L, plus the original allowance 134944, is

    274171207928811099.                              (LOW)

## 3. HIGH Records Use The Same Resource

The completed-basis resource used by the required suppliers has
P_d=prod_(i=1)^10(67472+i). Its HIGH raw>=7 weight is at least
10488/125: the value at seven exceeds 84(1-77/67473), it increases
on 7..84 since 12*84<67473, and the truncated weight beyond 84 is
at least 84, including margins above d.

The common resource U_0(J)/[(67472+J)P_d] is convex in J. With
y=67472+J its expansion is a positive polynomial plus a positive
multiple of 1/y. The exact endpoint ceilings on [L,E] are at most

    C_0=14024864706947406176.

Consequently the HIGH quotient plus 134944 is at most

    floor(125*C_0/10488)+134944=167153707891861276.    (HIGH)

LOW and HIGH share ONE tuple budget. Dividing by the smaller per-record
lower count, their resulting bounds combine by MAXIMUM, not addition.
(LOW) exceeds (HIGH), proving (CONTRACTION). The existing maximum-density
supplier pays [65000,169999] by 274929007493481160. The maximum of
these two whole-source alternatives proves (UNION), including the single
shared endpoint. Subtracting from the original field budget gives the
stated reserve. This node does not perform original-source normalization.

## Provenance

This is the finite consequence of the new local contraction proof and
the already proved completed-basis/maximum-density suppliers. The earlier
affine-envelope experiment was weaker and is not a proof dependency.
The stronger quadratic certificate was selected by a tiny exploratory
search, then frozen to eight identical tangent choices and reconstructed
independently by polynomial multiplication. No external extremal theorem,
unproved carrier classification or numerical survival premise is imported.
