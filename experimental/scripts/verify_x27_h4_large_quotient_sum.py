#!/usr/bin/env python3
"""X27 large h=4 quotient-sum extension.

X26 reduced the checked h=4 exceptional-prime mass to the quotient h=2
sum-collision problem

    {1, a} and {b, c} in mu_{n/2},      1 + a = b + c.

This verifier extends that cheap quotient arithmetic to the full n=128 and
n=256 boundary windows.  It does not sort h=4 supports.  It only measures the
paid antipodal quotient-lift supply that X26 identified as the finite-p h=4
exception mechanism.
"""

from __future__ import annotations

from collections import defaultdict
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
    "x27-h4-large-quotient-sum",
    "x27_h4_large_quotient_sum.json",
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


def quotient_h2_row(p: int, m: int) -> dict[str, Any]:
    """Count anchored unordered quotient h=2 sum collisions in mu_m.

    The implementation is O(m^2) per prime: build unordered pair sums once,
    then query the anchored sums 1+a.  This keeps the n=256 full window small
    and avoids the O(m^3) loop used by X26's tiny-row certificate.
    """
    domain = h1.mu_domain(p, m)
    pair_sums: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for b in range(m - 1):
        xb = domain[b]
        for c in range(b + 1, m):
            pair_sums[(xb + domain[c]) % p].append((b, c))

    zero_sum = 0
    extra = 0
    examples: list[dict[str, Any]] = []
    for a in range(1, m):
        anchored_sum = (domain[0] + domain[a]) % p
        for b, c in pair_sums.get(anchored_sum, ()):
            if b == 0 or c == 0 or b == a or c == a:
                continue
            if a == m // 2 and (c - b) % m == m // 2:
                zero_sum += 1
                reason = "zero_sum_mu4_full_fiber"
            else:
                extra += 1
                reason = "extra_antipodal_quotient_lift"
            if len(examples) < 8:
                examples.append(
                    {
                        "P_quotient_exponents": [0, a],
                        "Q_quotient_exponents": [b, c],
                        "reason": reason,
                    }
                )

    return {
        "p": p,
        "zero_sum_mu4_full_fiber": zero_sum,
        "extra_antipodal_quotient_lifts": extra,
        "total_anchored_quotient_collisions": zero_sum + extra,
        "examples": examples,
    }


def analyze_family(n: int) -> dict[str, Any]:
    m = n // 2
    primes = x21.primes_one_mod_n(n, n * n, n**3)
    check(f"n={n}: prime list is nonempty", bool(primes))
    baseline = m // 2 - 1
    extra_rows: list[dict[str, Any]] = []
    total_extra = 0
    max_extra = 0
    baseline_bad: list[dict[str, Any]] = []

    for p in primes:
        row = quotient_h2_row(p, m)
        if row["zero_sum_mu4_full_fiber"] != baseline:
            baseline_bad.append(row)
        extra = row["extra_antipodal_quotient_lifts"]
        if extra:
            extra_rows.append(row)
            total_extra += extra
            max_extra = max(max_extra, extra)

    check(f"n={n}: zero-sum baseline holds at every prime", not baseline_bad)
    check(f"n={n}: extra quotient rows are sparse", len(extra_rows) < n, f"{len(extra_rows)} rows")
    check(f"n={n}: extra quotient mass is below n^2", total_extra < n * n, str(total_extra))
    check(f"n={n}: every single-row extra count is below n", max_extra < n, str(max_extra))

    return {
        "n": n,
        "quotient_m": m,
        "prime_count": len(primes),
        "p_min": primes[0],
        "p_max": primes[-1],
        "zero_sum_baseline": baseline,
        "extra_row_count": len(extra_rows),
        "extra_total": total_extra,
        "max_extra": max_extra,
        "extra_density": len(extra_rows) / len(primes),
        "baseline_bad": baseline_bad,
        "extra_rows": extra_rows,
    }


def compact_summary(family: dict[str, Any]) -> dict[str, Any]:
    return {
        "n": family["n"],
        "quotient_m": family["quotient_m"],
        "prime_count": family["prime_count"],
        "p_min": family["p_min"],
        "p_max": family["p_max"],
        "zero_sum_baseline": family["zero_sum_baseline"],
        "extra_row_count": family["extra_row_count"],
        "extra_total": family["extra_total"],
        "max_extra": family["max_extra"],
        "extra_density": family["extra_density"],
        "top_extra_rows": sorted(
            (
                {
                    "p": row["p"],
                    "extra_antipodal_quotient_lifts": row["extra_antipodal_quotient_lifts"],
                }
                for row in family["extra_rows"]
            ),
            key=lambda row: (-row["extra_antipodal_quotient_lifts"], row["p"]),
        )[:12],
    }


def build_certificate() -> dict[str, Any]:
    families = [analyze_family(128), analyze_family(256)]
    check("both large quotient families have intact baselines", all(not f["baseline_bad"] for f in families))
    check("both large quotient families have extra mass below n^2", all(f["extra_total"] < f["n"] ** 2 for f in families))
    return {
        "task": "X27 h=4 large quotient-sum extension",
        "node": "active_core_count_bound",
        "status": (
            "EXACT FINITE EVIDENCE: full n=128,256 quotient h=2 windows "
            "show sparse paid antipodal-lift mass and no baseline failure"
        ),
        "families": families,
        "summary": {"families": [compact_summary(f) for f in families]},
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
    print(json.dumps(cert["summary"], indent=2, sort_keys=True))

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X27 h=4 large quotient-sum checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
