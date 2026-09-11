# K3 / DIRECT: Actual Collision Interpolation And Low Image Degree

```yaml
workboard_item: K3
row: KoalaBear, q=2130706433^6, n=2097152, k=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: High-image-degree pencil-free regular3 terminals fit the inherited raw1/2 allowances; excess has image degree 2..10.
architecture: DIRECT
partition_digest: not applicable to DIRECT
atom_or_cell: Original-error-rank12 source class, not an active-v4 atom
quantifier: Every such source in J9965..21499 and every valid original assignment, after the proved original large-pencil source alternatives are removed.
projection_and_unit: Original distinct finite bad slopes; terminal weights sum original assigned raw defects.
claimed_bound: 52 image-degree gates and 104 exact incidence inequalities; uniform image thresholds (9,10,11,11).
status: PROVED LOCAL; independent mathematical review due
impact: LOCAL_ONLY
falsifier: A source-valid violation of the printed incidence, actual-pair ownership, product-rank or terminal-weight inequality.
replay: python3 -B experimental/notes/kb-regular-terminal-collision-interpolation-20260911/replay.py
```

This grouped four-node extension follows the
[spectral-mask packet](../kb-regular-terminal-rich-core-fibres-20260911/README.md)
at `f328d9fb39991cfa699216c826014c3dfd2c0ee1`. It continues the
source-bound weighted-anchor program discussed in #1179/#1180.
It supplies an aggregate collision bound, not just a new maximum-fibre gate.

## Scope And Coordinates

An original error-rank12 residual has
`(n,K,m)=(1048576+J,J,67472+J)` and shared carrier dimension11.
For actual raw-two pair rank19, eight regular anchors leave a dimension3
operator enclosure. Pair rank19 is NOT the original error rank.
After the fixed invertible pair-coordinate change its directions are
`(y,T(y))`, for an original-field endomorphism T.

Remove the full polynomial gcd G of the auxiliary shared carrier U0.
Set `kappa=1+actual max degree(U0/G)`. If z counts distinct nonanchor
domain roots of G, retain `v=J-8-kappa-z>=0`. All polynomial-degree slack,
repeated roots and nondomain gcd roots are included. The resulting domain
and core lower bound are `N_v=1048576+kappa+v` and
`A_v=67472+kappa-t+v`. Original one-pair weight remains
`C_t=1048576-67472+t`, for the original raw cutoff t=1 or2.

## What Is Proved

1. **Aggregate eigen-root incidence.** Hereditary actual eigenline and
   affine-plane capacities q1,q2 give a root-incidence charge at most
   `(kappa-1)*(0,q2,q2+q1,3*q2/2)_e`, for e=0,1,2,3 distinct eigenvalues
   in the ORIGINAL field. Repeated and nonsplit cases are retained.
   The improved whole-gap sufficient intersection caps are
   `2108/1985/1948/1866`. Primitive degree `kappa<=H_e+2` is automatically
   affordable; excess forces large actual shared-core mass.
2. **Actual-pair-owned interpolation.** Select exactly
   `M=floor(L_t/C_t)+1` actual pairs. At each nonzero projective evaluation
   point p outside the eigen-root mask, select a coordinate with maximal
   agreeing group size r_p. Any pair in that group uniquely determines p,
   so different groups consume disjoint unordered pairs:
   `C=sum_p binom(r_p,2)<=binom(M,2)`.
   A degree-ell form vanishing to order r_p-1 costs at most C conditions.
   If the PRODUCT RANK exceeds C, it has a nonzero pullback and gives
   `M*A_v<=B+N_v+(kappa-1)*ell`.
3. **Exact image rank and finite payment.** If eta is the degree of the
   primitive equation of the plane image, the product rank is exactly
   `H_eta(ell)=binom(ell+2,2)-binom(ell-eta+2,2)`, with the second term
   zero for ell<eta. The finite certificate proves the strict reverse of
   the preceding incidence bound at kappa=J1-8,v=0; the written monotonicity
   argument covers EVERY primitive degree and v>=0 in each profile.
   Thus all pencil-free terminals with eta>=11 fit the SAME L_1,L_2.
4. **Constraint on the surviving class.** Every first-unaffordable M-subset
   of an excessive low-image terminal must have `C>=H_eta(ell)`.
   For the last three-eigenvalue profile, eta=10 would require at least
   1465 of1596 unordered pairs in the chosen actual collision groups.
   This is actual collision mass, not the number of possible directions.

The stronger uniform image thresholds by e=0,1,2,3 are **9/10/11/11**.
See the [image profile table](source/background/nodes/rate_half_mca_regular_terminal_low_image_degree_frontier/thresholds.md)
and [primitive-degree table](source/background/nodes/rate_half_mca_regular_terminal_eigen_capacity_frontier/thresholds.md).
These are sufficient gates, not claims of optimality.
Eta is not polynomial degree, map multiplicity, pencil height or shift-pair h.

## What Remains Open

An over-budget rank19 source must expose an excessive cutoff/path with
actual span3. Its pencil-free branch now has image degree **2..10**,
with sharper profile-specific limits. Those low-degree cases are NOT paid.
Whole constant-direction dimension3 on J14965..21499 remains separate.

The inherited available-weight test maximum `272127061148955779`,
reserve `2853666962439308`, is unchanged and is **NOT an unrestricted
rank19 source bound**. Higher raw resources and near134944 are retained once.
No whole J, rank19, pair ranks20..22, higher source rank, active-v4 atom,
ordinary-LIST row or Prize problem closes. No endpoint moves.

## Review And Replay

Start with [INTEGRATION.md](INTEGRATION.md), then the four linked proofs.
[VALIDATION.md](VALIDATION.md) distinguishes exact arithmetic checks from
the universal geometry still requiring external review.
[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) pins59 new source files,
the116-node locally PROVED required closure, and345 inherited proof documents.

```sh
python3 -B experimental/notes/kb-regular-terminal-collision-interpolation-20260911/replay.py
python3 -B -O experimental/notes/kb-regular-terminal-collision-interpolation-20260911/replay.py
```

Python standard library only; serial, offline, no field census or Modal.
The source tree is reconstructed temporarily from pinned packet files,
not imported from the author's mutable research worktree.
