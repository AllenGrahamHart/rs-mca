# Original HIGH44 Pays Two Further Low-Pair Rank Cases

```yaml
workboard_item: K3
row: KoalaBear, F_(2130706433^6), smooth domain n=2097152, k=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
architecture: DIRECT
atom_or_cell: original error-rank-twelve source classes, J9965..21499
quantifier: every received line and valid original assignment in the printed classes
projection_and_unit: distinct original affine bad slopes, near included once
status: PROVED LOCAL; independent mathematical review due
impact: LOCAL_ONLY; two more pair-rank source classes exhausted
falsifier: a valid declared source violating the original ownership or whole-source bound
replay: python3 -B experimental/notes/kb-high44-pair-rank-extension-20260910/replay.py
```

This two-node companion to #1175 extends the
[deficient-projection packet](../kb-low-pair-projection-frontier-20260910/README.md).
It uses the already proved original HIGH44 resource to strengthen the
pencil-section bounds and then pay two further actual pair-rank cases.
No new conjectural premise, covering assumption or large computation is used.

## Main Theorem

Start with a complete original post-near error-rank-twelve selection.
Normalize only its complete original shared scalar core of size g and set
J=1048576-g. On 9965<=J<=21499 the unchanged-field source has

    (n,K,m)=(1048576+J,J,67472+J), dim V=11,
    h_gamma in h_*+V, original universal carrier core empty.

Fix any valid original scalar-agreement and minimizing-pair assignment.
The defect raw is its ORIGINAL second-component mismatch count. Write
P_t for the ACTUAL represented polynomial pairs assigned a label with
raw<=t. Affine rank below means the dimension of aff(P_t), not the
original error rank and not the number of arbitrary points of that hull.

**Theorem.** Each of the following hypotheses bounds the ENTIRE original
bad-slope set, including every higher-defect label and near=134944 once:

| Sufficient condition, with the empty family included | Bad-slope cap | Reserve below B* |
| --- | ---: | ---: |
| aff(P7) has dimension at most 16 | 261996525491320703 | 12984202620074384 |
| aff(P23) has dimension at most 17 | 270933399088173359 | 4047329023221728 |

These are NOT assertions that P2 affine rank 16 or 17 is paid. They are
two different low-defect family conditions. Whole-source alternatives
combine by MAXIMUM, never by adding their budgets or reserves.

## Two Proof Nodes

1. [Complete low-pair pencil unions](source/background/nodes/rate_half_mca_high44_pencil_union_payment/proof.md).
   For a primitive pencil A0*a+A1*b=Q, let U be the union of COMPLETE
   joint cores of ALL P43 pairs on the pencil and set e=n-|U|.
   A constant direction with e<=567500 pays the entire source by
   261996525491320703. For nonconstant height h, put
   ell=1+2000*floor((h-1)/2000). If e<=441382-8*ell, the source pays by
   110665369786278512. The eleven bands cover all 1<=h<J.
2. [Pair-rank sixteen/seventeen payment](source/background/nodes/rate_half_mca_low_pair_rank_sixteen_seventeen_payment/proof.md).
   Outside those already paid classes, five or six shared-carrier anchors
   reduce to equality children of pair/shared dimension 6/6 or 5/5.
   Both terminal direction ranks are priced, and the same original
   resource funds every other label. This proves the table above.

The pencil proof is split into
[constant directions](source/background/nodes/rate_half_mca_high44_pencil_union_payment/constant_union.md),
[nonconstant directions](source/background/nodes/rate_half_mca_high44_pencil_union_payment/nonconstant_union.md),
and [hereditary section bounds](source/background/nodes/rate_half_mca_high44_pencil_union_payment/hereditary_sections.md).
The complete original core union is fixed throughout every affine child.
For 1<=t<=43 these give scalar bounds C_t^v or P_t^v, where

    C_t=481076/(67473-t),
    P_t=max(9,607203/(67474-t)).

For t=7, q=16 and for t=23, q=17, set

    H_t=1027079/(45975-t),
    M_t=prod_(c=1)^(q-11) (1048576+c)/(67472-t+c)
                     *max(C_t^(22-q), H_t*P_t^(20-q)).

The rank-TWO terminal dominates for t=7, but the CONSTANT terminal
dominates for t=23. Neither may be silently dropped. The pair-cap floors
are 132933633906 and 260482505691, respectively. Keeping the rational
M_t until the final floor gives the no-large-pencil source price

    floor(W0/(t+1)+t/(t+1)*(981104+t)*M_t)+134944,
    W0=624373932788019251.

This is 192166560782635999 or 270933399088173359. Taking the maximum
with the alternative whole-source pencil bound gives the main theorem.

## Review Priorities

- The constant-direction refund applies to ALL retained original records,
  including off-pencil and high-defect records. It uses the exact rational
  Q(9965), not floor Q(9965), before multiplication by the refund factor.
- For one pair, original defect sets of its different labels are disjoint.
  Off-pencil owners cost at most (43/44)*(n-|H_f|) per pair. The smaller
  pencil-union complement e is valid only for on-pencil nonpreferred owners.
- Every anchor has s<r<=2s. Earlier anchor zeros are included in the bad
  evaluation count, and no assumption that later children stay rank two
  is made. At r=s, full-carrier rigidity makes rank-one directions constant.
- Only auxiliary LIST instances are padded or restricted. The original
  source, field, degree, raw values and label ownership are unchanged.

## Integration And Remaining Frontier

This is a K3 / DIRECT source-class result, not an active Grande Finale v4
atom or a payment transferred from a separately normalized residual.
It can be integrated as two lemmas following the original HIGH44 resource
and shared-carrier/projection results. The manifest names the full required
sub-DAG, including already published supplier proofs.

Together with the preceding deficient-projection theorem, EVERY assignment
on an over-budget source must now have P7 affine rank 17..22 and P23
affine rank 18..22. Both projections are generically full. There are at
most 5 and 4 exceptional finite rank-drop slopes, respectively. These are
statements about the actual pair families' affine hulls, not a claim that
every hull point is a realized bad explanation.

No entire J value is removed from the 11535-degree gap. The remaining
pair ranks, original error ranks>=13, active null atoms, unrestricted safe
endpoint, ordinary LIST problem and both Prize problems remain open.
The newer experimental polynomial-envelope work is NOT part of this packet.

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) freezes 22 source files,
90959 bytes, a 97-node locally PROVED required closure and 283 inherited
mathematical documents. See [validation and limits](VALIDATION.md).
Upstream main remains 93fba1be3f3299b0ba4708d88715377bbb656e45 and #1175
is open at 6c59f9aa75b897c9274e94c7aa8864acd26a85ea. This extension starts
at companion commit 1108726d01f96585a2e229fe1f6d2ab9ad77a82c; it does
not modify the author's branch, earlier packets or stable papers.
