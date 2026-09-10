# Price Small Intersections In Every Spectral Stratum

Put R=1048576,d=67472. A raw-t terminal pair has complete joint core
of size>=A=d+J-t in n=R+J points, and original weight<=R-d+t.
The eight-anchor shared carrier has dimension3 and polynomial degree
at most D=J-9. Only differences were divided by the anchor locator.

For e=0,1,2,3 the generic root-mask bounds are respectively

    b_e=J-3, J-1, 2J-10, 3J-19.

For a fixed H, the generic intersection theorem gives the pair cap
floor((n-b_e)*(A-b_e-H)/((A-b_e)^2-(n-b_e)*H)).
Multiplying by the ORIGINAL R-d+t bounds terminal weight.

## Whole-Profile Legality

The four A-b_e expressions are

    d+3-t, d+1-t, d-J+10-t, d-2J+19-t.

They are constant or decreasing in J; (n-b_e)-(A-b_e)=R-d+t
is constant. The generic proof's derivative shows that the Johnson
quotient decreases with A-b_e at fixed difference and fixed H.
Its denominator is positive at each certified high endpoint, hence
throughout that profile. Thus J1 is a simultaneous valid worst endpoint.
No integer enumeration of the11,535 source degrees is necessary.

For each profile and spectral count the certificate gives one integer H_e
and both cutoff calculations. It checks positive denominators, exact
floors and pair_cap*(R-d+t)<=L_t(J). All13 profiles are adjacent and
exhaustive. Their52 gates and104 cutoff inequalities prove the bound.
The gate-selection formula is not a theorem of optimality for actual
sources; the independent audit only needs legality and affordability.

## The Excessive Terminal Gives An Actual Witness

The required actual-span frontier says that an over-budget source has
a cutoff/path with terminal weight>L_t and actual span3. On the lower
prefix it is pencil-free; on the upper tail it may instead be whole
constant3. In a pencil-free terminal an F-eigenspace of dimension2 would
give a constant-direction rank-one plane, which is impossible. Thus the
new spectral theorem applies to every such pencil-free enclosure.

If all its two-core intersections on Omega were <=H_e, the preceding
weight inequality would contradict excess. Hence two distinct ACTUAL
pairs share at least H_e+1 coordinates there. Eigenvector differences
have no surviving zeros, so their difference y is not an F-eigenvector.
The independent polynomials y,T(y) annihilate one projective evaluation
fibre and share the locator of these actual shared-core coordinates.
The source-coordinate interpretation is proved in source_witness.md.

No fibre-size premise is installed as an unproved DAG leaf. This is a
proved conditional bound and its unconditional necessary-witness consequence,
not a claim that all surviving rich fibres are affordable.
