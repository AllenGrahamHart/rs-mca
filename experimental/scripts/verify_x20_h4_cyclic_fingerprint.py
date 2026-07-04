#!/usr/bin/env python3
"""X20 h=4 cyclic fingerprint for terminal active pairs.

X14 showed that every checked h=4 active pair is cyclic-paid.  This verifier
refines that statement into two explicit cyclic fingerprints:

  1. full mu_4 fibers of X^4;
  2. antipodal-pair unions, which descend through X^2 to an h=2 quotient
     same-sum trade and are charged in the degree window by an equivalent
     cyclic partition such as X^6 when t=3.

The packet is finite evidence plus a small algebraic identity check.  It is not
a proof that all h=4 trades are cyclic-paid.
"""

from __future__ import annotations

from array import array
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
import json
import math
import os
import sys
from typing import Any

import numpy as np

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3
import verify_x13_h3_q_sweep as x13


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x20-h4-cyclic-fingerprint",
    "x20_h4_cyclic_fingerprint.json",
)

FAILS: list[str] = []
NCHECK = 0


@dataclass(frozen=True)
class SweepRow:
    n: int
    exponent_num: int
    exponent_den: int


ROWS = tuple(
    SweepRow(n, a, b)
    for n in (32, 64, 128)
    for a, b in ((2, 1), (9, 4), (5, 2), (3, 1))
)


def check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"   ({detail})"
    print(line, flush=True)
    if not cond:
        FAILS.append(name)


def row_label(row: SweepRow) -> str:
    return f"n{row.n}_alpha_{x13.exponent_label(row.exponent_num, row.exponent_den)}"


def first_prime_after_power(row: SweepRow) -> tuple[int, int]:
    floor_threshold = x13.floor_power_fraction(row.n, row.exponent_num, row.exponent_den)
    p = floor_threshold + 1
    p += (1 - p) % row.n
    while not h3.is_prime(p):
        p += row.n
    return p, floor_threshold


def code4(comb: tuple[int, int, int, int]) -> int:
    i, j, k, ell = comb
    return i | (j << 8) | (k << 16) | (ell << 24)


def exps4(code: int) -> list[int]:
    return [(code >> (8 * s)) & 255 for s in range(4)]


def mask4(code: int) -> int:
    out = 0
    for i in exps4(code):
        out |= 1 << i
    return out


