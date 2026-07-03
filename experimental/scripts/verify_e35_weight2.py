#!/usr/bin/env python3
"""E35 [face 2] weight-2 abundance column: minimal weight-2 supports vs
symmetry-stratum membership, on E30's census machinery.

EXPERIMENTAL evidence verifier, not a proof.  Wave-5 probe E35
(evidence_plan_codex.md WAVE 5; prize-DAG node f_weight2_inverse): for a
stratified sample of ~1450 flats, count the minimal weight-2 dual
supports EXACTLY and, independently, test containment in a symmetry
stratum; deliver (1) the joint distribution, (2) the abundance
threshold W*, (3) the falsifier hunt, (4) the near-symmetric collapse.

Conventions (E30/E7/E9): K = F_17, H = mu_16 = F_17^*, n = 16;
D_j = squarefree monic degree-j divisors of X^16 - 1; a FLAT is a
linear-dim-d subspace P <= K[X]_{<=j} (projective dim d-1),
d in {3,4,5}, j in {3,4,5}.

Minimal weight-2 supports (exhaustive): pairs {x, y} of NONZERO
proportional evaluation columns.  Zero columns are weight-1 words
(the common-root strip).  Two counts per flat, which diverge exactly
on rank-1 clusters (near-pencils):
  w2   raw count      = sum C(m, 2) over projective column classes;
  w2m  matching count = sum floor(m/2)  (max pairwise-DISJOINT supports).

Symmetry strata (function space on H, tested via group elements --
all 15 rotations x -> ux and all 16 reflections x -> b/x, i.e. every
subgroup conjugate inside Dih_16, both parities):
  MULT      flat in { g(X^M) }: c_{ux} = c_x for all x, some u != 1
            (constant ratio rho = 1);
  MULT-PROJ flat in { X^e g(X^M) }: c_{ux} = rho c_x, constant
            rho = u^e != 1 (projective/twisted pullback);
  DIH       flat in the (b, k, c) stratum { f : f(b/x) = c x^k f(x) }
            with c^2 b^k = 1.  Even k is the literal
            X^e g(X^M + b^M X^-M) form (k = -2e); odd k is the odd-j
            (anti-)reciprocal form lambda_a = -+ a^{-j+2m}
            lambda_{a^-1} of E30 finding 1.  Fixed points x^2 = b are
            handled by the same columnwise test (ratio 1 or forced
            zero column).
  sym_lit = MULT or DIH   (the literal stratum list of the DAG node);
  sym_ext = MULT-PROJ or DIH  (stratum list stated projectively).
Anomaly flags (falsifier detectors): a FULL proportional matching
under a rotation with NON-constant ratio, or under a reflection with
NON-monomial ratio function, would be a symmetry outside the finite
ledger.  Counted per flat in "anom".

Verification: everything is recomputed from deterministic seeds and
compared per family against the embedded EXPECTED table (count,
stripped/symmetry tallies, sha256 fingerprint of per-flat records),
plus a global EXPECTED_GLOBAL block (W* thresholds, floors, falsifier
tallies) and an independent recount of the joint table from the stored
records.  PASS/FAIL per family and globally.

Run:  python3 experimental/scripts/verify_e35_weight2.py [--emit]
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import random
from collections import Counter, defaultdict

P = 17
N = 16
H = tuple(range(1, 17))
DEGREES = (3, 4, 5)

INV = {x: pow(x, P - 2, P) for x in H}


# ----------------------------------------------------------------- linear alg
def rref(rows: list[list[int]], width: int) -> list[tuple[int, ...]]:
    """Reduced row echelon form mod P; returns nonzero rows (canonical)."""
    work = [[e % P for e in row] for row in rows]
    out: list[list[int]] = []
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


# ------------------------------------------------------------------- divisors
def poly_mul_linear(coeffs: list[int], root: int) -> list[int]:
    """coeffs of f(X) -> coeffs of f(X) * (X - root), ascending order."""
    out = [0] * (len(coeffs) + 1)
    for i, c in enumerate(coeffs):
        out[i] = (out[i] - root * c) % P
        out[i + 1] = (out[i + 1] + c) % P
    return out


def divisors_of_degree(j: int) -> list[tuple[int, ...]]:
    """All squarefree monic degree-j divisors of X^16 - 1 (coeff vectors)."""
    out = []
    for roots in itertools.combinations(H, j):
        coeffs = [1]
        for r in roots:
            coeffs = poly_mul_linear(coeffs, r)
        out.append(tuple(coeffs))
    return out


DIVISORS = {j: divisors_of_degree(j) for j in DEGREES}


# ------------------------------------------------------------- flat analysis
def eval_columns(basis: list[tuple[int, ...]], j: int) -> dict:
    """Evaluation columns c_x = (p_1(x), ..., p_d(x)) for x in H."""
    cols = {}
    for x in H:
        vals = []
        for b in basis:
            acc = 0
            for c in reversed(b):
                acc = (acc * x + c) % P
            vals.append(acc)
        cols[x] = tuple(vals)
    return cols


def w2_census(cols: dict, d: int):
    """Zero columns (weight-1) + projective classes of nonzero columns.

    Minimal weight-2 supports = pairs inside a class; raw count
    sum C(m,2), matching count sum floor(m/2)."""
    zero = [x for x in H if not any(cols[x])]
    classes: dict = defaultdict(list)
    for x in H:
        c = cols[x]
        if not any(c):
            continue
        piv = next(i for i in range(d) if c[i])
        s = INV[c[piv]]
        classes[(piv, tuple((s * e) % P for e in c))].append(x)
    sizes = tuple(sorted((len(v) for v in classes.values() if len(v) >= 2),
                         reverse=True))
    pairs = sum(m * (m - 1) // 2 for m in sizes)
    matching = sum(m // 2 for m in sizes)
    return zero, sizes, pairs, matching


def matching_ratio(cols: dict, d: int, gamma) -> dict | None:
    """rho with c_{gamma(x)} = rho(x) c_x for ALL x (zero <-> zero), or None."""
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


def symmetry_profile(cols: dict, d: int):
    """Group-element symmetry scan over all of Dih_16's elements."""
    rot = []            # (u, constant rho)
    rot_nonconst = 0
    for u in H:
        if u == 1:
            continue
        rho = matching_ratio(cols, d, lambda x, u=u: (u * x) % P)
        if rho is None:
            continue
        vals = set(rho.values())
        if len(vals) == 1:
            rot.append((u, vals.pop()))
        elif len(vals) > 1:
            rot_nonconst += 1
    refl = []           # (b, k, c) with rho(x) = c x^k
    refl_nonmono = 0
    for b in H:
        rho = matching_ratio(cols, d, lambda x, b=b: (b * INV[x]) % P)
        if rho is None or not rho:
            continue
        fit = None
        xs = sorted(rho)
        for k in range(16):
            c = (rho[xs[0]] * pow(INV[xs[0]], k, P)) % P
            if all((c * pow(x, k, P) - rho[x]) % P == 0 for x in xs):
                fit = (k, c)
                break
        if fit is not None:
            refl.append((b, fit[0], fit[1]))
        else:
            refl_nonmono += 1
    return rot, rot_nonconst, refl, refl_nonmono


