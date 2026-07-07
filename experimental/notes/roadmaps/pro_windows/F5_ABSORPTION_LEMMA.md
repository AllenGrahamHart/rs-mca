# PRO WINDOW — F5 PROOF PROGRAM: the ABSORPTION LEMMA. OBJECTIVE: PROVE or REFUTE.

*Context: the F5 floor (post-strip spread remainder ≤ 16n³) is being
converted from a hardened conjecture into a theorem by obstruction
mining. Every step is done except ONE self-contained linear-algebra
statement. This window's job: prove it, or construct a counterexample.
Either outcome completes a milestone.*

## Setup (self-contained)

Fix a prime q, an integer k ≥ 2, σ ≥ 1, A = k + σ. For an A-subset
S = {x_1..x_A} ⊂ F_q^* let Π_S : F_q^S → F_q^σ be the top-coefficient
functionals (coefficients of x^k..x^{A−1} of the deg<A interpolant).
ker Π_S = restrictions of deg<k polynomials.

A CONFIGURATION is: A-subsets S_1..S_m of a finite set U ⊂ F_q^* with
pairwise |S_i ∩ S_j| ≤ A − 2, and DISTINCT slopes z_1..z_m ∈ F_q. Its
ALIGNMENT SYSTEM is the σm functionals on F_q^U × F_q^U:

>  (u, v) ↦ Π_{S_i}(u|_{S_i}) + z_i·Π_{S_i}(v|_{S_i}),  i = 1..m.

Let R = the span of these functionals. For a union point y ∈ U \ S_i,
the EXTENSION ROW χ_{i,y} is the extra functional obtained by replacing
S_i with S_i ∪ {y} (equivalently: the spillover functional
c_i(y) − u(y) − z_i·v(y), where c_i is the deg<k interpolant determined
on the solution locus).

## THE LEMMA TO PROVE (or refute)

> **ABSORPTION: if rank R < σm (the alignment system is dependent), then
> some one-point extension does not increase the rank: there exist i and
> y ∈ U \ S_i with χ_{i,y} ∈ R** — or, the invalidity alternative: some
> support's full Π_{S_i}(v)-block of functionals (v-side only) lies in R.

Equivalently (contrapositive): if every one-point extension strictly
increases rank and no Π(v)-block is absorbed, the alignment system is
independent. This is an exchange-type statement about the interpolation
matroid.

## Why this suffices (context, already proved on our side)

Independent systems cap live families at 2n/σ (dimension count).
Absorption kills dependent families: χ_{i,y} ∈ R forces agreement
spillover identically on the solution locus, so the family's true
agreement sets exceed A and it re-classifies into the already-charged
tangent column; the Π(v)-alternative re-classifies into the pencil-
degenerate column. Either way, dependent families cannot occur as
post-strip spread objects, and the F5 theorem follows with ~2^100 slack.

## Evidence (all replayable; nothing contradicts the lemma)

- 1,290/1,290 dependent embedded configurations across q ∈ {47, 97,
  193, 389} (random rigid designs to P = 14): ALL absorb (the spillover
  mode fires every time; the exact decision procedure, no sampling).
- The full minimal stratum (1,485 shapes, P=8, m=6, 3-regular, cores ≤ 2)
  × 8 embeddings at p = 2^61−1: all INDEPENDENT — generic embeddings
  are not even dependent (the dependence locus is a proper subvariety);
  absorption is only ever needed ON that locus.
- Proved on our side and available: (L3a) any dependence has every
  participant point covered ≥ 3 times or slope-shared (per-point
  2-moment collapse with nonvanishing leading Lagrange weights);
  the pencil identity Π_{S_j}(u + z_i v) = (z_i − z_j)Π_{S_j}(v) on the
  solution locus; a first-order no-go (formal syndrome pairings cannot
  decide this — the proof must use the interpolation geometry).

## Suggested attack lines (yours to ignore)

1. Exchange/matroid: view rows as elements of the module over the
   Cayley–Menger/interpolation structure; a circuit through support S_i
   may force the local rank of S_i's column-block to saturate, at which
   point the extension row of S_i is spanned. The per-point L3a collapse
   says circuits are combinatorially fat — use the fatness.
2. Dimension of the solution locus: generically V = the pencil-degenerate
   plane (deg<k × deg<k, dim 2k); dependence adds a direction; show any
   extra direction satisfies a spillover identity (the q=47 worked
   example: rank 11/12, dim V = 5 = 4 + 1, the +1 direction carries two
   identically-vanishing spillovers).
3. Refutation: a configuration with dependent rows where EVERY one-point
   extension increases rank AND no Π(v)-block is absorbed. Exact
   arithmetic + replayable script required; we replay within a day.

Conventions as always: exact arithmetic, explicit certificates,
replayable verifier with any claim.
