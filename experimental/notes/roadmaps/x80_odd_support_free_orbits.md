# X80: odd-support free scaling orbits

- **DAG node:** `x80_odd_support_free_orbits`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved h=5 orbit bookkeeping.
- **Verifier:** `experimental/scripts/verify_x80_odd_support_free_orbits.py`.
- **Certificate:**
  `experimental/data/certificates/x80-odd-support-free-orbits/x80_odd_support_free_orbits.json`.

## Statement

Let `n=2^s` and `H=mu_n`.  If `A subset H` has odd cardinality, then its
multiplicative stabilizer inside `H` is trivial:

```text
{gamma in H : gamma A = A} = {1}.
```

In particular, for h=5 every ordered pair `(P,Q)` of disjoint h-supports has
free scaling orbit:

```text
|H . (P,Q)| = n.
```

If `N_ord` is the full ordered row count and `N_anchor` is the ordered count
with `1 in P`, then

```text
N_ord = (n/h) N_anchor.
```

For unordered h=5 pairs, the only possible nontrivial stabilizer is the
antipodal swap:

```text
P <-> -P.
```

## Proof

Let `K` be the stabilizer of `A`.  Since `K` is a subgroup of the cyclic
2-group `H`, its order is a power of two.  If `K` is nontrivial, every
`K`-orbit in `H` has even size `|K|`; because `A` is `K`-stable, it is a
disjoint union of such even orbits.  That makes `|A|` even, contradiction.

Thus every odd support has trivial stabilizer.  For an ordered h=5 pair,
any scaling fixing the ordered pair fixes `P`, so it is trivial.  Hence the
ordered pair orbit has size `n`.

Each ordered orbit has exactly `h` anchored representatives with `1 in P`:
for every `p in P`, the unique scaling `p^{-1}` sends `p` to `1`, and the
trivial stabilizer makes these `h` representatives distinct.  Therefore

```text
N_anchor = (h/n) N_ord,
```

which is the displayed conversion.

For unordered pairs, a nontrivial stabilizer cannot fix `P` and `Q`
separately.  It must swap them.  If `gamma P=Q` and `gamma Q=P`, then
`gamma^2 P=P`; by the odd-support freeness just proved, `gamma^2=1`.  In a
2-power cyclic group the unique nontrivial element of order two is `-1`.
Thus the only unordered nontrivial symmetry is

```text
Q = -P.
```

## Consequence for h=5

X78 and X79 move the h=5 residue into 10-support square-shift and obstruction
norm-gate currency.  X80 fixes the orbit bookkeeping around that residue:

- ordered h=5 pair mass has no hidden stabilizer denominator;
- anchored ordered h=5 mass converts to row count by exactly `n/5`;
- if an unordered 10-support has symmetry, it is exactly the antipodal-swap
  branch and not an additional scaling family.

This is useful because the terminal compiler consumes row-wise ordered mass,
while many h=5 probes naturally anchor one point in the first support.

## Replay

The verifier exhaustively checks odd-support stabilizers on small rows:

```text
n=16, h=1,3,5
n=32, h=3,5
```

It also verifies the antipodal unordered h=5 example at `n=16`, and checks the
exact conversion identity

```text
h * N_ord = n * N_anchor
```

for `n=16,32,64`, `h=5`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x80_odd_support_free_orbits.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x80_odd_support_free_orbits.py --write-certificate
```
