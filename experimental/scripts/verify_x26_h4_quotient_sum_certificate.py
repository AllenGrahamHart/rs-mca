#!/usr/bin/env python3
"""X26 h=4 quotient-sum certificate.

The h=4 finite exceptions seen in X20-X22 are antipodal h=2 quotient lifts.
This verifier computes the underlying quotient h=2 sum-collision problem
directly:

    {1, a} and {b, c} in mu_{n/2},     1+a = b+c.

The zero-sum quotient collisions lift to the persistent mu_4 full fibers.  Any
extra quotient sum collision lifts to the paid antipodal_h2_quotient_lift
family.  The verifier sweeps the full n=16,32,64 boundary windows and records
exactly where those extra quotient collisions occur.
"""

from __future__ import annotations

from collections import Counter
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x21_h4_prime_sweep as x21


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x26-h4-quotient-sum-certificate",
    "x26_h4_quotient_sum_certificate.json",
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


def quotient_h2_anchored_collisions(p: int, m: int) -> dict[str, Any]:
    """Count anchored unordered h=2 quotient sum collisions in mu_m."""
    domain = h1.mu_domain(p, m)
    collisions: list[dict[str, Any]] = []
    reason_counts = Counter()
    for a in range(1, m):
        s = (domain[0] + domain[a]) % p
        anchor_pair = {0, a}
        for b in range(m):
            if b in anchor_pair:
                continue
            for c in range(b + 1, m):
                if c in anchor_pair:
                    continue
                if (domain[b] + domain[c]) % p != s:
                    continue
                q_pair = {b, c}
                zero_sum = (a == m // 2) and ((c - b) % m == m // 2)
                reason = "zero_sum_mu4_full_fiber" if zero_sum else "extra_antipodal_quotient_lift"
                reason_counts[reason] += 1
                if len(collisions) < 12:
                    collisions.append(
                        {
                            "P_quotient_exponents": [0, a],
                            "Q_quotient_exponents": [b, c],
                            "reason": reason,
                        }
                    )
    baseline = m // 2 - 1
    return {
        "p": p,
        "m": m,
        "total_anchored_quotient_collisions": sum(reason_counts.values()),
        "zero_sum_baseline": baseline,
        "extra_antipodal_quotient_lifts": reason_counts["extra_antipodal_quotient_lift"],
        "reason_counts": dict(sorted(reason_counts.items())),
        "examples": collisions,
    }


def analyze_family(n: int) -> dict[str, Any]:
    m = n // 2
    primes = x21.primes_one_mod_n(n, n * n, n**3)
    check(f"n={n}: prime list is nonempty", bool(primes))
    rows = [quotient_h2_anchored_collisions(p, m) for p in primes]
    baseline = m // 2 - 1
    check(
        f"n={n}: every quotient row contains the zero-sum baseline",
        all(row["zero_sum_baseline"] == baseline and row["reason_counts"].get("zero_sum_mu4_full_fiber", 0) == baseline for row in rows),
    )
    extra_rows = [row for row in rows if row["extra_antipodal_quotient_lifts"]]
    if n in (16, 32):
        check(f"n={n}: no extra quotient h=2 collisions", not extra_rows)
    if n == 64:
        expected = {
            4993: 12,
            7937: 12,
            10177: 4,
            11329: 4,
            26177: 4,
            50177: 4,
            51137: 4,
            65537: 4,
            156353: 4,
        }
        observed = {row["p"]: row["extra_antipodal_quotient_lifts"] for row in extra_rows}
        check("n=64: quotient extra rows match X22 antipodal primes", observed == expected, str(observed))
    return {
        "n": n,
        "quotient_m": m,
        "prime_count": len(primes),
        "p_min": primes[0],
        "p_max": primes[-1],
        "zero_sum_baseline": baseline,
        "extra_rows": extra_rows,
    }


def build_certificate() -> dict[str, Any]:
    families = [analyze_family(16), analyze_family(32), analyze_family(64)]
    check("all nonzero quotient extras are in n=64", all(not f["extra_rows"] for f in families if f["n"] != 64))
    return {
        "task": "X26 h=4 quotient-sum certificate",
        "node": "active_core_count_bound",
        "status": "EXACT FINITE CERTIFICATE: h=4 exceptional-prime mass is precisely quotient h=2 sum-collision mass",
        "families": families,
        "summary": {
            "families": [
                {
                    "n": f["n"],
                    "quotient_m": f["quotient_m"],
                    "prime_count": f["prime_count"],
                    "p_min": f["p_min"],
                    "p_max": f["p_max"],
                    "zero_sum_baseline": f["zero_sum_baseline"],
                    "extra_primes": {
                        str(row["p"]): row["extra_antipodal_quotient_lifts"]
                        for row in f["extra_rows"]
                    },
                }
                for f in families
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
        check("certificate matches recomputed summary", cert == expected)

    print("\nsummary:")
    for family in cert["summary"]["families"]:
        print(
            f"n={family['n']:<3d} q_m={family['quotient_m']:<3d} "
            f"primes={family['prime_count']:<4d} extras={family['extra_primes']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X26 h=4 quotient-sum certificate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
