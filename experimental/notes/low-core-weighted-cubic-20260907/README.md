# Weighted singular cubics: two remaining lower-strip patterns

```yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: on the exact normalized source for 7117<=J<=8655, N<=274979661292365251 or one of the two printed cubic patterns remains
architecture: DIRECT
atom_or_cell: normalized rank-twelve source class, not an active-v4 owner
quantifier: every source satisfying SOURCE_CONTRACT.md
projection_and_unit: distinct original finite affine slopes
claimed_bound: 274979661292365251 outside the two residual patterns
status: PROVED
impact: LOCAL_ONLY
falsifier: a contract source exceeding this bound and satisfying neither remaining pattern
replay: python3 -B experimental/notes/low-core-weighted-cubic-20260907/replay.py
```

Agent: Codex acting for AllenGrahamHart. Date: 2026-09-07.
This extends the [earlier cubic packet](../low-core-cubic-20260907/README.md)
on the same companion branch. Earlier immutable exports are unchanged.
The local proofs are submitted for independent review, not represented as
accepted upstream results or a banked Grande Finale v4 atom.

## What Changes

Let `N=|Gamma|+134944` under the exact [source contract](SOURCE_CONTRACT.md).
For `7117<=J<=8655`, either

```text
N <= 274979661292365251 < B*=274980728111395087,
reserve = 1066819029836,
```

or all but at most 64 represented LOW pairs lie on the earlier
affine-singular cubic, smooth at its unique point at infinity, with
one of these two patterns:

```text
d=7,  dim Y=3, 1301<=h<=4327;
d=10, dim Y=4,    1<=h<=865.
```

Here `d` is the kernel dimension of the primitive infinity-direction
projection on `V x V`, `h` is its coefficient height, and `Y` is the
full algebraic coefficient locus, not the finite set of selected pairs.
Neither parameter is a raw margin or a trade height. Both patterns
remain unresolved; no full interval or prize row closes.

The [residual proof](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/weighted_cubic_residual.md)
combines the earlier whole-kernel coverage with two new estimates.
The larger paid-alternative constant above must accompany this stronger
restriction; do not attach it to the earlier, smaller numerical bound.

## New Theorems

1. **Weighted singular-cubic incidence.** For a shared s-dimensional
   degree-<K carrier and primitive projection `(A,B)` of height h and
   kernel dimension d, the affine-singular cubic coefficient locus has
   dimension at most `ceil(d/3)`. If its dimension is at most r and
   `Q_h=(n-K-h+1)/(A_agree-K-h+1)>=3`, `A_agree>=K+h`, then

   ```text
   #joint-rich pairs <= floor(2^d * 3^(2s-d-r) * Q_h^r).
   ```

   See the [statement](source/critical/nodes/mca_singular_cubic_weighted_incidence_payment/statement.md)
   and [proof](source/critical/nodes/mca_singular_cubic_weighted_incidence_payment/proof.md).
   Characteristic is zero or `p>3, p>=K`. An elementary finite power
   cover uses weights two and three and retains every component of the
   actual equation locus. Singular pairs and parameter poles are included.

2. **Projection height and exact carrier structure.** For `1<=d<s`,
   `floor((s-1)/(s-d))*h<=K-1`; for `d=s`, `h=0`.
   When `d=s-1`, the entire carrier, not just a chain inside it, is

   ```text
   V=q*span{B^(s-1), A*B^(s-2), ..., A^(s-1)},
   deg q+(s-1)*h<K.
   ```

   The [proof](source/critical/nodes/mca_singular_cubic_weighted_incidence_payment/projection_height.md)
   does not descend the received word to `A/B`. The factor q is nonzero
   on the complete joint-core union only. Its other zeros, all roots of B,
   and their original scalar-defect labels remain in the accounting.

3. **Completed-HIGH resource.** The earlier completed-basis resource
   gives weight at least 5500 for every HIGH record (`raw>=501`), improving
   the common resource/near base to `4194116990084347`. Thus a cubic
   cap M and at most 64 off-curve pairs cost at most

   ```text
   4194116990084347 + 981604*(M+64).
   ```

   The [short proof](source/critical/nodes/mca_singular_cubic_weighted_incidence_payment/completed_high_weight.md)
   uses monotonicity and an eleven-factor Bernoulli estimate, not a scan.
   It pays every constant-infinity-direction affine-singular cubic
   whole-source class on `4801..169999`, with no off-curve exceptions,
   at `N<=268384711205699531`. In the lower strip it also pays d=7
   through h=1300. Failure of the h=1301 expression is not an unsafe
   construction.

## Reading And Replay

The packet contains 132 byte-pinned proof/checker sources, including the
earlier prerequisites. [Provenance](PROVENANCE.md) distinguishes new work
from Hughes's nonuniform resource and the previously posted basis theorem.
[Audit notes](AUDIT.md) identify the high-risk proof steps and verification
limits. The replay runs 35 small checks serially, using only the Python
standard library. It checks arithmetic, guards and hashes, not universal
geometry. Assertions remain enabled in child checks even with an optimized
wrapper. No field-sized enumeration, TeX build or Lean proof is required
or claimed.

Original-row use still requires the actual normalization, exhaustive
original-label coverage and original near allowance at the integration
commit. Active-v4 use additionally needs chronology-correct ownership and
inherited-charge transport. Higher ranks, unrestricted ordinary LIST,
the adjacent safe endpoint and both prizes remain open.

## Compute Requests

None. All replay tasks are tiny local checks. No Modal spending is needed.
