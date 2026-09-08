# Audit and provenance

PR #1174, Scott Hughes, commit
`1b613fc669158a690a52b64f0eeb440f10672f1e`,
`experimental/grande_finale.tex`, `thm:mca-uniform-rank-one-weighted-line`.
[Pinned source](https://github.com/scottdhughes/rs-mca/blob/1b613fc669158a690a52b64f0eeb440f10672f1e/experimental/grande_finale.tex).
The function `weighted_line_cap` in the pinned release verifier was read
to check the exact numerical expression, not executed.

The geometric low/high proof is reconstructed from that source. The
histogram domination, reduction to the integer quadratic, and uniform
low estimate are a new local analytic substitute for its million-row scan.
All arithmetic shown in the proof was checked by hand; no programs were run.

Guards: remove only universally incident zero normals; retain never-incident
coordinates solely as unused available weight; keep two line classes when
reselecting M points; truncate a dominant line's credited weight at M-1;
include both deficiency types before proving their domination. The exact
maximum is of the certificate formula, not a realized received-line count.

This proves the previously pending numerical base case. It does not prove
the nine optimized recurrence maxima or the rank-twelve optimum. The proof
is elementary and has no dependence on any previous scanned payment.
