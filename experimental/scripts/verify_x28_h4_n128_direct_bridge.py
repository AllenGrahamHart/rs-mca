#!/usr/bin/env python3
"""X28 selected n=128 direct h=4 bridge.

X27 measured the cheap quotient h=2 supply for the h=4 antipodal-lift
mechanism.  This verifier checks selected n=128 primes directly in h=4 support
space and compares the observed h=4 fingerprints with the X27 quotient row.

The selected primes include the largest n=128 quotient row, two other high
extra rows, one boundary extra row, and one clean high-end row.  This is
evidence only: it does not replace a full n=128 h=4 prime-window sort.
"""

from __future__ import annotations

from array import array
from collections import Counter
import json
import os
import sys
import time
from typing import Any

import numpy as np

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3
import verify_x20_h4_cyclic_fingerprint as x20
import verify_x27_h4_large_quotient_sum as x27


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x28-h4-n128-direct-bridge",
    "x28_h4_n128_direct_bridge.json",
)

N = 128
SELECTED_PRIMES = (17921, 33409, 65537, 665857, 697601, 2095361)

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


def signature_arrays(p: int, n: int, domain: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return sorted h=4 signature arrays using uint32 packed supports."""
    p2 = p * p
    check(
        f"n={n}, p={p}: h=4 signature fits uint64",
        p2 * (p - 1) + p * (p - 1) + (p - 1) < 2**64,
    )

    keys = array("Q")
    codes = array("I")
    for a in range(n - 3):
        xa = domain[a]
        for b in range(a + 1, n - 2):
            xb = domain[b]
            e1_ab = (xa + xb) % p
            e2_ab = (xa * xb) % p
            for c in range(b + 1, n - 1):
                xc = domain[c]
                e1_abc = (e1_ab + xc) % p
                e2_abc = (e2_ab + xc * e1_ab) % p
                e3_abc = (xc * e2_ab) % p
                for d in range(c + 1, n):
                    xd = domain[d]
                    e1 = (e1_abc + xd) % p
                    e2 = (e2_abc + xd * e1_abc) % p
                    e3 = (e3_abc + xd * e2_abc) % p
                    keys.append(e1 + p * e2 + p2 * e3)
                    codes.append(x20.code4((a, b, c, d)))

    key_arr = np.frombuffer(keys, dtype=np.uint64).copy()
    code_arr = np.frombuffer(codes, dtype=np.uint32).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, code_arr, order


def analyze_prime(p: int) -> dict[str, Any]:
    check(f"p={p}: prime", h3.is_prime(p))
    check(f"p={p}: p == 1 mod {N}", (p - 1) % N == 0)
    check(f"p={p}: in n^2..n^3 boundary window", N * N < p <= N**3)

    start_time = time.time()
    domain = h1.mu_domain(p, N)
    key_arr, code_arr, order = signature_arrays(p, N, domain)

    counts = Counter()
    collision_groups = 0
    raw_anchored_pairs = 0
    examples: dict[str, list[dict[str, Any]]] = {}

    start = 0
    while start < len(order):
        end = start + 1
        key = key_arr[order[start]]
        while end < len(order) and key_arr[order[end]] == key:
            end += 1
        if end - start > 1:
            collision_groups += 1
            masks = [x20.mask4(int(code_arr[order[i]])) for i in range(start, end)]
            for p_mask in masks:
                if not (p_mask & 1):
                    continue
                for q_mask in masks:
                    if q_mask == p_mask or (q_mask & p_mask):
                        continue
                    raw_anchored_pairs += 1
                    kind = x20.classify_pair(p_mask, q_mask, N, domain, p)
                    counts[kind] += 1
                    bucket = examples.setdefault(kind, [])
                    if len(bucket) < 4:
                        bucket.append(
                            {
                                "P_exponents": x20.exps(p_mask, N),
                                "Q_exponents": x20.exps(q_mask, N),
                                "signature_code": int(key),
                            }
                        )
        start = end

    quotient = x27.quotient_h2_row(p, N // 2)
    expected_mu4 = quotient["zero_sum_mu4_full_fiber"]
    expected_extra = quotient["extra_antipodal_quotient_lifts"]

    check(f"p={p}: no primitive h=4 residue", counts.get("other", 0) == 0, str(dict(counts)))
    check(f"p={p}: mu4 count matches quotient baseline", counts.get("mu4_full_fiber", 0) == expected_mu4)
    check(
        f"p={p}: antipodal count matches quotient extra",
        counts.get("antipodal_h2_quotient_lift", 0) == expected_extra,
    )
    check(f"p={p}: raw h=4 count matches quotient total", raw_anchored_pairs == quotient["total_anchored_quotient_collisions"])

    return {
        "p": p,
        "collision_groups": collision_groups,
        "raw_anchored_pairs": raw_anchored_pairs,
        "fingerprint_counts": dict(sorted(counts.items())),
        "quotient_prediction": {
            "zero_sum_mu4_full_fiber": expected_mu4,
            "extra_antipodal_quotient_lifts": expected_extra,
            "total_anchored_quotient_collisions": quotient["total_anchored_quotient_collisions"],
        },
        "examples": examples,
        "elapsed_seconds": time.time() - start_time,
    }


def build_certificate() -> dict[str, Any]:
    rows = [analyze_prime(p) for p in SELECTED_PRIMES]
    check("selected set includes n=128 max quotient-extra row", any(row["p"] == 65537 and row["quotient_prediction"]["extra_antipodal_quotient_lifts"] == 52 for row in rows))
    check("selected set includes a clean high-end row", any(row["p"] == 2095361 and row["quotient_prediction"]["extra_antipodal_quotient_lifts"] == 0 for row in rows))
    check("all selected rows match quotient prediction", all(row["raw_anchored_pairs"] == row["quotient_prediction"]["total_anchored_quotient_collisions"] for row in rows))
    return {
        "task": "X28 h=4 n=128 direct bridge",
        "node": "active_core_count_bound",
        "status": (
            "EXACT FINITE EVIDENCE: selected n=128 direct h=4 support rows "
            "match the quotient h=2 ledger exactly"
        ),
        "n": N,
        "selected_primes": list(SELECTED_PRIMES),
        "rows": rows,
        "summary": {
            "rows": [
                {
                    "p": row["p"],
                    "collision_groups": row["collision_groups"],
                    "raw_anchored_pairs": row["raw_anchored_pairs"],
                    "fingerprint_counts": row["fingerprint_counts"],
                    "quotient_prediction": row["quotient_prediction"],
                }
                for row in rows
            ]
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
        for row, old_row in zip(comparable["rows"], expected["rows"]):
            row["elapsed_seconds"] = old_row.get("elapsed_seconds")
        check("certificate matches recomputed summary", comparable == expected)

    print("\nsummary:")
    print(json.dumps(cert["summary"], indent=2, sort_keys=True))

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X28 h=4 n=128 direct-bridge checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
