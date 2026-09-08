# Proof by scalar-agreement dimension descent

## Uniform actual-slope induction

Set U_1=4070947, supplied by the required weighted-line theorem,
including its rank-zero case. For 2<=s<=11 define

```text
U_s = floor((1048576+s)*U_(s-1)/(67472+s)).
```

Induct on the allowed explanation dimension s, simultaneously over
every 1<=K<=1048576 and every exact same-support bad selected family
on (1048576+K,K,67472+K). The base is the required rank-one theorem.
If actual dimension is smaller than s, use induction, since U_s>=U_(s-1).
Otherwise K>=s, and at every nonzero evaluation the required
scalar-agreement theorem gives a child in dimension at most s-1 on
the exact shortened row. Induction bounds each such child by U_(s-1).
The theorem's common-zero incidence ledger then proves |Z|<=U_s.

This uses no post-near hypothesis, same-rank branch, cutoff, raw margin,
optimized numerical table or Johnson bound. The exact finite values are

```text
s      U_s
1      4070947
2      63264449
3      983145945
4      15278131113
5      237419535554
6      3689407679988
7      57331172265517
8      890879518951761
9      13843347021828845
10     215108323408189165
11     3342468347844980987
```

Every line is certified by
(67472+s)*U_s <= (1048576+s)*U_(s-1)
< (67472+s)*(U_s+1). There is no ambient-degree scan behind this table.
The old bounds |Z|<ceil(4100000*(79/5)^(s-1)) remain valid:
U_1<4100000 and (1048576+s)/(67472+s)<79/5 for s>=2.

## Large-field refinement

The required padded-Johnson theorem strengthens the simultaneous caps to
V_9=10755802499540570 and V_10=156765527508668296 whenever
|F|>=2097152. Its seven certificates and degree induction include
the cost of nonuniversal common-zero removals. The field-independent
induction above is retained as a separate valid result. The original
KoalaBear field, and all children used here, satisfy the new field gate.

## Error-rank gauge

The elementary gauge is unchanged. If the selected family has at most
one slope, its claimed bound is immediate. Same-support badness implies
r_1 is not a codeword, since otherwise (h_gamma-gamma*r_1,r_1)
would explain the received pair on the selected support.

Choose gamma_0 and form

```text
E = span{(gamma-gamma_0,h_gamma-h_gamma0)} subset F direct_sum C.
```

The linear map (delta,c) -> delta*r_1-c is injective on E:
a nonzero delta in its kernel would make r_1 a codeword. Its image
is the error-difference space, of dimension a<=11. The slope projection
of E is nonzero; choose (1,b) in E. Replacing

```text
r_1 by r_1-b,        h_gamma by h_gamma-gamma*b
```

leaves scalar errors and the exact supports unchanged. Subtracting b
from a pair's second explanation and adding it back proves two-way
preservation of same-support pair containment. The new explanation
differences form the zero-slope kernel of E, of dimension a-1<=10.
The field-independent theorem gives |Z|<=U_10; on the actual KoalaBear
field its new refinement gives the stronger |Z|<=V_10.

## Near add-back and selection scope

For the complete post-near selection in the statement, the disjoint
near set has at most 2d=134944 slopes by the required two-anchor
near theorem, whose gate 3d<=1048576 holds. Thus

```text
|Z_bad| <= V_10+134944
        =156765527508803240
        <274980728111395087,
slack  =118215200602591847.
```

This strengthens the preceding scalar-only total 215108323408324109.
It does not pay error rank twelve: even before near add-back, the new
V_11=2283382040940633027 exceeds the budget. No all-source rank
bound has been supplied.

When a support-wise bad witness is larger than m, an exact m-point
bad subset exists. Otherwise explaining pairs on adjacent m-subsets
agree on m-1>=K points and hence coincide; connectedness of one-point
exchanges would give one pair on the entire witness, a contradiction.
Selection precedes the error-rank test. Changing it may change that rank,
so the complete-selection hypothesis is retained without modification.

The historical raw_low_alternative.md is a separate proof of the weaker
constant and is not used here. No v4 owner ledger is asserted.
