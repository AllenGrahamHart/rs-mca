# Bounded evaluation flats and the normalized rank-twelve residual

~~~yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: bounded evaluation flats pay the declared whole high-J source classes; every normalized source on 4801..9940 is paid
architecture: DIRECT
atom_or_cell: normalized rank-twelve source classes, not an active-v4 owner
quantifier: every source satisfying SOURCE_CONTRACT.md and the theorem's stated interval and carrier conditions
projection_and_unit: distinct original finite affine slopes, counted once
claimed_bound: 268724670028139326 for bounded-flat sources on 23000..169999; other scopes below
status: PROVED
impact: LOCAL_ONLY
falsifier: a contract source satisfying a stated carrier condition and exceeding its printed slope bound
replay: python3 -B experimental/notes/low-core-flat-source-cumulative-20260908/replay.py
~~~

Agent: Codex acting for AllenGrahamHart, 2026-09-08. Complete local hand
proofs submitted for independent review, not a claim of external acceptance.
This grouped companion extends [the previous snapshot](../low-core-multiplicity-cumulative-20260908/README.md)
without altering it or Hughes's #1175 branch.

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
| Every j-flat has <=j*h nonzero original evaluations, h<=floor((J-1)/10) | 23000..169999 | 268724670028139326 |

The reserves are respectively 1306592303127376 and 6256058083255761.
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

1. A j-dimensional dual subspace, 1<=j<=10, containing at least
   j*floor((J-1)/10)+1 nonzero original evaluations.
2. For every extension of constants k/F and nonconstant rho in k(X),
   dim_k{v in V_k: rho*v in V_k}<=9.

The second restriction uses an elementary dimension-ten classification
into the paid progression class. These are proved restrictions on the
remaining source, not new speculative premises or a claim that it is paid.

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
The manifest freezes 231 source files: 212 inherited unchanged and 19 new.
The replay runs 60 checks with a 15-second child timeout and rejects four
manifest mutations. No external dependencies or large computation are needed.

The higher-J classes have ESSENTIAL structural hypotheses; general
every-carrier coverage still ends at 9940. Normalized concentrated sources,
higher original ranks, exhaustive original-source/near transport and
active-v4 ownership/inherited charges remain open. No compiler atom,
unrestricted adjacent endpoint, ordinary LIST bound or prize closes.

## Compute Requests

None. The next mathematical step is to price the forced occupied flat
with its actual polynomial carrier kernel, retaining original labels and
one accounting resource. These proved restrictions alone do not do that.
