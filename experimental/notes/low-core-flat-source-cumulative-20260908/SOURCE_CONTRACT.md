# Exact direct source contract

Current all-carrier addition: J=23000..23999, following the proved
J=24000..29999 intervals, uses the same normalized source below but needs
no canonical maximal-raw selector. Its statement and assembly section13
are authoritative. The new source-fiber payments use a>=J-6000 on
21000..52999 or a>=J-8000 on23000..52999. These are alternative whole-source
bounds, not new premises on the every-carrier intervals. The remaining
original rank-twelve gap is J=9941..22999. Older density/mass statements
on23000..29999 and the degree-4700/8000 gates no longer constrain this gap.


This is the inherited contract for the older lower-strip and source-class
bounds. The [new high-interval statement](source/critical/nodes/rate_half_mca_maximum_density_high_interval/statement.md)
does not require its canonical selector; the [original-source assembly](source/critical/nodes/rate_half_mca_rank_twelve_paid_interval_assembly/proof.md)
proves the bridge from the stated original rank/core classes to this
contract. It is not a predicate assignable for free to an arbitrary v4 residual.

Let F have size 2130706433^6 and D be ANY set of n=1048576+J distinct
F-points. Let m=67472+J, 4801<=J<=169999, V a polynomial F-space
of ACTUAL dimension eleven and degree <J, and h_* a polynomial of
degree <J. Let (u,v) be an arbitrary received pair on D.

The universal carrier core is required to be empty:

    {x in D: V(x)=0, v(x)=0, u(x)=h_*(x)} = empty.

Let Gamma be a set of DISTINCT finite labels gamma in F. Every label
must have an explanation h in h_*+V and a size-m support S with
u+gamma*v=h on S, such that NO pair of degree-<J polynomials explains
(u,v) on S. Full-code badness is stronger than badness merely relative
to V. All counting is uniform in this source; alternative sources are
not summed.

For each gamma maximize the minimum mismatch count

    raw(S)=min_(b in V) |{x in S: v(x)!=b(x)}|

over ALL its size-m full-bad supports and explanations in the SAME fixed
carrier, and choose one maximizer. Set T=500. The canonical selection
lemma, using 2T<67472, proves that at raw<=T the minimizing allowed
pair (a,b)=(h-gamma*b,b) has complete joint core H satisfying

    {x:u(x)+gamma*v(x)=h(x)} = H disjoint_union D_gamma,
    |D_gamma|=raw, D_gamma subset S, |H|>=m-raw.

Every D_gamma is nonempty. For different labels assigned to the same
pair, the D_gamma are disjoint outside its OWN complete core. No union
of other cores may be substituted for that core. LOW means raw<=500;
all other labels remain HIGH, even after a partition of LOW pairs.

The included ordered-normal-basis proof gives, without whole-line farness,

    sum_Gamma min(67473,raw_gamma) <= F(J),
    F(J)=prod_(i=0)^11(1048576+J-i)
         / ((67472+J)*prod_(i=1)^10(67472+i)).

Consequently, for ANY disjoint assignment of represented LOW pairs to
groups (their labels stay with them),

    |Gamma| <= F(J)/501 + sum_groups G_i,
    G_i = sum_(gamma assigned to i)(1-raw_gamma/501).

The resource is used once. Each individual represented LOW pair has
at most 981604 original finite labels. Constant-direction group bounds
that include F(J)/501 are COUPLED expression bounds, not independently
maximized group gains.

## Meaning of the original-row add-back

The direct mathematical statement proved in this packet is an upper bound
on |Gamma|+134944 under the above hypotheses. Writing it as
N_original is justified ONLY when Gamma exhausts the transported post-near
labels of the original row, with at most 134944 omitted near labels.
The packet does not assume this for every received pair without proof.

The included common-core transport shows how G-saturated supports are
cancelled by their locator, preserving field, labels, degree gap, carrier
dimension and raw counts. Reselect canonically on the normalized source;
do not pretend arbitrary old support choices were maximal. To identify a
particular upstream rank-twelve residual with this source, verify its
actual carrier, entire universal core, saturated full-bad supports and
original near bound. These are explicit transport obligations, not
equalities inferred from matching numerical row parameters.

The interval theorems prove bounds for EVERY source in this contract
with 4801<=J<=9940. They assume no interpolation relation, conic/cubic
cover, field-drop, random-fiber assertion, or numerical MCA Hensel bound.
The source contract itself is unchanged from the earlier packets; the
covered interval is enlarged by multiplicity and raw-weighted accounting.

