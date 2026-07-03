#!/usr/bin/env python3
"""Face-2 step (i): matching composition of the weight-2 inverse theorem.

Verifier for experimental/notes/roadmaps/f_matching_composition.md
(prize-DAG node f_weight2_inverse, step (i)).  Deterministic,
stdlib-only, exact arithmetic in F_17 (n = 16 toy scale).

Checks (see the note, Section 7):
  CHECK 1  q-flat counterexample certification (falsifies step (ii)
           as stated at n = q-1): span{1, q, q^2}, q = X^2+3X, is
           stripped, w2m = 7, in NO Dih_16 stratum, IS a span of 3
           squarefree quartic divisors of X^16-1, has composition
           degree e = 2 with fibers = orbits of x -> -3-x, and every
           fiber pair is a flat-wide ratio edge (Theorem 1(b)).
  CHECK 2  E35 symmetric census artifacts: every dim-3 stratum flat
           has e >= 2; for stripped ones the collision classes are
           the orbits of the detected Dih_16 subgroup, generic class
           size = e, exceptional classes <= 2e-2.
  CHECK 3  near-pencils (E35 seeds): e = 1, the Mobius ratio clause,
           all edges on the cancellation locus Z(P_1), accidental
           bound m <= D + (D-1)^2.
  CHECK 4  Lemma B sanity: seeded generating pairs have e = 1 and
           rational collision count <= 2(F-1)^2; a non-generating
           pair has e = 2 and a large collision set (the generation
           hypothesis is load-bearing).
  CHECK 5  Lemma D exact: dependency -> g reconstruction; laws (D1),
           (D2), deg g <= n-j-2, |I| >= ceil((j+2)/2), on the q-flat
           and on a census flat.
  CHECK 6  Mobius involution census: non-Dih max disjoint pairs on
           F_17^* is 7 (160 attainers), Dih max is 8; mu_8 collapse
           of the q-construction to m = 2.
  CHECK 7  randomized exact n = 16 checks: pullback flats get e >= 2
           and Theorem 1(b) holds on every psi-fiber pair; random
           background flats get e = 1 and m <= 3.

Run:  python3 experimental/scripts/verify_f_matching_composition.py
"""
from __future__ import annotations

import itertools
import random
from collections import defaultdict

P = 17
N = 16
H = tuple(range(1, 17))
INV = {x: pow(x, P - 2, P) for x in H}


# ------------------------------------------------------------ F_17[x] helpers
def pnorm(a):
    a = [c % P for c in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    out = [0] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] = (out[i] + c) % P
    for i, c in enumerate(b):
        out[i] = (out[i] + c) % P
    return pnorm(out)


def pscale(a, s):
    return pnorm([c * s % P for c in a])


def pmul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            out[i + k] = (out[i + k] + x * y) % P
    return pnorm(out)


def pdivmod(a, b):
    a, b = pnorm(list(a)), pnorm(list(b))
    assert b, "division by zero poly"
    q = [0] * max(0, len(a) - len(b) + 1)
    inv_lead = INV[b[-1]]
    while len(a) >= len(b):
        s = a[-1] * inv_lead % P
        d = len(a) - len(b)
        q[d] = s
        a = pnorm([(a[i] - s * b[i - d]) % P if i >= d else a[i]
                   for i in range(len(a))])
        if not a:
            break
    return pnorm(q), a


def pgcd(a, b):
    a, b = pnorm(list(a)), pnorm(list(b))
    while b:
        a, b = b, pdivmod(a, b)[1]
    if a:
        a = pscale(a, INV[a[-1]])
    return a


def peval(a, x):
    acc = 0
    for c in reversed(a):
        acc = (acc * x + c) % P
    return acc


def pmul_linear(coeffs, root):
    out = [0] * (len(coeffs) + 1)
    for i, c in enumerate(coeffs):
        out[i] = (out[i] - root * c) % P
        out[i + 1] = (out[i + 1] + c) % P
    return pnorm(out)


# -------------------------------------------------- linear algebra mod P
def rref(rows, width):
    work = [[e % P for e in row] for row in rows]
    rank = 0
    for col in range(width):
        piv = None
        for r in range(rank, len(work)):
            if work[r][col]:
                piv = r
                break
        if piv is None:
            continue
        work[rank], work[piv] = work[piv], work[rank]
        s = INV[work[rank][col]]
        work[rank] = [(s * e) % P for e in work[rank]]
        for r in range(len(work)):
            if r != rank and work[r][col]:
                m = work[r][col]
                work[r] = [(work[r][i] - m * work[rank][i]) % P
                           for i in range(width)]
        rank += 1
        if rank == len(work):
            break
    return [tuple(row) for row in work[:rank]]


