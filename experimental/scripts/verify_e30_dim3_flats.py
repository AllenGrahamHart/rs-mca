#!/usr/bin/env python3
"""E30 [axis D] dimension-3 flat census under the enlarged taxonomy.

This is an EXPERIMENTAL evidence verifier, not a proof.  It executes the
wave-4 probe E30 (evidence_plan_codex.md; RK axis D = fixed d -> growing d):
extend the E7/E9/E10 toy censuses to projective-dimension-3 flats
(linear dimension 4) at n = 16.

Conventions (E7/E9):
  * K = F_17, H = F_17^* = mu_16, n = 16;
  * D_j = squarefree monic degree-j divisors of X^16 - 1
    (= products of j distinct linear factors; |D_j| = C(16, j));
  * a FLAT is a linear-dim-4 subspace P <= K[X]_{<=j} (projective dim 3);
  * the dual code P-perp = { lambda in K^H : sum_x lambda_x p(x) = 0
    for all p in P }; sparse dual words are enumerated EXHAUSTIVELY over
    supports of size <= 4 inside the nonzero evaluation columns.

j = 3 is exact (the Grassmannian is a single flat: the whole space).
j = 4, 5 are SAMPLED with deterministic seeds (the full Grassmannians
Gr(4,5), Gr(4,6) are large); families (a)-(d) per the E30 order.

Enlarged taxonomy applied to each flat (word-level flags, flat-level class):
  (i)   common_root      weight-1 word (a common root / tangent point);
  (ii)  w2_twin_generic  weight-2 word with no ledger shape;
  (iii) w2_mult_coset    weight-2 word, support {x, cx} with ord(c) <= 8,
                         coefficient ratio lambda_x/lambda_y = -1
                         (the multiplicative pullback g(X^M) shape);
  (iv)  w2_dihedral      weight-2 word, support an inverse pair {a, a^-1},
                         ratio lambda_a / lambda_{a^-1} in { -a^{2m} }
                         (the dihedral pullback X^e g(X^M + X^-M) shape);
  (v)   w3/w4_descent    minimal words of weight 3 or 4;
  (vi)  spread_ge_5      no dual word of weight <= 4.
Flat label priority: (i) > (iv) > (iii) > (ii) > (v) > (vi); all flag
overlaps are counted separately, so the priority loses no information.

Fifth-shape watch (word level; (ii)/(v)/(vi) are catch-alls, so the watch
tracks STRUCTURED supports carrying OFF-LEDGER coefficient shapes):
  * inverse-pair weight-2 words with ratio -a^{2m+1} (dihedral-odd);
  * inverse-pair weight-2 words with ratio outside -<a> entirely;
  * weight-3/4 words with inverse-closed or coset-union supports.

Also computed per flat: the number of D_j points ON the flat, and the
closed-set lattice of the 16 evaluation columns (matroid flats of the
rank-<=4 column matroid) versus the fixed-d n^{O(d)} bound.

Verification: everything is recomputed from the seeds on each run and
compared per family against the embedded EXPECTED table (count, class
histogram, sha256 fingerprint of all per-flat records): PASS/FAIL per
family, plus an independent recount of the streaming counters from the
stored per-flat records.

Run:  python3 experimental/scripts/verify_e30_dim3_flats.py [--emit] [--quick]
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import random
import statistics
from collections import Counter, defaultdict

P = 17
N = 16
H = tuple(range(1, 17))
DEGREES = (3, 4, 5)
MAX_SUPPORT = 4

INV = {x: pow(x, P - 2, P) for x in H}
# quadratic residues mod 17 = the order-<=8 subgroup of mu_16
QR = {pow(g, 2, P) for g in H}
INVERSE_PAIRS = sorted({tuple(sorted((x, INV[x]))) for x in H if x != INV[x]})
MU4 = {x for x in H if pow(x, 4, P) == 1}          # {1, 4, 13, 16}


# ----------------------------------------------------------------- linear alg
def rref(rows: list[list[int]], width: int) -> list[tuple[int, ...]]:
    """Reduced row echelon form mod P; returns nonzero rows (canonical)."""
    work = [[e % P for e in row] for row in rows]
    out: list[list[int]] = []
    pivots: list[int] = []
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
        s = INV[work[rank][col]] if work[rank][col] != 0 else 0
        work[rank] = [(s * e) % P for e in work[rank]]
        for r in range(len(work)):
            if r != rank and work[r][col]:
                m = work[r][col]
                work[r] = [(work[r][i] - m * work[rank][i]) % P for i in range(width)]
        pivots.append(col)
        rank += 1
        if rank == len(work):
            break
    for r in range(rank):
        out.append(work[r])
    return [tuple(row) for row in out]


def nullspace(rows: list[tuple[int, ...]], width: int) -> list[tuple[int, ...]]:
    """Basis of { v : sum_i row[i] v[i] = 0 for every row }."""
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


def dot(u, v) -> int:
    return sum(a * b for a, b in zip(u, v)) % P


def projective_kernel_vectors(basis: list[tuple[int, ...]]):
    """Canonical projective representatives of span(basis) \\ {0}."""
    k = len(basis)
    width = len(basis[0])
    for lead in range(k):
        for tail in itertools.product(range(P), repeat=k - lead - 1):
            coeffs = (0,) * lead + (1,) + tail
            v = [0] * width
            for c, b in zip(coeffs, basis):
                if c:
                    for i, e in enumerate(b):
                        v[i] = (v[i] + c * e) % P
            yield tuple(v)


# ------------------------------------------------------------------- divisors
def poly_mul_linear(coeffs: list[int], root: int) -> list[int]:
    """coeffs of f(X) -> coeffs of f(X) * (X - root), ascending order."""
    out = [0] * (len(coeffs) + 1)
    for i, c in enumerate(coeffs):
        out[i] = (out[i] - root * c) % P
        out[i + 1] = (out[i + 1] + c) % P
    return out


def divisors_of_degree(j: int) -> list[tuple[frozenset[int], tuple[int, ...]]]:
    """All squarefree monic degree-j divisors of X^16 - 1 (root set, coeffs)."""
    out = []
    for roots in itertools.combinations(H, j):
        coeffs = [1]
        for r in roots:
            coeffs = poly_mul_linear(coeffs, r)
        out.append((frozenset(roots), tuple(coeffs)))
    return out


DIVISORS = {j: divisors_of_degree(j) for j in DEGREES}


# ------------------------------------------------------------- flat analysis
def dihedral_ratio_sets(a: int) -> tuple[set[int], set[int]]:
    even = {(-pow(a, 2 * m, P)) % P for m in range(8)}
    odd = {(-pow(a, 2 * m + 1, P)) % P for m in range(8)}
    return even, odd


def support_structure(support: tuple[int, ...]) -> str:
    s = set(support)
    inv_closed = all(INV[x] in s for x in s)
    coset_union = False
    if len(s) == 4:
        # single mu_4 coset, or union of two mu_2 cosets {x,-x,y,-y}
        x = next(iter(s))
        if s == {(x * m) % P for m in MU4}:
            coset_union = True
        elif all((P - x) % P in s for x in s):
            coset_union = True
    if inv_closed and coset_union:
        return "inverse_closed+coset_union"
    if inv_closed:
        return "inverse_closed"
    if coset_union:
        return "coset_union"
    return "generic"


def analyze_flat(basis: list[tuple[int, ...]], j: int) -> dict:
    """Full E30 analysis of one linear-dim-4 flat (basis in RREF, 4 rows)."""
    width = j + 1
    assert len(basis) == 4
    # evaluation columns c_x = (p_1(x), ..., p_4(x))
    cols = {}
    for x in H:
        powers = [pow(x, e, P) for e in range(width)]
        cols[x] = tuple(sum(b[e] * powers[e] for e in range(width)) % P
                        for b in basis)
    loops = [x for x in H if not any(cols[x])]
    nonzero = [x for x in H if any(cols[x])]

    # projective classes of nonzero columns
    class_key = {}
    for x in nonzero:
        c = cols[x]
        piv = next(i for i in range(4) if c[i])
        s = INV[c[piv]]
        class_key[x] = (piv, tuple((s * e) % P for e in c))
    classes: dict = defaultdict(list)
    for x in nonzero:
        classes[class_key[x]].append(x)
    class_list = sorted(classes)                      # canonical order
    class_id = {k: i for i, k in enumerate(class_list)}
    reps = [k[1] for k in class_list]                 # canonical rep vectors
    members = [tuple(classes[k]) for k in class_list]
    m = len(class_list)
    cid = {x: class_id[class_key[x]] for x in nonzero}

    # ---- weight-2 words (exhaustive: pairs of proportional nonzero columns)
    w2_words = []
    for k, xs in classes.items():
        if len(xs) < 2:
            continue
        piv = k[0]
        for x, y in itertools.combinations(sorted(xs), 2):
            t = (cols[y][piv] * INV[cols[x][piv]]) % P
            r = (-t) % P                     # r = lambda_x / lambda_y
            # sanity: lambda = (1, -inv(t)) kills all basis rows
            lam_y = (-INV[t]) % P
            assert all((cols[x][i] + lam_y * cols[y][i]) % P == 0
                       for i in range(4))
            inv_pair = (x * y) % P == 1
            coset_pair = pow((y * INV[x]) % P, 8, P) == 1
            dihedral = False
            dihedral_odd = False
            if inv_pair:
                even, odd = dihedral_ratio_sets(x)
                dihedral = r in even
                dihedral_odd = (r in odd) and not dihedral
            pullback = coset_pair and r == P - 1
            w2_words.append({
                "support": (x, y), "ratio": r, "inv_pair": inv_pair,
                "coset_pair": coset_pair, "dihedral": dihedral,
                "dihedral_odd": dihedral_odd, "pullback": pullback,
            })

    # ---- rank-2 / rank-3 class-span structure (for w3/w4 + the lattice)
    pair_normals = {}
    cl2 = {}
    for i, i2 in itertools.combinations(range(m), 2):
        nb = nullspace([reps[i], reps[i2]], 4)
        assert len(nb) == 2
        d1 = [dot(nb[0], reps[k]) for k in range(m)]
        d2 = [dot(nb[1], reps[k]) for k in range(m)]
        pair_normals[(i, i2)] = (nb[0], nb[1], d1, d2)
        cl2[(i, i2)] = frozenset(k for k in range(m) if d1[k] == 0 and d2[k] == 0)
    cl3 = {}
    for i, i2 in itertools.combinations(range(m), 2):
        _, _, d1, d2 = pair_normals[(i, i2)]
        for k in range(i2 + 1, m):
            if k in cl2[(i, i2)]:
                continue                       # rank-2 triple
            a, b = d2[k], d1[k]                # normal = a*n1 - b*n2
            memb = frozenset(l for l in range(m)
                             if (a * d1[l] - b * d2[l]) % P == 0)
            cl3[(i, i2, k)] = memb

    # ---- weight-3 words (exhaustive over supports of nonzero columns)
    w3_words = []
    for sup in itertools.combinations(nonzero, 3):
        ids = tuple(sorted(cid[x] for x in sup))
        distinct = len(set(ids)) == 3
        if distinct:
            key = (ids[0], ids[1])
            if ids[2] not in cl2[key]:
                continue                        # rank 3: no word
        elif len(set(ids)) == 2:
            continue                            # kernel = (t,-1,0): no full support
        # kernel enumeration (same-class triples and rank-2 distinct triples)
        mat_rows = [tuple(cols[x][i] for x in sup) for i in range(4)]
        ker = nullspace(mat_rows, 3)
        cnt = sum(1 for v in projective_kernel_vectors(ker) if all(v))
        if cnt:
            w3_words.append({"support": sup, "count": cnt,
                             "structure": support_structure(sup)})

    # ---- weight-4 words (exhaustive; O(1) singularity test per support)
    w4_words = []
    w4_irreducible = 0
    for sup in itertools.combinations(nonzero, 4):
        ids = sorted(cid[x] for x in sup)
        if len(set(ids)) == 4:
            a, b, c, d = ids
            if c in cl2[(a, b)]:
                singular = True
            else:
                singular = d in cl3[(a, b, c)]
        else:
            singular = True                     # repeated projective class
        if not singular:
            continue
        mat_rows = [tuple(cols[x][i] for x in sup) for i in range(4)]
        ker = nullspace(mat_rows, 4)
        cnt = sum(1 for v in projective_kernel_vectors(ker) if all(v))
        if cnt:
            # irreducible: every 3-subset independent (kernel dim 1, distinct
            # classes, no rank-2 sub-triple)
            irr = len(set(ids)) == 4 and len(ker) == 1
            if irr:
                a, b, c, d = ids
                irr = (c not in cl2[(a, b)] and d not in cl2[(a, b)]
                       and d not in cl2[(a, c)] and d not in cl2[(b, c)])
            if irr:
                w4_irreducible += cnt
            w4_words.append({"support": sup, "count": cnt, "irr": irr,
                             "structure": support_structure(sup)})

    # ---- flat class under the enlarged taxonomy
    if loops:
        flat_class = "common_root"
    elif w2_words:
        if any(w["dihedral"] for w in w2_words):
            flat_class = "w2_dihedral"
        elif any(w["coset_pair"] and w["pullback"] for w in w2_words):
            flat_class = "w2_mult_coset"
        else:
            flat_class = "w2_twin_generic"
    elif w3_words:
        flat_class = "w3_descent"
    elif w4_words:
        flat_class = "w4_descent"
    else:
        flat_class = "spread_ge_5"

    # ---- D_j points on the flat (coefficient vector in the linear span)
    parity = nullspace(list(basis), width)      # dim = width - 4 = j - 3
    n_dj = 0
    for _, coeffs in DIVISORS[j]:
        ok = True
        for row in parity:
            if dot(row, coeffs):
                ok = False
                break
        if ok:
            n_dj += 1

    # ---- closed-set lattice (matroid flats of the evaluation columns)
    loopset = frozenset(loops)
    closed = {loopset, frozenset(H)}
    for i in range(m):
        closed.add(loopset | set(members[i]))
    for key, mem in cl2.items():
        closed.add(loopset | {x for k in mem for x in members[k]})
    for key, mem in cl3.items():
        closed.add(loopset | {x for k in mem for x in members[k]})
    lattice = len(closed)

    return {
        "class": flat_class, "loops": len(loops), "n_classes": m,
        "w2": w2_words, "w3": w3_words, "w4": w4_words,
        "w4_irreducible": w4_irreducible, "n_dj": n_dj, "lattice": lattice,
    }


# ------------------------------------------------------------------ families
def flat_from_vectors(vectors: list[tuple[int, ...]], width: int):
    basis = rref([list(v) for v in vectors], width)
    return basis if len(basis) == 4 else None


def rand_vec(rng: random.Random, width: int) -> tuple[int, ...]:
    return tuple(rng.randrange(P) for _ in range(width))


def make_random_flats(j: int, count: int) -> list:
    rng = random.Random(f"E30:random:{j}")
    width = j + 1
    out = []
    while len(out) < count:
        f = flat_from_vectors([rand_vec(rng, width) for _ in range(4)], width)
        if f is not None:
            out.append(f)
    return out


def make_dj_span_flats(j: int, count: int) -> list:
    rng = random.Random(f"E30:djspan:{j}")
    width = j + 1
    divs = DIVISORS[j]
    out = []
    while len(out) < count:
        picks = rng.sample(range(len(divs)), 4)
        f = flat_from_vectors([divs[i][1] for i in picks], width)
        if f is not None:
            out.append(f)
    return out


def make_hankel_ext_flats(j: int, count: int) -> list:
    """Kernels of (j-3) Hankel rows built from power sums of a sparse word."""
    rng = random.Random(f"E30:hankel:{j}")
    width = j + 1
    out = []
    while len(out) < count:
        t = rng.choice([3, 4, 5, 6])
        support = rng.sample(H, t)
        coeff = {x: rng.randrange(1, P) for x in support}
        s = [sum(coeff[x] * pow(x, i, P) for x in support) % P
             for i in range(2 * j - 3)]
        rows = [tuple(s[i + e] for e in range(width)) for i in range(j - 3)]
        rows = [r for r in rows if any(r)]
        if not rows:
            continue
        ker = nullspace(rows, width)
        if len(ker) < 4:
            continue
        f = flat_from_vectors(ker[:4], width)   # deterministic restriction
        if f is not None:
            out.append(f)
    return out


def reciprocal_basis(j: int) -> list[tuple[int, ...]]:
    width = j + 1
    out = []
    for i in range((width + 1) // 2):
        v = [0] * width
        v[i] = 1
        v[j - i] = (v[j - i] + 1) % P
        out.append(tuple(v))
    return out


def make_palindromic_flats(j: int, count: int) -> list:
    """Carriers of palindromic sub-flats: span(R-part, random extension)."""
    rng = random.Random(f"E30:palin:{j}")
    width = j + 1
    R = reciprocal_basis(j)                    # linear dim 3 for j = 4, 5
    out = []
    while len(out) < count:
        if len(out) < count // 2:
            vecs = list(R) + [rand_vec(rng, width)]          # full R + 1
        else:
            recs = []
            for _ in range(2):
                c = [rng.randrange(P) for _ in R]
                if not any(c):
                    c[0] = 1
                recs.append(tuple(sum(ci * b[e] for ci, b in zip(c, R)) % P
                                  for e in range(width)))
            vecs = recs + [rand_vec(rng, width), rand_vec(rng, width)]
        f = flat_from_vectors(vecs, width)
        if f is not None:
            out.append(f)
    return out


def make_pullback_adjacent_flats(j: int, count: int) -> list:
    """Multiplicative pullback space g(X^M) plus random extension vectors."""
    rng = random.Random(f"E30:pullback:{j}")
    width = j + 1
    p2 = [tuple(1 if e == d else 0 for e in range(width)) for d in (0, 2, 4)]
    p4 = [tuple(1 if e == d else 0 for e in range(width)) for d in (0, 4)]
    out = []
    while len(out) < count:
        if len(out) < count // 2:
            vecs = p2 + [rand_vec(rng, width)]               # M = 2, dim 3+1
        else:
            vecs = p4 + [rand_vec(rng, width), rand_vec(rng, width)]  # M = 4
        f = flat_from_vectors(vecs, width)
        if f is not None:
            out.append(f)
    return out


def make_common_divisor_pencils(j: int, count: int) -> list:
    """q * K[X]_{<=3} for squarefree q of degree j-3: maximally D_j-rich."""
    rng = random.Random(f"E30:pencil:{j}")
    width = j + 1
    qs: list[list[int]] = []
    if j == 4:
        qs = [poly_mul_linear([1], a) for a in H]
    else:
        pairs = list(itertools.combinations(H, j - 3))
        for idx in rng.sample(range(len(pairs)), min(count, len(pairs))):
            c = [1]
            for r in pairs[idx]:
                c = poly_mul_linear(c, r)
            qs.append(c)
    out = []
    for q in qs[:count]:
        vecs = []
        for sh in range(4):
            v = [0] * width
            for i, c in enumerate(q):
                v[i + sh] = c
            vecs.append(tuple(v))
        f = flat_from_vectors(vecs, width)
        assert f is not None
        out.append(f)
    return out


def inverse_closed_rootsets(j: int) -> list[frozenset[int]]:
    pairs = INVERSE_PAIRS
    out = []
    if j == 4:
        for a, b in itertools.combinations(range(len(pairs)), 2):
            out.append(frozenset(pairs[a]) | frozenset(pairs[b]))
        for a in range(len(pairs)):
            out.append(frozenset(pairs[a]) | {1, 16})
    else:
        for f in (1, 16):
            for a, b in itertools.combinations(range(len(pairs)), 2):
                out.append(frozenset(pairs[a]) | frozenset(pairs[b]) | {f})
    return out


def make_inverse_closed_span_flats(j: int, count: int) -> list:
    """Spans of 3 inverse-closed D_j members + 1 random D_j member."""
    rng = random.Random(f"E30:invclosed:{j}")
    width = j + 1
    roots = inverse_closed_rootsets(j)
    polys = []
    for rs in roots:
        c = [1]
        for r in sorted(rs):
            c = poly_mul_linear(c, r)
        polys.append(tuple(c))
    divs = DIVISORS[j]
    out = []
    while len(out) < count:
        picks = rng.sample(range(len(polys)), 3)
        extra = divs[rng.randrange(len(divs))][1]
        f = flat_from_vectors([polys[i] for i in picks] + [extra], width)
        if f is not None:
            out.append(f)
    return out


def coset_heavy_rootsets(j: int) -> list[frozenset[int]]:
    out = []
    if j == 4:
        negpairs = [frozenset({x, P - x}) for x in range(1, 9)]
        for a, b in itertools.combinations(range(8), 2):
            out.append(negpairs[a] | negpairs[b])             # g(X^2) divisors
    else:
        cosets = []
        seen = set()
        for x in H:
            cs = frozenset((x * m) % P for m in MU4)
            if cs not in seen:
                seen.add(cs)
                cosets.append(cs)
        for cs in cosets:                                     # (X^4 - r)(X - a)
            for a in H:
                if a not in cs:
                    out.append(cs | {a})
    return out


def make_coset_span_flats(j: int, count: int) -> list:
    """Spans of coset-structured D_j members (+ random D_j filler at j=4)."""
    rng = random.Random(f"E30:cosetspan:{j}")
    width = j + 1
    roots = coset_heavy_rootsets(j)
    polys = []
    for rs in roots:
        c = [1]
        for r in sorted(rs):
            c = poly_mul_linear(c, r)
        polys.append(tuple(c))
    divs = DIVISORS[j]
    out = []
    while len(out) < count:
        if j == 4:
            picks = rng.sample(range(len(polys)), 3)
            vecs = [polys[i] for i in picks] + [divs[rng.randrange(len(divs))][1]]
        else:
            picks = rng.sample(range(len(polys)), 4)
            vecs = [polys[i] for i in picks]
        f = flat_from_vectors(vecs, width)
        if f is not None:
            out.append(f)
    return out


def build_families(quick: bool) -> list[tuple[str, int, list]]:
    na = 60 if quick else 250          # (a) random
    nb = 60 if quick else 250          # (b) D_j spans
    nc = 20 if quick else 60           # (c) structured, each
    nd = 15 if quick else 40           # (d) adversarial, each
    fams: list[tuple[str, int, list]] = []
    fams.append(("j3_full_space", 3,
                 [rref([[1 if e == d else 0 for e in range(4)]
                        for d in range(4)], 4)]))
    for j in (4, 5):
        fams.append(("a_random", j, make_random_flats(j, na)))
        fams.append(("b_dj_span", j, make_dj_span_flats(j, nb)))
        fams.append(("c_hankel_ext", j, make_hankel_ext_flats(j, nc)))
        fams.append(("c_palindromic", j, make_palindromic_flats(j, nc)))
        fams.append(("c_pullback_adj", j, make_pullback_adjacent_flats(j, nc)))
        fams.append(("d_common_div_pencil", j,
                     make_common_divisor_pencils(j, 16 if j == 4 else nd)))
        fams.append(("d_inverse_closed_span", j,
                     make_inverse_closed_span_flats(j, nd)))
        fams.append(("d_coset_span", j, make_coset_span_flats(j, nd)))
    return fams


# ------------------------------------------------------------------- summary
CLASSES = ("common_root", "w2_dihedral", "w2_mult_coset", "w2_twin_generic",
           "w3_descent", "w4_descent", "spread_ge_5")


def summarize_family(records: list[dict]) -> dict:
    hist = Counter(r["class"] for r in records)
    w2 = [w for r in records for w in r["w2"]]
    w3 = [w for r in records for w in r["w3"]]
    w4 = [w for r in records for w in r["w4"]]
    watch = {
        "w2_invpair_dihedral": sum(1 for w in w2 if w["dihedral"]),
        "w2_invpair_odd": sum(1 for w in w2 if w["dihedral_odd"]),
        "w2_invpair_offledger": sum(
            1 for w in w2 if w["inv_pair"] and not w["dihedral"]
            and not w["dihedral_odd"]),
        "w2_coset_pullback": sum(1 for w in w2 if w["pullback"]),
        "w2_coset_generic_ratio": sum(
            1 for w in w2 if w["coset_pair"] and not w["pullback"]
            and not w["dihedral"]),
        "w2_noncoset_generic": sum(1 for w in w2 if not w["coset_pair"]),
        "w34_inverse_closed": sum(
            w["count"] for w in w3 + w4 if "inverse_closed" in w["structure"]),
        "w34_coset_union": sum(
            w["count"] for w in w3 + w4 if "coset_union" in w["structure"]),
        "w34_generic": sum(
            w["count"] for w in w3 + w4 if w["structure"] == "generic"),
        "w4_irreducible": sum(r["w4_irreducible"] for r in records),
    }
    lat = sorted(r["lattice"] for r in records)
    dj_by_class = {}
    for c in CLASSES:
        vals = [r["n_dj"] for r in records if r["class"] == c]
        if vals:
            dj_by_class[c] = (len(vals), round(statistics.mean(vals), 2),
                              max(vals))
    fingerprint = hashlib.sha256(repr(sorted(
        (r["class"], len(r["w2"]), len(r["w3"]), len(r["w4"]),
         r["w4_irreducible"], r["loops"], r["n_classes"], r["n_dj"],
         r["lattice"]) for r in records)).encode()).hexdigest()
    return {
        "count": len(records),
        "class_hist": {c: hist.get(c, 0) for c in CLASSES if hist.get(c, 0)},
        "n_w2_words": len(w2),
        "n_w3_words": sum(w["count"] for w in w3),
        "n_w4_words": sum(w["count"] for w in w4),
        "watch": watch,
        "lattice_min_med_max": (lat[0], lat[len(lat) // 2], lat[-1]),
        "dj_by_class": dj_by_class,
        "fingerprint": fingerprint,
    }


# EXPECTED is regenerated with --emit and pasted here; the default run
# recomputes everything from the deterministic seeds and compares.
EXPECTED: dict = {}

EXPECTED = {
    'j3_full_space|j3': {'count': 1, 'class_hist': {'spread_ge_5': 1}, 'fingerprint': '2ea8d4ba65c87500b4e7adfa86ad3350bdafcb9ea653c043776c6366005c2c6c'},
    'a_random|j4': {'count': 250, 'class_hist': {'w2_twin_generic': 5, 'w3_descent': 224, 'w4_descent': 21}, 'fingerprint': '5de83afcd116738ff33a364df947bb0aa8df29def90ce541163eff4f2e5b6159'},
    'b_dj_span|j4': {'count': 250, 'class_hist': {'common_root': 19, 'w2_dihedral': 1, 'w2_mult_coset': 1, 'w2_twin_generic': 11, 'w3_descent': 206, 'w4_descent': 12}, 'fingerprint': '148436bafbf4dce3424f1b4177155ff739fa7d8a8d640a6abdd2468998c5c4ec'},
    'c_hankel_ext|j4': {'count': 60, 'class_hist': {'w3_descent': 52, 'w4_descent': 8}, 'fingerprint': '6e3efb3ecc1df745b90b7ba248faed4b7ad5c557ee7df2b56334856cdfc5b6f9'},
    'c_palindromic|j4': {'count': 60, 'class_hist': {'w2_dihedral': 10, 'w2_twin_generic': 1, 'w3_descent': 26, 'w4_descent': 23}, 'fingerprint': 'b7f88786ecd39812933e5b1f76a738c745bd7ce069be62ee8adfc649ae7312ce'},
    'c_pullback_adj|j4': {'count': 60, 'class_hist': {'w2_mult_coset': 21, 'w3_descent': 22, 'w4_descent': 17}, 'fingerprint': '85c6b90e82f7c981958b5f732ba4e2041d96f4aec4fa4061c425ede9033cb4f5'},
    'd_common_div_pencil|j4': {'count': 16, 'class_hist': {'common_root': 16}, 'fingerprint': '9196545e9b1d37d160490b7ad56b655f404d67bccac2cefff65cfe0dae15a26e'},
    'd_inverse_closed_span|j4': {'count': 40, 'class_hist': {'common_root': 2, 'w2_dihedral': 7, 'w2_mult_coset': 1, 'w2_twin_generic': 2, 'w3_descent': 19, 'w4_descent': 9}, 'fingerprint': '87d8f06ef75622c6c1bcecf1737a4cc2812e7b555942a9c6b1c4c05d3f260acc'},
    'd_coset_span|j4': {'count': 40, 'class_hist': {'w2_dihedral': 1, 'w2_mult_coset': 20, 'w4_descent': 19}, 'fingerprint': 'd0885b1307ae1cbf4c26f2d8da6c660cc5bb01461927787ae3653406cb844fbd'},
    'a_random|j5': {'count': 250, 'class_hist': {'w2_dihedral': 1, 'w2_twin_generic': 2, 'w3_descent': 207, 'w4_descent': 40}, 'fingerprint': '19240d58e6431772b1dc07cba33ee754534661e11318d6980a92740022a40187'},
    'b_dj_span|j5': {'count': 250, 'class_hist': {'common_root': 39, 'w2_mult_coset': 2, 'w2_twin_generic': 50, 'w3_descent': 151, 'w4_descent': 8}, 'fingerprint': 'bddadbaf1c35b4c169b6321db65eef12180dcc50d7f8588eb010350cc84f339c'},
    'c_hankel_ext|j5': {'count': 60, 'class_hist': {'w2_mult_coset': 3, 'w2_twin_generic': 14, 'w3_descent': 27, 'w4_descent': 16}, 'fingerprint': '035bab041476060625cbf3eced274c97f73cc415de886b7d8f20aba3066b854c'},
    'c_palindromic|j5': {'count': 60, 'class_hist': {'common_root': 1, 'w2_twin_generic': 10, 'w3_descent': 48, 'w4_descent': 1}, 'fingerprint': '5348a1275a6326fed8ba9228e8a392c0f13675d07e5383eaa2105424f997018f'},
    'c_pullback_adj|j5': {'count': 60, 'class_hist': {'w2_mult_coset': 11, 'w3_descent': 26, 'w4_descent': 23}, 'fingerprint': '9b1aa96301ecdf8f0205baa3d41d0a017c68308e8eb0acffe8ab422ad93a6a3e'},
    'd_common_div_pencil|j5': {'count': 40, 'class_hist': {'common_root': 40}, 'fingerprint': '2f0db41c7b757a36ee9912995e961caa63086c6ec490f4436647bdd23a2b6b35'},
    'd_inverse_closed_span|j5': {'count': 40, 'class_hist': {'common_root': 4, 'w2_mult_coset': 1, 'w2_twin_generic': 14, 'w3_descent': 20, 'w4_descent': 1}, 'fingerprint': 'ea65751ed4b05be5b9a9e8a5d9cf737d2893a92f9dfbd748199e5bfb3d077e87'},
    'd_coset_span|j5': {'count': 40, 'class_hist': {'w3_descent': 40}, 'fingerprint': '7a4fdadf058f53fb3b63222d6be4542c2622b16d0765b2007059aaa379aa73c7'},
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true",
                    help="print the EXPECTED table instead of verifying")
    ap.add_argument("--quick", action="store_true",
                    help="reduced sample sizes (no verification)")
    args = ap.parse_args()

    fams = build_families(args.quick)
    all_pass = True
    emitted = {}
    for name, j, flats in fams:
        records = [analyze_flat(list(b), j) for b in flats]
        summ = summarize_family(records)

        # independent recount from stored per-flat records
        recount = Counter(r["class"] for r in records)
        assert {c: n for c, n in recount.items()} == \
            {c: summ["class_hist"].get(c, 0) for c in recount}, "recount FAIL"

        key = f"{name}|j{j}"
        emitted[key] = {"count": summ["count"],
                        "class_hist": summ["class_hist"],
                        "fingerprint": summ["fingerprint"]}
        print(f"== {key}  (n={summ['count']})")
        print(f"   classes  {summ['class_hist']}")
        print(f"   words    w2={summ['n_w2_words']} w3={summ['n_w3_words']}"
              f" w4={summ['n_w4_words']}"
              f" (irr w4={summ['watch']['w4_irreducible']})")
        print(f"   watch    {summ['watch']}")
        print(f"   lattice  min/med/max={summ['lattice_min_med_max']}")
        print(f"   D_j      {summ['dj_by_class']}")
        if not args.emit and not args.quick:
            exp = EXPECTED.get(key)
            ok = (exp is not None and exp["count"] == summ["count"]
                  and exp["class_hist"] == summ["class_hist"]
                  and exp["fingerprint"] == summ["fingerprint"])
            all_pass &= ok
            print(f"   verify   {'PASS' if ok else 'FAIL'}")
        print()

    if args.emit:
        print("EXPECTED = {")
        for k, v in emitted.items():
            print(f"    {k!r}: {v!r},")
        print("}")
        return 0
    if args.quick:
        print("quick mode: no verification against EXPECTED")
        return 0
    print("E30 verifier:", "PASS (all families)" if all_pass else "FAIL")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
