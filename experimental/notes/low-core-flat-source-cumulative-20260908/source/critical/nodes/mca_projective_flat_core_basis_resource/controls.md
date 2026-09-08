# Small Algebraic Controls

The first four controls use F_7 and actual polynomial evaluations.
The last hand example uses F_11. These test interfaces, not a claim
about the deployed large field.

1. V=span(1,X,X^2), K=4, two raw-one records on common core
   {0,1,2,3}, with different defect points 4 and 5.
   Each record has exactly 96 independent ordered incidence tuples;
   the two sets are disjoint. This tests the insertion factor and
   slope ownership with more than one label.
2. V=span(1,X,X^3), K=4, core {0,1,2,6} and defect 3.
   Fibers are all distinct, but evaluations at 0,1,6 are dependent.
   Only 72 independent ordered tuples occur, less than the false
   unsupported h=1 beta(1)=96. A rank-two subspace contains three nonzero
   evaluations, violating 2*h=2. Distinct fibers alone do not imply the
   required higher-dimensional occupancy bound.
3. V=X*span(1,X,X^2), K=4, core {0,1,2,3} and defect 4.
   The carrier-zero agreement at 0 gives g=z=1. The correct product
   gives exactly 24 independent tuples; dropping g falsely gives 96.
4. V=span(1,X^2,X^4), K=5, core {0,1,2,3,4} and defect 5.
   The projective map X^2 has fibers of size at most two.
   Its arc bound with h=2 is valid. Treating those fibers as singletons
   overcounts available independent bases.
5. Strictly weaker premise, by hand: over F_11, V=span(1,X,X^3)
   has singleton fibers, while every rank-two evaluation subspace has
   at most three coordinates by the degree-three root bound. It satisfies
   occupancy <=j*h with h=2, yet 0,1,10 are a dependent triple, so it
   is not an arc. Take core {0,1,10,2,3,4,5}, defect 6, K=4, m=8,
   u=0 and v zero on the core and one at the defect. The valid flat
   theorem supplies the positive lower count 4*7*5*3=420; both
   implementations recount 792 actual tuples. The weaker theorem
   therefore covers sources excluded by the arc premise.

In each case u and v are explicitly printed in the check code, b=0
is a raw-one minimizer, and full-code pair badness follows because
a degree-<K second polynomial cannot vanish at K distinct core points
and then equal one at the defect. Carrier zeros outside a complete joint
core, and the infinity fiber of a rational progression, are retained in
the finite proof rather than silently deleted.
