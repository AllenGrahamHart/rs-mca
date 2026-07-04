#!/usr/bin/env python3
"""X22 h=4 full n=64 prime-window sweep.

This medium-cost verifier extends X21's bounded n=64 sample to the full
boundary window

    n = 64,       p == 1 mod 64,       64^2 < p <= 64^3.

It is intentionally isolated from the faster X21 verifier because it takes a
few minutes on the local machine.  The memory footprint stays small: each prime
uses the h=4 low-memory sort, then releases the table before the next prime.
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Any

import verify_x21_h4_prime_sweep as x21


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x22-h4-n64-full-window",
    "x22_h4_n64_full_window.json",
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


def build_certificate() -> dict[str, Any]:
    start = time.time()
    family = x21.analyze_family(64, "all primes n^2 < p <= n^3")
    elapsed = time.time() - start

    antipodal_primes = [row["p"] for row in family["antipodal_rows"]]
    check("full n=64 window has 693 primes", family["prime_count"] == 693)
    check("full n=64 window starts at p=4289", family["p_min"] == 4289)
    check("full n=64 window ends at p=261761", family["p_max"] == 261761)
    check("full n=64 window has no primitive/non-fingerprinted rows", not family["nonfingerprinted_rows"])
    check(
        "full n=64 window antipodal primes match certificate target",
        antipodal_primes == [4993, 7937, 10177, 11329, 26177, 50177, 51137, 65537, 156353],
    )

    return {
        "task": "X22 h=4 n=64 full prime-window sweep",
        "node": "active_core_count_bound",
        "status": (
            "EXACT FINITE EVIDENCE: full n=64, h=4 window has no primitive "
            "residue; all exceptional-prime mass is antipodal quotient-paid"
        ),
        "elapsed_seconds": elapsed,
        "family": family,
        "summary": {
            "n": 64,
            "prime_count": family["prime_count"],
            "p_min": family["p_min"],
            "p_max": family["p_max"],
            "nonfingerprinted_count": len(family["nonfingerprinted_rows"]),
            "antipodal_primes": antipodal_primes,
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
        comparable["elapsed_seconds"] = expected.get("elapsed_seconds")
        check("certificate matches recomputed summary", comparable == expected)

    print("\nsummary:")
    print(json.dumps(cert["summary"], indent=2, sort_keys=True))
    print(f"elapsed_seconds={cert['elapsed_seconds']:.2f}")

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X22 h=4 n=64 full-window checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
