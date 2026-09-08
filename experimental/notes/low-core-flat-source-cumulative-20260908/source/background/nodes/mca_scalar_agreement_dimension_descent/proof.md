# Proof

## A nonzero evaluation gives a proper child

Fix x outside the common zero set T. Choose c in C' with c(x)!=0
and put

```text
b_0 = (r_1(x)/c(x))*c,
a_0 = h_* + ((r_0(x)-h_*(x))/c(x))*c.
```

These are one COMMON polynomial pair for all incident records;
b_0 lies in C', a_0 in h_*+C', and they match the received pair
at x. For every record whose SELECTED support contains x,

```text
v_gamma = h_gamma-a_0-gamma*b_0
```

lies in C' and vanishes at x. Evaluation at x is a nonzero linear
functional on C', so its kernel has dimension s-1. On D minus {x},
divide the received pair minus (a_0,b_0) and each v_gamma by X-x.
The new explanations lie in the injective image of this kernel and
have degree <K-1. They retain the same distinct finite slope labels.

Each chosen support becomes EXACTLY S_gamma minus {x}, of size m-1.
If a degree-<K-1 pair explained the shortened received pair there,
multiplying by X-x and adding (a_0,b_0) would give a degree-<K
pair explaining the original received pair on S_gamma, including x.
This contradicts the original same-support hypothesis. Thus badness is
preserved in the FULL child code, not merely the chosen subspace.
When K=1, the child code is the zero space and the same argument applies.

There is no same-dimension alternative: evaluation at x was nonzero.
There is no exact-support reselection: the anchor was selected through
the original scalar support rather than through a complete pair core.
No old margin or post-near condition is asserted in the child.

## Charge the common zeros instead of shortening on them

Division by the locator of T embeds C' into degree-<K-z polynomials.
Consequently s<=K-z. At x in T, every explanation has the same
value h_*(x). The selected-support incidence equation is therefore

```text
r_0(x)+gamma*r_1(x)=h_*(x).
```

A coordinate counted by g can be incident to at most |Z| selected
records. A coordinate counted by tau can be incident to at most ONE,
because the slope is unique. A remaining coordinate of T is never
incident. Distinct slope labels are essential for the one-record charge.
Counting the m|Z| original support incidences gives

```text
m|Z| <= sum_(x outside T) U_x + g|Z| + tau.
```

This proves the first ledger. It accounts for exceptional zero
coordinates without assuming that all common zeros are universally
satisfied, discarding a whole slope family, or using a lossless branch.

## Uniform envelope

Let e=z-g and j=K-z, so j>=s, 0<=tau<=e, and

```text
((n-z)U+tau)/(m-g) <= ((R+j)U+e)/(d+j+e)
                  <= (R+j)U/(d+j)
                  <= (R+s)U/(d+s).
```

For the middle comparison, cross multiplication leaves
e*((R+j)U-(d+j))>=0, since R>=d and U>=1. For the last,
(R+j)/(d+j) decreases in j because R>=d. All denominators
are positive. Flooring is valid because the original count is integral.

If uniform integer caps U_(s-1) are already known for all shortened
rows with these R,d and smaller actual dimension, this proves
U_s=floor((R+s)U_(s-1)/(d+s)). The caps do not decrease, so
smaller actual dimensions are covered as well. This is an induction
on dimension ONLY; no induction through same-rank ambient degrees
and no numerical extremum over K is needed.

## Exact rank-zero base

Suppose all explanations equal h_*. Let g_0 count coordinates where
(r_0,r_1)=(h_*,0), without restricting to T. Every other coordinate
supports at most one selected slope. A selected support needs at least
max(1,m-g_0) such coordinates: if it needed none, (h_*,0) would
explain the received pair on that same support. Therefore

```text
|Z|*max(1,m-g_0) <= n-g_0.
```

If g_0>=m-1 the quotient is at most n-m+1. Otherwise set
t=m-g_0>=2; (n-g_0)/t=1+(n-m)/t<=n-m+1.

The cap is attained for a selected rank-zero family: take h_*=0,
put (r_0,r_1)=(0,0) on m-1 coordinates, and put (-gamma_j,1)
on each of the other n-m+1 coordinates, using distinct field elements
gamma_j. There are enough since |F|>=n. Each selected slope gamma_j
has the m-point zero-explanation support consisting of the common core
and its own coordinate. A polynomial of degree <K explaining r_1
there would vanish on m-1>=K points, hence be zero, contradicting the
remaining value one. For K=0 the only polynomial is already zero.
Only this selected family is asserted; unselected explanations are not counted.