def nullspace(rows, width):
    red = rref([list(r) for r in rows], width)
    pivots = []
    for row in red:
        for col in range(width):
            if row[col]:
                pivots.append(col)
                break
    free = [c for c in range(width) if c not in pivots]
    basis = []
    for f in free:
        v = [0] * width
        v[f] = 1
        for r, pc in zip(red, pivots):
            v[pc] = (-r[f]) % P
        basis.append(tuple(v))
    return basis


# ------------------------------------- composition degree e (bivariate gcd)
# Bivariate polynomials in y with coefficients in F_17[x] are lists (by
# y-degree) of coefficient polynomials.  Primitive PRS gcd over F_17(x)[y].
def bnorm(A):
    A = [pnorm(list(c)) for c in A]
    while A and not A[-1]:
        A.pop()
    return A


def bcontent(A):
    g = []
    for c in A:
        g = pgcd(g, c) if g else pnorm(list(c))
    return g


def bprim(A):
    A = bnorm(A)
    if not A:
        return A
    cont = bcontent(A)
    return [pdivmod(c, cont)[0] for c in A]


def bscale_poly(A, s):
    return bnorm([pmul(c, s) for c in A])


def bsub(A, B):
    out = [list(c) for c in A] + [[]] * max(0, len(B) - len(A))
    out = [pnorm(c) for c in out]
    for i, c in enumerate(B):
        out[i] = padd(out[i], pscale(c, P - 1))
    return bnorm(out)


def bshift(A, k):
    return bnorm([[]] * k + [pnorm(list(c)) for c in A])


def pseudo_rem(A, B):
    """Pseudo-remainder of A by B in (F_17[x])[y]."""
    A, B = bnorm(A), bnorm(B)
    assert B
    lb = B[-1]
    while len(A) >= len(B):
        la = A[-1]
        A = bsub(bscale_poly(A, lb), bshift(bscale_poly(B, la),
                                            len(A) - len(B)))
        A = bnorm(A)
        if not A:
            break
    return A


def bgcd(A, B):
    A, B = bprim(A), bprim(B)
    if not A:
        return B
    if not B:
        return A
    if len(A) < len(B):
        A, B = B, A
    while B:
        R = bprim(pseudo_rem(A, B))
        A, B = B, R
    return bprim(A)


def collision_biform(u, v):
    """G(x,y) = u(x)v(y) - u(y)v(x) as element of (F_17[x])[y].

    y-coefficient of degree t:  v[t]*u(x) - u[t]*v(x)."""
    u, v = pnorm(list(u)), pnorm(list(v))
    deg = max(len(u), len(v)) - 1
    out = []
    for t in range(deg + 1):
        ut = u[t] if t < len(u) else 0
        vt = v[t] if t < len(v) else 0
        out.append(padd(pscale(u, vt), pscale(v, P - ut)))
    return bnorm(out)


def composition_degree(basis):
    """e = [Kbar(x) : Kbar(P_2/P_1, ..., P_r/P_1)] via deg_y of the gcd of
    the reduced collision biforms (generic fiber of the joint ratio map)."""
    polys = [pnorm(list(b)) for b in basis]
    w = polys[0]
    for q in polys[1:]:
        w = pgcd(w, q)
    red = [pdivmod(q, w)[0] for q in polys]
    p1 = red[0]
    G = None
    for pk in red[1:]:
        g = pgcd(pk, p1)
        u, v = pdivmod(pk, g)[0], pdivmod(p1, g)[0]
        bf = collision_biform(u, v)
        G = bf if G is None else bgcd(G, bf)
        if G and len(G) - 1 == 1:
            break
    assert G, "degenerate ratio tuple (proportional basis members?)"
    return len(G) - 1


# ----------------------------------------------------------- flat analysis
def eval_columns(basis, d):
    cols = {}
    for x in H:
        cols[x] = tuple(peval(list(b), x) for b in basis)
    return cols


def collision_classes(cols, d):
    """Zero columns + projective classes of nonzero columns."""
    zero = [x for x in H if not any(cols[x])]
    classes = defaultdict(list)
    for x in H:
        c = cols[x]
        if not any(c):
            continue
        piv = next(i for i in range(d) if c[i])
        s = INV[c[piv]]
        classes[(piv, tuple((s * e) % P for e in c))].append(x)
    return zero, sorted(classes.values(), key=lambda v: (len(v), v),
                        reverse=True)


