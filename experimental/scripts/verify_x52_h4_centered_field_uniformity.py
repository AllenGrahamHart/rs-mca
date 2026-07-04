#!/usr/bin/env python3
"""X52 h=4 centered field-uniform quotient shell reduction.

X48-X50 were introduced with prime-field replay rows, but their algebra only
needs a cyclic multiplicative subgroup H of even order n in a field of odd
characteristic.  This verifier exercises the same identities in quadratic
extension fields where mu_n is not contained in the prime field.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import json
import math
import os
import sys
from typing import Any, Iterable

import verify_x50_h4_centered_threshold as x50


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x52-h4-centered-field-uniformity",
    "x52_h4_centered_field_uniformity.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

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
        "x48_h4_centered_coset_shell_param": "PROVED",
        "x49_h4_centered_quotient_energy": "PROVED",
        "x50_h4_centered_threshold": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def factor_distinct(value: int) -> list[int]:
    out = []
    d = 2
    while d * d <= value:
        if value % d == 0:
            out.append(d)
            while value % d == 0:
                value //= d
        d += 1 if d == 2 else 2
    if value > 1:
        out.append(value)
    return out


@dataclass(frozen=True)
class Fp2Field:
    p: int
    nonsquare: int

    def element(self, a: int, b: int = 0) -> tuple[int, int]:
        return (a % self.p, b % self.p)

    def add(self, x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        return ((x[0] + y[0]) % self.p, (x[1] + y[1]) % self.p)

    def sub(self, x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        return ((x[0] - y[0]) % self.p, (x[1] - y[1]) % self.p)

    def mul(self, x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        return (
            (x[0] * y[0] + self.nonsquare * x[1] * y[1]) % self.p,
            (x[0] * y[1] + x[1] * y[0]) % self.p,
        )

    def pow(self, x: tuple[int, int], exponent: int) -> tuple[int, int]:
        if exponent < 0:
            x = self.inv(x)
            exponent = -exponent
        out = self.one
        base = x
        while exponent:
            if exponent & 1:
                out = self.mul(out, base)
            base = self.mul(base, base)
            exponent >>= 1
        return out

    def inv(self, x: tuple[int, int]) -> tuple[int, int]:
        den = (x[0] * x[0] - self.nonsquare * x[1] * x[1]) % self.p
        if den == 0:
            raise ZeroDivisionError(x)
        inv_den = pow(den, -1, self.p)
        return ((x[0] * inv_den) % self.p, (-x[1] * inv_den) % self.p)

    @property
    def zero(self) -> tuple[int, int]:
        return (0, 0)

    @property
    def one(self) -> tuple[int, int]:
        return (1, 0)

    @property
    def q(self) -> int:
        return self.p * self.p

    def elements(self) -> Iterable[tuple[int, int]]:
        for a in range(self.p):
            for b in range(self.p):
                yield (a, b)

    def nonzero_elements(self) -> list[tuple[int, int]]:
        return [x for x in self.elements() if x != self.zero]

    def primitive(self) -> tuple[int, int]:
        order = self.q - 1
        factors = factor_distinct(order)
        for candidate in self.nonzero_elements():
            if all(self.pow(candidate, order // fac) != self.one for fac in factors):
                return candidate
        raise RuntimeError(f"no primitive element in GF({self.q})")

    def subgroup(self, n: int) -> list[tuple[int, int]]:
        if (self.q - 1) % n:
            raise ValueError(f"n={n} does not divide q-1={self.q - 1}")
        gen = self.primitive()
        zeta = self.pow(gen, (self.q - 1) // n)
        out = [self.pow(zeta, i) for i in range(n)]
        if len(set(out)) != n:
            raise RuntimeError(f"constructed subgroup has {len(set(out))} elements")
        return out


def pair_sum(field: Fp2Field, pair: tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int]:
    return field.add(pair[0], pair[1])


def direct_shells(
    field: Fp2Field, subgroup: list[tuple[int, int]]
) -> dict[tuple[int, int], list[tuple[tuple[int, int], tuple[int, int]]]]:
    shells: dict[tuple[int, int], list[tuple[tuple[int, int], tuple[int, int]]]] = defaultdict(list)
    for i, x in enumerate(subgroup):
        for y in subgroup[i + 1 :]:
            s = field.add(x, y)
            if s != field.zero:
                shells[s].append((x, y))
    return shells


def quotient_shells(field: Fp2Field, subgroup: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    n = len(subgroup)
    one = field.one
    counts: Counter[tuple[int, int]] = Counter()
    for r in subgroup:
        if r == one:
            continue
        shifted = field.add(one, r)
        if shifted == field.zero:
            continue
        counts[field.pow(shifted, n)] += 1
    return {coset_key: count // 2 for coset_key, count in counts.items()}


def row_report(label: str, field: Fp2Field, n: int) -> dict[str, Any]:
    subgroup = field.subgroup(n)
    subgroup_set = set(subgroup)
    shells = direct_shells(field, subgroup)
    quotient = quotient_shells(field, subgroup)
    q = field.q
    threshold = x50.exact_threshold(n)

    check(f"{label}: subgroup has order n", len(subgroup_set) == n)
    check(f"{label}: subgroup is not contained in prime field", any(x[1] != 0 for x in subgroup))
    check(f"{label}: n-th power kernel is H", sum(1 for x in field.nonzero_elements() if field.pow(x, n) == field.one) == n)

    inconsistent_cosets: dict[str, list[int]] = {}
    by_coset: dict[tuple[int, int], list[int]] = defaultdict(list)
    for s, entries in shells.items():
        by_coset[field.pow(s, n)].append(len(entries))
    for coset_key, values in by_coset.items():
        if len(set(values)) != 1:
            inconsistent_cosets[str(coset_key)] = values

    direct_hist = Counter(len(entries) for entries in shells.values())
    quotient_hist = Counter(quotient.values())
    quotient_mass = sum(quotient.values())
    quotient_energy = n * sum(math.comb(value, 4) for value in quotient.values() if value >= 4)
    max_shell = max(quotient.values(), default=0)
    bound = x50.centered_bound(n, max_shell)
    ratio_counts_even = all(
        sum(
            1
            for r in subgroup
            if r != field.one
            and field.add(field.one, r) != field.zero
            and field.pow(field.add(field.one, r), n) == coset_key
        )
        == 2 * shell_size
        for coset_key, shell_size in quotient.items()
    )

    check(f"{label}: direct shells are coset-constant", not inconsistent_cosets)
    check(f"{label}: quotient mass is (n-2)/2", quotient_mass == (n - 2) // 2, f"mass={quotient_mass}")
    check(
        f"{label}: quotient shell histogram matches direct coset histogram",
        sorted(quotient.values()) == sorted(values[0] for values in by_coset.values()),
    )
    check(f"{label}: quotient ratio counts are twice shell sizes", ratio_counts_even)
    check(f"{label}: X49 energy identity holds", quotient_energy == sum(math.comb(len(v), 4) for v in shells.values() if len(v) >= 4))
    check(f"{label}: measured shell maximum fits X50 threshold", max_shell <= threshold, f"M={max_shell}, T={threshold}")
    check(f"{label}: measured X50 bound fits n^3", bound <= n**3)

    return {
        "label": label,
        "field": f"GF({field.p}^2)",
        "p": field.p,
        "q": q,
        "n": n,
        "quotient_cosets": (q - 1) // n,
        "nonzero_pair_sum_values": len(shells),
        "direct_shell_size_histogram": {str(k): v for k, v in sorted(direct_hist.items())},
        "quotient_shell_size_histogram": {str(k): v for k, v in sorted(quotient_hist.items())},
        "quotient_shell_mass": quotient_mass,
        "expected_shell_mass": (n - 2) // 2,
        "max_shell_size": max_shell,
        "exact_threshold": threshold,
        "x49_quotient_energy": quotient_energy,
        "x50_bound_fraction": f"{bound.numerator}/{bound.denominator}",
        "x50_bound_ceiling": (bound.numerator + bound.denominator - 1) // bound.denominator,
        "n_cubed": n**3,
        "inconsistent_cosets": inconsistent_cosets,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    rows = [
        row_report("GF25_mu8", Fp2Field(5, 2), 8),
        row_report("GF49_mu16", Fp2Field(7, 3), 16),
        row_report("GF121_mu24", Fp2Field(11, 2), 24),
    ]
    check("all extension rows satisfy X50 threshold", all(row["max_shell_size"] <= row["exact_threshold"] for row in rows))
    check("some extension row has a non-prime-field subgroup", all(row["q"] != row["p"] for row in rows))
    return {
        "task": "X52 h=4 centered field-uniformity",
        "node": "active_core_count_bound",
        "status": "PROVED FIELD-UNIFORM EXTENSION OF X48-X50",
        "theorem": (
            "Let F be any field of odd characteristic and H <= F^* be cyclic of even order n. "
            "For s != 0, unordered H-pairs with sum s are in two-to-one correspondence with "
            "ratios r in H\\{1} satisfying 1+r in sH.  Hence shell sizes are constant on "
            "F^*/H-cosets.  If F is finite, the n-th power map has kernel H, so the quotient "
            "coset can be represented by s^n.  X49's quotient energy and X50's threshold are "
            "therefore field-uniform, not prime-field artifacts."
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

    print("\nfield-uniform rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: q={row['q']} n={row['n']} "
            f"cosets={row['quotient_cosets']} M={row['max_shell_size']} "
            f"T={row['exact_threshold']} energy={row['x49_quotient_energy']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X52 h4 field-uniformity checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
