# QF.12 + QF.13 — F-termination foundations: the support-lattice accounting identity and the MDS corollary

- **Status:** PROVED (full proofs written inline) for every numbered
  statement below — Lemmas 1, 2, 3, 5, 6, 7, Theorem 4, Corollary 4.6,
  Proposition 8, Corollary 9. AUDIT for the framework-alignment remarks
  (SS0.4, SS8): this note PINS its own descent procedure; the in-flight
  QF.6/QF.7 conventions are reconciled at integration, not assumed.
  Nothing here is heuristic; no external citation is load-bearing
  (standard coding facts are re-proved inline).
- **Verifier:** `experimental/scripts/verify_qf12_qf13_support_lattice.py`
  — deterministic, stdlib-only, exact arithmetic over `F_17`; 31/31 PASS
  at this writing. Key numbers quoted in SS7.
- **DAG nodes:** `f_support_lattice` (QF.12), `f_termination_mds` (QF.13).
  Queue: `execution_queue.md` Tier D2. Parents/context: Conjecture F as
  installed in `proof_sketch/s3b_iii_3` SS1-2; Tier F2 (QF.6 dual-code
  frame, QF.7 descent step — in flight upstream); E9/E17 census packets.

## 0. Pinned notation and the descent framework

### 0.1 Objects

Fix a prime power `q` and a set `H` of `n` distinct points of `F_q^*`
(Conjecture-F semantics: `H = mu_n`, the roots of `X^n - 1`; **no group
structure on `H` is used anywhere in this note** — only distinctness).
For `T subset H` write `ell_T = prod_{x in T} (X - x)`.

**Flat (monic, degree `d`, evaluation set `E`).** A pair `(P, E)` with
`E subset H` and `P = f_0 + V` a nonempty affine subspace of monic
degree-`d` polynomials over `F_q`; the direction space `V` is a linear
subspace of `F_q[X]_{<= d-1}` (differences of monics). Set
`dim P := dim V` and the **budget** `beta(P) := d - dim P`. Since
`dim V <= d`, always `beta(P) >= 0`.

**Members.** `M(P, E) := {f in P : f = ell_R for some R subset E, |R| = d}`
— the squarefree members split over `E`. For Conjecture F
(`s3b_iii_3` SS1): `E = H`, `d = j`, and `#M(P, H) = #(P cap D_j)` is the
quantity the fiber/plane bounds need.

### 0.2 Dual codes and sparse supports

For a flat `(P, E)`:

```text
C_dir(P,E)  := { (g(x))_{x in E} : g in V }          the direction code;
Ann(P,E)    := { u in F_q^E : sum_{x in E} u_x f(x) = 0  for ALL f in P }
                                                      the affine annihilator.
```

**Lemma 0.1.** `Ann(P,E) = C_dir^perp cap (ev_E f_0)^perp`; in particular
`Ann subset C_dir^perp`, of codimension `<= 1`.
*Proof.* If `u in Ann` then for `g in V` both `f_0` and `f_0 + g` lie in
`P`, so `sum u_x g(x) = 0`; and `sum u_x f_0(x) = 0` directly. Conversely
both conditions give `sum u_x (f_0 + g)(x) = 0` for all `g in V`. QED

**Sparse supports at threshold `r`.**
`S_r(P,E) := { supp(u) : 0 != u in Ann(P,E), wt(u) <= r }` and
`W_r(P,E) :=` the inclusion-minimal elements of `S_r(P,E)`. Every
`T in S_r` contains some element of `W_r`. Note minimal supports cannot
be nested (an annihilator word supported strictly inside another minimal
support would contradict minimality).

### 0.3 The (a)/(b) split this note formalizes

Given a sparse word with support `S`, the descent splits members into
(a) those whose root set contains `S` — they share the divisor `ell_S`
and descend to a smaller instance — and (b) those missing `>= 2` points
of `S` (Lemma 1 shows "missing exactly one" is impossible). Iterating
(a) naively yields a binary tree of depth up to `n`, hence the standing
`2^depth` objection against F-termination. Theorem 4 defuses it.

