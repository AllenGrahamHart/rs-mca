# Bounded evaluation flats, large fibers and the normalized rank-twelve residual

Historical overview at commit ef8e3316. The [current contribution](README.md)
adds every-carrier high-interval coverage and original-source transport.
Statements below about those tasks remaining open describe the earlier
snapshot, not the current contribution. Its source-class theorems remain valid.

~~~yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: large-fiber sources on 65000..169999 satisfy |Gamma|+134944<=274929007493481160; bounded-flat and lower-strip scopes below
architecture: DIRECT
atom_or_cell: normalized rank-twelve source classes, not an active-v4 owner
quantifier: every source satisfying SOURCE_CONTRACT.md and the theorem's stated interval and carrier conditions
projection_and_unit: distinct original finite affine slopes, counted once
claimed_bound: 274929007493481160 for large-fiber sources on 65000..169999; other scopes below
status: PROVED
impact: LOCAL_ONLY
falsifier: a contract source satisfying a stated carrier condition and exceeding its printed slope bound
replay: python3 -B experimental/notes/low-core-flat-source-cumulative-20260908/replay.py
~~~

Agent: Codex acting for AllenGrahamHart, 2026-09-08. Complete local hand
proofs submitted for independent review, not a claim of external acceptance.
This grouped companion extends [the previous snapshot](../low-core-multiplicity-cumulative-20260908/README.md)
without altering it or Hughes's #1175 branch.

## Follow-Up: Large Projective Fibers

The [new short proof](source/critical/nodes/mca_projective_fiber_core_basis_resource/proof.md)
counts bases using the annihilator of an actual projective evaluation
fiber. After dividing its locator, the remaining polynomial degree excess
is retained. Exactly-one-inside and zero-inside basis classes are disjoint;
their sum has its minimum at three explicit endpoints. Inserting one
actual defect then supplies independent incidence tuples on the original
coordinates, without descending the receiver.

For EVERY source satisfying [SOURCE_CONTRACT.md](SOURCE_CONTRACT.md), with
`65000<=J<=169999` and one projective fiber of size `a>=ceil(J/2)`, the
[finite theorem](source/background/nodes/rate_half_mca_cancelled_low_core_relation_payment/large_projective_fiber_payment.md)
gives

~~~text
N=|Gamma|+134944 <= 274929007493481160,
reserve >= 51720617913927.
~~~

LOW raw<=6 and HIGH raw>=7 use ONE tuple budget, combined by maximum,
not addition. Four explicit lower envelopes and derivative/convexity
inequalities cover all J and all admissible fiber sizes. This class lies
outside the earlier bounded-flat hypothesis, so this is a new source-class
payment, not a rechecking of the same class.

The bounded-flat proof also works for REAL `h>=1`. The finite hypothesis
can therefore be weakened from `h<=floor((J-1)/10)` to `h<=(J-1)/10`
without changing its bound. The unpaid-source restriction below now
uses ranks 1..9 and `floor(j*(J-1)/10)+1`; rank ten is automatic by roots.
The stronger all-carrier maximum-density argument still being audited
locally is NOT included in this publication.

## Main Contribution: Count Core Bases Directly

For an s-dimensional polynomial carrier V, suppose every j-dimensional
subspace of V* contains nonzero evaluations from at most j*h original
coordinates, for 1<=j<s. On a selected size-m bad support let r>=1 be
the minimum mismatch to b in V, and g the number of universally agreeing
zero incidence normals. The [generic theorem](source/critical/nodes/mca_projective_flat_core_basis_resource/statement.md)
and its [short proof](source/critical/nodes/mca_projective_flat_core_basis_resource/proof.md)
give at least

~~~text
beta(r)=(s+1)*r*prod_(j=0)^(s-1)(m-r-g-j*h)
~~~

independent ordered incidence tuples when the last factor is positive
(use zero otherwise). Choose s independent core evaluations, then insert
one actual defect in any of s+1 positions. The resulting tuple determines
the complete affine parameter vector, hence belongs to at most one slope.

The old completed-basis lower count and beta share the SAME tuples:
combine them by maximum, not addition. Monotonicity of beta at small r
and the old lower count at large r give a complete source bound using
one resource. No curve containing selected polynomial pairs is required.

The hypothesis is weaker than a projective arc with fibers of size <=h,
but stronger than a fiber-size bound alone. A positive-bound non-arc
example satisfies it; another example defeats the fiber-only substitution.
Zero normals, repeated fibers and the rational point at infinity are
covered explicitly in the [controls](source/critical/nodes/mca_projective_flat_core_basis_resource/controls.md).

