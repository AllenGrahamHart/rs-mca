#!/usr/bin/env python3
"""QF.12 + QF.13 verifier: support-lattice accounting + the MDS fiber-flat corollary.

Companion to experimental/notes/roadmaps/qf12_qf13_support_lattice_mds.md
(DAG nodes f_support_lattice, f_termination_mds; execution_queue.md Tier D2).

Deterministic, pure standard library, exact arithmetic over F_17.

PART A (QF.13, MDS corollary), n = 16 over F_17, H = F_17^*:
  fiber flat P = {f : deg f < k=6, f|_{S0} = w0}, |S0| = 4, evaluated on
  E = H \\ S0 (n' = 12, k' = 2).  Checks: the direction code is the
  S0-shortening of RS_6(H); it is [12,2,11] MDS; its dual is [12,10,3]
  (min dual weight == k'+1 == 3, exhaustively below that range); 2-wise
  uniformity of the flat's evaluations; the exact moment identity
  sum_f C(rho(f),2) = C(12,2); the derived member bounds; and the descent
  tree at threshold r = 2 has size exactly 1 (trivial support lattice).

PART B (QF.12, accounting identity), toy descent on a NON-MDS plane:
  monic degree-4 plane over F_17 with a planted forced root f(1)=0
  (weight-1 dual word) and a planted twin f(2)=2 f(9) (weight-2 dual
  word).  Checks: the dichotomy lemma on every (instance, word, member);
  per-edge descent parameters (deg drop = |S|, dim drop <= |S|-1,
  beta drop >= 1); state determinism (path-composed instance == from-
  scratch instance); the accounting (states inject into (closed set,
  residual budget) pairs; naive binary tree collapses onto the state
  DAG; reachable states subset of the union-closure lattice L; chain
  bounds); and the member-charging partition.

Run:  python3 verify_qf12_qf13_support_lattice.py     (exit 0 iff all PASS)
"""
from itertools import combinations, product
from math import comb

Q = 17

RESULTS = []


def check(name, ok, info=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("  [" + info + "]") if info else ""))
    RESULTS.append(bool(ok))


# ---------------------------------------------------------------- F_17 linalg
def rref(rows):
    """Row reduce mod Q. Returns (nonzero rref rows, pivot column list)."""
    mat = [list(r) for r in rows]
    mat = [r for r in mat if any(v % Q for v in r)]
    if not mat:
        return [], []
    ncols = len(mat[0])
    piv = []
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, len(mat)):
            if mat[i][c] % Q:
                pr = i
                break
        if pr is None:
            continue
        mat[r], mat[pr] = mat[pr], mat[r]
        inv = pow(mat[r][c] % Q, Q - 2, Q)
        mat[r] = [(v * inv) % Q for v in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] % Q:
                f = mat[i][c] % Q
                mat[i] = [(a - f * b) % Q for a, b in zip(mat[i], mat[r])]
        piv.append(c)
        r += 1
        if r == len(mat):
            break
    return [row for row in mat[:r] if any(v % Q for v in row)], piv


def nullspace(rows, ncols):
    """Basis of {u : rows . u = 0} in F_Q^ncols."""
    R, piv = rref(rows)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for row, pc in zip(R, piv):
            v[pc] = (-row[fc]) % Q
        basis.append(v)
    return basis


def solve_affine(rows, rhs):
    """Solve rows.t = rhs. Returns (particular t, nullspace basis) or None."""
    n = len(rows[0]) if rows else 0
    aug = [list(r) + [b % Q] for r, b in zip(rows, rhs)]
    R, piv = rref(aug)
    for row, pc in zip(R, piv):
        if pc == n:
            return None  # inconsistent
    t = [0] * n
    for row, pc in zip(R, piv):
        t[pc] = row[n] % Q
    return t, nullspace(rows, n)


# ---------------------------------------------------------------- polynomials
def pe(f, x):
    """Evaluate coefficient vector f (low->high) at x, mod Q."""
    acc = 0
    for c in reversed(f):
        acc = (acc * x + c) % Q
    return acc


def div_linear(f, a):
    """Exact division of f (length m) by (X - a); returns length m-1 vector."""
    m = len(f)
    g = [0] * (m - 1)
    g[m - 2] = f[m - 1] % Q
    for i in range(m - 2, 0, -1):
        g[i - 1] = (f[i] + a * g[i]) % Q
    rem = (f[0] + a * g[0]) % Q
    assert rem == 0, "non-exact division"
    return g