### 0.4 Alignment remark [AUDIT]

QF.6 (`f_dual_distance_frame`) and QF.7 (`f_sparse_descent_step`) are in
flight in parallel PRs and their exact conventions are not in this
worktree. This note is self-contained: every object above is defined
here and every claim proved against THESE definitions. Two deliberate
choices to flag for reconciliation: (i) the descent processes words of
the AFFINE annihilator `Ann` (the dichotomy needs the relation to hold
on the flat, not merely on directions); (ii) leaf counting via full
`r`-wise uniformity is stated for `C_dir^perp` (Remark 5.2 records the
gap between the two duals honestly). Direction-dual words `u` with
`sum u_x f(x) = c != 0` on the flat give a "pinned-value" variant (a
member nonzero at exactly one point of `S` has that value FORCED to
`c/u_x`); it is not needed here and is left to QF.14.

## 1. The dichotomy (closure) lemma [PROVED]

**Lemma 1.** Let `(P, E)` be a flat and `0 != u in Ann(P,E)` with
`supp(u) = S`. Then NO `f in P` has exactly one nonzero value on `S`.
Consequently every member `f in M(P,E)` satisfies exactly one of:

```text
(a)  S subset root(f)          (f vanishes on all of S), or
(b)  f is nonzero on >= 2 points of S  ("misses >= 2 points of S").
```

If `|S| = 1`, say `S = {x}`, case (b) is empty: every `f in P` vanishes
at `x` (a forced root).

*Proof.* For `f in P`: `sum_{x in S} u_x f(x) = 0` with `u_x != 0` for
all `x in S`. If `f` vanished on `S \ {y}` only, the sum collapses to
`u_y f(y) = 0`, forcing `f(y) = 0` — contradiction. QED

## 2. The descent step [PROVED]

**Lemma 2.** Let `(P, E)` be a monic flat of degree `d`, and
`0 != u in Ann(P,E)`, `S := supp(u)`, `w := |S|`. Put
`P^S := {f in P : f|_S == 0}` and, if `P^S` is nonempty,
`P_S := { f / ell_S : f in P^S }` with evaluation set `E \ S`. Then:

```text
(1) (when P^S is nonempty)  codim_P(P^S) = dim ev_S(P) <= w - 1;
(2) (P_S, E \ S) is a monic flat of degree d - w  with
    dim P_S = dim P^S >= dim P - (w - 1);
(3) beta(P_S) <= beta(P) - 1   (and beta >= 0 holds at every instance);
(4) f -> f/ell_S is a BIJECTION
    { f in M(P,E) : S subset root(f) }  ->  M(P_S, E \ S).
```

*Proof.* (1) The affine map `f -> f|_S`, `P -> F_q^S`, has image inside
the hyperplane `U := {t : sum_{x in S} u_x t_x = 0}` (that is what
`u in Ann` says), so the image is an affine subspace of dimension
`<= dim U = w - 1`; `P^S` is the fiber of `0`, and fibers of an affine
map onto its image have codimension `= dim(image)`.
(2) Every `f in P^S` vanishes at the `w` distinct points of `S`, so
`ell_S | f`; division by the fixed monic `ell_S` is linear and injective
on multiples of `ell_S`, so `P_S` is an affine flat, monic of degree
`d - w`, with `dim P_S = dim P^S`.
(3) `beta(P_S) = (d - w) - dim P^S = beta(P) - w + dim ev_S(P)
<= beta(P) - w + (w-1) = beta(P) - 1`. Nonnegativity is SS0.1.
(4) A member with `S subset root(f)` lies in `P^S`; `f/ell_S` is monic
of degree `d - w`, squarefree, split over `E \ S`, and lies on `P_S` —
a member of the child. The inverse is `g -> ell_S * g` (which lands in
`P^S` by definition of `P_S`, and is a member: its root set is the
disjoint union `S cup root(g) subset E` of `d` distinct points). QED

## 3. The two descent procedures, pinned; state determinism [PROVED]

