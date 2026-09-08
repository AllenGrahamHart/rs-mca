# Joint LIST does not remove cross-core scalar ownership

Status: PROVED obstruction, 2026-09-07. This is not a prize-row
counterexample. No speculative weighted-joint supplier is installed.

The shared-carrier extension of ordinary LIST padding is valid:
joint lists in (h_*+C') x C' use dim C', not the full tuple
dimension. This does NOT justify using the outside-of-U factor
e=n-|U| in an unrestricted MCA weighted conversion.

For a fixed minimizing pair f=(a,b), a scalar agreement may lie
in U minus H_f: it is jointly explained by another represented
pair but only scalarly explained by f. The constant kernel excludes
these labels except for its kernel slope. The nonconstant polynomial
relation excludes them except for the explicitly charged rational
direction labels. Without either relation, that exclusion is absent.

## Actual empty-universal-core counterexample

Use F_17, D={0,...,11}, K=3, m=7, d=4, C'=span{1,X}, h_*=0.
Let (u,v)=(0,0) on 0,...,5 and (u,v)=(x,-1) on 6,...,11.

For gamma=0,...,5 take h=X-gamma and S={6,...,11,gamma};
the unique minimizing b is -1, raw=1, and its complete pair is
(X,-1), with core {6,...,11}. For gamma=6,...,11 take h=0
and S={0,...,5,gamma}; the unique minimizing b is 0, raw=1,
and its complete pair is (0,0), with core {0,...,5}.

Every support is full-pair bad: six equal v-values force any
degree-<3 second polynomial to be that constant, contradicted at
the seventh point. Minima are unique because a nonconstant linear
b matches the six equal values at at most one coordinate. The
universal carrier core is empty since 1 belongs to C'.

At T=3 the union of low complete cores is ALL D, so e=0. The
empty-universal-core resource is

    F=12*11*10/(7*5)=264/7.

The proposed uncharged joint-list conversion would give

    12 <= F/(T+1)=66/7,

which is false. Every selected noncore coordinate lies in the OTHER
pair's core. The existing charged polynomial-relation proof correctly
handles these labels: the row (1,X) has preferred slopes gamma=x,
and the n charge is retained. This uses the same actual control as
the earlier omitted-preferred-label counterexample, not a new scan.

## A valid unrestricted replacement, not yet affordable

Let a_f=|H_f| and t_f=max(1,m-a_f). All selected records for one
fixed pair have at least t_f noncore coordinates, and any coordinate
outside H_f can agree with at most one of their distinct slopes.
Thus the unconditional multiplicity is at most (n-a_f)/t_f, NOT
(n-|U|)/t_f. Put c=n-m and let M_t count represented pairs with
t_f<=t. The global resource C and summation by parts give the valid

    |Gamma| <= C/(T+1)
        + sum_(t=1)^T M_t*(c/(t*(t+1))+1/(T+1)).           (J)

Indeed n-a_f<=c+t_f, including a_f>=m. The pair's discounted
weight is at most (c+t_f)*(1/t_f-1/(T+1)). Its successive
difference is c/(t*(t+1))+1/(T+1), and it vanishes at T+1.
The usual global resource covers all high labels. Joint LIST can
bound M_t, but no affordability at the original prize budget is
claimed for (J).

The next useful question is whether actual-source structure controls
these cross-core scalar labels more efficiently than the unconditional
(n-a_f) charge. The large low-core union and its joint LIST count
alone must not be substituted for that missing ownership bound.
