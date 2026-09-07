# Common-core cancellation preserves low-margin relations

Status: PROVED. All fields and polynomial degrees below are unchanged
unless explicitly divided by a locator.

Let D have n distinct points, 1<=s<=K<m=K+d<=n, d>=1,
and let C' be an s-dimensional space of degree-<K polynomials.
For distinct labels gamma choose h_gamma in h_*+C'. Its COMPLETE
scalar agreement set A_gamma has size at least m and is not explained
by a degree-<K received pair. Let G be any subset of

    {x in D: C'(x)=0, u(x)=h_*(x), v(x)=0}.

Write g=|G|, P=P_G, J=K-g. Then g<=K-s and J>=s.
Every label admits an exact m-point bad support containing G.
Choose any such supports, and any raw-minimizing b_gamma in C'.
On D'=D minus G set

    u'=(u-h_*)/P, v'=v/P, C''=C'/P,
    h'_gamma=(h_gamma-h_*)/P, S'_gamma=S_gamma minus G.

This preserves every label, badness of each selected support, carrier
dimension, d=m-K, every raw margin, and the entire set of minimizers
under b -> b/P. Complete minimizing pair cores satisfy H'_gamma=
H_gamma minus G. Hence, for a nonempty raw<=T family, U'_T=U_T minus G.

For 1<=T<=d, put ell=d-T and A=K+ell. The polynomial row spaces

    {R: deg R_i<=ell,
       deg rem_(P_U)(R_0 u_U+R_1 v_U)<A}

and the corresponding child space with (U',u',v',A-g) are IDENTICAL
as subspaces of F[X]^2. Primitive heights and the constant gluing
kernel are preserved. Thus the received-pair gluing defect is preserved.

These are assertions about G-saturated supports. Reselecting an old
support can change its raw margin; no preservation from arbitrary old
supports is asserted. No counting upper bound is part of this theorem.
