# Remove The Full Polynomial Gcd, Not Just Its Domain Roots

Put R=1048576,d=67472. In the original regular3 terminal, U0 has dimension3
and actual maximum polynomial degree delta<=J-9. If its monic polynomial
gcd has degree g, dividing by G gives a dimension3 carrier U of maximum
degree delta-g=kappa-1, hence kappa>=3. Retain slack s=J-9-delta>=0.
Conjugate T by the F-linear isomorphism u->G*u. This preserves eigenspaces,
regularity and pencil-freeness. The divided polynomial carrier has gcd1
and therefore no common evaluation zero on ANY F-point.

Let z be the number of DISTINCT roots of G on the original domain excluding
the eight anchors. Set v=s+g-z=J-8-kappa-z>=0. Degree slack, roots outside
the domain, repeated roots and roots at anchors can contribute to v.
Setting v=0 is not an identity, nor is setting delta=J-9.

Delete just the eight anchors and these z points. On the remaining domain
the actual affine pair family is transformed by subtracting its base pair,
the fixed invertible pair-coordinate change, and dividing by H_a*G.
Transform the fixed receiver pointwise there as well. Only this auxiliary
description changes; the original represented pairs and owners are fixed.
The new domain and the lower core size are

    N_v=R+kappa+v,  A_v=d+kappa-t+v.

The original one-pair raw weight is still at most C_t=R-d+t=N_v-A_v.
Lost coordinates are NOT removed from that original raw weight.

## Why The Finite Certificate May Use v=0

For fixed kappa,t,e, the next proof gives capacities valid for every v>=0.
Let B be their aggregate eigen-root incidence bound, and M the first
unaffordable number of pairs. Then S_v=M*A_v-B=S0+M*v.
The certificate proves S0>=N0; also S0<=M*N0 since A0<=N0 and B>=0.
Thus r=S_v/N_v stays in [1,M] for all v>=0. Differentiation gives

    d/dv (S_v^2/N_v-S_v)=M*(2r-1)-r^2>=M-1>0.

The last inequality follows because the quadratic increases on [1,M]
and has value M-1 at r=1. Hence the strict fixed-M energy inequality
at v=0 implies it for every possible v. No unproved gcd-root saturation
or original-source shortening is hidden in this endpoint reduction.