def analyze_flat(basis: list[tuple[int, ...]], j: int, d: int) -> dict:
    cols = eval_columns(basis, j)
    zero, sizes, pairs, matching = w2_census(cols, d)
    rot, rot_nc, refl, refl_nm = symmetry_profile(cols, d)
    mult_strict = any(r == 1 for _, r in rot)
    mult_proj = bool(rot)
    dih = bool(refl)
    return {
        "w1": len(zero), "w2": pairs, "w2m": matching, "profile": sizes,
        "mult_strict": mult_strict, "mult_proj": mult_proj, "dih": dih,
        "dih_even": any(k % 2 == 0 for _, k, _ in refl),
        "dih_odd": any(k % 2 == 1 for _, k, _ in refl),
        "sym_lit": mult_strict or dih,
        "sym_ext": mult_proj or dih,
        "anom": rot_nc + refl_nm,
        "rot": tuple(sorted(rot)), "refl": tuple(sorted(refl)),
    }


# ----------------------------------------------- exhaustive symmetric census
def symmetric_census(j: int) -> list[tuple[str, list[tuple[int, ...]]]]:
    """ALL maximal in-degree symmetric spaces of dim 3 at degree <= j.

    Rotation strata { p : p(ux) = rho p(x) } (monomial-support classes)
    and reflection strata { p : p(b/x) = c x^k p(x) } for every b in H,
    every k mod 16, every c with c^2 b^k = 1 (both parities), computed
    as nullspaces of the 16 functional-equation rows on coefficient
    space.  Deduped by canonical RREF.  For j <= 5 every stratum has
    dim <= ceil((j+1)/2) <= 3, so members are the dim-3 strata
    themselves (asserted)."""
    width = j + 1
    found: dict = {}
    for u in H:
        if u == 1:
            continue
        for rho in H:
            sup = [i for i in range(width)
                   if (pow(u, i, P) - rho) % P == 0]
            if len(sup) >= 3:
                assert len(sup) == 3
                basis = [tuple(1 if e == i else 0 for e in range(width))
                         for i in sup]
                key = tuple(rref([list(v) for v in basis], width))
                found.setdefault(key, f"rot:u={u}:rho={rho}")
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
    return sorted((lbl, [tuple(r) for r in key])
                  for key, lbl in found.items())


