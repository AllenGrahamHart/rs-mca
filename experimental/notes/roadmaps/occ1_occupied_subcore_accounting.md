# OCC-1: occupied-subcore accounting audit

- **DAG node:** `a1_lower_overlap_occupied_subcore_accounting`.
- **Task:** OCC-1.
- **Status:** CONDITIONAL / RESIDUE.  The E33 occupancy column is benign, but
  the advertised direct packing proof is under-specified.
- **Verifier:** `experimental/scripts/verify_occ1_occupied_subcore_accounting.py`.
- **Certificate:**
  `experimental/data/certificates/occ1-occupied-subcore-accounting/occ1_occupied_subcore_accounting.json`.

## What Was Checked

The verifier extends the E33 toy rows with the missing occupancy columns.  For
each sampled anchor it records:

```text
actual occupied cores C = T cap T0,
per-core multiplicities K_C,
the induced (k-1)-shadow inside T0,
the joint (number of occupied cores, max K_C) distribution.
```

It reuses the pinned E33 rows and seeds, so the event totals match E33:

```text
F_97 / mu_16: r=6 -> 186, r=7 -> 684
F_17 / mu_16: r=6 -> 852, r=7 -> 2882
```

## Toy Verdict

The toy occupancy remains linear:

```text
F_97: max partner events/anchor = 13
      max actual occupied cores/anchor = 9
      max K_C = 5
      max (k-1)-shadow cells/anchor = 30

F_17: max partner events/anchor = 72
      max actual occupied cores/anchor = 42
      max K_C = 5
      max (k-1)-shadow cells/anchor = 104
```

So the E33 falsifier still does not fire.  The observed decomposition is:
core multiplicity stays bounded, while the remaining work is bounding how many
actual cores can be occupied.

## Direct Packing Obstruction

The fixed-subcore cap alone cannot imply the desired `O(n)` accounting.  At
every clean row, even a purely formal family with one event in each `(k-1)`
cell already has super-linear size.  The verifier records the elementary
lower bound

```text
#(k-1 cells in T0) = C(A,k-1) = C(A,t+1) >= C(A,2) > n.
```

For the Row-C clean rows the exact small-`t` counts are:

```text
RowC 1/4:  C(261,6) = 414356272512
RowC 1/8:  C(133,6) = 6856577728
RowC 1/16: C(67,4)  = 766480
```

The lower-overlap shell is larger still:

```text
RowC 1/4:  C(261,7) = 15094407070080
RowC 1/8:  C(133,7) = 124397910208
RowC 1/16: C(67,5)  = 9657648
```

This is not an aligned-support construction; it is the obstruction to the
proposed proof method.  A constant per-cell cap plus lattice packing does not
count occupied cells.

## Named Residue

The remaining theorem should be stated as:

```text
a1_lower_core_shadow_incidence_bound
```

After the unified strip, for a fixed anchor `T0`, the actual lower-overlap
cores

```text
C = T cap T0,       k/2 < |C| < k,
```

must have `O(n)` occupied incidence mass, or else a positive-density subfamily
forces one of the already-paid structures: tangent pencil, unified pullback,
dihedral, extension, or moment/PTE trade.  Equivalently, the post-strip
alignment equations must compress the enormous `(k-1)` shadow down to a
linear active shadow.

Once this incidence theorem is supplied, A1's existing assembly gives:

```text
# near-k partners <= (fixed-core cap) * O(n).
```

The same statement is the first input for OCC-2, with the cells replaced by
graded tangent-depth cells.

## Verification

Run:

```bash
python3 experimental/scripts/verify_occ1_occupied_subcore_accounting.py
```
