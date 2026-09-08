# Proof On One Original Incidence-Tuple Resource

## 1. LOW Uses The New Hereditary Density Theorem

For each raw<=6 selected label, its already fixed minimizing pair has
at least m-6=J+D joint agreements. Choose exactly J+D core points.
Every such evaluation on V is nonzero: a zero evaluation in the joint
core would have u=h_* and v=0, violating empty universal carrier core.
The full source's proper-flat density bounds this subset's density too.

Since floor(11^2/4)=30, DENSITY gives the required basis count

    P(J)=product_(i=0)^10(D+J-i*(J-1)/10).

The old witness supplies an actual defect. Insertion in twelve recoverable
positions gives at least 12*P(J) original independent incidence tuples.
This does not change its minimizing pair, selected explanation or slope.
All independent tuples on different labels are disjoint, as in the
required completed-basis resource.

Put U(J)=(R+J)_falling_12, L=23000 and E=29999. The factors of P
are D+1+alpha*(J-1), alpha=0,1/10,...,1. On the whole real [L,E],

    (log P)' >= (11/2)/(D+E),
    (log U)' <= 12/(R+L-11),
    11*(R+L-11) > 24*(D+E).

Thus U/P decreases throughout the interval. Exact rational arithmetic gives

    floor(U(L)/(12*P(L)))+134944 =268913508505087358.       (LOW)

This is analytic interval coverage, not interpolation between samples.

## 2. HIGH Retains Its Previous Weight

Let P_d=product_(i=1)^10(d+i). The earlier completed-basis weight for
7<=r<=84 is at least

    12*r*(1-11*r/(d+1)).

Indeed the ten product factors and (m-r)/m are each at least
1-r/(d+1); their product is at least 1-11*r/(d+1). The displayed
quadratic increases on [7,84], since 22*84<d+1, and its value at seven
exceeds 10488/125. For r>=84, including r>d, the truncated mismatch
weight is at least 84. Hence every HIGH record uses at least
(d+J)*P_d*10488/125 original tuples.

The crude endpoint-separate bound suffices uniformly:

    floor(125*U(E)/((d+L)*P_d*10488))+134944
       =166836445768446334.                              (HIGH)

LOW and HIGH share ONE tuple budget. Consequently the total number of
labels is bounded by U divided by the smaller record cost, and the two
whole-family bounds combine by MAXIMUM, not addition. LOW is larger and
gives PAYMENT. The added 134944 is the original allowance once, not a
new near event on any contracted basis space.

## 3. Remaining Maximizing Flat Ranks

A proper maximizing rank-j flat is spanned by its contained evaluations;
otherwise its smaller span has strictly larger density. Its polynomial
annihilator has dimension 11-j and vanishes at all a coordinates. Root
capacity gives a<=J-11+j, so h=a/j<=1+(J-11)/j.

The sufficient integer gate is

    (30-j)*J <= j*D+330-30*j.

For j=8,9,10 its largest allowed J is respectively 24537,28916,33734.
The right-hand density bound decreases with j, since J>11. This proves
the stated rank gates and their contrapositive restrictions. The interval
does not shrink: small-rank dense flats can still evade this result.

## Provenance And Limits

The completed-basis defect count, raw weight, polynomial flat root bound
and original-source transport are existing suppliers. The new point is
that a hereditary moment condition permits the full basis product on an
explicit actual-source class. The density-free product is not used: the
required generic node supplies its exact large-fiber counterexample.
Neither an unproved recursive envelope nor a sampled source classification
is substituted for DENSITY. Both prize problems remain open.
