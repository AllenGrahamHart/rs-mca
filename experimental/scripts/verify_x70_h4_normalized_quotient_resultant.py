#!/usr/bin/env python3
"""X70 quotient-resultant reduction for normalized h=4 norm gates.

After X69, primitive h=4 certifier keys have normalized representatives

    f_{r,s}(X) = X + X^r - X^s - 1.

Every such word has the universal factor X-1.  For 2-power n and odd row
characteristic, Res(Phi_n, X-1) has no row-prime divisor, so the sparse
norm-gate certifier can test the quotient f_{r,s}/(X-1).
"""

from __future__ import annotations

from collections import Counter, defaultdict
import json
import os
import sys
from typing import Any

import verify_x68_h4_norm_gate_certifier_keys as x68
import verify_x69_h4_unit_anchor_normal_form as x69


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x70-h4-normalized-quotient-resultant",
    "x70_h4_normalized_quotient_resultant.json",
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
        "x68_h4_norm_gate_certifier_keys": "PROVED",
        "x69_h4_unit_anchor_normal_form": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def normalized_poly(n: int, member: tuple[int, int, int]) -> list[int]:
    a, r, s = member
    assert a % n == 1
    coeffs = [0] * n
    coeffs[1] += 1
    coeffs[r % n] += 1
    coeffs[s % n] -= 1
    coeffs[0] -= 1
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def divide_by_x_minus_one(coeffs: list[int]) -> tuple[list[int], int]:
    """Return q, rem with P=(X-1)q+rem for coeffs in ascending order."""
    if not coeffs:
        return [], 0
    if len(coeffs) == 1:
        return [], coeffs[0]
    degree = len(coeffs) - 1
    q = [0] * degree
    q[degree - 1] = coeffs[degree]
    for k in range(degree - 1, 0, -1):
        q[k - 1] = coeffs[k] + q[k]
    rem = coeffs[0] + q[0]
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q, rem


def multiply_x_minus_one(q: list[int], rem: int = 0) -> list[int]:
    if not q:
        return [rem]
    out = [0] * (len(q) + 1)
    for i, coeff in enumerate(q):
        out[i] -= coeff
        out[i + 1] += coeff
    out[0] += rem
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_weight(coeffs: list[int]) -> int:
    return sum(1 for coeff in coeffs if coeff)


def quotient_l1(coeffs: list[int]) -> int:
    return sum(abs(coeff) for coeff in coeffs)


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    p = int(row["p"])
    reps = x68.replay_primitive_x64_reps(row)
    classes: dict[tuple[int, int, int], list[tuple[int, int, int]]] = defaultdict(list)
    for rep in sorted(reps):
        classes[x68.certifier_key(n, rep)].append(rep)

    identity_failures: list[dict[str, Any]] = []
    diagonal_quotients: list[dict[str, Any]] = []
    quotient_weights: Counter[int] = Counter()
    quotient_l1_norms: Counter[int] = Counter()
    normalized_member_count = 0
    sample_quotients: list[dict[str, Any]] = []

    for key in sorted(classes):
        for member in sorted(x69.normalized_members(n, key)):
            normalized_member_count += 1
            coeffs = normalized_poly(n, member)
            q, rem = divide_by_x_minus_one(coeffs)
            reconstructed = multiply_x_minus_one(q, rem)
            if rem != 0 or reconstructed != coeffs:
                if len(identity_failures) < 5:
                    identity_failures.append(
                        {
                            "key": list(key),
                            "member": list(member),
                            "coeffs": coeffs,
                            "quotient": q,
                            "reconstructed": reconstructed,
                            "remainder": rem,
                        }
                    )
            if member[1] == member[2] and len(diagonal_quotients) < 5:
                diagonal_quotients.append({"key": list(key), "member": list(member), "quotient": q})
            quotient_weights[poly_weight(q)] += 1
            quotient_l1_norms[quotient_l1(q)] += 1
            if len(sample_quotients) < 5:
                sample_quotients.append(
                    {
                        "key": list(key),
                        "member": list(member),
                        "quotient_degree": len(q) - 1 if q else -1,
                        "quotient_weight": poly_weight(q),
                        "quotient_l1": quotient_l1(q),
                        "quotient_prefix": q[:12],
                    }
                )

    phi_n_at_one = 2
    check(f"{row['label']}: row characteristic is odd", p % 2 == 1, f"p={p}")
    check(
        f"{row['label']}: removed X-1 resultant factor is prime-safe",
        p % phi_n_at_one != 0,
        f"p={p}, Phi_n(1)={phi_n_at_one}",
    )
    check(
        f"{row['label']}: every normalized word divides by X-1",
        not identity_failures,
        f"sample_failures={identity_failures}",
    )
    check(
        f"{row['label']}: replay has no diagonal quotient-only keys",
        not diagonal_quotients,
        f"sample_diagonal={diagonal_quotients}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "certifier_key_count": len(classes),
        "normalized_member_count": normalized_member_count,
        "removed_factor": "X-1",
        "removed_resultant_abs": phi_n_at_one,
        "quotient_identity_failures": identity_failures,
        "diagonal_quotient_examples": diagonal_quotients,
        "quotient_weight_histogram": {str(k): v for k, v in sorted(quotient_weights.items())},
        "quotient_l1_histogram": {str(k): v for k, v in sorted(quotient_l1_norms.items())},
        "sample_quotients": sample_quotients,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    rows = [row_report(row) for row in x60["rows"]]
    check(
        "all replay normalized words divide exactly by X-1",
        all(not row["quotient_identity_failures"] for row in rows),
    )
    check(
        "all replay rows have odd characteristic prime-safe removed factor",
        all(row["p"] % row["removed_resultant_abs"] != 0 for row in rows),
    )
    check(
        "some quotient has nontrivial length",
        any(any(int(weight) > 2 for weight in row["quotient_weight_histogram"]) for row in rows),
    )

    return {
        "task": "X70 h=4 normalized quotient-resultant reduction",
        "node": "active_core_count_bound",
        "status": "PROVED CERTIFIER REDUCTION: NORMALIZED WORDS FACTOR BY X-1 WITH ONLY A 2-FACTOR RESULTANT",
        "theorem": (
            "For every X69 normalized word f_{r,s}=X+X^r-X^s-1, f_{r,s}(1)=0, "
            "so f_{r,s}=(X-1)q_{r,s} in Z[X].  For 2-power n, Phi_n(1)=2, "
            "hence Res(Phi_n,f_{r,s})=+/-2*Res(Phi_n,q_{r,s}).  Since row "
            "characteristic is odd, the p-specific norm-gate predicate is "
            "equivalent to p | Res(Phi_n,q_{r,s})."
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

    print("\nnormalized quotient-resultant rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: normalized={row['normalized_member_count']} "
            f"quotient_weights={row['quotient_weight_histogram']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X70 h4 normalized quotient-resultant checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
