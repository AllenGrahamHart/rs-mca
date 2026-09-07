# KoalaBear residual geometry: jets, cubic bounds and one remaining family

```yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: for every printed normalized source on 7117..8655, N<=255637082913634099 OR all but <=65 LOW pairs have the affine-singular cubic normal form below
architecture: DIRECT
atom_or_cell: normalized rank-twelve source, not an active-v4 owner
quantifier: uniform over every source satisfying SOURCE_CONTRACT.md
projection_and_unit: N=number of selected distinct finite slopes + 134944; exceptions counted as polynomial pairs
claimed_bound: 255637082913634099 on the paid alternative; remaining alternative UNPAID
status: PROVED
impact: LOCAL_ONLY
falsifier: a contracted source violating both alternatives, or a coefficient family violating a printed dimension bound
replay: python3 -B experimental/notes/low-core-cubic-20260907/replay.py
```

This grouped companion continues [PR #1175](https://github.com/przchojecki/rs-mca/pull/1175).
It does not change Scott Hughes's branch, a live compiler atom or an official
endpoint. The earlier [conic/4801..7116 packet](../low-core-algebraic-20260907/README.md)
is preserved unchanged. These are local analytic proofs submitted for
independent external hand review, not accepted upstream theorems.

## Main reduction

Read the [source contract](SOURCE_CONTRACT.md) first. Fix the canonical
normalized source `(n,K,m)=(1048576+J,J,67472+J)`, actual common carrier
dimension eleven, empty universal carrier core, and `T=500`. Preserve the
complete minimizing pair cores and distinct original finite slope labels.

On **7117<=J<=8655**, the [full-kernel dichotomy](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/cubic_obstruction.md)
proves either

```text
N = |Gamma|+134944 <=255637082913634099,
reserve              19343645197760988,
```

or all but at most 64 LOW pairs lie on one geometrically integral cubic
with an affine singular point and exactly one normalization point above
infinity. The [explicit normal form](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/affine_singular_normal_form.md)
then gives, for all but at most **65** LOW pairs,

```text
f(tau) = f_s + (tau^2-lambda)*(P+tau*Q),
f_s in F(X)^2, lambda in F(X), P,Q in F(X)^2 independent,
tau in F(X), tau^2 != lambda.
```

The extra possible pair is the singular point itself. The original pairs
remain polynomials of degree <J in the same carrier. The parameter and
normal-form coefficients can be rational: no degree-<J assertion about
tau, pole deletion or square-root field extension is used.

**This remaining family is not paid.** The dichotomy is not a closure of
7117..8655 and is not a counterexample. The overall unpaid normalized
range remains 7117..169999, with higher original ranks also open.

## Reusable theorems

| Result | Proof and finite consequence |
|---|---|
| Projective jets | [Proof](source/critical/nodes/mca_polynomial_map_projective_jet_dimension/proof.md): characteristic zero or p>=K gives dimension <=ceil(s/e) for bounded polynomial parameters mapped into one s-dimensional output carrier. Actual graph degrees 2..9 give N<=140379757249624860. |
| Coupled moving projection | [Proof](source/critical/nodes/mca_polynomial_map_projective_jet_dimension/moving_projection_graphs.md): for A*Phi+B*Psi=Z, put d=dim ker(A,B) on VxV, r=ceil(d/e), N_input=2s-d. Degree charge e^(N_input-r) and actual input degree K+h are retained together. Cubic height h<=51391 gives whole-source bound 265092257458790508. |
| Smooth projective cubic | [Section-dimension proof](source/critical/nodes/elliptic_curve_bounded_polynomial_section_dimension/proof.md), [original-coordinate count](source/critical/nodes/mca_low_core_smooth_cubic_payment/proof.md): coefficient dimension <=1, and zero when j is nonconstant. Whole-source bounds 205228871902226632 and 76846974125034288 respectively. |
| Normalization unit | [Proof](source/critical/nodes/mca_normalization_unit_curve_payment/proof.md): a nonconstant unit on the affine normalization bounds coefficient dimension by one. This pays rational-normalization cubics with at least two boundary points, including singular examples outside the earlier product/graph classes. |

All finite whole-source bounds in this table use the contract on
4801..169999 and one resource/near charge. They are **alternative source
classes**, not additive row atoms. The smooth/unit cubic group gain is
159185671413625180; arbitrary mixtures must still pay every group.

## Why the residual is smaller

The entire pair-degree-eight interpolation kernel has gcd of pair-degree
at most three, since `D_8-n-D_mult4=960724-111J>0` on this strip.
Bezout leaves <=64 pairs off it. An asymmetric ordinary Johnson split
bounds every populated constant-direction line by 132 pairs unless the
whole source already pays. All remaining line/conic combinations, smooth
cubics and rational multi-boundary cubics have explicit prices.

A one-boundary cubic singular at infinity is a polynomial graph in a
linear projection. The primitive kernel equation forces projection height
<=17580; the coupled theorem pays its group by 71875471818343284. What
survives is therefore the affine-singular (2,3) family above, not an
arbitrary cubic or an assumed unproved classification.

## Review, integration and replay

[PROVENANCE.md](PROVENANCE.md) gives the dependency graph, attribution,
upstream pins and overlap audit. [AUDIT.md](AUDIT.md) lists the review
guards. Supporting analytic sources and standard-library checkers are
vendored as a bounded snapshot, pinned by `SOURCE_MANIFEST.json`; this is
not a complete copy of the local DAG. Only the claims selected here and
their proof dependencies are offered for integration. Historical parent
dossiers may also describe other local results outside this submission.

```bash
python3 -B experimental/notes/low-core-cubic-20260907/replay.py
python3 -O -B experimental/notes/low-core-cubic-20260907/replay.py
```

Checks run serially, with a 15-second timeout each and assertion-enabled
children even under an optimized wrapper. They verify arithmetic and
controls, not the universal geometry proofs. No Sage, CAS, Lean, TeX build,
finite-field scan or large matrix is required or claimed.

Original-row use still needs the actual normalization and original-near
transport. Active-v4 use additionally needs exhaustive first-match
ownership and inherited charges. No unrestricted ordinary LIST bound,
adjacent-safe row, original red closure or prize resolution follows.

## Compute requests

None. This is an analytic contribution with tiny serial checks; no Modal
run or spending is requested.
