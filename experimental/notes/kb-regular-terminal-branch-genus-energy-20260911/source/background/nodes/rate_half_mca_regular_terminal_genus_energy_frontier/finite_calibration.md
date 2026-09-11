# Exact Quadratic Certificate

For one eta,e,t, let c2=2*c_e, P=binom(M,2), g=binom(eta-1,2), and

    z0=2*M*(d-t)+c2-R, z1=2*M-c2-1,
    u0=eta*R-2*g, u1=eta+2*g,
    w0=eta*R-8*P, w1=eta+8*P.

At v=0, Z=z0+z1*kappa and the strict price polynomial is
F(kappa)=eta^2*(z0+z1*kappa)^2-(u0+u1*kappa)*(w0+w1*kappa).
Its three integer coefficients and endpoint values are printed.

If F=a*kappa^2+b*kappa+c is convex with its vertex in [eta+1,K],
also require4*a*c-b^2>0. Otherwise endpoints suffice. Z is affine,
so its positivity at both endpoints suffices independently of squaring.

The v derivative at zero is
2*eta^2*(2*M-1)*(z0+z1*kappa)-eta*(u0+w0+(u1+w1)*kappa).
It is affine; both endpoint values are printed and required nonnegative.
The positive v^2 coefficient completes the all-v argument.

The independent audit evaluates the original rational branch-energy
difference directly, reconstructs its quadratic by exact differences and
checks its real vertex. It imports no primary verifier or helper.
The thirteen shards cover every original J profile, every spectral count,
both raw cutoffs and every newly paid integer eta. Larger eta uses the
pinned old theorem. There is no claim the new gates are optimal.
