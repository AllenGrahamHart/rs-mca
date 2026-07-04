# Flip packet: rate_half_coverage_gap

- **Node:** `rate_half_coverage_gap`
- **Current critical label:** UNPROVED
- **Verdict:** PROMOTE-PROVED
- **Referee summary:** the statement is exact arithmetic already reproduced by
  `verify_qa3_e14_fm_margins.py`. It has no req children and should not remain
  red.

## Statement

> At prize-max rate 1/2 the exact 2-power quotient-core window undershoots the mean crossing: M_max = 2^33 vs sigma* = 8,592,912,738 leaves 2,978,147 radii that are neither proved-unsafe (quotient windows) nor extras-zero (integrality) — an uncovered band the current mechanisms do not reach. Rates 1/4, 1/8, 1/16 are CLEAN (first open radius margins < -121 at Row C, < -3.4e11 at prize-max). Together with the s* verdict and the thin -12.87 margins, all three wave-1 findings point the same way: RATE 1/2 IS THE BATTLEFIELD; the other three rates look dramatically more closable.

## Req Children

There are no live req children.

## Referee Argument

This is a citation-closure arithmetic node. The verifier recomputes the
quotient-core 2-power windows and prints exactly the quantities in the
statement:

```text
prize rate 1/2:
  M_max = 2^33 = 8,589,934,592
  sigma* = 8,592,912,738
  gap = sigma* - M_max + 1 = 2,978,147 radii
```

For the other prize-max rates the same verifier checks that the proved-unsafe
window overshoots `sigma*` and that the first open radius has large negative
margin:

```text
rate 1/4:  first open radius margin < -4.0066e11 bits
rate 1/8:  first open radius margin < -9.7896e11 bits
rate 1/16: first open radius margin < -3.4070e11 bits
```

For the Row-C clean rates the verifier/note gives first-open margins below
`-121` bits, with the rate-1/2 Row-C case isolated as a one-radius gap. The
same run also records the thin rate-1/2 prize-max integrality mirror:
`LM(sigma*+1) = -12.84` and `ZM(A*+2) = -12.87`, matching the statement's
"thin -12.87 margins" language.

This node therefore has no remaining mathematical content. It should flip to
PROVED by citation to the deterministic arithmetic verifier and its note.

## Evidence Pins

- `rate_half_coverage_gap`: `2202f5b7b9f119ad`

## Verifier

```bash
python3 experimental/scripts/verify_qa3_e14_fm_margins.py
```

Current run: 117 PASS, 0 FAIL, 17 LOUDFLAG findings. The loud flags are the
reported knife-edge and thin-margin facts, not verifier failures.

## Source Quotes

- `qa3_e14_fm_margin_tables.md` Section 6, Finding F6 gives the exact
  `M_max`, `sigma*`, and `2,978,147` gap.
- `q3r5_three_rate_dossier_skeleton.md` Section 7 restates this as the
  rate-1/2 exclusion/residual for the three-rate dossier.
