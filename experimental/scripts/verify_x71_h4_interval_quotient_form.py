#!/usr/bin/env python3
"""X71 interval quotient form for normalized h=4 norm gates.

X70 reduces normalized words

    X + X^r - X^s - 1

to their quotient by X-1.  This verifier records the closed form of that
quotient: a constant plus or minus one consecutive monomial interval.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import json
import os
import sys
from typing import Any

import verify_x68_h4_norm_gate_certifier_keys as x68
import verify_x69_h4_unit_anchor_normal_form as x69
import verify_x70_h4_normalized_quotient_resultant as x70


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x71-h4-interval-quotient-form",
    "x71_h4_interval_quotient_form.json",
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
        "x69_h4_unit_anchor_normal_form": "PROVED",
        "x70_h4_normalized_quotient_resultant": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def trim(coeffs: list[int]) -> list[int]:
    coeffs = list(coeffs)
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def interval_quotient(member: tuple[int, int, int]) -> tuple[list[int], dict[str, int | str]]:
    _, r, s = member
    if r == s:
        return [1], {"sign": "zero", "start": r, "length": 0}
    start = min(r, s)
    stop = max(r, s)
    sign = 1 if r > s else -1
    coeffs = [0] * stop
    coeffs[0] = 1
    for exp in range(start, stop):
        coeffs[exp] += sign
    return trim(coeffs), {
        "sign": "positive" if sign > 0 else "negative",
        "start": start,
        "length": stop - start,
    }


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    reps = x68.replay_primitive_x64_reps(row)
    classes: dict[tuple[int, int, int], list[tuple[int, int, int]]] = defaultdict(list)
    for rep in sorted(reps):
        classes[x68.certifier_key(n, rep)].append(rep)

    form_failures: list[dict[str, Any]] = []
    weight_failures: list[dict[str, Any]] = []
    diagonal_members: list[dict[str, Any]] = []
    sign_hist: Counter[str] = Counter()
    length_hist: Counter[int] = Counter()
    start_hist: Counter[int] = Counter()
    sample_interval_quotients: list[dict[str, Any]] = []
    normalized_member_count = 0

    for key in sorted(classes):
        for member in sorted(x69.normalized_members(n, key)):
            normalized_member_count += 1
            q, rem = x70.divide_by_x_minus_one(x70.normalized_poly(n, member))
            interval_q, meta = interval_quotient(member)
            if rem != 0 or q != interval_q:
                if len(form_failures) < 5:
                    form_failures.append(
                        {
                            "key": list(key),
                            "member": list(member),
                            "division_quotient": q,
                            "interval_quotient": interval_q,
                            "remainder": rem,
                        }
                    )
            if meta["sign"] == "zero":
                if len(diagonal_members) < 5:
                    diagonal_members.append({"key": list(key), "member": list(member)})
            else:
                expected_weight = int(meta["length"]) + 1
                actual_weight = x70.poly_weight(q)
                if actual_weight != expected_weight and len(weight_failures) < 5:
                    weight_failures.append(
                        {
                            "key": list(key),
                            "member": list(member),
                            "weight": actual_weight,
                            "expected": expected_weight,
                        }
                    )
            sign_hist[str(meta["sign"])] += 1
            length_hist[int(meta["length"])] += 1
            start_hist[int(meta["start"])] += 1
            if len(sample_interval_quotients) < 5:
                sample_interval_quotients.append(
                    {
                        "key": list(key),
                        "member": list(member),
                        "sign": meta["sign"],
                        "start": meta["start"],
                        "length": meta["length"],
                        "quotient_prefix": interval_q[:12],
                    }
                )

    check(
        f"{row['label']}: every X70 quotient equals the interval formula",
        not form_failures,
        f"sample_failures={form_failures}",
    )
    check(
        f"{row['label']}: replay has no diagonal constant quotient",
        not diagonal_members,
        f"sample_diagonal={diagonal_members}",
    )
    check(
        f"{row['label']}: interval quotient weight is length plus one",
        not weight_failures,
        f"sample_failures={weight_failures}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": int(row["p"]),
        "certifier_key_count": len(classes),
        "normalized_member_count": normalized_member_count,
        "sign_histogram": dict(sorted(sign_hist.items())),
        "length_histogram": {str(k): v for k, v in sorted(length_hist.items())},
        "start_histogram_support_size": len(start_hist),
        "min_interval_length": min(length_hist) if length_hist else 0,
        "max_interval_length": max(length_hist) if length_hist else 0,
        "sample_interval_quotients": sample_interval_quotients,
        "form_failures": form_failures,
        "diagonal_members": diagonal_members,
        "weight_failures": weight_failures,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    rows = [row_report(row) for row in x60["rows"]]
    check(
        "all replay quotients match interval form",
        all(not row["form_failures"] for row in rows),
    )
    check(
        "all replay non-diagonal interval weights match length plus one",
        all(not row["weight_failures"] for row in rows),
    )
    check(
        "both interval signs occur in replay",
        any("positive" in row["sign_histogram"] for row in rows)
        and any("negative" in row["sign_histogram"] for row in rows),
    )

    return {
        "task": "X71 h=4 interval quotient form",
        "node": "active_core_count_bound",
        "status": "PROVED NORMAL FORM: X70 QUOTIENTS ARE SIGNED INTERVAL POLYNOMIALS",
        "theorem": (
            "Let A_m=1+X+...+X^{m-1}.  For an X69 normalized word "
            "X+X^r-X^s-1, the X70 quotient by X-1 is q_{r,s}=1+A_r-A_s.  "
            "Thus if r>s, q_{r,s}=1+X^s+...+X^{r-1}; if s>r, "
            "q_{r,s}=1-X^r-...-X^{s-1}; and if r=s, q_{r,s}=1.  "
            "The primitive norm-gate certifier can therefore work with "
            "constant-plus-signed-interval polynomials."
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

    print("\ninterval quotient rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: normalized={row['normalized_member_count']} "
            f"signs={row['sign_histogram']} "
            f"length_range={row['min_interval_length']}..{row['max_interval_length']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X71 h4 interval-quotient checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
