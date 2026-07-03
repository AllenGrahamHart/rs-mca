#!/usr/bin/env python3
"""H1 verifier: toy harness for u1_primitive_star_pte_bound (v1).

For small prime-field rows, exhaustively enumerate degree-A locators on
mu_n, group them by the top t locator coefficients, and for every base
locator in a same-top-t class compute the canonical star trades

    target = common core + P,     base = common core + Q.

The frozen W3 test asks that, after removing trades charged by some v1
pullback family, at most n^2 star trades survive from any base.  This harness
implements the explicit quotient and dihedral pullback filters and records the
stronger fact observed in these rows: even the raw per-base same-top-t list is
already below n^2.

Run:
  python3 experimental/scripts/verify_h1_u1_toy_harness.py
Refresh certificate:
  python3 experimental/scripts/verify_h1_u1_toy_harness.py --write-certificate
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
import json
import math
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "h1-u1-toy-harness",
    "h1_u1_toy_harness.json",
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


@dataclass(frozen=True)
class RowSpec:
    name: str
    p: int
    n: int
    A: int
    t: int


ROWS = (
    RowSpec("F17_mu8_A4_t3", 17, 8, 4, 3),
    RowSpec("F13_mu12_A5_t3", 13, 12, 5, 3),
    RowSpec("F13_mu12_A6_t3", 13, 12, 6, 3),
    RowSpec("F17_mu16_A6_t3", 17, 16, 6, 3),
    RowSpec("F17_mu16_A8_t3", 17, 16, 8, 3),
    RowSpec("F97_mu16_A8_t3", 97, 16, 8, 3),
    RowSpec("F41_mu20_A8_t3", 41, 20, 8, 3),
    RowSpec("F41_mu20_A10_t3", 41, 20, 10, 3),
    RowSpec("F97_mu24_A8_t3", 97, 24, 8, 3),
)


def factor_distinct(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    fac = factor_distinct(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in fac):
            return g
    raise RuntimeError(f"no primitive root mod {p}")


def mu_domain(p: int, n: int) -> list[int]:
    if (p - 1) % n != 0:
        raise ValueError(f"n={n} does not divide p-1={p - 1}")
    g = primitive_root(p)
    zeta = pow(g, (p - 1) // n, p)
    vals = [pow(zeta, i, p) for i in range(n)]
    if len(set(vals)) != n:
        raise RuntimeError(f"bad mu_{n} generator in F_{p}")
    return vals


def mask_from_comb(comb: tuple[int, ...]) -> int:
    out = 0
    for i in comb:
        out |= 1 << i
    return out


def exps_from_mask(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def elementary_signature(values: list[int], t: int, p: int) -> tuple[int, ...]:
    e = [0] * (t + 1)
    e[0] = 1
    for x in values:
        for r in range(t, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    return tuple(e[1:])


def mask_signature(mask: int, domain: list[int], t: int, p: int) -> tuple[int, ...]:
    return elementary_signature([domain[i] for i in range(len(domain)) if (mask >> i) & 1], t, p)


def transform_mask(mask: int, n: int, shift: int, inv: bool) -> int:
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            j = (-i if inv else i) + shift
            out |= 1 << (j % n)
    return out


def canonical_trade_key(P: int, Q: int, n: int) -> tuple[int, int]:
    images = []
    for inv in (False, True):
        for shift in range(n):
            images.append((transform_mask(P, n, shift, inv), transform_mask(Q, n, shift, inv)))
    return min(images)


def quotient_classes(n: int, M: int) -> list[int]:
    g = math.gcd(n, M)
    if g <= 1:
        return []
    step = n // g
    classes = []
    for r in range(step):
        mask = 0
        for j in range(g):
            mask |= 1 << ((r + j * step) % n)
        classes.append(mask)
    return classes


def dihedral_classes(n: int, M: int) -> list[int]:
    g = math.gcd(n, M)
    step = n // g
    seen = set()
    classes = []
    for r in range(step):
        if r in seen:
            continue
        residues = {r % step, (-r) % step}
        seen.update(residues)
        mask = 0
        for a in residues:
            for j in range(g):
                mask |= 1 << ((a + j * step) % n)
        classes.append(mask)
    return classes


def is_union_of_classes(mask: int, classes: list[int]) -> bool:
    if not classes:
        return False
    for cls in classes:
        hit = mask & cls
        if hit and hit != cls:
            return False
    return True


def v1_paid_partitions(n: int, t: int) -> list[tuple[str, list[int]]]:
    # W3 v1 degree window: deg psi in (t, floor(log2 n)^2].
    max_deg = int(math.log2(n)) ** 2
    out = []
    for M in range(t + 1, max_deg + 1):
        qclasses = quotient_classes(n, M)
        if qclasses:
            out.append((f"quotient:X^{M}", qclasses))
        dclasses = dihedral_classes(n, M)
        if dclasses:
            out.append((f"dihedral:X^{M}+X^-{M}", dclasses))
    return out


def v1_paid_reason(P: int, Q: int, partitions: list[tuple[str, list[int]]]) -> str | None:
    for reason, classes in partitions:
        if is_union_of_classes(P, classes) and is_union_of_classes(Q, classes):
            return reason
    return None


def analyze_row(row: RowSpec) -> dict[str, object]:
    domain = mu_domain(row.p, row.n)
    sig_cache: dict[int, tuple[int, ...]] = {}

    def sig(mask: int) -> tuple[int, ...]:
        if mask not in sig_cache:
            sig_cache[mask] = mask_signature(mask, domain, row.t, row.p)
        return sig_cache[mask]

    paid_partitions = v1_paid_partitions(row.n, row.t)
    paid_cache: dict[tuple[int, int], str | None] = {}

    def paid(P: int, Q: int) -> str | None:
        key = (P, Q)
        if key not in paid_cache:
            paid_cache[key] = v1_paid_reason(P, Q, paid_partitions)
        return paid_cache[key]

    groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for comb in combinations(range(row.n), row.A):
        mask = mask_from_comb(comb)
        groups[sig(mask)].append(mask)

    max_family_size = 0
    multi_classes = 0
    raw_star_trades = 0
    paid_star_trades = 0
    survivor_star_trades = 0
    max_raw_per_base = 0
    max_survivors_per_base = 0
    star_pte_failures = 0
    paid_reasons: dict[str, int] = defaultdict(int)
    worst = None

    for class_sig, masks in groups.items():
        max_family_size = max(max_family_size, len(masks))
        if len(masks) > 1:
            multi_classes += 1
        for base in masks:
            raw_here = 0
            paid_here = 0
            survivors_here = 0
            seen_trades = set()
            for target in masks:
                if target == base:
                    continue
                P = target & ~base
                Q = base & ~target
                key = (P, Q)
                if key in seen_trades:
                    continue
                seen_trades.add(key)
                raw_here += 1
                if sig(P) != sig(Q):
                    star_pte_failures += 1
                reason = paid(P, Q)
                if reason is None:
                    survivors_here += 1
                else:
                    paid_here += 1
                    paid_reasons[reason] += 1
            raw_star_trades += raw_here
            paid_star_trades += paid_here
            survivor_star_trades += survivors_here
            if raw_here > max_raw_per_base:
                max_raw_per_base = raw_here
            if survivors_here > max_survivors_per_base:
                max_survivors_per_base = survivors_here
                worst = {
                    "signature": list(class_sig),
                    "base": exps_from_mask(base, row.n),
                    "family_size": len(masks),
                    "raw_trades": raw_here,
                    "paid_trades": paid_here,
                    "survivors": survivors_here,
                    "survivor_representatives": [],
                }
                for target in masks:
                    if target == base:
                        continue
                    P = target & ~base
                    Q = base & ~target
                    if paid(P, Q) is None:
                        worst["survivor_representatives"].append(
                            {
                                "target": exps_from_mask(target, row.n),
                                "P": exps_from_mask(P, row.n),
                                "Q": exps_from_mask(Q, row.n),
                                "orbit_key": [
                                    exps_from_mask(canonical_trade_key(P, Q, row.n)[0], row.n),
                                    exps_from_mask(canonical_trade_key(P, Q, row.n)[1], row.n),
                                ],
                            }
                        )
                    if len(worst["survivor_representatives"]) >= 8:
                        break

    out = {
        "row": row.name,
        "p": row.p,
        "n": row.n,
        "A": row.A,
        "t": row.t,
        "subset_count": math.comb(row.n, row.A),
        "same_top_classes": len(groups),
        "multi_locator_classes": multi_classes,
        "max_family_size": max_family_size,
        "raw_star_trades": raw_star_trades,
        "paid_star_trades": paid_star_trades,
        "survivor_star_trades": survivor_star_trades,
        "max_raw_per_base": max_raw_per_base,
        "max_survivors_per_base": max_survivors_per_base,
        "n_squared_cap": row.n * row.n,
        "star_pte_failures": star_pte_failures,
        "paid_reasons": dict(sorted(paid_reasons.items())),
        "worst_base": worst,
    }
    check(
        f"{row.name}: star-PTE normal form replay",
        star_pte_failures == 0,
        f"trades={raw_star_trades}",
    )
    check(
        f"{row.name}: H1 survivor cap",
        max_survivors_per_base <= row.n * row.n,
        f"max survivors/base={max_survivors_per_base}, n^2={row.n * row.n}",
    )
    check(
        f"{row.name}: raw cap stronger than H1",
        max_raw_per_base <= row.n * row.n,
        f"max raw/base={max_raw_per_base}",
    )
    return out


def build_certificate() -> dict[str, object]:
    rows = [analyze_row(row) for row in ROWS]
    return {
        "task": "H1 U1 toy harness",
        "node": "u1_pullback_dichotomy",
        "dictionary": "w3_chargeable_dictionary_grammar.md v1",
        "rows": rows,
        "max_survivors_per_base": max(row["max_survivors_per_base"] for row in rows),
        "max_raw_per_base": max(row["max_raw_per_base"] for row in rows),
        "verdict": "PASS: every checked base has <= n^2 v1-uncharged star trades",
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    cert = build_certificate()
    check(
        "H1 aggregate survivor cap",
        all(row["max_survivors_per_base"] <= row["n_squared_cap"] for row in cert["rows"]),
        f"max survivors/base={cert['max_survivors_per_base']}",
    )
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(cert, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")
    if FAILS:
        print("\nFAILURES:")
        for f in FAILS:
            print(f"  - {f}")
        return 1
    print(f"\nAll {NCHECK} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
