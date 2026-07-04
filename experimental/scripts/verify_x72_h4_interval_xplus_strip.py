#!/usr/bin/env python3
"""X72 optional X+1 strip for h=4 interval norm gates.

X71 puts every X70 quotient in the form

    q(X) = 1 +/- (X^a + ... + X^(a+ell-1)).

This verifier records the exact parity condition for q(-1)=0.  When it
holds, X+1 is another row-prime-safe factor for 2-power rows in odd
characteristic, so the sparse-resultant certifier can test q/(X+1).
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
import verify_x71_h4_interval_quotient_form as x71


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x72-h4-interval-xplus-strip",
    "x72_h4_interval_xplus_strip.json",
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
        "x68_h4_norm_gate_certifier_keys": "PROVED",
        "x70_h4_normalized_quotient_resultant": "PROVED",
        "x71_h4_interval_quotient_form": "PROVED",
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


def eval_at_minus_one(coeffs: list[int]) -> int:
    return sum(coeff if exp % 2 == 0 else -coeff for exp, coeff in enumerate(coeffs))


def divide_by_x_plus_one(coeffs: list[int]) -> tuple[list[int], int]:
    """Return q, rem with P=(X+1)q+rem for coeffs in ascending order."""
    coeffs = trim(coeffs)
    if len(coeffs) == 1:
        return [], coeffs[0]
    degree = len(coeffs) - 1
    quotient = [0] * degree
    quotient[degree - 1] = coeffs[degree]
    for exp in range(degree - 1, 0, -1):
        quotient[exp - 1] = coeffs[exp] - quotient[exp]
    rem = coeffs[0] - quotient[0]
    return trim(quotient), rem


def multiply_x_plus_one(quotient: list[int], rem: int = 0) -> list[int]:
    if not quotient:
        return [rem]
    out = [0] * (len(quotient) + 1)
    for exp, coeff in enumerate(quotient):
        out[exp] += coeff
        out[exp + 1] += coeff
    out[0] += rem
    return trim(out)


def parity_predicts_xplus(meta: dict[str, int | str]) -> bool:
    sign_name = str(meta["sign"])
    if sign_name == "zero":
        return False
    sign = 1 if sign_name == "positive" else -1
    start = int(meta["start"])
    length = int(meta["length"])
    return length % 2 == 1 and sign * ((-1) ** start) == -1


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    p = int(row["p"])
    reps = x68.replay_primitive_x64_reps(row)
    classes: dict[tuple[int, int, int], list[tuple[int, int, int]]] = defaultdict(list)
    for rep in sorted(reps):
        classes[x68.certifier_key(n, rep)].append(rep)

    parity_failures: list[dict[str, Any]] = []
    division_failures: list[dict[str, Any]] = []
    key_invariance_failures: list[dict[str, Any]] = []
    sample_stripped: list[dict[str, Any]] = []
    key_flag_histogram: Counter[str] = Counter()
    normalized_flag_histogram: Counter[str] = Counter()
    residual_weight_histogram: Counter[int] = Counter()
    residual_degree_histogram: Counter[int] = Counter()
    normalized_member_count = 0

    for key in sorted(classes):
        key_flags: list[bool] = []
        for member in sorted(x69.normalized_members(n, key)):
            normalized_member_count += 1
            quotient, rem = x70.divide_by_x_minus_one(x70.normalized_poly(n, member))
            interval_quotient, meta = x71.interval_quotient(member)
            predicted = parity_predicts_xplus(meta)
            actual = eval_at_minus_one(quotient) == 0
            key_flags.append(actual)
            normalized_flag_histogram["xplus_strip" if actual else "no_xplus_strip"] += 1

            if rem != 0 or quotient != interval_quotient or predicted != actual:
                if len(parity_failures) < 5:
                    parity_failures.append(
                        {
                            "key": list(key),
                            "member": list(member),
                            "meta": meta,
                            "predicted": predicted,
                            "actual": actual,
                            "q_at_minus_one": eval_at_minus_one(quotient),
                            "xminus_remainder": rem,
                        }
                    )

            if actual:
                residual, residual_rem = divide_by_x_plus_one(quotient)
                reconstructed = multiply_x_plus_one(residual, residual_rem)
                if residual_rem != 0 or reconstructed != quotient:
                    if len(division_failures) < 5:
                        division_failures.append(
                            {
                                "key": list(key),
                                "member": list(member),
                                "quotient": quotient,
                                "residual": residual,
                                "reconstructed": reconstructed,
                                "remainder": residual_rem,
                            }
                        )
                residual_weight_histogram[x70.poly_weight(residual)] += 1
                residual_degree_histogram[len(residual) - 1 if residual else -1] += 1
                if len(sample_stripped) < 5:
                    sample_stripped.append(
                        {
                            "key": list(key),
                            "member": list(member),
                            "sign": meta["sign"],
                            "start": meta["start"],
                            "length": meta["length"],
                            "residual_degree": len(residual) - 1 if residual else -1,
                            "residual_weight": x70.poly_weight(residual),
                            "residual_prefix": residual[:14],
                        }
                    )

        if any(key_flags) and not all(key_flags):
            if len(key_invariance_failures) < 5:
                key_invariance_failures.append({"key": list(key), "flags": key_flags})
        key_flag_histogram["xplus_strip" if any(key_flags) else "no_xplus_strip"] += 1

    check(f"{row['label']}: row is a 2-power row with n >= 4", n >= 4 and n & (n - 1) == 0, f"n={n}")
    check(f"{row['label']}: row characteristic is odd", p % 2 == 1, f"p={p}")
    check(
        f"{row['label']}: removed X+1 resultant factor is prime-safe",
        p % 2 == 1,
        f"p={p}, Phi_n(-1)=2",
    )
    check(
        f"{row['label']}: parity condition equals q(-1)=0",
        not parity_failures,
        f"sample_failures={parity_failures}",
    )
    check(
        f"{row['label']}: X+1 division reconstructs stripped quotients",
        not division_failures,
        f"sample_failures={division_failures}",
    )
    check(
        f"{row['label']}: X+1 strip flag is constant on each X68 key",
        not key_invariance_failures,
        f"sample_failures={key_invariance_failures}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "certifier_key_count": len(classes),
        "normalized_member_count": normalized_member_count,
        "key_flag_histogram": dict(sorted(key_flag_histogram.items())),
        "normalized_flag_histogram": dict(sorted(normalized_flag_histogram.items())),
        "residual_weight_histogram": {str(k): v for k, v in sorted(residual_weight_histogram.items())},
        "residual_degree_histogram": {str(k): v for k, v in sorted(residual_degree_histogram.items())},
        "parity_failures": parity_failures,
        "division_failures": division_failures,
        "key_invariance_failures": key_invariance_failures,
        "sample_stripped_residuals": sample_stripped,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    rows = [row_report(row) for row in x60["rows"]]
    check(
        "all replay rows satisfy the parity X+1 criterion",
        all(not row["parity_failures"] for row in rows),
    )
    check(
        "all replay stripped quotients divide exactly by X+1",
        all(not row["division_failures"] for row in rows),
    )
    check(
        "all replay rows have X68-key-invariant X+1 strip flags",
        all(not row["key_invariance_failures"] for row in rows),
    )
    check(
        "some replay key admits the X+1 strip",
        any(row["key_flag_histogram"].get("xplus_strip", 0) > 0 for row in rows),
    )
    check(
        "some replay key does not admit the X+1 strip",
        any(row["key_flag_histogram"].get("no_xplus_strip", 0) > 0 for row in rows),
    )

    return {
        "task": "X72 h=4 interval X+1 strip",
        "node": "active_core_count_bound",
        "status": "PROVED CERTIFIER REDUCTION: PARITY-MATCHED INTERVAL QUOTIENTS STRIP X+1 SAFELY",
        "theorem": (
            "For q=1+eps*(X^a+...+X^(a+ell-1)), q(-1)=0 if and only if "
            "ell is odd and eps*(-1)^a=-1.  In that case q=(X+1)h.  For "
            "2-power n>=4, Phi_n(-1)=2, so odd row characteristic makes "
            "p | Res(Phi_n,q) equivalent to p | Res(Phi_n,h).  The strip "
            "flag is invariant on X68 certifier keys because it is equivalent "
            "to the original four-term word vanishing at -1, and the X64/Galois "
            "key operations preserve that vanishing."
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

    print("\nX+1 strip rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: keys={row['key_flag_histogram']} "
            f"normalized={row['normalized_flag_histogram']}"
        )

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X72 h4 interval X+1-strip checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
