# Use Branch Energy Only Where Its Exact Price Is Proved

Use R=1048576,d=67472, kappa=1+actual max degree(U0/G), and the proved
v>=0 from full gcd removal and unused degree. The original core bounds are

    N_v=R+kappa+v, A_v=d+kappa-t+v, C_t=R-d+t.

Original weight>L_t supplies exactly M=floor(L_t/C_t)+1 actual pairs.
For each profile ending at J1 put K=J1-8. The proved hereditary source
capacities give q1=floor((R-g_J)/(d+1-t)) and
qbar=floor((R-K+2)/(d-K+2-t)). Since the plane-capacity ratio increases
with kappa, an upper bound on removed eigen-root incidence is

    B=(kappa-1)*c_e, c_e=(0,qbar,qbar+q1,3*qbar/2)_e.

The branch-energy supplier applies to this very selected actual subset.
Its plane-image normalization has degree nu=(kappa-1)/eta, with branch
budget g=(eta-1)*(eta-2)/2 and unordered-pair budget P=binom(M,2).
No new source field, receivers or weights are introduced.

Let Z=2*(M*A_v-B)-N_v. The exact certificate proves Z>0 and

    eta^2*Z^2
      > (eta*N_v+2*g*(kappa-1))*(eta*N_v+8*P*(kappa-1)).

This is the strict reverse of branch energy. Hence M actual pairs cannot
exist, and original weight<=(M-1)*C_t<=L_t.

The certificate covers the continuous interval eta+1<=kappa<=K, larger
than the physical integer set where eta divides kappa-1. At v=0 the
difference is an exact quadratic in kappa; its real minimum is checked
at both endpoints and at an interior vertex when convex. The v derivative
at zero is affine in kappa and nonnegative at both endpoints. The v^2
coefficient is4*eta^2*M*(M-1)>0. Z increases with v. Thus the strict reverse
holds for ALL kappa in the interval and ALL v>=0, not only at a sampled
original degree or at a saturated gcd.

For each spectral/profile cell the new test is checked separately for
each eta from its new threshold through the OLD threshold minus one.
All higher eta is paid by the required collision-interpolation theorem.
This finite union is exhaustive above the new threshold, without a
monotonicity assumption in eta. The original weighted-anchor template
therefore applies to these bounded terminal classes at its unchanged cost.

The inherited actual-span theorem makes excess existential over a
cutoff/path. Removing the newly paid classes forces2<=eta<=5 on that
pencil-free branch; it does not rule out all remaining terminals or the
whole-constant upper tail. The original critical router stays TARGET.
