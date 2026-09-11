# K3 / DIRECT: Receiver-Conditioned Original-Source Bounds

```yaml
workboard_item: K3
row: KoalaBear, F_(2130706433^6), n=2097152, k=1048576
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: entire original bad-slope source bounded under each printed receiver condition
architecture: DIRECT
partition_digest: not applicable to this direct source theorem
atom_or_cell: DIRECT
quantifier: every original error-rank12 fixed-frame source satisfying the selected condition
projection_and_unit: distinct original finite bad slopes, not supports or polynomial pairs
claimed_bound: exact integers in the table below, all strictly below B_star
status: PROVED locally at the printed scopes; external mathematical review due
impact: LOCAL_ONLY; source-class coverage, not an active-v4 atom or unrestricted row closure
falsifier: a valid original source satisfying one printed condition but exceeding its stated bound
replay: replay.py normal and optimized; immutable source pins in SOURCE_MANIFEST.json
```

## Results

This grouped extension adds four whole-source results and two reusable
colour lemmas to the existing #1180 review discussion. It complements the
[rank/projection contributions](../kb-raw-one-rank-nineteen-source-tail-20260911/README.md);
none of the four new consumers requires a P1/P2 pair-rank or projection bound.

All rows below apply on the ENTIRE normalized degree interval
`9965 <= J <= 21499`, containing 11535 integers. The original error
rank is twelve and the fixed shared carrier has dimension eleven.
[The source contract](SOURCE_INTERFACE.md) is part of every row.

A receiver-colour class is defined using a nonzero projective evaluation
fibre of that fixed carrier AND the normalized received pair.
`sigma_t` counts coordinates in classes of size at most `t`;
`b=sigma_1`; `e_43` counts coordinates in classes larger than 43.
These are coordinate counts, not numbers of classes.

| Original receiver condition | Entire source upper bound | Reserve below B* |
|---|---:|---:|
| Nonsingular F(X)-conic of weighted degree <=2J, at most 276035 exceptions | 274980278712737789 | 449398657298 |
| sigma_43 <=53067 | 274978354983575055 | 2373127820032 |
| All class sizes <=2, b<=1717 | 274979228268047446 | 1499843347641 |
| All class sizes <=43, b<=1465 | 274977964220092532 | 2763891302555 |
| All class sizes <=286, b=0 | 274980091354143171 | 636757251916 |
| e_43<=3000, b<=824 | 274980301923454583 | 426187940504 |
| e_43<=4639, b=0 | 274979909180000584 | 818931394503 |

Each is a theorem about the entire original source, not a separately
additive charge for a subfamily. Whole-source alternatives compose by
taking their MAXIMUM over the covered cases, never by summing their budgets.
Their union is NOT proved exhaustive.

## Reusable Content

The canonical-colour lemma places every small complete defect in a
small whole colour class. It restricts the available independent tuples
and charges zero-evaluation labels globally.

The trimmed-profile basis lemma contracts complete fibres INSIDE an actual
joint core. It retains the actual mass of large classes instead of charging
every core point at the largest class size. Its minimizing allocation is
a lower relaxation, not a claimed realizable core.

Together with the proportional-normal tuple count, these give an exact
pointwise source inequality for EVERY actual profile. Its value need not
fit the Prize budget. The sparse-heavy result is a proved finite
application of this stronger inequality, not a universal profile theorem.

## Review And Replay

Start with [INTEGRATION.md](INTEGRATION.md) and
[SOURCE_INTERFACE.md](SOURCE_INTERFACE.md).
[DEPENDENCIES.md](DEPENDENCIES.md) links the six new roots and all inherited
proof documents in their 22-node green required closure.
[VALIDATION.md](VALIDATION.md) separates proof obligations from finite checks;
[PROVENANCE.md](PROVENANCE.md) records custody and overlap limits.

```sh
python3 -B experimental/notes/kb-receiver-conditioned-source-bounds-20260911/replay.py
python3 -B -O experimental/notes/kb-receiver-conditioned-source-bounds-20260911/replay.py
```

The replay is offline and serial, uses the Python standard library, and
requires no installation, Modal, or original-field enumeration. Run from
a checkout containing this packet and its pinned earlier packets.

## Remaining Scope

Remaining sources may fail every listed condition. Singleton-rich and
mixed-concentration profiles are not eliminated. A recipe exceeding
budget at an adjacent parameter is NOT an unsafe source or an optimality
certificate. Higher original error ranks, ordinary LIST, active-v4
ownership/atoms, the adjacent safe row and BOTH Prize problems remain open.
No deployed row integer or maximal-safe endpoint moves.

## Compute Requests

None. The replay is small and serial; no large computation is proposed.
