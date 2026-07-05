# PRO WINDOW W3 — "E1-DENSITY"

*Fresh window. Self-contained analytic number theory. A WEAKENED target: the
zero-certificate was over-strong; only o(1)-sparsity is needed.*

## Setting
Row prime p ~ 2^250 (admissible, |F| < 2^256), N' a 2-power quotient order
(cells N' in {128, 256}), zeta a primitive N'-th root in F_p, l' ~ N'/2. For an
l'-subset B of mu_{N'}, e_1(B) = sum_{y in B} y. A "quotient" (signed-core /
antipodal) collision is the known/paid class. A "non-quotient" collision is
B != B' with e_1(B) = e_1(B') mod p not of quotient type.

## Proved inputs (black boxes)
- collision_norm_criterion: a non-quotient collision forces
  p | Norm_{Q(zeta_{N'})/Q}(e_1(B) - e_1(B')), a nonzero integer of bounded
  height (every archimedean conjugate <= 2 l').
- kernel_lattice_reframing: equivalently, a sparse ternary kernel vector of
  K_p = {v : sum v_x zeta^x = 0 mod p} beyond the cyclotomic relations.
- graded_collision_radius: if (2s)^{phi(N')} < p then the norm < p, so small
  swap-distance s gives NO collision.

## What is ACTUALLY needed (verified over-strong before)
e1_fullness needs only that non-quotient collisions are **o(1)-SPARSE** relative
to the value set |{e_1(B) mod p}| (~ p ~ 2^249): a DENSITY bound, NOT the
zero-survivor folded lattice certificate. The folded dim-128 {-2..2}-box zero
cert is (a) likely IMPOSSIBLE at N'=256 (random model: ~2^48 expected non-
quotient box collisions at |F| < 2^256) and (b) UNNECESSARY (2^48 / 2^249 =
2^-201 = o(1)). Empirically: prize-shape birthday scans at N'=128/256 (250-bit
primes, 2^22 samples) found ZERO -- consistent with a negligible density.

## The ask (choose your target)
- **(A) Density/typicality bound:** prove non-quotient e_1 collisions are
  o(1)-sparse for admissible prize primes. Routes (from e1_fullness's own
  statement): (i) a bad-prime UNION BOUND -- the exceptional integers
  Norm(e_1(B)-e_1(B')) have bounded height 2l', so the primes dividing any of
  them have controlled density; bound the chance an admissible p is exceptional;
  (ii) split-prime transfer extending the proved small-prime range; (iii) a
  norm-threshold argument. Target: the non-quotient collision count is
  q^{-Omega(1)} times the value set (any negligible bound suffices).
- **(B) Refute:** a positive-density non-quotient collision family at admissible
  primes -- would break e1-fullness and the zone_b -> mca_unsafe route.
- **(C) Conditional:** o(1)-sparsity modulo a clean bound on the exceptional
  norm-divisor density.

## Downstream
Closes e1_fullness -> zone_b -> mca_unsafe -> mca_grand -> prize (the unsafe half
of grand challenge 1). Do NOT attempt the dim-128 exact lattice enumeration --
it is over-engineered; the density bound is the intended, achievable route.
(The N'=128 zero cert already HELD, lambda_1 = 31.67 > 16, as a bonus.)
