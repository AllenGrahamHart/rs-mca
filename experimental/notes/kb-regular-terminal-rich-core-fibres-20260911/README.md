# K3 / DIRECT: Spectral Masks And Actual Shared-Core Fibres

```yaml
workboard_item: K3
row: KoalaBear, q=2130706433^6, n=2097152, k=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: Small two-core intersections fit the regular3 terminal allowances; excess forces an actual rank9 shared-core flat.
architecture: DIRECT
partition_digest: not applicable to DIRECT
atom_or_cell: Original-error-rank12 source class, not an active-v4 atom
quantifier: Every such source in J9965..21499 and every valid original assignment, after the proved large-pencil source alternatives are removed.
projection_and_unit: Original distinct finite bad slopes; terminal weights sum original assigned raw defects.
claimed_bound: 52 spectral gates and 104 exact cutoff inequalities; uniform intersection caps (1913,1913,1022,169).
status: PROVED LOCAL; independent mathematical review due
impact: LOCAL_ONLY
falsifier: A valid source/terminal violating a printed inequality, root-mask hypothesis, ownership rule or actual-witness implication.
replay: python3 -B experimental/notes/kb-regular-terminal-rich-core-fibres-20260911/replay.py
```

This two-node extension follows the
[rational-plane and actual-span packet](../kb-regular-terminal-actual-span-20260910/README.md)
at `918324a10b1d8235e5d06418cbfdca83544d339c`. It continues the
source-bound weighted-anchor program discussed in #1179/#1180.
The new conclusion concerns ACTUAL shared cores, not an arbitrary large
fibre of an unoccupied parameter map.

## What Is Proved

An original error-rank12 residual has
`(n,K,m)=(1048576+J,J,67472+J)` and an 11-dimensional shared carrier.
For actual raw-two pair rank19, eight regular anchors leave a dimension3
operator enclosure. Pair rank19 is not the original error rank.

1. **A spectral-mask Johnson theorem.** In a pencil-free operator terminal,
   every original-field eigenspace has dimension at most one. Delete the
   anchors and the roots of one polynomial per original-field eigenvalue;
   if there are no eigenvalues, delete common carrier zeros instead.
   Eigenvector differences have no remaining common zeros. Other pair
   differences can share core coordinates in just one nonzero projective
   evaluation fibre. This gives an exact pair count from a bound on actual
   two-core intersections, without assuming joint evaluation rank two.
2. **An actual-source necessary witness.** Thirteen complete degree profiles
   and both original raw cutoffs fit the inherited allowances whenever
   those intersections are small. An excessive pencil-free terminal
   therefore supplies TWO actual represented pairs, with independent
   parameter differences sharing a large polynomial factor. Together with
   the eight anchors, their shared-core coordinates span an original
   evaluation flat of rank exactly nine.

For `e=0,1,2,3` distinct eigenvalues **in the original field**, the deleted
coordinate bounds are `b_e=J-3,J-1,2J-10,3J-19`. With
`n=1048576+J`, `A=67472+J-t`, the pair count is bounded by

```text
floor((n-b_e)*(A-b_e-H) / ((A-b_e)^2-(n-b_e)*H)).
```

The denominator must be positive. Multiply by the ORIGINAL one-pair weight
`1048576-67472+t`; auxiliary coordinate deletion does not reset any weight.
Whole-gap sufficient intersection caps are:

| Original-field spectral count e | 0 | 1 | 2 | 3 |
| --- | ---: | ---: | ---: | ---: |
| H | 1913 | 1913 | 1022 | 169 |

The [profile table](source/background/nodes/rate_half_mca_regular_terminal_rich_fibre_frontier/thresholds.md)
is stronger on individual intervals. Excess forces at least `H_e(J)+1`
shared-core coordinates outside the mask, not just a formal direction.
These are sufficient thresholds, not optimality claims about true sources.

## What Remains Open

For J9965..14964 an over-budget rank19 source must expose the pencil-free
rich-core case. On J14965..21499 a whole constant-direction dimension3
terminal remains possible too. Rich-core incidence mass is not yet bounded.

The inherited available-weight maximum `272127061148955779`, reserve
`2853666962439308`, is unchanged and NOT an unrestricted rank19 source bound.
Higher raw labels and the near contribution `134944` are retained once.
No whole degree, rank19, pair ranks20..22, active-v4 atom, ordinary-LIST row,
or Prize problem is closed. Newer unfinished research is not in this packet.

## Review And Replay

- [Generic proof](source/background/nodes/pair_space_operator_spectral_fibre_johnson/proof.md).
- [Finite proof](source/background/nodes/rate_half_mca_regular_terminal_rich_fibre_frontier/proof.md)
  and [actual source witness](source/background/nodes/rate_half_mca_regular_terminal_rich_fibre_frontier/source_witness.md).
- [Integration and attribution](INTEGRATION.md), [validation limits](VALIDATION.md),
  [source and dependency manifest](SOURCE_MANIFEST.json).

```sh
python3 -B experimental/notes/kb-regular-terminal-rich-core-fibres-20260911/replay.py
python3 -B -O experimental/notes/kb-regular-terminal-rich-core-fibres-20260911/replay.py
```

Replay is offline, serial, and uses only the Python standard library.
Both modes took under3seconds and29MiB measured peak RSS. No Modal use,
paid computation or new compute request. Independent proof review is due.
