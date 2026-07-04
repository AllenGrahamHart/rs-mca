# Pro brief (Brief-D thread, round 2) — prove PCF, the flatness estimate

*Your route-(C) conditional closure was verified and banked: b2b_primitive_core
is now CONDITIONAL on exactly the hypothesis you isolated. This brief asks for
PCF itself — the last input. The Hankel thread (running in parallel) closed its
node through exactly this kind of staged dialogue; same rules: every claim you
make gets machine-verified here before banking, counterexamples to my framing
are as valuable as proofs.*

## The target (your own formulation, now the named node pcf_norm_gate_flatness)
For every central level-j profile M:

    |G_j(M)|  <=  q^{-L_j + eta_j} U_j(M),        sum_j eta_j = o(t)
    (prize-row budget: H = sum eta_j <= 122/256 via W_cen <= 2^n, or the
     exact q^{-t+H} W_cen <= 2^122)

where G_j(M) = {zero skew} u {nonzero d in D_j(M): |supp d| >= L_j + 1 and
q | gcd_{ell <= L_j} Res(X^{N_j} + 1, Q_{d, 2ell-1})} — the large-support
bounded-coefficient skews whose ENTIRE folded-resultant packet carries the
fixed ~2^250-bit prime.

## Proved structure you may use freely
- The exact cascade B_j(M) = q^{-L_j} sum_lambda prod_y sum_d psi(d lambda.v_y);
  sum_j L_j = t; the Vandermonde threshold (nonzero skew => support >= L_j+1);
  the simultaneous norm gate (every nonzero skew is resultant-gated at every
  imposed odd exponent); complement duality L_A L_{A^c} = X^n - 1.
- THE UNCONDITIONAL BASE CASE: the two-level gate bound (levels 0/1) is
  already proved — the non-coset excess there is carried by skews of support
  >= 2^32+1 / 2^31+1 passing all gates. Any induction you build has its floor.
- Numerics for calibration: at exceptional prime 17 the gated sets are RICH
  (the signed vanishing-sum object); at inert 97/193 they are EMPTY — PCF is
  trivially true at generic small primes and the content is at structured
  primes. The level-2 falsifier data (exact census reproduction at mu_32) is
  available on request.

## Suggested attack surfaces (yours to accept or replace)
1. **Resultant-magnitude counting:** each Res(X^{N_j}+1, Q_{d,r}) is a nonzero
   integer of bit-size <= phi(2N_j) log2(weight bound); q ~ 2^250 divides it
   for AT MOST bitsize/250 prime slots. The gcd over L_j ~ 2^{32-j}
   simultaneous resultants is the lever: how many d can have q dividing ALL
   of them? A union/moment bound over the L_j gates, even losing polynomial
   factors per gate, wins if it beats q^{-L_j + eta_j}.
2. **The divisor-pair route (your route B):** both halves of
   L_A L_{A^c} = X^n - 1 are constrained; a skew that passes all gates at
   level j constrains the complement's tower too — a bilinear/pairing
   argument may force eta_j = 0 outside boundary levels.
3. **Per-level Fourier/second-moment:** E_lambda |sum_d psi(...)|^2 over the
   nonzero frequencies, using |D_j| structure — the deviation is a variance,
   and the norm gate says the large-deviation set is resultant-thin.

## Deliverables (choose; reformulation welcome)
- (A) PCF in full (any eta_j profile with sum = o(t) + the prize-row budget).
- (B) A counterexample: a central profile M and level j with |G_j(M)| >>
  q^{-L_j+o(L_j)} U_j(M) — i.e. structured mass of simultaneously-gated
  large-support skews. This would defeat the tower route for the primitive
  core and be a major (publishable) discovery about vanishing sums.
- (C) PCF conditional on ONE sharper named estimate (e.g. a bound on
  simultaneous resultant divisibility for a single support pattern), with
  the reduction proved.
Constraint: no interpolation-style counting (dead at k=16: reaches 2^128);
no prefix-fiber circularity.
