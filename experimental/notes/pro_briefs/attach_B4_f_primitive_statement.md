# f_primitive_case

- **status:** CONJECTURE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

For every linear P <= P^j and pair (u,v): #{ell in P cap D_j : gcd(P cap D_j) = 1, ell not a pullback, ell unpaid} <= n^{B_F}. By f_gcd_reduction + f_scale_recursion this implies full Conjecture F.

## Attack surface

the irreducible instance every route must face; coordinate planes first (perfiber is its coordinate case), kernel planes second

## Falsifier

toy-scale (n = 16..32) exhaustive plane searches finding super-poly primitive unpaid points

## Ledger (migrated notes)

E7 EVIDENCE (PR #183, replayed green): exact n=16 j=3 projective-plane census — the paid spike is EXACTLY the 16 common-root planes (105 = C(15,2) points each, the tangent shape as predicted); primitive max after removing them = 38 across 240 top planes, BELOW the weighted pair-bound floor 60. Hankel-kernel sample (j=5, t=3, 2048 full-rank planes — the consumer-relevant family): primitive max 13 < floor 30. No rich unpaid primitive dim-2 plane in census or sample. Prior UP. Next refinement: exhaustive j=4 Grassmannian or structured Hankel row-space enumeration.
