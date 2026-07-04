#!/usr/bin/env python3
"""SP-CENSUS-2 coprime-dihedral reclassification check.

The SP-CENSUS support classifier includes cyclic pullbacks and dihedral
fiber-unions with gcd(n,m)>1.  A natural cheap repair for the F1153/mu32,h=8
boundary mass is to add the missing coprime dihedral pair-fibers
X^m + alpha X^-m with gcd(n,m)=1.  This verifier tests that repair directly on
the known in-range falsifier cell.

Result: the augmented classifier charges no additional anchored h=8 pairs.
The 976 survivors remain survivors, so the boundary mass is not an omitted
coprime-dihedral artifact.
"""

from __future__ import annotations

from array import array
from collections import Counter
from itertools import combinations
import json
import math
import os
import sys
from typing import Any

import numpy as np

import verify_h1_u1_toy_harness as h1
import verify_sp_census_split_pairs as sp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "spc2-dihedral-g1-reclass",
    "spc2_dihedral_g1_reclass.json",
)

FAILS: list[str] = []
NCHECK = 0

P = 1153
N = 32
T = 3
H = 8


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


def dihedral_classes_include_g1(n: int, m: int, offset: int) -> list[int]:
    g = math.gcd(n, m)
    step = n // g
    out: list[int] = []
    seen: set[int] = set()
    for r in range(step):
        if r in seen:
            continue
        residues = {r % step, (offset - r) % step}
        seen.update(residues)
        mask = 0
        for a in residues:
            for j in range(g):
                mask |= 1 << ((a + j * step) % n)
        out.append(mask)
    return out


def augmented_partitions(row: sp.SplitRow) -> list[tuple[str, list[int]]]:
    out = sp.charged_partitions(row)
    for m in range(row.t + 1, sp.h_max(row) + 1):
        if math.gcd(row.n, m) != 1:
            continue
        for offset in range(row.n):
            out.append(
                (
                    f"dihedral:g=1:m={m}:offset={offset}",
                    dihedral_classes_include_g1(row.n, m, offset),
                )
            )
    return out


def comb_mask_and_code(comb: tuple[int, ...], domain: list[int]) -> tuple[int, int]:
    mask = 0
    e = [0] * (T + 1)
    e[0] = 1
    for i in comb:
        mask |= 1 << i
        x = domain[i]
        for r in range(T, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % P
    code = 0
    mul = 1
    for v in e[1:]:
        code += v * mul
        mul *= P
    return mask, code


def signature_arrays(domain: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    keys = array("Q")
    masks = array("I")
    for comb in combinations(range(N), H):
        mask, code = comb_mask_and_code(comb, domain)
        keys.append(code)
        masks.append(mask)
    key_arr = np.frombuffer(keys, dtype=np.uint64).copy()
    mask_arr = np.frombuffer(masks, dtype=np.uint32).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, mask_arr, order


def analyze() -> dict[str, Any]:
    row = sp.SplitRow("F1153_mu32_t3_h8", P, N, T)
    domain = h1.mu_domain(P, N)
    old_partitions = sp.charged_partitions(row)
    new_partitions = augmented_partitions(row)

    check("row is in the intended q>n^2 range", P > N * N, f"p={P}, n^2={N*N}")
    check("row has n | p-1", (P - 1) % N == 0)
    check("augmented classifier adds coprime dihedral partitions", len(new_partitions) > len(old_partitions))

    key_arr, mask_arr, order = signature_arrays(domain)
    counts = Counter()
    old_reasons = Counter()
    new_reasons = Counter()
    remaining_examples: list[dict[str, Any]] = []

    start = 0
    while start < len(order):
        code = key_arr[order[start]]
        end = start + 1
        while end < len(order) and key_arr[order[end]] == code:
            end += 1
        if end - start < 2:
            start = end
            continue
        group = [int(mask_arr[order[i]]) for i in range(start, end)]
        for q_mask in group:
            if q_mask & 1:
                continue
            for p_mask in group:
                if not (p_mask & 1):
                    continue
                if p_mask == q_mask or (p_mask & q_mask):
                    continue
                old = sp.charged_reason(q_mask, p_mask, old_partitions)
                new = sp.charged_reason(q_mask, p_mask, new_partitions)
                if old is None:
                    counts["old_nontoral"] += 1
                else:
                    counts["old_charged"] += 1
                    old_reasons[old] += 1
                if new is None:
                    counts["new_nontoral"] += 1
                    if len(remaining_examples) < 8:
                        remaining_examples.append(
                            {
                                "Q_exponents": sp.exps(q_mask, N),
                                "P_exponents": sp.exps(p_mask, N),
                                "signature_code": int(code),
                            }
                        )
                else:
                    counts["new_charged"] += 1
                    new_reasons[new] += 1
        start = end

    added_reasons = {
        reason: count
        for reason, count in new_reasons.items()
        if reason.startswith("dihedral:g=1:")
    }
    check("old classifier reproduces 976 h=8 survivors", counts["old_nontoral"] == 976)
    check("augmented classifier leaves the 976 h=8 survivors", counts["new_nontoral"] == 976)
    check("coprime dihedral adds no charges", not added_reasons)
    check(
        "anchored accounting total is unchanged",
        counts["old_nontoral"] + counts["old_charged"] == counts["new_nontoral"] + counts["new_charged"],
    )

    return {
        "row": row.name,
        "p": P,
        "n": N,
        "t": T,
        "h": H,
        "subset_count": math.comb(N, H),
        "old_partition_count": len(old_partitions),
        "augmented_partition_count": len(new_partitions),
        "old_charged": counts["old_charged"],
        "old_nontoral": counts["old_nontoral"],
        "new_charged": counts["new_charged"],
        "new_nontoral": counts["new_nontoral"],
        "old_reasons": dict(sorted(old_reasons.items())),
        "new_reasons": dict(sorted(new_reasons.items())),
        "coprime_dihedral_added_charges": added_reasons,
        "remaining_examples": remaining_examples,
    }


def build_certificate() -> dict[str, Any]:
    result = analyze()
    return {
        "task": "SP-CENSUS-2 coprime-dihedral reclassification",
        "node": "spc2_dihedral_g1_reclass",
        "status": "NEGATIVE RESULT: coprime dihedral pair-fibers do not charge the F1153/mu32,h=8 boundary survivors",
        "interpretation": (
            "The known 976 anchored h=8 survivors are not an artifact of omitting "
            "gcd(n,m)=1 dihedral fibers from the SP-CENSUS support classifier."
        ),
        "result": result,
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

    r = cert["result"]
    print("\nreclassification summary:")
    print(
        f"{r['row']}: old_nontoral={r['old_nontoral']} new_nontoral={r['new_nontoral']} "
        f"old_charged={r['old_charged']} new_charged={r['new_charged']}"
    )
    print(f"old reasons: {r['old_reasons']}")
    print(f"coprime dihedral added charges: {r['coprime_dihedral_added_charges']}")

    if FAILS:
        print("\nFAIL:")
        for fail in FAILS:
            print(f"  - {fail}")
        return 1
    print(f"\nPASS: {NCHECK} SP-CENSUS-2 coprime-dihedral reclassification checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