def div_points(f, pts):
    for a in sorted(pts):
        f = div_linear(f, a)
    return f


def ell(pts, length):
    """prod (X-x), padded to coefficient length `length`."""
    f = [1]
    for x in sorted(pts):
        f = [(-x * f[0]) % Q] + [(f[i - 1] - x * f[i]) % Q for i in range(1, len(f))] + [f[-1]]
    assert len(f) == len(pts) + 1
    return f + [0] * (length - len(f))


# ---------------------------------------------------------------- affine flats
def make_flat(f0, basis, deg):
    """Affine flat f0 + span(basis) of coefficient vectors, canonicalized.
    deg = monic degree (Part B) or None (Part A degree-bound normalization)."""
    m = len(f0)
    B, piv = rref(basis)
    f0c = [v % Q for v in f0]
    for row, pc in zip(B, piv):
        c = f0c[pc]
        if c:
            f0c = [(a - c * b) % Q for a, b in zip(f0c, row)]
    return {"m": m, "f0": tuple(f0c), "basis": tuple(tuple(r) for r in B),
            "piv": tuple(piv), "deg": deg}


def flat_dim(fl):
    return len(fl["basis"])


def flat_equal(a, b):
    return a["m"] == b["m"] and a["f0"] == b["f0"] and a["basis"] == b["basis"]


def flat_points(fl):
    dim = flat_dim(fl)
    for coeffs in product(range(Q), repeat=dim):
        v = list(fl["f0"])
        for t, b in zip(coeffs, fl["basis"]):
            if t:
                v = [(a + t * c) % Q for a, c in zip(v, b)]
        yield tuple(v)


def flat_contains(fl, f):
    """Membership test: f - f0 in span(basis)."""
    d = [(a - b) % Q for a, b in zip(f, fl["f0"])]
    rows = [list(b) for b in fl["basis"]] + [d]
    R, _ = rref(rows)
    return len(R) == flat_dim(fl)


# ------------------------------------------------- sparse affine-dual supports
def full_support_word_exists(nbasis, w):
    """Does span(nbasis) contain a vector with all w coordinates nonzero?"""
    if not nbasis:
        return False
    for coeffs in product(range(Q), repeat=len(nbasis)):
        if not any(coeffs):
            continue
        v = [0] * w
        for t, b in zip(coeffs, nbasis):
            if t:
                v = [(a + t * c) % Q for a, c in zip(v, b)]
        if all(v):
            return True
    return False


def ann_sparse_supports(fl, pts, r):
    """All supports T (|T| <= r) of nonzero words of Ann(P,E):
    sum_{x in T} u_x f(x) = 0 for every f in the flat (f0 and basis rows)."""
    rows_polys = [fl["f0"]] + list(fl["basis"])
    found = []
    for w in range(1, r + 1):
        for T in combinations(sorted(pts), w):
            M = [[pe(g, x) for x in T] for g in rows_polys]
            N = nullspace(M, w)
            if full_support_word_exists(N, w):
                found.append(frozenset(T))
    return found


def minimal_supports(found):
    out = [S for S in found if not any(S2 < S for S2 in found)]
    return sorted(set(out), key=lambda S: (len(S), tuple(sorted(S))))


# ---------------------------------------------------------------- the descent
def vanish_and_divide(root_fl, A):
    """Inst(A) = ((P cap {f|_A == 0}) / ell_A), or None if empty."""
    if not A:
        return root_fl
    S = sorted(A)
    basis = [list(b) for b in root_fl["basis"]]
    rows = [[pe(b, x) for b in basis] for x in S]
    rhs = [(-pe(root_fl["f0"], x)) % Q for x in S]
    sol = solve_affine(rows, rhs)
    if sol is None:
        return None
    t, N = sol
    f0 = list(root_fl["f0"])
    for ti, b in zip(t, basis):
        if ti:
            f0 = [(a + ti * c) % Q for a, c in zip(f0, b)]
    newbasis = []
    for n in N:
        v = [0] * root_fl["m"]
        for ni, b in zip(n, basis):
            if ni:
                v = [(a + ni * c) % Q for a, c in zip(v, b)]
        newbasis.append(v)
    f0d = div_points(f0, S)
    basis_d = [div_points(v, S) for v in newbasis]
    deg = root_fl["deg"] - len(S) if root_fl["deg"] is not None else None
    return make_flat(f0d, basis_d, deg)


