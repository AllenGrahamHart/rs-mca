# Uniform Child Counts With Original Source Capacities

Put R=1048576,d0=67472,K=J1-8,H=floor((J1-1)/10). A regular child
has primitive polynomial degree E=eta*n, where n is its normalization
degree, and inherited parameters

    N_v=R+E+1+v, A_v=d0+E+1-t+v, E<=K-1, v>=0.

Original source gates give q1 and qbar with2q1<=qbar, so all spectral
root-incidence constants are bounded by3*qbar/2. Interpolation and
branch energy therefore apply with B=3*qbar*E/2, in every spectrum.
No field extension or new source census is used.

## A Coarse Count Valid Even At Rank-One Evaluation Points

Every affine line of actual pairs has at most
floor((R+1)/(d0+1-t)) pairs: outside at most E common zeros of its
nonzero direction, at most one pair agrees at a coordinate.

Every actual affine plane has function-field rank two by pencil-freeness.
Its determinant has degree at most2E. Counting outside its zero set gives

    count<=(N_v-2E)/(A_v-2E)
         <=(R-E+1)/(d0-E+1-t)<=qbar.

All denominators are positive. At any coordinate the actual agreeing
set lies in an affine plane or line: primitive evaluation is nonzero
and the operator graph has joint rank at least one. Hence occupancy
is at most qbar EVERYWHERE, giving

    count<=floor(qbar*(R+eta+1)/(d0+eta+1-t)).

The last ratio uses E>=eta and v>=0 and is decreasing in both. In
particular, an eigen-root mask is NOT assumed to remove all rank-one
evaluation points. Those agreeing groups may be planes, not lines.

The exact pencil-free F5 example in off_mask_plane.md has an empty
eigen-root mask but a rank-one evaluation plane with25 pairs. It is an
algebraic guard, not an official-source counterexample.

## Sharper Certified Counts

For each candidate count M, interpolation uses the least ell with
H_eta(ell)>binom(M,2). The strict reverse

    2M*A_v>3*qbar*E+2N_v+2E*ell

is affine, decreases with n since ell>=M-1, and increases with v.
Checking n at its maximum and v=0 proves the whole interval.

Alternatively put Z=2M*A_v-3*qbar*E-N_v. Branch energy excludes M if
Z>0 and

    Z^2>(N_v+n*(eta-1)*(eta-2))*(N_v+4n*M*(M-1)).

The certificate checks the real quadratic minimum in n, positive Z
separately, and the nonnegative v derivative and positive v^2 coefficient.
The third option is the coarse occupancy count proved above.

For a birational inner centre, n=nu<=H and parent degree
nu*(eta+m)<=K with m>=1, so n<=min(H,floor(K/(eta+1))).
For arbitrary children, n<=floor((K-1)/eta). The same original source
allowances and complete cores apply to these different intervals.

An integer b0 is certified for EVERY birational child. For eta>=b0,
interpolation at ell=b0 and E=K-1 proves count<=b0 without an image-
degree ceiling. Only eta=2,...,b0-1 need separate C_eta bounds.
