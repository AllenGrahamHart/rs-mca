# Plane Branch Pairs Consume Arithmetic Genus

Work over the algebraic closure. At a point p of the integral plane image,
the completed local equation factors into distinct irreducible branches
f=f1*...*fb in O=Fbar[[x,y]]. Its normalization quotient has dimension
delta_p. Completion preserves that quotient and its length, by the finite
normalization facts in [Stacks 33.41.2](https://stacks.math.columbia.edu/tag/0C1R).

For coprime branch products h,k the elementary exact sequence is

    0 -> O/(hk) -> O/(h) direct_sum O/(k) -> O/(h,k) -> 0.

The last map is the difference of the two residue classes. Its kernel
description follows from (h) intersection (k)=(hk) in the power-series UFD.
Taking lengths inside the normalization gives
delta(hk)=delta(h)+delta(k)+length O/(h,k).

For a fixed irreducible branch fi, the quotient O/(fi) is a domain.
For nonzero a,b in this one-dimensional local domain the exact sequence
0->A/(a) --times b--> A/(ab)->A/(b)->0 proves additivity of the finite
intersection lengths. Induction therefore gives

    delta_p=sum_i delta(fi)+sum_(i<j) length O/(fi,fj)
            >=binom(b_p,2).

Every distinct pair of branches meets at p, so each intersection length
is at least one. This uses PLANARITY; the weaker general-space inequality
delta>=b-1 would not justify the required quadratic branch budget.

Globally, normalization has exact sequence
0->O_C->pi_*O_Ctilde->Q->0, with length Q=sum delta_p.
Taking Euler characteristics gives
sum delta_p=p_a(C)-g(Ctilde)<=p_a(C), since the normalization genus is
nonnegative. The plane-curve equation sequence gives
p_a(C)=(eta-1)*(eta-2)/2; see
[Stacks 53.9](https://stacks.math.columbia.edu/tag/0BYA).

Summing the local inequality proves sum_p binom(b_p,2)<=g.
This remains valid for nonordinary singularities: tangencies and singular
individual branches only increase delta. Unibranch singularities contribute
zero to this branch-pair sum even when their multiplicity is greater than one.
Only the finite set of actual evaluation points is needed for the energy
bound, so omitting other geometric points cannot increase its charge.
