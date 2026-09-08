# Maximum-density flats and coupled core bases

Status: PROVED by the hand proof; external independent review remains due.

Use a fixed degree-<K polynomial carrier V of actual dimension eleven,
fixed affine translate h_*+V, distinct evaluation coordinates and distinct
finite selected slopes. Every selected size-m support is bad in the FULL
degree-<K pair code, with m=K+d. The universal carrier core is empty,
g=0, but V may have common zeros outside the joint cores. No maximal-raw
selection, receiver descent or pair-curve cover is required.

Fix 1<=T<=d-11 and set M=m-T, c=M-K+1>=12. Over proper nonzero
subspaces F of V*, maximize the number of nonzero original evaluations
in F divided by dim F. Let h be that maximum, and choose a maximizing
flat of dimension j and cardinality a=j*h. Necessarily

    1<=j<=10, 1<=a<=K-11+j.

All M-point actual joint-core subsets have at least

    B0=M*prod_(i=1)^10(M-min(i*h,K-11+i))             (HYBRID)

independent ordered evaluation bases. If 1<=j<=4 they also have at least

    B_F=min_(t in {0,a,c if c<=a}) P(M-t)*g_j(t),     (FLAT)
    l=11-j, e=K-a-l,
    P(X)=X*prod_(i=1)^(l-1)(X-min(e+i,i*h)),
    A_k=prod_(i=0)^(k-1)(c+i), A_0=1,
    g_j(t)=prod_(i=0)^(j-1)(c+i-t) +11*A_(j-1)*t,   0<=t<=c,
    g_j(t)=11*A_(j-1)*t,                            t>=c.

The product term is zero at c, so the two definitions agree. Set
B=max(B0,B_F) wherever (FLAT) applies, including the scoped rank-five
supplement below, and B=B0 otherwise. Every selected raw<=T record
has at least 12*B independent ordered incidence tuples. If a proved
completed weight floor L>0 holds for every raw>T, then

    |Gamma|<=floor((n-z)_falling_12
                  /min(12*B,m*P_d*L)),              (SOURCE)
    P_d=prod_(i=1)^10(d+i),

where z counts zero incidence normals. LOW and HIGH use one resource.

The maximum-density flat is chosen from the actual original evaluation
configuration, not conjectured to exist in a prescribed low dimension.
The finite consumer proves its exhaustive numerical case split. It also
owns original near and original-row/owner transport obligations.

The [rank-five supplement](rank_five_extension.md) extends (FLAT) to j=5
when a<=c and c>=100. Two negative coefficients are absorbed using the
actual inequalities E_3<=t*E_2 and E_4<=t^2*E_2, not discarded.
The same endpoint bound holds on every restricted interval [0,b], b<=a.
