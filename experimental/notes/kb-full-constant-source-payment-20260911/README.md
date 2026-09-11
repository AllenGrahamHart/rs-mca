# K3 / DIRECT: Full-Constant Original-Source Payment

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
direct_statement: full constant11 P2-rank19 sources have at most 270000000000000000 bad slopes
claimed_bound: 270000000000000000
status: PROVED locally; independent mathematical review due
impact: LOCAL_ONLY, with exhaustive coverage of the declared source class
falsifier: a valid original source above the claimed bound, or failure of the all-coordinate weighted recurrence
replay: python3 -B experimental/notes/kb-full-constant-source-payment-20260911/replay.py
```

One grouped extension of published commit
9955a726beca0598838d6b500c3cc58c0b48c785. Two new proved nodes,
34 frozen source files, and a 135-node acyclic locally PROVED required closure.
[Integration and review order](INTEGRATION.md).
[Validation and limitations](VALIDATION.md).

## Source Theorem

Fix an original complete post-near error-rank12 source with shared carrier
dimension 11, normalized degree J in [9965,21499], and actual raw-at-most-two
pair affine rank 19. Write W for its pair-direction hull in V squared.

If W contains a constant-direction 11-dimensional subspace, its ENTIRE
original bad-slope set has cardinality at most

    270000000000000000 < 274980728111395087.

The statement includes every normalization degree and valid original owner
assignment in the class. It does not require actual pairs to fill a formal
pencil. The exact residual-branch maximum is 239161133377346211 over the
13 whole J profiles. Earlier proved whole-source pencil alternatives have
caps at most 270000000000000000 and combine by MAXIMUM, never addition.

Together with the preceding maximum-pencil-dimension10 theorem, every such
source whose maximum dimension of a function-field-rank-one F-linear
subspace of W is at least 10 has bound

    272127061148955779, reserve 2853666962439308.

An excessive original rank19 source therefore has maximum pencil dimension
8 or 9. Every ORIGINAL-FIELD projective scalar projection of its hull has
rank 10 or 11; at most three finite directions have rank 10. The former full
constant11 alternative is paid, not replaced by a conditional premise.

## Mechanism

A fixed change of basis of the two pair components puts the hull in the form

    W = (V,0) + (0,B), B subset V, dim V = 11, dim B = 8.

The change of basis does not reparameterize original finite slope labels.
In state (s,c), put dim V=s, dim B=s-c and kappa=D-(s-1), where D is the
primitive shared degree. Every remaining coordinate is retained:

- At a nonroot of B, joint evaluation has rank two; the child is (s-1,c).
- At a root of B, joint evaluation has rank one; the child is (s-1,c-1).

There are at most kappa+c root coordinates. Full shared gcd division makes
kappa nonincreasing in both cases. If C and F bound the original child raw
weights, incidence gives

    A * Omega <= N*C + (kappa+c)*max(F-C,0),
    N = R+s+kappa+v, A = d+s+kappa-t+v, v >= 0.

For fixed child bounds, the ratio is bounded by the two kappa-band endpoints
at v=0 and its limit C as v grows. Lower-degree prefix maxima cover all
possible extra gcd degree drops. At c=0 the root branch is absent.

The 42-state table has four terminals and 38 recurrences. Whole-constant
scalar terminals use same-field LIST bounds on their OWN original core-union
complements and one globally preferred finite-slope charge. The zero-dimensional
terminal contains at most one original pair, with raw weight at most 981104+t.

Both cutoffs use the same original P2 enclosure. The final source resource is

    floor(W_raw/3 + M_1/2 + M_2/6) + 134944.

All anchor factors are already in M_1 and M_2. Original owners, raw weights,
full gcds, unused degree, higher raw and near remain once.

## Boundaries

The local constant-pencil gates apply AFTER already-paid whole-source
alternatives are removed. Those alternatives are separately paid and included
by maximum; this is not an avoidance conjecture.

This theorem pays an ORIGINAL source class. It does not make every isolated
whole-constant terminal affordable. It assumes neither a rank-two drop at
every anchor nor generic regularity of every rank-two child.

No unrestricted rank19, pair rank20..22, whole J, higher original error rank,
active-v4 atom, ordinary LIST row, adjacent endpoint or Prize closes.
Newer all-coordinate NON-product drafts are excluded from this packet.

## Replay

```sh
python3 -B experimental/notes/kb-full-constant-source-payment-20260911/replay.py
python3 -B -O experimental/notes/kb-full-constant-source-payment-20260911/replay.py
```

The replay checks all 424 degree bands, 93384 scalar LIST transitions and
16112 recurrence identities, plus two inherited focused audits. The new
independent arithmetic rejects 45 semantic mutations, including a fully
repriced omission of rank-one roots. The wrapper rejects 61 malformed
manifests and checks 1613 listed source hashes and 439 inherited proof documents.
Small algebraic controls are not official large-agreement source witnesses.
See [measured replay and audit limits](VALIDATION.md).

Source manifest SHA256:

    a1a442d4083a1d8ce7eedd6d424e4a7abff48a0257d1e2f09b338b923107428b

## Compute Requests

None. No Modal, spending, large field census or new search was needed.
Replays are serial, offline and bounded locally by 256 MiB address space and
60 seconds wall time. Written proofs still require external review.