def matching_edges(classes):
    """Greedy disjoint pairing inside classes: (a, b, ratio) triples with
    ratio c s.t. col(b) = c col(a) is recovered by the caller."""
    edges = []
    for cl in classes:
        for i in range(0, len(cl) - 1, 2):
            edges.append((cl[i], cl[i + 1]))
    return edges


def column_ratio(cols, a, b, d):
    ca, cb = cols[a], cols[b]
    piv = next(i for i in range(d) if ca[i])
    c = cb[piv] * INV[ca[piv]] % P
    assert all((c * ca[i] - cb[i]) % P == 0 for i in range(d))
    return c


def matching_ratio(cols, d, gamma):
    rho = {}
    for x in H:
        y = gamma(x)
        cx, cy = cols[x], cols[y]
        zx, zy = not any(cx), not any(cy)
        if zx or zy:
            if zx != zy:
                return None
            continue
        piv = next(i for i in range(d) if cx[i])
        r = (cy[piv] * INV[cx[piv]]) % P
        if any((r * cx[i] - cy[i]) % P for i in range(d)):
            return None
        rho[x] = r
    return rho


def dih16_profile(cols, d):
    """Full Dih_16 element scan (E35 conventions)."""
    rot = []
    for u in H:
        if u == 1:
            continue
        rho = matching_ratio(cols, d, lambda x, u=u: (u * x) % P)
        if rho is None:
            continue
        vals = set(rho.values())
        if len(vals) == 1:
            rot.append(u)
    refl = []
    for b in H:
        rho = matching_ratio(cols, d, lambda x, b=b: (b * INV[x]) % P)
        if rho is None or not rho:
            continue
        xs = sorted(rho)
        for k in range(16):
            c = (rho[xs[0]] * pow(INV[xs[0]], k, P)) % P
            if all((c * pow(x, k, P) - rho[x]) % P == 0 for x in xs):
                refl.append(b)
                break
    return rot, refl


def group_orbits(rot, refl, points):
    """Orbits on `points` of the subgroup generated by detected elements."""
    gens = [(lambda x, u=u: (u * x) % P) for u in rot]
    gens += [(lambda x, b=b: (b * INV[x]) % P) for b in refl]
    parent = {x: x for x in points}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x in points:
        for g in gens:
            y = g(x)
            if y in parent:
                parent[find(x)] = find(y)
    orb = defaultdict(list)
    for x in points:
        orb[find(x)].append(x)
    return sorted(orb.values(), key=lambda v: (len(v), v), reverse=True)


# --------------------------------------------- E35 census reconstructions
def divisors_of_degree(j):
    out = []
    for roots in itertools.combinations(H, j):
        coeffs = [1]
        for r in roots:
            coeffs = pmul_linear(coeffs, r)
        out.append(tuple(c % P for c in coeffs + [0] * (j + 1 - len(coeffs))))
    return out


def symmetric_census(j):
    """All maximal in-degree dim-3 symmetry strata (E35's construction)."""
    width = j + 1
    found = {}
    for u in H:
        if u == 1:
            continue
        for rho in H:
            sup = [i for i in range(width) if (pow(u, i, P) - rho) % P == 0]
            if len(sup) >= 3:
                assert len(sup) == 3
                basis = [tuple(1 if e == i else 0 for e in range(width))
                         for i in sup]
                key = tuple(rref([list(v) for v in basis], width))
                found.setdefault(key, f"rot:u={u}")
    for b in H:
        for k in range(16):
            for c in H:
                if (c * c % P) * pow(b, k, P) % P != 1:
                    continue
                rows = []
                for x in H:
                    y = (b * INV[x]) % P
                    rows.append(tuple((pow(y, i, P) - c * pow(x, k + i, P))
                                      % P for i in range(width)))
                ker = nullspace(rows, width)
                if len(ker) >= 3:
                    assert len(ker) == 3
                    key = tuple(rref([list(v) for v in ker], width))
                    found.setdefault(key, f"dih:b={b}:k={k}:c={c}")
    return sorted((lbl, [tuple(r) for r in key]) for key, lbl in found.items())


