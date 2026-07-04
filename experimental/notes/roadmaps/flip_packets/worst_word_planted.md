# Flip packet: worst_word_planted

- **Node:** `worst_word_planted`
- **Current critical label:** UNPROVED
- **Verdict:** DEFECT
- **Referee summary:** the revised node correctly records the E15 falsifier,
  but its live req set does not match the revised statement. The statement
  now needs challenger-class pricing/exhaustion in addition to the `imgfib`
  safe-side input.

## Statement

> REVISED per the E15 COUNTEREXAMPLE (#197): the naive planted-only form is FALSE — a structured low-slack NON-planted challenger exists at sigma = 1 in the toy cell. Revised statement: at the crossing radii the sup-over-words list is attained by the planted sunflower family OR the E15 structured challenger class, and list_planted_arithmetic must price BOTH classes exactly. The challenger is structured (not a fifth-mechanism signal); the endgame arithmetic gains one classified column.

## Req Children

| child | live status | critical label | role |
|---|---:|---:|---|
| `imgfib` | CONJECTURE | UNPROVED | Safe-side image-fiber bound; prevents unpriced extras once the candidate worst classes are known. |

The statement also names `list_planted_arithmetic`, but that node is not wired
as a req child. It says:

> planted_count(delta) is an explicit combinatorial formula (core/petal choices x scalar factors). Under worst_word_planted + imgfib + integrality, the list crossing is decided by EXACT arithmetic: windows [planted_count - margin, planted_count) in eps*|F|-space, the census/dodge structure transferring verbatim from the MCA side — with NO zone-(b) analogue (no value sets mod p; counts are explicit).

The revised statement further needs the E15 challenger-class arithmetic
(`QL.5` in `execution_queue.md`) or an equivalent node.

## Referee Argument

This packet cannot recommend `PROMOTE-CONDITIONAL` from the live child set.
Granting `imgfib` only bounds extras after the modeled worst classes are fixed;
it does not prove that the supremum is attained by planted or E15-structured
families, and it does not price the E15 column. The statement itself says
`list_planted_arithmetic` must price both planted and E15 classes, but that
dependency is prose-only.

The right repair is precise:

1. Wire `list_planted_arithmetic` as a req child after it is revised to include
   the E15 challenger column, or add a separate `challenger_class_arithmetic`
   child.
2. Add an exhaustion/classification child for "planted or E15 structured" if
   the roadmap lane wants the extremality assertion separated from the pricing
   arithmetic.

Until then the node is not a clean mathematical red theorem and not an amber
assembly implication; it is a wiring defect caused by the E15 repair.

## Evidence Pins

- `worst_word_planted`: `260596841634e691`
- `imgfib`: `0701cb2b6f534e11`
- `list_planted_arithmetic`: `981bbfa57a032011`

## Source Quotes

- `campaign_report_02_falsification_ledger.md` records the E15 falsifier and
  the repair: planted-family OR E15 structured challenger class.
- `execution_queue.md` names `QL.5 [challenger-class arithmetic]`: price the
  E15 structured challenger class alongside planted counts in
  `list_planted_arithmetic`.
