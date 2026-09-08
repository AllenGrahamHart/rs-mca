# Proof By Exceptional Labels And A Filtered Resource

## 1. The Explicit Exceptional Set

At each carrier-zero coordinate with v(x)!=0, put the unique agreeing
label (h_*(x)-u(x))/v(x) in E. If v(x)=0, universal-core emptiness implies
u(x)!=h_*(x), so no label agrees there. This contributes at most z labels.

On a nonzero projective fiber A, choose ell in V* and f in V with
ell(f)=1 and ev_x=f(x)*ell. Here f(x)!=0 for every x in A. Define

    alpha_x=(u(x)-h_*(x))/f(x), beta_x=v(x)/f(x).

For each unordered pair x,y in A with beta_x!=beta_y, put

    gamma=(alpha_y-alpha_x)/(beta_x-beta_y)

in E. This is at most binom(|A|,2) labels per fiber, and unioning the
sets counts repeated labels only once. It is a conservative upper bound;
identical colors or coincident secant slopes do not create extra labels.

## 2. Surviving Independent Tuples Have Distinct Fibers

Fix gamma outside E and any coordinates agreeing with its explanation.
No carrier-zero coordinate can occur, by section1. If two agreeing
coordinates x,y lie in the same fiber, their scalar equations give

    alpha_x+gamma*beta_x = ell(h_gamma-h_*)
                        = alpha_y+gamma*beta_y.

They cannot have different beta values: that would put gamma in E.
Their beta values, and hence alpha values, are equal. After dividing by
f(x) and f(y), their incidence normals (v(x),-ev_x) coincide, so the
original two normals are proportional. They cannot both belong to an
independent tuple. This proves the asserted distinct-fiber restriction.

This argument applies to the COMPLETE scalar-agreement set, not only
the selected size-m witness. A minimizing pair core and the old witness
defects used by completed-basis counts still lie in this same set.
No source, polynomial pair, label or raw margin has been reselected.

## 3. One Shared Resource

There are exactly (s+1)! e_(s+1)(a_i) ordered coordinate tuples choosing
one coordinate from each of s+1 different nonzero evaluation fibers.
Some are dependent or do not belong to any selected record; counting all
of them is a valid resource upper bound. The required support-margin
proof shows that an independent tuple determines at most one parameter
point (gamma, coefficients of h_gamma-h_*). In particular the tuples
owned by distinct selected labels are disjoint. Sum their valid lower
costs over Gamma minus E. This proves FILTERED and then COUNT.

There is no division of an exception count by a basis cost. The original
labels in E are charged first, once each. All other label costs use the
same FILTERED resource; different record cases do not receive separate
budgets. When fewer than s+1 fibers exist, this resource is zero and
there can be no surviving full-code-bad record, by the required full-rank
support argument.

## 4. A Whole-Fiber-Count Envelope

Pad the a_i with zeros to length F0 and fix their sum N=n-z. On the
compact nonnegative simplex, e_r attains its maximum. Among maximizers
choose one minimizing the sum of squared entries. If two entries a,b
are unequal, replace them by their mean. With the other entries fixed,

    e_r = e_r(rest)+(a+b)e_(r-1)(rest)+ab e_(r-2)(rest).

All coefficients are nonnegative, so this cannot decrease e_r; it
strictly decreases the sum of squares, a contradiction. The maximum
therefore occurs at all entries N/F0. This proves BALANCE after
multiplying binom(F0,s+1)*(N/F0)^(s+1) by (s+1)!.
The argument includes zero entries and is a real relaxation, not a new
fractional coordinate domain.

The incidence construction and disjoint-tuple argument are inherited
from the support-margin resource. Fiber color normalization is also
used by the existing receiver-peeling and scalar-incidence ledgers.
The present refinement is to pay the global exceptional slope SET first
and then restrict the resource for every remaining label simultaneously.
