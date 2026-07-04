#!/usr/bin/env python3
"""X45 h=4 common-gcd orbit compression.

X33 gives the h=4 common-gcd certifier.  This packet proves that the
certifier is invariant under the natural affine exponent symmetries:

    a -> u a + d,       u in (Z/nZ)^*, d in Z/nZ,

and under swapping the positive and negative sides.  Hence a row certifier for
the h=4 top-level branch may check one canonical affine-orbit representative.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
import math
import os
import sys
from typing import Any, Iterable

import verify_x30_finite_p_norm_gate as x30
import verify_x33_h4_common_gcd_gate as x33


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x45-h4-common-gcd-orbit-compression",
    "x45_h4_common_gcd_orbit_compression.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

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


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def units_mod(n: int) -> list[int]:
    return [u for u in range(n) if math.gcd(u, n) == 1]


def transform_set(support: tuple[int, ...], n: int, unit: int, shift: int) -> tuple[int, ...]:
    return tuple(sorted(((unit * value + shift) % n) for value in support))


def transform_pair(
    p_set: tuple[int, ...],
    q_set: tuple[int, ...],
    n: int,
    unit: int,
    shift: int,
    swap: bool = False,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    left = transform_set(p_set, n, unit, shift)
    right = transform_set(q_set, n, unit, shift)
    return (right, left) if swap else (left, right)


def canonical_pair(p_set: tuple[int, ...], q_set: tuple[int, ...], n: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Canonical representative for affine exponent symmetries and side swap.

    A lexicographically minimal affine translate has 0 in the union.  It is
    therefore enough to translate one of the eight support elements to 0 after
    each unit dilation.
    """

    best: tuple[tuple[int, ...], tuple[int, ...]] | None = None
    anchors = p_set + q_set
    for unit in units_mod(n):
        for anchor in anchors:
            shift = (-unit * anchor) % n
            for swap in (False, True):
                candidate = transform_pair(p_set, q_set, n, unit, shift, swap)
                if best is None or candidate < best:
                    best = candidate
    assert best is not None
    return best


def common_degree(n: int, p: int, p_set: tuple[int, ...], q_set: tuple[int, ...]) -> int:
    return x33.common_h4_gcd_degree(n, p, tuple(sorted(p_set)), tuple(sorted(q_set)))


def anchored_ordered_pairs(n: int) -> Iterable[tuple[tuple[int, ...], tuple[int, ...]]]:
    indices = tuple(range(n))
    for tail in combinations(range(1, n), 3):
        p_set = (0,) + tail
        remaining = tuple(i for i in indices if i not in p_set)
        for q_set in combinations(remaining, 4):
            yield p_set, q_set


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x33_h4_common_gcd_gate": "PROVED",
        "x35_h4_power_sum_gate": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def check_symbolic_identities() -> dict[str, Any]:
    n = 32
    modulus = 1_000_003
    p_set = (0, 1, 2, 17)
    q_set = (3, 8, 19, 21)
    shift = 5
    unit = 7

    translated_ok = True
    dilated_ok = True
    for r in (1, 2, 3):
        base = x33.elementary_diff_poly(n, p_set, q_set, r, modulus)
        translated = x33.elementary_diff_poly(
            n,
            transform_set(p_set, n, 1, shift),
            transform_set(q_set, n, 1, shift),
            r,
            modulus,
        )
        expected_translated = [0] * n
        for exponent, coeff in enumerate(base):
            expected_translated[(exponent + r * shift) % n] = (
                expected_translated[(exponent + r * shift) % n] + coeff
            ) % modulus
        translated_ok &= translated == x33.trim(expected_translated)

        dilated = x33.elementary_diff_poly(
            n,
            transform_set(p_set, n, unit, 0),
            transform_set(q_set, n, unit, 0),
            r,
            modulus,
        )
        expected_dilated = [0] * n
        for exponent, coeff in enumerate(base):
            expected_dilated[(unit * exponent) % n] = (
                expected_dilated[(unit * exponent) % n] + coeff
            ) % modulus
        dilated_ok &= dilated == x33.trim(expected_dilated)

    check("translation identity E_r(P+d,Q+d)=X^(rd) E_r(P,Q)", translated_ok)
    check("unit identity E_r(uP,uQ)=E_r(P,Q)(X^u)", dilated_ok)
    return {
        "n": n,
        "P": list(p_set),
        "Q": list(q_set),
        "shift": shift,
        "unit": unit,
        "translation_identity": translated_ok,
        "unit_identity": dilated_ok,
    }


