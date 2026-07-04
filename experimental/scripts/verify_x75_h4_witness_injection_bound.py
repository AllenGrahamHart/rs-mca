#!/usr/bin/env python3
"""X75 h=4 witness-injection bound.

X74 bounded h=4 primitive norm-gate orbits through X68 keys.  X75 removes that
extra key-to-row loss: a primitive X64 row orbit with a unit-anchor transform
gives a unique interval witness (primitive root, sign, length).  Since the
interval start is forced for each witness, there are at most 2*phi(n)*(n-1)
primitive h=4 canonical row orbits.
"""

from __future__ import annotations

from collections import Counter
import json
import math
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x64_h4_linear_orbit_compression as x64
import verify_x68_h4_norm_gate_certifier_keys as x68
import verify_x71_h4_interval_quotient_form as x71


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x75-h4-witness-injection-bound",
    "x75_h4_witness_injection_bound.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X65_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x65-h4-linear-orbit-budget",
    "x65_h4_linear_orbit_budget.json",
)
X73_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x73-h4-normalized-pair-sieve",
    "x73_h4_normalized_pair_sieve.json",
)
X74_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x74-h4-sieve-orbit-bound",
    "x74_h4_sieve_orbit_bound.json",
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


def by_label(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["label"]: row for row in rows}


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x64_h4_linear_orbit_compression": "PROVED",
        "x65_h4_linear_orbit_budget": "PROVED",
        "x71_h4_interval_quotient_form": "PROVED",
        "x73_h4_normalized_pair_sieve": "PROVED",
        "x74_h4_sieve_orbit_bound": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def normalized_witnesses(n: int, rep: tuple[int, int, int]) -> list[tuple[int, str, int]]:
    witnesses: list[tuple[int, str, int]] = []
    for member in sorted(x64.transforms(n, rep)):
        first = member[0] % n
        if math.gcd(first, n) != 1:
            continue
        inv = pow(first, -1, n)
        normalized = (1, (member[1] * inv) % n, (member[2] * inv) % n)
        _, meta = x71.interval_quotient(normalized)
        if meta["sign"] == "zero":
            continue
        witnesses.append((first, str(meta["sign"]), int(meta["length"])))
    return witnesses


def choose_witness(n: int, rep: tuple[int, int, int]) -> tuple[int, str, int]:
    witnesses = normalized_witnesses(n, rep)
    if not witnesses:
        raise AssertionError(f"no unit-anchor witness for {rep} mod {n}")
    return min(witnesses)


def witness_is_realized(
    n: int,
    p: int,
    domain: list[int],
    rep: tuple[int, int, int],
    witness: tuple[int, str, int],
) -> bool:
    root_exp, sign, length = witness
    for member in x64.transforms(n, rep):
        first = member[0] % n
        if first != root_exp:
            continue
        inv = pow(first, -1, n)
        normalized = (1, (member[1] * inv) % n, (member[2] * inv) % n)
        _, meta = x71.interval_quotient(normalized)
        if (str(meta["sign"]), int(meta["length"])) != (sign, length):
            continue
        _, r, s = normalized
        if (domain[root_exp] + domain[(r * root_exp) % n] - domain[(s * root_exp) % n] - 1) % p == 0:
            return True
    return False


