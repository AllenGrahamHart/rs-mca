# K3 / DIRECT: Rational-Plane Bounds And Actual-Span-Three Terminals

```yaml
workboard_item: K3
row: KoalaBear, q=2130706433^6, n=2097152, k=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: Bound declared regular rank19 terminal classes and force full actual span in an excessive terminal.
architecture: DIRECT
partition_digest: not applicable to DIRECT
atom_or_cell: Original-error-rank12 source class, not an active-v4 atom
quantifier: Every such source in J9965..21499 and every valid original assignment; terminal bounds after the proved large-pencil source alternatives are removed.
projection_and_unit: Original distinct finite bad slopes; terminal weights sum original assigned raw defects.
claimed_bound: Available-weight test maximum 272127061148955779; not an unrestricted source upper bound.
status: PROVED LOCAL; independent mathematical review due
impact: LOCAL_ONLY
falsifier: A valid source/terminal violating a printed bound, ownership rule or geometric implication.
replay: python3 -B experimental/notes/kb-regular-terminal-actual-span-20260910/replay.py
```

This grouped four-node extension follows the
[regular operator reduction](../kb-raw-two-regular-operator-frontier-20260910/README.md)
at `ae6fbacd96826d9a273cdd2fbbfb90cb1a411ced`. It continues Scott Hughes's
source-bound weighted-anchor and compression methods in #1179/#1180.
No third-party branch, stable paper or earlier frozen proof is changed.

## Mathematical Contribution

The original error-rank12 residual has
`(n,K,m)=(1048576+J,J,67472+J)`, with an 11-dimensional shared carrier.
Actual raw-two pair rank19 admits eight regularity-preserving anchors and
a regular pair/shared enclosure of dimensions3/3. This pair rank is NOT
the original error rank.

1. **Rational compression with original ownership.** For a primitive row
   of height h, complete quotient-fibre unions overlap only on one root
   set of degree at most J+h-1. Their positive shifted masses share
   `sum x_c <= 1048577-h`. An inside defect forces the same original
   label at its coordinate across ALL fibres, so the global inside charge
   is at most the union size, or t for constant direction. A nonconstant
   rank-one plane in a shared three-space has the quadratic-product normal
   form, giving `2h <= J-9` after eight anchors.
2. **Affordable rational-plane terminals throughout the gap.** Every
   function-field-rank-two enclosure containing a rank-one plane satisfies
   explicit rational bounds L_1(J), L_2(J) on original raw weights.
   Thirteen J profiles, degree-adapted original pencil gates and scalar
   dimension-two LIST bounds cover the full interval.
3. **Proper actual spans and a whole-constant prefix are also bounded.**
   Every actual terminal family of affine span at most two fits the SAME
   allowances throughout J9965..21499. This includes nonconstant pencil
   planes by item2, not by incorrectly treating them as constant.
   Whole constant-direction three-dimensional enclosures fit the same
   allowances on J9965..14964, a prefix of 5,000 degrees.
4. **An exceptional-fibre guard for the remaining geometry.** Over
   characteristic zero or p>7, set v=X^3-X, w=Xv, U=span(1,v,w), with T
   cycling this basis. W={(f,Tf)} is regular and contains no rank-one
   plane. Its kernel-direction map is generically one-to-one but has
   the exact three-point fibre {-1,0,1}. Generic fibre size cannot
   substitute for a uniform joint-intersection bound. This is NOT
   an official large-agreement MCA source or a Prize counterexample.

The inherited available-weight test is

```text
floor(W(J)/3 + A_1*L_1(J)/2 + A_2*L_2(J)/6) + 134944
    <= 272127061148955779
B*   = 274980728111395087
reserve = 2853666962439308
A_t = product_(j=1)^8 (1048576+j)/(67472-t+j)
```

W(J) is the pinned original truncated-raw resource. Neither W nor original
weights are recomputed on auxiliary sections. The bounds apply to the
declared terminal classes only; there is no exhaustive terminal cover.

## Precise Remaining Obstruction

If an original rank19 source is over budget, at least one cutoff t=1,2
and retained anchor path has terminal weight greater than its L_t(J).
That excessive terminal must have ACTUAL affine span three:

| Original degree J | Possible excessive terminal enclosure |
| --- | --- |
| 9965..14964 | Function-field rank two with no rank-one plane |
| 14965..21499 | The same pencil-free class, or whole constant direction |

This does not assert that every terminal is excessive, or that every
terminal of a source belongs to one of these unpriced classes.
It does not close rank19, any whole J value, pair ranks20..22, original
error ranks>=13, an active-v4 atom, an ordinary-LIST row or either Prize.

## Review And Replay

- [Generic rational-compression proof](source/background/nodes/mca_rational_compression_fibre_weight/proof.md).
- [Finite rational-plane proof](source/background/nodes/rate_half_mca_regular_rational_plane_terminal_bounds/proof.md).
- [Actual-span proof](source/background/nodes/rate_half_mca_regular_terminal_actual_span_frontier/proof.md) and [constant prefix](source/background/nodes/rate_half_mca_regular_terminal_actual_span_frontier/constant_prefix.md).
- [Exceptional-fibre construction](source/background/nodes/pair_space_regular_kernel_multiple_fibre/proof.md).
- [Integration and attribution](INTEGRATION.md), [validation limits](VALIDATION.md),
  [source/dependency manifest](SOURCE_MANIFEST.json).

```sh
python3 -B experimental/notes/kb-regular-terminal-actual-span-20260910/replay.py
python3 -B -O experimental/notes/kb-regular-terminal-actual-span-20260910/replay.py
```

The packet freezes 56 new source files (1,122,842 bytes), a 111-node
locally PROVED required closure and 325 unchanged inherited proof documents.
Replay is offline and serial. Exact arithmetic checks are not a substitute
for independent review of the universal geometry and ownership proofs.
Historical node-local provenance records retain their original local status.

## Compute Requests

None. No Modal use, spending or large experiment. The next missing input
is a source-bound census for full actual-span-three pencil-free terminals,
and whole-constant terminals on the upper tail. Existing unrelated compute
requests are not authorized by this publication.
