# Hand audit, 2026-09-06

## Exact-gate continuation

Reread BCHKS Lemma 3.1 and its smaller-m paragraph in the primary
paper. Rechecked the strict variables-versus-equations inequality at
m=1,2, retaining Z=max(Y,Z_0). The selected-witness substitution
uses only X<=m*a. The separate d+1-point collinearity load was
proved again for m=1, m=2 and m>=3; interpolant existence alone
would not justify this continuation. No Hensel numerator, factor,
Frobenius or content-root bound changed.

19243 tiny exact monomial-count and load checks passed, including
624 m=1 cases needing the maximum-Z branch, plus the rounding
counterexample to using floor(X). These do not prove the external
Hensel results. The consumer independently checked its integer
affordability formula using rational upper/lower radical brackets.
Peak resident memory was below 12 MiB, with no Modal job.

## Checked in this work cycle

- Read primary BCHKS Lemma 3.1 and Section 3.2, and the relevant BCIKS
  Section 5 and Appendix C estimates. The full numerator is reconstructed
  from chosen bad witnesses; the sketched MCA theorem is not a premise.
- Distinct scalar slopes, existential same-support noncontainment and
  actual RS dimension are preserved.
- Full pre-specialization factor degrees are used. All content-root
  exceptions are charged with +Z instead of assumed absent.
- L=ceil(X) makes the coefficient index inequalities genuinely integral.
  No claim that the source theorem is false follows from this precaution.
- Inseparable middle degrees retain BOTH Frobenius factors in w_ij.
  Appendix C's final (2*b*d+1)*d0*h0*z0 bound is dominated by
  (2*d+1)*w_ij; no silent large-characteristic restriction.
- The coordinate agreement argument is written independently with d+1
  interpolation points, avoiding rate/dimension ambiguity in source text.
- A fixed codeword line has at most r+1 of the preselected bad witnesses,
  whether or not the received pair is within joint distance r of that line.
- A final degree-deficit audit replaced the sharp root-weight shortcut
  with hensel_weight_ledger.md. It proves the numerator recurrence,
  exceptional-denominator count and inseparable evaluation estimate
  without assuming Lambda(T)=Lambda(W)+b. The coarse bound is unchanged.
- The q<=H branch is explicit; otherwise the requisite common Hensel
  starting point exists by a direct resultant-degree bound.

## Not performed / not claimed

At the original import no scripts, tests or numerical jobs were run.
The exact-gate continuation above adds small checks, not graph generation.
No independent second-person hand audit. No upstream acceptance or exact
printed-constant closure. Node-local PROVED records the complete argument
at THIS rounded constant, not an empirical status or a completion claim.

The main independent-review target is Section 4's mapping of the published
regular-numerator estimates, especially inseparable substitutions. A gap
there reopens this node and its new bracket contributions; the separate
quadratic and almost-half-distance suppliers remain available.
