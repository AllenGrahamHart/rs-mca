# Certify Whole Primitive-Degree Boxes With Integer Quadratics

For a fixed integer q>=2 the exact box where
q=floor((R-kappa+2)/(d-kappa+2-t)) is

    lo=max(3,ceil((q*(d+2-t)-(R+2))/(q-1))),
    hi=min(J1-8,ceil(((q+1)*(d+2-t)-(R+2))/q)-1).

Omit empty boxes. This follows by solving q<=ratio<q+1 with its positive
denominator. The ratio increases with kappa; checking the two endpoint
floors and consecutive full coverage is also an independent certification.
The allowed range begins at3, NOT J0-8: the original carrier may have a gcd.

Split each box at H_e+2, as in proof.md. With2*S0=b+s*kappa and
H_used=u*kappa+w, four times the strict energy difference has coefficients

    a0=b^2-2*R*b-4*R*M*(M-1)*w,
    a1=2*b*s-2*(b+R*s)-4*M*(M-1)*(R*u+w),
    a2=s^2-2*s-4*M*(M-1)*u.

Both endpoint values must be strictly positive. If a2>0 and the vertex
-a1/(2*a2) is in the box, also require4*a2*a0-a1^2>0. These conditions
prove positivity throughout the real interval, hence at every integer.
The linear S0-N0 test is checked at both endpoints and must be nonnegative.

The primary prints the coefficients and witnesses. The independent audit
evaluates the energy directly using rational arithmetic at endpoints and
at an interior vertex; it does not import the primary or its box selector.
Gate values are sufficient, not asserted optimal for real source families.
Thirteen separately hashed shards prevent a single oversized certificate.
