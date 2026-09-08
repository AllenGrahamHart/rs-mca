# Multiplicity interpolation and cumulative margin accounting

~~~yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: every exact normalized source with 4801<=J<=9821 has |Gamma|+134944<=274979661975561635
architecture: DIRECT
atom_or_cell: normalized rank-twelve source class, not an active-v4 owner
quantifier: every source satisfying SOURCE_CONTRACT.md in the printed interval
projection_and_unit: distinct original finite affine slopes, counted once
claimed_bound: 274979661975561635
status: PROVED
impact: LOCAL_ONLY
falsifier: a source satisfying the exact contract and exceeding the stated bound
replay: python3 -B experimental/notes/low-core-multiplicity-cumulative-20260908/replay.py
~~~

**Agent:** Codex acting for AllenGrahamHart, 2026-09-08.
Complete local hand proofs, offered for independent review. The replays
check arithmetic and small algebraic controls, not the universal geometry.

## Contribution

This grouped follow-up to the
[previous cubic packet](https://github.com/przchojecki/rs-mca/pull/1175#issuecomment-5575781509)
contains two reusable proof ingredients and their exact finite application.
The published interval was 4801..8655. The new interval is **4801..9821**:
1166 additional integer J values. No chosen-curve premise is needed.

The [source contract](SOURCE_CONTRACT.md) retains actual carrier dimension
eleven, an empty universal carrier core, canonical maximal-raw selection
over ALL full-code-bad supports and explanations, complete joint cores,
all scalar defects, the original field and distinct finite labels.
These are source hypotheses, not an exhaustive original-row transport theorem.

### 1. Multiplicity interpolation escapes arbitrary curves

For component degrees <=w, at least A joint agreements among n points,
and an irreducible degree-g curve G over F(X), put

~~~text
Phi_w(d) = sum_(i>=0) (i+1)*max(d-i*w,0), with Phi_w(d)=0 for d<=0.
~~~

The characteristic-free [theorem and proof](source/critical/nodes/mca_multiplicity_interpolation_curve_escape/proof.md)
give

~~~text
Phi_w(r*A)-Phi_w(r*A-g*w) > n*binom(r+2,3)
  => at most g*floor((r*A-1)/w) rich polynomial pairs on G.
~~~

Full Hasse multiplicity is imposed in **X,Y,Z**: for r=2 there are FOUR
conditions, not three. Substitution proves repeated roots. Primitive Gauss
division and weighted degree show that not every kernel polynomial can be
divisible by G; plane intersection then counts all rich pairs, including
singular and isolated solutions. No coefficient-height or family-dimension
hypothesis is needed. No giant interpolation matrix is constructed.

The [full-kernel corollary](source/critical/nodes/mca_multiplicity_interpolation_curve_escape/kernel_corollary.md)
also bounds the gcd degree and all off-gcd pairs. On 9527..9821 its cover
has degree <=3, <=256 exceptions and factor weighted degree <2A.
The old simple-point <A height and 64-exception allowance do NOT transfer.

### 2. Keep the entire raw-margin profile

The [completed-basis continuation](source/critical/nodes/mca_core_completed_basis_margin_resource/cumulative_low_weights.md)
proves w(r;g)>=11*min(r,500). For any 1<=T<=500 on the SAME selected
source, let L_t count raw<=t labels and S_t sum their raw margins. Then

~~~text
|Gamma| <= floor(C/(11T) + (1/T)*sum_(t=1)^(T-1) L_t)
         = the same upper bound expressed as
           floor(C/(11T) + sum_(t=1)^(T-1) S_t/[t*(t+1)]),
C = 23067643444721720934.
~~~

The equality is between expressions, not a claim of an attained maximum.
Defect disjointness provides the stronger per-pair raw budget
S_t<=(n-m+t)*M_t when M_t counts every represented pair at that depth.
The [finite application](source/background/nodes/rate_half_mca_cancelled_low_core_relation_payment/cumulative_low_accounting.md)
uses a convex two-endpoint bound to pay the d=7 cubic case through
coefficient height 1600. There is one resource, one original near charge,
and no reuse of a /501-discounted gain in a /5500 ledger.

### 3. Exhaustive finite composition

Put N=|Gamma|+134944.

| Normalized J interval | Bound on N |
| --- | ---: |
| 4801..7116 | 272837082962714299 |
| 7117..8655 | 274979661292365251 |
| 8656..8763 | 274903465748372176 |
| 8764..9526 | 274979661975561635 |
| 9527..9821 | 274778805314695460 |

The [LOW-101 stage](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/low_cutoff_strip.md),
[quartic stage](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/quartic_strip_payment.md)
and [complete cubic tail](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/double_point_cubic_tail.md)
supply the three new rows. Their whole-source alternatives combine by
MAXIMUM, not addition. The uniform reserve is 1066135833452.

For the last row, all cubic types pay at their ACTUAL doubled factor
height and 256 exceptions. A populated factor line with >980 pairs has
a [bounded-degree complement payment](source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/cubic_tail_line_partition.md).
Otherwise lines are small and the existing conic cap pays every remaining
reducible pattern. No arbitrary cubic/quartic family is assumed absent.

## Review And Replay

Start with [REVIEW.md](REVIEW.md), then the two short reusable arguments,
then the finite composition. [PROVENANCE.md](PROVENANCE.md) records
attribution, immutable upstream pins, dependency directions and non-overlap.
The source snapshot is identified by [SHA-256 hashes](SOURCE_MANIFEST.json);
it does not rely on the dirty local worktree's HEAD as a proof identifier.
The [publication replay record](VALIDATION.md) gives measured resource use:
212 frozen sources, 55 serial checks and four rejected manifest mutations.

Run the command above from the repository root. Checks run serially with
a 15-second timeout per child and bytecode writing disabled. The wrapper
retains child assertions even when itself run with Python -O. A separate
256 MiB/60-second RAMguard was used locally. No field-sized enumeration,
CAS, TeX or Lean build, external package, or Modal job is required.

## Limits And Integration

This is a **local source theorem**, not a new active-v4 compiler integer.
Original-source normalization and exhaustive original labels, original
near transport, higher ranks and normalized 9822..169999 remain open.
Active-v4 use additionally requires ownership chronology and inherited
charges. The ordinary LIST problem and both prizes remain unresolved.

The failed sufficient interpolation inequality at J=9822 is NOT an
unsafe-source counterexample. Earlier snapshot frontiers and dated proof
stages are historical; the table above is this packet's assembled scope.
No claim of upstream acceptance, external independent mathematical review,
formal proof certification or literature priority is made.

## Compute Requests

None. These contributions are analytic with small exact arithmetic checks.
