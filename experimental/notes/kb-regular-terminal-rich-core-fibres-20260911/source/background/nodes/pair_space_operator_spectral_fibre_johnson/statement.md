# Spectral Root Removal Turns Small Projective Fibres Into A Pair Count

Status: PROVED locally; independent mathematical review remains due.

Let U be a three-dimensional F-space of polynomials of degree<K-a,
D=K-a-1>=2, and T:U->U an F-linear operator. Assume each eigenspace
for an eigenvalue IN F has dimension at most one. Let e in{0,1,2,3}
be the number of distinct such eigenvalues, including zero.

On n distinct F-points, let a anchor points have locator H_a. Actual
pairs lie in f_*+H_a*{((I-alpha*T)y,T*y):y in U}; their complete joint
cores against one receiver have size>=A. There is no claim that the
represented y fill U or have full actual affine span.

Delete the anchors from the AUXILIARY coordinate count. If e>0 also
delete roots of one nonzero eigenpolynomial y_lambda for each F-eigenvalue.
If e=0 instead delete all common evaluation zeros of U. Call the remaining
domain Omega. Nonzero projective evaluations [ev_x|U] are defined on Omega.
Suppose every fibre of this ACTUAL finite-domain map has size at most H.

A bound on the number of removed coordinates is

    b_e=a+D-2=K-3                 if e=0,
    b_e=a+e*D                    if e>=1.

Set N=n-b_e and A'=A-b_e. If 0<A'<=N and A'^2>N*H, the number of
distinct actual pairs is at most

    floor(N*(A'-H)/(A'^2-N*H)).                         (COUNT)

It suffices more generally that H bound every intersection of TWO actual
cores on Omega; a bound on every finite evaluation fibre is one way to
ensure this. An excessive family therefore forces an actual shared-core
intersection, not merely an unoccupied large evaluation fibre.

For original MCA owner weights as in mca_weighted_pencil_raw_mass,
the total ORIGINAL raw weight is at most (n-A) times (COUNT).
No label, weight or original source resource is shortened or reset.

H bounds the maximum actual projective evaluation fibre AFTER the stated
root removal. Generic map degree, average fibre size, kernel-map degree,
or eigenvalues over an extension of F cannot replace these data.
An F-eigenspace of dimension>=2 is excluded, not silently removed.
No unrestricted MCA source or Prize bound is asserted.