## Exact Finite Consequences

Write N=|Gamma|+134944 under the [unchanged source hypotheses](SOURCE_CONTRACT.md):
actual carrier dimension eleven, full-code-bad supports, empty universal
carrier core, original field, coordinates and distinct finite labels.

| Additional carrier condition | J interval | Bound on N |
| --- | --- | ---: |
| Projectively distinct nonzero evaluations; any at most eleven independent | 10000..169999 | 273674135808267711 |
| Every j-flat has <=j*h nonzero original evaluations, real h<=(J-1)/10 | 23000..169999 | 268724670028139326 |
| One projective fiber has >=ceil(J/2) nonzero original evaluations | 65000..169999 | 274929007493481160 |

The first two reserves are respectively 1306592303127376 and 6256058083255761.
The [finite proof](source/background/nodes/rate_half_mca_cancelled_low_core_relation_payment/projective_arc_carrier_payment.md)
uses T=500, beta(1) for LOW, and completed weight >=5500 for HIGH.
The two quotients combine by MAXIMUM. Exact derivative inequalities prove
the all-J extension, not a scan of sample rows.

The second class includes every full progression carrier

~~~text
V=q*span{B^10,A*B^9,...,A^10}, gcd(A,B)=1,
rho=A/B nonconstant, h=max(deg A,deg B), deg q+10h<J.
~~~

This description may hold after any extension of CONSTANTS k/F.
Homogeneous interpolation includes poles, and each rational fiber contains
at most h original points. There is no assumption that the receiver descends
along these fibers and no change to the slope denominator.

Consequently an over-budget source on 23000..169999 must have BOTH:

1. A j-dimensional dual subspace, 1<=j<=9, containing at least
   floor(j*(J-1)/10)+1 nonzero original evaluations.
2. For every extension of constants k/F and nonconstant rho in k(X),
   dim_k{v in V_k: rho*v in V_k}<=9.

The second restriction uses an elementary dimension-ten classification
into the paid progression class. These are proved restrictions on the
remaining source, not new speculative premises or a claim that it is paid.
On 65000..169999 the large-fiber theorem additionally forces EVERY
projective fiber of an over-budget source to have size <=ceil(J/2)-1.

## Grouped Companion: Every-Carrier Coverage Through 9940

The [raw-weighted strip proof](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/raw_weighted_strip.md)
adds 119 integer J values, 9822..9940, with

~~~text
N<=274811931500367244, reserve>=168796611027843.
Combined every-carrier interval: 4801..9940.
Uniform bound on that combined interval: 274979661975561635.
~~~

It uses a full double-point kernel at accounting cutoff 125, actual factor
height <2A, at most 256 off-cover pairs, and a raw-margin SUM per pair.
All cubic and reducible factor patterns are priced. The large-line branch
explicitly handles raw margins 126..500; it does not silently omit them.

The [all-multiplicity method boundary](source/critical/nodes/mca_multiplicity_interpolation_curve_escape/cubic_recipe_boundary.md)
proves that the same sufficient degree-three kernel criterion fails for
EVERY multiplicity and positive cutoff on 9981..169999. Convexity and
an analytic bound for all multiplicities >=5 prove this without an
unbounded search. It is a limit of this recipe, NOT an unsafe MCA source.

## Review, Replay And Remaining Work

[REVIEW.md](REVIEW.md) isolates the short new arguments and risk points.
[PROVENANCE.md](PROVENANCE.md) credits upstream prerequisites, distinguishes
the new contribution from earlier ones and maps the local dependency DAG.
[VALIDATION.md](VALIDATION.md) records bounded serial arithmetic/control tests.
The manifest freezes 241 source files: 224 unchanged from commit 1a87f28f,
seven revised for real h, and ten new for the large-fiber theorem.
The replay runs 62 checks with a 15-second child timeout and rejects four
manifest mutations. No external dependencies or large computation are needed.

The higher-J classes have ESSENTIAL structural hypotheses; general
every-carrier coverage still ends at 9940. Normalized concentrated sources,
higher original ranks, exhaustive original-source/near transport and
active-v4 ownership/inherited charges remain open. No compiler atom,
unrestricted adjacent endpoint, ordinary LIST bound or prize closes.

## Compute Requests

None. Intermediate fibers and higher-dimensional occupied flats still
need payment with their actual polynomial kernels, original labels and
one accounting resource. The submitted theorem does not cover those cases.
