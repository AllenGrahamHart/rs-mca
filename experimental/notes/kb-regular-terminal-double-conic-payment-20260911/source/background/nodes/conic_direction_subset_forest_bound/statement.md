# Null-Direction Forests Give Exact Subset Resources

Let F have odd characteristic and Q be a nondegenerate ternary quadratic
form. Let S be M>=2 distinct points of F^3. Let R_i subset S, |R_i|=r_i>=2,
lie on pairwise DISTINCT affine lines with Q-null directions. Parallel
lines are allowed. Choose a tree on each R_i and take their union graph.

This simple graph is triangle-free. Every triple of distinct vertices has
at most2 common neighbours. For any integer s with2<=s<=M, define K_s
as follows. For s<=5 use floor(s^2/4). For s>=6 put

    phi_s(d)=binom(d,3)-2*binom(d,2)+(s-2)*d,
    psi_s(x)=(s-4)*x                         for0<=x<=5,

and above5 use linear interpolation of phi_s at consecutive integers.
Let K_s be the largest integer E<=floor(s^2/4) with
s*psi_s(2E/s)<=2*binom(s,3). The graph has at most K_M edges.
K_s is a sufficient upper bound, NOT the exact graph extremal number.

The stronger subset resource holds simultaneously for each s:

    sum_i f_(M,s)(r_i)<=K_s,
    f_(M,s)(r)=s*r/M-1+binom(M-r,s)/binom(M,s).

Binomial coefficients with upper argument below s are zero. Extend f(0)=
f(1)=0, so groups of size0 or1 may be included freely. Suppose fibre sizes
l_i<=nu, sum l_i<=N and every r_i<=q. If a>=1,b>=0 and
r<=a+b*f(r) for all integers0<=r<=q, then

    sum_i l_i*r_i <= a*N+b*nu*K_s.

This is deterministic finite averaging over all subsets, not a randomized
experiment, a formal-hull census, or a claim that clique edges form a forest.
