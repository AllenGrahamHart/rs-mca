#!/usr/bin/env python3
"""U2C-PRIME verifier: boundary fiber test for the X-8 construction.

The original U2-C toy classifier only charged full 2-power cosets with
M > t.  X-8 produced boundary examples at M = t: if n = t R and
S is an antipodal-free zero-sum subset of mu_R, then the preimage of S under
x -> x^t is t-null.  It is a union of mu_t cosets, but it is deliberately not
a union of any larger 2-power cosets when S chooses exactly one point from
each antipodal pair.

This verifier runs the construction at tiny tame rows with q < 2^(R/2), so the
zero-sum patterns are visible by exhaustive enumeration.  It then checks that
the repaired classifier ("some M >= t") charges every hit while the old
classifier ("some M > t") rejects them.
"""

from __future__ import annotations

import json
import os
import sys
from itertools import product
from typing import Any


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "u2c-prime-boundary-fiber-test",
    "u2c_prime_boundary_fiber_test.json",
)

FAILS: list[str] = []
NCHECK = 0


TOYS = [
    {
        "label": "F257_mu128_t4_R32",
        "q": 257,
        "n": 128,
        "t": 4,
    },
    {
        "label": "F257_mu256_t8_R32",
        "q": 257,
        "n": 256,
        "t": 8,
    },
]


def check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    if not cond:
        FAILS.append(name)


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise ValueError(f"no primitive root found for {p}")


def powers_of_two_dividing(n: int) -> list[int]:
    out: list[int] = []
    m = 1
    while m <= n:
        if n % m == 0:
            out.append(m)
        m *= 2
    return out


def is_union_of_mu_m_cosets(block: set[int], n: int, m: int) -> bool:
    """Exponent test for union of fibers of x -> x^m on mu_n."""
    if n % m != 0:
        return False
    stride = n // m
    for residue in range(stride):
        count = sum(1 for j in range(m) if (residue + j * stride) % n in block)
        if count not in (0, m):
            return False
    return True


def classify_boundary_block(block: set[int], n: int, t: int) -> dict[str, Any]:
    old_ms = [m for m in powers_of_two_dividing(n) if m > t]
    repaired_ms = [m for m in powers_of_two_dividing(n) if m >= t]
    old_hits = [m for m in old_ms if is_union_of_mu_m_cosets(block, n, m)]
    repaired_hits = [m for m in repaired_ms if is_union_of_mu_m_cosets(block, n, m)]
    return {
        "old_M_gt_t_hits": old_hits,
        "repaired_M_ge_t_hits": repaired_hits,
        "minimal_repaired_M": min(repaired_hits) if repaired_hits else None,
    }


def quotient_sign_patterns(r: int) -> list[list[int]]:
    """All patterns choosing exactly one exponent from each antipodal pair."""
    half = r // 2
    patterns: list[list[int]] = []
    for bits in product((0, 1), repeat=half):
        patterns.append([i + half * bits[i] for i in range(half)])
    return patterns


def lift_preimage(support_q: list[int], n: int, t: int) -> set[int]:
    r = n // t
    return {a + j * r for a in support_q for j in range(t)}


def power_sums_vanish(block: set[int], zeta: int, q: int, t: int) -> bool:
    return all(sum(pow(zeta, r * e, q) for e in block) % q == 0 for r in range(1, t + 1))


def run_toy(toy: dict[str, int | str]) -> dict[str, Any]:
    label = str(toy["label"])
    q = int(toy["q"])
    n = int(toy["n"])
    t = int(toy["t"])
    r = n // t
    check(f"{label}: q is prime", is_prime(q), f"q={q}")
    check(f"{label}: n divides q-1", (q - 1) % n == 0, f"n={n}, q-1={q - 1}")
    check(f"{label}: t divides n", n % t == 0, f"t={t}")
    check(f"{label}: boundary trigger q < 2^(R/2)", q < (1 << (r // 2)), f"R={r}")
    check(f"{label}: t is a 2-power boundary scale", t in powers_of_two_dividing(n))

    g = primitive_root(q)
    zeta = pow(g, (q - 1) // n, q)
    eta = pow(zeta, t, q)
    check(f"{label}: zeta has exact order n", pow(zeta, n, q) == 1 and pow(zeta, n // 2, q) != 1)
    check(f"{label}: eta has exact quotient order R", pow(eta, r, q) == 1 and pow(eta, r // 2, q) != 1)

    zero_patterns: list[dict[str, Any]] = []
    t_null_failures = 0
    old_classifier_failures = 0
    repaired_classifier_failures = 0
    for support_q in quotient_sign_patterns(r):
        quotient_sum = sum(pow(eta, a, q) for a in support_q) % q
        if quotient_sum != 0:
            continue
        block = lift_preimage(support_q, n, t)
        classification = classify_boundary_block(block, n, t)
        if not power_sums_vanish(block, zeta, q, t):
            t_null_failures += 1
        if classification["old_M_gt_t_hits"] != []:
            old_classifier_failures += 1
        if classification["minimal_repaired_M"] != t:
            repaired_classifier_failures += 1
        zero_patterns.append(
            {
                "quotient_support": support_q,
                "block_weight": len(block),
                "classification": classification,
            }
        )

    check(f"{label}: X-8 boundary zero-sum patterns found", len(zero_patterns) > 0)
    check(f"{label}: all lifted blocks are t-null", t_null_failures == 0, f"failures={t_null_failures}")
    check(
        f"{label}: old M>t classifier rejects every boundary block",
        old_classifier_failures == 0,
        f"failures={old_classifier_failures}",
    )
    check(
        f"{label}: repaired M>=t classifier charges every boundary block at M=t",
        repaired_classifier_failures == 0,
        f"failures={repaired_classifier_failures}",
    )
    check(
        f"{label}: every zero-sum pattern is repaired-charged and old-primitive",
        all(
            pattern["classification"]["old_M_gt_t_hits"] == []
            and pattern["classification"]["minimal_repaired_M"] == t
            for pattern in zero_patterns
        ),
        f"count={len(zero_patterns)}",
    )

    return {
        "label": label,
        "q": q,
        "n": n,
        "t": t,
        "R": r,
        "primitive_root": g,
        "zeta": zeta,
        "eta": eta,
        "threshold_2_to_R_over_2": 1 << (r // 2),
        "enumerated_antipodal_free_patterns": 1 << (r // 2),
        "zero_sum_pattern_count": len(zero_patterns),
        "sample_zero_sum_patterns": zero_patterns[:8],
        "verdict": "old M>t classifier would call these primitive; repaired M>=t classifier charges them at M=t",
    }


def build_certificate() -> dict[str, Any]:
    rows = [run_toy(toy) for toy in TOYS]
    check("U2C-PRIME: all toy rows found boundary witnesses", all(row["zero_sum_pattern_count"] > 0 for row in rows))
    return {
        "task": "U2C-PRIME boundary fiber test",
        "node": "u2c_boundary_scale_column",
        "status": "PASS: X-8 boundary witnesses are exactly old-primitive and repaired-charged in the toy rows",
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

    print("\nsummary:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: q={row['q']} n={row['n']} t={row['t']} R={row['R']} "
            f"zero_sum_patterns={row['zero_sum_pattern_count']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print("  -", name)
        print("\nrecomputed summary:")
        print(json.dumps(cert, indent=2, sort_keys=True))
        return 1
    print(f"\nPASS: {NCHECK} U2C-PRIME boundary fiber-test checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