The completed-basis resource also proves weight >=5500 for every HIGH
label (raw>=501). With C=23067643444721720934, an all-LOW pair cap M
therefore gives the whole-source bound

    |Gamma|+134944 <= C//5500+134944+981604*M.

M must include every represented LOW pair, including any singular and
off-curve exceptions. The older /501 group ledger above remains valid;
do not add its full resource to this alternative /5500 resource.

## Finite theorem interfaces

- One nonsingular conic, on 4801..169999:
  |Gamma|+134944<=170738199574037868.
- Full-kernel strip, on 4801..7116:
  |Gamma|+134944<=272837082962714299.
- Complete cubic strip, on 7117..8655:
  |Gamma|+134944<=274979661292365251.
- LOW-101 continuation, on 8656..8763:
  |Gamma|+134944<=274903465748372176.
- Complete quartic strip, on 8764..9526:
  |Gamma|+134944<=274979661975561635.
- Complete double-point cubic tail, on 9527..9821:
  |Gamma|+134944<=274778805314695460.
- Raw-weighted continuation, on 9822..9940:
  |Gamma|+134944<=274811931500367244.
- Combined entire interval, on 4801..9940:
  |Gamma|+134944<=274979661975561635.
- Original-row target budget: floor(|F|/2^128)=274980728111395087.

The first line requires the declared single-conic premise. The entire-
interval theorems do not assume a curve premise. None is an unrestricted
original-row theorem. The not-fully-paid normalized range is 9941..169999;
original normalization/near and active-owner transport remain separate.

## Cumulative resource interface

On the SAME canonically selected source the completed-basis proof gives
w(r;g)>=11*min(r,500). For any integer 1<=T<=500, define
L_t=#{gamma:raw_gamma<=t} and S_t=sum_(gamma:raw_gamma<=t) raw_gamma.
The one resource gives the equivalent expressions

    |Gamma|<=floor(C/(11T)+(1/T)*sum_(t=1)^(T-1) L_t)
            = the same upper bound written as
              floor(C/(11T)+sum_(t=1)^(T-1) S_t/(t*(t+1))).

The equality identifies the two expressions, not attainment of the bound.
The pair-to-label conversion preserves complete cores. If M_t bounds all
represented pairs with at least m-t joint agreements, disjoint defects
give S_t<=(n-m+t)*M_t, including every exceptional pair in M_t.
This is a newly derived resource conversion, not insertion of old /501
discounts into a /5500 resource. The original near allowance is still once.

The full double-point kernel on 9527..9821 supplies a degree-<=3 cover
with <=256 off-cover pairs and factor weighted degree <2*(J+66972).
Neither the old <J+66972 height bound nor the old 64 exceptions may be
used for that cover. Its full factor accounting is included separately.

## Additional Whole-Carrier Interfaces

The core-basis suppliers only require a selected full-code-bad support
per label, not maximal raw selection. The finite statements retain the
source above and impose the following ADDITIONAL carrier conditions:

- On 10000..169999, nonzero evaluations are pairwise projectively distinct
  and every at most eleven are independent:
  |Gamma|+134944<=273674135808267711.
- On 23000..169999, every j-dimensional subspace of V*, 1<=j<=10,
  contains nonzero evaluations of at most j*h ORIGINAL coordinates,
  for some real 1<=h<=(J-1)/10:
  |Gamma|+134944<=268724670028139326.
- On 65000..169999, some projective evaluation fiber contains at least
  ceil(J/2) nonzero ORIGINAL coordinates:
  |Gamma|+134944<=274929007493481160.
  This theorem uses LOW<=6, HIGH>=7 and weight floor 10488/125;
  the older LOW<=500 partition is not substituted into this proof.

These are entire-source counts without a pair-curve premise or off-curve
exceptions. The second includes full rational progression carriers,
including those described only after constant-field extension. Field,
original coordinates, defects and slope denominator never change.

These hypotheses are not automatic. Bounding projective fibers alone
does not establish higher-dimensional occupancy. In the second interval,
an over-budget source must violate this occupancy bound and have
dim_k{v in V_k: rho*v in V_k}<=9 for every extension of constants k/F
and nonconstant rho in k(X). The consumer proves both restrictions;
the failed occupancy condition means some rank 1<=j<=9 flat has at least
floor(j*(J-1)/10)+1 nonzero evaluations. On 65000..169999 every fiber
must additionally have size <=ceil(J/2)-1. Intermediate fibers and
higher-dimensional concentration remain unpaid by this packet.

Earlier frozen source status pages retain their historical intervals.
This contract and README identify the cumulative scope; use the explicit
proof paths there rather than interpreting old status prose as current.
