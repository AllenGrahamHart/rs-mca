# A Bounded Same-Core Rational Atlas

Agent: Codex acting for AllenGrahamHart, 2026-09-08. Extension of the
existing #1175 companion, relative to `0a573449`. One complete local
hand proof is submitted for independent review. No row payment is added.

~~~yaml
workboard_item: K3
row: KoalaBear MCA, q=2130706433^6, n0=2097152, k0=1048576
object: rank-six polynomial evaluation flats in one fixed LOW core
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: under the all-proper-flat density gate h>(K-4)/7, maximum rank-six flats have full pairwise joins and a bounded injective two-anchor rational atlas
architecture: DIRECT
atom_or_cell: structural source geometry, not an active-v4 owner
quantifier: every actual rank-eleven polynomial carrier and fixed nonzero core satisfying the printed gates
projection_and_unit: flats and rational directions per core; NOT distinct bad slopes
claimed_bound: at most 25 maximum six-flats for J=20481..22999, at most 17 for J=22500..22999; rational component degrees at most 3284
status: PROVED locally; external independent review remains due
impact: LOCAL_ONLY
falsifier: a same-core flat family satisfying all printed hypotheses but violating the packing bound or strict-root rational conclusion
replay: python3 -B replay.py --atlas-only; python3 -B -O replay.py --atlas-only
~~~

## The Proved Statement

Let `V <= F[X]_(<K)` have actual dimension eleven, `K>=26`, and let H
contain `M>K` distinct points with all V-evaluations nonzero. Let h be
the maximum coordinate density over ALL proper evaluation flats of H,
and suppose `h>(K-4)/7`. A complete maximizing rank-six flat has
`a=6h` points. The family can be empty.

Distinct such flats A,B span the full evaluation carrier. Their
subspace intersection has rank one, so `|A intersect B|<=h`. Cauchy
packing in this SAME H gives

~~~text
L <= 5M/(36h-M), provided 36h>M.
~~~

Write W_A for the five-dimensional annihilator in V, P_A for the full
locator of A, and U_A=W_A/P_A. Fix two flats A,B. Their annihilators
have zero intersection and sum to a ten-space U. For any further C,
`d_C=dim(W_C intersect U)` is four or five. There is a coprime pair
of nonzero polynomials `(f_C,g_C)` and a d_C-dimensional multiplier
space T_C such that

~~~text
W_C intersect U = (P_A*f_C + P_B*g_C)*T_C,
f_C*T_C <= U_A,  g_C*T_C <= U_B,
deg f_C, deg g_C <= K-6h-d_C.
~~~

Different C give different projective rational directions `[f_C:g_C]`.
The mechanism is an exact polynomial identity, not a numerical fit:
each cross determinant vanishes on `C outside (A union B)`, and the
strict root count forces it to vanish identically. A direction then
lies in two fixed normalized annihilator spaces instead of an unrelated
space for each C.

If G_C is the monic gcd of T_C, the full locator obeys

~~~text
P_C divides (P_A*f_C + P_B*g_C)*G_C.
~~~

G_C cannot be deleted. The actual F_1201 fixture includes a root of
G_C that is not a root of the primitive polynomial in parentheses.

The [complete statement](source/background/nodes/mca_rank_six_maximum_flat_rational_atlas/statement.md)
also gives the three-flat lemma without maximal-density assumptions:
pairwise full joins and `|C outside (A union B)|>2K-|A|-|B|-2` suffice.
The [self-contained proof](source/background/nodes/mca_rank_six_maximum_flat_rational_atlas/proof.md)
includes root capacity, packing, coprimality, degree bounds and injectivity.

## Finite Scope And Near-Maximum Band

For `K=J`, `M=J+67466`, the decreasing envelope is

~~~text
5M/(36h-M) < 35(67466+J)/(29J-7*67466-144).
~~~

Its endpoint values lie strictly between 25 and 26 at J=20481, and
between 17 and 18 at J=22500. Thus the integer family caps are 25 and
17 on the intervals above. The component degrees are at most 3284.
These are proved upper bounds, not optimality claims for these constants.

The robust extension covers ALL complete rank-six flats of size at least
an integer b when `6<=b<=6h` and `2b-5h>K-4`. They have the same rational
structure and their OWN packing bound

~~~text
L <= M(b-h)/(b^2-Mh), provided b^2>Mh.
~~~

The maximum-family caps 25/17 do not automatically apply to this larger
band. The statement does not cover every vaguely near-dense flat.

## Why This Helps, And What It Does Not Prove

This gives shared algebraic structure at the dense rank-six bottleneck
in the current basis-count route. The F_193 fixture has three maximizing
six-flats but singleton projective evaluation fibers, so the structure
is not merely the previously exported large-fiber/secant situation.
The next step is to use these fixed annihilators to improve a basis
count or price selected records on one source resource.

Different bad labels can have different cores and different anchors.
Multiplying a child payment by 17 or 25 is NOT justified. The positive
packing denominator generally fails if M is replaced by the full
original domain size. Rank-one through rank-five maximizing flats,
flats outside the explicit band, and varying-core ownership remain due.

The atlas is a separate one-node PROVED inventory with an evidence-only
connection to the local rank/support-distance router. It is NOT in the
65-node paid-interval assembly or the separate nine-node scalar inventory.
No requirement edge or mathematical status changes in this publication.
The unrestricted rank-twelve residual stays **J=9941..22999**; no complete
degree is removed and the main cap **274979661975561635** is unchanged.
Higher original error ranks, ordinary LIST and both Prize problems remain open.

## Audit And Provenance

The hand review checks the proper-join contradiction, positive-denominator
Cauchy step, full-locator quotient spaces, strict root count, rational
direction injectivity and retained gcd roots. Elementary flat geometry
and polynomial root methods are antecedents; no general literature
novelty is claimed. This does not import or claim Hughes's earlier
rank/near and incidence results as a new theorem.

The primary checker uses four tiny actual-field controls, including the
indispensable gcd root and a counterexample to omitting the strict-root
gate. It also checks 87 near-maximum gates. The independent checker uses
integer endpoint inequalities and 1695 small set families, without the
primary implementation or Fraction. These are controls of a hand proof,
not field-wide computational certification or external peer review.

All eight proof/control files are frozen byte-for-byte from the local
PROVED node. All 637 parent sources are unchanged. The current manifest
has 645 sources; [provenance](PROVENANCE.md) records its digest and dirty
source custody, and [validation](VALIDATION.md) records the bounded replays.
The collision-interval prototype and the newer root-moment/Bonferroni
packets are excluded: their proposed finite interval has not completed
its independent audit and original-source assembly.

No computation request, Modal use or spending is needed for this contribution.
