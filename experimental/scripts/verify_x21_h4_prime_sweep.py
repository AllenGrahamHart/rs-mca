#!/usr/bin/env python3
"""X21 h=4 prime sweep for the cyclic-fingerprint route.

This is a low-memory prime sweep around the h=4 terminal boundary.  X20
classified the first-prime rows by two cyclic fingerprints.  Here we vary the
prime while holding n fixed:

  * n=16 and n=32: every prime p == 1 mod n with n^2 < p <= n^3;
  * n=64: the first 25 primes p == 1 mod n above n^2.

The sweep is deliberately modest.  Its purpose is to catch exceptional-prime
behavior without starting a large scan.  It finds that the only non-mu4
component in this range is still the paid antipodal h=2 quotient lift.
"""

from __future__ import annotations

from array import array
from collections import Counter
import json
import math
import os
import sys
from typing import Any

import numpy as np

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3
import verify_x20_h4_cyclic_fingerprint as x20


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x21-h4-prime-sweep",
    "x21_h4_prime_sweep.json",
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


def primes_one_mod_n(n: int, lo_exclusive: int, hi_inclusive: int, limit: int | None = None) -> list[int]:
    p = lo_exclusive + 1
    p += (1 - p) % n
    out: list[int] = []
    while p <= hi_inclusive and (limit is None or len(out) < limit):
        if h3.is_prime(p):
            out.append(p)
        p += n
    return out


def signature_arrays(p: int, n: int, domain: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    keys = array("Q")
    masks = array("Q")
    p2 = p * p
    if not (p2 * (p - 1) + p * (p - 1) + (p - 1) < 2**64):
        raise ValueError(f"h=4 signature does not fit uint64 for n={n}, p={p}")
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
                    masks.append((1 << a) | (1 << b) | (1 << c) | (1 << d))
    key_arr = np.frombuffer(keys, dtype=np.uint64).copy()
    mask_arr = np.frombuffer(masks, dtype=np.uint64).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, mask_arr, order


def analyze_prime(n: int, p: int) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    key_arr, mask_arr, order = signature_arrays(p, n, domain)
    counts = Counter()
    collision_groups = 0
    raw = 0

    start = 0
    while start < len(order):
        end = start + 1
        key = key_arr[order[start]]
        while end < len(order) and key_arr[order[end]] == key:
            end += 1
        if end - start > 1:
            collision_groups += 1
            group = [int(mask_arr[order[i]]) for i in range(start, end)]
            for p_mask in group:
                if not (p_mask & 1):
                    continue
                for q_mask in group:
                    if q_mask == p_mask or (q_mask & p_mask):
                        continue
                    raw += 1
                    counts[x20.classify_pair(p_mask, q_mask, n, domain, p)] += 1
        start = end

    return {
        "p": p,
        "collision_groups": collision_groups,
        "raw_anchored_partner_pairs": raw,
        "fingerprint_counts": dict(sorted(counts.items())),
    }


def analyze_family(n: int, mode: str, limit: int | None = None) -> dict[str, Any]:
    hi = n**3
    primes = primes_one_mod_n(n, n * n, hi, limit)
    check(f"n={n}: prime list is nonempty", bool(primes))
    if limit is None:
        check(f"n={n}: exhaustive window reaches p<=n^3", primes[-1] <= hi)
    else:
        check(f"n={n}: bounded sample has requested length", len(primes) == limit, f"limit={limit}")

    rows = [analyze_prime(n, p) for p in primes]
    bad = [row for row in rows if row["fingerprint_counts"].get("other", 0) > 0]
    check(f"n={n}: no h=4 non-fingerprinted pairs", not bad)
    check(
        f"n={n}: every prime has the persistent mu4 family",
        all(row["fingerprint_counts"].get("mu4_full_fiber", 0) == n // 4 - 1 for row in rows),
    )

    antipodal = [
        row for row in rows if row["fingerprint_counts"].get("antipodal_h2_quotient_lift", 0) > 0
    ]
    if n in (16, 32):
        check(f"n={n}: exhaustive window has no antipodal exceptions", not antipodal)
    if n == 64:
        check(
            "n=64 sample catches a paid antipodal exceptional prime",
            any(row["p"] == 4993 and row["fingerprint_counts"].get("antipodal_h2_quotient_lift") == 12 for row in antipodal),
        )

    return {
        "n": n,
        "mode": mode,
        "prime_count": len(primes),
        "p_min": primes[0],
        "p_max": primes[-1],
        "rows": rows,
        "nonfingerprinted_rows": bad,
        "antipodal_rows": antipodal,
    }


def build_certificate() -> dict[str, Any]:
    families = [
        analyze_family(16, "all primes n^2 < p <= n^3"),
        analyze_family(32, "all primes n^2 < p <= n^3"),
        analyze_family(64, "first 25 primes above n^2", limit=25),
    ]
    check(
        "all swept h=4 rows are cyclic-fingerprinted",
        all(not family["nonfingerprinted_rows"] for family in families),
    )
    check(
        "sweep includes the n=64 p=4993 paid antipodal exception",
        any(
            row["p"] == 4993
            for family in families
            for row in family["antipodal_rows"]
        ),
    )
    return {
        "task": "X21 h=4 prime sweep",
        "node": "active_core_count_bound",
        "status": "EXACT FINITE EVIDENCE: h=4 prime sweep finds no primitive residue; exceptional-prime mass is antipodal quotient-paid",
        "families": families,
        "summary": {
            "families": [
                {
                    "n": family["n"],
                    "mode": family["mode"],
                    "prime_count": family["prime_count"],
                    "p_min": family["p_min"],
                    "p_max": family["p_max"],
                    "antipodal_primes": [row["p"] for row in family["antipodal_rows"]],
                }
                for family in families
            ],
            "nonfingerprinted_count": sum(len(family["nonfingerprinted_rows"]) for family in families),
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

    print("\nfamily summary:")
    for family in cert["summary"]["families"]:
        print(
            f"n={family['n']:<3d} primes={family['prime_count']:<4d} "
            f"p=[{family['p_min']},{family['p_max']}] "
            f"antipodal={family['antipodal_primes']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X21 h=4 prime-sweep checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
