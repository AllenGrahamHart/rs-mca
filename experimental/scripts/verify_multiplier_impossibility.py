#!/usr/bin/env python3
"""Verifier for qa16_multiplier_impossibility.md (QA.16 scoping packet).

Re-derives every quantitative claim of the note:

  [L1]   Lemma 1 rank-1 collapse + mod-p kernel equality at (N',p)=(8,257),
         and the concrete failure of the integer-kernel claim without good
         multipliers.
  [T2]   Theorem 2: exhaustive multiplier search at (8,257), (16,65537),
         (16,12289): zero good c; exact best max-residues (61/15556/2890,
         refuting the prior "threshold+1" spot-check); generator
         independence; negation pairing.
  [H]    Section 4 heuristic tables (naive + refined), sign crossovers,
         the refined-boundary == norm-threshold coincidence, and toy
         consistency (loose, labelled heuristic).
  [MITM] Section 5.3 exact cost table at N'=128, budget bands, free
         height radius w<=14 / d*=7 at log2 p = 250.
  [C8]   Section 5.4: certificate C(8) at (16,12289) and (16,65537) by
         BOTH full exhaustion and the Proposition-4 MITM: 848 canonical
         kernel vectors, all cyclotomic, MITM == exhaustive; height
         freebie boundaries.

Deterministic (no randomness), stdlib only. Exits 0 iff all PASS.
"""

import itertools
import math
import sys

FAILURES = []


def report(ok, tag, msg):
    line = f"{'PASS' if ok else 'FAIL'} [{tag}] {msg}"
    print(line)
    if not ok:
        FAILURES.append(line)


def bal(a, p):
    """Balanced residue in (-p/2, p/2)."""
    a %= p
    return a - p if a > p // 2 else a


