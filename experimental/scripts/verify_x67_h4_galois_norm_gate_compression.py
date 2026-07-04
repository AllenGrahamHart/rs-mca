#!/usr/bin/env python3
"""X67 Galois compression for h=4 sparse norm gates.

The unit action u in (Z/nZ)^* sends

    f_(a,b,c)(X) = X^a + X^b - X^c - 1

to f_(ua,ub,uc)(X) = f_(a,b,c)(X^u).  This does not preserve the fixed
generator row count.  It does preserve the cyclotomic norm/resultant because
u permutes the primitive n-th roots.

This verifier checks the resulting certifier identity on the primitive
canonical X64 representatives from the existing replay rows.
"""

from __future__ import annotations

import json
import math
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
    "x67-h4-galois-norm-gate-compression",
    "x67_h4_galois_norm_gate_compression.json",
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
        "x62_h4_linear_norm_gate": "PROVED",
        "x64_h4_linear_orbit_compression": "PROVED",
        "x65_h4_linear_orbit_budget": "PROVED",
        "x66_h4_norm_gate_orbit_invariance": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def units_mod(n: int) -> list[int]:
    return [u for u in range(n) if math.gcd(u, n) == 1]


def unit_scale(n: int, triple: tuple[int, int, int], u: int) -> tuple[int, int, int]:
    a, b, c = triple
    return ((u * a) % n, (u * b) % n, (u * c) % n)


def galois_factor_multiset(n: int, triple: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    return sorted(unit_scale(n, triple, v) for v in units_mod(n))


def replay_primitive_canonical_reps(row: dict[str, Any]) -> set[tuple[int, int, int]]:
    n = int(row["n"])
    p = int(row["p"])
    domain = h1.mu_domain(p, n)
    exponent_by_value = {value: exp for exp, value in enumerate(domain)}

    reps: set[tuple[int, int, int]] = set()
    for a, x in enumerate(domain):
        for b, y in enumerate(domain):
            z = (x + y - 1) % p
            c = exponent_by_value.get(z)
            if c is None or not x64.is_filtered(n, a, b, c):
                continue
            triple = (a, b, c)
            if x64.content(n, triple) == 1:
                reps.add(x64.canonical(triple, n))
    return reps


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    units = units_mod(n)
    reps = replay_primitive_canonical_reps(row)

    check(f"{row['label']}: has primitive canonical reps", bool(reps))
    relation_failures: list[dict[str, Any]] = []
    filter_failures: list[dict[str, Any]] = []
    content_failures: list[dict[str, Any]] = []
    nontrivial_unit_examples: list[dict[str, Any]] = []
    unit_orbit_sizes: list[int] = []
    factor_identity_checks = 0

    for rep in sorted(reps):
        base_factors = galois_factor_multiset(n, rep)
        unit_orbit = {unit_scale(n, rep, u) for u in units}
        unit_orbit_sizes.append(len(unit_orbit))
        for u in units:
            scaled = unit_scale(n, rep, u)
            if not x64.is_filtered(n, *scaled) and len(filter_failures) < 5:
                filter_failures.append({"rep": list(rep), "u": u, "scaled": list(scaled)})
            if x64.content(n, scaled) != 1 and len(content_failures) < 5:
                content_failures.append({"rep": list(rep), "u": u, "scaled": list(scaled)})
            scaled_factors = galois_factor_multiset(n, scaled)
            factor_identity_checks += 1
            if scaled_factors != base_factors and len(relation_failures) < 5:
                relation_failures.append({"rep": list(rep), "u": u, "scaled": list(scaled)})
            if scaled != rep and len(nontrivial_unit_examples) < 5:
                nontrivial_unit_examples.append({"rep": list(rep), "u": u, "scaled": list(scaled)})

    check(
        f"{row['label']}: unit scaling preserves X60 filter congruences",
        not filter_failures,
        f"sample_failures={filter_failures}",
    )
    check(
        f"{row['label']}: unit scaling preserves primitive content",
        not content_failures,
        f"sample_failures={content_failures}",
    )
    check(
        f"{row['label']}: Galois factor multisets are invariant",
        not relation_failures,
        f"sample_failures={relation_failures}",
    )
    check(
        f"{row['label']}: primitive raw unit action is free",
        all(size == len(units) for size in unit_orbit_sizes),
        f"unit_count={len(units)}, orbit_sizes={sorted(set(unit_orbit_sizes))}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": int(row["p"]),
        "unit_count": len(units),
        "primitive_canonical_representatives": len(reps),
        "factor_identity_checks": factor_identity_checks,
        "unit_orbit_size_histogram": {
            str(size): unit_orbit_sizes.count(size) for size in sorted(set(unit_orbit_sizes))
        },
        "nontrivial_unit_examples": nontrivial_unit_examples,
        "filter_failures": filter_failures,
        "content_failures": content_failures,
        "factor_identity_failures": relation_failures,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    rows = [row_report(row) for row in x60["rows"]]
    check(
        "all replay rows preserve Galois factor multisets",
        all(not row["factor_identity_failures"] for row in rows),
    )
    check(
        "all replay rows preserve filter and primitive content",
        all(not row["filter_failures"] and not row["content_failures"] for row in rows),
    )
    check(
        "the verifier exercised nontrivial unit relabels",
        sum(len(row["nontrivial_unit_examples"]) for row in rows) > 0,
    )

    return {
        "task": "X67 h=4 Galois norm-gate compression",
        "node": "active_core_count_bound",
        "status": "PROVED CERTIFIER COMPRESSION: UNIT EXPONENT ACTION PRESERVES RESULTANT PRIME SETS",
        "theorem": (
            "For u in (Z/nZ)^*, f_(ua,ub,uc)(X)=f_(a,b,c)(X^u).  The map "
            "zeta -> zeta^u permutes primitive n-th roots, so the cyclotomic "
            "norm and resultant Res(Phi_n,f) are unchanged up to sign.  Unit "
            "scaling also preserves the X60 congruence filters and primitive "
            "content.  This is a sparse-resultant certifier compression, not "
            "a fixed-generator row-count symmetry."
        ),
        "warning": (
            "Do not divide finite-field triple counts by phi(n) from this "
            "lemma.  Unit exponent scaling is a Galois relabeling of primitive "
            "roots for the resultant, not an additive symmetry of the row."
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

    print("\nGalois norm-gate rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: reps={row['primitive_canonical_representatives']} "
            f"units={row['unit_count']} "
            f"factor_checks={row['factor_identity_checks']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X67 h4 Galois norm-gate compression checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