Fix a sparseness threshold `r >= 1` and the **canonical order** on
supports: `S < S'` iff `(|S|, sorted tuple of S)` is lexicographically
smaller. For a forced-root set `A subset E` define the **instance**

```text
Inst(A) := ( (P cap {f : f|_A == 0}) / ell_A ,  E \ A ),
```

(possibly the empty flat), and `W(A) := W_r(Inst(A))`, sorted
canonically. **Leaf conditions** (pinned): `Inst(A)` empty, or
`dim Inst(A) = 0` (single polynomial: direct check), or `W(A)` empty
(the moment leaf, SS5).

**Batch descent BD.** States are forced-root sets; root `A = {}`. A
non-leaf state `A` has children `{ A cup S : S in W(A) }` — one per
sparse support, all processed at once. (Distinctness: `S != S'` both
disjoint from `A` force `A cup S != A cup S'`.)

**Sequential binary descent SBD** (the "naive tree"). Nodes carry
`(A, i)` with `0 <= i <= |W(A)|`; root `({}, 0)`. At a non-leaf `(A, i)`
with `i < |W(A)|`, process the `(i+1)`-st word `S` of `W(A)`: the
(a)-child is `(A cup S, 0)`, the (b)-child is `(A, i+1)`; `(A, |W(A)|)`
is the residue leaf. This is the binary tree of SS0.3.

**Lemma 3 (state determinism).** Along any path of either procedure with
(a)-supports `S_1, ..., S_m` (in order), the iterated single-step child
of Lemma 2 equals `Inst(S_1 cup ... cup S_m)`. Hence the instance at any
node is a function of `A(nu)` alone — independent of the path, the order
of the supports, and the entire (b)-record.

*Proof.* One composition step suffices: for disjoint `S, S'` (children
supports are subsets of the child's evaluation set, hence disjoint from
everything before), and `x notin S`: `(f/ell_S)(x) = f(x) / ell_S(x)`
with `ell_S(x) != 0`, so `(f/ell_S)|_{S'} == 0 <=> f|_{S'} == 0`;
therefore `{f : f|_S == 0, (f/ell_S)|_{S'} == 0} = {f : f|_{S cup S'} == 0}`,
and `(f/ell_S)/ell_{S'} = f/ell_{S cup S'}`. Induct on `m`. QED

**Remark 3.4 (member payloads are path-dependent — bounds are not).**
In SBD two nodes can share a state `(A, i)` while carrying different
member subsets (their paths recorded different (b)-constraints). The
STATE determines the flat, `W(A)`, the pending word, and hence the
entire subtree shape (Lemma 3 + induction); and since (b)-constraints
only shrink member sets, any upper bound computed on states is valid
for every node with that state. The exact count statement that avoids
this subtlety entirely is the charging partition, Theorem 4(iv).

## 4. The accounting identity [PROVED]

