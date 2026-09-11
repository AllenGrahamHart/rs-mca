# Verification Scope And Limits

## Fresh Frozen Replay

From the outbound checkout, both commands completed successfully:

```sh
python3 -B experimental/notes/kb-receiver-conditioned-source-bounds-20260911/replay.py
python3 -B -O experimental/notes/kb-receiver-conditioned-source-bounds-20260911/replay.py
```

Measured under RAMguard tiny, serially with no network:

| Mode | Wall seconds | Peak process RSS, KiB |
|---|---:|---:|
| normal | 4.27 | 45424 |
| optimized | 4.94 | 45756 |

The wrapper verifies 1804 listed source hashes, 49 inherited proof
documents and the 22-node acyclic required closure. It rejects 54
malformed manifests. These are custody/structure checks, not proof of
the geometric statements.

It builds a temporary common source tree and runs ten new focused
checks plus three inherited checks serially. Each child has a 20-second
timeout; the external RAMguard envelope limits the complete local run
to 60 seconds and 256 MiB address space. The wrapper itself is not a
replacement for a resource limiter. It cleans up its temporary tree.

## Arithmetic And Small Exact Controls

- Dense conic: primary and independent 43-row source ledgers; seven
  repriced bad ledgers among 39 mutations; all conic types, 1000 raw
  identities, 15 polynomial lifts and four retained coefficient roots.
- Canonical colours: actual F17 constant and zero-evaluation controls;
  a nonmaximizing raw-one example shows why canonicalization is required.
- Small-colour consumer: independent first-hit versus complement tuple
  counting; 122 exhaustive small banks, 1000 cost identities, a rational
  rounding counterexample and 39 mutations, six with repriced totals.
- Bounded colours: independent 128-branch tree, 127 whole-interval input
  gates and cap/J monotonicity; 3000 LOW/HIGH cost controls; 15 exact
  tuple-profile controls; 37 mutations, six repriced.
- Trimmed profiles: 69 exact allocations, 453 complete-core controls,
  153 heavy-tail inequalities; an F17 core has 462 actual ordered bases
  versus lower bounds 350 (trimmed) and 315 (maximum-only).
- Sparse heavy: independent full branch reconstruction and whole-J/E
  gates; 300 tail-cost and 300 raw-cost controls; 34 scope/ledger
  mutations including six repriced totals.

Fresh inherited checks reconstruct the original min-envelope resource
(765 input-branch gates and 512 transfers), exhaust 27 small joint-LIST
sources/49299 tuples, and test 20358 moving-parabola labels with all
27 pairs represented. Other inherited arithmetic is NOT freshly replayed
in full. Its proof documents and listed source hashes are retained.

## What The Checks Do Not Establish

The finite controls do not enumerate the original field, received lines,
bad supports or full Prize sources. Hand proofs supply canonical complete
defects, nonzero core evaluations, exact label ownership, whole-fibre
contraction, shared-carrier LIST and the original-source transport.

The primary and independent arithmetic reconstructions share proved
ancestor mathematics. Passing them does not constitute independent
external review of that mathematics. Mutation counts describe specific
tested alterations, not every possible implementation or proof error.
An altered looser upper estimate need not be a false theorem.

Adjacent parameters failing a chosen upper recipe are not unsafe
witnesses. No completeness theorem for arbitrary receiver profiles,
full error-rank coverage, active-v4 atom, LIST endpoint or Prize closure
is certified here.

## Resource And Compute Requests

None. No Modal, spending, large enumeration, CAS elimination or field
construction was needed. The next missing step is an original-source
incidence/coverage argument, not an unbounded numerical search.
