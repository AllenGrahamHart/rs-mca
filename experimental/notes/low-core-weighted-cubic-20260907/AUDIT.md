# Audit Scope

Status: complete local hand proofs and exact arithmetic checks, offered
for independent mathematical review. This is not formal certification.

## Proof Review Focus

1. The coefficient equations have weights two on the projection image
   and three on its kernel; the cubic term contains no kernel variables.
   After the finite power cover all equations have ordinary degree <=6.
2. The degree budget `sum deg(Z_i)*6^dim(Z_i)<=6^(2s)` uses the
   actual nonpure equation locus. A pure over-cover can introduce
   components with constant scalar projection and invalidate incidence.
3. Auxiliary shifts avoid branching on the finite set of counted pairs.
   Only then is division by the full `2^(2s-d)*3^d` lift multiplicity
   valid. It does not change the field denominator for original labels.
4. The rational normalization parameter is bounded in a fixed function
   space; it is not assumed polynomial of degree <K. The projection has
   finite fibers on all subvarieties and input degree <K+h.
5. The height argument uses iterated intersections, not an unproved
   small-height claim. The common factor q is nonzero only on joint cores;
   zeros elsewhere and roots of B cannot be silently removed.
6. The same resource is used once. LOW weights are dropped only as a
   nonnegative relaxation; other LOW groups are not reclassified HIGH.
   The near allowance is added once. The singular pair is in the count.
7. The stronger residual restriction comes with the larger paid bound
   274979661292365251. It does not strengthen the old smaller constant
   at the old scope. Both remaining patterns have polynomial examples;
   these are neither unsafe received sources nor a closure theorem.

The new primary arithmetic check, the completed-HIGH check and the
independent integer-cover check reconstruct the same bound differently.
The included completed-basis control uses only a tiny finite example.
The other 31 serial tests replay the previous packet's prerequisites.
Numerical checks do not prove the universal geometry in items 1--5.

Publication replay on 2026-09-07, under a 256 MiB RAMguard ceiling:

- Normal wrapper: 35/35 PASS, 3.16 seconds, maximum RSS 16512 KiB.
- Optimized wrapper: 35/35 PASS, 3.36 seconds, maximum RSS 20800 KiB.
- All 132 source hashes PASS.
- In-memory manifest mutations for hash drift, duplicate source, unlisted
  source and path escape are all rejected. The unmodified baseline passes.

These measurements describe the two actual publication replays; timing is
not a promised performance bound. No Modal resources were used.

## Resource And Reproduction Policy

Run `python3 -B experimental/notes/low-core-weighted-cubic-20260907/replay.py`
from the repository root. Each child has a 15-second timeout. There is
no parallel pool, third-party dependency, field-sized scan or Modal task.
An interrupted/failed check is not success. The wrapper clears
`PYTHONOPTIMIZE` for assertion-enabled children in either wrapper mode.

The manifest detects missing, extra or altered source files, and duplicate
paths. It is a reproducibility checksum, not authentication against an
attacker rewriting both files and their manifest; the Git commit pins the
packet. Full local DAG diagnostics already contained 260 DAG and 11
crosswalk errors before this export. No globally clean DAG, TeX build,
Lean certification or upstream acceptance is claimed.
