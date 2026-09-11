# An Eigen-Root Mask Can Leave A Rank-One Evaluation Plane

Over F5 use U=span(1,X,X^2) and the operator

    T(1)=0, T(X)=X^2, T(X^2)=2X.

Its characteristic polynomial is lambda*(lambda^2-2). Since2 is not a
square in F5, the only original-field eigenvalue is0, with eigenpolynomial1.
That polynomial has no roots, so the original-field eigen-root mask is empty.
At X=0, however, the joint evaluation rows are(1,0,0) and(0,0,0).
The agreeing set through zero is the full affine plane with y=aX+bX^2,
and consists of25 actual pairs(y,Ty), not a line of5 pairs.

This graph is pencil-free, including nonconstant pencils. The alternating
map (u,v)->u*T(v)-v*T(u) sends the exterior basis to

    X^2, 2X, 2X^2-X^4.

These are independent. Thus no nonzero decomposable exterior vector is
in its kernel, so no F5-plane of pair directions has function-field rank1.
The coefficient matrix in the basis X,X^2,X^4 has determinant2 mod5.

This is an algebraic scope control, not an official large-agreement MCA
source or a violation of the proved original-source plane bounds. It
explains why child_caps.md uses plane occupancy at all evaluation points.
The inherited interpolation and branch-energy proofs already allow this
case; no correction to the published eigen-root theorem is required.
