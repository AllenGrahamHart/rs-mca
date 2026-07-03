#!/usr/bin/env python3
"""P-A verifier: active-core probe for u1_alpha_active_core_incidence.

Extends the H1 toy harness with a per-base, per-core column.  For each base
locator S0 in a same-top-t class, and each target locator S in that class,
write the canonical star trade as

    S0 = C union Q,      S = C union P.

The minimal full-fiber band has |Q|=|P|=t+1.  In that case equality of the
top t locator coefficients is equivalent to L_P(X)-L_Q(X) being constant.
The active-core column counts, for each base S0, the cores Q that admit at
least one v1-unpaid minimal full-fiber trade, and their multiplicities K_Q.

Run:
  python3 experimental/scripts/verify_pa_active_core_probe.py
Refresh certificate:
  python3 experimental/scripts/verify_pa_active_core_probe.py --write-certificate
"""

from __future__ import annotations

from collections import Counter, defaultdict
import json
import math
import os
import sys
from itertools import combinations

import verify_h1_u1_toy_harness as h1


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "pa-active-core-probe",
    "pa_active_core_probe.json",
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


def mask_key(mask: int, n: int) -> str:
    return ",".join(str(i) for i in h1.exps_from_mask(mask, n))


def analyze_row(row: h1.RowSpec) -> dict[str, object]:
    domain = h1.mu_domain(row.p, row.n)
    sig_cache: dict[int, tuple[int, ...]] = {}

    def sig(mask: int) -> tuple[int, ...]:
        if mask not in sig_cache:
            sig_cache[mask] = h1.mask_signature(mask, domain, row.t, row.p)
        return sig_cache[mask]

    paid_partitions = h1.v1_paid_partitions(row.n, row.t)
    paid_cache: dict[tuple[int, int], str | None] = {}

    def paid(P: int, Q: int) -> str | None:
        key = (P, Q)
        if key not in paid_cache:
            paid_cache[key] = h1.v1_paid_reason(P, Q, paid_partitions)
        return paid_cache[key]

    groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for comb in combinations(range(row.n), row.A):
        mask = h1.mask_from_comb(comb)
        groups[sig(mask)].append(mask)

    hmin = row.t + 1
    bases_total = 0
    bases_with_active_core = 0
    minimal_full_fiber_trades = 0
    sporadic_minimal_trades = 0
    paid_minimal_trades = 0
    full_fiber_identity_failures = 0
    active_core_hist: Counter[int] = Counter()
    max_k_hist: Counter[int] = Counter()
    joint_hist: Counter[tuple[int, int]] = Counter()
    total_sporadic_hist: Counter[int] = Counter()
    max_active_cores = 0
    max_k_q = 0
    max_active_times_max_k = 0
    max_total_sporadic = 0
    worst_bases: list[dict[str, object]] = []

    for class_sig, masks in groups.items():
        for base in masks:
            bases_total += 1
            per_core: dict[int, int] = defaultdict(int)
            paid_here = 0
            minimal_here = 0
            for target in masks:
                if target == base:
                    continue
                P = target & ~base
                Q = base & ~target
                if P.bit_count() != hmin or Q.bit_count() != hmin:
                    continue
                minimal_here += 1
                minimal_full_fiber_trades += 1
                if sig(P) != sig(Q):
                    full_fiber_identity_failures += 1
                    continue
                reason = paid(P, Q)
                if reason is None:
                    per_core[Q] += 1
                    sporadic_minimal_trades += 1
                else:
                    paid_here += 1
                    paid_minimal_trades += 1

            active = len(per_core)
            max_k = max(per_core.values(), default=0)
            total_sporadic = sum(per_core.values())
            mass = active * max_k
            active_core_hist[active] += 1
            max_k_hist[max_k] += 1
            joint_hist[(active, max_k)] += 1
            total_sporadic_hist[total_sporadic] += 1
            if active:
                bases_with_active_core += 1
            max_active_cores = max(max_active_cores, active)
            max_k_q = max(max_k_q, max_k)
            max_active_times_max_k = max(max_active_times_max_k, mass)
            max_total_sporadic = max(max_total_sporadic, total_sporadic)

            if active and (not worst_bases or mass >= worst_bases[0]["active_times_max_k"]):
                record = {
                    "signature": list(class_sig),
                    "base": h1.exps_from_mask(base, row.n),
                    "family_size": len(masks),
                    "minimal_trades": minimal_here,
                    "paid_minimal_trades": paid_here,
                    "active_cores": active,
                    "max_K_Q": max_k,
                    "total_sporadic_minimal_trades": total_sporadic,
                    "active_times_max_k": mass,
                    "sample_cores": [
                        {
                            "Q": h1.exps_from_mask(qmask, row.n),
                            "K_Q": count,
                        }
                        for qmask, count in sorted(
                            per_core.items(),
                            key=lambda item: (-item[1], mask_key(item[0], row.n)),
                        )[:8]
                    ],
                }
                worst_bases.append(record)
                worst_bases = sorted(
                    worst_bases,
                    key=lambda r: (
                        -int(r["active_times_max_k"]),
                        -int(r["active_cores"]),
                        -int(r["max_K_Q"]),
                    ),
                )[:5]

    n2 = row.n * row.n
    check(
        f"{row.name}: minimal full-fiber identities",
        full_fiber_identity_failures == 0,
        f"minimal={minimal_full_fiber_trades}",
    )
    check(
        f"{row.name}: active-core mass below n^2",
        max_active_times_max_k <= n2,
        f"max active*maxK={max_active_times_max_k}, n^2={n2}",
    )
    check(
        f"{row.name}: total sporadic minimal trades per base below n^2",
        max_total_sporadic <= n2,
        f"max total={max_total_sporadic}, n^2={n2}",
    )

    return {
        "row": row.name,
        "p": row.p,
        "n": row.n,
        "A": row.A,
        "t": row.t,
        "minimal_h": hmin,
        "bases_total": bases_total,
        "bases_with_active_core": bases_with_active_core,
        "minimal_full_fiber_trades": minimal_full_fiber_trades,
        "sporadic_minimal_trades": sporadic_minimal_trades,
        "paid_minimal_trades": paid_minimal_trades,
        "full_fiber_identity_failures": full_fiber_identity_failures,
        "active_core_count_distribution": dict(sorted(active_core_hist.items())),
        "max_K_Q_distribution": dict(sorted(max_k_hist.items())),
        "total_sporadic_minimal_distribution": dict(sorted(total_sporadic_hist.items())),
        "joint_active_cores_by_max_K_Q": {
            f"{a},{k}": v for (a, k), v in sorted(joint_hist.items())
        },
        "max_active_cores_per_base": max_active_cores,
        "max_K_Q": max_k_q,
        "max_active_times_max_K_Q": max_active_times_max_k,
        "max_total_sporadic_minimal_trades_per_base": max_total_sporadic,
        "n_squared_budget": n2,
        "max_active_cores_over_n": max_active_cores / row.n,
        "max_active_times_max_K_Q_over_n_squared": max_active_times_max_k / n2,
        "max_total_sporadic_over_n_squared": max_total_sporadic / n2,
        "worst_bases": worst_bases,
    }


