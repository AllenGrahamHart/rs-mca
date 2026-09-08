# Audit and provenance

The two-anchor companion and its rank-twelve small-core application are now
proposed in [PR #1175](https://github.com/przchojecki/rs-mca/pull/1175#issuecomment-5563629435).
The [export record](../../../notes/correspondence/TWO_ANCHOR_PR1175_EXPORT_20260907.md)
pins the exact public proof and certificate. Review remains pending; this
does not export or certify an unrestricted rank-twelve theorem.

Hand reconstruction, 2026-09-07. The setting and finite application were
motivated by PR #1174 at 1b613fc669158a690a52b64f0eeb440f10672f1e.
This elementary argument is recorded independently; it does not import
the PR's optimized recurrence table, claim novelty priority for scalar
incidence, or certify its other statements.

The subsequent upstream subtraction audit identified the existing ordinary
LIST analogue, thm:affine-span-list in experimental/grande_finale.tex,
already on main at 93fba1be3f3299b0ba4708d88715377bbb656e45. Credit
that induction and common-zero ratio as antecedents. The MCA-specific
content here is the slope-dependent common polynomial-pair gauge, exact
selected-support transport and the tau charge at exceptional common zeros.
The field-linear space is over the ambient field, not just a coefficient
subfield. The false MCA ordered-basis denominator retracted by #1165 is
not used: on its (n,K,m)=(100,1,21) example our generic rank-zero
base gives the much weaker valid rank-one cap 380, not the false 23.

The proof and its finite application were proposed for review in
[PR #1174 comment 5563239109](https://github.com/przchojecki/rs-mca/pull/1174#issuecomment-5563239109).
The local export record pins the exact text. Publication is not an
independent audit, merge, active-v4 payment or proof of the missing
arbitrary-source rank hypothesis.

The decisive change is that the anchor lies in the SELECTED scalar
support. A common affine/codeword gauge forces every incident explanation
into a codimension-one kernel, and direct lifting preserves that very
support's badness. Raw-low minimizers are unnecessary for this purpose.
Common evaluation zeros are counted separately, including their exceptional
unique slopes. The resulting induction is purely on explanation dimension.

The audit checked membership of both translations, full-child-code badness,
the K=1 zero-code child, z<=K-s, never-satisfied zero coordinates, the
integer floor, smaller actual dimensions, and the exact rank-zero witness.
Finite checks supplement, but do not prove, these general arguments.
Independent external hand review and generated global replay remain due.

verify.py passed 73 actual selected records, 262 exact proper transports,
13 exceptional-zero incidences, 21 rank-zero witnesses, 77220 integer
envelope controls and all nine deployed-row recurrence values. Initial
local run: 0.08 seconds, peak RSS 11264 KiB, RAMguard tiny. No Modal
job or large row construction was run. These finite checks do not stand
in for the full hand proof or an independent external audit.

## Coupled two-anchor continuation

The new companion uses evaluation functionals on C' ALONE, not the
MCA incidence normals with the extra r_1 coordinate. For two distinct
projective fibers, the common kernel has dimension s-2, giving the joint
size bound w_i+w_j<=K-s+2 by polynomial division. This is why the
false proper-normal occupancy premise from #1165 is not being reused.

The first child's common zero set is exactly its parent's projective
fiber minus the anchor. Its universal/exceptional split is retained before
the real envelope is relaxed. Convexity gives two endpoints, both of
which are kept. All rational denominators are positive at the stated scope.
The normalization comparison allows increased slack; it does not silently
keep the old row when common zeros were not universally satisfied.

verify_two_anchor.py passed 24 actual child zero-set controls, 3732
partition envelopes and 3612 normalized-row comparisons, plus two explicit
invalid-shortcut controls. Runtime 0.12 s, peak RSS 11648 KiB. The new
finite rank-twelve consumer owns normalization, core identification, exact
payments and its separate finite Johnson certificate. No general proof
is inferred from the bounded controls.
