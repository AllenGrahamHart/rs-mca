# Audit

## Cumulative low-margin continuation

The new cumulative_low_weights.md keeps all eleven positive factors and
uses M>=67483. Bernoulli gives a strict linear LOW bound at r<=500;
the logarithmic derivative remains positive through r=5500, after which
the truncated resource suffices. The nested-count identity uses one fixed
label set and raw selection. It adds no new tuple resource and does not
reuse the old /501 discount. The finite tail's primary and independent
verifiers check exact weight products and the integer cumulative identity.

The H used here is the in-support pair core of one actual minimizing b,
not an arbitrary guessed subset. When r<=d its size >=K guarantees
full evaluation rank s. A zero normal incident with S is universally
satisfied, so at most g such coordinates can lie in H.

Every counted tuple has exactly one coordinate outside H. This proves
both the s+1 insertion factor and absence of internal overcounting.
Across records, independent affine incidence equations determine at
most one parameter point, hence at most one slope. The old and new
counts are not disjoint, so their SUM would be wrong.

The alpha argument treats r<=s and r>=s+1 separately, including all
large margins; it is not an inference from a numerical small-margin
sample. The generic d>=s(s+1) gate is sufficient, not asserted necessary.

The small verifier checks exact weights and an actual one-defect support
attaining alpha. It explicitly rejects adding the old and new tuple
counts. The mathematical proof is the source; the check is corroboration.
Independent external review remains due.

Local replay: 729 exact weight checks, three actual F_17 same-support
bad records with 168 independent tuples each, global tuple disjointness,
and an explicit rejection of adding the overlapping old/new lower counts.
Runtime 0.06 seconds, peak RSS 11648 KiB; no Modal computation.
