# PRO WINDOW P4 — "M720-NORMGATE"

*Self-contained. A structural nonvanishing/norm-gate theorem. Brute-force census
is infeasible (exponential MITM: 73/79 deployed cases hit the probe ceiling), so
a STRUCTURAL proof is required — not exhaustion.*

## Setting
Official-shape primitive rows; a "norm-gate case" at primitive parameter
h = 7..20 asks whether any anchored NON-TORAL survivor exists (a survivor core
that beats the planted/toral count through the norm gate). W = window, n the
domain size. A case is discharged by either a uniform nonvanishing theorem OR a
complete=true zero-survivor certificate.

## Evidence (Modal, exact — the empirical spine)
Full census run: gate_pass = true; every case that EXHAUSTED (n=16,32 at h=7)
returned ZERO anchored non-toral survivors and ZERO anchored toral survivors;
larger cases (n>=64, higher h) hit the 6,000,000-probe ceiling INCOMPLETE. No
counterexample anywhere the search finished. So the conjecture is: for all
official-shape primitive h in 7..20, there are NO anchored non-toral norm-gate
survivors.

## The ask (structural discharge)
> Prove a uniform nonvanishing theorem covering every official-shape primitive
> h = 7..20 norm-gate case: no anchored non-toral survivor exists (equivalently
> the relevant norm/resultant is nonzero for all official parameters), so every
> case is discharged without per-case enumeration.

- **(A)** The structural theorem. Likely levers: (i) the survivor condition is
  divisibility of an explicit NORM (of a bounded-height algebraic integer built
  from the anchored core) by the row characteristic/modulus — bound its height
  and show non-divisibility at official scale (cf. the e1 bad-prime union bound
  and graded_collision_radius: if (2s)^phi < p the norm is too small to vanish);
  (ii) a toral/non-toral dichotomy that makes non-toral survivors violate a
  degree or conductor count; (iii) an MITM->analytic conversion turning the
  enumeration into a single character/norm-sum bound.
- **(B)** an official-shape primitive case with a genuine anchored non-toral
  survivor (a counterexample the census missed at larger n) — refutes the gate.
- **(C)** conditional on a clean height/degree bound for the anchored-core norm.

Downstream: m720 manifest -> midlarge norm-gate column -> the mca_safe staircase.
