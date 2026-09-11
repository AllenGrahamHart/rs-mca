# A Maximal Constant Three-Pencil Has Only Root-Exceptional Children

Let V subset F[X] have dimension4, full gcd1 and actual maximum degree D.
Let W subset V x V have dimension5 and full generic projection a+z*b.
Suppose S=T*u is a constant-direction subspace of dimension3, where
u is a nonzero vector in F^2, and suppose W contains no constant-direction
subspace of dimension4. Thus S is maximal in its direction.
Put E=max degree(T/gcd(T)), so 2<=E<=D.

At every regular anchor supplied by pair_space_regular_projection_anchor:

- If x is not a common zero of T, the3/3 child has function-field rank2
  and contains a constant-direction plane.
- Otherwise the entire child equals S and is whole constant. After full
  gcd division its primitive scalar degree is E.

There are at most D-E distinct exceptional coordinates. No separability,
normalization ceiling or curve-image assumption is needed.

If N>=A>D, actual pairs have nonnegative fixed original weights, ordinary
regular children have total weight at most C>=0, and exceptional regular
children have weight at most U(E)>=0, then

    Omega <= ((N-D)*C+(D-E)*max(U(E)-C,0))/(A-D).

A constant four-pencil is excluded deliberately: it can make EVERY regular
child whole constant. A plane need not be occupied by actual pairs.