# ------------------------------------------------------------------ families
def flat_from_vectors(vectors, width: int, d: int):
    basis = rref([list(v) for v in vectors], width)
    return [tuple(r) for r in basis] if len(basis) == d else None


def rand_vec(rng: random.Random, width: int) -> tuple[int, ...]:
    return tuple(rng.randrange(P) for _ in range(width))


def make_random_flats(j: int, d: int, count: int) -> list:
    rng = random.Random(f"E35:random:{j}:{d}")
    width = j + 1
    out = []
    while len(out) < count:
        f = flat_from_vectors([rand_vec(rng, width) for _ in range(d)],
                              width, d)
        if f is not None:
            out.append(f)
    return out


def make_djspan_flats(j: int, d: int, count: int) -> list:
    rng = random.Random(f"E35:djspan:{j}:{d}")
    width = j + 1
    divs = DIVISORS[j]
    out = []
    while len(out) < count:
        picks = rng.sample(range(len(divs)), d)
        f = flat_from_vectors([divs[i] for i in picks], width, d)
        if f is not None:
            out.append(f)
    return out


def make_carrier_flats(j: int, d: int, count: int, census: list) -> list:
    """Dim-3 symmetric stratum + (d-3) random extension vectors.

    Honest label (as in E30): carriers of symmetric sub-flats -- for
    j <= 5 no symmetry stratum has dim > 3, so no d >= 4 flat can be
    stratum-CONTAINED; these populate the near-symmetric nonsym side."""
    rng = random.Random(f"E35:carrier:{j}:{d}")
    width = j + 1
    out = []
    while len(out) < count:
        _, base = census[rng.randrange(len(census))]
        vecs = list(base) + [rand_vec(rng, width) for _ in range(d - 3)]
        f = flat_from_vectors(vecs, width, d)
        if f is not None:
            out.append(f)
    return out


def make_near_pencil_flats(j: int, d: int, count: int) -> list:
    """Rank-1 clusters WITHOUT symmetry and WITHOUT weight-1 words:
    span{q, qX, ...} + one generic vector nonvanishing on q's roots.
    The columns on q's root set S form ONE projective class of size
    |S| = deg q: C(|S|,2) raw weight-2 supports, matching floor(|S|/2).
    deg q = j-1 at d = 3 (2 shifts), j-2 at d = 4 (3 shifts)."""
    rng = random.Random(f"E35:nearpencil:{j}:{d}")
    width = j + 1
    deg_q = j - (d - 2)
    out = []
    while len(out) < count:
        roots = rng.sample(H, deg_q)
        q = [1]
        for r in roots:
            q = poly_mul_linear(q, r)
        vecs = []
        for sh in range(d - 1):
            v = [0] * width
            for i, c in enumerate(q):
                v[i + sh] = c
            vecs.append(tuple(v))
        v = rand_vec(rng, width)
        if any(sum(c * pow(y, i, P) for i, c in enumerate(v)) % P == 0
               for y in roots):
            continue
        f = flat_from_vectors(vecs + [v], width, d)
        if f is not None:
            out.append(f)
    return out


