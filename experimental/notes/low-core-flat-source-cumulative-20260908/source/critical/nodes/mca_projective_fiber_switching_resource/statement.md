# Sharp Coordinate-Weighted Distinct-Fiber Resource

Let n>r>=2 distinct coordinates be partitioned into fibers A_i of sizes
a_i. Give x in A_i weight w_x=a_i-1. Let G_r be the ordered r-tuples
of distinct coordinates meeting every fiber at most once, and put

    W_r=sum_(v in G_r) sum_(x in v) w_x,
    lambda_*=(r-1)/(2(n-r)).

Then

    |G_r|+lambda_* W_r <=(n)_r.                     (SWITCH)

The constant is SHARP uniformly over all partitions: equality with W_r>0
holds for one two-point fiber and n-2 singleton fibers. No bound on the
largest fiber or on total collision mass is needed. At n=r the same
resource inequality holds for any finite nonnegative lambda, since either
all fibers are singletons or G_r is empty; the displayed formula is not used.

For the actual selected-source setup of the projective-fiber secant theorem,
pad each carrier-zero coordinate by a singleton. Outside its SAME exception
set E, the weighted independent-tuple resource is therefore at most(n)_r
for every0<=lambda<=lambda_*. Here r=s+1 and all weights are fixed from
the full source. Keep|E|<=z+sum_i binom(a_i,2); no extra near allowance.
Any previously proved weighted core cost for this same lambda may be used.
On n0<=n<=n1 with n0>r, lambda=(r-1)/(2(n1-r)) works uniformly.

For r>=4 the sharp partition is already realized by an actual rank-(r-1)
polynomial evaluation carrier of degree<r on any n>r distinct field points
including0,1, with enough field elements. This proves optimality only of
the full distinct-fiber resource relaxation, NOT of an MCA row bound.
It does not assert that every counted tuple is an agreeing independent
tuple for a received line, or construct an unsafe line.
