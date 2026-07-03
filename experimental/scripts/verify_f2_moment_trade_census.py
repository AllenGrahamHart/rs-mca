#!/usr/bin/env python3
"""F2/E37 verifier: low-memory census for primitive moment-trade blocks.

Searches for 0/1 dual words on mu_n with t=3 leading zero syndromes:

    sum_{e in E} zeta^(r e) = 0,  r = 1,2,3.

The exact MITM census is intentionally capped at b <= 8 on this machine.  The
full F2 spec asks for b in (t, 2t+4] = 4..10; b=9,10 need the n=64 h=5
half-table and are left as an explicit unscanned band here.

Run:
  python3 experimental/scripts/verify_f2_moment_trade_census.py
To refresh the pinned certificate:
  python3 experimental/scripts/verify_f2_moment_trade_census.py --write-certificate
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
import json
import math
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "f2-moment-trade-census",
    "f2_moment_trade_census.json",
)

T = 3
MAX_SCANNED_B = 8
REP_TARGETS = ("near_n", "n2", "n3", "2^61")

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


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic for n < 2^64.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    import math as _math

    c = 1
    while True:
        x = 2
        y = 2
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = _math.gcd(abs(x - y), n)
        if d != n:
            return d
        c += 1


def factor(n: int, out: list[int]) -> None:
    if n == 1:
        return
    if is_prime(n):
        out.append(n)
        return
    d = pollard_rho(n)
    factor(d, out)
    factor(n // d, out)


def next_prime_congruent_one(n: int, target: int) -> int:
    k = max(1, (target - 1 + n - 1) // n)
    while True:
        p = k * n + 1
        if is_prime(p):
            return p
        k += 1


def first_primes_congruent_one(n: int, count: int) -> list[int]:
    out: list[int] = []
    k = 1
    while len(out) < count:
        p = k * n + 1
        if is_prime(p):
            out.append(p)
        k += 1
    return out


def primitive_root(p: int) -> int:
    fac: list[int] = []
    factor(p - 1, fac)
    prime_factors = sorted(set(fac))
    g = 2
    while True:
        if all(pow(g, (p - 1) // r, p) != 1 for r in prime_factors):
            return g
        g += 1


def mask_from_exponents(exps: list[int]) -> int:
    mask = 0
    for e in exps:
        mask |= 1 << e
    return mask


def exponents_from_mask(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def dihedral_class(mask: int, n: int) -> str:
    exps = set(exponents_from_mask(mask, n))
    for shift in range(1, n):
        if {(e + shift) % n for e in exps} == exps:
            return "quotient_or_rotational"
    for shift in range(n):
        if {(shift - e) % n for e in exps} == exps:
            return "dihedral"
    return "primitive"


def syndrome(exps: list[int], zeta: int, p: int, t: int = T) -> tuple[int, ...]:
    out = [0] * t
    for e in exps:
        x = pow(zeta, e, p)
        y = x
        for r in range(t):
            out[r] = (out[r] + y) % p
            y = y * x % p
    return tuple(out)


def singleton_vectors(n: int, p: int, t: int = T) -> tuple[int, list[tuple[int, ...]]]:
    g = primitive_root(p)
    zeta = pow(g, (p - 1) // n, p)
    vecs = []
    for e in range(n):
        x = pow(zeta, e, p)
        y = x
        row = []
        for _ in range(t):
            row.append(y)
            y = y * x % p
        vecs.append(tuple(row))
    return zeta, vecs


def precompute_half_tables(n: int, p: int, t: int = T) -> tuple[int, dict[int, list[tuple[tuple[int, ...], int]]], dict[int, dict[tuple[int, ...], list[int]]]]:
    zeta, vecs = singleton_vectors(n, p, t)
    entries: dict[int, list[tuple[tuple[int, ...], int]]] = {}
    tables: dict[int, dict[tuple[int, ...], list[int]]] = {}
    for h in (2, 3, 4):
        cur: list[tuple[tuple[int, ...], int]] = []
        table: dict[tuple[int, ...], list[int]] = defaultdict(list)
        for comb in combinations(range(n), h):
            syn = tuple(sum(vecs[i][r] for i in comb) % p for r in range(t))
            mask = mask_from_exponents(list(comb))
            cur.append((syn, mask))
            table[syn].append(mask)
        entries[h] = cur
        tables[h] = table
    return zeta, entries, tables


def find_primitive_block(
    n: int,
    p: int,
    b: int,
    entries: dict[int, list[tuple[tuple[int, ...], int]]],
    tables: dict[int, dict[tuple[int, ...], list[int]]],
) -> dict:
    h = b // 2
    k = b - h
    total = 0
    structured = 0
    first_structured: list[int] | None = None
    for syn2, mask2 in entries[k]:
        target = tuple((-x) % p for x in syn2)
        for mask1 in tables[h].get(target, ()):
            if mask1 & mask2:
                continue
            if h == k and mask1 > mask2:
                continue
            mask = mask1 | mask2
            cls = dihedral_class(mask, n)
            total += 1
            if cls == "primitive":
                return {
                    "b": b,
                    "primitive_exists": True,
                    "zero_syndrome_blocks_seen_until_witness": total,
                    "structured_before_witness": structured,
                    "witness_exponents": exponents_from_mask(mask, n),
                }
            structured += 1
            if first_structured is None:
                first_structured = exponents_from_mask(mask, n)
    return {
        "b": b,
        "primitive_exists": False,
        "zero_syndrome_blocks_total": total,
        "structured_zero_syndrome_blocks": structured,
        "first_structured_exponents": first_structured,
    }


@dataclass(frozen=True)
class Row:
    n: int
    p: int
    label: str


def representative_rows() -> list[Row]:
    rows: list[Row] = []
    for n in (16, 32, 64):
        targets = {
            "near_n": n + 1,
            "n2": n * n,
            "n3": n * n * n,
            "2^61": 2**61,
        }
        seen: set[int] = set()
        for label in REP_TARGETS:
            p = next_prime_congruent_one(n, targets[label])
            if p not in seen:
                rows.append(Row(n, p, label))
                seen.add(p)
    return rows


def scan_row(row: Row) -> dict:
    zeta, entries, tables = precompute_half_tables(row.n, row.p)
    by_weight = [find_primitive_block(row.n, row.p, b, entries, tables) for b in range(T + 1, MAX_SCANNED_B + 1)]
    primitive_weights = [r["b"] for r in by_weight if r["primitive_exists"]]
    return {
        "n": row.n,
        "p": row.p,
        "label": row.label,
        "log_p_over_log_n": math.log(row.p, row.n),
        "zeta": zeta,
        "primitive_weights": primitive_weights,
        "by_weight": by_weight,
    }


def threshold_scan_n64() -> list[dict]:
    rows = []
    for p in first_primes_congruent_one(64, 10):
        zeta, entries, tables = precompute_half_tables(64, p)
        row = find_primitive_block(64, p, 8, entries, tables)
        row.update({
            "n": 64,
            "p": p,
            "log_p_over_log_n": math.log(p, 64),
            "zeta": zeta,
        })
        rows.append(row)
    return rows


def known_witness_checks() -> dict:
    n = 64
    p = 193
    zeta = 11
    exps = [0, 1, 2, 4, 16, 45, 50, 60]
    mask = mask_from_exponents(exps)
    return {
        "n": n,
        "p": p,
        "zeta": zeta,
        "zeta_order_check": pow(zeta, n, p) == 1 and pow(zeta, n // 2, p) != 1,
        "exponents": exps,
        "syndrome_t3": list(syndrome(exps, zeta, p, 3)),
        "power_sum_r4": syndrome(exps, zeta, p, 4)[3],
        "dihedral_class": dihedral_class(mask, n),
    }


def adversarial_pattern_scan(rows: list[Row]) -> list[dict]:
    out = []
    for row in rows:
        zeta, _, _ = precompute_half_tables(row.n, row.p)
        ap_hits = 0
        primitive_ap_hits = 0
        first_hit = None
        for b in range(T + 1, MAX_SCANNED_B + 1):
            for start in range(row.n):
                for step in range(row.n):
                    exps = sorted({(start + step * i) % row.n for i in range(b)})
                    if len(exps) != b:
                        continue
                    if syndrome(exps, zeta, row.p) == (0, 0, 0):
                        ap_hits += 1
                        cls = dihedral_class(mask_from_exponents(exps), row.n)
                        if cls == "primitive":
                            primitive_ap_hits += 1
                        if first_hit is None:
                            first_hit = {"b": b, "exponents": exps, "class": cls}
        transported = None
        if row.n == 64:
            exps = [0, 1, 2, 4, 16, 45, 50, 60]
            transported = {
                "known_exponent_set_syndrome": list(syndrome(exps, zeta, row.p, 3)),
                "is_zero": syndrome(exps, zeta, row.p, 3) == (0, 0, 0),
            }
        out.append({
            "n": row.n,
            "p": row.p,
            "label": row.label,
            "ap_zero_syndrome_hits": ap_hits,
            "primitive_ap_zero_syndrome_hits": primitive_ap_hits,
            "first_ap_hit": first_hit,
            "known_witness_transport": transported,
            "subfield_supported_blocks": "not applicable in prime field F_p; prime-power q rows remain a separate construction check",
        })
    return out


def main() -> None:
    rows = representative_rows()
    representative = [scan_row(row) for row in rows]
    threshold = threshold_scan_n64()
    witness = known_witness_checks()
    adversarial = adversarial_pattern_scan(rows)

    n64_threshold_primes = [r for r in threshold if r["primitive_exists"]]
    high_rep_primitives = [
        (r["n"], r["p"], r["primitive_weights"])
        for r in representative
        if r["label"] in {"n2", "n3", "2^61"} and r["primitive_weights"]
    ]
    unscanned = [9, 10]

    check("known F_193/mu_64 witness has primitive zeta", witness["zeta_order_check"])
    check("known witness has t=3 zero syndrome", witness["syndrome_t3"] == [0, 0, 0])
    check("known witness is primitive under dihedral filter", witness["dihedral_class"] == "primitive")
    check("known witness is not t=4-null", witness["power_sum_r4"] != 0)
    check("n=64 threshold scan finds low-p primitive examples", bool(n64_threshold_primes))
    check("representative scales n^2 and above have no primitive b<=8 blocks", not high_rep_primitives)
    check("adversarial AP scan finds no primitive hits", all(r["primitive_ap_zero_syndrome_hits"] == 0 for r in adversarial))

    result = {
        "node": "x4b_moment_trade_exclusion",
        "task": "F2/E37",
        "status": "EVIDENCE: U2 survives checked t=3, b<=8 bands; b=9,10 unscanned here",
        "t": T,
        "scanned_weights": list(range(T + 1, MAX_SCANNED_B + 1)),
        "unscanned_weights_from_spec": unscanned,
        "representative_rows": representative,
        "n64_b8_threshold_scan": threshold,
        "known_witness": witness,
        "adversarial_patterns": adversarial,
        "summary": {
            "n64_primitive_primes_in_first_10": [
                {"p": r["p"], "log_p_over_log_n": r["log_p_over_log_n"], "witness": r.get("witness_exponents")}
                for r in n64_threshold_primes
            ],
            "first_n64_prime_after_low_hits_with_no_b8_primitive": next(
                (r["p"] for r in threshold if not r["primitive_exists"] and r["p"] > 577),
                None,
            ),
            "representative_high_scale_primitive_rows": high_rep_primitives,
        },
        "checks": NCHECK,
    }

    if "--write-certificate" in sys.argv:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")

    expected = None
    if os.path.exists(CERT):
        with open(CERT) as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print("  -", name)
        print(json.dumps(result["summary"], indent=2, sort_keys=True))
        sys.exit(1)

    print("\nsummary:")
    print(json.dumps(result["summary"], indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} F2 moment-trade census checks")


if __name__ == "__main__":
    main()