def make_perturbed_flats(j: int, s: int, count: int, census: list) -> list:
    """Symmetric census member with s random basis-matrix cells bumped
    by a random nonzero amount (adversarial near-symmetric flats)."""
    rng = random.Random(f"E35:perturb:{j}:{s}")
    width = j + 1
    cells = [(r, cc) for r in range(3) for cc in range(width)]
    out = []
    while len(out) < count:
        _, base = census[rng.randrange(len(census))]
        rows = [list(r) for r in base]
        for r, cc in rng.sample(cells, s):
            rows[r][cc] = (rows[r][cc] + rng.randrange(1, P)) % P
        f = flat_from_vectors(rows, width, 3)
        if f is not None:
            out.append(f)
    return out


GRID = ((3, 3), (4, 3), (4, 4), (5, 3), (5, 4), (5, 5))


def build_families() -> list[tuple[str, int, int, list]]:
    census = {j: symmetric_census(j) for j in DEGREES}
    assert len(census[3]) == 0          # no dim-3 symmetric space at j = 3
    fams: list[tuple[str, int, int, list]] = []
    fams.append(("cal_full", 3, 4,
                 [[tuple(1 if e == i else 0 for e in range(4))
                   for i in range(4)]]))
    fams.append(("cal_full", 4, 5,
                 [[tuple(1 if e == i else 0 for e in range(5))
                   for i in range(5)]]))
    for j, d in GRID:
        fams.append(("a_random", j, d, make_random_flats(j, d, 100)))
        fams.append(("b_djspan", j, d, make_djspan_flats(j, d, 50)))
    for j in (4, 5):
        fams.append(("c_sym_census", j, 3, [b for _, b in census[j]]))
    for j, d in ((4, 4), (5, 4), (5, 5)):
        fams.append(("c_sym_carrier", j, d,
                     make_carrier_flats(j, d, 25, census[j])))
    for j, d, cnt in ((4, 3, 30), (5, 3, 30), (5, 4, 20)):
        fams.append(("d_near_pencil", j, d,
                     make_near_pencil_flats(j, d, cnt)))
    for j in (4, 5):
        for s in (1, 2, 3):
            fams.append((f"d_perturb_s{s}", j, 3,
                         make_perturbed_flats(j, s, 60, census[j])))
    return fams


# ------------------------------------------------------------------- summary
def record_tuple(r: dict) -> tuple:
    return (r["w1"], r["w2"], r["w2m"], r["profile"], r["mult_strict"],
            r["mult_proj"], r["dih"], r["dih_even"], r["dih_odd"], r["anom"])


def summarize_family(records: list[dict]) -> dict:
    stripped = [r for r in records if r["w1"] == 0]
    w2m = sorted(r["w2m"] for r in records)
    fingerprint = hashlib.sha256(
        repr(sorted(record_tuple(r) for r in records)).encode()).hexdigest()
    return {
        "count": len(records),
        "n_stripped": len(stripped),
        "n_sym_ext": sum(r["sym_ext"] for r in records),
        "n_sym_lit": sum(r["sym_lit"] for r in records),
        "n_anom": sum(r["anom"] for r in records),
        "w2m_hist": dict(sorted(Counter(w2m).items())),
        "w2_max": max(r["w2"] for r in records),
        "ns_strip_max_w2": max((r["w2"] for r in stripped
                                if not r["sym_ext"]), default=-1),
        "ns_strip_max_w2m": max((r["w2m"] for r in stripped
                                 if not r["sym_ext"]), default=-1),
        "fingerprint": fingerprint,
    }


