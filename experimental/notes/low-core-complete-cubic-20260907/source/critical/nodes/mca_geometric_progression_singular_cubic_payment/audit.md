# Audit And Provenance

Status: PROVED local hand argument, 2026-09-07. Independent external
mathematical review remains due. Numerical checks are not that review.

The previous turn exported weighted-cubic commit
`f4379ee656a12ac80a27c44d0c582fe81c81e352`, comment 5575191028 on
#1175. This new theorem is NOT in that immutable packet. It is a later
direct mathematical advance. Canonical Fable remains read-only at
`0dd5b324482194208be0289f76ed3f0817648a46`. Main and open #1175 were
freshly checked at `93fba1be3f3299b0ba4708d88715377bbb656e45` and
`6c59f9aa75b897c9274e94c7aa8864acd26a85ea`. No upstream adoption
or banked active-owner atom follows.

## Hand Review

- The geometric-progression identity describes ALL of V. Its coefficient
  isomorphism retains the actual degree-ten cap. Curve descent uses a
  function-field basis that remains independent after constant extension.
  Dimension four refers to the full algebraic locus, not sampled F-points.
- Root-ball classes are all retained initially; their number is not
  assumed small. Negative valuations use floor, not truncation. A full
  four-dimensional coset forces the leading coefficient to be a cube up
  to a constant. Monicity then removes poles from EVERY other nonsingular
  parameter, not merely the component used to find that coset.
- The moving leading coefficient -c*T in the second output rules out
  parameter degree >=4 by strict degree comparison. This covers all
  coefficient components. The possible singular pair is counted separately.
- The infinity fiber is computed by degree-ten output/degree-three
  parameter homogenization. The cubic vector never vanishes, and at most
  five projective fibers need lists of size three instead of two.
- Lists belong to original coordinates and may vary within a projection
  fiber. q roots outside cores and B roots are retained. The field size
  and original slope labels never change.
- The coefficient dimension <=3 branch uses the older weighted count;
  its larger total, not the dimension-four bound, is the uniform d=10
  result. Exactly one singular pair, <=64 off-curve pairs, one HIGH
  resource and one original near allowance are charged as applicable.

## Checks

`verify.py`: exact two-interval Fraction bounds, PASS, 0.07 seconds,
11392 KiB maximum RSS. `verify_audit.py`: independent integer Cauchy
boundaries, negative valuation residues, finite double/infinity triple
fibers over F_7 and projection collisions over F_17, PASS, 0.01 seconds,
10496 KiB RSS. A draft typo in the smaller-dimensional pair cap was
corrected to 80233354159 before manifest registration.

These are tiny stdlib checks, not field-sized enumeration or computer
algebra. No Modal use, spending or new compute request. DAG registration
and diagnostic comparison are recorded in the cycle record. Existing
global errors are not claimed fixed.

The general proof uses the weighted supplier's attributed nonuniform
margin/basis and jet inputs. Valuation-ring facts are linked at their
exact use in `maximal_parameter_family.md`. The new curve-descent,
maximal-family and original-coordinate list arguments are supplied here
in full. Original-row normalization and active-owner add-back remain
separate integration obligations.