def batch_descent(root_fl, root_pts, r):
    """Batch descent; memoized on the forced-root set A. Returns (R, edges)."""
    R = {}
    queue = [frozenset()]
    while queue:
        A = queue.pop(0)
        if A in R:
            continue
        pts = [x for x in root_pts if x not in A]
        fl = vanish_and_divide(root_fl, A)
        rec = {"pts": pts, "fl": fl, "W": [], "leaf": None}
        if fl is None:
            rec["leaf"] = "empty"
        elif flat_dim(fl) == 0:
            rec["leaf"] = "dim0"
        else:
            W = minimal_supports(ann_sparse_supports(fl, pts, r))
            rec["W"] = W
            if not W:
                rec["leaf"] = "moment"
        R[A] = rec
        if rec["leaf"] is None:
            for S in rec["W"]:
                queue.append(A | S)
    edges = [(A, A | S, S) for A in sorted(R, key=lambda a: (len(a), tuple(sorted(a))))
             for S in R[A]["W"] if R[A]["leaf"] is None]
    return R, edges


def sbd_naive(R):
    """Sequential binary descent, unmemoized: count tree nodes and states."""
    nodes = 0
    statecount = {}
    stack = [(frozenset(), 0)]
    while stack:
        A, i = stack.pop()
        nodes += 1
        statecount[(A, i)] = statecount.get((A, i), 0) + 1
        rec = R[A]
        if rec["leaf"] is not None or i == len(rec["W"]):
            continue
        S = rec["W"][i]
        stack.append((A, i + 1))
        stack.append((A | S, 0))
    return nodes, statecount


def union_closure(supports):
    L = {frozenset()} | set(supports)
    while True:
        new = {a | b for a in L for b in L} - L
        if not new:
            return L
        L |= new
        assert len(L) < 5000, "union closure blow-up (unexpected at toy scale)"


def members(fl, pts):
    """Monic flat members: exactly deg distinct roots inside pts."""
    d = fl["deg"]
    out = []
    for f in flat_points(fl):
        roots = [x for x in pts if pe(f, x) == 0]
        if len(roots) == d:
            out.append(f)
    return out


def all_root_paths(R):
    """All root-to-node paths in the state DAG (toy scale)."""
    paths = [[frozenset()]]
    out = []
    while paths:
        p = paths.pop()
        out.append(p)
        rec = R[p[-1]]
        if rec["leaf"] is None:
            for S in rec["W"]:
                paths.append(p + [p[-1] | S])
    return out