def exps(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def signature_arrays(p: int, n: int, domain: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    keys = array("Q")
    codes = array("I")
    p2 = p * p
    check(
        f"n={n}, p={p}: h=4 signature fits uint64",
        p2 * (p - 1) + p * (p - 1) + (p - 1) < 2**64,
    )
    for comb in combinations(range(n), 4):
        e = [0, 0, 0, 0]
        e[0] = 1
        for i in comb:
            x = domain[i]
            for r in range(3, 0, -1):
                e[r] = (e[r] + x * e[r - 1]) % p
        keys.append(e[1] + p * e[2] + p2 * e[3])
        codes.append(code4(comb))
    key_arr = np.frombuffer(keys, dtype=np.uint64).copy()
    code_arr = np.frombuffer(codes, dtype=np.uint32).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, code_arr, order


def is_mu4_fiber(mask: int, n: int) -> bool:
    if mask.bit_count() != 4 or n % 4:
        return False
    step = n // 4
    residues = exps(mask, n)
    return all(((residues[0] + j * step) % n) in residues for j in range(4))


def antipodal_pairs(mask: int, n: int) -> list[int] | None:
    if mask.bit_count() != 4 or n % 2:
        return None
    half = n // 2
    residues = set(exps(mask, n))
    reps: list[int] = []
    seen: set[int] = set()
    for i in sorted(residues):
        if i in seen:
            continue
        j = (i + half) % n
        if j not in residues:
            return None
        seen.add(i)
        seen.add(j)
        reps.append(i % half)
    if len(reps) != 2:
        return None
    return sorted(reps)


def quotient_sum(mask: int, n: int, domain: list[int], p: int) -> int | None:
    reps = antipodal_pairs(mask, n)
    if reps is None:
        return None
    return sum((domain[i] * domain[i]) % p for i in reps) % p


def classify_pair(p_mask: int, q_mask: int, n: int, domain: list[int], p: int) -> str:
    if is_mu4_fiber(p_mask, n) and is_mu4_fiber(q_mask, n):
        return "mu4_full_fiber"

    p_sum = quotient_sum(p_mask, n, domain, p)
    q_sum = quotient_sum(q_mask, n, domain, p)
    if p_sum is not None and q_sum is not None and p_sum == q_sum:
        return "antipodal_h2_quotient_lift"

    return "other"


def verify_algebraic_fingerprints() -> None:
    # Full mu_4 fiber: roots of X^4-a have e1=e2=e3=0.
    for n in (32, 64, 128):
        p = first_prime_after_power(SweepRow(n, 3, 1))[0]
        domain = h1.mu_domain(p, n)
        mask = sum(1 << ((1 + j * (n // 4)) % n) for j in range(4))
        values = [domain[i] for i in exps(mask, n)]
        e = [0, 0, 0, 0]
        e[0] = 1
        for x in values:
            for r in range(3, 0, -1):
                e[r] = (e[r] + x * e[r - 1]) % p
        check(f"n={n}: mu_4 fiber has zero top-three signature", e[1:] == [0, 0, 0])

    # Antipodal union {+/-a,+/-b}: locator is
    # (X^2-a^2)(X^2-b^2), so e1=e3=0 and e2=-(a^2+b^2).
    p = 1153
    n = 32
    domain = h1.mu_domain(p, n)
    mask = (1 << 0) | (1 << 16) | (1 << 3) | (1 << 19)
    values = [domain[i] for i in exps(mask, n)]
    e = [0, 0, 0, 0]
    e[0] = 1
    for x in values:
        for r in range(3, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    qsum = quotient_sum(mask, n, domain, p)
    check("antipodal lift has e1=e3=0", e[1] == 0 and e[3] == 0)
    check("antipodal lift has e2 equal to minus quotient sum", qsum is not None and e[2] == (-qsum) % p)


def analyze_row(row: SweepRow) -> dict[str, Any]:
    label = row_label(row)
    p, floor_threshold = first_prime_after_power(row)
    check(f"{label}: p is prime", h3.is_prime(p), f"p={p}")
    check(f"{label}: p == 1 mod n", (p - 1) % row.n == 0)
    check(f"{label}: p exceeds floor(n^alpha)", p > floor_threshold, f"floor={floor_threshold}")

    domain = h1.mu_domain(p, row.n)
    key_arr, code_arr, order = signature_arrays(p, row.n, domain)

    fingerprint_counts = Counter()
    collision_groups = 0
    raw_anchored_pairs = 0
    examples: dict[str, list[dict[str, Any]]] = {}

    start = 0
    while start < len(order):
        end = start + 1
        code = key_arr[order[start]]
        while end < len(order) and key_arr[order[end]] == code:
            end += 1
        if end - start > 1:
            collision_groups += 1
            masks = [mask4(int(code_arr[order[i]])) for i in range(start, end)]
            for p_mask in masks:
                if not (p_mask & 1):
                    continue
                for q_mask in masks:
                    if q_mask == p_mask or (q_mask & p_mask):
                        continue
                    raw_anchored_pairs += 1
                    kind = classify_pair(p_mask, q_mask, row.n, domain, p)
                    fingerprint_counts[kind] += 1
                    bucket = examples.setdefault(kind, [])
                    if len(bucket) < 6:
                        bucket.append(
                            {
                                "P_exponents": exps(p_mask, row.n),
                                "Q_exponents": exps(q_mask, row.n),
                                "signature_code": int(code),
                            }
                        )
        start = end

    check(
        f"{label}: every active h=4 pair has a cyclic fingerprint",
        fingerprint_counts.get("other", 0) == 0,
        str(dict(fingerprint_counts)),
    )

    return {
        "label": label,
        "n": row.n,
        "p": p,
        "h": 4,
        "t": 3,
        "floor_n_alpha": floor_threshold,
        "subset_count": math.comb(row.n, 4),
        "signature_collision_groups": collision_groups,
        "raw_anchored_partner_pairs": raw_anchored_pairs,
        "fingerprint_counts": dict(sorted(fingerprint_counts.items())),
        "examples": examples,
    }


def build_certificate() -> dict[str, Any]:
    verify_algebraic_fingerprints()
    rows = [analyze_row(row) for row in ROWS]
    check(
        "all checked h=4 active pairs are cyclic-fingerprinted",
        all(row["fingerprint_counts"].get("other", 0) == 0 for row in rows),
    )
    check(
        "persistent mu4 full-fiber family appears in every row",
        all(row["fingerprint_counts"].get("mu4_full_fiber", 0) > 0 for row in rows),
    )
    check(
        "antipodal quotient-lift appears only in n128 alpha2",
        [
            row["label"]
            for row in rows
            if row["fingerprint_counts"].get("antipodal_h2_quotient_lift", 0) > 0
        ]
        == ["n128_alpha_2"],
    )

    return {
        "task": "X20 h=4 cyclic fingerprint",
        "node": "active_core_count_bound",
        "status": "FINITE EVIDENCE + PROVED FINGERPRINT IDENTITIES: checked h=4 active pairs split into mu4 full fibers or antipodal h2 quotient lifts",
        "rows": rows,
        "summary": {
            "rows_checked": [row["label"] for row in rows],
            "nonzero_other_rows": [
                row["label"] for row in rows if row["fingerprint_counts"].get("other", 0) > 0
            ],
            "antipodal_rows": [
                row["label"]
                for row in rows
                if row["fingerprint_counts"].get("antipodal_h2_quotient_lift", 0) > 0
            ],
        },
        "checks": NCHECK,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    cert = build_certificate()
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as fh:
            json.dump(cert, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"[write] {CERT}")

    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    print("\nrow summary:")
    for row in cert["rows"]:
        print(
            f"{row['label']:18s} p={row['p']:<9d} active={row['raw_anchored_partner_pairs']:<4d} "
            f"fingerprints={row['fingerprint_counts']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X20 h=4 cyclic-fingerprint checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
