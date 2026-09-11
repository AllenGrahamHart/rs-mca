# K3 / DIRECT: Constant-Hyperplane Original-Source Payment

```yaml
workboard_item: K3
row: KoalaBear, q=2130706433^6, n=2097152, k=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
architecture: DIRECT
partition_digest: DIRECT
atom_or_cell: DIRECT intrinsic original-source class, not a v4 atom
quantifier: uniform over valid original assignments in the printed source class
projection_and_unit: distinct original finite affine bad slopes on one received line
direct_statement: constant10/no11 generic-regular P2-rank19 sources have at most 270000000000000000 bad slopes
claimed_bound: 270000000000000000
status: PROVED locally; independent mathematical review due
impact: LOCAL_ONLY, with exhaustive coverage of the declared source class
falsifier: a valid original source in the stated class above the claimed bound, or a failure of the weighted degree-descent inequality
replay: python3 -B experimental/notes/kb-constant-hyperplane-source-payment-20260911/replay.py
```

One grouped extension of published commit
d8ab3ac67f71bd95fbc698543d38a2305d3045de. Four new proved nodes,
71 frozen source files, and a133-node acyclic locally PROVED required closure.
[Integration and review order](INTEGRATION.md).
[Validation and limitations](VALIDATION.md).

## Source Theorem

Fix an original complete post-near error-rank12 source with shared carrier
dimension11, normalized degree J9965..21499, actual raw-at-most-two pair
affine rank19, and full generic scalar projection. Let W be its19-dimensional
pair-direction hull inside V squared, with dim V=11.

If W contains a constant-direction10-dimensional subspace but no
constant-direction11-dimensional subspace, its ENTIRE original bad-slope
set has cardinality at most

    270000000000000000 < 274980728111395087.

This covers every normalization degree and original owner assignment in
the class. Actual pairs need not fill the formal pencil.
The exact residual-branch maximum is266908096047530929 over13 J profiles.
The earlier proved whole-source pencil alternatives have caps at most
270000000000000000 and combine by MAXIMUM, never addition.

Combining the preceding nonconstant10-pencil source theorem, every such
source whose maximum dimension of a function-field-rank-one F-linear
subspace of W is exactly10 has bound

    272127061148955779, reserve2853666962439308.

An excessive original regular rank19 source therefore has maximum pencil
dimension8 or9, OR a full constant11 subspace. The lower bound8 follows
from rank-nullity of W19 to V11. No ORIGINAL-FIELD projective scalar
projection of such an excessive hull can have rank9: its kernel would
be a maximal constant10 pencil, and a different constant11 cannot coexist
inside dimension19. The direction at infinity is included; no coefficient
field extension is made.

## Mechanism

For a regular prefix with shared dimension s and pair dimension2s-3,
a maximal constant(s-1) pencil has primitive scalar degree E. At nonroot
anchors it stays maximal and its primitive degree drops by at least one.
At its at most D-E common-root coordinates, the child instead has a full
constant carrier of primitive degree E. Full constant carriers persist
under further regular anchors.

Degree-refined same-field scalar LIST bounds price those children.
Write zeta=E-(s-2). Its nonroot child value cannot increase, while on a
band[lo,hi] the exceptional-coordinate count is at most J1-10-lo.
Normalize by the ORIGINAL remaining anchor factor

    A_s,t = product_(ell=1)^(s-3) (1048576+ell)/(67472-t+ell).

Prefix maxima over lower degree bands give a proved eight-stage recurrence,
not an assumed random transition. The original source resource is

    floor(W_raw/3 + M_1/2 + M_2/6) + 134944.

Original raw labels, full gcds, unused degree, owners, higher raw and near
are retained. Both cutoffs use the same P2 enclosure even when the actual
P1 family does not span it.

A companion theorem pays every seven-anchor5/4 enclosure with constant3
but no constant4 at the original eighth-anchor allowance, with no
normalization cap. Its26 exact prices use48 whole degree bands and5238
scalar LIST steps. Root exceptions share E; their individual terminal
prices need not be affordable.

## Boundaries

The local gates require the residual source AFTER already-paid whole-source
pencil alternatives are removed. Sources in those alternatives are separately
paid and combined by maximum, so this is not a new avoidance conjecture.

Some intermediate prices in the new ORIGINAL-source recurrence exceed the
older local L_t allowance. The original resource funds them. This theorem
does NOT pay all constant4 penultimate enclosures or all whole-constant3
upper-tail terminals individually.

No unrestricted rank19, pair rank20..22, whole J, higher original error
rank, active-v4 atom, ordinary LIST row, adjacent endpoint, or Prize closes.
The claimed source-class bound is not an all-row upper bound.

## Replay

```sh
python3 -B experimental/notes/kb-constant-hyperplane-source-payment-20260911/replay.py
python3 -B -O experimental/notes/kb-constant-hyperplane-source-payment-20260911/replay.py
```

Six new and four inherited focused checks pass from temporary frozen-source
trees in4.75/5.56seconds,40892/41236KiB peak RSS. The independent source
checker audits218 degree bands and119988 legal scalar LIST transitions.
New arithmetic rejects41+40 semantic mutations; the wrapper rejects57
malformed manifests and checks1579 listed source hashes.
Small algebraic controls are not official large-agreement source witnesses.

Manifest SHA256:
68d245f2a6c2dd34674e847865a7da21d3338c68f0355b66d132e1f7769a5f47.

## Compute Requests

None for this contribution. No Modal, spending, field enumeration, or large
search was needed. Replay is serial and was run under a256MiB address-space
cap and60second wall limit. Written proofs still require external review.