def prime_factors(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            f.add(d)
            n //= d
        d += 1
    if n > 1:
        f.add(n)
    return f


def element_of_exact_order(p, order):
    """Deterministic: smallest a >= 2 with a^((p-1)/order) of exact order."""
    assert (p - 1) % order == 0
    e = (p - 1) // order
    for a in range(2, p):
        w = pow(a, e, p)
        if pow(w, order, p) != 1:
            continue
        if all(pow(w, order // q, p) != 1 for q in prime_factors(order)):
            return w
    raise AssertionError("no element found")


def exact_order(a, p):
    o, x = 1, a % p
    while x != 1:
        x = x * a % p
        o += 1
    return o


# ----------------------------------------------------------------------
# [L1] Lemma 1: rank-1 mod p; kernel equality; integer-claim failure.
# ----------------------------------------------------------------------

def rank_mod_p(rows, p):
    rows = [list(r) for r in rows]
    rank, ncols = 0, len(rows[0])
    for col in range(ncols):
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [v * inv % p for v in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % p:
                f = rows[i][col]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def ternary_kernels(Np, p, z, R):
    """(base mod-p kernel, stacked mod-p kernel) over all ternary vectors."""
    base_ker, stacked_ker = set(), set()
    for v in itertools.product((-1, 0, 1), repeat=Np):
        if not any(v):
            continue
        if sum(vx * zx for vx, zx in zip(v, z)) % p == 0:
            base_ker.add(v)
        if all(sum(vx * rx for vx, rx in zip(v, row)) % p == 0 for row in R):
            stacked_ker.add(v)
    return base_ker, stacked_ker


def check_lemma1():
    mults = [2, 3, 5, 7]  # deterministic; none good (no good c exists, T2/SS2)

    # ---- rank-1 + kernel equality at both demo pairs ----
    for Np, p in ((8, 257), (8, 41)):
        w = element_of_exact_order(p, Np)
        z = [pow(w, x, p) for x in range(Np)]
        R = [[bal(c * zx, p) for zx in z] for c in mults]
        r = rank_mod_p(R, p)
        report(r == 1, "L1", f"({Np},{p}) k=4 residue matrix rank mod p = {r} (claim: 1)")
        base_ker, stacked_ker = ternary_kernels(Np, p, z, R)
        report(
            base_ker == stacked_ker,
            "L1",
            f"({Np},{p}) ternary mod-p kernel of stacked k=4 system == kernel "
            f"of base row ({len(base_ker)} vectors): zero new information mod p",
        )

    # ---- (8,257): the FULL ternary kernel is exactly cyclotomic ----
    # bonus PROVED fact (digit argument): folding zeta^{x+4} = -zeta^x turns a
    # ternary relation into a+4b+16c+64d = 0 mod 257 with digits in [-2,2];
    # 2*(1+4+16+64) = 170 < 257 makes it exact; digit uniqueness kills it.
    Np, p = 8, 257
    w = element_of_exact_order(p, Np)
    z = [pow(w, x, p) for x in range(Np)]
    base_ker, _ = ternary_kernels(Np, p, z, [])
    cyc = {v for v in base_ker if all(v[x] == v[x + 4] for x in range(4))}
    report(
        len(base_ker) == 80 and base_ker == cyc and 2 * (1 + 4 + 16 + 64) < p,
        "L1",
        f"(8,257) full ternary kernel = {len(base_ker)} vectors, all "
        f"cyclotomic (digit bound 170 < 257): certificate C(8) holds "
        f"unconditionally at (8,257)",
    )

    # ---- (8,41): extras exist; the exact-integer-relation claim fails ----
    Np, p = 8, 41
    w = element_of_exact_order(p, Np)
    z = [pow(w, x, p) for x in range(Np)]
    R = [[bal(c * zx, p) for zx in z] for c in mults]
    base_ker, _ = ternary_kernels(Np, p, z, [])
    cyc = {v for v in base_ker if all(v[x] == v[x + 4] for x in range(4))}
    extras = base_ker - cyc
    report(
        len(base_ker) == 160 and len(cyc) == 80 and len(extras) == 80,
        "L1",
        f"(8,41) ternary kernel: {len(cyc)} cyclotomic + {len(extras)} "
        f"non-cyclotomic collisions",
    )
    nonzero_pairs, dist = 0, {i: 0 for i in range(5)}
    for v in extras:
        nz = 0
        for row in R:
            s = sum(vx * rx for vx, rx in zip(v, row))
            if s % p != 0:
                report(False, "L1", "pairing not a multiple of p (impossible)")
                return
            if s != 0:
                nz += 1
        nonzero_pairs += nz
        dist[nz] += 1
    report(
        nonzero_pairs == 176 and dist == {0: 16, 1: 4, 2: 8, 3: 52, 4: 0},
        "L1",
        f"(8,41) integer-claim failure: {nonzero_pairs}/320 (collision, "
        f"multiplier) pairings are NONZERO multiples of p; per-extra "
        f"failing-row distribution {tuple(dist[i] for i in range(5))} "
        f"(16 extras even survive all 4 rows: k multipliers do not exclude)",
    )
    # cyclotomic relations, by contrast, are exact for EVERY c (r_{x+4}=-r_x)
    ok = all(
        sum(vx * rx for vx, rx in zip(v, row)) == 0 for v in cyc for row in R
    )
    report(ok, "L1", "(8,41) cyclotomic relations are exact for every multiplier (sanity)")
    # no good c at (8,41) either (pigeonhole: 8 coset elements vs +-{1,2})
    good, best, _ = multiplier_scan(Np, p, w)
    report(
        good == 0 and best == 14,
        "L1",
        f"(8,41) exhaustive: 0 good c, best max-residue {best} vs threshold "
        f"{p / 20:.2f}",
    )


# ----------------------------------------------------------------------
# [T2] exhaustive multiplier search
# ----------------------------------------------------------------------

TOYS = [
    # (N', p, expected best, expected best c (smallest attaining), pinned coset)
    (8, 257, 61, 13, (13, 49, 52, 61)),
    (16, 65537, 15556, 3313, (3313, 3853, 3889, 12529, 13252, 15412, 15421, 15556)),
    (16, 12289, 2890, 821, (821, 1273, 2250, 2262, 2352, 2550, 2569, 2890)),
]


def multiplier_scan(Np, p, w):
    """Return (#good c, best max-residue, smallest best c)."""
    lp = Np // 2 + 1
    thr = p / (4 * lp)
    pw = [pow(w, x, p) for x in range(Np)]
    half = p // 2
    good, best, bestc = 0, p, None
    for c in range(1, p):
        m = 0
        for zx in pw:
            r = c * zx % p
            if r > half:
                r = p - r
            if r > m:
                m = r
        if m <= thr:
            good += 1
        if m < best:
            best, bestc = m, c
    return good, best, bestc


def check_theorem2():
    observed_best = []
    for Np, p, exp_best, exp_c, exp_coset in TOYS:
        lp = Np // 2 + 1
        thr = p / (4 * lp)
        w = element_of_exact_order(p, Np)
        assert exact_order(w, p) == Np
        # negation pairing (drives the refined heuristic)
        report(
            pow(w, Np // 2, p) == p - 1,
            "T2",
            f"(N'={Np}, p={p}) zeta^(N'/2) = -1: residues come in +- pairs",
        )
        good, best, bestc = multiplier_scan(Np, p, w)
        observed_best.append(best)
        report(
            good == 0,
            "T2",
            f"(N'={Np}, p={p}) l'={lp} threshold p/(4l')={thr:.2f}: "
            f"#good c over ALL {p - 1} multipliers = {good} (claim: 0)",
        )
        report(
            best == exp_best and bestc == exp_c,
            "T2",
            f"(N'={Np}, p={p}) best max-residue = {best} at c={bestc} "
            f"(pinned {exp_best} at c={exp_c}); ratio best/threshold = "
            f"{best / thr:.2f}",
        )
        coset = tuple(sorted(abs(bal(bestc * pow(w, x, p), p)) for x in range(Np)))
        # coset is +-symmetric: magnitudes come in equal pairs; unique magnitudes
        mags = tuple(sorted(set(coset)))
        report(
            mags == exp_coset,
            "T2",
            f"(N'={Np}, p={p}) best-coset magnitudes {mags} match note",
        )
        report(
            best > math.floor(thr) + 1,
            "T2",
            f"(N'={Np}, p={p}) prior spot-check 'best = threshold+1' "
            f"({math.floor(thr) + 1}) REFUTED: actual best {best}",
        )
    # generator independence at (8,257): w and w^3 give identical scan results
    Np, p = 8, 257
    w = element_of_exact_order(p, Np)
    w2 = pow(w, 3, p)  # gcd(3,8)=1 => same exact order, different generator
    assert exact_order(w2, p) == Np and w2 != w
    report(
        multiplier_scan(Np, p, w)[:2] == multiplier_scan(Np, p, w2)[:2],
        "T2",
        f"(8,257) scan identical for generators w={w} and w^3={w2} "
        f"(count depends only on the coset of mu_N')",
    )
    return observed_best


# ----------------------------------------------------------------------
# [H] heuristic tables and boundary coincidence
# ----------------------------------------------------------------------

def check_heuristics(observed_best):
    log2p = 250.0
    pinned = {
        32: (87.20, 168.60),
        64: (-136.84, 56.58),
        128: (-648.86, -199.43),
        256: (-1800.87, -775.44),
        512: (-4360.88, -2055.44),
    }
    print("     N'    log2 E naive    log2 E refined   (log2 p = 250, rho = 1/2)")
    ok = True
    for Np, (en, er) in pinned.items():
        lg = math.log2(Np + 2)  # 2l' = N' + 2
        naive = log2p - Np * lg
        refined = log2p - (Np / 2) * lg
        print(f"    {Np:4d}   {naive:12.2f}   {refined:14.2f}")
        ok &= abs(naive - en) < 0.01 and abs(refined - er) < 0.01
    report(ok, "H", "heuristic table matches note to 0.01")
    report(
        all(log2p - Np * math.log2(Np + 2) < -100 for Np in (128, 256, 512)),
        "H",
        "naive column overwhelming (< -100) at zone-(b) orders 128/256/512",
    )
    report(
        all(log2p - (Np / 2) * math.log2(Np + 2) < -100 for Np in (128, 256, 512)),
        "H",
        "refined column overwhelming (< -100) at zone-(b) orders 128/256/512",
    )

    def crossover(f):
        for Np in range(2, 600, 2):
            if f(Np) < 0:
                return Np
        return None

    cn = crossover(lambda N: log2p - N * math.log2(N + 2))
    cr = crossover(lambda N: log2p - (N / 2) * math.log2(N + 2))
    report(cn == 46, "H", f"naive sign crossover at N' = {cn} (44 -> 46 per note)")
    report(cr == 80, "H", f"refined sign crossover at N' = {cr} (78 -> 80 per note)")
    # refined boundary == norm threshold p = (2l')^(N'/2); s2 quotes at
    # log2 q = 256: N'=80 inside zone (a) (254.3 <= 256), N'=82 outside (262.1)
    a80 = 40 * math.log2(82)
    a82 = 41 * math.log2(84)
    report(
        a80 <= 256 < a82 and abs(a80 - 254.3) < 0.05 and abs(a82 - 262.1) < 0.05,
        "H",
        f"s2 zone-(a) boundary arithmetic reproduced: (80/2)log2(82)={a80:.1f}"
        f" <= 256 < (82/2)log2(84)={a82:.1f} — same expression as the refined"
        f" existence boundary (coincidence is rate-uniform in l' = rho N'+1)",
    )
    # toys: both formulas predict << 1 good multipliers; refined order
    # statistic predicts the observed best scale within a factor 2 (loose,
    # HEURISTIC consistency only)
    for (Np, p, _, _, _), best in zip(TOYS, observed_best):
        lp = Np // 2 + 1
        e_ref = (p - 1) * (1 / (2 * lp)) ** (Np / 2)
        pred_best = ((Np / (p - 1)) ** (2 / Np) * p - 1) / 2
        report(
            e_ref < 0.05 and 0.5 < best / pred_best < 2.0,
            "H",
            f"(N'={Np}, p={p}) refined model: E[#good]={e_ref:.2e} (<<1, "
            f"observed 0); predicted best ~{pred_best:.0f} vs observed {best} "
            f"(ratio {best / pred_best:.2f}) [HEURISTIC consistency]",
        )


# ----------------------------------------------------------------------
# [MITM] cost table, budget bands, free radius
# ----------------------------------------------------------------------

def check_mitm_costs():
    Np, log2p = 128, 250.0
    pinned = {
        12: 38.34, 14: 43.46, 16: 48.38, 18: 53.12, 20: 57.69,
        22: 62.11, 24: 66.40, 26: 70.55, 28: 74.59, 30: 78.52,
    }
    costs = {}
    print("      w    log2 cost = log2 C(128, w/2) + w/2")
    ok = True
    for w, exp in pinned.items():
        s = w // 2
        c = math.log2(math.comb(Np, s)) + s
        costs[w] = c
        print(f"     {w:2d}    {c:.2f}")
        ok &= abs(c - exp) < 0.01
    report(ok, "MITM", "N'=128 cost table matches note to 0.01")
    bands = {40: 12, 50: 16, 60: 20, 70: 24, 80: 30}
    got = {
        b: max((w for w in pinned if costs[w] <= b), default=0) for b in bands
    }
    report(
        got == bands,
        "MITM",
        f"budget bands max-w {got} (note: 2^40->12, 2^50->16, 2^60->20, "
        f"2^70->24, 2^80->30); QUEUE ESTIMATE 'w~24-30 at 2^40-2^50' CORRECTED",
    )
    free_w = max(w for w in range(1, 40) if (Np / 2) * math.log2(w) < log2p)
    dstar = max(d for d in range(1, 20) if (Np / 2) * math.log2(2 * d) < log2p)
    report(
        free_w == 14 and dstar == 7,
        "MITM",
        f"free height radius at (128, 2^250): w <= {free_w}, d* = {dstar} "
        f"swaps (MITM adds value from w = 15)",
    )


# ----------------------------------------------------------------------
# [C8] certificate C(8) at the two N'=16 toys: exhaustion vs MITM
# ----------------------------------------------------------------------

def census_exhaustive(Np, p, pw, W):
    """All ternary kernel vectors, 1 <= wt <= W, canonical (first sign +1)."""
    out = set()
    for wt in range(1, W + 1):
        for sup in itertools.combinations(range(Np), wt):
            states = [(pw[sup[0]] % p, (1,))]
            for x in sup[1:]:
                states = [
                    ((v + pw[x]) % p, s + (1,)) for v, s in states
                ] + [
                    ((v - pw[x]) % p, s + (-1,)) for v, s in states
                ]
            for v, s in states:
                if v == 0:
                    out.add((sup, s))
    return out


def census_mitm(Np, p, pw, W):
    """Proposition 4: halves of size <= ceil(W/2), disjoint opposite pairs."""
    s_max = (W + 1) // 2
    table = {}
    for sz in range(0, s_max + 1):
        for sup in itertools.combinations(range(Np), sz):
            for sgn in itertools.product((1, -1), repeat=sz):
                v = sum(e * pw[x] for x, e in zip(sup, sgn)) % p
                table.setdefault(v, []).append((sup, sgn))
    out = set()
    for v, lst in table.items():
        neg = (-v) % p
        if neg not in table:
            continue
        for s1, g1 in lst:
            for s2, g2 in table[neg]:
                if (not s1 and not s2) or set(s1) & set(s2):
                    continue
                vec = [0] * Np
                for x, e in zip(s1, g1):
                    vec[x] = e
                for x, e in zip(s2, g2):
                    vec[x] = e
                for e in vec:
                    if e:
                        if e < 0:
                            vec = [-t for t in vec]
                        break
                sup = tuple(i for i in range(Np) if vec[i])
                out.add((sup, tuple(vec[i] for i in sup)))
    return out


def check_certificate_c8():
    Np, W = 16, 8
    # predicted ternary-P count at weight <= 8, canonical (up to sign)
    pred = sum(math.comb(8, j) * 2 ** j for j in range(1, 5)) // 2
    report(pred == 848, "C8", f"predicted cyclotomic count at wt<=8: {pred}")
    for p in (12289, 65537):
        w = element_of_exact_order(p, Np)
        pw = [pow(w, x, p) for x in range(Np)]
        exh = census_exhaustive(Np, p, pw, W)
        mitm = census_mitm(Np, p, pw, W)
        report(
            exh == mitm,
            "C8",
            f"(16,{p}) MITM output == exhaustive census ({len(exh)} vectors)",
        )

        def is_cyc(entry):
            sup, s = entry
            vec = [0] * Np
            for x, e in zip(sup, s):
                vec[x] = e
            return all(vec[x] == vec[x + 8] for x in range(8))

        extras = [e for e in exh if not is_cyc(e)]
        report(
            len(exh) == 848 and not extras,
            "C8",
            f"(16,{p}) certificate C(8) HOLDS: {len(exh)} kernel vectors, "
            f"all cyclotomic, {len(extras)} extras",
        )
    # height freebie boundaries: real work at 12289 (w<=3 free), 65537 (w<=4)
    fw_12289 = max(w for w in range(1, 10) if w ** 8 < 12289)
    fw_65537 = max(w for w in range(1, 10) if w ** 8 < 65537)
    report(
        fw_12289 == 3 and fw_65537 == 4,
        "C8",
        f"height freebie: w <= {fw_12289} at p=12289, w <= {fw_65537} at "
        f"p=65537 — weights above that are genuinely MITM-certified "
        f"(radius extension 1 -> 4 swaps at p=12289)",
    )


def main():
    print("== QA.16 multiplier-impossibility verifier ==")
    print("-- [L1] Lemma 1: rank-1 collapse --")
    check_lemma1()
    print("-- [T2] Theorem 2: exhaustive multiplier search --")
    observed_best = check_theorem2()
    print("-- [H] Section 4: counting heuristic at scale --")
    check_heuristics(observed_best)
    print("-- [MITM] Section 5.3: cost table --")
    check_mitm_costs()
    print("-- [C8] Section 5.4: certificate C(8) at the toys --")
    check_certificate_c8()
    print()
    if FAILURES:
        print(f"OVERALL: FAIL ({len(FAILURES)} failing checks)")
        return 1
    print("OVERALL: PASS (all checks green)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
