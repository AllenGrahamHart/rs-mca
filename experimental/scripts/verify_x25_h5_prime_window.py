#!/usr/bin/env python3
"""X25 h=5 finite prime-window sweep.

X24 proves that characteristic-zero dyadic trades are empty when h is not a
power of two.  The first campaign-relevant odd size is h=5.  This verifier
checks whether finite-characteristic reductions create h=5 same-top-four
collisions in the first full boundary windows:

  n=16 and n=32, all primes p == 1 mod n with n^2 < p <= n^3.

The scan is exact and low-memory.  It intentionally stops at n=32 because a
full n=64 h=5 all-prime sweep would be much heavier.
"""

from __future__ import annotations

from array import array
from itertools import combinations
import json
import os
import sys
import time
from typing import Any

import numpy as np

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3
import verify_x21_h4_prime_sweep as x21


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x25-h5-prime-window",
    "x25_h5_prime_window.json",
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
    print(line, flush=True)
    if not cond:
        FAILS.append(name)


def signature_arrays_h5(p: int, n: int, domain: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return h=5 top-four signatures as two uint64 words plus subset masks."""
    key_lo = array("Q")
    key_hi = array("Q")
    masks = array("Q")
    if p * p >= 2**64:
        raise ValueError(f"h=5 two-word signature does not fit uint64 for p={p}")
    for comb in combinations(range(n), 5):
        e = [0, 0, 0, 0, 0]
        e[0] = 1
        mask = 0
        for i in comb:
            mask |= 1 << i
            x = domain[i]
            for r in range(4, 0, -1):
                e[r] = (e[r] + x * e[r - 1]) % p
        key_lo.append(e[1] + p * e[2])
        key_hi.append(e[3] + p * e[4])
        masks.append(mask)
    lo = np.frombuffer(key_lo, dtype=np.uint64).copy()
    hi = np.frombuffer(key_hi, dtype=np.uint64).copy()
    mask_arr = np.frombuffer(masks, dtype=np.uint64).copy()
    order = np.lexsort((lo, hi))
    return lo, hi, mask_arr, order


def analyze_prime(n: int, p: int) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    lo, hi, masks, order = signature_arrays_h5(p, n, domain)
    collision_groups = 0
    collision_subsets = 0
    max_group_size = 1
    examples: list[dict[str, Any]] = []

    start = 0
    while start < len(order):
        end = start + 1
        key_lo = lo[order[start]]
        key_hi = hi[order[start]]
        while end < len(order) and lo[order[end]] == key_lo and hi[order[end]] == key_hi:
            end += 1
        size = end - start
        if size > 1:
            collision_groups += 1
            collision_subsets += size
            max_group_size = max(max_group_size, size)
            if len(examples) < 5:
                examples.append(
                    {
                        "signature_low": int(key_lo),
                        "signature_high": int(key_hi),
                        "subsets": [
                            [i for i in range(n) if (int(masks[order[j]]) >> i) & 1]
                            for j in range(start, end)
                        ],
                    }
                )
        start = end

    return {
        "p": p,
        "subset_count": int(len(order)),
        "signature_collision_groups": collision_groups,
        "signature_collision_subsets": collision_subsets,
        "max_signature_group_size": max_group_size,
        "collision_examples": examples,
    }


def analyze_family(n: int) -> dict[str, Any]:
    primes = x21.primes_one_mod_n(n, n * n, n**3)
    check(f"n={n}: prime list is nonempty", bool(primes))
    check(f"n={n}: full boundary window has expected endpoint", primes[-1] <= n**3)

    start = time.time()
    rows = [analyze_prime(n, p) for p in primes]
    elapsed = time.time() - start
    collision_rows = [row for row in rows if row["signature_collision_groups"]]
    check(f"n={n}: no h=5 same-top-four collisions in full window", not collision_rows)
    return {
        "n": n,
        "mode": "all primes n^2 < p <= n^3",
        "prime_count": len(primes),
        "p_min": primes[0],
        "p_max": primes[-1],
        "elapsed_seconds": elapsed,
        "collision_rows": collision_rows,
        "max_subset_count": max(row["subset_count"] for row in rows),
    }


def build_certificate() -> dict[str, Any]:
    families = [analyze_family(16), analyze_family(32)]
    check("all checked h=5 prime windows are collision-free", all(not f["collision_rows"] for f in families))
    return {
        "task": "X25 h=5 prime-window sweep",
        "node": "active_core_count_bound",
        "status": "EXACT FINITE EVIDENCE: h=5 has no same-top-four collisions in full n=16,32 boundary windows",
        "families": families,
        "summary": {
            "families": [
                {
                    "n": f["n"],
                    "prime_count": f["prime_count"],
                    "p_min": f["p_min"],
                    "p_max": f["p_max"],
                    "collision_rows": len(f["collision_rows"]),
                    "max_subset_count": f["max_subset_count"],
                }
                for f in families
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
        comparable = dict(cert)
        for fam, exp in zip(comparable["families"], expected["families"]):
            fam["elapsed_seconds"] = exp.get("elapsed_seconds")
        check("certificate matches recomputed summary", comparable == expected)

    print("\nsummary:")
    for family in cert["summary"]["families"]:
        print(
            f"n={family['n']:<3d} primes={family['prime_count']:<4d} "
            f"p=[{family['p_min']},{family['p_max']}] collisions={family['collision_rows']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X25 h=5 prime-window checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
