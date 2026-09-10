# Use Concavity Of Weighted Branch Minima, Not Convexity Of The Envelope

The required full-fiber contraction partitions the N nonzero evaluations
into projective fibers of sizes a_i and gives

    B_r=sum_i a_i*B_(r-1)(child_i)>=sum_i a_i*F(K-a_i).

There are at least r fibers. Any r-1 lie in a proper flat, hence their
total size is at most K-1 by the polynomial root bound. Set m=r-1,
t=r-2, order fiber sizes decreasingly and put b=a_m. Then
1<=b<=(K-1)/m, tail sizes<=b, and every size is at most K-r+1.

## 1. The Extreme Top Partition Still Gives A Lower Bound

Each branch is nondecreasing, so F=min_i F_i is nondecreasing. For fixed K
and1<=s<=K-r+1 put phi_i(s)=s*F_i(K-s). Its second derivative is

    phi_i''(s)=s*F_i''(K-s)-2F_i'(K-s)<=0

by s<=E and(SHAPE). A finite minimum of concave functions is concave:
its hypograph is the intersection of their convex hypographs. Therefore
phi(s)=s*F(K-s)=min_i phi_i(s) is concave as well.

Replace each tail F(K-a_i) by the no-larger F(K-b). The contraction
sum is then at least

    N*F(K-b)+sum_(top m) psi(a_i),
    psi(s)=phi(s)-s*F(K-b).

This psi is concave, psi(b)=0 and psi(s)<=0 for s>=b. These properties
imply psi is nonincreasing there, even at a branch switch: for b<x<y,
concavity gives psi(y)<=psi(x)*(y-b)/(x-b)<=psi(x).

Increasing the top mass to K-1 can only lower the expression. At that
fixed mass, concavity minimizes the sum at the extreme partition
(a,b,...,b), where a=K-1-t*b>=b. All entries stay in the allowed interval.
Consequently

    B_r>=C_K(b)=a*F(K-a)+(N-a)*F(K-b).                   (EXTREME)

This uses only F at actual child degrees before the real relaxation.

## 2. Mixed Branches Make C_K Concave

Both weights a,N-a are positive. Hence C_K(b)=min_(i,j) C_ij(b), where

    C_ij(b)=a*F_i(K-a)+(N-a)*F_j(K-b).

With a'= -t, direct differentiation gives

    C_ij''=t^2*[a*F_i''(K-a)-2F_i'(K-a)]
                     +(N-a)*F_j''(K-b)-2t*F_j'(K-b).

The first bracket is nonpositive because a<=E. The remaining terms
are nonpositive because N-a<=D+E and the last gate in(SHAPE) holds.
All arguments K-a,K-b lie in[r-1,E]. Thus every mixed C_ij is concave,
and their finite minimum C_K is concave. This argument explicitly allows
different minimizing branches at the two child arguments.

The minimum on1<=b<=(K-1)/(r-1) is attained at an endpoint. At b=1,
(EXTREME) is S_r(K); at b=(K-1)/(r-1) it is U_r(K). This proves
(ENDPOINT) universally. Real b only lower-bounds an expression valid on
actual integer fiber partitions; it does not define a fractional-degree code.

Repeated application may represent F by an increasing finite branch
family. A consumer must verify(SHAPE) for EVERY branch at EVERY step.
It may not apply Jensen to a potentially nonconvex minimum, or replace
min(S,U) by whichever branch gives a numerically preferable LOWER bound.
