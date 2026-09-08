# Proof By Pair-Collision Inclusion And Exclusion

Use the explicit exceptional SET from the required secant theorem. Outside
it, every owned independent tuple has distinct nonzero projective fibers.
Pad each zero coordinate as its own singleton class. This only enlarges
the collection of counted tuples and does not change T or the largest
nontrivial class. Count ordered r-tuples of DISTINCT coordinates in these
padded classes.

Let X be the number of unordered position pairs whose coordinates share
a class. For every integer X>=0,

    1_(X=0) <= 1-X+binom(X,2).

For X=0 equality holds; at X>=1 the right side is
(X-1)*(X-2)/2>=0. Sum this pointwise inequality over the (n)_r tuples.

There are binom(r,2) single pair events. Each has exactly
T*(n-2)_(r-2) tuples. Two pair events sharing one position have a common
triple. There are3*binom(r,3) such pairs of events, each with
sum_i(a_i)_3*(n-3)_(r-3) tuples. Since a_i<=A,

    sum_i(a_i)_3 <= (A-2)*T.

Two disjoint position-pair events have exactly

    [sum_i(a_i)_4+sum_(i!=j)(a_i)_2*(a_j)_2]*(n-4)_(r-4)

tuples. The bracket is at most T^2: the difference is
sum_i(a_i)_2*(4a_i-6)>=0. There are3*binom(r,4) such event pairs.
Substitution proves RESOURCE. No independence or random-fiber hypothesis
was made about these events or about the received line.

The derivative of U in real T, after division by the positive
(n-4)_(r-4), is

    -binom(r,2)*(n-2)*(n-3)
     +3*binom(r,3)*(A-2)*(n-3)+6*binom(r,4)*T.

Its maximum on the stated T interval occurs at n*(A-1), proving
MONOTONE. The real interval is an analytic relaxation of an actual integer
statistic, not an invented fractional source.

Finally use the required secant theorem's unique ownership of independent
tuples by finite labels. The exceptional set is charged once, and all
surviving LOW/HIGH records share this resource. The padding does not
create agreeing zero coordinates, discard nonuniversal zero labels, or
supply a near allowance. Those labels are already in the exceptional set.