def wstar(stripped: list[dict], sym_key: str, cnt_key: str):
    nonsym = [r[cnt_key] for r in stripped if not r[sym_key]]
    sym = [r[cnt_key] for r in stripped if r[sym_key]]
    w = (max(nonsym) + 1) if nonsym else 0
    return {"wstar": w,
            "nonsym_max": max(nonsym) if nonsym else None,
            "sym_min": min(sym) if sym else None,
            "sym_max": max(sym) if sym else None,
            "separates": bool(sym) and min(sym) >= w}


# ----------------------------------------------------------------- self test
def self_test() -> None:
    # MULT anchor {1, X^2, X^4} at j=4: strict pullback, 8 disjoint pairs
    r = analyze_flat([(1, 0, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 0, 1)],
                     4, 3)
    assert r["mult_strict"] and r["w2"] == 8 == r["w2m"] and r["w1"] == 0
    # twisted mult {X, X^3, X^5} at j=5: PROJECTIVE pullback only --
    # 8 weight-2 pairs but NOT in g(X^M) nor in any dihedral stratum
    # (the literal-list gap witness)
    r = analyze_flat([(0, 1, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0),
                      (0, 0, 0, 0, 0, 1)], 5, 3)
    assert (r["mult_proj"] and not r["mult_strict"] and not r["dih"]
            and r["w2"] == 8 and r["w1"] == 0)
    # reciprocal quartics: dihedral (b=1, k=-4=12, c=1), stripped-clean
    r = analyze_flat([(1, 0, 0, 0, 1), (0, 1, 0, 1, 0), (0, 0, 1, 0, 0)],
                     4, 3)
    assert r["dih"] and (1, 12, 1) in r["refl"] and r["w1"] == 0
    # reciprocal quintics: ODD k = -5 = 11, forced weight-1 at x = -1
    # (E30 finding 1: odd-degree self-reciprocal divisible by X + 1)
    r = analyze_flat([(1, 0, 0, 0, 0, 1), (0, 1, 0, 0, 1, 0),
                      (0, 0, 1, 1, 0, 0)], 5, 3)
    assert r["dih"] and r["dih_odd"] and r["w1"] == 1
    # RS[16,4] calibration row: no weight-<=2 words, no symmetry
    r = analyze_flat([tuple(1 if e == i else 0 for e in range(4))
                      for i in range(4)], 3, 4)
    assert r["w1"] == 0 and r["w2"] == 0 and not r["sym_ext"]


# EXPECTED is regenerated with --emit and pasted here; the default run
# recomputes everything from the deterministic seeds and compares.
EXPECTED: dict = {}
EXPECTED_GLOBAL: dict = {}

