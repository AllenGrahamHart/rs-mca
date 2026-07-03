#!/usr/bin/env python3
"""F2-EXT verifier: exact t=3 moment-trade MITM for b=9,10.

This extends the F2/E37 census into the two previously unscanned weights
without materializing Python dictionaries for the n=64, h=5 half-table.

For b=9 it uses a 4+5 meet-in-the-middle.  For b=10 it builds the h=5
half-table as numpy uint64 arrays, lexicographically sorts the syndrome
triples, and uses vectorized target lookup.  Peak memory is bounded by a few
uint64 arrays over C(64,5)=7,624,512 entries.

Run:
  python3 experimental/scripts/verify_f2_ext_large_bands.py
Refresh certificate:
  python3 experimental/scripts/verify_f2_ext_large_bands.py --write-certificate
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
import json
import math
import os
import sys
import time

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "f2-ext-large-bands",
    "f2_ext_large_bands.json",
)

T = 3
WEIGHTS = (9, 10)
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
    print(line, flush=True)
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
    c = 1
    while True:
        x = 2
        y = 2
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
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


def primitive_root(p: int) -> int:
    fac: list[int] = []
    factor(p - 1, fac)
    prime_factors = sorted(set(fac))
    g = 2
    while True:
        if all(pow(g, (p - 1) // r, p) != 1 for r in prime_factors):
            return g
        g += 1


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


def singleton_vectors(n: int, p: int) -> tuple[int, tuple[list[int], list[int], list[int]]]:
    g = primitive_root(p)
    zeta = pow(g, (p - 1) // n, p)
    rows = ([], [], [])
    for e in range(n):
        x = pow(zeta, e, p)
        y = x
        for r in range(T):
            rows[r].append(y)
            y = y * x % p
    return zeta, rows


def build_h4_table(n: int, p: int, vecs: tuple[list[int], list[int], list[int]]) -> dict[tuple[int, int, int], list[int]]:
    v0, v1, v2 = vecs
    table: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    bits = [1 << i for i in range(n)]
    for a, b, c, d in combinations(range(n), 4):
        syn = (
            (v0[a] + v0[b] + v0[c] + v0[d]) % p,
            (v1[a] + v1[b] + v1[c] + v1[d]) % p,
            (v2[a] + v2[b] + v2[c] + v2[d]) % p,
        )
        table[syn].append(bits[a] | bits[b] | bits[c] | bits[d])
    return table


def build_h5_arrays(n: int, p: int, vecs: tuple[list[int], list[int], list[int]]) -> tuple[np.ndarray, np.ndarray]:
    v0, v1, v2 = vecs
    bits = [np.uint64(1 << i) for i in range(n)]
    N = math.comb(n, 5)
    syn = np.empty((3, N), dtype=np.uint64)
    masks = np.empty(N, dtype=np.uint64)
    for idx, (a, b, c, d, e) in enumerate(combinations(range(n), 5)):
        syn[0, idx] = (v0[a] + v0[b] + v0[c] + v0[d] + v0[e]) % p
        syn[1, idx] = (v1[a] + v1[b] + v1[c] + v1[d] + v1[e]) % p
        syn[2, idx] = (v2[a] + v2[b] + v2[c] + v2[d] + v2[e]) % p
        masks[idx] = bits[a] | bits[b] | bits[c] | bits[d] | bits[e]
    return syn, masks


def classify_or_return(n: int, mask: int) -> tuple[bool, str, list[int]]:
    cls = dihedral_class(mask, n)
    return cls == "primitive", cls, exponents_from_mask(mask, n)


def scan_b9(
    n: int,
    p: int,
    h4: dict[tuple[int, int, int], list[int]],
    h5_syn: np.ndarray,
    h5_masks: np.ndarray,
) -> dict[str, object]:
    zero_seen = 0
    structured = 0
    first_structured = None
    for i in range(h5_masks.size):
        target = (
            (-int(h5_syn[0, i])) % p,
            (-int(h5_syn[1, i])) % p,
            (-int(h5_syn[2, i])) % p,
        )
        masks4 = h4.get(target)
        if not masks4:
            continue
        m5 = int(h5_masks[i])
        for m4 in masks4:
            if m4 & m5:
                continue
            mask = m4 | m5
            zero_seen += 1
            primitive, cls, exps = classify_or_return(n, mask)
            if primitive:
                return {
                    "b": 9,
                    "primitive_exists": True,
                    "zero_syndrome_blocks_seen_until_witness": zero_seen,
                    "structured_before_witness": structured,
                    "witness_exponents": exps,
                }
            structured += 1
            if first_structured is None:
                first_structured = {"class": cls, "exponents": exps}
    return {
        "b": 9,
        "primitive_exists": False,
        "zero_syndrome_blocks_total": zero_seen,
        "structured_zero_syndrome_blocks": structured,
        "first_structured": first_structured,
    }


def sorted_h5_groups(h5_syn: np.ndarray, h5_masks: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    order = np.lexsort((h5_syn[2], h5_syn[1], h5_syn[0]))
    syn = h5_syn[:, order]
    masks = h5_masks[order]
    diff = np.ones(masks.size, dtype=bool)
    diff[1:] = np.any(syn[:, 1:] != syn[:, :-1], axis=0)
    starts = np.nonzero(diff)[0]
    ends = np.r_[starts[1:], masks.size]
    return syn, masks, starts, ends


def scan_b10(n: int, p: int, syn: np.ndarray, masks: np.ndarray, starts: np.ndarray, ends: np.ndarray) -> dict[str, object]:
    uniq = syn[:, starts]
    dtype = np.dtype([("a", "<u8"), ("b", "<u8"), ("c", "<u8")])
    keys = np.empty(starts.size, dtype=dtype)
    keys["a"], keys["b"], keys["c"] = uniq[0], uniq[1], uniq[2]
    targets = np.empty(starts.size, dtype=dtype)
    pp = np.uint64(p)
    targets["a"] = (pp - uniq[0]) % pp
    targets["b"] = (pp - uniq[1]) % pp
    targets["c"] = (pp - uniq[2]) % pp
    pos = np.searchsorted(keys, targets)
    clipped = pos.clip(max=len(keys) - 1)
    valid = (pos < len(keys)) & (keys[clipped] == targets)

    zero_seen = 0
    structured = 0
    first_structured = None
    for gi in np.nonzero(valid)[0].tolist():
        tj = int(pos[gi])
        if gi > tj:
            continue
        left = masks[starts[gi] : ends[gi]]
        right = masks[starts[tj] : ends[tj]]
        for ma64 in left:
            ma = int(ma64)
            disjoint = right[(right & ma64) == 0]
            for mb64 in disjoint:
                mb = int(mb64)
                if gi == tj and ma > mb:
                    continue
                mask = ma | mb
                zero_seen += 1
                primitive, cls, exps = classify_or_return(n, mask)
                if primitive:
                    return {
                        "b": 10,
                        "primitive_exists": True,
                        "zero_syndrome_blocks_seen_until_witness": zero_seen,
                        "structured_before_witness": structured,
                        "witness_exponents": exps,
                    }
                structured += 1
                if first_structured is None:
                    first_structured = {"class": cls, "exponents": exps}
    return {
        "b": 10,
        "primitive_exists": False,
        "zero_syndrome_blocks_total": zero_seen,
        "structured_zero_syndrome_blocks": structured,
        "first_structured": first_structured,
    }


@dataclass(frozen=True)
class Row:
    n: int
    p: int
    label: str


def scan_rows() -> list[Row]:
    rows = []
    for n in (32, 64):
        seen: set[int] = set()
        for p in first_primes_congruent_one(n, 10):
            rows.append(Row(n, p, "first10"))
            seen.add(p)
        targets = {
            "near_n": n + 1,
            "n2": n * n,
            "n3": n * n * n,
            "2^61": 2**61,
        }
        for label in REP_TARGETS:
            p = next_prime_congruent_one(n, targets[label])
            if p not in seen:
                rows.append(Row(n, p, label))
                seen.add(p)
    return rows


def scan_row(row: Row) -> dict[str, object]:
    print(f"[row] n={row.n} p={row.p} label={row.label}", flush=True)
    t0 = time.time()
    zeta, vecs = singleton_vectors(row.n, row.p)
    h4 = build_h4_table(row.n, row.p, vecs)
    h4_class_count = len(h4)
    t_h4 = time.time()
    h5_syn, h5_masks = build_h5_arrays(row.n, row.p, vecs)
    t_h5 = time.time()
    b9 = scan_b9(row.n, row.p, h4, h5_syn, h5_masks)
    t_b9 = time.time()
    syn_sorted, masks_sorted, starts, ends = sorted_h5_groups(h5_syn, h5_masks)
    t_sort = time.time()
    b10 = scan_b10(row.n, row.p, syn_sorted, masks_sorted, starts, ends)
    t_b10 = time.time()
    del h4, h5_syn, h5_masks, syn_sorted, masks_sorted, starts, ends
    return {
        "n": row.n,
        "p": row.p,
        "label": row.label,
        "zeta": zeta,
        "log_p_over_log_n": math.log(row.p, row.n),
        "by_weight": [b9, b10],
        "timing_seconds": {
            "h4": round(t_h4 - t0, 3),
            "h5": round(t_h5 - t_h4, 3),
            "b9": round(t_b9 - t_h5, 3),
            "sort_h5": round(t_sort - t_b9, 3),
            "b10": round(t_b10 - t_sort, 3),
            "total": round(t_b10 - t0, 3),
        },
        "h5_entries": math.comb(row.n, 5),
        "h4_syndrome_classes": h4_class_count,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    rows = [scan_row(row) for row in scan_rows()]
    primitive_rows = [
        {"n": r["n"], "p": r["p"], "label": r["label"], "weights": [w["b"] for w in r["by_weight"] if w["primitive_exists"]]}
        for r in rows
        if any(w["primitive_exists"] for w in r["by_weight"])
    ]
    high_scale_hits = [
        row for row in primitive_rows if row["label"] in {"n2", "n3", "2^61"}
    ]
    n64_low = [row for row in primitive_rows if row["n"] == 64 and row["label"] == "first10"]
    n32_low = [row for row in primitive_rows if row["n"] == 32 and row["label"] == "first10"]

    check("F2-EXT scans both requested weights", all({w["b"] for w in r["by_weight"]} == set(WEIGHTS) for r in rows))
    check("F2-EXT scans n=32 and n=64", {r["n"] for r in rows} == {32, 64})
    check("low-p n=64 rows include primitive b=9 or b=10 examples", bool(n64_low))
    check("low-p n=32 rows include primitive b=9 or b=10 examples", bool(n32_low))
    check("representative n^2/n^3/2^61 rows have no primitive b=9,10 hits", not high_scale_hits, str(high_scale_hits[:3]))

    result = {
        "node": "x4b_moment_trade_exclusion",
        "task": "F2-EXT",
        "status": "EVIDENCE: exact b=9,10 MITM sweep completed for n=32,64 rows",
        "t": T,
        "weights": list(WEIGHTS),
        "rows": rows,
        "summary": {
            "primitive_rows": primitive_rows,
            "representative_high_scale_hits": high_scale_hits,
            "row_count": len(rows),
        },
        "checks": NCHECK,
    }
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")
    if FAILS:
        print("\nFAILURES:")
        for name in FAILS:
            print(f"  - {name}")
        print(json.dumps(result["summary"], indent=2, sort_keys=True))
        return 1
    print("\nsummary:")
    print(json.dumps(result["summary"], indent=2, sort_keys=True))
    print(f"\nAll {NCHECK} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