def build_certificate() -> dict[str, object]:
    rows = [analyze_row(row) for row in h1.ROWS]
    return {
        "task": "P-A active-core probe",
        "node": "u1_alpha_active_core_incidence",
        "source_harness": "verify_h1_u1_toy_harness.py",
        "rows": rows,
        "summary": {
            "max_active_cores_per_base": max(row["max_active_cores_per_base"] for row in rows),
            "max_K_Q": max(row["max_K_Q"] for row in rows),
            "max_active_times_max_K_Q": max(row["max_active_times_max_K_Q"] for row in rows),
            "max_total_sporadic_minimal_trades_per_base": max(
                row["max_total_sporadic_minimal_trades_per_base"] for row in rows
            ),
            "rows_with_active_cores": [
                row["row"] for row in rows if row["bases_with_active_core"]
            ],
        },
        "verdict": "PASS: active-core mass is far below n^2 in every checked toy row",
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    cert = build_certificate()
    check(
        "P-A aggregate active-core budget",
        all(row["max_active_times_max_K_Q"] <= row["n_squared_budget"] for row in cert["rows"]),
        f"max={cert['summary']['max_active_times_max_K_Q']}",
    )
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(cert, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")
    if FAILS:
        print("\nFAILURES:")
        for name in FAILS:
            print(f"  - {name}")
        return 1
    print("\nsummary:")
    print(json.dumps(cert["summary"], indent=2, sort_keys=True))
    print(f"\nAll {NCHECK} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
