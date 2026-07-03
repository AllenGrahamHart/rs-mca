#!/usr/bin/env python3
"""Verifier + census for experimental/notes/roadmaps/e27_exceptional_pair_census.md
(wave-4 probe E27, RK axis Q: the exceptional-pair census at the toy corridor).

Row: RS[F_97, mu_16, k=8] (n = 16, rate 1/2), corridor agreement A* = the
first A with FM(A) = C(n, n-A) * q^(1-(A-k)) < 1 (computed, not assumed;
it is A* = 11), contrast point A*-1 = 10.

Deep bad slope of a pair (u, v) at agreement A: a slope z in F_q such that
u + z*v agrees with SOME codeword on >= A points.  Detection is by
syndrome/rank checks, never codeword enumeration:
  * per support S, |S| = A: RS_k|_S has dual dimension A-k with explicit
    GRS dual rows r_m(i) = lam_i x_i^m (lam_i = prod_{j!=i}(x_i-x_j)^{-1});
  * the slope PENCIL: syndrome of u + z*v is <r,u> + z <r,v>, so each dual
    row kills z on {}, {one z}, or all of F_q; a support is aligned at z
    iff all its rows kill z.  One pair costs 2 syndrome vectors, not 97.

Sections (exit 0 iff all PASS):
  S1  corridor arithmetic (exact fractions)
  S2  domain + orbit audit (mu_16, aperiodicity of all size-A supports,
      dihedral-support baseline)
  S3  method cross-checks (pencil == per-word dual syndrome == brute-force
      all-C(16,8) interpolation, seeded samples)
  S4  constructed census, 2000 pairs: multiplicity histogram
  S5  classification of every multiplicity->=2 constructed pair
  S6  organic control, 100000 pairs: FM band + histogram + classification
  S6b the forcing stratum: no multiplicity-2 pair carries a core >= A-1;
      core >= A-1 pairs cascade to multiplicity ~ n-core (tangent pencil)
  S6c cascade replication on two further seeds (the primary seed drew the
      low tail of the cascade count, P ~ 1.2e-3; disclosed, not reshuffled)
  S7  contrast point A = 10: abundance below the corridor

Determinism: numpy default_rng with fixed seeds; frozen expected values were
produced with numpy 2.3.4 / python 3.12.3 (any drift FAILs loudly).
Runtime: ~5 min, single process, < 1 GB RSS.
Run with --freeze to print the observed-values dict instead of comparing.
"""
import itertools
import math
import sys
from collections import defaultdict
from fractions import Fraction

import numpy as np

Q, N, K = 97, 16, 8
SEED_TRIPLES = 20260703
SEED_ORGANIC = 20260704
SEED_XCHECK = 20260705
SEED_CONTRAST = 20260706
SEEDS_REPL = (987654, 13579)
N_CONSTRUCTED = 2000
N_ORGANIC = 100000
N_CONTRAST = 300
ALL, EMPTY = 97, 98
TANGENT_MIN_OVERLAP = K + 1  # forced agreement of u,v with codewords on > k pts

RESULTS = []
FREEZE = "--freeze" in sys.argv
OBS = {}


