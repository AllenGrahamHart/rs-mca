#!/usr/bin/env python3
"""X73 complete normalized-pair sieve for h=4 norm-gate rows.

X69-X72 reduce h=4 primitive norm-gate certification to normalized interval
quotients.  This verifier closes the row-local loop for the replay rows: it
enumerates every filtered normalized pair (1,r,s), tests whether the row
prime sees a primitive-root zero, and checks that the surviving X68 keys are
exactly the keys obtained by replaying the finite-field X60 triples.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x64_h4_linear_orbit_compression as x64
import verify_x68_h4_norm_gate_certifier_keys as x68
import verify_x70_h4_normalized_quotient_resultant as x70
import verify_x71_h4_interval_quotient_form as x71
import verify_x72_h4_interval_xplus_strip as x72


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x73-h4-normalized-pair-sieve",
    "x73_h4_normalized_pair_sieve.json",
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
X71_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x71-h4-interval-quotient-form",
    "x71_h4_interval_quotient_form.json",
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
        "x68_h4_norm_gate_certifier_keys": "PROVED",
        "x69_h4_unit_anchor_normal_form": "PROVED",
        "x71_h4_interval_quotient_form": "PROVED",
        "x72_h4_interval_xplus_strip": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def normalized_candidates(n: int) -> list[tuple[int, int, int]]:
    return [
        (1, r, s)
        for r in range(n)
        for s in range(n)
        if x64.is_filtered(n, 1, r, s) and x64.content(n, (1, r, s)) == 1
    ]


def primitive_root_zero(
    n: int,
    p: int,
    domain: list[int],
    units: list[int],
    member: tuple[int, int, int],
) -> bool:
    _, r, s = member
    for u in units:
        if (domain[u] + domain[(r * u) % n] - domain[(s * u) % n] - 1) % p == 0:
            return True
    return False


def replay_keys(row: dict[str, Any]) -> dict[tuple[int, int, int], list[tuple[int, int, int]]]:
    n = int(row["n"])
    classes: dict[tuple[int, int, int], list[tuple[int, int, int]]] = defaultdict(list)
    for rep in sorted(x68.replay_primitive_x64_reps(row)):
        classes[x68.certifier_key(n, rep)].append(rep)
    return classes


def interval_meta_for_member(member: tuple[int, int, int]) -> dict[str, int | str]:
    _, meta = x71.interval_quotient(member)
    return meta


def row_report(row: dict[str, Any], x71_row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    p = int(row["p"])
    domain = h1.mu_domain(p, n)
    units = x68.units_mod(n)
    candidates = normalized_candidates(n)
    expected_by_key = replay_keys(row)
    expected_keys = set(expected_by_key)

    survivor_pairs_by_key: dict[tuple[int, int, int], list[tuple[int, int, int]]] = defaultdict(list)
    sign_histogram: Counter[str] = Counter()
    xplus_histogram: Counter[str] = Counter()
    length_histogram: Counter[int] = Counter()
    sample_survivors: list[dict[str, Any]] = []

    for member in candidates:
        if not primitive_root_zero(n, p, domain, units, member):
            continue
        key = x68.certifier_key(n, member)
        survivor_pairs_by_key[key].append(member)
        meta = interval_meta_for_member(member)
        sign_histogram[str(meta["sign"])] += 1
        length_histogram[int(meta["length"])] += 1
        xplus_histogram["xplus_strip" if x72.parity_predicts_xplus(meta) else "no_xplus_strip"] += 1
        if len(sample_survivors) < 5:
            quotient, rem = x70.divide_by_x_minus_one(x70.normalized_poly(n, member))
            sample_survivors.append(
                {
                    "key": list(key),
                    "member": list(member),
                    "sign": meta["sign"],
                    "start": meta["start"],
                    "length": meta["length"],
                    "xminus_remainder": rem,
                    "quotient_prefix": quotient[:12],
                }
            )

    survivor_keys = set(survivor_pairs_by_key)
    missing = sorted(expected_keys - survivor_keys)
    extra = sorted(survivor_keys - expected_keys)
    survivor_pair_count = sum(len(items) for items in survivor_pairs_by_key.values())
    survivor_pair_histogram = Counter(len(items) for items in survivor_pairs_by_key.values())
    expected_rep_histogram = Counter(len(items) for items in expected_by_key.values())

    check(
        f"{row['label']}: normalized pair candidates have closed form count",
        len(candidates) == (n - 3) * (n - 1),
        f"candidates={len(candidates)}, expected={(n - 3) * (n - 1)}",
    )
    check(
        f"{row['label']}: complete normalized sieve finds exactly replay keys",
        not missing and not extra,
        f"missing={list(map(list, missing[:5]))}, extra={list(map(list, extra[:5]))}",
    )
    check(
        f"{row['label']}: survivor pair count matches X71 normalized replay count",
        survivor_pair_count == int(x71_row["normalized_member_count"]),
        f"survivors={survivor_pair_count}, X71={x71_row['normalized_member_count']}",
    )
    check(
        f"{row['label']}: every survivor key has at least one row representative",
        all(key in expected_by_key for key in survivor_pairs_by_key),
        f"survivor_keys={len(survivor_pairs_by_key)}, replay_keys={len(expected_by_key)}",
    )
    check(
        f"{row['label']}: every replay key has at least one normalized survivor",
        all(key in survivor_pairs_by_key for key in expected_by_key),
        f"survivor_keys={len(survivor_pairs_by_key)}, replay_keys={len(expected_by_key)}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "normalized_pair_candidate_count": len(candidates),
        "primitive_root_unit_count": len(units),
        "survivor_normalized_pair_count": survivor_pair_count,
        "survivor_key_count": len(survivor_keys),
        "replay_key_count": len(expected_keys),
        "rejected_normalized_pair_count": len(candidates) - survivor_pair_count,
        "missing_replay_keys": [list(key) for key in missing],
        "extra_sieve_keys": [list(key) for key in extra],
        "survivor_pairs_per_key_histogram": {
            str(k): v for k, v in sorted(survivor_pair_histogram.items())
        },
        "replay_representatives_per_key_histogram": {
            str(k): v for k, v in sorted(expected_rep_histogram.items())
        },
        "survivor_interval_sign_histogram": dict(sorted(sign_histogram.items())),
        "survivor_xplus_strip_histogram": dict(sorted(xplus_histogram.items())),
        "survivor_length_histogram": {str(k): v for k, v in sorted(length_histogram.items())},
        "sample_survivors": sample_survivors,
    }


def by_label(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["label"]: row for row in rows}


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    x71_cert = load_json(X71_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    check("X71 certificate has replay rows", bool(x71_cert.get("rows")))
    x71_rows = by_label(x71_cert["rows"])

    rows = []
    for row in x60["rows"]:
        label = row["label"]
        check(f"{label}: X71 row exists", label in x71_rows)
        rows.append(row_report(row, x71_rows[label]))

    check(
        "all complete normalized sieves match replay key sets",
        all(not row["missing_replay_keys"] and not row["extra_sieve_keys"] for row in rows),
    )
    check(
        "some normalized candidate is rejected in every row",
        all(row["rejected_normalized_pair_count"] > 0 for row in rows),
    )
    check(
        "some normalized candidate survives in every row",
        all(row["survivor_normalized_pair_count"] > 0 for row in rows),
    )
    check(
        "some survivor uses the X+1 strip branch",
        any(row["survivor_xplus_strip_histogram"].get("xplus_strip", 0) > 0 for row in rows),
    )

    return {
        "task": "X73 h=4 normalized pair sieve",
        "node": "active_core_count_bound",
        "status": "PROVED ROW-LOCAL CERTIFIER: COMPLETE NORMALIZED PAIR SIEVE MATCHES REPLAY KEYS",
        "theorem": (
            "For p == 1 mod n, p not dividing n, Phi_n splits over F_p as the "
            "simple product over primitive n-th roots zeta^u.  Therefore a "
            "normalized word X+X^r-X^s-1 is p-norm-gated iff it vanishes at "
            "zeta^u for some unit u.  Enumerating every filtered normalized "
            "pair (1,r,s), applying this primitive-root test, and grouping "
            "survivors by the X68 key gives the complete row-local certifier "
            "key set.  In the replay rows this complete sieve matches exactly "
            "the keys obtained independently from finite-field X60 triples."
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

    print("\nnormalized-pair sieve rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: candidates={row['normalized_pair_candidate_count']} "
            f"survivor_pairs={row['survivor_normalized_pair_count']} "
            f"keys={row['survivor_key_count']}"
        )

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X73 h4 normalized-pair sieve checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
