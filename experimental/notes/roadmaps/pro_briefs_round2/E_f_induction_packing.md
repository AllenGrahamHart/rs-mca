# Pro brief E — the global packing step (close F_{r-1} => F_r)

*Self-contained continuation of your Brief B. You proved the dichotomy and the
descent; this closes the one remaining step you flagged.*

## The frame (recap of your Brief B, all proved)
An `r`-flat `P ~ P^r`; for each domain point `x`, an evaluation hyperplane
`H_x = { t in P : ell_t(x) = 0 }`; `P cap D_j` = points on `>= j` of the
`H_x`. For `p in P cap D_j`, `R(p) = { x : p in H_x }`, `m(p) = |R(p)|`.
Gcd-trivial = no `H_x` is the whole flat.

- **L1 (dichotomy, proved):** for any `0 < alpha < 1`, either the incident
  functionals are SPREAD — `I_r(p) >= (1-alpha)^{r-1} C(m,r)` independent
  `r`-subsets (greedy span-avoidance) — or `> alpha m` of them lie in a proper
  subspace `U`, giving a positive-dimensional proper subflat carrying the
  shared divisor `g_{S_U}`.
- **L2 (spread bound, proved):** `|Spr_alpha(P)| <= C(n,r) /
  [ (1-alpha)^{r-1} C(j,r) ]` (double counting through independent
  `r`-tuples).
- **L3 (descent, proved):** coincidence gives strict descent — division by
  `g_S` is linear, degree drops by `|S|`, dimension drops; lands in
  `F_{dim Q}`, `dim Q < r`, or re-triggers gcd-reduction.

## The proved recursions you may use as black boxes
- **f_gcd_reduction (PROVED):** with `w = deg gcd(P cap D_j)`, division by the
  gcd maps `P cap D_j` injectively into `P' cap D'_{j-w}`, `dim P' <= dim P`,
  over `(X^n - 1)/gcd`, with trivial image gcd. So `F` reduces to gcd-trivial
  planes.
- **f_scale_recursion (PROVED):** `P cap D_j^{per}(M)` is linearly isomorphic
  to `P' cap D'_{j/M}` at scale `n/M` (an `M`-pullback `ell = g(X^M)` embeds
  `g`'s coefficients at multiples of `M`). Hence
  `F(n) <= F_primitive(n) + sum_{M | gcd(n,j)} F(n/M)` — the periodic branch
  recurses to smaller scale.

## The gap (the one step to close)
The target is `F_r`: `#(P cap D_j)_{gcd-trivial} <= n^{B_F}` with `B_F`
absolute, independent of `r`. L2 alone gives a numerator of order `n^r` before
further structure — too weak on its own. The spread points must be packed into
an absolute exponent.

## The ask (choose your target)
- **(A) Close the induction:** prove `F_{r-1} => F_r` with absolute `B_F`,
  absorbing the `n^r / j^r` spread numerator. The natural route:
  the rank-defect branch (L1) yields a shared divisor -> f_gcd_reduction or a
  proper subflat -> lower `r`; the spread branch (L2) must be controlled by a
  PACKING argument over the flat family (each independent `r`-tuple charges
  `<= 1` point; bound the reuse), possibly combined with f_scale_recursion to
  recurse the periodic mass. Show the two branches compose to a bound with
  `B_F` independent of `r`.
- **(B) Counterexample:** a gcd-trivial `r`-flat with `>> n^{B_F}` `D_j`-points
  for every absolute `B_F` (would refute the induction and redirect the
  program).
- **(C) Conditional:** `F_r` modulo a clean packing hypothesis on independent
  `r`-tuple incidences (state it precisely), reducing the induction to that
  lemma.

This is the last open link in the chain `f_dim_induction -> f_primitive_case
-> conj_f` (Conjecture F). Reformulation welcome if the natural invariant is
not `#(P cap D_j)` but a moment/packing count.
