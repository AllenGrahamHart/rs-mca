# Review priorities and replay limits

This is a hand-proof contribution with small arithmetic/control checks.
PROVED denotes the local mathematical status at the exact source contract;
it does not denote independent external review or formal certification.

## Hand Review Priorities

1. d=10 coefficient descent uses infinitely many points of the actual
   algebraic coefficient locus, not the finite closure of sampled pairs.
   The receiver, its coordinates and the original slope field do not descend.
2. The maximal-family proof first places admissible rational parameters in
   finitely many divisor-space cosets. Dimension four forces one full coset;
   its monic polynomial model then covers ALL other nonsingular bounded
   pairs. The uncounted number of initial cosets is not used as a pair cap.
3. Projective T=infinity is retained by degree-ten homogenization. Common
   factor zeros outside the complete-core union have empty joint lists,
   not deleted scalar defects. Receiver values may differ within a T-fiber.
4. In d=7, irreducibility, centering and gcd removal force infinitely many
   evaluation values at every finite X and at the leading coefficient.
   These are the reasons pole cancellation cannot hide in the family.
5. The homogeneous cubic normalization has no basepoints and a rational
   generic inverse. The degree formula is used in ORIGINAL pair coefficient
   degree, counting all geometric components, not only rational components.
6. Dimension two is applied only to the complement of all top components,
   using the actual nonpure lifted-locus degree budget. The whole locus is
   still dimension three. No artificial pure over-cover replaces it.
7. Constant matching fibers cost agreement and domain coordinates together;
   all such fibers are roots of the exceptional-list polynomial. This
   gives the `-3g` term in the list budget. Singular and off-curve pairs
   are added explicitly, and one HIGH resource/near charge is used.
8. Full-strip alternative bounds combine by maximum. The kernel surplus
   changes sign between 8655 and 8656; no extrapolation is made.

## Replay

```sh
python3 -B experimental/notes/low-core-complete-cubic-20260907/replay.py
python3 -O -B experimental/notes/low-core-complete-cubic-20260907/replay.py
```

The wrapper checks every source hash and the exact source inventory,
rejects hash/duplicate/missing-entry/path-escape mutations, and runs each
checker serially with a 15-second timeout. It removes PYTHONOPTIMIZE from
the child environment and starts assertion-enabled children in both modes.
The local publishing run additionally uses RAMguard tiny (256 MiB RAM,
64 MiB swap, 60 seconds). No field-sized search or large computation occurs.

The new checks independently reproduce the d=10 interval budgets, the
d=7 Cauchy exclusion and component counts, and the aggregate reserve.
The cumulative checks also exercise earlier algebraic and accounting
controls. A passing integer check is not a proof of a universal statement
about parameter families, geometric components, or source exhaustion.

No full-upstream build, TeX compilation or Lean proof is claimed. No
original-row endpoint is certified and no Modal compute is requested.

Publication replay: all 158 source files match the local origin byte for
byte and their hashes; 39/39 checks pass in both modes. Normal replay:
3.15 seconds, 16640 KiB peak RSS. Optimized wrapper: 3.24 seconds,
20948 KiB peak RSS. Four in-memory manifest mutations are rejected
in each run, followed by a successful baseline check. These measurements
are resource observations, not an independent audit of the hand proofs.

Audit verdict: OPEN GAP. K3's unrestricted original-source coverage and
K4's normalization/ownership/add-back obligations are still open; the
proved normalized source theorem does not discharge those obligations.