def report(name, ok, detail):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ------------------------------------------------------------------ field row
def find_omega():
    for g in range(2, Q):
        if all(pow(g, (Q - 1) // p, Q) != 1 for p in (2, 3)):
            return pow(g, (Q - 1) // N, Q)
    raise RuntimeError("no generator")


OMEGA = find_omega()
XS = np.array([pow(OMEGA, i, Q) for i in range(N)], dtype=np.int64)
GMAT = np.array([[pow(int(x), m, Q) for x in XS] for m in range(K)],
                dtype=np.int64)
INV = [0] + [pow(a, Q - 2, Q) for a in range(1, Q)]
INV_ARR = np.array(INV, dtype=np.int32)


def fm(A):
    return Fraction(math.comb(N, N - A)) * Fraction(Q) ** (1 - (A - K))


def dual_rows(support):
    s = len(support)
    xs = [int(XS[i]) for i in support]
    rows = np.zeros((s - K, N), dtype=np.int64)
    for a, i in enumerate(support):
        lam = 1
        for b in range(s):
            if b != a:
                lam = lam * ((xs[a] - xs[b]) % Q) % Q
        lam = INV[lam]
        for m in range(s - K):
            rows[m, i] = lam * pow(xs[a], m, Q) % Q
    return rows


def build_H(A):
    sups = list(itertools.combinations(range(N), A))
    H = np.concatenate([dual_rows(s) for s in sups], axis=0)
    return H.astype(np.float64), sups


def interpolate(word, pts):
    """Codeword through word[pts] (len K), evaluated everywhere (mod Q)."""
    M = np.zeros((K, K + 1), dtype=np.int64)
    for r, i in enumerate(pts):
        for m in range(K):
            M[r, m] = pow(int(XS[i]), m, Q)
        M[r, K] = int(word[i]) % Q
    for c in range(K):
        piv = next(r for r in range(c, K) if M[r, c] % Q)
        M[[c, piv]] = M[[piv, c]]
        M[c] = M[c] * INV[int(M[c, c] % Q)] % Q
        for r in range(K):
            if r != c and M[r, c] % Q:
                M[r] = (M[r] - M[r, c] * M[c]) % Q
    return (M[:, K] % Q) @ GMAT % Q


# ------------------------------------------------------------ pencil engine
def row_codes(A, B):
    return np.where(B != 0, (Q - A) % Q * INV_ARR[B] % Q,
                    np.where(A == 0, ALL, EMPTY)).astype(np.int16)


def code_intersect(a, b):
    return np.where((a == EMPTY) | (b == EMPTY), EMPTY,
                    np.where(a == ALL, b,
                             np.where(b == ALL, a,
                                      np.where(a == b, a, EMPTY)))
                    ).astype(np.int16)


def support_codes(U, V, HT, nsup, ncheck):
    """codes[p, s] in {0..96: the one bad slope of support s for pair p,
    97: all slopes, 98: none}."""
    SU = ((U.astype(np.float64) @ HT) % Q).astype(np.int32)
    SV = ((V.astype(np.float64) @ HT) % Q).astype(np.int32)
    codes = row_codes(SU, SV).reshape(-1, nsup, ncheck)
    out = codes[:, :, 0]
    for m in range(1, ncheck):
        out = code_intersect(out, codes[:, :, m])
    return out


def word_alignments(word, H, sups, A, ncheck):
    """Per-word reference: all (codeword, agreement set), agreement >= A."""
    syn = (H @ word.astype(np.float64)) % Q
    hit = np.nonzero((syn.reshape(len(sups), ncheck) == 0).all(axis=1))[0]
    out = {}
    for h in hit:
        cw = interpolate(word, sups[h][:K])
        agr = frozenset(np.nonzero((cw - word) % Q == 0)[0].tolist())
        assert len(agr) >= A
        out[tuple(cw.tolist())] = agr
    return out


def brute_alignments(word, A):
    """Slow reference: interpolate through ALL C(16,8) point sets."""
    out = {}
    for pts in itertools.combinations(range(N), K):
        cw = interpolate(word, pts)
        agr = frozenset(np.nonzero((cw - word) % Q == 0)[0].tolist())
        if len(agr) >= A:
            out[tuple(cw.tolist())] = agr
    return out


# --------------------------------------------------------- support structure
def rot_periodic(J):
    Js = set(J)
    return any(all((i + s) % N in Js for i in Js) for s in (8, 4, 2, 1))


def dihedral_sym(J):
    Js = set(J)
    return any(all((e - i) % N in Js for i in Js) for e in range(N))


def orbit_rep(sup):
    return min(tuple(sorted((i + r) % N for i in sup)) for r in range(N))


def slope_class(J0, aligns):
    """Priority label for one extra slope given its codeword alignments."""
    tang = any(len(J0 & J) >= TANGENT_MIN_OVERLAP for J in aligns.values())
    mult = any(rot_periodic(J) for J in aligns.values())
    dih = any(dihedral_sym(J) for J in aligns.values())
    if tang:
        return "TANGENT"
    if mult:
        return "MULT"
    if dih:
        return "DIHEDRAL"
    return "UNSTRUCTURED"
    # extension-type: vacuous at this row (F_97 prime; no proper tower
    # acts on mu_16), see note sect. 5 — deliberately not a branch here.


def slopes_from_codes(codes_row):
    if (codes_row == ALL).any():
        return list(range(Q))
    return sorted(set(codes_row[codes_row <= 96].tolist()))


def max_overlap(al0, al1):
    """Max |J0 ^ J1| over codeword alignments of two slopes."""
    return max(len(J0 & J1) for J0 in al0.values() for J1 in al1.values())


def joint_close(u, v, z0, c0, z1, c1, core):
    """Two-slope forced words: on the core, u = a, v = b for the codeword
    pencil b = (c0-c1)/(z0-z1), a = c0 - z0 b.  Returns (ok_on_core,
    off_size) where off_size = #points where (u,v) != (a,b)."""
    ib = INV[(z0 - z1) % Q]
    b = (np.array(c0, dtype=np.int64) - np.array(c1, dtype=np.int64)) \
        * ib % Q
    a = (np.array(c0, dtype=np.int64) - z0 * b) % Q
    mism = np.nonzero(((u - a) % Q != 0) | ((v - b) % Q != 0))[0]
    ok_core = not (set(mism.tolist()) & set(core))
    return ok_core, len(mism)


def alignments_at(w, codes_row, z, sups, A):
    """Codeword-level alignments of w at slope z from the support codes."""
    out = {}
    for s in np.nonzero((codes_row == z) | (codes_row == ALL))[0]:
        cw = interpolate(w, sups[s][:K])
        agr = frozenset(np.nonzero((cw - w) % Q == 0)[0].tolist())
        assert len(agr) >= A
        out[tuple(cw.tolist())] = agr
    return out


# ------------------------------------------------------------------ sections
def s1():
    fms = {A: fm(A) for A in range(K + 1, 14)}
    astar = min(A for A, f in fms.items() if f < 1)
    ok = (astar == 11 and fms[11] == Fraction(4368, 9409)
          and fms[10] == Fraction(8008, 97) and fms[10] > 1 > fms[11])
    report("S1 corridor", ok,
           f"A*={astar}, FM(11)={fms[11]}~{float(fms[11]):.4f}, "
           f"FM(10)={fms[10]}~{float(fms[10]):.2f}")
    return astar


def s2(sups):
    ok_dom = (pow(OMEGA, N, Q) == 1
              and all(pow(OMEGA, d, Q) != 1 for d in (1, 2, 4, 8))
              and len(set(XS.tolist())) == N)
    orbits = defaultdict(list)
    for s in sups:
        orbits[orbit_rep(s)].append(s)
    free = all(len(v) == 16 for v in orbits.values())
    aper = sum(1 for s in sups if not rot_periodic(s))
    dih = sum(1 for s in sups if dihedral_sym(s))
    ok = (ok_dom and len(sups) == 4368 and len(orbits) == 273 and free
          and aper == 4368 and dih == 336)
    report("S2 domain/orbits", ok,
           f"omega={OMEGA} (order 16), {len(sups)} size-11 supports, "
           f"{len(orbits)} rotation orbits (all free => every deep slope at "
           f"A* is automatically APERIODIC), dihedral-symmetric supports "
           f"{dih}/4368 = {dih/4368:.4f} (chance baseline)")
    return sorted(orbits.keys())


def s3(H, sups, A):
    rng = np.random.default_rng(SEED_XCHECK)
    npairs = 40
    U = rng.integers(0, Q, (npairs, N))
    V = rng.integers(0, Q, (npairs, N))
    for p in range(0, npairs, 2):  # plant constructions in half
        T = sorted(rng.choice(N, A, replace=False).tolist())
        z0 = int(rng.integers(0, Q))
        cw = (rng.integers(0, Q, K) @ GMAT) % Q
        U[p, T] = (cw[T] - z0 * V[p, T]) % Q
    codes = support_codes(U, V, H.T.copy(), len(sups), A - K)
    ok_a, planted_found = True, 0
    for p in range(npairs):
        ref = [z for z in range(Q)
               if word_alignments((U[p] + z * V[p]) % Q, H, sups, A, A - K)]
        got = slopes_from_codes(codes[p])
        ok_a &= (got == ref)
        planted_found += (p % 2 == 0 and len(got) >= 1)
    report("S3a pencil==per-word", ok_a and planted_found == npairs // 2,
           f"{npairs} pairs x 97 slopes, all planted found "
           f"({planted_found}/{npairs//2})")
    # brute-force cross-check on 8 words (2 planted at distance n-A)
    ok_b = True
    for t in range(8):
        if t < 2:
            w = (rng.integers(0, Q, K) @ GMAT) % Q
            e = rng.choice(N, N - A, replace=False)
            w[e] = (w[e] + rng.integers(1, Q, N - A)) % Q
        else:
            w = rng.integers(0, Q, N)
        ok_b &= (word_alignments(w, H, sups, A, A - K)
                 == brute_alignments(w, A))
    report("S3b per-word==brute C(16,8)", ok_b, "8 seeded words (2 planted)")


def constructed_census(H, sups, A, reps):
    """2000 constructed pairs (T, z0, c, v): u := c - z0 v on T, random off."""
    rng = np.random.default_rng(SEED_TRIPLES)
    sup_arr = [tuple(r) for r in reps]  # all 273 aperiodic orbit reps first
    idx = rng.integers(0, len(sups), N_CONSTRUCTED - len(reps))
    sup_arr += [sups[i] for i in idx]
    U = np.zeros((N_CONSTRUCTED, N), dtype=np.int64)
    V = rng.integers(0, Q, (N_CONSTRUCTED, N))
    Z0, CW = [], []
    for p, T in enumerate(sup_arr):
        z0 = int(rng.integers(0, Q))
        cw = (rng.integers(0, Q, K) @ GMAT) % Q
        u = rng.integers(0, Q, N)
        u[list(T)] = (cw[list(T)] - z0 * V[p, list(T)]) % Q
        U[p], Z0, CW = u, Z0 + [z0], CW + [cw]
    codes = support_codes(U, V, H.T.copy(), len(sups), A - K)
    return U, V, Z0, CW, sup_arr, codes


def s4_s5(H, sups, A, reps):
    U, V, Z0, CW, Ts, codes = constructed_census(H, sups, A, reps)
    sup_index = {s: i for i, s in enumerate(sups)}
    hist = defaultdict(int)
    z0_ok, extra_slope_events, extra_support_events = True, 0, 0
    multi = []  # (p, bad_slopes)
    for p in range(N_CONSTRUCTED):
        bad = slopes_from_codes(codes[p])
        z0_ok &= (Z0[p] in bad)
        ci = codes[p][sup_index[Ts[p]]]
        z0_ok &= ci == Z0[p] or ci == ALL
        m = len(bad)
        hist[min(m, 3)] += 1
        extra_slope_events += m - 1
        extra_support_events += int(
            ((codes[p] <= 96) & (codes[p] != Z0[p])).sum())
        if m >= 2:
            multi.append((p, bad))
    OBS["s4_hist"] = dict(hist)
    OBS["s4_extra_slopes"] = extra_slope_events
    OBS["s4_extra_sup_events"] = extra_support_events
    exp_sup = Fraction(N_CONSTRUCTED * (Q - 1) * 4368, Q ** 3)
    band = 5 * math.sqrt(float(exp_sup))
    in_band = abs(extra_support_events - float(exp_sup)) <= band
    ok = z0_ok and in_band and (not EXPECTED or (
        EXPECTED["s4_hist"] == dict(hist)
        and EXPECTED["s4_extra_slopes"] == extra_slope_events
        and EXPECTED["s4_extra_sup_events"] == extra_support_events))
    report("S4 constructed census", ok,
           f"{N_CONSTRUCTED} pairs (all 273 aperiodic orbit reps + seeded), "
           f"multiplicity hist 1:{hist[1]} 2:{hist[2]} 3+:{hist[3]}; "
           f"z0 always bad: {z0_ok}; extra (z,S) events "
           f"{extra_support_events} vs FM expectation {float(exp_sup):.1f} "
           f"(+-{band:.0f} pre-registered)")

    # ---- S5: classify every extra slope of every multiplicity->=2 pair
    cls = defaultdict(int)
    ohist = defaultdict(int)  # anchor-overlap per extra slope
    pair_all_structured = 0
    deep_uv = 0
    casc, casc_ok = 0, 0
    casc_pairs = set()
    j0_sizes = defaultdict(int)
    for p, bad in multi:
        wz0 = (U[p] + Z0[p] * V[p]) % Q
        J0 = frozenset(np.nonzero((wz0 - CW[p]) % Q == 0)[0].tolist())
        j0_sizes[len(J0)] += 1
        labels = []
        for z in bad:
            if z == Z0[p]:
                continue
            w = (U[p] + z * V[p]) % Q
            al = alignments_at(w, codes[p], z, sups, A)
            labels.append(slope_class(J0, al))
            o = max(len(J0 & J) for J in al.values())
            ohist[o] += 1
            if o >= A - 1:  # forcing threshold: common core of size >= A-1
                casc += 1
                casc_pairs.add(p)
                cbest = max(al, key=lambda c: len(J0 & al[c]))
                core = J0 & al[cbest]
                okc, off = joint_close(U[p], V[p], Z0[p],
                                       tuple(CW[p].tolist()), z, cbest, core)
                casc_ok += (okc and off <= N - len(core) and len(bad) >= 3)
        for L in labels:
            cls[L] += 1
        pair_all_structured += all(L != "UNSTRUCTURED" for L in labels)
        du = bool(word_alignments(U[p] % Q, H, sups, A, A - K))
        dv = bool(word_alignments(V[p] % Q, H, sups, A, A - K))
        deep_uv += (du or dv)
    OBS["s5_class"] = dict(cls)
    OBS["s5_ohist"] = dict(ohist)
    OBS["s5_cascades"] = (casc, casc_ok, len(casc_pairs))
    OBS["s5_all_structured_pairs"] = pair_all_structured
    OBS["s5_deep_uv"] = deep_uv
    tot = sum(cls.values())
    base_t = Fraction(606, 4368)  # P(|J0 ^ J'| >= 9), both size 11, null
    base_d = Fraction(336, 4368)
    ok5 = casc == casc_ok and (not EXPECTED or (
        EXPECTED["s5_class"] == dict(cls)
        and EXPECTED["s5_ohist"] == dict(ohist)
        and EXPECTED["s5_cascades"] == (casc, casc_ok, len(casc_pairs))
        and EXPECTED["s5_all_structured_pairs"] == pair_all_structured
        and EXPECTED["s5_deep_uv"] == deep_uv))
    report("S5 classification (constructed)", ok5,
           f"{len(multi)} mult>=2 pairs, {tot} extra slopes: "
           f"TANGENT {cls['TANGENT']} ({cls['TANGENT']/max(tot,1):.3f} vs "
           f"chance {float(base_t):.3f}), MULT {cls['MULT']}, DIHEDRAL "
           f"{cls['DIHEDRAL']} ({cls['DIHEDRAL']/max(tot,1):.3f} vs chance "
           f"{float(base_d):.3f}), UNSTRUCTURED {cls['UNSTRUCTURED']}; "
           f"anchor-overlap hist {dict(sorted(ohist.items()))}; cascade "
           f"slopes (o>={A-1}) {casc} on {len(casc_pairs)} pairs, verified "
           f"{casc_ok}; fully-structured pairs "
           f"{pair_all_structured}/{len(multi)}; u/v-deep pairs {deep_uv}; "
           f"|J0| sizes {dict(sorted(j0_sizes.items()))}")


def s6(H, sups, A):
    rng = np.random.default_rng(SEED_ORGANIC)
    HT = H.T.copy()
    hist = defaultdict(int)
    sup_events = 0
    all_codes = 0
    multi = []  # (U,V, bad, codes_row) for mult>=2
    chunk = 2000
    for c0 in range(0, N_ORGANIC, chunk):
        U = rng.integers(0, Q, (chunk, N))
        V = rng.integers(0, Q, (chunk, N))
        codes = support_codes(U, V, HT, len(sups), A - K)
        all_codes += int((codes == ALL).sum())
        sup_events += int((codes <= 96).sum())
        npair_bad = codes <= 96
        for p in np.nonzero(npair_bad.any(axis=1))[0]:
            bad = slopes_from_codes(codes[p])
            hist[min(len(bad), 3)] += 1
        hist[0] = c0 + chunk - sum(hist[m] for m in (1, 2, 3))
        for p in np.nonzero((npair_bad.sum(axis=1) >= 2))[0]:
            bad = slopes_from_codes(codes[p])
            if len(bad) >= 2:
                multi.append((U[p].copy(), V[p].copy(), bad,
                              codes[p].copy()))
    OBS["s6_hist"] = dict(hist)
    OBS["s6_sup_events"] = sup_events
    exp_sup = Fraction(N_ORGANIC * 4368, Q ** 2)  # = N * FM(11), exact
    band = 5 * math.sqrt(float(exp_sup))
    in_band = abs(sup_events - float(exp_sup)) <= band

    cls = defaultdict(int)
    all_structured = 0
    ohist2 = defaultdict(int)  # max J-overlap of exactly-2-slope pairs
    casc_mults, casc_ok = [], 0
    for u, v, bad, crow in multi:
        aligns = {z: alignments_at((u + z * v) % Q, crow, z, sups, A)
                  for z in bad}
        J0 = aligns[bad[0]][min(aligns[bad[0]])]  # lex-min cw: deterministic
        labels = [slope_class(J0, aligns[z]) for z in bad[1:]]
        for L in labels:
            cls[L] += 1
        all_structured += all(L != "UNSTRUCTURED" for L in labels)
        # ---- forcing stratum: max pairwise agreement-set overlap
        best, bpair = -1, None
        for i in range(len(bad)):
            for j in range(i + 1, len(bad)):
                for c0, Ja in aligns[bad[i]].items():
                    for c1, Jb in aligns[bad[j]].items():
                        if len(Ja & Jb) > best:
                            best = len(Ja & Jb)
                            bpair = (bad[i], c0, Ja, bad[j], c1, Jb)
        if len(bad) == 2:
            ohist2[best] += 1
        if best >= A - 1:  # common core of size >= A-1: the cascade
            casc_mults.append(len(bad))
            z0, c0, Ja, z1, c1, Jb = bpair
            core = Ja & Jb
            okc, off = joint_close(u, v, z0, c0, z1, c1, core)
            casc_ok += (okc and off <= N - len(core))
    casc_mults.sort()
    OBS["s6_class"] = dict(cls)
    OBS["s6_all_structured_pairs"] = all_structured
    OBS["s6_ohist2"] = dict(ohist2)
    OBS["s6_cascades"] = (casc_mults, casc_ok)
    tot = sum(cls.values())
    frozen_ok = (not EXPECTED or (
        EXPECTED["s6_hist"] == dict(hist)
        and EXPECTED["s6_sup_events"] == sup_events
        and EXPECTED["s6_class"] == dict(cls)
        and EXPECTED["s6_all_structured_pairs"] == all_structured
        and EXPECTED["s6_ohist2"] == dict(ohist2)
        and EXPECTED["s6_cascades"] == (casc_mults, casc_ok)))
    # pre-registered: FM band; no structured EXCESS (rates near chance);
    # unstructured extras are the FM/clause-(ii) remainder, not a new class
    rate_t = cls["TANGENT"] / max(tot, 1)
    rate_d = cls["DIHEDRAL"] / max(tot, 1)
    # cascade stratum: exact first moment 8008 * q^-4 * N pairs; all
    # cascades must verify joint codeword-closeness; no 2-slope pair may
    # carry a core >= A-1 (forcing would have raised its multiplicity)
    exp_casc = float(Fraction(N_ORGANIC * 8008, Q ** 4))
    casc_band_ok = (1 <= len(casc_mults) <= exp_casc + 5 * exp_casc ** 0.5
                    and casc_ok == len(casc_mults)
                    and all(o < A - 1 for o in ohist2)
                    and min(casc_mults) >= 3)
    bands_ok = (in_band and all_codes == 0
                and 0.05 <= rate_t <= 0.30 and 0.01 <= rate_d <= 0.16)
    report("S6 organic control", frozen_ok and bands_ok and casc_band_ok,
           f"{N_ORGANIC} pairs: hist 0:{hist[0]} 1:{hist[1]} 2:{hist[2]} "
           f"3+:{hist[3]}; (z,S) events {sup_events} vs exact FM expectation "
           f"{float(exp_sup):.1f} (+-{band:.0f}): {'in' if in_band else 'OUT'}"
           f" of band; extra-slope classes of {len(multi)} mult>=2 pairs: "
           f"T {cls['TANGENT']} ({rate_t:.3f}) M {cls['MULT']} D "
           f"{cls['DIHEDRAL']} ({rate_d:.3f}) U {cls['UNSTRUCTURED']}; "
           f"ALL-codes {all_codes}")
    report("S6b forcing stratum (organic)", frozen_ok and casc_band_ok,
           f"2-slope pairs max-core hist {dict(sorted(ohist2.items()))} — "
           f"NO core >= {A-1} at multiplicity 2; cascade pairs (core >= "
           f"{A-1}): {len(casc_mults)} vs first-moment {exp_casc:.1f}, "
           f"multiplicities {casc_mults}, all {casc_ok} verified "
           f"joint-codeword-close (u,v)=(a,b) off <= n-core pts")


def s6c(H, sups, A):
    """Cascade replication: the primary organic seed drew the LOW TAIL of
    the cascade count (1 observed vs first-moment 9.0; Poisson P(N<=1)
    ~ 1.2e-3).  Two further seeds, fixed before freezing, recount the
    cascade stratum only (support-level core detection + pencil check)."""
    HT = H.T.copy()
    sup_sets = [frozenset(s) for s in sups]
    out = {}
    pooled = 0
    all_ok = True
    for seed in SEEDS_REPL:
        rng = np.random.default_rng(seed)
        mults, nver = [], 0
        for c0 in range(0, N_ORGANIC, 2000):
            U = rng.integers(0, Q, (2000, N))
            V = rng.integers(0, Q, (2000, N))
            codes = support_codes(U, V, HT, len(sups), A - K)
            ev = codes <= 96
            for p in np.nonzero(ev.sum(axis=1) >= 2)[0]:
                ss = np.nonzero(ev[p])[0]
                best, bp = 0, None
                for i in range(len(ss)):
                    for j in range(i + 1, len(ss)):
                        zi, zj = int(codes[p][ss[i]]), int(codes[p][ss[j]])
                        if zi != zj:
                            o = len(sup_sets[ss[i]] & sup_sets[ss[j]])
                            if o > best:
                                best, bp = o, (ss[i], zi, ss[j], zj)
                if best >= A - 1:
                    si, zi, sj, zj = bp
                    mults.append(len(set(codes[p][ss].tolist())))
                    wi = (U[p] + zi * V[p]) % Q
                    wj = (U[p] + zj * V[p]) % Q
                    ci = tuple(interpolate(wi, sups[si][:K]).tolist())
                    cj = tuple(interpolate(wj, sups[sj][:K]).tolist())
                    okc, off = joint_close(U[p], V[p], zi, ci, zj, cj,
                                           sup_sets[si] & sup_sets[sj])
                    nver += (okc and off <= N - best and mults[-1] >= 3)
        mults.sort()
        out[seed] = (mults, nver)
        pooled += len(mults)
        all_ok &= (nver == len(mults))
    OBS["s6c_repl"] = out
    exp_pool = float(Fraction(3 * N_ORGANIC * 8008, Q ** 4))  # incl. primary
    pooled_total = pooled + len(OBS["s6_cascades"][0])
    band_ok = abs(pooled_total - exp_pool) <= 5 * math.sqrt(exp_pool)
    frozen_ok = not EXPECTED or EXPECTED["s6c_repl"] == out
    report("S6c cascade replication", frozen_ok and all_ok and band_ok,
           f"seeds {SEEDS_REPL}: counts "
           f"{[len(out[s][0]) for s in SEEDS_REPL]} with multiplicities "
           f"{[out[s][0] for s in SEEDS_REPL]}, all pencil-verified; pooled "
           f"with primary {pooled_total} vs first-moment {exp_pool:.1f} "
           f"(+-{5*math.sqrt(exp_pool):.0f}); primary seed's count 1 is a "
           f"disclosed low-tail draw (P~1.2e-3), not reshuffled")


def s7():
    A = 10
    H10, sups10 = build_H(A)
    HT = H10.T.copy()
    rng = np.random.default_rng(SEED_CONTRAST)
    # constructed
    U = np.zeros((N_CONTRAST, N), dtype=np.int64)
    V = rng.integers(0, Q, (N_CONTRAST, N))
    for p in range(N_CONTRAST):
        T = sorted(rng.choice(N, A, replace=False).tolist())
        z0 = int(rng.integers(0, Q))
        cw = (rng.integers(0, Q, K) @ GMAT) % Q
        u = rng.integers(0, Q, N)
        u[T] = (cw[T] - z0 * V[p, T]) % Q
        U[p] = u
    mc = [len(slopes_from_codes(r))
          for r in support_codes(U, V, HT, len(sups10), A - K)]
    # organic
    Uo = rng.integers(0, Q, (N_CONTRAST, N))
    Vo = rng.integers(0, Q, (N_CONTRAST, N))
    mo = [len(slopes_from_codes(r))
          for r in support_codes(Uo, Vo, HT, len(sups10), A - K)]
    OBS["s7_sum_constructed"] = int(sum(mc))
    OBS["s7_sum_organic"] = int(sum(mo))
    frozen_ok = (not EXPECTED or (
        EXPECTED["s7_sum_constructed"] == sum(mc)
        and EXPECTED["s7_sum_organic"] == sum(mo)))
    ok = (frozen_ok and sum(mc) / N_CONTRAST >= 20
          and sum(mo) / N_CONTRAST >= 20)
    report("S7 contrast A=10", ok,
           f"FM(10)={float(fm(10)):.2f}>1: mean multiplicity constructed "
           f"{sum(mc)/N_CONTRAST:.1f}, organic {sum(mo)/N_CONTRAST:.1f} "
           f"(pre-registered >= 20 both) — the corridor cliff vs A*=11")


# Frozen observed values (numpy 2.3.4, python 3.12.3; --freeze recomputes).
EXPECTED = {
    's4_hist': {1: 1309, 2: 562, 3: 129},
    's4_extra_slopes': 857,
    's4_extra_sup_events': 869,
    's5_class': {'UNSTRUCTURED': 690, 'TANGENT': 123, 'DIHEDRAL': 44},
    's5_ohist': {8: 333, 7: 326, 6: 75, 9: 109, 10: 14},
    's5_cascades': (14, 14, 3),
    's5_all_structured_pairs': 111,
    's5_deep_uv': 15,
    's6_hist': {1: 28365, 2: 6123, 3: 1058, 0: 64454},
    's6_sup_events': 46205,
    's6_class': {'UNSTRUCTURED': 6773, 'DIHEDRAL': 558, 'TANGENT': 1021},
    's6_all_structured_pairs': 1173,
    's6_ohist2': {8: 2347, 7: 2367, 9: 735, 6: 674},
    's6_cascades': ([7], 1),
    's6c_repl': {987654: ([5, 6, 6, 6, 6, 7, 7, 8], 8),
                 13579: ([4, 5, 6, 6, 6, 6, 6, 7, 8], 9)},
    's7_sum_constructed': 16714,
    's7_sum_organic': 16467,
}
if FREEZE:
    EXPECTED = None


def main():
    astar = s1()
    H, sups = build_H(astar)
    reps = s2(sups)
    s3(H, sups, astar)
    s4_s5(H, sups, astar, reps)
    s6(H, sups, astar)
    s6c(H, sups, astar)
    s7()
    if FREEZE:
        print("\nEXPECTED =", repr(OBS))
    ok = all(RESULTS)
    print(f"\n{sum(RESULTS)}/{len(RESULTS)} PASS -> "
          f"{'ALL PASS' if ok else 'FAIL'}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
