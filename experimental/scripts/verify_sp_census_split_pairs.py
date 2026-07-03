#!/usr/bin/env python3
"""SP-CENSUS verifier: domain-wide split-pair census.

This is the X-10 support census requested after P-A/P-B.  It enumerates every
ordered disjoint split pair

    (Q, P),       |Q|=|P|=h,       e_i(Q)=e_i(P) for 1<=i<=t,

for h in (t, floor(log2(n))^2], capped by h<=n/2.  The scan is domain-wide:
it is not conditioned on a base locator S0.

The charged classifier is the X-9 toral normal-form dictionary on mu_n:

  * cyclic fibers:    psi = F(x^m)
  * dihedral fibers:  psi = F(x^m + alpha x^-m), all alpha/scaling offsets

A pair is charged when both Q and P are unions of fibers for one common
cyclic/dihedral partition in the frozen degree window.  Everything else is
recorded as uncharged, with compact per-pair anatomy:

    [h, Q_mask, P_mask, route_code, defect_degree,
     Q_derivative_zero_mask, P_derivative_zero_mask]

where route_code 1 means a minimal subtrade is present and route_code 3 means
primitive moment/PTE handoff.  Masks are exponent masks in the fixed mu_n
generator order.

Run:
  python3 experimental/scripts/verify_sp_census_split_pairs.py
Refresh certificate:
  python3 experimental/scripts/verify_sp_census_split_pairs.py --write-certificate
"""

from __future__ import annotations

from array import array
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
import json
import math
import os
import sys

import numpy as np

import verify_h1_u1_toy_harness as h1


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "sp-census-split-pairs",
    "sp_census_split_pairs.json",
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


def quiet_check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    if not cond:
        line = name
        if detail:
            line += f" ({detail})"
        FAILS.append(line)


@dataclass(frozen=True)
class SplitRow:
    name: str
    p: int
    n: int
    t: int


ROWS = (
    SplitRow("F17_mu8_t3", 17, 8, 3),
    SplitRow("F13_mu12_t3", 13, 12, 3),
    SplitRow("F17_mu16_t3_small_q", 17, 16, 3),
    SplitRow("F97_mu16_t3_large_q", 97, 16, 3),
    SplitRow("F41_mu20_t3", 41, 20, 3),
    SplitRow("F97_mu24_t3", 97, 24, 3),
)

ROUTE_MINIMAL_SUBTRADE = 1
ROUTE_PRIMITIVE_MOMENT_PTE = 3


