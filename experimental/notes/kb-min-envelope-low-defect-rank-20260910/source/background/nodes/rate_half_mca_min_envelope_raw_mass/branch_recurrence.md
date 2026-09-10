# Retain The Entire Endpoint Tree

For T in{9,44,150}, put D=67472-T and E=21499. Define
P_r(D)=prod_(i=1)^(r-1)(D+i). In the shifted variable x=k-r, a rank-r
basis lower bound will be P_r(D)*min_(q in Q_r) q(x).

The rank-three seed gives the single branch

    q3(x)=D+3+(3D+7)/(2(D+2))*x+x^2/(2(D+2)).

For each r=4..11 and EVERY child branch q in Q_(r-1), retain both

    qS(x)=q(x)+1+x,
    qU(x)=(D+r+x)/(D+r-1)*q((r-2)/(r-1)*x).            (TREE)

All child branches have q(0)=D+r-1 and nonnegative coefficients.
At x=K-r, the spike endpoint has child argument K-1, hence shifted
argument x, and the other child argument is r-1, where all branches
coincide. The equal endpoint has shifted argument (r-2)/(r-1)*x.
Dividing by P_r gives(TREE) exactly. Thus the generic minimum-envelope
theorem gives the minimum over this entire new family, not a lower bound
by each branch separately. No branch is pruned or selected optimistically.

At each step verify, on the FULL real child interval x in[0,E-r+1],

    q'>=0, q''>=0, 2q'-E*q''>=0,
    2(r-2)q'-(D+E)q''>=0.                             (SHAPE)

The exact certificate is the fixed recurrence and the nonnegative
Bernstein coefficients for every one of these polynomials. If
p(low+(high-low)y)=sum a_j*y^j has degree v, its Bernstein coefficients are

    b_i=sum_(j=0)^i a_j*binom(i,j)/binom(v,j).

The binomial expansion gives
p=sum_i b_i*binom(v,i)*y^i*(1-y)^(v-i), so b_i>=0 proves p>=0
on the entire interval. This criterion is sufficient, not necessary.
verify.py and the import-free unshifted-degree verify_audit.py check all
255 input branches for each T, 765 in total. Q_11 has256 branches.

Put f_T=12*P_11(67472-T) and

    beta_T(J)=f_T*min_(q in Q_11) q(J-11), U(J)=(1048576+J)_12.

Every final branch has nonnegative coefficients and satisfies exactly

    q'(9941-11)*(1048576+9941-11)>12*q(E-11),
    (67472+11)*q[1]>=q[0].                             (MONO)

The first gate gives q'/q>12/(1048576+J-11)>=U'/U throughout the
interval, using increasing q,q'. Thus EVERY U/(f_T*q) decreases; their
MAXIMUM U/beta_T decreases too. For the second gate, writing c=67483,
the derivative numerator of q(x)/(c+x) is
c*q[1]-q[0]+sum_(i>=2) q[i]*(i*c*x^(i-1)+(i-1)*x^i), which is
nonnegative for x>=0. Minima preserve this monotonicity, so beta_T/m
increases. No differentiability of the branch minimum is required.

Exact endpoint floors of U/beta_T at J9941 and14000 are

    T9:   578501226347492453, 469162745598573006;
    T44:  581590844909990298, 471656010466926030;
    T150: 591058329359405303, 479295814582433859.

The T150 numbers are basis-resource quotients only. To fund EVERY raw
value, the same-source recordwise transfer in proof.md is essential.
