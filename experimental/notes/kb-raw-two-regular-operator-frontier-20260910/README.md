# K3 / DIRECT: Raw-Two Projection And Regular Operator Frontier

```yaml
workboard_item: K3
row: KoalaBear, q=2130706433^6, n=2097152, k=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: Every deficient generic P2-projection rank12 source in J9965..21499 pays; regular survivors admit dimension-at-most-three operator terminals.
architecture: DIRECT
partition_digest: not applicable to DIRECT
atom_or_cell: DIRECT original-error-rank12 source class, not an active-v4 atom
quantifier: Every such original source and every valid support/minimizing-pair assignment.
projection_and_unit: Distinct original finite bad slopes; auxiliary pairs retain original raw weights.
claimed_bound: 274462040894062110 for deficient P2 projection; no affordable regular-terminal bound asserted.
status: PROVED locally; independent mathematical review due
impact: LOCAL_ONLY
falsifier: A valid source violating a printed source bound, or a regular pair space violating the guarded anchor theorem.
replay: python3 -B experimental/notes/kb-raw-two-regular-operator-frontier-20260910/replay.py
```

This four-node extension follows the [rank18 payment](../kb-source-bound-integer-compression-rank18-20260910/README.md)
at `ff28dfa4`. It continues the source-bound program of Scott Hughes's
#1179/#1180. It does not modify those branches, the stable papers, or any
previously frozen proof. No result here is a Prize or adjacent-row closure.

## What Is New

Let `P2` be the ACTUAL polynomial pairs assigned at least one original
label with raw defect at most two. On the original error-rank12 residual,
the normalized source has `(n,K,m)=(1048576+J,J,67472+J)`, a shared
11-dimensional polynomial carrier, and `9965 <= J <= 21499`.
Auxiliary pair rank is not original error rank.

1. **Raw-two quadratic moving normals are paid.** For independent carrier
   functionals `ell0,ell1` and source-compatible offsets `a0,b0`, put
   `Q(z,h)=ell0(h-a0-z*b0)+z*ell1(h-a0-z*b0)`.
   Pointwise containment of every raw-two label gives whole-source bound
   `252231263277797075`. Formal containment of every represented pair
   line gives `252214244730017023`. Every over-budget assignment has at
   least `34124197250397019` low labels outside EACH declared Q.
   No arbitrary normal cover is assumed.
2. **Every deficient generic P2 projection is paid.** The existing rank18
   payment and proper-carrier payment leave only rank19, shared dimension11,
   and normal degree1. That is precisely a quadratic moving-normal
   hypersurface from item1. The alternative whole-source bounds combine
   by MAXIMUM, `274462040894062110`, not addition.
3. **Full generic projection survives appropriately guarded anchors.**
   For `W subset V x V`, with dimensions `r,s`, `s<r<=2s`, and
   `pi_z(a,b)=a+z*b` onto `V` over `F(z)`, the generic-kernel
   annihilator excludes at most `K+s-r` coordinates. Every retained
   section has dimensions `r-2,s-1` and remains generically onto.
   Joint rank two alone does NOT guarantee this preservation.
4. **Surviving regular sources reduce to small operator enclosures.**
   The same worst-case weighted incidence factors give:

| Actual P2 rank r | Anchors | Terminal pair/shared dimensions | Finite projection-rank drops, at most |
| ---: | ---: | ---: | ---: |
| 19 | 8 | 3 / 3 | 3 |
| 20 | 9 | 2 / 2 | 2 |
| 21 | 10 | 1 / 1 | 1 |
| 22 | 11 | 0 / 0 | 0 |

For t=1,2, retain the original owner weights
`omega_t(f)=sum of original raw values of labels assigned to f with raw<=t`.
A uniform terminal bound L_t transfers as

```text
M_t <= [product_(j=1)^(r-11) (1048576+j)/(67472-t+j)] * L_t.
```

After subtracting an actual terminal pair and dividing only differences
by the anchor locator H_a, some original-field operator T on a
c-dimensional polynomial space U gives the terminal enclosure

```text
(a,b) = (a_*,b_*) + H_a*((I-alpha*T)y, T*y),  c=22-r,
h_gamma = a_*+gamma*b_* + H_a*(I+(gamma-alpha)*T)y.
```

Only represented y and their original labels/weights are counted.
Neither the base pair nor the receiver is asserted divisible by H_a.
The finite chart uses `|F|>c`; scalar, nilpotent and nonsplit operators
are not excluded. The zero-dimensional case has at most one pair and
original weight at most `981104+t`.

**This normal form does not supply an affordable L_t.** In particular,
the dimension-three terminal is not a rank19 payment.

## Reading And Replay

- [Quadratic payment](source/background/nodes/rate_half_mca_raw_two_quadratic_normal_payment/proof.md).
- [Exhaustive deficient-projection payment](source/background/nodes/rate_half_mca_raw_two_projection_regular_frontier/proof.md).
- [Generic regularity-preserving anchor](source/background/nodes/pair_space_regular_projection_anchor/proof.md).
- [Original weighted operator reduction](source/background/nodes/rate_half_mca_regular_operator_terminal_reduction/proof.md).
- [Integration and review map](INTEGRATION.md), [validation limits](VALIDATION.md),
  [complete source/dependency manifest](SOURCE_MANIFEST.json).

From the repository root, offline and serially:

```sh
python3 -B experimental/notes/kb-raw-two-regular-operator-frontier-20260910/replay.py
python3 -B -O experimental/notes/kb-raw-two-regular-operator-frontier-20260910/replay.py
```

There are 38 new frozen sources, 50,656 bytes, with a 107-node required
closure and 313 unchanged inherited mathematical documents. Every
required node is locally PROVED; external mathematical review remains due.
The historical provenance files saying "local" or "no new export" record
their creation state, not the publication status of this frozen packet.

## Remaining Work

Every over-budget assignment in the rank12 gap must have actual P2
rank19..22, full shared carrier and full generic projection. Regular
operator-terminal weights, all 11,535 whole degrees, original error
ranks>=13, exhaustive row coverage and both Prize problems remain open.
All higher original raw labels and near=134944 are retained once in the
stated payments. No active-v4 atom, ordinary-LIST bound, maximal-safe
endpoint, or new unsafe witness follows.

## Compute Requests

None for this contribution. No Modal use, spending, large scan or new
compute request. The next missing input is a proved source-bound terminal
census; enumerating formal operator matrices is not an exhaustive source
bound. Existing unrelated deferred requests are not authorized here.