def exps(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def h_max(row: SplitRow) -> int:
    return min(int(math.log2(row.n)) ** 2, row.n // 2)


def comb_mask_and_code(
    comb: tuple[int, ...],
    domain: list[int],
    t: int,
    p: int,
) -> tuple[int, int]:
    mask = 0
    e = [0] * (t + 1)
    e[0] = 1
    for i in comb:
        mask |= 1 << i
        x = domain[i]
        for r in range(t, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    code = 0
    mul = 1
    for v in e[1:]:
        code += v * mul
        mul *= p
    return mask, code


def signature_arrays(row: SplitRow, h: int, domain: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    keys = array("I")
    masks = array("I")
    for comb in combinations(range(row.n), h):
        mask, code = comb_mask_and_code(comb, domain, row.t, row.p)
        keys.append(code)
        masks.append(mask)
    key_arr = np.frombuffer(keys, dtype=np.uint32).copy()
    mask_arr = np.frombuffer(masks, dtype=np.uint32).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, mask_arr, order


def quotient_classes(n: int, m: int) -> list[int]:
    g = math.gcd(n, m)
    if g <= 1:
        return []
    step = n // g
    out = []
    for r in range(step):
        mask = 0
        for j in range(g):
            mask |= 1 << ((r + j * step) % n)
        out.append(mask)
    return out


def dihedral_classes(n: int, m: int, offset: int) -> list[int]:
    g = math.gcd(n, m)
    if g <= 1:
        return []
    step = n // g
    out = []
    seen: set[int] = set()
    for r in range(step):
        if r in seen:
            continue
        residues = {r % step, (offset - r) % step}
        seen.update(residues)
        mask = 0
        for a in residues:
            for j in range(g):
                mask |= 1 << ((a + j * step) % n)
        out.append(mask)
    return out


def is_union(mask: int, classes: list[int]) -> bool:
    if not classes:
        return False
    for cls in classes:
        hit = mask & cls
        if hit and hit != cls:
            return False
    return True


def charged_partitions(row: SplitRow) -> list[tuple[str, list[int]]]:
    out: list[tuple[str, list[int]]] = []
    for m in range(row.t + 1, h_max(row) + 1):
        qclasses = quotient_classes(row.n, m)
        if qclasses:
            out.append((f"cyclic:m={m}", qclasses))
        step = row.n // math.gcd(row.n, m)
        for offset in range(step):
            dclasses = dihedral_classes(row.n, m, offset)
            if dclasses:
                out.append((f"dihedral:m={m}:offset={offset}", dclasses))
    return out


def charged_reason(q_mask: int, p_mask: int, partitions: list[tuple[str, list[int]]]) -> str | None:
    for reason, classes in partitions:
        if is_union(q_mask, classes) and is_union(p_mask, classes):
            return reason
    return None


def locator_coeffs(mask: int, domain: list[int], p: int) -> list[int]:
    coeffs = [1]
    for i, x in enumerate(domain):
        if not ((mask >> i) & 1):
            continue
        out = [0] * (len(coeffs) + 1)
        for j, c in enumerate(coeffs):
            out[j] = (out[j] - x * c) % p
            out[j + 1] = (out[j + 1] + c) % p
        coeffs = out
    return coeffs


def defect_degree(q_mask: int, p_mask: int, domain: list[int], p: int) -> int:
    cq = locator_coeffs(q_mask, domain, p)
    cp = locator_coeffs(p_mask, domain, p)
    m = max(len(cq), len(cp))
    cq += [0] * (m - len(cq))
    cp += [0] * (m - len(cp))
    for i in range(m - 1, -1, -1):
        if (cp[i] - cq[i]) % p:
            return i
    return -1


def derivative_zero_mask(mask: int, domain: list[int], p: int) -> int:
    coeffs = locator_coeffs(mask, domain, p)
    deriv = [(i * coeffs[i]) % p for i in range(1, len(coeffs))]
    out = 0
    for idx, x in enumerate(domain):
        value = 0
        power = 1
        for c in deriv:
            value = (value + c * power) % p
            power = (power * x) % p
        if value == 0:
            out |= 1 << idx
    return out


def minimal_subtrade_signature_set(
    mask: int,
    row: SplitRow,
    domain: list[int],
) -> frozenset[int]:
    bits = exps(mask, row.n)
    return frozenset(
        comb_mask_and_code(comb, domain, row.t, row.p)[1]
        for comb in combinations(bits, row.t + 1)
    )


def analyze_row(row: SplitRow) -> dict[str, object]:
    domain = h1.mu_domain(row.p, row.n)
    partitions = charged_partitions(row)
    min_sig_cache: dict[int, frozenset[int]] = {}
    deriv_cache: dict[int, int] = {}
    defect_cache: dict[tuple[int, int], int] = {}

    def has_minimal_subtrade(q_mask: int, p_mask: int) -> bool:
        if q_mask not in min_sig_cache:
            min_sig_cache[q_mask] = minimal_subtrade_signature_set(q_mask, row, domain)
        if p_mask not in min_sig_cache:
            min_sig_cache[p_mask] = minimal_subtrade_signature_set(p_mask, row, domain)
        return not min_sig_cache[q_mask].isdisjoint(min_sig_cache[p_mask])

    def dz(mask: int) -> int:
        if mask not in deriv_cache:
            deriv_cache[mask] = derivative_zero_mask(mask, domain, row.p)
        return deriv_cache[mask]

    def deg(q_mask: int, p_mask: int) -> int:
        key = (q_mask, p_mask)
        if key not in defect_cache:
            defect_cache[key] = defect_degree(q_mask, p_mask, domain, row.p)
        return defect_cache[key]

    total = 0
    charged = 0
    uncharged = 0
    by_h = Counter()
    charged_by_h = Counter()
    uncharged_by_h = Counter()
    charged_reasons = Counter()
    route_counts = Counter()
    defect_degrees = Counter()
    derivative_zero_counts = Counter()
    max_signature_group = 0
    uncharged_anatomy: list[list[int]] = []

    for h in range(row.t + 1, h_max(row) + 1):
        key_arr, mask_arr, order = signature_arrays(row, h, domain)
        start = 0
        while start < len(order):
            code = key_arr[order[start]]
            end = start + 1
            while end < len(order) and key_arr[order[end]] == code:
                end += 1
            size = end - start
            max_signature_group = max(max_signature_group, size)
            if size < 2:
                start = end
                continue
            masks = [int(mask_arr[order[i]]) for i in range(start, end)]
            for q_mask in masks:
                for p_mask in masks:
                    if q_mask == p_mask or (q_mask & p_mask):
                        continue
                    total += 1
                    by_h[h] += 1
                    reason = charged_reason(q_mask, p_mask, partitions)
                    if reason is not None:
                        charged += 1
                        charged_by_h[h] += 1
                        charged_reasons[reason] += 1
                        continue

                    d = deg(q_mask, p_mask)
                    quiet_check(
                        f"{row.name}: split pair has expected defect degree",
                        d <= h - row.t - 1,
                        f"h={h}, degree={d}, bound={h-row.t-1}",
                    )
                    if h == row.t + 1 or has_minimal_subtrade(q_mask, p_mask):
                        route = ROUTE_MINIMAL_SUBTRADE
                    else:
                        route = ROUTE_PRIMITIVE_MOMENT_PTE
                    q_dz = dz(q_mask)
                    p_dz = dz(p_mask)
                    uncharged += 1
                    uncharged_by_h[h] += 1
                    route_counts[route] += 1
                    defect_degrees[d] += 1
                    derivative_zero_counts[(q_dz.bit_count(), p_dz.bit_count())] += 1
                    uncharged_anatomy.append([h, q_mask, p_mask, route, d, q_dz, p_dz])
            start = end

    n2 = row.n * row.n
    check(
        f"{row.name}: split-pair accounting partitions total",
        total == charged + uncharged,
        f"total={total}, charged={charged}, uncharged={uncharged}",
    )
    check(
        f"{row.name}: uncharged anatomy is complete",
        len(uncharged_anatomy) == uncharged,
    )

    return {
        "row": row.name,
        "p": row.p,
        "q": row.p,
        "n": row.n,
        "t": row.t,
        "h_range": [row.t + 1, h_max(row)],
        "subset_signature_max_group": max_signature_group,
        "ordered_split_pairs": total,
        "charged_ordered_pairs": charged,
        "uncharged_ordered_pairs": uncharged,
        "n_squared_budget": n2,
        "ordered_uncharged_over_n_squared": uncharged / n2,
        "ordered_split_pairs_by_h": {str(k): v for k, v in sorted(by_h.items())},
        "charged_by_h": {str(k): v for k, v in sorted(charged_by_h.items())},
        "uncharged_by_h": {str(k): v for k, v in sorted(uncharged_by_h.items())},
        "charged_reasons": dict(sorted(charged_reasons.items())),
        "uncharged_route_counts": {str(k): v for k, v in sorted(route_counts.items())},
        "uncharged_defect_degrees": {str(k): v for k, v in sorted(defect_degrees.items())},
        "derivative_zero_count_pairs": {
            f"{a},{b}": v for (a, b), v in sorted(derivative_zero_counts.items())
        },
        "uncharged_anatomy_encoding": [
            "h",
            "Q_mask",
            "P_mask",
            "route_code",
            "defect_degree",
            "Q_derivative_zero_mask",
            "P_derivative_zero_mask",
        ],
        "route_code_legend": {
            str(ROUTE_MINIMAL_SUBTRADE): "contains a minimal size-(t+1) subtrade",
            str(ROUTE_PRIMITIVE_MOMENT_PTE): "primitive moment/PTE handoff",
        },
        "uncharged_pair_anatomy": uncharged_anatomy,
        "sample_uncharged_pairs": [
            {
                "h": item[0],
                "Q": exps(item[1], row.n),
                "P": exps(item[2], row.n),
                "route_code": item[3],
                "defect_degree": item[4],
                "Q_derivative_zero_exponents": exps(item[5], row.n),
                "P_derivative_zero_exponents": exps(item[6], row.n),
            }
            for item in uncharged_anatomy[:10]
        ],
    }


def build_result() -> dict[str, object]:
    rows = [analyze_row(row) for row in ROWS]
    by_name = {row["row"]: row for row in rows}
    n16_small = by_name["F17_mu16_t3_small_q"]["uncharged_ordered_pairs"]
    n16_large = by_name["F97_mu16_t3_large_q"]["uncharged_ordered_pairs"]
    check(
        "small-q warning is visible at n=16",
        n16_small > n16_large,
        f"F17={n16_small}, F97={n16_large}",
    )
    check(
        "at least one domain-wide row exceeds n^2 before activity filtering",
        any(row["uncharged_ordered_pairs"] > row["n_squared_budget"] for row in rows),
    )
    return {
        "node": "u1_alpha_active_core_incidence / u1_beta_band_trade_reduction",
        "task": "SP-CENSUS domain-wide split-pair census",
        "status": "EVIDENCE: exact toy census; domain-wide uncharged pairs can exceed n^2 at small q",
        "scope": "ordered disjoint split pairs Q,P in mu_n with e_i(Q)=e_i(P), 1<=i<=t, h in (t, floor(log2 n)^2]",
        "charged_classifier": "X-9 toral normal forms on mu_n: cyclic F(x^m) and dihedral F(x^m + alpha x^-m), exact fiber-union pairs",
        "rows": rows,
        "summary": {
            "rows_checked": [row["row"] for row in rows],
            "max_ordered_uncharged": max(row["uncharged_ordered_pairs"] for row in rows),
            "max_ordered_uncharged_over_n_squared": max(row["ordered_uncharged_over_n_squared"] for row in rows),
            "small_q_warning_n16": {
                "F17_mu16_t3_small_q": n16_small,
                "F97_mu16_t3_large_q": n16_large,
            },
            "rows_over_n_squared": [
                row["row"] for row in rows if row["uncharged_ordered_pairs"] > row["n_squared_budget"]
            ],
        },
        "checks": NCHECK,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    result = build_result()

    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")

    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as f:
            expected = json.load(f)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    print("\nrow summary:")
    for row in result["rows"]:
        print(
            f"{row['row']:22s} total={row['ordered_split_pairs']:<6d} "
            f"charged={row['charged_ordered_pairs']:<5d} "
            f"uncharged={row['uncharged_ordered_pairs']:<6d} "
            f"unch/n^2={row['ordered_uncharged_over_n_squared']:.4f}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS[:40]:
            print(f"  - {name}")
        if len(FAILS) > 40:
            print(f"  ... {len(FAILS) - 40} more")
        print("\nsummary:")
        print(json.dumps(result["summary"], indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} SP-CENSUS split-pair checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
