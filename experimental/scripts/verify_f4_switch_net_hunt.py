#!/usr/bin/env python3
"""F4 verifier: characteristic-p switch-net hunt for U1.

The frozen v1 dictionary excludes unbounded map-orbit counts.  F4's residual
attack asks whether tame toy rows contain many disjoint ordered gadgets

    (P_i, Q_i),  |P_i| = |Q_i| = h,  P_i cap Q_i = empty,

with identical nonzero moment-defect vector

    Delta_i(r) = sum_{x in P_i} x^r - sum_{x in Q_i} x^r,   1 <= r <= t.

In characteristic p, any p of R identical-defect gadgets cancel together, so
R disjoint gadgets would create C(R,p) same-top-t switches.  The v1 frozen
test is only threatened when C(R,p) > n^2 and the gadgets are not explained by
at most floor(log2 n) domain-stabilizer orbits.

Run:
  python3 experimental/scripts/verify_f4_switch_net_hunt.py
Refresh certificate:
  python3 experimental/scripts/verify_f4_switch_net_hunt.py --write-certificate
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
import json
import math
import os
import sys
from typing import Iterable


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "f4-switch-net-hunt",
    "f4_switch_net_hunt.json",
)

FAILS: list[str] = []
NCHECK = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    if not cond:
        FAILS.append(name)


# ---------------------------------------------------------------------------
# Finite fields GF(p^e), int-encoded by base-p polynomial representatives.
# The small rows here have e <= 4; irreducibles are found by deterministic
# trial division over F_p rather than hard-coded.
# ---------------------------------------------------------------------------


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_divmod_p(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    a = trim(a[:])
    b = trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    q = [0] * max(1, (len(a) - len(b) + 1))
    inv_lc = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        d = len(a) - len(b)
        c = a[-1] * inv_lc % p
        q[d] = c
        for i, bi in enumerate(b):
            a[d + i] = (a[d + i] - c * bi) % p
        trim(a)
    return trim(q), trim(a)


def monic_polys_p(p: int, degree: int) -> Iterable[list[int]]:
    if degree == 0:
        yield [1]
        return
    for coeffs in product(range(p), repeat=degree):
        if coeffs[0] == 0:
            continue
        yield list(coeffs) + [1]


def is_irreducible_p(poly: list[int], p: int) -> bool:
    deg = len(poly) - 1
    if deg <= 1:
        return True
    for d in range(1, deg // 2 + 1):
        for div in monic_polys_p(p, d):
            _, rem = poly_divmod_p(poly, div, p)
            if rem == [0]:
                return False
    return True


def find_irreducible(p: int, e: int) -> tuple[int, ...]:
    if e == 1:
        return ()
    for poly in monic_polys_p(p, e):
        if is_irreducible_p(poly, p):
            return tuple(poly[:-1])
    raise RuntimeError(f"no irreducible found for GF({p}^{e})")


class GF:
    def __init__(self, p: int, e: int = 1):
        self.p = p
        self.e = e
        self.q = p**e
        self.name = f"F_{self.q}" if e == 1 else f"GF({self.q})"
        q = self.q
        if e == 1:
            self.modulus = ()
            add = [[(a + b) % p for b in range(q)] for a in range(q)]
            mul = [[(a * b) % p for b in range(q)] for a in range(q)]
        else:
            self.modulus = find_irreducible(p, e)

            def dec(x: int) -> list[int]:
                return [(x // (p**i)) % p for i in range(e)]

            def enc(dg: list[int]) -> int:
                return sum(d * (p**i) for i, d in enumerate(dg))

            def pmul(da: list[int], db: list[int]) -> list[int]:
                res = [0] * (2 * e - 1)
                for i, ai in enumerate(da):
                    if ai:
                        for j, bj in enumerate(db):
                            res[i + j] = (res[i + j] + ai * bj) % p
                for d in range(2 * e - 2, e - 1, -1):
                    c = res[d]
                    if c:
                        res[d] = 0
                        for i in range(e):
                            res[d - e + i] = (res[d - e + i] - c * self.modulus[i]) % p
                return res[:e]

            add = [
                [enc([(x + y) % p for x, y in zip(dec(a), dec(b))]) for b in range(q)]
                for a in range(q)
            ]
            mul = [[enc(pmul(dec(a), dec(b))) for b in range(q)] for a in range(q)]
        self.ADD = add
        self.MUL = mul
        self.NEG = [next(b for b in range(q) if add[a][b] == 0) for a in range(q)]
        self.SUB = [[add[a][self.NEG[b]] for b in range(q)] for a in range(q)]
        self.INV = [None] + [
            next(b for b in range(1, q) if mul[a][b] == 1) for a in range(1, q)
        ]

    def pow(self, a: int, m: int) -> int:
        out = 1
        x = a
        while m:
            if m & 1:
                out = self.MUL[out][x]
            x = self.MUL[x][x]
            m >>= 1
        return out

    def add_many(self, vals: Iterable[int]) -> int:
        acc = 0
        for v in vals:
            acc = self.ADD[acc][v]
        return acc

    def axioms_ok(self) -> bool:
        for a in range(self.q):
            if self.ADD[a][0] != a or self.MUL[a][1] != a:
                return False
            if a and self.MUL[a][self.INV[a]] != 1:
                return False
            for b in range(self.q):
                if self.ADD[a][b] != self.ADD[b][a] or self.MUL[a][b] != self.MUL[b][a]:
                    return False
        return True


def factor_distinct(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def primitive_element(F: GF) -> int:
    fac = factor_distinct(F.q - 1)
    for g in range(2, F.q):
        if all(F.pow(g, (F.q - 1) // r) != 1 for r in fac):
            return g
    raise RuntimeError(f"no primitive element found in {F.name}")


def mu_domain(F: GF, n: int) -> list[int]:
    if (F.q - 1) % n != 0:
        raise ValueError(f"n={n} does not divide q-1={F.q - 1}")
    g = primitive_element(F)
    omega = F.pow(g, (F.q - 1) // n)
    vals = [1]
    for _ in range(1, n):
        vals.append(F.MUL[vals[-1]][omega])
    if len(set(vals)) != n or F.pow(omega, n) != 1:
        raise RuntimeError(f"bad mu_{n} generator in {F.name}")
    return vals


# ---------------------------------------------------------------------------
# Switch-net enumeration and exact disjoint-family packing.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RowSpec:
    name: str
    p: int
    e: int
    n: int
    t: int
    gadget_sizes: tuple[int, ...]
    verdict_scope: str = "tame"


ROWS = (
    RowSpec("F8_mu7_small_p", 2, 3, 7, 3, (1, 2)),
    RowSpec("F9_mu8_prime_power", 3, 2, 8, 3, (1, 2, 3)),
    RowSpec("F16_mu15_char2", 2, 4, 15, 3, (1, 2)),
    RowSpec("F25_mu24_char5", 5, 2, 24, 3, (1, 2)),
    RowSpec("F27_mu26_char3", 3, 3, 26, 3, (1, 2)),
    RowSpec("F49_mu48_dickson_control", 7, 2, 48, 3, (1,), "wild-control"),
    RowSpec("F81_mu80_char3", 3, 4, 80, 3, (1,)),
)


def mask_from_comb(comb: tuple[int, ...]) -> int:
    out = 0
    for i in comb:
        out |= 1 << i
    return out


def exps_from_mask(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def transform_mask(mask: int, n: int, shift: int, inv: bool) -> int:
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            j = (-i if inv else i) + shift
            out |= 1 << (j % n)
    return out


def oriented_orbit_key(pmask: int, qmask: int, n: int) -> tuple[int, int]:
    images = []
    for inv in (False, True):
        for shift in range(n):
            images.append(
                (
                    transform_mask(pmask, n, shift, inv),
                    transform_mask(qmask, n, shift, inv),
                )
            )
    return min(images)


def subset_sums(F: GF, domain: list[int], h: int, t: int) -> list[tuple[int, tuple[int, ...]]]:
    powers = [[F.pow(x, r) for r in range(1, t + 1)] for x in domain]
    out = []
    for comb in combinations(range(len(domain)), h):
        sums = []
        for r in range(t):
            sums.append(F.add_many(powers[i][r] for i in comb))
        out.append((mask_from_comb(comb), tuple(sums)))
    return out


@dataclass
class Gadget:
    pmask: int
    qmask: int
    support: int
    orbit_key: tuple[int, int]


def enumerate_by_defect(F: GF, domain: list[int], h: int, t: int) -> dict[tuple[int, ...], list[Gadget]]:
    subs = subset_sums(F, domain, h, t)
    groups: dict[tuple[int, ...], list[Gadget]] = {}
    for pmask, psum in subs:
        for qmask, qsum in subs:
            if pmask & qmask:
                continue
            defect = tuple(F.SUB[a][b] for a, b in zip(psum, qsum))
            support = pmask | qmask
            groups.setdefault(defect, []).append(
                Gadget(pmask, qmask, support, oriented_orbit_key(pmask, qmask, len(domain)))
            )
    return groups


def first_family_at_least(cands: list[Gadget], n: int, need: int) -> list[Gadget] | None:
    if need <= 0:
        return []
    cands = sorted(cands, key=lambda g: (g.support.bit_count(), g.support, g.pmask, g.qmask))
    by_index = cands
    suffix_union = [0] * (len(by_index) + 1)
    for i in range(len(by_index) - 1, -1, -1):
        suffix_union[i] = suffix_union[i + 1] | by_index[i].support

    def rec(start: int, used: int, chosen: list[Gadget]) -> list[Gadget] | None:
        if len(chosen) >= need:
            return chosen[:]
        free_slots = (n - used.bit_count()) // max(1, by_index[0].support.bit_count())
        if len(chosen) + free_slots < need:
            return None
        if start >= len(by_index):
            return None
        future_free = (suffix_union[start] & ~used).bit_count()
        if len(chosen) + future_free // max(1, by_index[0].support.bit_count()) < need:
            return None
        for i in range(start, len(by_index)):
            g = by_index[i]
            if used & g.support:
                continue
            got = rec(i + 1, used | g.support, chosen + [g])
            if got is not None:
                return got
        return None

    return rec(0, 0, [])


def greedy_lower_bound(cands: list[Gadget]) -> list[Gadget]:
    out = []
    used = 0
    for g in sorted(cands, key=lambda z: (z.support, z.pmask, z.qmask)):
        if not (used & g.support):
            out.append(g)
            used |= g.support
    return out


def exact_max_family(cands: list[Gadget], n: int) -> list[Gadget]:
    lower = greedy_lower_bound(cands)
    best = lower[:]
    if not cands:
        return best
    edge_size = cands[0].support.bit_count()
    cands = sorted(cands, key=lambda g: (g.support, g.pmask, g.qmask))
    suffix_union = [0] * (len(cands) + 1)
    for i in range(len(cands) - 1, -1, -1):
        suffix_union[i] = suffix_union[i + 1] | cands[i].support

    def rec(start: int, used: int, chosen: list[Gadget]) -> None:
        nonlocal best
        if len(chosen) > len(best):
            best = chosen[:]
        if start >= len(cands):
            return
        free_slots = (n - used.bit_count()) // edge_size
        if len(chosen) + free_slots <= len(best):
            return
        future_free = (suffix_union[start] & ~used).bit_count()
        if len(chosen) + future_free // edge_size <= len(best):
            return
        for i in range(start, len(cands)):
            g = cands[i]
            if used & g.support:
                continue
            rec(i + 1, used | g.support, chosen + [g])

    rec(0, 0, [])
    return best


def threshold_for_more_than_n2(n: int, p: int, capacity: int) -> int | None:
    for r in range(p, capacity + 1):
        if math.comb(r, p) > n * n:
            return r
    return None


def family_record(fam: list[Gadget], n: int, p: int) -> dict[str, object]:
    orbit_count = len({g.orbit_key for g in fam})
    return {
        "R": len(fam),
        "switches_C_R_p": math.comb(len(fam), p) if len(fam) >= p else 0,
        "switches_log2": round(math.log2(math.comb(len(fam), p)), 6)
        if len(fam) >= p and math.comb(len(fam), p) > 0
        else None,
        "orbit_count": orbit_count,
        "v1_orbit_cap": int(math.log2(n)),
        "v1_chargeable_by_orbit_cap": orbit_count <= int(math.log2(n)),
        "gadgets": [
            {
                "P": exps_from_mask(g.pmask, n),
                "Q": exps_from_mask(g.qmask, n),
            }
            for g in fam
        ],
    }


def analyze_row(row: RowSpec) -> dict[str, object]:
    F = GF(row.p, row.e)
    domain = mu_domain(F, row.n)
    check(f"{row.name}: field axioms", F.axioms_ok(), f"q={F.q}, char={F.p}")
    row_out: dict[str, object] = {
        "row": row.name,
        "scope": row.verdict_scope,
        "field": F.name,
        "p": F.p,
        "e": F.e,
        "q": F.q,
        "n": row.n,
        "t": row.t,
        "modulus_low_coeffs": list(F.modulus),
        "gadget_sizes": [],
    }
    for h in row.gadget_sizes:
        groups = enumerate_by_defect(F, domain, h, row.t)
        zero = tuple([0] * row.t)
        nonzero_groups = {d: gs for d, gs in groups.items() if d != zero}
        capacity = row.n // (2 * h)
        danger_threshold = threshold_for_more_than_n2(row.n, F.p, capacity)
        p_switch_classes = 0
        danger_classes = 0
        max_family: list[Gadget] = []
        max_defect: tuple[int, ...] | None = None
        max_candidates = 0
        danger_record = None
        for defect, cands in nonzero_groups.items():
            max_candidates = max(max_candidates, len(cands))
            if len(cands) > len(max_family):
                fam_exact = exact_max_family(cands, row.n)
                if len(fam_exact) > len(max_family):
                    max_family = fam_exact
                    max_defect = defect
            if len(cands) < F.p:
                continue
            fam_p = first_family_at_least(cands, row.n, F.p)
            if fam_p is not None:
                p_switch_classes += 1
            need = danger_threshold
            if need is not None and len(cands) >= need:
                fam_danger = first_family_at_least(cands, row.n, need)
                if fam_danger is not None:
                    danger_classes += 1
                    rec = family_record(fam_danger, row.n, F.p)
                    if danger_record is None:
                        danger_record = {"defect": list(defect), "family": rec}
                    if not rec["v1_chargeable_by_orbit_cap"]:
                        max_family = fam_danger
                        max_defect = defect
                        break
        max_rec = family_record(max_family, row.n, F.p) if max_family else None
        h_out = {
            "h": h,
            "total_defect_classes": len(groups),
            "nonzero_defect_classes": len(nonzero_groups),
            "total_ordered_gadgets": sum(len(v) for v in groups.values()),
            "zero_defect_ordered_gadgets": len(groups.get(zero, [])),
            "max_candidates_in_one_defect_class": max_candidates,
            "packing_capacity": capacity,
            "p_switch_classes": p_switch_classes,
            "danger_threshold_R": danger_threshold,
            "danger_classes": danger_classes,
            "max_disjoint_family_defect": list(max_defect) if max_defect is not None else None,
            "max_disjoint_family": max_rec,
            "first_danger_family": danger_record,
        }
        row_out["gadget_sizes"].append(h_out)
        no_unchargeable = True
        if danger_record is not None:
            no_unchargeable = bool(danger_record["family"]["v1_chargeable_by_orbit_cap"])
        check(
            f"{row.name}, h={h}: no v1-uncharged dangerous switch-net",
            no_unchargeable,
            f"p-switch classes={p_switch_classes}, danger classes={danger_classes}",
        )
    return row_out


def build_certificate() -> dict[str, object]:
    rows = [analyze_row(row) for row in ROWS]
    dangerous = []
    uncharged = []
    for row in rows:
        for h_out in row["gadget_sizes"]:
            rec = h_out["first_danger_family"]
            if rec is not None:
                dangerous.append((row["row"], h_out["h"], rec))
                if not rec["family"]["v1_chargeable_by_orbit_cap"]:
                    uncharged.append((row["row"], h_out["h"], rec))
    return {
        "task": "F4 characteristic-p switch-net hunt",
        "node": "u1_pullback_dichotomy",
        "dictionary": "w3_chargeable_dictionary_grammar.md v1",
        "rows": rows,
        "dangerous_family_count": len(dangerous),
        "uncharged_dangerous_family_count": len(uncharged),
        "verdict": "NEGATIVE-CLEAN: no v1-uncharged C(R,p)>n^2 switch-net found",
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    cert = build_certificate()
    check(
        "F4 verdict: no uncharged dangerous switch-net",
        cert["uncharged_dangerous_family_count"] == 0,
        f"dangerous={cert['dangerous_family_count']}",
    )
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(cert, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")
    if FAILS:
        print("\nFAILURES:")
        for f in FAILS:
            print(f"  - {f}")
        return 1
    print(f"\nAll {NCHECK} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