def check_invariance_examples() -> list[dict[str, Any]]:
    examples = [
        (16, 257, (0, 4, 8, 12), (1, 5, 9, 13)),
        (16, 257, (0, 1, 2, 9), (3, 4, 7, 12)),
        (32, 4993, (0, 8, 16, 24), (1, 9, 17, 25)),
        (32, 4993, (0, 1, 2, 17), (3, 8, 19, 21)),
    ]
    rows: list[dict[str, Any]] = []
    for n, p, p_set, q_set in examples:
        base = common_degree(n, p, p_set, q_set)
        transformed_degrees = []
        for unit in units_mod(n)[: min(6, len(units_mod(n)))]:
            for shift in (0, 1, 3, n // 2 - 1):
                for swap in (False, True):
                    left, right = transform_pair(p_set, q_set, n, unit, shift, swap)
                    transformed_degrees.append(common_degree(n, p, left, right))
        key = canonical_pair(p_set, q_set, n)
        key_degree = common_degree(n, p, *key)
        invariant = all(degree == base for degree in transformed_degrees) and key_degree == base
        check(f"n={n}, p={p}, P={p_set}: affine orbit preserves gcd degree", invariant)
        rows.append(
            {
                "n": n,
                "p": p,
                "P": list(p_set),
                "Q": list(q_set),
                "base_degree": base,
                "canonical_P": list(key[0]),
                "canonical_Q": list(key[1]),
                "canonical_degree": key_degree,
                "checked_transforms": len(transformed_degrees),
            }
        )
    return rows


def full_n16_orbit_report() -> dict[str, Any]:
    n = 16
    p = 257
    orbit_sizes: Counter[tuple[tuple[int, ...], tuple[int, ...]]] = Counter()
    orbit_degrees: dict[tuple[tuple[int, ...], tuple[int, ...]], int] = {}
    degree_hist = Counter()
    inconsistent: list[dict[str, Any]] = []
    positive_non_descended: list[dict[str, Any]] = []

    total = 0
    for p_set, q_set in anchored_ordered_pairs(n):
        total += 1
        key = canonical_pair(p_set, q_set, n)
        degree = common_degree(n, p, p_set, q_set)
        orbit_sizes[key] += 1
        if key in orbit_degrees and orbit_degrees[key] != degree and len(inconsistent) < 5:
            inconsistent.append(
                {
                    "canonical_P": list(key[0]),
                    "canonical_Q": list(key[1]),
                    "first_degree": orbit_degrees[key],
                    "new_degree": degree,
                    "P": list(p_set),
                    "Q": list(q_set),
                }
            )
        orbit_degrees.setdefault(key, degree)

    for key, degree in orbit_degrees.items():
        degree_hist[degree] += 1
        if degree > 0 and not x30.divisible_by_phi_power_two(x30.coeff_word(n, key[0], key[1])):
            positive_non_descended.append(
                {
                    "canonical_P": list(key[0]),
                    "canonical_Q": list(key[1]),
                    "degree": degree,
                }
            )

    check("n=16 anchored ordered pair count is complete", total == math.comb(15, 3) * math.comb(12, 4), str(total))
    check("n=16 canonical orbit grouping preserves gcd degree", not inconsistent)
    check("n=16 positive-degree orbits are descended/paid", not positive_non_descended)
    check("n=16 affine compression is nontrivial", len(orbit_sizes) * 10 < total, f"{total}->{len(orbit_sizes)}")

    size_hist = Counter(orbit_sizes.values())
    return {
        "n": n,
        "p": p,
        "anchored_ordered_pairs": total,
        "canonical_orbits": len(orbit_sizes),
        "compression_factor": total / len(orbit_sizes),
        "orbit_size_histogram": {str(k): v for k, v in sorted(size_hist.items())},
        "degree_histogram_by_orbit": {str(k): v for k, v in sorted(degree_hist.items())},
        "positive_non_descended_examples": positive_non_descended[:5],
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    identities = check_symbolic_identities()
    examples = check_invariance_examples()
    n16 = full_n16_orbit_report()
    return {
        "task": "X45 h=4 common-gcd orbit compression",
        "node": "active_core_count_bound",
        "status": "PROVED ORBIT COMPRESSION FOR THE H4 COMMON-GCD CERTIFIER",
        "theorem": (
            "For n=2^s and p == 1 mod n, the degree of "
            "gcd(Phi_n,E1,E2,E3) for an h=4 signed exponent pattern is "
            "invariant under common translation, odd-unit dilation, and side "
            "swap.  Translation multiplies E_r by X^(rd), which is coprime to "
            "Phi_n; unit dilation composes E_r with X^u and permutes primitive "
            "n-th roots; swapping sides multiplies E_r by -1.  Thus a row "
            "certifier may check one canonical affine-orbit representative."
        ),
        "dependency_statuses": deps,
        "symbolic_identities": identities,
        "invariance_examples": examples,
        "n16_full_orbit_report": n16,
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
        expected = load_json(CERT)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    report = cert["n16_full_orbit_report"]
    print("\nn=16 orbit compression:")
    print(
        f"anchored ordered pairs={report['anchored_ordered_pairs']} "
        f"canonical_orbits={report['canonical_orbits']} "
        f"factor={report['compression_factor']:.2f}"
    )
    print(f"degree histogram by orbit={report['degree_histogram_by_orbit']}")

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X45 h4 orbit-compression checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