Fix a terminated run of BD (SBD visits exactly the same `A`-sets: its
(a)-children are BD's children). Let `R` be the set of reachable states,
`Proc := union over non-leaf A in R of W(A)` the processed supports
(as subsets of `E`), and the **support lattice**

```text
L := {empty set} cup { unions of nonempty subfamilies of Proc },
```

the union-closure — its elements are the CLOSED SETS. Let
`Wmax := max_{A in R} |W(A)|`.

**Theorem 4 (accounting identity).**

```text
(i)   [state collapse]  Every node nu of BD or SBD has instance
      Inst(A(nu)) — a function of the closed set A(nu) alone; and
      A(nu) in L for every node.
(ii)  [injection]  BD states biject with R subset L. SBD states inject
      into pairs (closed set, residual budget):
          (A, i)  ->  (A, b),   b := |W(A)| - i in {0, ..., |W(A)|},
      and the state determines the subtree (Remark 3.4).
(iii) [size]  #BD-nodes = #R <= #L;
      #SBD-states <= sum_{A in R} (1 + |W(A)|) <= #L * (1 + Wmax).
(iv)  [member accounting]  Canonical charging: send f in M(P,E) down
      the tree, at each non-leaf state descending along the
      canonically least S in W(A) with S subset root(f/ell_A), stopping
      at a leaf or when no processed support is contained. This
      partitions the members:
          M(P,E)  =  disjoint union over A in R of  Res(A),
      where Res(A) ~ {members of Inst(A) containing no S in W(A)} —
      and by Lemma 1 each such residual member is nonzero on >= 2
      points of EVERY S in W(A).
(v)   [chains]  Every root-to-node path has m (a)-edges with pairwise
      disjoint supports, so
          m <= |A_end| = total degree drop,   and   m <= beta(P) - beta_end
      (the beta form over the path's nonempty instances; an empty
      instance can only be terminal);
      chain node count <= deg drop + 1 <= dim P + deg drop + 1.
```

*Proof.* (i) Lemma 3; `A(nu)` is a union of processed supports, so in
`L`. (ii) For BD, states ARE the reachable `A`; for SBD, `A` determines
`W(A)` (Lemma 3), so `(A, b)` recovers `i = |W(A)| - b`: injective.
(iii) Count the pairs allowed by (ii). (iv) The walk is well-defined
(Lemma 2(4) transports the member; each descent drops degree by
`|S| >= 1`, so it terminates) and deterministic, so each member is
charged exactly once; at the stopping state the member contains no
`S in W(A)`, and Lemma 1 upgrades "not containing `S`" to "nonzero on
`>= 2` points of `S`". At a moment leaf `W(A)` is empty and the
condition is vacuous — the residue is all members of the instance.
(v) Each (a)-edge adds `S_{i+1} subset E \ A_i`, disjoint from `A_i`,
so `|A|` grows by `|S_i| >= 1` per step and equals the accumulated
degree drop (Lemma 2(2)); `beta` drops by `>= 1` per (a)-edge
(Lemma 2(3)) and is `>= 0` throughout. QED

**Corollary 4.6 (the `2^depth` objection, defused).** The naive binary
tree exceeds the state count only by DUPLICATED subtrees (two nodes
with equal state have isomorphic subtrees). Memoized on states — which
is how any actual computation or induction evaluates the recursion —
the descent costs at most `#L * (1 + Wmax)` node evaluations
(`<= #R <= #L <= #L * maxchain` in the batch form, which recovers the
queue's phrasing verbatim, with `maxchain <= dim P + deg drop + 1` by
(v)), with recursion depth linear, never exponential. Super-polynomial
descent cost therefore REQUIRES super-polynomially many generated
closed sets. The polynomial question for F-termination becomes exactly:
**count the closed sets of the generated support lattice** — which is
family-specific: trivial for fiber flats (SS6), coset-structured for
Hankel-kernel flats (QF.14/E17's prediction), and measured by the E9
census in general.

*Proof.* All contained in Theorem 4; the queue-form chain bound is (v)
plus `deg drop + 1 <= dim P + deg drop + 1`. QED

**Remark 4.7 (honest second factor).** For the one-word-per-node binary
form the correct second factor is `(1 + Wmax)`, not the chain length;
the advertised product `#closed-sets x maxchain` is exact for the
batch/memoized form (factor `1 <= maxchain`). Both defuse `2^depth`;
neither bounds `#L` itself — see Non-claims.

## 5. The leaf: r-wise uniformity and the moment count [PROVED]

**Lemma 5.** Let `(P, E)` be any flat (monicity not needed) whose
direction dual `C_dir(P,E)^perp` contains no nonzero word of weight
`<= r`. Write `rho_E(f) := #{x in E : f(x) = 0}`. Then:

```text
(a) [uniformity]  for every T subset E with |T| <= r, the evaluation
    map ev_T : P -> F_q^T is ONTO with all fibers of size |P| / q^{|T|};
(b) [exact moment identity]
    sum_{f in P} C(rho_E(f), r)  =  C(|E|, r) * |P| * q^{-r};
(c) [member bound]  for every j >= r:
    #{ f in P : rho_E(f) >= j }  <=  |P| * C(|E|, r) / ( q^r * C(j, r) ).
```

*Proof.* (a) If `ev_T(V)` were a proper subspace of `F_q^T`, a nonzero
functional `u` would annihilate it — a nonzero word of `C_dir^perp`
supported in `T`, weight `<= r`: contradiction. A surjective linear map
has equal fibers; the affine shift by `ev_T(f_0)` preserves both.
(b) Double count pairs `(f, T)` with `|T| = r`, `T subset zeros(f)`:
`sum_T #{f : f|_T == 0} = sum_T |P| q^{-r}` by (a) (the fiber of `0`).
(c) `C(rho, r)` is nondecreasing in `rho`, so
`#{rho >= j} * C(j, r) <= sum_f C(rho_E(f), r)`. QED

**Remark 5.2 (the two duals at a leaf — honest scope).** The leaf
condition `W_r(Ann) = empty` stops the RECURSION; the full moment count
(Lemma 5) additionally needs the (possibly one-dimension-larger)
direction dual to be free of weight-`<= r` words. If `Ann` is clean but
`C_dir^perp` retains a sparse word `u` (necessarily with
`sum u_x f(x) = c != 0` on the flat), projections onto its support are
uniform on an explicit affine subspace instead of all of `F_q^T`; the
counting consequence is family-specific and NOT claimed here. For the
QF.13 flats of SS6 the strong condition holds for the direction dual
itself, so nothing is lost.

## 6. QF.13: fiber flats are MDS-dual — trivial lattice, tree size 1 [PROVED]

**Lemma 6 (shortening of MDS is MDS).** Let `C` be `[n, k, n-k+1]` MDS
with `2 <= k <= n-1`, and `sh_i(C) := { c|_{[n] \ i} : c in C, c_i = 0 }`.
Then `sh_i(C)` is `[n-1, k-1, n-k+1]` MDS.
*Proof (3 lines).* No coordinate of `C` is identically zero (else drop
it: an `[n-1, k]` code of distance `>= n-k+1 > (n-1)-k+1`, violating
Singleton); so `ev_i` is onto `F_q` and `{c : c_i = 0}` has dimension
`k-1`, mapping injectively to `sh_i(C)` (a codeword vanishing on the
rest and at `i` is `0`). Weights are preserved (only a zero coordinate
is dropped), so `d(sh_i C) >= n-k+1`; Singleton gives
`d <= (n-1)-(k-1)+1 = n-k+1`. Equality: MDS. Iterate for a set `S_0`. QED

**Lemma 7 (dual of MDS is MDS; "Singleton-dual").** Let `C` be
`[n, k, n-k+1]` MDS, `1 <= k <= n-1`. Then every `k`-subset of
coordinates is an information set, and `C^perp` is `[n, n-k, k+1]` MDS.
*Proof.* For `|T| = k`: `ker(ev_T|_C) = {c : c|_T = 0}` has weight
`<= n-k < n-k+1`, hence is `0`; so `ev_T : C -> F_q^T` is bijective.
If `0 != u in C^perp` had `wt(u) <= k`, extend `supp(u)` to a `k`-set
`T`; since `ev_T(C) = F_q^T`, some codeword has `sum_T u_x c_x != 0` —
contradicting `u perp C`. So `d(C^perp) >= k+1`, and Singleton forces
`d(C^perp) = n - (n-k) + 1 = k+1`. QED

**Proposition 8 (fiber flats).** Pin `S_0 subset H`, `|S_0| = s`,
`0 <= s <= k-1 < n-1`, a word `w_0 : S_0 -> F_q`, and the
**coordinate-prefix/fiber flat**

```text
P := { f in F_q[X] : deg f < k,  f(x) = w_0(x) for all x in S_0 },
E := H \ S_0,   n' := n - s,   k' := k - s.
```

Then:

```text
(i)   P != empty and its direction space is V = ell_{S_0} * F_q[X]_{<k'},
      of dimension k';
(ii)  C := ev_E(V) IS the S_0-shortening of the Reed-Solomon code
      RS_k(H) (restricted to E), and C is [n', k', n'-k'+1] MDS;
(iii) C^perp is [n', n'-k', k'+1]: the dual evaluation code meets
      Singleton with minimum distance k'+1 = (n') - dim(C^perp) + 1,
      so there are NO nonzero dual words of weight <= k'; a fortiori
      none in Ann(P,E) (Lemma 0.1).
```

*Proof.* (i) Interpolation gives some `f_0` (`s <= k-1 < k` conditions
on a `k`-dimensional space); `g` is a direction iff `deg g < k` and
`g|_{S_0} = 0` iff `ell_{S_0} | g`, i.e. `g = ell_{S_0} h` with
`deg h < k'`; `h -> ell_{S_0} h` is injective, so `dim V = k'`.
(ii) The `S_0`-shortening of `RS_k(H)` is by definition
`{ev(g)|_E : deg g < k, g|_{S_0} = 0}` — the same set, by (i). MDS
directly: `ev_E` is injective on `V` (if `ell_{S_0} h` vanishes on all
of `E` then `h`, of degree `< k' <= n' - 1 < n'`, has `n'` roots, so
`h = 0`), giving dimension `k'`; a nonzero `g = ell_{S_0} h` has at most
`deg h <= k'-1` roots in `E` (the `S_0`-roots are outside `E`), so
weight `>= n' - k' + 1`; Singleton closes. (Alternatively: Lemma 6
applied `s` times to `RS_k(H)`, itself `[n, k, n-k+1]` MDS by the same
root count.) (iii) Lemma 7 applied to (ii); `Ann subset C^perp` is
Lemma 0.1. QED

**Corollary 9 (immediate termination + moment count).** For any descent
threshold `r <= k'`, the fiber flat has `S_r(P,E) = empty`: the support
lattice is `L = {empty}`, both descent procedures consist of the single
root node (tree size 1, batch and naive alike), and the moment-count
branch applies immediately: by Lemma 5 at order `r = k'` (the direction
dual is clean at that order by Proposition 8(iii)), for every `j >= k'`

```text
#{ f in P : f has >= j distinct roots in E }
     <=  |P| * C(n',k') / (q^{k'} * C(j,k'))   =   C(n',k') / C(j,k'),
```

since `|P| = q^{k'}`. In particular the F-descent for coordinate-
prefix/fiber flats terminates at depth 0 with the polynomial,
`n`-explicit bound `C(n',k')/C(j,k')` — no tree, no lattice count.

*Proof.* Everything is assembled: Proposition 8(iii) empties `S_r`, so
the root satisfies the moment-leaf condition; Lemma 5(c) with
`|P| = q^{dim V} = q^{k'}` (fibers of the direction space are affine
translates). QED

## 7. Verifier contract and key numbers

`experimental/scripts/verify_qf12_qf13_support_lattice.py` (run:
`python3 ...`; deterministic; exits 0 iff all checks pass; 31/31 PASS).

**Part A — QF.13 at `n = 16` over `F_17`** (`H = F_17^*`,
`S_0 = {1,2,4,8}`, `w_0 = (5,11,2,7)`, `k = 6`, so `n' = 12`, `k' = 2`):

```text
A1-A2  direction code = [12, 2, 11], MDS (min weight 11 = n'-k'+1,
       over all 288 nonzero codewords);
A3     dual code exactly: dimension 10; NO words of weight <= 2
       (exhaustive over all supports AND all coefficient vectors);
       a weight-3 word exists => min dual weight = 3 = k'+1
       = n' - dim(dual) + 1 (Singleton-dual met);
A4     Ann(P,E) likewise has no weight <= 2 words;
A5     1- and 2-wise uniformity of the 289 flat evaluations
       (fibers exactly 17 and exactly 1) — Lemma 5(a);
A6     exact moment identity sum_f C(rho,2) = C(12,2) = 66;
       rho histogram {0:142, 1:99, 2:39, 3:9}; member bounds
       #(rho>=j) <= 66/C(j,2) for j = 2..5 (e.g. 9 <= 22 at j = 3,
       0 <= 6 at j = 5) — Lemma 5(b,c);
A7     the direction code EQUALS the S_0-shortening of RS_6(H)
       (row-space identity) — Proposition 8(ii);
A8     descent at threshold r = 2: W(root) empty, batch tree = 1 node,
       naive tree = 1 node, L = {empty} — Corollary 9.
```

**Part B — QF.12 on a non-MDS plane** (monic degree-4 flat over `F_17`,
`E = H = F_17^*`, planted forced root `f(1) = 0` and planted twin
`f(2) = 2 f(9)`; threshold `r = 2`; dim P = 2, beta = 2):

```text
B0     construction: dim 2; W(root) = {{1}, {2,9}} exactly (the two
       planted words; computed exhaustively, no accidentals);
B1     Lemma 1 checked on every (reachable instance, sparse word,
       member) triple — no member with exactly one nonzero on a support;
B2     Lemma 2 on every edge: deg drop = |S|, dim drop <= |S|-1,
       beta drop >= 1;
B3     Lemma 3 on every edge: single-step child == Inst(A) from scratch;
B4     Theorem 4: R = L = {empty, {1}, {2,9}, {1,2,9}} (4 closed sets);
       #states = 8 <= #L*(1+Wmax) = 12 (Wmax = 2); naive binary tree
       = 9 nodes > 8 states, duplicated state ({1,2,9}, 0) — the
       reconvergence {1}+{2,9} -> {1,2,9} has in-degree 2: the collapse
       is REAL and strict; max chain = 3 nodes <= |A_end|+1 per path
       <= dim P + deg drop + 1 = 6; residual budgets within range;
B5     charging partition: the 31 members of M(P,H) split as
       18 residues at {1} + 13 at {1,2,9}, each residue verified inside
       its instance flat and missing >= 2 points of every remaining
       sparse support;
B6     batch tree size = #R = 4 <= #L = 4 <= #L*maxchain = 12
       (the queue's product form, verbatim);
B7     non-MDS contrast: min Ann weight = 1 (< the MDS-protected range
       of Part A) — sparse words exist, the descent is genuinely active.
```

## 8. Non-claims

```text
N1  This note does NOT prove Conjecture F, nor any polynomial bound on
    #(P cap D_j) for general flats. Theorem 4 RELOCATES the question:
    tree size is polynomial iff the generated closed-set count is —
    and counting closed sets is family-specific (QF.14/E17 for
    Hankel-kernel flats; E9 census in general). #L and Wmax can a
    priori be exponential for adversarial flats.
N2  The accounting identity bounds tree/state SIZE and gives the exact
    member partition (Thm 4(iv)); it does not by itself bound member
    COUNTS — that needs leaf bounds (Lemma 5 where the direction dual
    is clean; family-specific otherwise, Remark 5.2).
N3  Residue counting at INTERNAL states (members missing >= 2 points of
    every processed support) is an interface handed to the family-
    specific analysis; no bound on it is claimed here.
N4  The pinned procedure is THIS note's; the in-flight QF.6/QF.7
    conventions (parallel PRs, not in this worktree) may differ in
    which dual they process and in leaf semantics — reconcile at
    integration (SS0.4). [AUDIT]
N5  The queue's phrase "tree size <= #closed-sets x maxchain" is
    recovered verbatim for the batch/memoized form; for the sequential
    binary form the proved second factor is (1 + Wmax) (Remark 4.7).
N6  Part B's twin plane is CONSTRUCTED to the E7-census specification
    (a plane with a weight-2 dual word); it is not E7's literally
    recorded artifact (that artifact lives in a parallel PR and is not
    in this worktree).
N7  Corollary 9's bound C(n',k')/C(j,k') is what the moment count
    yields at order k' = k - s; whether that suffices for a given
    downstream budget depends on (n, k, s, j) — the consumers (QF.9/
    QF.10 fiber-side audit) must check their own parameters.
N8  Nothing here uses the group structure of H = mu_n; conversely,
    nothing is claimed about non-distinct or extension-field evaluation
    points.
```
