# Proof: Extend The Box Scope And Tighten Only The Degree Cover

Put R=1048576, d=67472, D=67466, c=67467 and s=11. We reuse the
generic density-aware completion, full-fiber quotient contraction and
receiver-flat cost accounting already required by the parent interval.
The parent states its numerical conclusion only from J=32000. The
argument below checks why the same formula certificate is valid on
the additional degrees; that conclusion is not inferred from a script
accepting an out-of-range argument.

## 1. The Geometric Split Extends Below 32000

Every proper maximum-density flat has rank 1<=j<=10, size a and density
a/j, with a<=J-11+j. On every block used here, J>=30000>11 and

    a<=31998<c, R>=d, R+J>2(d+J).

The low-density case a/j<=J/11 retains the full-core greedy lower
count product_(i=0)^10(J+D-i*J/11). Each factor is positive and
increases with J. HIGH records retain the same proved charge
(J+d)*product_(i=1)^10(d+i)*10488/125; its raw>=7 gate is unchanged.

Otherwise use h_r(J)=1+(J-11)/r and choose j<=r<=10 with
j*h_(r+1)<=a<=j*h_r. This follows from the root-space bound and
the low-density split, independently of J=32000. All affine size
edges have the form alpha*J+beta with 0<alpha<=1 and beta<=0.

When j=r=1, integer fibers a>=J-2000 are already covered by the
receiver-fiber supplier on 14000..52999. The remaining integer sizes
obey a<=J-2001, so replacing that one upper edge loses no source.
Our entire new interval lies inside the supplier's scope. The separately
paid class has original-near-inclusive cap 248408859318207582.

## 2. The Same Universal Record-Cost Formula Applies

Split each affine size region into eight slices and each actual complete
pair-core occupancy z/a into 64 bins. For each block [J0,J1], use its
four size/J vertices and the two occupancy endpoints. These regions
cover all integer sizes and all record occupancies, including boundaries.

For each LOW record the complete-core packing keeps all z flat points
in an M=J+D point subset of its complete joint core. This is possible
since z<=a<c<M. It retains the old witness's actual defect and the
original minimizing pair. The quotient has rank ell=11-j, degree J-a,
nonzero evaluation count J+D-z and gap D+a-z.

The inherited certificate computes the integer degree hull [k0,E] and
lower gap D0. It checks ell<=k0<=E<=D0 and all directed-rounding,
positivity and contraction gates. Their proof depends only on these
gates, not a lower bound J>=32000: restricting to D0+(J-a) nonzero
quotient points keeps actual rank, and the certified increasing quadratic
may be evaluated at k0. The tangent remainder is nonnegative, coefficient
rounding is downward and the other profile is affine after subtracting
the retained quadratic term, so its endpoints cover the whole degree hull.
No assumed monotonicity of an optimized bound in the gap is used.

The completion factors remain

    d_i=max(c+i,J+D-(10-i)*a/j), 0<=i<j.

The exact density/degree switches occur on the same r-regions. All
positive affine product and log-concavity arguments from the parent
therefore cover the entire smaller degree blocks. Minima of each separate
positive inside-cardinality term may be added; a minimum of their sum
is not assumed to be at one vertex. Signed tangent coefficients still
use actual inside-extension ratios, with upper ratios for negative tails.
All calibrations are <c, and positivity precedes multiplication of lower
counts. Greedy, quotient-quadratic, coupled-inside and full-core bounds
are alternative valid lower costs; their maximum is available. The old
rank<=5 supplement is used only at its proved rank and positive-c scope.

Multiply the integer basis lower count by twelve for recoverable defect
insertion, then take its minimum with the HIGH cost. This gives one
uniform cost beta_v for every record in its occupancy bin. It does not
assign an independent total resource to each bin.

## 3. Receiver Groups And The Original Resource

The proved projected-pair distance is a/j, so there is at most one heavy
group with complete occupancy t>a-a/(2j). The other groups have occupancy
at most 2a-a/j-t. The unchanged same-field empty-core child bound is

    Q(t)=(R+J-a)*U_j/(d+J-t)+a-t,

using the parent's proved full dimension-(10-j) child caps, including
the exact dimension-zero cap 981105. All original exceptional labels
are charged; no new child near allowance is used.

Split t/a into eight bins [kappa0,kappa1] between 1-1/(2j) and 1.
The ratio in Q increases with a and kappa: its a-derivative has numerator
kappa(R+J)-(d+J)>=0 by the inequality in section 1. Along an upper
size edge a=alpha*J+beta, its J-derivative numerator is

    (1-alpha)d-(1-kappa*alpha)R+beta(1-kappa)
      =(1-alpha)(d-R)+(1-kappa)(beta-alpha*R)<=0.

Thus the SAME corner formula for ceil(Q_box) remains a uniform upper
bound over every smaller block. The nonnegative exception term uses
the upper J endpoint. beta_L and beta_H are uniform minima over all
record bins meeting the relevant light and heavy ranges; including a
neighboring boundary bin only weakens those costs. No-heavy sources use
the first heavy bin and its correct light threshold.

Every source box consequently satisfies

    |Gamma|+134944
      <=floor(((R+J1)_falling_12
                   +max(0,beta_L-beta_H)*ceil(Q_box))/beta_L)+134944.

This is the existing two-cost inequality on ONE original tuple resource.
Different source boxes or degrees are alternatives and combine by maximum.

## 4. Three Exact Certificates And The Union

Use the consecutive degree blocks below. Their maxima include every
record/source box and the low-density case, but not yet the separately
paid large-fiber class from section 1:

    30000..30199: 274471852330442343, at (j,r,u,v)=(8,8,7,0);
    30200..30799: 273508821582726287, at (7,7,7,0);
    30800..31999: 270145570079495459, at (7,7,7,0).

For each block there are 28160 record-cost boxes and 3520 source boxes.
Both exact implementations check every cost and source bound, with matching
streaming digests. The independent engine uses fixed branch formulas,
another coordinate scale, prefix derivatives and polynomial composition;
the new independent source wrapper uses rational arithmetic instead of
the primary wrapper's combined-denominator expression. It imports neither
primary implementation.

The maximum of these three values and 248408859318207582 is
274471852330442343. This proves NEW, including one original allowance.
Taking its maximum with the parent's 32000..169999 cap proves UNION.
No empirical endpoint interpolation, free sum over carriers or structural
assumption about a hypothetical extremizer is involved.

The gain is smaller uniform parameter boxes, not a new geometric theorem.
The earlier generic proofs and full child caps are credited prerequisites.
The full-fiber scalar-census supplier from the preceding research cycle
is not an input and no recursive convexity hypothesis is assumed.
