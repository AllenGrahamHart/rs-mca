# A Fixed Unaffordable Subset Cannot Satisfy The Energy Bound

Use primitive_carrier.md and section_capacities.md. Fix a profile, t and e.
Let L_t be the unchanged parent rational allowance and C_t=R-d+t. Define

    M=floor(L_t/C_t)+1>=2.

If terminal weight exceeds L_t, there are at least M distinct actual pairs,
since each has original weight<=C_t. Select exactly M. The hereditary
capacities bound their total eigen-root core incidence by B=(kappa-1)*c_e,
where c_e=0,q2,q2+q1,3*q2/2. The generic theorem then applies with
S0=M*(d+kappa-t)-B and N0=R+kappa.

## Natural Degree And Exact Finite Gates

Outside E, eigenvector differences have no common roots; other differences
are two independent degree<=kappa-1 polynomials and share at most kappa-2
distinct roots. Thus the required intersection bound is

    H_used=min(H_e,kappa-2).

For every kappa in3..J1-8 the certificate proves S0>=N0 and

    S0^2-N0*S0 > N0*M*(M-1)*H_used.

The primitive-carrier proof extends this from v=0 to EVERY v=s+g-z>=0,
including slack between the actual polynomial degree and J-9.
The generic theorem excludes an M-element actual subset. Hence the pair
count is<=M-1 and the original terminal weight is<=(M-1)*C_t<=L_t.
No monotonicity in the unknown full family size is needed.

On each exact q2 box, split at kappa=H_e+2. Put H_used=u*kappa+w,
with (u,w)=(1,-2) on the natural-degree part and (0,H_e) otherwise.
If c2=2*c_e, then2*S0=b+s*kappa, b=2*M*(d-t)+c2, s=2*M-c2.
Four times the energy difference is the quadratic printed in
finite_calibration.md. Positive endpoint values, plus a positive value at
any interior convex vertex, prove it on the WHOLE real box. Exact q2
floor boxes exhaust every allowed primitive degree; no J scan is needed.

## Excess Is Supported By Original Cores

If kappa<=H_e+2 the natural root bound alone suffices, so this entire
primitive-degree terminal class is paid. Otherwise excess forces two actual
cores to share at least H_e+1 coordinates in Omega. Their primitive
differences y,T(y) are independent and share that locator. Their original
shared polynomials have the further factor G, of total shared degree
at least g+H_e+1. On Omega, G and H_a are nonzero, so the projective
evaluation class is unchanged. The prior source_witness.md therefore
gives rank exactly9 after restoring the eight independent anchors.
The actual-span source alternative and whole-constant upper tail are
inherited unchanged. The energy test does not pay the remaining rich class.

For EVERY M-subset of an excessive terminal, the generic pair-mass form
gives2*I2>=S_v^2/N_v-S_v>M*(M-1)*H_e. Here kappa>=H_e+3 has already
been forced, so the certified natural minimum equals H_e. Thus total
actual intersection mass exceeds binom(M,2)*H_e in every such subset.
Any future thinning argument needs just ONE M-subset below that average;
a uniform maximum-fibre bound is sufficient but not necessary.
