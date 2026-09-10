# K3 / DIRECT: Pay Actual Pair Rank Eighteen

**Review status:** six locally PROVED nodes with complete printed required
proofs and exact arithmetic certificates. Independent mathematical review
remains due. This extends the minimum-envelope packet at `457bbc73` and
the source-bound methods of Scott Hughes's unmerged #1179/#1180.

## Result And Scope

Row: KoalaBear MCA, field `q=2130706433^6`, original code length `2097152`,
dimension `1048576`, agreement `1116048`, target `2^-128`, integer budget
`B*=274980728111395087`. Units: distinct original finite bad slopes on one
received line, not pairs, scalar codewords, or a sum of independent sources.

For **every original error-rank-twelve source** in the remaining normalized
degree interval `9965 <= J <= 21499`, and **any valid original assignment**
of supports and minimizing pairs, let `P2` be the ACTUAL pairs assigned at
least one original label with raw defect at most two. Then

```text
dim aff(P2) <= 18, including the empty family
    => entire original bad-slope count <= 274462040894062110
    < B*, with reserve 518687217332977.
```

The bound retains every higher-raw label and adds `near=134944` once.
It needs no sparse-only or proper-scalar-span premise. In particular,
full actual scalar-span-five compression terminals are now included.
Auxiliary pair rank eighteen is NOT original error rank eighteen.

| Normalized degree J | Whole-source bound for actual P2 rank <= 18 |
| --- | ---: |
| 9965..12964 | 274462040894062110 |
| 12965..14164 | 270702759681887570 |
| 14165..21499 | 273715780528023745 |

These are alternative whole-source bounds and combine by MAXIMUM, not
addition. Actual P2 rank at most seventeen also has the stronger uniform
bound `270000000000000000`.

## What Closes The Compression Case

Six source-preserving anchors leave pair/shared dimensions `6/5`.
Occupied compression fibres have INTEGER shifted core masses
`x_c=|C_c|-J+1`, with `sum x_c <= S=1048577`. Thus at most two have
`x_c >= 349526`, since `3*349526=1048578>S`.

A small-fibre linear bound and a large-fibre affine bound give

```text
w_t(x) <= alpha*x          for x <= 349525
w_t(x) <= alpha*x + beta   for x >= 349526
total original raw weight <= t + alpha*S + 2*beta.
```

The preferred finite slope costs `t` ONCE across all fibres. The same
mass budget `S` is used once. Keeping the actual degree ranges before
applying the scalar LIST bound is enough to pay compression. The new
cap fits under the earlier sparse numerical cap on the prefix; a uniform
middle cap and the inherited upper interval complete the result.

## Proof Entry Points

- [Final payment](source/background/nodes/rate_half_mca_integer_compression_rank_eighteen_payment/proof.md)
  and [integer envelopes](source/background/nodes/rate_half_mca_integer_compression_rank_eighteen_payment/integer_envelopes.md).
- [Integer fibre-count lemma](source/background/nodes/mca_compression_fibre_integer_envelope/proof.md).
- [Shared compression mass](source/background/nodes/mca_compression_fibre_raw_mass/proof.md)
  and [original weighted pencil ownership](source/background/nodes/mca_weighted_pencil_raw_mass/proof.md).
- [Pluecker classification](source/background/nodes/mca_shared_carrier_pluecker_dichotomy/proof.md)
  and [coupled sparse/upper-interval payment](source/background/nodes/rate_half_mca_coupled_pair_rank_frontier/proof.md).
- [Integration and review map](INTEGRATION.md), [validation and limits](VALIDATION.md),
  and [complete source/dependency manifest](SOURCE_MANIFEST.json).

Run offline from the repository root:

```sh
python3 -B experimental/notes/kb-source-bound-integer-compression-rank18-20260910/replay.py
python3 -B -O experimental/notes/kb-source-bound-integer-compression-rank18-20260910/replay.py
```

The replay is serial, standard-library only, with small temporary copies
and no dependency on the live research tree. Use a memory/time guard on
constrained machines. No Modal, paid computation, or compute request.

## Remaining Frontier

Every over-budget assignment in this original-rank-twelve gap must have
actual P2 rank `19..22`. Generic fullness of P2 is NOT proved. Higher
pair ranks, original error ranks at least thirteen, complete degree
coverage, and both unrestricted Prize problems remain open. No active-v4
`U_paid`, Q, BC, row certificate, or maximal-safe endpoint is supplied.

The earlier four-node certificates remain frozen at their old scopes;
their coarse all-J full-rank-eighteen upper bound above budget is not a
counterexample. The final payment uses the stronger integer envelope.
Historical source-local notes saying LOCAL describe their creation state;
this packet freezes those proofs for review, not prior external acceptance.
