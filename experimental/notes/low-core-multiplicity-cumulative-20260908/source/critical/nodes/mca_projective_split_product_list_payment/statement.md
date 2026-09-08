# Projective split-product joint lists

Status: PROVED. Let F be a finite field, D a set of n distinct F-points,
V an s-dimensional F-space of polynomials of degree <J, s>=1, and
J<=A<=n. Fix h_* of degree <J and an arbitrary received pair (u,v) on D.
For (a,b) in (h_*+V) x V, put

    x=alpha*a+beta*b+c0(X), y=gamma*a+delta*b+c1(X),
    alpha,beta,gamma,delta in F, alpha*delta-beta*gamma!=0,
    c0,c1 in F(X), m>=1, R in F(X), R!=0.

Count distinct pairs satisfying the EXACT identity x*y^m=R and at least
A joint agreements with (u,v). With Q=(n-J+1)/(A-J+1), their number is

    M <= max{binom(2s,s)*m^s,
             floor(Q)*binom(2s-2,s-1)*m^(s-1)}.          (SP)

More precisely, x and y range in affine cosets x0+V and y0+V. Write
eps_x=0 if x0 belongs to V, and 1 otherwise, and similarly for eps_y.
The four bounds for (eps_x,eps_y)=(1,1),(0,1),(1,0),(0,0) are

    binom(2s,s)*m^s;
    binom(2s-1,s-1)*m^s;
    binom(2s-1,s)*m^s;
    floor(Q)*binom(2s-2,s-1)*m^(s-1).                  (Cases)

The first three count ALL function-field pairs, without evaluating the
rational offsets. The fourth explicitly pays common zero coordinates.
No field extension replaces the original counting field.

For s=11,m=3 and (n,J,A)=(1048576+J,J,J+66972), the bounds are
124965162504, 62482581252, 62482581252 and 163644855660.
Thus M<=163644855660 uniformly. The finite consumer separately proves
N<=164828561948185643 when at most 64 LOW pairs lie off this product
curve, on its canonical normalized 4801..169999 source contract.

This is not a count for moving factor directions, zero levels, every
rational quartic, or all quartics with a specified infinity multiplicity.
There is no asserted product cover of an arbitrary MCA source. The
exponent m here is NOT the finite consumer's agreement parameter.
