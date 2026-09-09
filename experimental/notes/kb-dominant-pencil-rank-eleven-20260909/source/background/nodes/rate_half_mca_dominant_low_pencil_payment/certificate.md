# Three Small Outside LIST Certificates And A Reused Source Ledger

No new large artifact is needed. Reuse
../rate_half_mca_low_pair_pencil_payment/certificate/manifest.json,
SHA256 d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d.
Its eight complete JSONL shards contain982 rows and19640 exact LIST steps.
Its hand proof and independent supplier audit remain required.

New exact arithmetic:

    A=67471, J_min=9965, J_max=21499, N0=981106
    e0=211756, e_max=456878
    Johnson(e0,J_max,A)=floor(9735058588/5353)=1818617
    uniform off-pair cap=456878*57507=26273683146
    constant small-complement total=274138707278280353
    constant middle-complement maximum=254493279590417819
    constant large-complement maximum=262886297505008376
    nonconstant total=254037905932250471
    nonconstant e<=250000 total=242763223224476195
    final reserve=842020833114734.

outside_list_caps.json stores three uniform shared-carrier joint-LIST caps
with eleven steps each,33 steps total. K_max=21499 and carrier dimension11:

    e_bar    A_bar    cap
    400000   67471    3146811647
    500000   67471    54886611863
    250000   45973    14781874200.

Each row uses the supplier's corridor (r,w)=(e_bar-K_max,A_bar-K_max).
Dimension steps have degree0; positive-degree steps are Johnson/padding.
Each exact upper is checked directly against the P/S inequalities. There
is no assumption of optimal choice, field search or full-code Johnson
positivity at K_max.

For constant e211757..400000, add981106*3146811647 to each prior E(a,b)
whose box intersects that range. There are190 boxes, maximum in row211.
For e400001..500000, use981106*54886611863:101 boxes, maximum in row400.
Row400 meets both disjoint source intervals. Thus291 branch-box evaluations
use290 distinct old rows. Do not shorten the previous refund/LIST endpoint
b in a clipped boundary box, or floor R0 before multiplying a refund.

verify.py regenerates the33 new chosen steps and uses the previous primary's
exact envelope. verify_audit.py
does not import either primary or the LIST compiler: it checks the pinned
shards and recomputes the whole expression with one common integer
denominator. The prior independent audit separately validates all19640
LIST transitions and the basis certificates. The independent new checker
also rejects nine corrupted outside certificates and three failed Johnson
gates. No finite-field source search or optimality claim is hidden here.
