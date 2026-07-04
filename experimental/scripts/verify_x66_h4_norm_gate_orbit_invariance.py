#!/usr/bin/env python3
"""X66 h=4 norm-gate orbit invariance.

X64 gives eight chord-pair transforms of a filtered triple (a,b,c).  This
verifier records the stronger algebraic fact needed by a sparse-resultant
certifier: each transformed word

    X^a + X^b - X^c - 1

is a signed monomial multiple of the original word in the group ring
Z[C_n].  Hence the primitive-root zero condition, and the set of prime
divisors of the cyclotomic norm/resultant, is invariant on X64 orbits.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x64_h4_linear_orbit_compression as x64


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x66-h4-norm-gate-orbit-invariance",
    "x66_h4_norm_gate_orbit_invariance.json",
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
        "x62_h4_linear_norm_gate": "PROVED",
        "x64_h4_linear_orbit_compression": "PROVED",
        "x65_h4_linear_orbit_budget": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def word(n: int, triple: tuple[int, int, int]) -> tuple[int, ...]:
    a, b, c = triple
    coeffs = [0] * n
    coeffs[a % n] += 1
    coeffs[b % n] += 1
    coeffs[c % n] -= 1
    coeffs[0] -= 1
    return tuple(coeffs)


def signed_shift(n: int, coeffs: tuple[int, ...], sign: int, shift: int) -> tuple[int, ...]:
    out = [0] * n
    for exp, coeff in enumerate(coeffs):
        out[(exp + shift) % n] += sign * coeff
    return tuple(out)


def transforms_with_units(
    n: int, triple: tuple[int, int, int]
) -> list[dict[str, Any]]:
    a, b, c = triple
    return [
        {
            "name": "positive_pair_identity",
            "triple": (a % n, b % n, c % n),
            "sign": 1,
            "shift": 0,
        },
        {
            "name": "positive_pair_swap",
            "triple": (b % n, a % n, c % n),
            "sign": 1,
            "shift": 0,
        },
        {
            "name": "negative_pair_reanchor_z",
            "triple": ((a - c) % n, (b - c) % n, (-c) % n),
            "sign": 1,
            "shift": (-c) % n,
        },
        {
            "name": "negative_pair_reanchor_z_after_swap",
            "triple": ((b - c) % n, (a - c) % n, (-c) % n),
            "sign": 1,
            "shift": (-c) % n,
        },
        {
            "name": "side_swap_reanchor_x",
            "triple": ((c - a) % n, (-a) % n, (b - a) % n),
            "sign": -1,
            "shift": (-a) % n,
        },
        {
            "name": "side_swap_reanchor_x_after_swap",
            "triple": ((-a) % n, (c - a) % n, (b - a) % n),
            "sign": -1,
            "shift": (-a) % n,
        },
        {
            "name": "side_swap_reanchor_y",
            "triple": ((c - b) % n, (-b) % n, (a - b) % n),
            "sign": -1,
            "shift": (-b) % n,
        },
        {
            "name": "side_swap_reanchor_y_after_swap",
            "triple": ((-b) % n, (c - b) % n, (a - b) % n),
            "sign": -1,
            "shift": (-b) % n,
        },
    ]


def replay_triples(row: dict[str, Any]) -> set[tuple[int, int, int]]:
    n = int(row["n"])
    p = int(row["p"])
    domain = h1.mu_domain(p, n)
    exponent_by_value = {value: exp for exp, value in enumerate(domain)}

    triples: set[tuple[int, int, int]] = set()
    for a, x in enumerate(domain):
        for b, y in enumerate(domain):
            z = (x + y - 1) % p
            c = exponent_by_value.get(z)
            if c is not None and x64.is_filtered(n, a, b, c):
                triples.add((a, b, c))
    return triples


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    triples = replay_triples(row)
    expected = int(row["filtered_linear_triple_count"])
    check(
        f"{row['label']}: replayed filtered triples match X60",
        len(triples) == expected,
        f"computed={len(triples)}, expected={expected}",
    )

    relation_failures: list[dict[str, Any]] = []
    orbit_mismatch = 0
    action_names: set[str] = set()
    unit_histogram: dict[str, int] = {}
    primitive_relation_checks = 0

    for triple in sorted(triples):
        base_word = word(n, triple)
        unit_transforms = transforms_with_units(n, triple)
        action_names.update(transform["name"] for transform in unit_transforms)
        if {item["triple"] for item in unit_transforms} != x64.transforms(n, triple):
            orbit_mismatch += 1
        for item in unit_transforms:
            transformed_word = word(n, item["triple"])
            shifted_word = signed_shift(n, base_word, int(item["sign"]), int(item["shift"]))
            if transformed_word != shifted_word and len(relation_failures) < 5:
                relation_failures.append(
                    {
                        "triple": list(triple),
                        "transform": item["name"],
                        "target": list(item["triple"]),
                        "sign": item["sign"],
                        "shift": item["shift"],
                    }
                )
            key = f"sign={item['sign']},shift_source={item['name'].split('_')[-1]}"
            unit_histogram[key] = unit_histogram.get(key, 0) + 1
        if x64.content(n, triple) == 1:
            primitive_relation_checks += len(unit_transforms)

    check(
        f"{row['label']}: unit transforms match X64 orbit transforms",
        orbit_mismatch == 0,
        f"orbit_mismatch={orbit_mismatch}",
    )
    check(
        f"{row['label']}: every transform is a signed monomial multiple",
        not relation_failures,
        f"sample_failures={relation_failures}",
    )
    check(
        f"{row['label']}: all eight action names are present",
        len(action_names) == 8,
        ",".join(sorted(action_names)),
    )

    primitive_orbits = len({x64.canonical(triple, n) for triple in triples if x64.content(n, triple) == 1})

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": int(row["p"]),
        "filtered_linear_triple_count": len(triples),
        "primitive_canonical_orbit_count": primitive_orbits,
        "signed_monomial_relation_failures": relation_failures,
        "orbit_mismatch_count": orbit_mismatch,
        "primitive_relation_checks": primitive_relation_checks,
        "unit_action_count": 8,
        "unit_histogram": dict(sorted(unit_histogram.items())),
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    rows = [row_report(row) for row in x60["rows"]]
    check(
        "all replay rows have signed-monomial orbit invariance",
        all(not row["signed_monomial_relation_failures"] for row in rows),
    )
    check(
        "all replay rows match X64 orbit transforms",
        all(row["orbit_mismatch_count"] == 0 for row in rows),
    )
    check(
        "some primitive orbit checks were exercised",
        sum(row["primitive_relation_checks"] for row in rows) > 0,
    )

    return {
        "task": "X66 h=4 norm-gate orbit invariance",
        "node": "active_core_count_bound",
        "status": "PROVED ORBIT INVARIANCE: NORM-GATE PRIME SET IS CONSTANT ON X64 ORBITS",
        "theorem": (
            "For each of the eight X64 transforms, the transformed four-term "
            "word X^a+X^b-X^c-1 is equal in Z[C_n] to +/- X^m times the "
            "original word, with m in {0,-a,-b,-c}.  Therefore evaluation at "
            "any primitive n-th root is multiplied by a unit, and the "
            "cyclotomic norm/resultant prime divisibility test is invariant "
            "on each canonical orbit."
        ),
        "dependency_statuses": deps,
        "unit_identities": [
            {"transform": "positive_pair_identity", "unit": "+1"},
            {"transform": "positive_pair_swap", "unit": "+1"},
            {"transform": "negative_pair_reanchor_z", "unit": "+X^{-c}"},
            {"transform": "negative_pair_reanchor_z_after_swap", "unit": "+X^{-c}"},
            {"transform": "side_swap_reanchor_x", "unit": "-X^{-a}"},
            {"transform": "side_swap_reanchor_x_after_swap", "unit": "-X^{-a}"},
            {"transform": "side_swap_reanchor_y", "unit": "-X^{-b}"},
            {"transform": "side_swap_reanchor_y_after_swap", "unit": "-X^{-b}"},
        ],
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

    print("\nnorm-gate orbit-invariance rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: triples={row['filtered_linear_triple_count']} "
            f"primitive_orbits={row['primitive_canonical_orbit_count']} "
            f"primitive_relation_checks={row['primitive_relation_checks']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X66 h4 norm-gate orbit-invariance checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
