# PRO THREAD T1 — "SUBFIELD-TRACE-GATE" (SHARED: discharges dli + sov)

*Self-contained. The single highest-leverage open leaf: one node required by BOTH
the dli and sov character-sum programs, and plausibly reducible to machinery
already proved (the f1 Weil-restriction/interleaved reduction).*

## The phenomenon (two VERIFIED counterexamples)
Over an EXTENSION row F_q = F_{p^k} (k>=2), the additive character
psi(z)=exp(2pi i Tr_{F_q/F_p}(z)/p) becomes DEGENERATE on subfield-structured sets:
- **Frequency face (dli):** if the square-root section sigma(mu_n) lands in a
  subfield (p ≡ 1 mod 2n forces mu_{2n} subset F_p) and lambda is trace-zero
  (Tr(lambda)=0, a nonzero (k-1)-dim space), then Tr(lambda P(sigma(y)))=
  P(sigma(y)) Tr(lambda)=0 for P(X)=X, so psi=1 identically and the second moment
  S_{j,lambda}=Omega(L_j) (VERIFIED F_{13^2}).
- **Cell face (sov):** on the deployed row F=F_{17^32}, H=mu_512, the canonical
  trace character is FLAT on exactly 496 of 512 grid points (only mu_16=F_17^* has
  nonzero trace, by an LTE/Frobenius-pairing argument), giving a positive-density
  (0.506 at h=21) non-cancelling cell (VERIFIED).

Over PRIME rows (k=1) this is VACUOUS: Tr=id, psi(lambda .) is a nontrivial
character for every nonzero lambda, no collapse.

## The obligation (the node subfield_trace_paid_gate)
> Over extension rows, the trace-flat/subfield-degenerate locus is EITHER
> (a) a PAID ledger class (priced), OR (b) reduces to the base field F_p by Weil
> restriction, so the base (prime-field) estimate suffices.

## The tractability hook: reuse the PROVED f1 machinery
The interleaved/Weil-restriction reduction that closed f1_full_field_pole_forcing
already does base descent: an F-valued word source is an e=[F:B]-interleaved
base-list witness (D subset B, syndrome commutes with B-basis expansion, mult-by-z
= M_z). The question: does the SAME Weil restriction carry the dli/sov additive
character sums over F_q down to the base F_p?
- Tr_{F_q/F_p} = Tr_{B/F_p} o Tr_{F_q/B}; the inner trace is the natural pairing on
  the interleaved coordinates. Does summing over F_q decompose as an F_p-sum over
  the base-list coordinates plus a paid degenerate remainder?

## The ask
- **(A) Base reduction:** prove the dli second moment / sov grid sum over an
  extension row equals (up to a paid remainder) the corresponding base-F_p object,
  where the prime-field estimates (dli_bohr_flatness_prime, sov_gridsum_residual)
  apply. Use the proved interleaved decomposition.
- **(B) Priced gate:** if base reduction fails, prove the trace-flat/subfield locus
  is a paid class — bound its total mass/count and price it in the ledger
  (it must absorb the density-0.506 trace-flat cells).
- **(C) Refute:** an extension row whose trace-flat locus is neither base-reducible
  nor priceable within the prize budget.

Discharges the shared trace/subfield part of BOTH dli_harmonic_conductor_ledger
and sov_affine_piece_partition_payload. Prime-field residuals are separate leaves.
