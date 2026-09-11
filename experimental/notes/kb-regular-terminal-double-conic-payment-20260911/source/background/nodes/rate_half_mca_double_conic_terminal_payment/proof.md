# Price All Double-Conic Terminals By Exact Subset Averaging

The original one-pair weight is C_t=R-d+t=981104+t. Weight greater than
L_t supplies exactly M=floor(L_t/C_t)+1 ACTUAL distinct pairs. Retain
their full cores, with N_v,A_v as in rank_one_planes.md. Rank-one fibres
contribute at most30nu incidences.

At each remaining evaluation point p, choose one coordinate attaining the
largest agreeing group R_p, of size r_p. Different receivers within a fibre
are bounded by this size. Joint rank2 makes R_p an affine-line group;
the chi2 kernel isomorphism makes these lines' directions distinct points
of one nonsingular ternary conic. The source bounds give r_p<=qcap.
For r_p=0,1 no line needs to be chosen.

The required null-direction forest theorem gives, for each declared s,
sum f_(M,s)(r_p)<=K_s. Every fibre has at most nu coordinates and the
total domain size is at most N_v. Choose a>=1,b>=0 with
r<=a+b*f_(M,s)(r) for every integer0<=r<=qcap. Then

    M*A_v <=30nu+a*N_v+b*nu*K_s.

The certificate proves the STRICT reverse by the affine gap

    G(nu,v)=M*(d+2nu+1-t+v)-30nu
             -a*(R+2nu+1+v)-b*nu*K_s.

For V=floor((J1-9)/2), G is positive at (nu,v)=(1,0),(V,0), and its
v coefficient M-a is positive. It is affine in nu and v, so EVERY actual
nu in1..V and every v>=0 is covered, without saturation of the source
degree or map multiplicity. Thus M such pairs cannot exist; their original
weight is at most(M-1)*C_t<=L_t.

The thirteen profiles are consecutive and both cutoffs are checked. The
existing eight-anchor resource and whole-source alternatives are unchanged.
All double-conic terminals fit their allowances; this is not an assertion
that every terminal is double-conic. The required genus-energy frontier
still restricts the other pencil-free images to eta2..5. For eta2 the
geometric supplier now leaves only chi3,4 as possible excessive cases.
