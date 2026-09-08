# Historical raw-low alternative

This complete alternative proves the older, weaker constant. The current
proof.md uses scalar-agreement dimension descent and does not require
the raw-low or margin-resource suppliers. Their mathematical proofs remain
valid; this archived alternative is not a premise of the current proof.

## Actual-slope induction

Induct on the permitted explanation dimension s. The rank-one theorem,
including its rank-zero case, gives `|Z|<=4070947<M_1=4100000` on every
row, establishing s=1. Fix s>=2. Smaller actual dimension is already
covered, since M_s is increasing. Thus suppose the actual enclosing
direction space has dimension s, K>=s, and |Z|>=M_s.

The scan-free recurrence theorem gives

```text
Lambda_s(K;M_(s-1),512)<=M_s<=|Z|.
```

The inverse-pigeonhole formula guarantees that the raw-low core incidence
load I in the shortening theorem is at least M_(s-1): after subtracting
H=floor(C_s(K)/513), its defining quotient exceeds M_(s-1)-1. In
particular I>0, so an incident base pair exists.

A proper pair-difference span gives at least M_(s-1) ORIGINAL distinct
slopes on the shortened row with direction dimension at most s-1. Exact
bad-support reselection is supplied by the required shortening theorem,
so this contradicts induction. A full span shortens the entire family
without losing any slope and keeps dimension s. Reapply the same uniform
inequality on that row, recomputing the margin and exact supports. Such
lossless steps decrease K and cannot persist at K=s. A proper step is
therefore forced, yielding the same contradiction. This proves |Z|<M_s
for all K, with no post-near assumption in the induction.

Since the slope count is integral,
`|Z|<=ceil(X_10)-1<X_10<254610000000000000` at s=10.

## The error-rank gauge, with no numerical router imported

This is the existing error-rank gauge argument, reproduced to make clear
that none of the older router's scanned numerical consequences is needed.
If Z has at most one element, the final bound is immediate. Otherwise
same-support pair noncontainment implies r_1 is not a codeword: if it
were, `(h_gamma-gamma*r_1,r_1)` would explain the received pair there.

Fix gamma_0 and form

```text
E=span{(gamma-gamma_0,h_gamma-h_gamma0)} subset F direct_sum C.
```

The map `(delta,c)->delta*r_1-c` is injective on E, since a nonzero
delta in its kernel would put r_1 in C. Its image is the error-difference
space, of dimension a<=11. The slope projection of E is nonzero. Choose
`(1,b) in E`; b is a codeword. Under

```text
r'_1=r_1-b,           h'_gamma=h_gamma-gamma*b,
```

the explanation differences are the image of E under
`(delta,c)->c-delta*b`. This image is its zero-slope kernel, of dimension
a-1<=10. Errors and scalar agreement supports are unchanged. Subtracting
b from the second component of a pair explanation, and adding it back,
proves two-way preservation of same-support containment as well.
Apply the uniform shortened-family result at K=R to this gauged family.

## Near add-back and exact-record scope

The existing two-anchor near-rational theorem applies since
`3d=202416<=R`. It bounds the disjoint set N by `2d=134944` slopes.
Thus

```text
|Z_bad|<=254610000000000000-1+134944
        =254610000000134943
        <274980728111395087.
```

The slack is 20370728111260144. No claim that this is the optimal bound
is made.

If a support-wise bad witness is originally larger than m, an exact m
bad subset exists: otherwise explaining pairs on adjacent m-subsets agree
on at least m-1>=K points, hence coincide. Connectedness under one-point
exchanges would then give one pair on the entire witness, contradicting
its badness. This justifies complete exact-record selection before the
error-rank hypothesis is tested; changing a selection can change that
rank, so the theorem retains the existential selection hypothesis.

No bounds over different selections or owners have been added. The
contrapositive says that every complete selection on an unsafe line has
rank at least twelve. It does not exclude those higher-rank families.