EXPECTED = {
    'cal_full|j3d4': {'count': 1, 'n_stripped': 1, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 0, 'ns_strip_max_w2m': 0, 'fingerprint': '658a651b5ab875d610a00c1deb4364fcf7ada7009387e5b03c5591ccbd9f16b2'},
    'cal_full|j4d5': {'count': 1, 'n_stripped': 1, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 0, 'ns_strip_max_w2m': 0, 'fingerprint': '658a651b5ab875d610a00c1deb4364fcf7ada7009387e5b03c5591ccbd9f16b2'},
    'a_random|j3d3': {'count': 100, 'n_stripped': 100, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 1, 'ns_strip_max_w2m': 1, 'fingerprint': 'b42583b9bf609dcc0ff39c76bb3f4802080e9c41f232d97c77170f2626bee924'},
    'b_djspan|j3d3': {'count': 50, 'n_stripped': 45, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 1, 'ns_strip_max_w2m': 1, 'fingerprint': '2a7714ae717a4aca61069b1db3872a66036150c8c5c2d25c8789f460cc054130'},
    'a_random|j4d3': {'count': 100, 'n_stripped': 99, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 3, 'ns_strip_max_w2m': 3, 'fingerprint': '92c4647831a0175325c5cad49cf6a6d2c686bd806d1ab33c81e7811614041683'},
    'b_djspan|j4d3': {'count': 50, 'n_stripped': 39, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 3, 'ns_strip_max_w2m': 3, 'fingerprint': 'b74c9196ca1316267b29009dd19a33f3041bdd66d31b446747cb4694850b0644'},
    'a_random|j4d4': {'count': 100, 'n_stripped': 100, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 0, 'ns_strip_max_w2m': 0, 'fingerprint': 'b1c42bbac83a49ebbe313a26ed5470f969dba30ca8a0684decf97a5e6bb6d573'},
    'b_djspan|j4d4': {'count': 50, 'n_stripped': 49, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 1, 'ns_strip_max_w2m': 1, 'fingerprint': 'bbba93dc1e98fa53459140897d02d67424bc005a7daba20ee02b64a62075895c'},
    'a_random|j5d3': {'count': 100, 'n_stripped': 100, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 3, 'ns_strip_max_w2m': 3, 'fingerprint': '5efe6b39afc72436e6e655314d08a6a66c4226e08e26934a3c30fc9dbaeae1ec'},
    'b_djspan|j5d3': {'count': 50, 'n_stripped': 28, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 6, 'ns_strip_max_w2m': 3, 'fingerprint': '185807dbdddabf612e64cc58e70bdfffbdb4c1f2409741b7a538163158da8e51'},
    'a_random|j5d4': {'count': 100, 'n_stripped': 100, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 1, 'ns_strip_max_w2m': 1, 'fingerprint': '416bee23e9d19d027c58f513f826c3656ec875db8c229d2202fdcbb2da134e90'},
    'b_djspan|j5d4': {'count': 50, 'n_stripped': 46, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 1, 'ns_strip_max_w2m': 1, 'fingerprint': '8052bc48f59ff871faaeae85599d51466661bc7da9f0cfe590e7c69eaf0ce6db'},
    'a_random|j5d5': {'count': 100, 'n_stripped': 100, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 0, 'ns_strip_max_w2m': 0, 'fingerprint': 'b1c42bbac83a49ebbe313a26ed5470f969dba30ca8a0684decf97a5e6bb6d573'},
    'b_djspan|j5d5': {'count': 50, 'n_stripped': 49, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 1, 'ns_strip_max_w2m': 1, 'fingerprint': 'bbba93dc1e98fa53459140897d02d67424bc005a7daba20ee02b64a62075895c'},
    'c_sym_census|j4d3': {'count': 17, 'n_stripped': 17, 'n_sym_ext': 17, 'n_sym_lit': 17, 'n_anom': 0, 'ns_strip_max_w2': -1, 'ns_strip_max_w2m': -1, 'fingerprint': 'aedbda8a66f3d36f472610858bb89b4da4eefc2cc7b2bfda2cd1f027edc56ac9'},
    'c_sym_census|j5d3': {'count': 50, 'n_stripped': 34, 'n_sym_ext': 50, 'n_sym_lit': 49, 'n_anom': 0, 'ns_strip_max_w2': -1, 'ns_strip_max_w2m': -1, 'fingerprint': 'd3030ac5c3d26f239576288a9c7578d6f21e39f020e1f0f1b79bb7b40e0d529b'},
    'c_sym_carrier|j4d4': {'count': 25, 'n_stripped': 25, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 1, 'ns_strip_max_w2m': 1, 'fingerprint': '8d5a709e9b7ab9aa08e5de99a0dc6e93c71596b0666d004ea1e8863f19c6e70a'},
    'c_sym_carrier|j5d4': {'count': 25, 'n_stripped': 25, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 2, 'ns_strip_max_w2m': 2, 'fingerprint': 'f122f39e70ac305294d06d345eccc27a523af0dee099dc2dea7eeecbf88cf492'},
    'c_sym_carrier|j5d5': {'count': 25, 'n_stripped': 25, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 1, 'ns_strip_max_w2m': 1, 'fingerprint': '75b8194146734f941ac438c8095e2c52eee3b00511cdf1fcf687a262a964a1d3'},
    'd_near_pencil|j4d3': {'count': 30, 'n_stripped': 30, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 3, 'ns_strip_max_w2m': 1, 'fingerprint': 'e104853c5d0e5ee5cd884e0b5a849a289a9ddebdc811172363a95a16bcc058ba'},
    'd_near_pencil|j5d3': {'count': 30, 'n_stripped': 30, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 6, 'ns_strip_max_w2m': 2, 'fingerprint': '49e2f8d0b736dd5c5a9c982aac64d4c9d32a2cd26e677aea20df9f1f05d98b56'},
    'd_near_pencil|j5d4': {'count': 20, 'n_stripped': 20, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 3, 'ns_strip_max_w2m': 1, 'fingerprint': '9b259bf872f03519943e7f8f3586e2f1641f2390e02a1c7785def8d856f3ab0b'},
    'd_perturb_s1|j4d3': {'count': 60, 'n_stripped': 60, 'n_sym_ext': 11, 'n_sym_lit': 11, 'n_anom': 0, 'ns_strip_max_w2': 2, 'ns_strip_max_w2m': 2, 'fingerprint': 'fca12bdf085a6aec3727a62a30aff267cb550e831d1cf5c6c973ff822698dfde'},
    'd_perturb_s2|j4d3': {'count': 60, 'n_stripped': 60, 'n_sym_ext': 5, 'n_sym_lit': 5, 'n_anom': 0, 'ns_strip_max_w2': 2, 'ns_strip_max_w2m': 2, 'fingerprint': 'd7b14235d2ba086eaf330f34671ea493f437ec4f12fb357d32789a24f516b6b2'},
    'd_perturb_s3|j4d3': {'count': 60, 'n_stripped': 60, 'n_sym_ext': 1, 'n_sym_lit': 1, 'n_anom': 0, 'ns_strip_max_w2': 3, 'ns_strip_max_w2m': 2, 'fingerprint': '248ecc2f0869a8d5f317d8cf43e98d07e0f360392089342f3bf846808b9d2c55'},
    'd_perturb_s1|j5d3': {'count': 60, 'n_stripped': 60, 'n_sym_ext': 6, 'n_sym_lit': 5, 'n_anom': 0, 'ns_strip_max_w2': 2, 'ns_strip_max_w2m': 2, 'fingerprint': '892416a26d41f5e6e20b5f10118a2f462ba41e1a4984683b0bc7aa4c61e1371c'},
    'd_perturb_s2|j5d3': {'count': 60, 'n_stripped': 60, 'n_sym_ext': 0, 'n_sym_lit': 0, 'n_anom': 0, 'ns_strip_max_w2': 3, 'ns_strip_max_w2m': 3, 'fingerprint': 'a22a5ffb49200a572e332c44d88ff2ec36800b886afcd7fa0382d1e6f57d24ba'},
    'd_perturb_s3|j5d3': {'count': 60, 'n_stripped': 60, 'n_sym_ext': 1, 'n_sym_lit': 1, 'n_anom': 0, 'ns_strip_max_w2': 3, 'ns_strip_max_w2m': 3, 'fingerprint': '38324ae0fe0ce1e95d7dd423e292d73b150f3e8cc4e906343e6f829b61167f84'},
}

