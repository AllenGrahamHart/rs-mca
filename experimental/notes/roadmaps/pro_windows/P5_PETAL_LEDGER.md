# PRO WINDOW P5 — "PETAL-LEDGER"

*Self-contained classification problem. A finite ledger with a c-independent
bound closes it. The residue-kernel dimension bound (Lemma 13) is already proved.*

## Setting
L1 coset-chart full-petal residue bridge. For a missed-core defect d and petal
size ell, set c = d - ell (the "excess"). The residue-line kernel
    K_{I,d} = ker(pi_{>d} R_{I,d})
carries the extra (non-core) codewords. PROVED (Lemma 13, in-regime
d <= (t-1)ell - 1): dim K_{I,d} <= c + 1, with floor rank >= ell.

## What must be constructed (the terminal)
> A squarefree classification ledger covering EVERY squarefree realizable
> locator point in the residue-line kernels, where each family is recorded as:
> - a CHARGED class (with a citation to an already-paid family); or
> - an UNCHARGED class (with a polynomial bound whose exponents are INDEPENDENT
>   of the excess c),
> and the number of UNCHARGED class records is bounded INDEPENDENTLY of c.

The falsifier: a squarefree realizable kernel family missing from the ledger,
charged without a paid citation, or uncharged without a c-independent bound.

## The ask
- **(A)** Build the ledger. The dimension grows (dim K <= c+1), so the kernel
  gains ~c degrees of freedom as c grows; the claim is that ALL the c-dependent
  growth is CHARGED (cyclotomic/antipodal/coset-quotient families already paid
  in the worst_word/E22 ledger), leaving only O(1) uncharged classes. Likely
  lever: decompose K_{I,d} into (i) a coset/quotient-saturated part (charged to
  the dyadic quotient families, exactly as in the E22 tail-removed factor
  manifest) plus (ii) a bounded-dimension genuinely-new part whose squarefree
  realizable points form O(1) families with c-independent polynomial bounds.
  Give the explicit charged/uncharged split and the c-independent uncharged count.
- **(B)** a squarefree realizable kernel family whose count of genuinely-new
  (uncharged) classes GROWS with c — refutes the c-independent ledger.
- **(C)** conditional on a clean statement of which kernel directions are
  chargeable to paid families.

Evidence: value set = signed-core quotient EXACTLY at small N'; the charged part
looks quotient-shaped. Downstream: petal ledger -> petal_excess_induction ->
the worst_word/list pricing.
