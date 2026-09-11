# Exact Carriers With And Without A Degree Jump

These are shared-carrier controls, not complete official MCA sources.

Over F97 put H=X^12, h=H-1 and

    V4=span(X,h,hH,hH^2).

Its gcd is1 and its actual degree is36. Ratios hH/h=H and X/h
recover X=(X/h)*(H-1), so the normalization degree is1, as an identity
of function fields rather than a finite-point injectivity inference.
At any root a of H-1, evaluation is [a,0,0,0]. The inner image after
full-gcd division has basis1,H,H^2, degree24, conic image and normalization
degree12. The centre has12 branches, all distinct since12 is invertible.

Embed it in an original eleven-dimensional carrier by putting

    G7=product_(a=0)^6 (X-a),
    V11=F[X]_(<=6) + G7*V4.

Its eleven leading degrees are distinct and its actual degree is43.
Anchoring successively at0,...,6 removes the low-degree summand and leaves
G7*V4. At each of those steps the full fixed divisor added has degree1.
After division, the shared carrier is V4. The initial normalization degree
is1 since V11 contains1,X; at every intermediate stage the ratios above
recover X (or the remaining low-degree summand contains1,X).

Choose the next actual anchor16, a root of H-1. The full degree ledger is
43=7+12+24 and the normalization degrees are1,...,1,12. There are only10
available coordinates over this final centre after the earlier anchors:
roots1 and6 have already been removed. Restoring those coordinates would
not be the same actual path.

For a no-jump control over F101, take V11=span(1,X^2,...,X^20).
Anchors1,...,8 have distinct squares. At each step the full fixed factor
is X^2-a^2, not just X-a. After eight steps the carrier is a composition
of span(1,Y,Y^2) with Y=X^2. Its degree is4 and normalization degree2,
unchanged from the original degree20 rational-normal image. The telescope
is20=16+4, with sixteen actual roots in the removed fibres.
