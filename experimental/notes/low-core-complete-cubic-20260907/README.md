# Complete normalized cubic strip for KoalaBear MCA

```yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: every exact normalized source with 4801<=J<=8655 has |Gamma|+134944<=274979661292365251
architecture: DIRECT
atom_or_cell: normalized rank-twelve source class, not an active-v4 owner
quantifier: every source satisfying SOURCE_CONTRACT.md in the stated interval
projection_and_unit: distinct original finite affine slopes, counted once
claimed_bound: 274979661292365251
status: PROVED
impact: LOCAL_ONLY
falsifier: a contract source in this interval exceeding the stated slope bound
replay: python3 -B experimental/notes/low-core-complete-cubic-20260907/replay.py
```

Agent: Codex acting for AllenGrahamHart, 2026-09-07.
Complete local hand proofs, submitted for independent review. This is a
companion to #1175, not a change to its author's branch or a claim of
upstream acceptance. Earlier immutable packets remain unchanged.

## Main Result

The [preceding weighted-cubic packet](../low-core-weighted-cubic-20260907/README.md)
left two possible source families on `7117..8655`. Both now have bounds
below its paid-alternative constant. The [composition proof](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/cubic_strip_payment.md)
therefore establishes, for EVERY source in the [exact contract](SOURCE_CONTRACT.md),

```text
7117 <= J <= 8655:
N = |Gamma|+134944 <= 274979661292365251,
B* - N >= 1066819029836.
```

This adds 1539 integer J-values to the earlier `4801..7116` result.
The combined normalized interval `4801..8655` is covered, without
assuming that the received source already lies on a chosen cubic.
The entire interpolation kernel supplies the exhaustive curve reduction.
Alternative whole-source bounds combine by MAXIMUM, not addition.

Here `d` below is a projection-kernel dimension, not the degree gap or raw
margin; `h` is primitive projection-coefficient height, not trade height.

## Two New Ingredients

1. **Geometric-progression carrier, d=10.** The curve descends to
   `T=A/B`; the receiver need not descend. A four-dimensional coefficient
   family forces one polynomial normalization model covering ALL
   nonsingular bounded pairs, with parameter degree at most three.
   At most five projective T-values need three-element parameter lists;
   all other lists have at most two entries. Keeping original coordinates,
   including `B=0`, gives at most 1251 nonsingular pairs. Smaller coefficient
   dimensions use the weighted bound instead. The whole d=10 source,
   including up to 64 off-curve pairs, satisfies
   `N<=82951498428798039`.
2. **Componentwise polynomial model, d=7.** Centering and dividing the
   gcd of parameter differences makes evaluations vary on each component.
   Polynomial output degree bounds then control constant agreement fibers
   and exceptional three-element lists. There are at most 315 nonsingular
   rich pairs per three-dimensional component. Cubic normalization costs
   degree at least `3^r` on a component of dimension r, giving at most
   `3^16` top components. The weighted degree budget pays the entire
   lower-dimensional complement separately. Including the singular pair
   and up to 64 off-curve pairs gives `N<=73164604161759423`.

Both estimates include the same HIGH resource and the original near
allowance once. Common-factor zeros outside the joint-core union are
retained, as are arbitrary receiver variation and original finite labels.

## Short Reading Path

- Start with [SOURCE_CONTRACT.md](SOURCE_CONTRACT.md) and the
  [full-strip composition](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/cubic_strip_payment.md).
- d=10: [curve descent](source/critical/nodes/mca_geometric_progression_singular_cubic_payment/curve_descent.md),
  [maximal parameter family](source/critical/nodes/mca_geometric_progression_singular_cubic_payment/maximal_parameter_family.md),
  then [original-coordinate counting](source/critical/nodes/mca_geometric_progression_singular_cubic_payment/proof.md).
- d=7: [component model](source/critical/nodes/mca_singular_cubic_component_list_payment/component_model.md),
  [component degree](source/critical/nodes/mca_singular_cubic_component_list_payment/component_degree.md),
  [list envelope](source/critical/nodes/mca_singular_cubic_component_list_payment/component_list.md),
  then [assembly](source/critical/nodes/mca_singular_cubic_component_list_payment/proof.md).
- [PROVENANCE.md](PROVENANCE.md) gives the dependency graph and credits;
  [AUDIT.md](AUDIT.md) identifies review priorities and verification limits.

The source manifest freezes 158 proof/checker files (463144 bytes),
including the prerequisites as well as these new proofs. All 39 serial
checks pass in normal and optimized-wrapper runs; four manifest mutations
are rejected. Measured runs take about three seconds and under 21 MiB RSS.
Arithmetic and hostile controls run serially with the Python standard
library. They are NOT a proof of the universal geometry. No TeX build,
Lean certification, field-sized enumeration or Modal spending is required.

## Remaining Boundary

The unpaid normalized interval is `8656..169999`. Higher original ranks,
exhaustive original-source normalization and near transport, and active-v4
ownership and inherited-charge transport remain separate obligations.
No unrestricted original-row numerator, adjacent safe endpoint, ordinary
LIST bound or prize resolution follows. The local critical roots remain
open. There are no compute requests in this contribution.
