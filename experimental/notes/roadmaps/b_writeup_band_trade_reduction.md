# B-WRITEUP: band-trade reduction packet

- **DAG node:** `u1_beta_band_trade_reduction`.
- **Task:** B-WRITEUP.
- **Status:** conditional write-up; the remaining residue is named.
- **Verifier:** `experimental/scripts/verify_b_writeup_band_reduction.py`.
- **Certificate:**
  `experimental/data/certificates/b-writeup-band-reduction/b_writeup_band_reduction.json`.

## Statement

Let `H=mu_n` and let `(P,Q)` be a canonical band trade:

```text
P cap Q = empty,
|P| = |Q| = h,
t+1 < h <= floor(log2 n)^2,
e_i(P) = e_i(Q), 1 <= i <= t.
```

Equivalently,

```text
deg(L_P - L_Q) <= h-t-1.
```

The B reduction is a three-exit routing statement for any family of non-v1
canonical band trades.

## Exit 1: Minimal-Subtrade Descent

If a trade contains a size-`t+1` subtrade after deleting bounded tails, then it
belongs to the already measured minimal star-trade layer.  The point is not
that a single subtrade proves the whole band trade small; it gives a descent:
large mass in this exit projects to large mass in the minimal layer, with only
bounded tail choices and the same canonical scaling/orbit quotient.

This exit is therefore consumed by the P-A/H1 minimal-core machinery:

```text
large exit-1 family
  -> many minimal full-fiber trades through bounded tails
  -> active-core accounting / per-core cap.
```

## Exit 2: v1 Pullback Charging

If `L_Q + f` lies in a v1-chargeable pullback linear series, then the family is
charged by the frozen W3 dictionary.  This includes the cyclic and dihedral
pullback cases already present in the census.  The count is not a new
incidence theorem; it is the dictionary product-of-binomials count with the
map orbit and tail data fixed.

So exit 2 is a paid column:

```text
large exit-2 family
  -> one bounded map-orbit family
  -> W3/QA.22-style exact charge.
```

## Exit 3: Primitive Moment/PTE Residue

The dominant observed exit is primitive moment/PTE.  The old correspondence
route does **not** prove this exit: the curves move with `(P,Q)`, so fixed
curve-point theorems do not sum over all cores.

The correct reduction is the X-10 residue.  After anchoring by the scaling
action, a primitive non-toral exit-3 family is bounded by the anchored
non-toral PTE estimate, including its defect/tails version:

```text
anchored_nontoral_pte_bound:
  A_h^nt <= h n

defect/tails wrapper:
  A_{h,B}^nt <= C_{h,B} n.
```

With the old orbit-factor route, this gives the required `<= n^2` scale for
uncharged split pairs.  W4 replaces that local consumption point: exit 3 is now
charged directly to the final row-wise primitive PTE compiler column.  Thus B
still depends on the same residue, but the sufficient bound is the W4 L3
currency

```text
# uncharged split pairs <= n^3 per row
```

rather than the strict anchored `A_h^nt <= h n` form, provided tails are already
included in that final row-wise count or paid separately.

## Census Check

The P-B census routes every checked canonical band trade:

```text
total canonical band-trade orbits: 1016
exit 1 minimal subtrade:             15
exit 2 v1 pullback:                  79
exit 3 primitive moment/PTE:        922
unclassified:                         0
```

The large exit-3 count is the reason this packet is conditional.  It confirms
the routing table but also shows the proof cannot avoid the X-10 non-toral
PTE estimate.

## Conditional Theorem

Assume either the anchored non-toral PTE bound and its defect/tails wrapper, or
the W4 direct-column replacement in final post-strip row-wise currency.  Then
`u1_beta_band_trade_reduction` holds:

```text
every > n^2 non-v1 canonical band-trade family
  either descends to the minimal active-core layer,
  or is v1 pullback-charged,
  or is covered by the anchored non-toral PTE bound.
```

## Verification

Run:

```bash
python3 experimental/scripts/verify_b_writeup_band_reduction.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_b_writeup_band_reduction.py --write-certificate
```

Current replay: **18 PASS, 0 FAIL**.
