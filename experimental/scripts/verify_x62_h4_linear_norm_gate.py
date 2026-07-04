#!/usr/bin/env python3
"""X62 h=4 linear triples are finite-p norm-gate mass.

X60 reduced the centered h=4 surplus to filtered solutions of

    x + y - z = 1,        x,y,z in H.

X61 identified the true S-unit degeneracies.  This verifier records the next
step: over complex roots of unity there are no filtered solutions at all, so
every finite-field filtered solution is a p-specific four-term sparse
cyclotomic norm gate.
"""

from __future__ import annotations

import json
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
    "x62-h4-linear-norm-gate",
    "x62_h4_linear_norm_gate.json",
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
        "x30_finite_p_norm_gate": "PROVED",
        "x60_h4_linear_triple_form": "PROVED",
        "x61_h4_linear_degeneracy_ledger": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def reduced_coeff_vector_power_two(n: int, terms: list[tuple[int, int]]) -> tuple[int, ...]:
    """Reduce sum coeff*X^exp modulo Phi_n=X^(n/2)+1 in the standard basis."""
    coeffs = [0] * n
    for coeff, exp in terms:
        coeffs[exp % n] += coeff
    half = n // 2
    return tuple(coeffs[i] - coeffs[i + half] for i in range(half))


def phi_power_two_divides_linear_word(n: int, a: int, b: int, c: int) -> bool:
    # Word for x+y-z-1 with x=zeta^a, y=zeta^b, z=zeta^c.
    return all(
        value == 0
        for value in reduced_coeff_vector_power_two(
            n,
            [(1, a), (1, b), (-1, c), (-1, 0)],
        )
    )


def excluded_flags(n: int, a: int, b: int, c: int) -> dict[str, bool]:
    return {
        "x_equals_1": a % n == 0,
        "y_equals_1": b % n == 0,
        "z_equals_1": c % n == 0,
        "y_equals_x": b % n == a % n,
        "y_equals_minus_x": b % n == (a + n // 2) % n,
    }


def is_filtered(n: int, a: int, b: int, c: int) -> bool:
    return not any(excluded_flags(n, a, b, c).values())


def char_zero_row(n: int) -> dict[str, Any]:
    raw = 0
    filtered = 0
    branch_counts = {
        "x_equals_1": 0,
        "y_equals_1": 0,
        "z_equals_1": 0,
        "y_equals_x": 0,
        "y_equals_minus_x": 0,
    }
    bad_examples: list[dict[str, int]] = []

    for a in range(n):
        for b in range(n):
            for c in range(n):
                if not phi_power_two_divides_linear_word(n, a, b, c):
                    continue
                raw += 1
                flags = excluded_flags(n, a, b, c)
                for key, value in flags.items():
                    if value:
                        branch_counts[key] += 1
                if not any(flags.values()):
                    filtered += 1
                    if len(bad_examples) < 5:
                        bad_examples.append({"a": a, "b": b, "c": c})

    check(
        f"char-zero n={n}: filtered linear triple locus is empty",
        filtered == 0 and not bad_examples,
        f"raw={raw}, filtered={filtered}",
    )
    check(
        f"char-zero n={n}: raw solutions are all on X60/X61 branches",
        raw > 0 and all(value > 0 for value in branch_counts.values()),
        f"raw={raw}",
    )
    return {
        "n": n,
        "raw_char_zero_linear_triples": raw,
        "filtered_char_zero_linear_triples": filtered,
        "branch_counts": branch_counts,
        "bad_examples": bad_examples,
    }


def finite_row(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    p = int(row["p"])
    domain = h1.mu_domain(p, n)
    exponent_by_value = {value: exp for exp, value in enumerate(domain)}

    raw = 0
    filtered = 0
    non_phi_filtered = 0
    phi_filtered_examples: list[dict[str, Any]] = []
    norm_gate_examples: list[dict[str, Any]] = []

    for a, x in enumerate(domain):
        for b, y in enumerate(domain):
            z = (x + y - 1) % p
            c = exponent_by_value.get(z)
            if c is None:
                continue
            raw += 1
            if not is_filtered(n, a, b, c):
                continue
            filtered += 1
            phi_descended = phi_power_two_divides_linear_word(n, a, b, c)
            if phi_descended:
                if len(phi_filtered_examples) < 5:
                    phi_filtered_examples.append({"a": a, "b": b, "c": c})
            else:
                non_phi_filtered += 1
                if len(norm_gate_examples) < 5:
                    norm_gate_examples.append(
                        {
                            "a": a,
                            "b": b,
                            "c": c,
                            "word": f"X^{a}+X^{b}-X^{c}-1",
                        }
                    )

    expected = int(row["filtered_linear_triple_count"])
    check(
        f"{row['label']}: replayed raw linear count matches X60",
        raw == int(row["raw_linear_triple_count"]),
        f"computed={raw}, x60={row['raw_linear_triple_count']}",
    )
    check(
        f"{row['label']}: replayed filtered count matches X60",
        filtered == expected,
        f"computed={filtered}, x60={expected}",
    )
    check(
        f"{row['label']}: every filtered finite-field triple is non-Phi descended",
        non_phi_filtered == filtered and not phi_filtered_examples,
        f"filtered={filtered}, non_phi={non_phi_filtered}",
    )
    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "raw_linear_triple_count": raw,
        "filtered_linear_triple_count": filtered,
        "non_phi_descended_filtered_triples": non_phi_filtered,
        "norm_gate_interpretation": (
            "For each filtered triple, f(zeta)=0 in F_p and Phi_n does not "
            "divide f over Z; hence p divides Res(Phi_n,f)."
        ),
        "sample_norm_gate_words": norm_gate_examples,
        "phi_descended_filtered_examples": phi_filtered_examples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    char_zero_rows = [char_zero_row(n) for n in (8, 16, 32, 64)]
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    finite_rows = [finite_row(row) for row in x60["rows"]]
    check(
        "all characteristic-zero replay rows have empty filtered locus",
        all(row["filtered_char_zero_linear_triples"] == 0 for row in char_zero_rows),
    )
    check(
        "all finite X60 filtered triples are non-Phi descended",
        all(
            row["filtered_linear_triple_count"] == row["non_phi_descended_filtered_triples"]
            for row in finite_rows
        ),
    )
    check(
        "some finite replay row has genuine p-specific filtered mass",
        any(row["filtered_linear_triple_count"] > 0 for row in finite_rows),
    )
    return {
        "task": "X62 h=4 linear norm-gate localization",
        "node": "active_core_count_bound",
        "status": "PROVED LOCALIZATION: FILTERED H4 LINEAR TRIPLES ARE P-SPECIFIC NORM GATES",
        "theorem": (
            "Over complex roots of unity, x+y=z+1 has no X60-filtered "
            "solutions: if z != -1, the midpoint of the chord {x,y} equals "
            "the midpoint of {z,1}, and a circle chord is determined by its "
            "midpoint; if z=-1 then y=-x.  Therefore every finite-field "
            "filtered solution gives a four-term word f=X^a+X^b-X^c-1 with "
            "f(zeta)=0 but Phi_n not dividing f over Z.  By the X30 norm-gate "
            "principle, p divides Res(Phi_n,f)."
        ),
        "dependency_statuses": deps,
        "char_zero_rows": char_zero_rows,
        "finite_rows": finite_rows,
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

    print("\nfinite X60 rows:")
    for row in cert["finite_rows"]:
        print(
            f"{row['label']}: filtered={row['filtered_linear_triple_count']} "
            f"non_phi={row['non_phi_descended_filtered_triples']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X62 h4 linear norm-gate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
