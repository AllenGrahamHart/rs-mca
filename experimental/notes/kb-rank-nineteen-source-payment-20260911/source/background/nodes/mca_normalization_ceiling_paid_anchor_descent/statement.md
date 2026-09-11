# Pay Coordinates That Cross A Normalization Ceiling

Retain an original weighted MCA source, its actual anchors and finite-label
owners. Let the primitive shared carrier V have dimension s>=4,degree D,
normalization degree nu<=H, and image degree eta>=s-1, so D=nu*eta.
Assume characteristic0 or characteristic p>D. Let the pair enclosure have
rank2s-3 and full generic projection onto V.

Put kappa=D-(s-1), N=R+D+1+v,A=d+D+1-t+v,v>=0, with R>=d>t.
The hereditary low-ceiling class retains full generic projection, pair/shared
ranks2s-3/s, and normalization degree at most H.

Set h=floor(H/nu)+1>=2. The branch-budget supplier bounds coordinates
with inner degree mu>=h, hence child normalization nu*mu>H, by

    beta(nu,eta,s,H)
      = nu*floor(binom(eta-s+2,2)*b0/binom(b0+h-1,2)),
    b0=min(eta-h*(s-2),max(1,h-2)),

with beta=0 if eta-h*(s-2)<1.

Suppose C bounds regular rank-two children still below the ceiling;
F bounds generic rank-one and unrestricted rank-two nonregular children;
T bounds all full-generic rank-two children regardless of normalization.
For any uniform geometric upper bound B_geo>=beta, original incidence gives

    A*Omega <= N*C+(kappa+3)*max(F-C,0)+B_geo*max(T-C,0).       (PAID)

The two exceptional sets may overlap. The nonnegative increments make
overlap harmless. No coordinate is discarded and B_geo<A is NOT required.

On kappa in[lo,hi], let D_hi=s-1+hi. A uniform B_geo is the maximum of
beta(nu,floor(D_hi/nu),s,H) over
1<=nu<=min(H,floor(D_hi/(s-1))). This is a finite exact envelope, not a
claim that every candidate pair(nu,eta) occurs.

For fixed B_geo and child prices, maximize (PAID) at kappa=lo,hi,v=0
and at the v-infinity limit C. Preceding-stage lower-degree prefix maxima
provide hereditary child prices. One may also take the minimum with any
already proved untagged full-generic bound for the same state.

Terminal bounds and the original official source composition are separate
consumer obligations. No row payment or free geometric avoidance is assumed.
