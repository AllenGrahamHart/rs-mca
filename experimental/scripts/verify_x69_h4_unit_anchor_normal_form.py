#!/usr/bin/env python3
"""X69 unit-anchor normal form for primitive h=4 norm-gate keys.

For n=2^s, content one means at least one of a,b,c is odd.  The X64 chord
transforms can put an odd exponent into the first coordinate, and X67's
Galois unit scaling then sends that first coordinate to 1.  Thus every X68
primitive certifier key has a representative (1,r,s).

This is a certifier enumeration normal form; row-count expansion remains X65.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import json
import os
import sys
from typing import Any

import verify_x68_h4_norm_gate_certifier_keys as x68
import verify_x64_h4_linear_orbit_compression as x64


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x69-h4-unit-anchor-normal-form",
    "x69_h4_unit_anchor_normal_form.json",
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
        "x64_h4_linear_orbit_compression": "PROVED",
        "x67_h4_galois_norm_gate_compression": "PROVED",
        "x68_h4_norm_gate_certifier_keys": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def normalized_members(n: int, triple: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    return {member for member in x68.certifier_raw_orbit(n, triple) if member[0] % n == 1}


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    reps = x68.replay_primitive_x64_reps(row)
    classes: dict[tuple[int, int, int], list[tuple[int, int, int]]] = defaultdict(list)
    for rep in sorted(reps):
        classes[x68.certifier_key(n, rep)].append(rep)

    missing_normalized: list[dict[str, Any]] = []
    bad_normalized: list[dict[str, Any]] = []
    normalized_counts: list[int] = []
    sample_normalized: list[dict[str, Any]] = []

    for key, row_reps in sorted(classes.items()):
        members = normalized_members(n, key)
        normalized_counts.append(len(members))
        if not members and len(missing_normalized) < 5:
            missing_normalized.append({"key": list(key), "row_reps": [list(rep) for rep in row_reps[:5]]})
        for member in sorted(members):
            if (
                member[0] % n != 1
                or not x64.is_filtered(n, *member)
                or x64.content(n, member) != 1
                or x68.certifier_key(n, member) != key
            ) and len(bad_normalized) < 5:
                bad_normalized.append({"key": list(key), "member": list(member)})
        if len(sample_normalized) < 5:
            sample_normalized.append(
                {
                    "key": list(key),
                    "normalized_members": [list(member) for member in sorted(members)[:5]],
                    "row_representatives": [list(rep) for rep in sorted(row_reps)[:5]],
                }
            )

    check(
        f"{row['label']}: every certifier key has a unit-anchor representative",
        not missing_normalized,
        f"sample_missing={missing_normalized}",
    )
    check(
        f"{row['label']}: normalized representatives are filtered primitive and keyed correctly",
        not bad_normalized,
        f"sample_bad={bad_normalized}",
    )
    check(
        f"{row['label']}: normalized enumeration is at most n^2",
        len(classes) <= (n - 1) * (n - 1),
        f"keys={len(classes)}, pair_budget={(n-1)*(n-1)}",
    )

    hist = Counter(normalized_counts)
    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": int(row["p"]),
        "certifier_key_count": len(classes),
        "normalized_pair_budget": (n - 1) * (n - 1),
        "normalized_member_count_histogram": {str(k): v for k, v in sorted(hist.items())},
        "min_normalized_members_per_key": min(normalized_counts) if normalized_counts else 0,
        "max_normalized_members_per_key": max(normalized_counts) if normalized_counts else 0,
        "sample_normalized_classes": sample_normalized,
        "missing_normalized": missing_normalized,
        "bad_normalized": bad_normalized,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    rows = [row_report(row) for row in x60["rows"]]
    check(
        "all replay keys have normalized representatives",
        all(not row["missing_normalized"] for row in rows),
    )
    check(
        "all normalized representatives remain valid",
        all(not row["bad_normalized"] for row in rows),
    )
    check(
        "the replay exercises nontrivial normalized multiplicity",
        any(row["max_normalized_members_per_key"] > 1 for row in rows),
    )

    return {
        "task": "X69 h=4 unit-anchor normal form",
        "node": "active_core_count_bound",
        "status": "PROVED NORMAL FORM: EVERY PRIMITIVE CERTIFIER KEY HAS A REPRESENTATIVE (1,r,s)",
        "theorem": (
            "For n=2^s, content gcd(n,a,b,c)=1 implies at least one exponent is odd. "
            "The X64 chord transforms can place an odd exponent in the first coordinate; "
            "X67 unit scaling then sends it to 1.  Hence every primitive X68 "
            "norm-gate certifier key has a filtered content-one representative "
            "(1,r,s).  This reduces resultant enumeration to normalized pairs "
            "(r,s), while survivor row mass is still counted using X65."
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

    print("\nunit-anchor normal-form rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: keys={row['certifier_key_count']} "
            f"normalized_hist={row['normalized_member_count_histogram']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X69 h4 unit-anchor normal-form checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
