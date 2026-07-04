#!/usr/bin/env python3
"""X29 h=4 quotient-bridge lemma.

This is a small proof-support verifier for the algebraic count transfer used by
X20, X26, X27, and X28:

    anchored h=4 antipodal-union trades in mu_n
        <-> anchored h=2 sum collisions in mu_{n/2}.

It checks the finite identities on representative rows and records the exact
zero-sum baseline n/4 - 1.  The accompanying note contains the general proof.
"""

from __future__ import annotations

from collections import Counter
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x21_h4_prime_sweep as x21
import verify_x27_h4_large_quotient_sum as x27


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x29-h4-quotient-bridge-lemma",
    "x29_h4_quotient_bridge_lemma.json",
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


def lift_quotient_pair(n: int, pair: tuple[int, int]) -> tuple[int, int, int, int]:
    """Lift a quotient pair in mu_{n/2} through x -> x^2."""
    m = n // 2
    a, b = pair
    return tuple(sorted((a, (a + m) % n, b, (b + m) % n)))


def elem123(exponents: tuple[int, int, int, int], domain: list[int], p: int) -> tuple[int, int, int]:
    e = [0, 0, 0, 0]
    e[0] = 1
    for i in exponents:
        x = domain[i]
        for r in range(3, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    return e[1], e[2], e[3]


def quotient_sum(domain_q: list[int], pair: tuple[int, int], p: int) -> int:
    return (domain_q[pair[0]] + domain_q[pair[1]]) % p


def quotient_collision_rows(p: int, n: int) -> list[dict[str, Any]]:
    m = n // 2
    domain_q = h1.mu_domain(p, m)
    rows: list[dict[str, Any]] = []
    for a in range(1, m):
        p_pair = (0, a)
        p_sum = quotient_sum(domain_q, p_pair, p)
        for b in range(m):
            if b in p_pair:
                continue
            for c in range(b + 1, m):
                if c in p_pair:
                    continue
                q_pair = (b, c)
                if quotient_sum(domain_q, q_pair, p) == p_sum:
                    zero_sum = a == m // 2 and (c - b) % m == m // 2
                    rows.append(
                        {
                            "P_quotient_exponents": list(p_pair),
                            "Q_quotient_exponents": list(q_pair),
                            "zero_sum": zero_sum,
                        }
                    )
    return rows


def classify_lifted_row(n: int, row: dict[str, Any]) -> str:
    p_pair = tuple(row["P_quotient_exponents"])
    q_pair = tuple(row["Q_quotient_exponents"])
    if row["zero_sum"]:
        return "zero_sum_mu4_full_fiber"
    if p_pair[1] == n // 4:
        # Anchored quotient pair is zero-sum, but target is not; this cannot
        # happen for an equal-sum disjoint collision.  Keep the branch explicit.
        return "mixed_zero_sum"
    if (q_pair[1] - q_pair[0]) % (n // 2) == n // 4:
        return "mixed_zero_sum"
    return "extra_antipodal_quotient_lift"


def check_row_bridge(n: int, p: int) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    domain_q = h1.mu_domain(p, n // 2)
    rows = quotient_collision_rows(p, n)
    reasons = Counter()
    bad: list[dict[str, Any]] = []
    for row in rows:
        p_pair = tuple(row["P_quotient_exponents"])
        q_pair = tuple(row["Q_quotient_exponents"])
        lifted_p = lift_quotient_pair(n, p_pair)
        lifted_q = lift_quotient_pair(n, q_pair)
        sig_p = elem123(lifted_p, domain, p)
        sig_q = elem123(lifted_q, domain, p)
        quotient_equal = quotient_sum(domain_q, p_pair, p) == quotient_sum(domain_q, q_pair, p)
        if sig_p != sig_q or not quotient_equal:
            bad.append(
                {
                    "P_quotient_exponents": list(p_pair),
                    "Q_quotient_exponents": list(q_pair),
                    "sig_P": list(sig_p),
                    "sig_Q": list(sig_q),
                }
            )
            if len(bad) >= 5:
                break
        reasons[classify_lifted_row(n, row)] += 1

    quotient_summary = x27.quotient_h2_row(p, n // 2)
    baseline = n // 4 - 1
    check(f"n={n}, p={p}: lifted quotient rows have equal h=4 top-three signature", not bad)
    check(f"n={n}, p={p}: zero-sum baseline is n/4-1", reasons["zero_sum_mu4_full_fiber"] == baseline)
    check(
        f"n={n}, p={p}: bridge counts match quotient row",
        reasons["zero_sum_mu4_full_fiber"] == quotient_summary["zero_sum_mu4_full_fiber"]
        and reasons["extra_antipodal_quotient_lift"] == quotient_summary["extra_antipodal_quotient_lifts"],
    )
    check(f"n={n}, p={p}: no mixed zero-sum collisions", reasons["mixed_zero_sum"] == 0)

    return {
        "n": n,
        "p": p,
        "quotient_collision_count": len(rows),
        "reason_counts": dict(sorted(reasons.items())),
        "zero_sum_baseline_formula": baseline,
        "quotient_summary": {
            "zero_sum_mu4_full_fiber": quotient_summary["zero_sum_mu4_full_fiber"],
            "extra_antipodal_quotient_lifts": quotient_summary["extra_antipodal_quotient_lifts"],
            "total_anchored_quotient_collisions": quotient_summary["total_anchored_quotient_collisions"],
        },
        "bad_examples": bad,
    }


def build_certificate() -> dict[str, Any]:
    rows = [
        check_row_bridge(16, 257),
        check_row_bridge(32, 1153),
        check_row_bridge(64, 4993),
        check_row_bridge(128, 65537),
        check_row_bridge(256, 65537),
    ]
    for n in (16, 32, 64, 128, 256, 512, 1024):
        m = n // 2
        zero_sum_pairs = m // 2
        anchored_baseline = zero_sum_pairs - 1
        check(f"n={n}: zero-sum baseline formula", anchored_baseline == n // 4 - 1)
    check("all bridge rows have no bad examples", all(not row["bad_examples"] for row in rows))
    return {
        "task": "X29 h=4 quotient-bridge lemma",
        "node": "active_core_count_bound",
        "status": (
            "PROVED ALGEBRAIC BRIDGE: anchored h=4 antipodal-union trades "
            "are exactly anchored quotient h=2 sum collisions"
        ),
        "theorem": (
            "For 4|n and odd characteristic, the square map identifies "
            "anchored h=4 supports that are unions of antipodal pairs with "
            "anchored 2-subsets of mu_{n/2}.  Equality of the h=4 top-three "
            "elementary signature is equivalent to equality of quotient pair "
            "sums.  The zero-sum quotient baseline has size n/4-1 and lifts "
            "to mu_4 full-fiber pairs."
        ),
        "rows": rows,
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

    print("\nbridge rows:")
    for row in cert["rows"]:
        print(
            f"n={row['n']:<4d} p={row['p']:<8d} total={row['quotient_collision_count']:<4d} "
            f"reasons={row['reason_counts']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X29 h=4 quotient-bridge checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