def make_near_pencil_flats(j, d, count):
    """E35's exact seeded near-pencil constructor, keeping (q, shifts, v)."""
    rng = random.Random(f"E35:nearpencil:{j}:{d}")
    width = j + 1
    deg_q = j - (d - 2)
    out = []
    while len(out) < count:
        roots = rng.sample(H, deg_q)
        q = [1]
        for r in roots:
            q = pmul_linear(q, r)
        vecs = []
        for sh in range(d - 1):
            v = [0] * width
            for i, c in enumerate(q):
                v[i + sh] = c
            vecs.append(tuple(v))
        v = tuple(rng.randrange(P) for _ in range(width))
        if any(peval(list(v), y) == 0 for y in roots):
            continue
        basis = rref([list(w) for w in vecs] + [list(v)], width)
        if len(basis) == d:
            out.append((tuple(roots), [tuple(q) + (0,) * (width - len(q))]
                        + vecs[1:] + [v]))
    return out


def make_random_flats(j, d, count):
    rng = random.Random(f"E35:random:{j}:{d}")
    width = j + 1
    out = []
    while len(out) < count:
        vecs = [tuple(rng.randrange(P) for _ in range(width))
                for _ in range(d)]
        basis = rref([list(v) for v in vecs], width)
        if len(basis) == d:
            out.append([tuple(r) for r in basis])
    return out


