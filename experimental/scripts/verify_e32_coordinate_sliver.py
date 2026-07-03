#!/usr/bin/env python3
"""E32-COORD verifier: pointwise coordinate-special eliminant sliver.

E32-MERGED ruled out profile-forced light-triangle eliminant vanishing.  This
refinement applies the same normal-form evaluator to actual coordinate
placements, not just one canonical representative per Venn profile.  The run is
kept deliberately small and exact: it exhausts all ordered light support triples
for two n=8 toy rows and reports the defect density inside each full-rank light
profile.

Stdlib only; no Monte Carlo.
Run: python3 experimental/scripts/verify_e32_coordinate_sliver.py
To refresh the pinned certificate:
  python3 experimental/scripts/verify_e32_coordinate_sliver.py --write-certificate
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
import json
import os
import sys

from verify_e32_merged_census import Fp, Profile, normal_rank, realize_profile


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "e32-coordinate-sliver",
    "e32_coordinate_sliver.json",
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


def profile_of_triple(n: int, triple: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]) -> Profile:
    S0, S1, S2 = (set(T) for T in triple)
    h_set = S0 & S1 & S2
    a_set = (S0 & S1) - S2
    b_set = (S0 & S2) - S1
    c_set = (S1 & S2) - S0
    x0_set = S0 - S1 - S2
    x1_set = S1 - S0 - S2
    x2_set = S2 - S0 - S1
    used = len(h_set | a_set | b_set | c_set | x0_set | x1_set | x2_set)
    return Profile(
        h=len(h_set),
        a=len(a_set),
        b=len(b_set),
        c=len(c_set),
        x0=len(x0_set),
        x1=len(x1_set),
        x2=len(x2_set),
        outside=n - used,
    )


def is_light_budget_profile(P: Profile, k: int) -> bool:
    return P.sigma <= 2 * k and max(P.budgets()) >= k + 1


def paid_taxonomy_labels(P: Profile, k: int) -> list[str]:
    labels: list[str] = []
    if P.sigma == 2 * k:
        labels.append("light_heavy_boundary")
    if P.h > 0 and P.a == P.b == P.c == 0:
        labels.append("sunflower_core")
    if min(P.r01, P.r02, P.r12) == 0:
        labels.append("disconnected_pair_overlap")
    if max(P.r01, P.r02, P.r12) >= k:
        labels.append("rung_2b_boundary_or_tangent")
    return labels or ["unclassified_coordinate_special"]


def row_audit(name: str, p: int, n: int, k: int, A: int, domain: list[int]) -> dict:
    F = Fp(p)
    supports = list(combinations(range(n), A))
    profile_full_rank: dict[Profile, bool] = {}
    profile_counts: dict[Profile, list[int]] = defaultdict(lambda: [0, 0])
    examples = []
    light_triples = 0
    skipped_profile_defect = 0

    for triple in permutations(supports, 3):
        P = profile_of_triple(n, triple)
        if not is_light_budget_profile(P, k):
            continue
        light_triples += 1
        if P not in profile_full_rank:
            profile_full_rank[P] = normal_rank(F, domain, k, realize_profile(P)) == 0
        if not profile_full_rank[P]:
            skipped_profile_defect += 1
            continue
        kd = normal_rank(F, domain, k, triple)
        profile_counts[P][0] += 1
        if kd:
            profile_counts[P][1] += 1
            if len(examples) < 8:
                examples.append(
                    {
                        "profile": P.as_dict(),
                        "kernel_dim": kd,
                        "supports": [list(T) for T in triple],
                        "paid_taxonomy_labels": paid_taxonomy_labels(P, k),
                    }
                )

    profile_rows = []
    defective_profile_count = 0
    def profile_sort_key(item):
        P = item[0]
        return (P.sigma, P.h, P.a, P.b, P.c, P.x0, P.x1, P.x2, P.outside)

    for P, (total, defects) in sorted(profile_counts.items(), key=profile_sort_key):
        if defects:
            defective_profile_count += 1
        profile_rows.append(
            {
                "profile": P.as_dict(),
                "coordinate_placements": total,
                "defects": defects,
                "defect_density": "0" if defects == 0 else f"{defects}/{total}",
            }
        )

    check(
        f"{name}: light triples evaluated pointwise",
        light_triples > 0 and sum(row["coordinate_placements"] for row in profile_rows) > 0,
        f"light={light_triples}, full_rank_placements={sum(row['coordinate_placements'] for row in profile_rows)}",
    )
    check(
        f"{name}: no coordinate-special eliminant vanishing",
        not examples,
        f"defective_profiles={defective_profile_count}, examples={len(examples)}",
    )

    return {
        "name": name,
        "field": f"F_{p}",
        "n": n,
        "k": k,
        "A": A,
        "t": A - k,
        "supports": len(supports),
        "light_triples": light_triples,
        "profile_forced_defect_triples_skipped": skipped_profile_defect,
        "full_rank_light_profiles": len(profile_rows),
        "full_rank_coordinate_placements": sum(row["coordinate_placements"] for row in profile_rows),
        "coordinate_special_defects": sum(row["defects"] for row in profile_rows),
        "defective_profiles": defective_profile_count,
        "profile_density_table": profile_rows,
        "defect_examples": examples,
    }


def main() -> None:
    rows = [
        row_audit("coord_n8_k2_A4", 11, 8, 2, 4, list(range(8))),
        row_audit("coord_n8_k3_A4", 11, 8, 3, 4, list(range(8))),
    ]
    check(
        "all audited rows have zero coordinate-special defects",
        all(row["coordinate_special_defects"] == 0 for row in rows),
        "defects=%s" % [row["coordinate_special_defects"] for row in rows],
    )
    result = {
        "node": "xr_eliminant_vanishing_class",
        "task": "E32-COORD",
        "status": "AUDIT: no coordinate-special light-triangle eliminant vanishing found in exact n=8 toys",
        "scope": "pointwise coordinate placements inside full-rank light profiles; exact n=8 toy rows",
        "rows": rows,
        "unpaid_coordinate_special_class_found": False,
        "checks": NCHECK,
    }

    if "--write-certificate" in sys.argv:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")

    expected = None
    if os.path.exists(CERT):
        with open(CERT) as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    if FAILS:
        print("\nrecomputed summary:")
        print(json.dumps(result, indent=2, sort_keys=True))
        print("\nFAIL:")
        for name in FAILS[:25]:
            print("  -", name)
        if len(FAILS) > 25:
            print(f"  ... {len(FAILS) - 25} more")
        sys.exit(1)

    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} E32-COORD checks")


if __name__ == "__main__":
    main()
