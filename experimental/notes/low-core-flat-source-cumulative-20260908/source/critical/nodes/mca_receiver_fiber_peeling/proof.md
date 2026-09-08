# Proof: Use The Fixed Receiver, Not Independent Record Extremizers

## 1. Actual Colors And Disjoint Groups

Evaluation on A is f(x)*ell, with f nonzero there. For a chosen pair put
alpha=ell(a_gamma-h_*), beta=ell(b_gamma). Joint agreement on A is
equivalent to its normalized receiver color being (alpha,beta). Thus the
complete pair core meets A in that entire color class, not an arbitrary
subset chosen independently for each record. A selected core subset may
use fewer of its points. Distinct classes partition A, so if H>0 classes
have size >theta*a then H*theta*a<(sum of their sizes)<=a.
The zero-class case is immediate. In particular H<1/theta,
giving H<=ceil(1/theta)-1. Each original label belongs to just one group.

## 2. A Heavy Group Loses At Most a-t Original Labels

Fix its color (alpha,beta), size t, and W=ker ell. The actual rank of W
is s-1 and every W-polynomial vanishes on all of A. The common-root-space
bound gives a<=K-s+1. Its locator P_A divides W; W/P_A has actual
dimension s-1 and degree <K-a. No field extension is used.

For this ONE group gauge the words and explanations by

    u^g=u-h_*-alpha*f, v^g=v-beta*f,
    h_gamma^g=h_gamma-h_*-(alpha+gamma*beta)*f in W.

Both words vanish on C_(alpha,beta). At x in A minus C the equation
u^g(x)+gamma*v^g(x)=0 has at most one finite solution: if both
coefficients vanished x would have the same color. Remove the union of
these exceptional labels FROM THIS GROUP. Its size is at most a-t.
Every surviving complete scalar agreement set meets A exactly in C.

Outside A divide u^g,v^g and h_gamma^g by P_A. All divisors there are
nonzero. The row has length n-a, degree K-a, the same n-K and same field;
the surviving complete agreement set has at least m-t>=m-a points.
The child explanations lie in W/P_A, but their selected span may shrink.

If a degree-<K-a pair explained that complete child set, multiplying
by P_A and adding (h_*+alpha*f,beta*f) would explain its original
complete scalar agreement set: the only removed agreeing coordinates
are C, and both gauged words vanish there. This contradicts the original
full-code-bad selected subset. Full-code badness, not badness merely
inside V, is essential for this lifting argument.

There is an exact size-(m-a) bad subset of the complete child agreement
set. Otherwise explaining pairs on all such subsets agree on overlaps
of size m-a-1>=K-a. One-point exchanges connect all these subsets,
and polynomial uniqueness glues them to one pair on the whole set.
This is the same saturated-support argument as the required transport
supplier. The selected scalar explanation is retained. The uniform child
cap Q applies, proving HEAVY with no new child near removal or add-back.

The exception charge cannot simply be omitted. The small control has
an original bad slope agreeing at a nonmatching fiber point, whose
punctured complete agreement set is explained by a child polynomial pair.
Nor may one divide by only the matched color's locator: the projected
explanations vanish on the ENTIRE fiber, which supplies the stated degree.

## 3. Light Cores Have Restricted Fiber Occupancy

For a light record of raw<=T choose any fixed M-point subset of its
joint core. It has nonzero V-evaluations by universal-core emptiness,
and meets A in at most theta*a points. The required fiber-basis proof
gives at least F_A(t) ordered bases at this ACTUAL intersection size t.
Its two disjoint contributions have exactly one and zero inside-fiber
coordinates; their sum is the printed F_A, with the true degree excess e.

On each side of c, F_A is a product of positive affine factors.
Positive log-concavity bounds its minimum on [0,theta*a] by the stated
endpoints, including the kink c when present. These real endpoints are
relaxations of integer intersection sizes, not a fractional source.

Insert one actual defect at any of s+1 positions into each core basis.
This gives at least (s+1)*b_theta independent incidence tuples per LOW
record. HIGH records have at least m*P_d*L by the completed resource.
Every independent tuple determines the entire affine parameter, including
its ORIGINAL finite slope. All light labels therefore share one tuple
budget at most n_falling_(s+1), even after the heavy labels were removed.
Use the smaller per-record count, proving LIGHT. Only then add the bounds
for the disjoint heavy groups. Different groups may have different received
children; the explicit factor h pays for them. This proves PEEL.

## 4. A Useful Monotone Range

All l factors of P_e(M-t) are at least c+a-t>0 on 0<=t<=a/s.
For t<c its logarithmic derivative plus the last factor's derivative is
at least

    -l/(c+a-t) + l/(c+l*t) >=0,

because s*t<=a. For t>=c the last term is 1/t, and
1/t-l/(c+a-t)>=0 follows from s*t<=c+a. Continuity at c gives
monotonicity across that point too. Hence b_theta=F_A(0) for theta<=1/s.

This theorem uses actual receiver classes and explicit exceptions. It
does not assume their existence or cardinality from a hypothetical carrier,
and does not promote finite survival evidence to a universal statement.
