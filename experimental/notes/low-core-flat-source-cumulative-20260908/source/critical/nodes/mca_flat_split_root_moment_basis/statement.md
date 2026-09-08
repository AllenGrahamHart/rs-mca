# A Complete Flat Improves The Root Moment Of The Basis Recursion

Status: PROVED by the hand argument; external independent review remains due.

Let V have actual polynomial rank s>=3 and degree<K on N=D+K distinct
nonzero evaluations, D>=1. Every proper rank-j coordinate flat has size<=j*h.
Fix ANY complete rank-t flat A of size a, 1<=t<s. Put ell=s-t, k=K-a.
No maximum-density premise on A is needed. Define

    Q(n,k,1)=n^2,
    Q(n,k,r)=max(n*(k-1)/(r-1), n+(k-r+1)*(k-r)) for r>=2.

If S2 is the second moment of the ORIGINAL projective fiber sizes, then

    S2 <= a*h + min((N-a)*h,Q(N-a,K-a,ell)).             (SPLIT)

Also S2<=N*h. If C is any proved upper bound on the number of ordered
equal-fiber pairs in this core, then S2<=N+C.

Freeze the EXISTING rank-profile coefficients mu_r for the ORIGINAL rank s,
density h and a whole degree box K0<=K<=K1. Let F_(s-1)(D,x) be its
positive convex product using the SAME coefficients mu_3,...,mu_(s-1).
If S2/N<=q, with K-q>=1, then

    ordered s-bases >= N*F_(s-1)(D,K-q).                (ROOT)

In particular q may be the minimum of the split mean, h, a separately
proved collision mean, and the old root-profile mean mu_s*(K-1).
It may be smaller than (K-1)/(s-1). No unguarded balanced product is used.

For a box a0<=a<=a1, density<=h1, use N0=D+K0, k1=K1-a0 and

    q0=min(h1,mu_s*(K1-1),
           (a1*h1+min((D+k1)*h1,Q(D+k1,k1,ell)))/N0).

Add 1+C/N0 to this minimum if the collision cap C holds uniformly.
When K0-q0>=1, a whole-box lower bound is
N0*F_(s-1)(D,K0-q0); otherwise use zero. The outside quotient is used
only to bound a fiber moment, not to descend a receiver or delete labels.
