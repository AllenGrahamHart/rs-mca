# Full-Core Contraction Followed By A Linear Relaxation

For a pair(a,b) in(h_*+V) x V, its complete joint core occupies
exactly one receiver colour, if any, on each nonzero evaluation fibre.
Every coordinate of that colour is in the core. At a zero evaluation,
joint agreement would give u=h_* and v=0, contradicting the empty
universal carrier core. Thus H is a union of COMPLETE nonzero colour
classes, using at most one class per evaluation fibre.

For any class of size w, the kernel of its evaluation functional has
dimension s-1 and vanishes on every class coordinate. The locator
root-space bound gives w<=K-s+1. This is a bound on each class,
not a bound on the sum of unrelated large classes.

Fix a class A in H. It is the ENTIRE evaluation fibre relative to H.
The required full-fibre contraction identifies its annihilator divided
by the full locator with a degree-<(K-|A|), rank-(s-1) polynomial
space, with nonzero evaluations on H minus A. Its size is at least

    M-|A|=D+K-|A|.

Choose that many child coordinates. The polynomial root bound preserves
the child rank, and F(K-|A|) lower-bounds its ordered bases.
Each of the |A| possible first coordinates of a basis in H leaves
exactly this contraction. Hence

    B_s(H)>=sum_(classes A contained in H) |A|*F(K-|A|). (CONTRACT)

This is the actual full-core contraction, not contraction of a whole
evaluation fibre that also contains other receiver colours.

The right side uses at least M coordinates. Since costs are nonnegative,
discarding excess mass cannot increase its minimum. Relax the remaining
allocation to arbitrary 0<=x_i<=w_i with total M, without enforcing
whole-class membership or the one-class-per-fibre constraint. This
enlarges the feasible set and can only LOWER the minimum. It proves(TRIM).

Because F is nondecreasing, the cost per coordinate F(K-w_i) decreases
with w_i. If an allocation uses a more expensive coordinate while a
cheaper class has unused capacity, move mass to the cheaper class.
Repeating these exchanges gives the largest-first allocation. It may
take part of its last class; no claim that this relaxation is itself
a complete core is needed.

For(TAIL), each class larger than c has size<=E, since its size is
part of the total heavy mass. Every light coordinate costs at least
F(K-c), and every heavy coordinate costs at least F(K-E).
An M-coordinate allocation contains at most E heavy coordinates.
As F(K-E)<=F(K-c), its cost is at least

    (M-E)*F(K-c)+E*F(K-E).

Here E<=K-s+1<M, so the coefficients are nonnegative. All coordinates
are charged once. Finally every coordinate cost is at least
F(K-max w_i), giving the stated comparison to the old maximum-only bound.

This is a row-independent deterministic basis theorem. Turning bases
into a bad-slope count requires the consumer's actual-defect insertion,
label uniqueness, all-HIGH resource and original source allowances.
