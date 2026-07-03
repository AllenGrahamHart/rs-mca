#!/usr/bin/env python3
"""EXTREMAL-MINE verifier: derivative clustering for split-pair residues.

The script reads the landed SP-CENSUS and SP-CENSUS-2 certificates.  For every
uncharged / anchored non-toral pair in those certificates, it reconstructs the
Q-locator, extracts L_Q', computes its finite-field roots and critical values,
and clusters pairs by the normalized derivative polynomial.

No subset search is performed here; this is a post-processing verifier over
the recorded census anatomy.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_sp_census_split_pairs as sp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SP_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "sp-census-split-pairs",
    "sp_census_split_pairs.json",
)
SP2_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "sp-census2-inrange",
    "sp_census2_inrange.json",
)
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "extremal-derivative-clustering",
    "extremal_derivative_clustering.json",
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


def trim(coeffs: list[int]) -> list[int]:
    out = coeffs[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_eval(coeffs: list[int], x: int, p: int) -> int:
    value = 0
    for c in reversed(coeffs):
        value = (value * x + c) % p
    return value


def derivative(coeffs: list[int], p: int) -> list[int]:
    if len(coeffs) <= 1:
        return [0]
    return trim([(i * coeffs[i]) % p for i in range(1, len(coeffs))])


def normalize_poly(coeffs: list[int], p: int) -> tuple[int, ...]:
    coeffs = trim([c % p for c in coeffs])
    if coeffs == [0]:
        return (0,)
    inv = pow(coeffs[-1], -1, p)
    return tuple((c * inv) % p for c in coeffs)


def divide_by_linear(coeffs: list[int], root: int, p: int) -> tuple[list[int], int]:
    """Divide low-to-high coeffs by x-root, returning (quotient, remainder)."""
    coeffs = trim([c % p for c in coeffs])
    high = list(reversed(coeffs))
    b = [high[0]]
    for a in high[1:]:
        b.append((a + root * b[-1]) % p)
    remainder = b[-1]
    quotient = list(reversed(b[:-1])) or [0]
    return trim(quotient), remainder


def root_multiplicity(coeffs: list[int], root: int, p: int) -> int:
    work = trim([c % p for c in coeffs])
    mult = 0
    while len(work) > 1 and poly_eval(work, root, p) == 0:
        work, remainder = divide_by_linear(work, root, p)
        if remainder != 0:
            break
        mult += 1
    return mult


def locator_profile(mask: int, n: int, p: int, domain: list[int]) -> dict[str, Any]:
    locator = sp.locator_coeffs(mask, domain, p)
    deriv = derivative(locator, p)
    domain_exp_by_value = {value: i for i, value in enumerate(domain)}
    roots = [x for x in range(p) if poly_eval(deriv, x, p) == 0]
    root_records = []
    critical_values = []
    for root in roots:
        mult = root_multiplicity(deriv, root, p)
        value = poly_eval(locator, root, p)
        critical_values.append(value)
        root_records.append(
            {
                "root": root,
                "multiplicity": mult,
                "critical_value": value,
                "domain_exponent": domain_exp_by_value.get(root),
            }
        )
    domain_roots = [r["domain_exponent"] for r in root_records if r["domain_exponent"] is not None]
    mult_hist = Counter(record["multiplicity"] for record in root_records)
    return {
        "locator_coeffs": locator,
        "derivative_coeffs": deriv,
        "normalized_derivative": list(normalize_poly(deriv, p)),
        "derivative_degree": len(trim(deriv)) - 1,
        "roots": root_records,
        "root_structure": {
            "roots_in_Fp": len(root_records),
            "domain_root_exponents": sorted(domain_roots),
            "domain_root_count": len(domain_roots),
            "off_domain_root_count": len(root_records) - len(domain_roots),
            "multiplicity_histogram": {str(k): v for k, v in sorted(mult_hist.items())},
            "distinct_critical_value_count": len(set(critical_values)),
        },
        "critical_values": sorted(critical_values),
    }


def key_id(key: tuple[int, ...]) -> str:
    raw = ",".join(map(str, key)).encode("ascii")
    return hashlib.sha256(raw).hexdigest()[:16]


def pair_iter_from_sp(row: dict[str, Any]) -> list[dict[str, int]]:
    out = []
    for h, q_mask, p_mask, route, defect, q_dz, p_dz in row["uncharged_pair_anatomy"]:
        out.append(
            {
                "h": h,
                "Q_mask": q_mask,
                "P_mask": p_mask,
                "route_code": route,
                "defect_degree": defect,
                "Q_derivative_zero_mask": q_dz,
                "P_derivative_zero_mask": p_dz,
            }
        )
    return out


def pair_iter_from_sp2(row: dict[str, Any]) -> list[dict[str, int]]:
    out = []
    for item in row["nontoral_pair_anatomy"]:
        out.append(
            {
                "h": int(item["h"]),
                "Q_mask": int(item["Q_mask"]),
                "P_mask": int(item["P_mask"]),
                "route_code": int(item["route_code"]),
                "defect_degree": int(item["defect_degree"]),
                "Q_derivative_zero_mask": int(item["Q_derivative_zero_mask"]),
                "P_derivative_zero_mask": int(item["P_derivative_zero_mask"]),
            }
        )
    return out


def analyze_row(source: str, row: dict[str, Any], pairs: list[dict[str, int]]) -> dict[str, Any]:
    p = int(row["p"])
    n = int(row["n"])
    domain = h1.mu_domain(p, n)
    profile_cache: dict[int, dict[str, Any]] = {}
    clusters: dict[tuple[int, ...], dict[str, Any]] = {}
    h_counts = Counter()
    route_counts = Counter()
    root_structure_counts = Counter()
    derivative_zero_profile = Counter()

    for pair in pairs:
        q_mask = int(pair["Q_mask"])
        if q_mask not in profile_cache:
            profile_cache[q_mask] = locator_profile(q_mask, n, p, domain)
        profile = profile_cache[q_mask]
        key = tuple(profile["normalized_derivative"])
        if key not in clusters:
            clusters[key] = {
                "class_id": key_id(key),
                "normalized_derivative": list(key),
                "count": 0,
                "h_counts": Counter(),
                "route_counts": Counter(),
                "root_structure": profile["root_structure"],
                "critical_values": profile["critical_values"],
                "representative": {
                    "h": pair["h"],
                    "Q_exponents": sp.exps(q_mask, n),
                    "P_exponents": sp.exps(int(pair["P_mask"]), n),
                    "Q_mask": q_mask,
                    "P_mask": int(pair["P_mask"]),
                    "defect_degree": pair["defect_degree"],
                    "route_code": pair["route_code"],
                },
            }
        clusters[key]["count"] += 1
        clusters[key]["h_counts"][pair["h"]] += 1
        clusters[key]["route_counts"][pair["route_code"]] += 1
        h_counts[pair["h"]] += 1
        route_counts[pair["route_code"]] += 1
        rz = profile["root_structure"]
        root_structure_counts[
            (
                rz["roots_in_Fp"],
                rz["domain_root_count"],
                rz["off_domain_root_count"],
                tuple(sorted(rz["multiplicity_histogram"].items())),
                rz["distinct_critical_value_count"],
            )
        ] += 1
        derivative_zero_profile[
            (int(pair["Q_derivative_zero_mask"]).bit_count(), int(pair["P_derivative_zero_mask"]).bit_count())
        ] += 1

    cluster_rows = []
    for item in clusters.values():
        cluster_rows.append(
            {
                **item,
                "h_counts": {str(k): v for k, v in sorted(item["h_counts"].items())},
                "route_counts": {str(k): v for k, v in sorted(item["route_counts"].items())},
            }
        )
    cluster_rows.sort(key=lambda item: (-item["count"], item["class_id"]))
    total = len(pairs)
    max_cluster = cluster_rows[0]["count"] if cluster_rows else 0
    max_share = (max_cluster / total) if total else 0.0
    check(
        f"{source}:{row['row']}: all pairs assigned to derivative classes",
        sum(item["count"] for item in cluster_rows) == total,
        f"total={total}",
    )
    check(
        f"{source}:{row['row']}: Q-profile cache does not exceed pair count",
        len(profile_cache) <= total if total else len(profile_cache) == 0,
    )
    return {
        "source": source,
        "row": row["row"],
        "p": p,
        "q": int(row["q"]),
        "n": n,
        "q_over_n_squared": p / (n * n),
        "total_pairs": total,
        "distinct_Q_masks": len(profile_cache),
        "derivative_class_count": len(cluster_rows),
        "max_derivative_class_size": max_cluster,
        "max_derivative_class_share": max_share,
        "h_counts": {str(k): v for k, v in sorted(h_counts.items())},
        "route_counts": {str(k): v for k, v in sorted(route_counts.items())},
        "derivative_zero_profile": {
            f"{a},{b}": v for (a, b), v in sorted(derivative_zero_profile.items())
        },
        "root_structure_counts": {
            json.dumps(
                {
                    "roots_in_Fp": key[0],
                    "domain_root_count": key[1],
                    "off_domain_root_count": key[2],
                    "multiplicity_histogram": dict(key[3]),
                    "distinct_critical_value_count": key[4],
                },
                sort_keys=True,
            ): value
            for key, value in sorted(root_structure_counts.items(), key=lambda kv: (-kv[1], kv[0]))
        },
        "top_derivative_classes": cluster_rows[:12],
    }


def aggregate(label: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    total = sum(row["total_pairs"] for row in rows)
    class_count = sum(row["derivative_class_count"] for row in rows)
    max_share = max((row["max_derivative_class_share"] for row in rows), default=0.0)
    weighted_top_mass = sum(row["max_derivative_class_size"] for row in rows)
    return {
        "label": label,
        "rows": [row["row"] for row in rows],
        "total_pairs": total,
        "sum_row_derivative_classes": class_count,
        "max_row_top_class_share": max_share,
        "sum_row_top_class_mass": weighted_top_mass,
        "top_mass_share": (weighted_top_mass / total) if total else 0.0,
    }


def build_certificate() -> dict[str, Any]:
    sp_cert = load_json(SP_CERT)
    sp2_cert = load_json(SP2_CERT)

    low_rows = [
        analyze_row("SP-CENSUS-lowq-domainwide", row, pair_iter_from_sp(row))
        for row in sp_cert["rows"]
        if int(row["uncharged_ordered_pairs"]) > 0
    ]
    inrange_rows = [
        analyze_row("SP-CENSUS-2-inrange-anchored", row, pair_iter_from_sp2(row))
        for row in sp2_cert["rows"]
        if int(row["anchored_nontoral_pairs"]) > 0
    ]

    falsifier = next(row for row in inrange_rows if row["row"] == "F1153_mu32_t3_h_le_8")
    check("in-range falsifier row is present", falsifier["total_pairs"] == 1236)
    check(
        "in-range falsifier has many derivative classes, not one pencil",
        falsifier["derivative_class_count"] > 100,
        f"classes={falsifier['derivative_class_count']}",
    )
    check(
        "in-range falsifier top class is small",
        falsifier["max_derivative_class_share"] < 0.05,
        f"share={falsifier['max_derivative_class_share']:.4f}",
    )
    clean_deriv = falsifier["derivative_zero_profile"].get("0,0", 0)
    check(
        "in-range falsifier is mostly domain-critical-point-free",
        clean_deriv > 0.9 * falsifier["total_pairs"],
        f"0,0={clean_deriv}, total={falsifier['total_pairs']}",
    )

    return {
        "task": "EXTREMAL-MINE derivative clustering",
        "node": "anchored_nontoral_pte_bound",
        "status": (
            "EVIDENCE: in-range falsifier does not collapse to a few shared derivative classes; "
            "it is a broad primitive moment/PTE cloud with mostly no domain critical points"
        ),
        "sources": {
            "sp_census": "sp_census_split_pairs.json",
            "sp_census2": "sp_census2_inrange.json",
        },
        "low_q_domainwide_rows": low_rows,
        "inrange_anchored_rows": inrange_rows,
        "comparison": {
            "low_q_domainwide": aggregate("low_q_domainwide", low_rows),
            "inrange_anchored": aggregate("inrange_anchored", inrange_rows),
            "interpretation": [
                "In-range survivors are not explained by one or two derivative pencils.",
                "The F1153/mu32 falsifier has many derivative classes and a small top class.",
                "The dominant common feature is absence of domain roots of L_Q' and L_P', not shared critical values.",
            ],
        },
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

    expected = load_json(CERT) if os.path.exists(CERT) else None
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    print("\nrow summary:")
    for row in cert["inrange_anchored_rows"]:
        print(
            f"{row['row']:24s} pairs={row['total_pairs']:<5d} "
            f"classes={row['derivative_class_count']:<5d} "
            f"top_share={row['max_derivative_class_share']:.4f} "
            f"dz={row['derivative_zero_profile']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nsummary:")
        print(json.dumps(cert["comparison"], indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} EXTREMAL-MINE derivative-clustering checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