# ===================================================================== PART A
def part_a():
    print("== PART A: QF.13 fiber flat, n = 16 over F_17 ==")
    H = list(range(1, 17))
    S0 = [1, 2, 4, 8]
    w0 = {1: 5, 2: 11, 4: 2, 8: 7}
    E = [x for x in H if x not in S0]
    k, s = 6, len(S0)
    npr, kpr = len(E), k - s          # n' = 12, k' = 2

    # f0 = interpolation of w0 on S0 (degree <= 3), padded to length k.
    rows = [[pow(x, m, Q) for m in range(s)] for x in S0]
    t, N = solve_affine(rows, [w0[x] for x in S0])
    assert not N
    f0 = t + [0] * (k - s)
    check("A0 interpolant hits w0 on S0", all(pe(f0, x) == w0[x] for x in S0))

    # direction space V = ell_S0 * {1, X}; the fiber flat.
    b1 = ell(S0, k)
    b2 = [0] + b1[:-1]                # X * ell_S0 (deg 5 < 6)
    fl = make_flat(f0, [b1, b2], None)
    G = [[pe(b, x) for x in E] for b in (b1, b2)]

    R1, _ = rref(G)
    check("A1 direction code dimension k' == 2", len(R1) == 2 and flat_dim(fl) == 2)

    # A2: C is [12, 2, 11] MDS.
    weights = []
    for a, b in product(range(Q), repeat=2):
        if a == 0 and b == 0:
            continue
        cw = [(a * G[0][i] + b * G[1][i]) % Q for i in range(npr)]
        weights.append(sum(1 for v in cw if v))
    check("A2 code is [12,2,11] MDS (min weight == n'-k'+1 == 11)",
          min(weights) == npr - kpr + 1, "min weight = %d" % min(weights))

    # A3: dual code exactly; min dual weight == k'+1 == 3, exhaustive below.
    dual_basis = nullspace(G, npr)
    check("A3a dual dimension == n'-k' == 10", len(dual_basis) == npr - kpr)
    ok_perp = all(sum(u[i] * G[j][i] for i in range(npr)) % Q == 0
                  for u in dual_basis for j in range(2))
    check("A3b dual basis orthogonal to G", ok_perp)
    # exhaustive: no dual word of weight 1 or 2 (all supports x all coefficients)
    no12 = True
    for w in (1, 2):
        for T in combinations(range(npr), w):
            for coeffs in product(range(1, Q), repeat=w):
                if all(sum(c * G[j][i] for c, i in zip(coeffs, T)) % Q == 0
                       for j in range(2)):
                    no12 = False
    check("A3c NO dual words of weight <= 2 (exhaustive, coefficients included)", no12)
    found3 = False
    for T in combinations(range(npr), 3):
        M = [[G[j][i] for i in T] for j in range(2)]
        if full_support_word_exists(nullspace(M, 3), 3):
            found3 = True
            break
    check("A3d weight-3 dual word exists => min dual weight == k'+1 == 3", found3)
    check("A3e Singleton-dual: n' - dim(dual) + 1 == 3", npr - len(dual_basis) + 1 == 3)

    # A4: affine annihilator Ann(P,E) also has no words of weight <= 2.
    check("A4 Ann(P,E) has no words of weight <= 2",
          ann_sparse_supports(fl, E, 2) == [])

    # A5: 2-wise uniformity of the flat's evaluations on E.
    evals = [tuple(pe(f, x) for x in E) for f in flat_points(fl)]
    assert len(evals) == Q ** 2
    uni1 = all(all(sum(1 for e in evals if e[i] == v) == Q for v in range(Q))
               for i in range(npr))
    uni2 = True
    for i, j in combinations(range(npr), 2):
        seen = {}
        for e in evals:
            seen[(e[i], e[j])] = seen.get((e[i], e[j]), 0) + 1
        if len(seen) != Q * Q or set(seen.values()) != {1}:
            uni2 = False
    check("A5 evaluations are 1- and 2-wise uniform (fibers exactly 17 / 1)",
          uni1 and uni2)

    # A6: exact moment identity and member bounds.
    rhos = [sum(1 for v in e if v == 0) for e in evals]
    total = sum(comb(rho, 2) for rho in rhos)
    check("A6a moment identity sum_f C(rho,2) == C(12,2) == 66", total == comb(npr, 2),
          "sum = %d" % total)
    hist = {j: sum(1 for rho in rhos if rho == j) for j in sorted(set(rhos))}
    print("      rho histogram over the 289 flat members:", hist)
    ok_bounds = True
    for j in range(2, 6):
        cnt = sum(1 for rho in rhos if rho >= j)
        bound = comb(npr, 2) // comb(j, 2)
        print("      #(rho >= %d) = %d  <= C(12,2)/C(%d,2) = %d" % (j, cnt, j, bound))
        if cnt * comb(j, 2) > comb(npr, 2):
            ok_bounds = False
    check("A6b moment-count bounds #(rho>=j) <= C(12,2)/C(j,2) for j = 2..5", ok_bounds)

    # A7: direction code == S0-shortening of RS_6(H), as row spaces on E.
    vrows = [[pow(x, m, Q) for m in range(k)] for x in S0]
    short_basis = nullspace(vrows, k)          # {g : deg g < 6, g|_{S0} = 0}
    Gs = [[pe(g, x) for x in E] for g in short_basis]
    RA, _ = rref(G)
    RB, _ = rref(Gs)
    check("A7 direction code == shortened RS_6(H) (row-space equality)", RA == RB)

    # A8: trivial support lattice; descent tree size 1 at threshold r = 2.
    R, edges = batch_descent(fl, E, 2)
    n_naive, states = sbd_naive(R)
    L = union_closure([S for A in R for S in R[A]["W"]])
    check("A8 W_2(root) empty; batch tree = 1 node; naive tree = 1 node; L = {0}",
          R[frozenset()]["W"] == [] and len(R) == 1 and n_naive == 1 and L == {frozenset()})
    print("      Part A key numbers: [n',k',d] = [12,2,11], dual [12,10,3], "
          "|P| = 289, moment sum = 66, tree size = 1")


