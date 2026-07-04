#!/usr/bin/env python3
"""X64 eightfold orbit compression for X60/X63 linear triples.

The X60 equation is x+y=z+1.  It is an equality of two unordered pairs with
the same sum:

    {x,y}  and  {z,1}.

Swapping inside either pair, swapping the two pairs, and re-anchoring the
chosen fourth point at 1 gives an eight-element symmetry group on filtered
triples.  The X60 exclusions make the action free.  Content is invariant, so
the X63 primitive residue can be certified on canonical eight-orbit
representatives.
"""

from __future__ import annotations

from collections import Counter
import json
import math
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x64-h4-linear-orbit-compression",
    "x64_h4_linear_orbit_compression.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X60_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x60-h4-linear-triple-form",
    "x60_h4_linear_triple_form.json",
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


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x60_h4_linear_triple_form": "PROVED",
        "x63_h4_linear_content_descent": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def is_filtered(n: int, a: int, b: int, c: int) -> bool:
    return not (
        a % n == 0
        or b % n == 0
        or c % n == 0
        or b % n == a % n
        or b % n == (a + n // 2) % n
    )


def content(n: int, triple: tuple[int, int, int]) -> int:
    a, b, c = triple
    return math.gcd(math.gcd(math.gcd(n, a), b), c)


def transforms(n: int, triple: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    """The eight re-anchored pair-sum symmetries in exponent coordinates."""
    a, b, c = triple
    return {
        (a % n, b % n, c % n),
        (b % n, a % n, c % n),
        ((a - c) % n, (b - c) % n, (-c) % n),
        ((b - c) % n, (a - c) % n, (-c) % n),
        ((c - a) % n, (-a) % n, (b - a) % n),
        ((-a) % n, (c - a) % n, (b - a) % n),
        ((c - b) % n, (-b) % n, (a - b) % n),
        ((-b) % n, (c - b) % n, (a - b) % n),
    }


def canonical(triple: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    return min(transforms(n, triple))


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    p = int(row["p"])
    domain = h1.mu_domain(p, n)
    exponent_by_value = {value: exp for exp, value in enumerate(domain)}

    triples: set[tuple[int, int, int]] = set()
    for a, x in enumerate(domain):
        for b, y in enumerate(domain):
            z = (x + y - 1) % p
            c = exponent_by_value.get(z)
            if c is not None and is_filtered(n, a, b, c):
                triples.add((a, b, c))

    expected = int(row["filtered_linear_triple_count"])
    check(
        f"{row['label']}: replayed filtered triples match X60",
        len(triples) == expected,
        f"computed={len(triples)}, expected={expected}",
    )

    orbit_reps: set[tuple[int, int, int]] = set()
    primitive_orbit_reps: set[tuple[int, int, int]] = set()
    content_histogram: Counter[int] = Counter()
    orbit_size_histogram: Counter[int] = Counter()
    primitive_orbit_size_histogram: Counter[int] = Counter()
    closure_failures = 0
    content_failures = 0
    nonfree_examples: list[dict[str, Any]] = []

    for triple in sorted(triples):
        orbit = transforms(n, triple)
        if not orbit <= triples:
            closure_failures += 1
        d = content(n, triple)
        if any(content(n, member) != d for member in orbit):
            content_failures += 1
        if len(orbit) != 8 and len(nonfree_examples) < 5:
            nonfree_examples.append({"triple": list(triple), "orbit_size": len(orbit)})
        orbit_size_histogram[len(orbit)] += 1
        content_histogram[d] += 1
        rep = canonical(triple, n)
        orbit_reps.add(rep)
        if d == 1:
            primitive_orbit_reps.add(rep)
            primitive_orbit_size_histogram[len(orbit)] += 1

    primitive_count = sum(count for d, count in content_histogram.items() if d == 1)

    check(
        f"{row['label']}: eight symmetries preserve filtered triples",
        closure_failures == 0,
        f"closure_failures={closure_failures}",
    )
    check(
        f"{row['label']}: content is invariant on eight-orbits",
        content_failures == 0,
        f"content_failures={content_failures}",
    )
    check(
        f"{row['label']}: filtered action is free of size 8",
        not nonfree_examples and set(orbit_size_histogram) == {8},
        f"orbit_sizes={dict(orbit_size_histogram)}",
    )
    check(
        f"{row['label']}: canonical orbit count is filtered/8",
        8 * len(orbit_reps) == len(triples),
        f"orbits={len(orbit_reps)}, triples={len(triples)}",
    )
    check(
        f"{row['label']}: primitive canonical orbit count is primitive/8",
        8 * len(primitive_orbit_reps) == primitive_count,
        f"primitive_orbits={len(primitive_orbit_reps)}, primitive={primitive_count}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "filtered_linear_triple_count": len(triples),
        "canonical_orbit_count": len(orbit_reps),
        "primitive_content_one_count": primitive_count,
        "primitive_canonical_orbit_count": len(primitive_orbit_reps),
        "quotient_descended_count": len(triples) - primitive_count,
        "content_histogram": {str(k): v for k, v in sorted(content_histogram.items())},
        "orbit_size_histogram": {str(k): v for k, v in sorted(orbit_size_histogram.items())},
        "primitive_orbit_size_histogram": {
            str(k): v for k, v in sorted(primitive_orbit_size_histogram.items())
        },
        "sample_canonical_orbits": [list(rep) for rep in sorted(primitive_orbit_reps)[:5]],
        "nonfree_examples": nonfree_examples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    rows = [row_report(row) for row in x60["rows"]]
    check(
        "all replay rows have free eightfold filtered orbits",
        all(row["orbit_size_histogram"] == {"8": row["filtered_linear_triple_count"]} for row in rows),
    )
    check(
        "all primitive replay rows compress by exactly eight",
        all(
            8 * row["primitive_canonical_orbit_count"] == row["primitive_content_one_count"]
            for row in rows
        ),
    )
    return {
        "task": "X64 h=4 linear orbit compression",
        "node": "active_core_count_bound",
        "status": "PROVED ORBIT COMPRESSION: FILTERED LINEAR TRIPLES HAVE FREE EIGHTFOLD SYMMETRY",
        "theorem": (
            "The equation x+y=z+1 is an equality of unordered pairs {x,y} "
            "and {z,1}.  Swapping within pairs, swapping the two pairs, and "
            "renormalizing the chosen anchor to 1 gives eight exponent "
            "transforms.  The X60 filtered exclusions make the four points "
            "distinct and avoid the zero-sum stabilizer, so every filtered "
            "triple has orbit size 8.  The transforms are generated by "
            "subtracting one of a,b,c,0 and permuting roles, hence "
            "gcd(n,a,b,c) is invariant.  The X63 primitive residue can "
            "therefore be certified on canonical eight-orbit representatives."
        ),
        "dependency_statuses": deps,
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
        expected = load_json(CERT)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    print("\norbit rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: triples={row['filtered_linear_triple_count']} "
            f"orbits={row['canonical_orbit_count']} "
            f"primitive_orbits={row['primitive_canonical_orbit_count']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X64 h4 linear orbit-compression checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