# -------------------------------------------------------------- the checks
def check1():
    q = (0, 3, 1)
    q2 = pmul(list(q), list(q))
    flat = [(1, 0, 0, 0, 0), tuple(list(q) + [0, 0]),
            tuple(q2 + [0] * (5 - len(q2)))]
    cols = eval_columns(flat, 3)
    zero, classes = collision_classes(cols, 3)
    profile = tuple(sorted((len(c) for c in classes), reverse=True))
    w2m = sum(len(c) // 2 for c in classes)
    rot, refl = dih16_profile(cols, 3)
    ok = (not zero and w2m == 7 and profile == (2,) * 7 + (1,) * 2
          and not rot and not refl)
    # divisor-span identity
    def qs(c):
        return [(q[0] - c) % P, q[1], q[2]]
    d1 = pmul(qs(4), qs(10))
    d2 = pmul(qs(4), qs(1))
    d3 = pmul(qs(10), qs(1))
    for dd in (d1, d2, d3):
        roots = [x for x in H if peval(dd, x) == 0]
        ok &= len(roots) == 4 and len(set(roots)) == 4
    span = rref([d1, d2, d3], 5)
    ok &= span == rref([list(v) for v in flat], 5)
    # composition degree and Theorem 1(b) on the iota-fibers
    e = composition_degree(flat)
    ok &= e == 2
    iota = lambda x: (14 - x) % P
    fib_pairs = {frozenset((x, iota(x))) for x in H
                 if iota(x) in H and iota(x) != x}
    edge_pairs = {frozenset(c) for c in classes if len(c) == 2}
    ok &= edge_pairs == fib_pairs and len(fib_pairs) == 7
    for pair in fib_pairs:
        a, b = sorted(pair)
        column_ratio(cols, a, b, 3)      # asserts flat-wide ratio edge
    print(f"CHECK 1 q-flat counterexample: w2m={w2m} profile={profile} "
          f"Dih16=none e={e}  {'PASS' if ok else 'FAIL'}")
    return ok


def check2():
    ok = True
    n_flats = 0
    for j in (4, 5):
        for lbl, basis in symmetric_census(j):
            n_flats += 1
            e = composition_degree(basis)
            if e < 2:
                ok = False
                print(f"  census {lbl} j={j}: e={e} < 2 FAIL")
                continue
            cols = eval_columns(basis, 3)
            zero, classes = collision_classes(cols, 3)
            if zero:
                continue                  # not post-strip: only e-check
            sizes = [len(c) for c in classes]
            n_exc = sum(1 for s in sizes if s != e)
            if not all(s <= e for s in sizes) or n_exc > 2 * e - 2:
                ok = False
                print(f"  census {lbl} j={j}: sizes={sizes} e={e} FAIL")
            rot, refl = dih16_profile(cols, 3)
            orbits = group_orbits(rot, refl, [x for x in H if any(cols[x])])
            if sorted(map(sorted, orbits)) != sorted(map(sorted, classes)):
                ok = False
                print(f"  census {lbl} j={j}: classes != group orbits FAIL")
            for cl in classes:
                for a, b in itertools.combinations(cl, 2):
                    column_ratio(cols, a, b, 3)   # derived phi-form edges
    print(f"CHECK 2 census artifacts ({n_flats} strata): e>=2, classes = "
          f"Dih orbits, exceptions <= 2e-2  {'PASS' if ok else 'FAIL'}")
    return ok


def check3():
    ok = True
    tested = 0
    for j, d, cnt in ((4, 3, 30), (5, 3, 30)):
        for roots, vecs in make_near_pencil_flats(j, d, cnt):
            tested += 1
            e = composition_degree(vecs)
            ok &= e == 1
            cols = eval_columns(vecs, d)
            zero, classes = collision_classes(cols, d)
            ok &= not zero
            for cl in classes:
                if len(cl) >= 2:
                    ok &= all(x in roots for x in cl)
            Dd = max(len(pnorm(list(v))) - 1 for v in vecs)
            m = sum(len(c) // 2 for c in classes)
            ok &= m <= Dd + (Dd - 1) ** 2
    print(f"CHECK 3 near-pencils ({tested}): e=1 (Mobius ratio clause), "
          f"edges on Z(P_1), m <= D+(D-1)^2  {'PASS' if ok else 'FAIL'}")
    return ok


def rational_collisions(pair):
    """Ordered K-rational collision pairs of a tuple of polynomials."""
    cnt = 0
    for x in H + (0,):
        for y in H + (0,):
            if x == y:
                continue
            if all(peval(list(f), x) == peval(list(f), y) for f in pair):
                cnt += 1
    return cnt


def check4():
    rng = random.Random("FMC:lemmaB")
    ok = True
    for _ in range(25):
        f = [rng.randrange(P) for _ in range(6)]
        g = [rng.randrange(P) for _ in range(6)]
        basis = [(1, 0, 0, 0, 0, 0), tuple(f), tuple(g)]
        if len(rref([list(v) for v in basis], 6)) != 3:
            continue
        e = composition_degree(basis)
        F = max(len(pnorm(f)) - 1, len(pnorm(g)) - 1)
        if e == 1:
            ok &= rational_collisions((f, g)) <= 2 * (F - 1) ** 2
    # non-generating pair: functions of x^2 -> e = 2, big collision set
    A = (3, 0, 1)                       # x^2 + 3
    B = (0, 0, 5, 0, 1)                 # x^4 + 5x^2
    basis = [(1, 0, 0, 0, 0), tuple(A) + (0, 0), tuple(B)]
    e = composition_degree(basis)
    ok &= e == 2 and rational_collisions((A, B)) >= 14
    print(f"CHECK 4 Lemma B sanity: generating pairs within 2(F-1)^2; "
          f"non-generating pair e=2, collisions >= 14  "
          f"{'PASS' if ok else 'FAIL'}")
    return ok


def lemma_d_on(flat, j, d):
    cols = eval_columns(flat, d)
    zero, classes = collision_classes(cols, d)
    assert not zero
    edges = [(a, b, column_ratio(cols, a, b, d))
             for a, b in matching_edges(classes)]
    m = len(edges)
    r = d
    if m < j + 2 - r:
        return None
    rows = []                            # (j+1) x m matrix, columns l_i
    for s in range(j + 1):
        rows.append([(pow(b, s, P) - c * pow(a, s, P)) % P
                     for a, b, c in edges])
    ker = nullspace([tuple(row) for row in rows], m)
    assert ker, "expected a dependency at m >= j + 2 - r"
    t = ker[0]
    v = {x: 0 for x in H}
    for (a, b, c), ti in zip(edges, t):
        v[b] = ti % P
        v[a] = (-ti * c) % P
    gvals = {x: v[x] * INV[x] % P for x in H}
    # Lagrange interpolation of g through all 16 points
    g = []
    for x0 in H:
        num, den = [1], 1
        for x1 in H:
            if x1 == x0:
                continue
            num = pmul(num, [(-x1) % P, 1])
            den = den * (x0 - x1) % P
        g = padd(g, pscale(num, gvals[x0] * INV[den] % P))
    deg_g = len(g) - 1 if g else -1
    I = [i for i, ti in enumerate(t) if ti % P]
    ok = 0 <= deg_g <= N - j - 2 and len(I) >= (j + 2 + 1) // 2
    support = set()
    for i in I:
        a, b, c = edges[i]
        support |= {a, b}
        ok &= c == (-a * peval(g, a) * INV[b * peval(g, b) % P]) % P  # (D2)
    ok &= all(peval(g, x) == 0 for x in H if x not in support)        # (D1)
    return ok, deg_g, len(I)


def check5():
    q = (0, 3, 1)
    q2 = pmul(list(q), list(q))
    qflat = [(1, 0, 0, 0, 0), tuple(list(q) + [0, 0]),
             tuple(q2 + [0] * (5 - len(q2)))]
    res1 = lemma_d_on(qflat, 4, 3)
    # a stripped census flat: reciprocal quartics
    cflat = [(1, 0, 0, 0, 1), (0, 1, 0, 1, 0), (0, 0, 1, 0, 0)]
    res2 = lemma_d_on(cflat, 4, 3)
    ok = bool(res1 and res1[0] and res2 and res2[0])
    print(f"CHECK 5 Lemma D: q-flat (deg g={res1[1]}, |I|={res1[2]}), "
          f"census flat (deg g={res2[1]}, |I|={res2[2]})  "
          f"{'PASS' if ok else 'FAIL'}")
    return ok


def check6():
    best = {}
    for a, b, c in itertools.product(range(P), repeat=3):
        if (-a * a - b * c) % P == 0:
            continue
        first = next((v for v in (a, b, c) if v), None)
        if first != 1:
            continue

        def iota(x):
            num, den = (a * x + b) % P, (c * x - a) % P
            return None if den == 0 else num * INV[den] % P

        pairs = {frozenset((x, iota(x))) for x in H
                 if iota(x) not in (None, 0, x) and iota(x) in H}
        dih = (b == 0 and c == 0) or a == 0
        best.setdefault((len(pairs), dih), 0)
        best[(len(pairs), dih)] += 1
    nd_max = max(m for m, d in best if not d)
    d_max = max(m for m, d in best if d)
    n7 = best.get((7, False), 0)
    mu8 = {x for x in H if pow(x, 8, P) == 1}
    mu8_edges = {frozenset((x, (14 - x) % P)) for x in mu8
                 if (14 - x) % P in mu8 and (14 - x) % P != x}
    ok = nd_max == 7 and d_max == 8 and n7 == 160 and len(mu8_edges) == 2
    print(f"CHECK 6 involutions: non-Dih max={nd_max} (attainers {n7}), "
          f"Dih max={d_max}; mu_8 collapse m={len(mu8_edges)}  "
          f"{'PASS' if ok else 'FAIL'}")
    return ok


def check7():
    ok = True
    rng = random.Random("FMC:pullback")
    psis = [(0, 0, 1), (0, 3, 1), (0, 5, 1), (0, 0, 0, 0, 1)]
    for psi in psis:
        deg = len(psi) - 1
        psi2 = pmul(list(psi), list(psi))
        if deg == 2:
            flat = [(1,) + (0,) * 4, tuple(psi) + (0,) * (5 - len(psi)),
                    tuple(psi2) + (0,) * (5 - len(psi2))]
        else:
            flat = [(1,) + (0,) * 4, tuple(psi)]
        d = len(flat)
        e = composition_degree(flat)
        ok &= e == deg
        cols = eval_columns(flat, d)
        for x in H:
            for y in H:
                if x < y and peval(list(psi), x) == peval(list(psi), y):
                    column_ratio(cols, x, y, d)   # Theorem 1(b), exact
        # random pencils inside the pullback algebra keep e >= 2
        for _ in range(3):
            co = [rng.randrange(P) for _ in range(6)]
            v1 = padd(padd(pscale([1], co[0]), pscale(list(psi), co[1])),
                      pscale(psi2, co[2]))
            v2 = padd(padd(pscale([1], co[3]), pscale(list(psi), co[4])),
                      pscale(psi2, co[5]))
            if len(v1) - 1 > 5 or len(v2) - 1 > 5:
                continue
            pencil = rref([list(v1) + [0] * (6 - len(v1)),
                           list(v2) + [0] * (6 - len(v2))], 6)
            if len(pencil) != 2:
                continue
            ok &= composition_degree(pencil) >= 2
    n_e1 = 0
    for basis in make_random_flats(4, 3, 100):
        cols = eval_columns(basis, 3)
        zero, classes = collision_classes(cols, 3)
        m = sum(len(c) // 2 for c in classes)
        e = composition_degree(basis)
        if e == 1:
            n_e1 += 1
            ok &= m <= 3
    ok &= n_e1 == 100
    print(f"CHECK 7 pullback/background at n=16: pullback e matches psi, "
          f"fibers are ratio edges; random flats {n_e1}/100 e=1, m<=3  "
          f"{'PASS' if ok else 'FAIL'}")
    return ok


def main():
    results = [check1(), check2(), check3(), check4(), check5(), check6(),
               check7()]
    print("f_matching_composition verifier:",
          "PASS (7/7)" if all(results) else "FAIL")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
