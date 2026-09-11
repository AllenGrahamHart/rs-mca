# Constant-Projection Singleton And Rich-Fibre Census

Fix one received pair (u,v) on n distinct points of F and one assignment
of finite labels gamma to polynomial pairs f=(a,b), with deg a,deg b<K.
Retain labels with positive ORIGINAL selected raw values at most t,
and let P be their ACTUAL represented pairs. Each selected support consists
of scalar agreements for a+gamma*b. Suppose every complete joint core
H_f has at least A points, where K<=A<=n.

Fix ONE nonzero constant row rho=(lambda0,lambda1) over F.
Let q_f=lambda0*a+lambda1*b and partition P by equality of this polynomial.
For an occupied fibre q, let C_q be the union of its COMPLETE joint cores.
Call the fibre rich if it contains at least two distinct actual pairs.
Suppose rich fibres have original complement e_q=n-|C_q|>=g+1, with g>=0.

Let Q(e) bound the number of distinct ACTUAL projected polynomials agreeing
with lambda0*u+lambda1*v on at least n-e coordinates. It suffices to use
ordinary affine LIST bounds for the projected polynomial carrier.

Put E=n-2*A+K-1. Partition the integer interval [g+1,E] into bins [l,u].
For each bin let P(l) be a uniform scalar LIST cap for the affine
parameter spaces of these fibres at length n-l, degree<K and agreement A.
The scalar parameterization is along delta=(lambda1,-lambda0);
assume its affine dimension is at most s. The same-field ordinary
dimension-s LIST theorem supplies P(l). An empty interval contributes zero.

Then the sum of ORIGINAL raw weights satisfies

    Omega_t <= t+(n-A)*Q(n-A)+sum_bins u*P(l)*Q(u).       (CENSUS)

If lambda0=0 the first t can be replaced by zero. The base term is allowed
to count rich projections too; this only overpays. Bins' Q(u) counts may
overlap. No shared mass-packing constraint across different q is assumed.

In particular, every rich fibre has e_q<=E. This two-core threshold is
sharp in general. The assertion concerns original raw mass; a consumer
must perform the original slope-count conversion and add near once.