def row_report(row65: dict[str, Any], row74: dict[str, Any]) -> dict[str, Any]:
    label = row65["label"]
    n = int(row65["n"])
    p = int(row65["p"])
    phi = n // 2
    domain = h1.mu_domain(p, n)
    reps = x68.replay_primitive_x64_reps(row65)
    primitive_orbits = int(row65["primitive_canonical_orbit_count"])
    witness_bound = 2 * phi * (n - 1)
    witness_map: dict[tuple[int, str, int], tuple[int, int, int]] = {}
    collisions: list[dict[str, Any]] = []
    bad_realizations: list[dict[str, Any]] = []
    candidate_count_by_rep: Counter[int] = Counter()

    for rep in sorted(reps):
        candidates = normalized_witnesses(n, rep)
        candidate_count_by_rep[len(candidates)] += 1
        witness = min(candidates)
        if witness in witness_map and len(collisions) < 5:
            collisions.append(
                {
                    "witness": [witness[0], witness[1], witness[2]],
                    "first_rep": list(witness_map[witness]),
                    "second_rep": list(rep),
                }
            )
        witness_map[witness] = rep
        if not witness_is_realized(n, p, domain, rep, witness) and len(bad_realizations) < 5:
            bad_realizations.append({"rep": list(rep), "witness": [witness[0], witness[1], witness[2]]})

    check(
        f"{label}: replay primitive reps match X65",
        len(reps) == primitive_orbits,
        f"reps={len(reps)}, X65={primitive_orbits}",
    )
    check(
        f"{label}: every primitive orbit has a realized interval witness",
        not bad_realizations,
        f"sample_bad={bad_realizations}",
    )
    check(
        f"{label}: chosen interval witnesses are injective on primitive orbits",
        not collisions and len(witness_map) == len(reps),
        f"collisions={collisions[:3]}, witnesses={len(witness_map)}, reps={len(reps)}",
    )
    check(
        f"{label}: primitive orbit count obeys witness bound",
        primitive_orbits <= witness_bound,
        f"orbits={primitive_orbits}, bound={witness_bound}",
    )
    check(
        f"{label}: witness bound is below n^2",
        witness_bound < n**2,
        f"bound={witness_bound}, n^2={n**2}",
    )
    check(
        f"{label}: witness bound improves X74 uniform bound",
        witness_bound <= int(row74["uniform_orbit_bound"]),
        f"witness={witness_bound}, X74={row74['uniform_orbit_bound']}",
    )

    return {
        "label": label,
        "kind": row65["kind"],
        "n": n,
        "p": p,
        "phi_n": phi,
        "primitive_canonical_orbit_count": primitive_orbits,
        "chosen_witness_count": len(witness_map),
        "witness_bound_2_phi_n_minus_1": witness_bound,
        "n_squared_bound": n**2,
        "n_cubed_bound": n**3,
        "candidate_witness_count_histogram_per_orbit": {
            str(k): v for k, v in sorted(candidate_count_by_rep.items())
        },
        "sample_witnesses": [
            {"witness": [w[0], w[1], w[2]], "rep": list(rep)}
            for w, rep in sorted(witness_map.items())[:5]
        ],
        "collision_examples": collisions,
        "bad_realizations": bad_realizations,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x65 = load_json(X65_CERT)
    x73 = load_json(X73_CERT)
    x74 = load_json(X74_CERT)
    check("X65 certificate has replay rows", bool(x65.get("rows")))
    check("X73 certificate has replay rows", bool(x73.get("rows")))
    check("X74 certificate has replay rows", bool(x74.get("rows")))
    x74_rows = by_label(x74["rows"])
    rows = []
    for row65 in x65["rows"]:
        label = row65["label"]
        check(f"{label}: X74 row exists", label in x74_rows)
        rows.append(row_report(row65, x74_rows[label]))

    check(
        "all replay rows have injective h4 interval witnesses",
        all(not row["collision_examples"] for row in rows),
    )
    check(
        "all replay rows satisfy the O(n^2) h4 witness bound",
        all(row["primitive_canonical_orbit_count"] <= row["witness_bound_2_phi_n_minus_1"] for row in rows),
    )
    check(
        "all h4 witness bounds are below n^2",
        all(row["witness_bound_2_phi_n_minus_1"] < row["n_squared_bound"] for row in rows),
    )

    return {
        "task": "X75 h=4 witness-injection bound",
        "node": "active_core_count_bound",
        "status": "PROVED H4 STRENGTHENING: PRIMITIVE CANONICAL ORBITS INJECT INTO O(n^2) INTERVAL WITNESSES",
        "theorem": (
            "Every primitive h=4 X64 canonical row orbit has an X64 transform "
            "with odd first exponent d.  Scaling that transform by d^{-1} gives "
            "a normalized interval word which vanishes at the primitive root "
            "zeta^d.  For fixed d, interval sign, and interval length, X71's "
            "geometric-series equation forces the interval start if it exists. "
            "Choosing the lexicographically first such witness gives an "
            "injection from primitive canonical row orbits into at most "
            "2*phi(n)*(n-1)=n(n-1)<n^2 witnesses."
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

    print("\nh4 witness-bound rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: orbits={row['primitive_canonical_orbit_count']} "
            f"witness_bound={row['witness_bound_2_phi_n_minus_1']} "
            f"n^2={row['n_squared_bound']}"
        )

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X75 h4 witness-injection bound checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
