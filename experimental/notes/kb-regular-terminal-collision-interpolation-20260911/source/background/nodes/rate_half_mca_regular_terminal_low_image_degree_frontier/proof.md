# Interpolation Pays All High-Image-Degree Terminals

Put R=1048576,d=67472. The required eigen-capacity theorem preserves the
original one-pair raw bound C_t=R-d+t and gives, for every actual primitive
degree3<=kappa<=J1-8 and v>=0,

    N_v=R+kappa+v, A_v=d+kappa-t+v,
    q1=floor((R-g_J)/(d+1-t)),
    q2(kappa)=floor((R-kappa+2)/(d-kappa+2-t)).

These are hereditary actual line/plane capacities after the proved original
pencil-source alternatives are removed. The denominator in q2 is positive
and the ratio increases with kappa. Put K=J1-8 and qbar=q2(K).
Then2*q1<=qbar, and the generic eigen-root incidence charge for any selected
subset is at most(kappa-1)*cbar_e, where

    cbar_e=(0,qbar,qbar+q1,3*qbar/2)_e.

Suppose terminal weight>L_t and select exactly M=floor(L_t/C_t)+1 actual
pairs. Choose the certified integer ell>=M-1. The exact image Hilbert function
at degree ell is nondecreasing in eta. If eta>=eta0, the certificate proves

    H_eta(ell)>=H_eta0(ell)>binom(M,2).

The pair-owned collision interpolation theorem therefore gives

    M*A_v <= (kappa-1)*cbar_e+N_v+(kappa-1)*ell.        (BOUND)

The finite certificate proves the strict reverse at kappa=K,v=0. For fixed
M,ell,cbar_e, the left-minus-right difference has kappa coefficient
M-1-ell-cbar_e<=0 and v coefficient M-1>0. Hence the reverse holds for
EVERY kappa<=K and v>=0, not just a sampled endpoint. BOUND is impossible.
Thus at most M-1 actual pairs occur and original weight<=(M-1)*C_t<=L_t.

The interpolation proof uses actual collision groups and pullback
multiplicities, so singularities and repeated finite fibres need no separate
generic-degree estimate. The original field, raw values and labels are fixed.

Thirteen adjacent J profiles and both raw cutoffs give52 image-degree gates
and104 strict inequalities. The prior actual-span theorem supplies an
excessive cutoff/path for an over-budget rank19 source: it is pencil-free
on the lower prefix; whole constant3 remains possible on the upper tail.
The new theorem excludes eta>=eta0 on the pencil-free branch. It neither
assumes nor pays the remaining low-degree image class or constant tail.

For a surviving eta below eta0, the SAME ell still has the strict reverse
of BOUND, independently of eta. If an actual M-subset had C<H_eta(ell),
the generic theorem would again give BOUND and a contradiction. Hence
C>=H_eta(ell) in EVERY such subset. This lower bound counts the disjoint
pair sets of actual collision groups; it is not a formal direction census.
