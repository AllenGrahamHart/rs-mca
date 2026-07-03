# F4: characteristic-p switch-net hunt

- **DAG node:** `u1_pullback_dichotomy`.
- **Task:** F4.
- **Status:** EVIDENCE / NEGATIVE-CLEAN.  U1 survives this attack at the
  checked toy rows; this is not a proof of U1.
- **Verifier:** `experimental/scripts/verify_f4_switch_net_hunt.py`.
- **Certificate:**
  `experimental/data/certificates/f4-switch-net-hunt/f4_switch_net_hunt.json`.

## Attack Model

The frozen v1 dictionary deliberately excludes unbounded map-orbit counts.
The F4 residual attack asks whether small-characteristic rows contain many
pairwise disjoint ordered gadgets

```text
(P_i, Q_i),      |P_i| = |Q_i| = h,      P_i cap Q_i = empty,
```

with identical nonzero moment defects

```text
Delta_i(r) = sum_{x in P_i} x^r - sum_{x in Q_i} x^r,      1 <= r <= t.
```

In characteristic `p`, any `p` gadgets with the same defect cancel together.
Thus `R` disjoint identical-defect gadgets generate `C(R,p)` same-top-`t`
switches.  The v1 harness is threatened only when

```text
C(R,p) > n^2
```

and the family is not explainable by at most `floor(log2 n)` domain-stabilizer
orbits.

## Checked Rows

The verifier uses exact finite-field arithmetic and exact disjoint-family
packing.  It includes prime-power small-characteristic rows, since those are
the danger regime for `p`-fold cancellation:

```text
F8/mu7      t=3, h=1,2
F9/mu8      t=3, h=1,2,3
F16/mu15    t=3, h=1,2
F25/mu24    t=3, h=1,2
F27/mu26    t=3, h=1,2
F49/mu48    t=3, h=1      (Dickson/wild control)
F81/mu80    t=3, h=1
```

## Result

No checked cell contains a v1-uncharged dangerous switch-net:

```text
dangerous families with C(R,p) > n^2: 0
uncharged dangerous families:          0
```

The only `p`-switch classes found are capacity-limited:

```text
F16/mu15, h=2: 255 p-switch defect classes, max R = 3
F27/mu26, h=2: 728 p-switch defect classes, max R = 6
```

These do not threaten the frozen test:

```text
C(3,2)  = 3   <= 15^2
C(6,3)  = 20  <= 26^2
```

The danger-capable singleton rows are rigid:

```text
F25/mu24, h=1: threshold R = 12, max R = 1
F49/mu48, h=1: threshold R = 14, max R = 1
F81/mu80, h=1: threshold R = 35, max R = 1
```

## Interpretation

The characteristic-`p` switch-net template was the sharpest known way to break
the v1 compression dictionary by forcing many independent map orbits.  In the
checked small-characteristic prime-power toys, the template does not produce
any family large enough to exceed the `n^2` survivor allowance.

This supports the next U1 step: prove compression against grammar v1.  The
result should not be promoted as a theorem; it is a reproducible red-team
failure for the switch-net attack surface.

## Verification

Run:

```bash
python3 experimental/scripts/verify_f4_switch_net_hunt.py
```

To refresh the pinned certificate:

```bash
python3 experimental/scripts/verify_f4_switch_net_hunt.py --write-certificate
```