# ===================================================================== PART B
def part_b():
    print("== PART B: QF.12 accounting on a non-MDS plane (planted root + twin) ==")
    H = list(range(1, 17))
    r = 2
    # ambient: monic degree-4, coefficient vectors length 5 (top coeff 1)
    amb_f0 = [0, 0, 0, 0, 1]
    amb_basis = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0]]
    # constraints: f(1) = 0  and  f(2) - 2 f(9) = 0
    c_rows, c_rhs = [], []
    c_rows.append([pe(b, 1) for b in amb_basis]); c_rhs.append((-pe(amb_f0, 1)) % Q)
    c_rows.append([(pe(b, 2) - 2 * pe(b, 9)) % Q for b in amb_basis])
    c_rhs.append((-(pe(amb_f0, 2) - 2 * pe(amb_f0, 9))) % Q)
    t, N = solve_affine(c_rows, c_rhs)
    f0 = list(amb_f0)
    for ti, b in zip(t, amb_basis):
        if ti:
            f0 = [(a + ti * c) % Q for a, c in zip(f0, b)]
    basis = []
    for n in N:
        v = [0] * 5
        for ni, b in zip(n, amb_basis):
            if ni:
                v = [(a + ni * c) % Q for a, c in zip(v, b)]
        basis.append(v)
    P = make_flat(f0, basis, 4)
    check("B0a plane has dimension 2 (beta = deg - dim = 2)", flat_dim(P) == 2)

    W0 = minimal_supports(ann_sparse_supports(P, H, r))
    check("B0b planted words found: {1} and {2,9} in W(root)",
          frozenset([1]) in W0 and frozenset([2, 9]) in W0,
          "W(root) = %s" % [sorted(S) for S in W0])

    R, edges = batch_descent(P, H, r)
    Akey = lambda A: (len(A), tuple(sorted(A)))

    # B1: dichotomy on every (reachable instance, sparse word, member).
    ok1 = True
    member_cache = {}
    for A in sorted(R, key=Akey):
        rec = R[A]
        if rec["fl"] is None:
            continue
        mem = members(rec["fl"], rec["pts"]) if rec["fl"]["deg"] is not None else []
        member_cache[A] = mem
        for S in rec["W"]:
            for g in mem:
                nz = sum(1 for x in S if pe(g, x) != 0)
                if nz == 1:
                    ok1 = False
    check("B1 dichotomy: no member has exactly ONE nonzero value on a sparse support", ok1)

    # B2: per-edge descent parameters.
    ok2 = True
    for A, B, S in edges:
        pa, ch = R[A], R[B]
        if ch["fl"] is None:
            continue  # empty child: count-0 leaf, no parameters to check
        ddrop = pa["fl"]["deg"] - ch["fl"]["deg"]
        dimdrop = flat_dim(pa["fl"]) - flat_dim(ch["fl"])
        beta_p = pa["fl"]["deg"] - flat_dim(pa["fl"])
        beta_c = ch["fl"]["deg"] - flat_dim(ch["fl"])
        if not (ddrop == len(S) and 0 <= dimdrop <= len(S) - 1 and beta_p - beta_c >= 1):
            ok2 = False
    check("B2 every edge: deg drop == |S|, dim drop <= |S|-1, beta drop >= 1", ok2)

    # B3: state determinism — single-step child == from-scratch instance.
    ok3 = True
    for A, B, S in edges:
        pa = R[A]
        step = vanish_and_divide_local(pa["fl"], S)
        scratch = R[B]["fl"]
        if (step is None) != (scratch is None):
            ok3 = False
        elif step is not None and not flat_equal(step, scratch):
            ok3 = False
    check("B3 state determinism: path-composed instance == Inst(A) from scratch", ok3)

    # B4: the accounting identity.
    processed = [S for A in R for S in R[A]["W"]]
    L = union_closure(processed)
    ok_rl = all(A in L for A in R)
    check("B4a reachable states R lie in the union-closure lattice L", ok_rl,
          "#R = %d, #L = %d" % (len(R), len(L)))
    n_naive, states = sbd_naive(R)
    wmax = max((len(R[A]["W"]) for A in R), default=0)
    bound_states = len(L) * (1 + wmax)
    check("B4b #states <= #L * (1 + W_max)", len(states) <= bound_states,
          "#states = %d <= %d" % (len(states), bound_states))
    check("B4c naive binary tree >= state count (collapse)", n_naive >= len(states),
          "naive = %d, states = %d" % (n_naive, len(states)))
    dup = [st for st, c in states.items() if c >= 2]
    check("B4d strict collapse: some state reached by >= 2 tree nodes (reconvergence)",
          n_naive > len(states) and len(dup) >= 1,
          "duplicated states = %s" % [(sorted(A), i) for A, i in sorted(dup, key=lambda s: (Akey(s[0]), s[1]))])
    indeg = {}
    for A, B, S in edges:
        indeg[B] = indeg.get(B, 0) + 1
    check("B4e DAG reconvergence: some closed set has in-degree >= 2",
          any(v >= 2 for v in indeg.values()),
          "in-degrees = %s" % {tuple(sorted(k)): v for k, v in sorted(indeg.items(), key=lambda kv: Akey(kv[0]))})
    paths = all_root_paths(R)
    maxchain = max(len(p) for p in paths)
    dimP, degdrop_max = flat_dim(P), max(len(p[-1]) for p in paths)
    ok_chain = all(len(p) <= len(p[-1]) + 1 for p in paths)
    check("B4f chain bound: every chain has <= |A_end|+1 nodes <= dim P + deg drop + 1",
          ok_chain and maxchain <= dimP + degdrop_max + 1,
          "max chain = %d <= %d" % (maxchain, dimP + degdrop_max + 1))
    ok_res = all(0 <= i <= len(R[A]["W"]) for (A, i) in states)
    check("B4g residual budget range: every state (A,i) has 0 <= i <= |W(A)|", ok_res)

    # B5: member-charging partition.
    mem0 = member_cache[frozenset()]
    charges = {}
    ok_dich = True
    ok_membership = True
    for f in mem0:
        A = frozenset()
        g = f
        while True:
            rec = R[A]
            if rec["leaf"] is not None:
                break
            contained = [S for S in rec["W"] if all(pe(g, x) == 0 for x in S)]
            if not contained:
                for S in rec["W"]:
                    if sum(1 for x in S if pe(g, x) != 0) < 2:
                        ok_dich = False
                break
            S = contained[0]
            g = div_points(g, S)
            A = A | S
        if not flat_contains(R[A]["fl"], g):
            ok_membership = False
        charges.setdefault(A, []).append(f)
    tot = sum(len(v) for v in charges.values())
    check("B5a charging is a partition: total charged == #members(root)",
          tot == len(mem0), "%d members" % len(mem0))
    check("B5b every residue lands inside its instance flat", ok_membership)
    check("B5c residues miss >= 2 points of every remaining sparse support", ok_dich)
    print("      residue counts per closed set:",
          {tuple(sorted(A)): len(v) for A, v in sorted(charges.items(), key=lambda kv: Akey(kv[0]))})

    # B6: batch tree size == #R <= #L (<= #L * maxchain, the queue's slack form).
    check("B6 batch tree size == #R <= #L <= #L * maxchain",
          len(R) <= len(L) <= len(L) * maxchain,
          "batch nodes = %d, #L = %d, maxchain = %d" % (len(R), len(L), maxchain))

    # B7: non-MDS contrast with Part A.
    check("B7 non-MDS: the plane HAS dual words of weight <= 2 (min Ann weight == 1)",
          len(W0) >= 1 and min(len(S) for S in W0) == 1)

    print("      Part B key numbers: #R = %d, #L = %d, W_max = %d, maxchain = %d," %
          (len(R), len(L), wmax, maxchain))
    print("      naive tree = %d nodes, states = %d, members = %d" %
          (n_naive, len(states), len(mem0)))
    print("      lattice L =", sorted([tuple(sorted(A)) for A in L], key=lambda t: (len(t), t)))


def vanish_and_divide_local(fl, S):
    """Single descent step from an arbitrary instance flat (not the root)."""
    S = sorted(S)
    basis = [list(b) for b in fl["basis"]]
    rows = [[pe(b, x) for b in basis] for x in S]
    rhs = [(-pe(fl["f0"], x)) % Q for x in S]
    sol = solve_affine(rows, rhs)
    if sol is None:
        return None
    t, N = sol
    f0 = list(fl["f0"])
    for ti, b in zip(t, basis):
        if ti:
            f0 = [(a + ti * c) % Q for a, c in zip(f0, b)]
    newbasis = []
    for n in N:
        v = [0] * fl["m"]
        for ni, b in zip(n, basis):
            if ni:
                v = [(a + ni * c) % Q for a, c in zip(v, b)]
        newbasis.append(v)
    return make_flat(div_points(f0, S), [div_points(v, S) for v in newbasis],
                     fl["deg"] - len(S) if fl["deg"] is not None else None)


def main():
    part_a()
    print()
    part_b()
    print()
    ok = all(RESULTS)
    print("ALL CHECKS PASS: %s  (%d/%d)" % (ok, sum(RESULTS), len(RESULTS)))
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
