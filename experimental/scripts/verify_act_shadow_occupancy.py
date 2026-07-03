#!/usr/bin/env python3
"""ACT-SHADOW verifier: active occupied subcores and depth cells.

OCC-1 and OCC-2 show that formal cell lattices are too large; the useful
object is the active shadow, i.e. cells actually occupied by aligned partners
after the strip.  This verifier reuses the E33 sampled aligned-pair engine and
counts both:

* lower-overlap occupied subcores, the A1/OCC-1 client;
* partial-tangent depth cells r = k+d, the A2 active-shadow client.

The checked toy shape is the E33 shape n=16, k=8, A=11, t=3.  Its lower band is
r in {6,7}; its partial-tangent depth band is r=9 (d=1, s=2).
"""

from __future__ import annotations

from collections import Counter
import json
import math
import os
import sys
from typing import Any

import numpy as np

import verify_e33_deep_link_staircase as e33


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "act-shadow-occupancy",
    "act_shadow_occupancy.json",
)
OCC1_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "occ1-occupied-subcore-accounting",
    "occ1_occupied_subcore_accounting.json",
)
PA_CERT = os.path.join(
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
    print(line)
    if not cond:
        FAILS.append(name)


def load_json(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def lower_overlap_rs(row: e33.Row) -> list[int]:
    return [
        r
        for r in range(row.A + 1)
        if 2 * r > row.k and r < row.k and row.A - r <= row.n - row.A
    ]


def depth_cell_rs(row: e33.Row) -> list[int]:
    t = row.A - row.k
    return [
        r
        for r in range(row.k + 1, row.A - 1)
        if 2 <= row.A - r <= t - 1
    ]


def analyze_row(row: e33.Row) -> dict[str, Any]:
    engine = e33.build_engine(row)
    rng = np.random.default_rng(row.seed)
    q, n, k, A = row.q, row.n, row.k, row.A
    lower_rs = lower_overlap_rs(row)
    depth_rs = depth_cell_rs(row)

    lower_totals = Counter({r: 0 for r in lower_rs})
    depth_totals = Counter({r: 0 for r in depth_rs})
    lower_active_hist = Counter()
    depth_active_hist = Counter()
    lower_joint_hist = Counter()
    depth_joint_hist = Counter()
    lower_formal_cells = {
        r: math.comb(A, r) * math.comb(n - A, A - r) for r in lower_rs
    }
    depth_formal_cells = {r: math.comb(A, r) for r in depth_rs}

    max_lower_active = 0
    max_depth_active = 0
    max_lower_k = 0
    max_depth_k = 0
    max_lower_events = 0
    max_depth_events = 0
    anchors_with_lower = 0
    anchors_with_depth = 0

    chunk = 128
    done = 0
    while done < row.samples:
        m = min(chunk, row.samples - done)
        anchor_indices = rng.integers(0, len(engine.supports), m)
        anchor_z = rng.integers(0, q, m, dtype=np.int64)
        coeffs = rng.integers(0, q, (m, k), dtype=np.int64)
        codewords = coeffs @ engine.gmat % q
        V = rng.integers(0, q, (m, n), dtype=np.int64)
        U = rng.integers(0, q, (m, n), dtype=np.int64)
        for i, sidx in enumerate(anchor_indices.tolist()):
            T0 = engine.supports[sidx]
            U[i, list(T0)] = (codewords[i, list(T0)] - anchor_z[i] * V[i, list(T0)]) % q
        codes = e33.support_codes(engine, U, V)

        for i, sidx in enumerate(anchor_indices.tolist()):
            anchor_mask = engine.support_masks[sidx]
            anchor_z_i = int(anchor_z[i])
            lower_cells: dict[int, int] = {}
            depth_cells: dict[int, int] = {}

            for idx, code in enumerate(codes[i].tolist()):
                mask = engine.support_masks[idx]
                r = (mask & anchor_mask).bit_count()
                if r not in lower_rs and r not in depth_rs:
                    continue
                if code == engine.empty_code or code == anchor_z_i:
                    continue
                if code == engine.all_code:
                    multiplicity = q - 1
                elif 0 <= code < q:
                    multiplicity = 1
                else:
                    raise AssertionError(f"unexpected support code {code}")

                core = mask & anchor_mask
                if r in lower_rs:
                    lower_cells[core] = lower_cells.get(core, 0) + multiplicity
                    lower_totals[r] += multiplicity
                if r in depth_rs:
                    depth_cells[core] = depth_cells.get(core, 0) + multiplicity
                    depth_totals[r] += multiplicity

            lower_active = len(lower_cells)
            depth_active = len(depth_cells)
            lower_k = max(lower_cells.values(), default=0)
            depth_k = max(depth_cells.values(), default=0)
            lower_events = sum(lower_cells.values())
            depth_events = sum(depth_cells.values())

            anchors_with_lower += int(lower_active > 0)
            anchors_with_depth += int(depth_active > 0)
            max_lower_active = max(max_lower_active, lower_active)
            max_depth_active = max(max_depth_active, depth_active)
            max_lower_k = max(max_lower_k, lower_k)
            max_depth_k = max(max_depth_k, depth_k)
            max_lower_events = max(max_lower_events, lower_events)
            max_depth_events = max(max_depth_events, depth_events)
            lower_active_hist[lower_active] += 1
            depth_active_hist[depth_active] += 1
            lower_joint_hist[(lower_active, lower_k)] += 1
            depth_joint_hist[(depth_active, depth_k)] += 1

        done += m

    lower_mass = max_lower_active * max_lower_k
    depth_mass = max_depth_active * max_depth_k
    n2 = n * n
    check(
        f"F_{q}: lower active occupied subcores are O(n) in the toy shadow",
        max_lower_active <= 5 * n,
        f"max={max_lower_active}, 5n={5*n}",
    )
    check(
        f"F_{q}: lower active mass fits n^2",
        lower_mass <= n2 and max_lower_events <= n2,
        f"active*maxK={lower_mass}, events={max_lower_events}, n^2={n2}",
    )
    check(
        f"F_{q}: active depth cells are at most linear",
        max_depth_active <= n,
        f"max={max_depth_active}, n={n}",
    )
    check(
        f"F_{q}: active depth-cell mass fits n^2",
        depth_mass <= n2 and max_depth_events <= n2,
        f"active*maxK={depth_mass}, events={max_depth_events}, n^2={n2}",
    )
    check(
        f"F_{q}: active depth shadow is smaller than the formal depth lattice",
        all(max_depth_active < count for count in depth_formal_cells.values()),
        f"max_active={max_depth_active}, formal={dict(depth_formal_cells)}",
    )

    return {
        "row": f"F_{q}_mu{n}_k{k}_A{A}_t{A-k}",
        "q": q,
        "n": n,
        "k": k,
        "A": A,
        "t": A - k,
        "samples": row.samples,
        "lower_overlap_rs": lower_rs,
        "depth_cell_rs": depth_rs,
        "lower_formal_partner_cells_by_r": {str(r): v for r, v in lower_formal_cells.items()},
        "depth_formal_cells_by_r": {str(r): v for r, v in depth_formal_cells.items()},
        "lower_observed_events_by_r": {str(r): lower_totals[r] for r in lower_rs},
        "depth_observed_events_by_r": {str(r): depth_totals[r] for r in depth_rs},
        "anchors_with_lower_shadow": anchors_with_lower,
        "anchors_with_depth_shadow": anchors_with_depth,
        "max_lower_active_subcores_per_anchor": max_lower_active,
        "max_depth_active_cells_per_anchor": max_depth_active,
        "max_lower_multiplicity_per_subcore": max_lower_k,
        "max_depth_multiplicity_per_cell": max_depth_k,
        "max_lower_events_per_anchor": max_lower_events,
        "max_depth_events_per_anchor": max_depth_events,
        "max_lower_active_times_max_K": lower_mass,
        "max_depth_active_times_max_K": depth_mass,
        "n_squared_budget": n2,
        "lower_active_count_distribution": {str(k): v for k, v in sorted(lower_active_hist.items())},
        "depth_active_count_distribution": {str(k): v for k, v in sorted(depth_active_hist.items())},
        "lower_joint_active_by_max_K": {
            f"{a},{b}": v for (a, b), v in sorted(lower_joint_hist.items())
        },
        "depth_joint_active_by_max_K": {
            f"{a},{b}": v for (a, b), v in sorted(depth_joint_hist.items())
        },
    }


def build_certificate() -> dict[str, Any]:
    rows = [
        analyze_row(e33.Row(q=97, n=16, k=8, A=11, samples=4096, seed=20260733)),
        analyze_row(e33.Row(q=17, n=16, k=8, A=11, samples=512, seed=20260734)),
    ]
    occ1 = load_json(OCC1_CERT)
    pa = load_json(PA_CERT)
    max_lower_active = max(row["max_lower_active_subcores_per_anchor"] for row in rows)
    max_depth_active = max(row["max_depth_active_cells_per_anchor"] for row in rows)
    max_depth_mass = max(row["max_depth_active_times_max_K"] for row in rows)
    check(
        "ACT-SHADOW lower column agrees with OCC-1 max active cores",
        max_lower_active == occ1["aggregate"]["max_actual_occupied_cores_per_anchor"],
        f"act={max_lower_active}, occ1={occ1['aggregate']['max_actual_occupied_cores_per_anchor']}",
    )
    check(
        "ACT-SHADOW depth column has no super-budget toy row",
        all(row["max_depth_active_times_max_K"] <= row["n_squared_budget"] for row in rows),
        f"max_depth_mass={max_depth_mass}",
    )

    return {
        "task": "ACT-SHADOW active occupancy audit",
        "nodes": [
            "a1_lower_overlap_occupied_subcore_accounting",
            "a2_depth_cell_active_shadow_bound",
            "u1_alpha_active_core_incidence",
        ],
        "source": "E33 sampled aligned-pair engine plus P-A/OCC-1 certificates",
        "rows": rows,
        "summary": {
            "max_lower_active_subcores_per_anchor": max_lower_active,
            "max_depth_active_cells_per_anchor": max_depth_active,
            "max_depth_active_times_max_K": max_depth_mass,
            "pa_max_active_cores_per_base": pa["summary"]["max_active_cores_per_base"],
            "pa_max_active_times_max_K_Q": pa["summary"]["max_active_times_max_K_Q"],
            "occ1_max_partner_events_through_one_actual_core": occ1["aggregate"][
                "max_partner_events_through_one_actual_core"
            ],
            "verdict": (
                "No active-shadow falsifier: active lower subcores and active "
                "depth cells stay within the calibrated linear/n^2 budgets in "
                "the toy aligned-pair rows."
            ),
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

    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    print("\nsummary:")
    print(json.dumps(cert["summary"], indent=2, sort_keys=True))

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed summary:")
        print(json.dumps(cert, indent=2, sort_keys=True))
        return 1
    print(f"\nPASS: {NCHECK} ACT-SHADOW occupancy checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