EXPECTED_GLOBAL = {'n_stripped': 1423, 'wstar_ext_matching': {'wstar': 4, 'nonsym_max': 3, 'sym_min': 7, 'sym_max': 8, 'separates': True}, 'wstar_ext_raw': {'wstar': 7, 'nonsym_max': 6, 'sym_min': 7, 'sym_max': 8, 'separates': True}, 'wstar_lit_matching': {'wstar': 9, 'nonsym_max': 8, 'sym_min': 7, 'sym_max': 8, 'separates': False}, 'wstar_lit_raw': {'wstar': 9, 'nonsym_max': 8, 'sym_min': 7, 'sym_max': 8, 'separates': False}, 'n_anom_total': 0, 'joint_fingerprint': '151126a82fe64b4861e163b9f65b5b73ce0aa188eecd551d7176d60d27d6e4b5', 'n_falsifier_ext': 43}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true",
                    help="print the EXPECTED tables instead of verifying")
    args = ap.parse_args()

    self_test()
    fams = build_families()
    all_pass = True
    emitted = {}
    pool: list[tuple[str, dict]] = []
    for name, j, d, flats in fams:
        records = [analyze_flat(list(b), j, d) for b in flats]
        summ = summarize_family(records)
        key = f"{name}|j{j}d{d}"
        pool.extend((key, r) for r in records)
        emitted[key] = {k: summ[k] for k in
                        ("count", "n_stripped", "n_sym_ext", "n_sym_lit",
                         "n_anom", "ns_strip_max_w2", "ns_strip_max_w2m",
                         "fingerprint")}
        print(f"== {key}  (n={summ['count']}, stripped={summ['n_stripped']})")
        print(f"   sym      ext={summ['n_sym_ext']} lit={summ['n_sym_lit']}"
              f" anom={summ['n_anom']}")
        print(f"   w2m hist {summ['w2m_hist']}  w2_max={summ['w2_max']}")
        print(f"   nonsym-stripped max: w2={summ['ns_strip_max_w2']}"
              f" w2m={summ['ns_strip_max_w2m']}")
        if not args.emit:
            exp = EXPECTED.get(key)
            ok = exp == emitted[key]
            all_pass &= ok
            print(f"   verify   {'PASS' if ok else 'FAIL'}")
        print()

    # ---- global: joint distribution + W* (post common-root strip)
    stripped = [(k, r) for k, r in pool if r["w1"] == 0]
    joint = Counter()
    for _, r in stripped:
        status = ("sym_lit" if r["sym_lit"]
                  else "sym_ext_only" if r["sym_ext"] else "nonsym")
        joint[(r["w2m"], status)] += 1
    # independent recount from the stored per-flat records
    recount = Counter()
    for _, r in pool:
        if r["w1"] != 0:
            continue
        recount[(r["w2m"], "sym_lit" if r["sym_lit"] else
                 "sym_ext_only" if r["sym_ext"] else "nonsym")] += 1
    assert recount == joint, "joint-table recount FAIL"

    print("== joint distribution (stripped flats): w2m x symmetry status")
    for m in sorted({m for m, _ in joint}):
        row = {s: joint.get((m, s), 0)
               for s in ("nonsym", "sym_ext_only", "sym_lit")}
        print(f"   w2m={m:2d}  {row}")

    srecs = [r for _, r in stripped]
    glob = {
        "n_stripped": len(srecs),
        "wstar_ext_matching": wstar(srecs, "sym_ext", "w2m"),
        "wstar_ext_raw": wstar(srecs, "sym_ext", "w2"),
        "wstar_lit_matching": wstar(srecs, "sym_lit", "w2m"),
        "wstar_lit_raw": wstar(srecs, "sym_lit", "w2"),
        "n_anom_total": sum(r["anom"] for _, r in pool),
        "joint_fingerprint": hashlib.sha256(
            repr(sorted(joint.items())).encode()).hexdigest(),
    }
    print("\n== W* (abundance thresholds, post common-root strip)")
    for k in ("wstar_ext_matching", "wstar_ext_raw",
              "wstar_lit_matching", "wstar_lit_raw"):
        print(f"   {k}: {glob[k]}")
    print(f"   anomaly flags total: {glob['n_anom_total']}")

    # ---- falsifier hunt: stripped, abundant, outside every stratum
    print("\n== falsifier hunt (stripped, nonsym under EXT list, w2m >= 3"
          " or w2 >= 5)")
    hits = [(k, r) for k, r in stripped
            if not r["sym_ext"] and (r["w2m"] >= 3 or r["w2"] >= 5)]
    for k, r in hits:
        print(f"   {k}: w2={r['w2']} w2m={r['w2m']} profile={r['profile']}")
    if not hits:
        print("   none")
    glob["n_falsifier_ext"] = len(hits)

    if args.emit:
        print("\nEXPECTED = {")
        for k, v in emitted.items():
            print(f"    {k!r}: {v!r},")
        print("}")
        print(f"\nEXPECTED_GLOBAL = {glob!r}")
        return 0
    ok = glob == EXPECTED_GLOBAL
    all_pass &= ok
    print(f"\nglobal verify: {'PASS' if ok else 'FAIL'}")
    print("E35 verifier:", "PASS (all families)" if all_pass else "FAIL")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
