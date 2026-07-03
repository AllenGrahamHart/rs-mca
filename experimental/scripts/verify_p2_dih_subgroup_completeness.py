#!/usr/bin/env python3
"""Verifier for the P2 dihedral subgroup-completeness packet.

The proof packet is intentionally conditional: the raw statement that every
2-power multiplicative domain has PGL2 stabilizer Dih_n is false over extension
fields.  This verifier pins the first wild subfield-circle exceptions and
nearby clean rows by exact ordered-triple enumeration.

Stdlib only.
Run: python3 experimental/scripts/verify_p2_dih_subgroup_completeness.py
To refresh the pinned certificate:
  python3 experimental/scripts/verify_p2_dih_subgroup_completeness.py --write-certificate
"""

from __future__ import annotations

from itertools import permutations
import json
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "p2-dih-subgroup-completeness",
    "p2_dih_subgroup_completeness.json",
)

INF = None
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


class GFp2:
    """F_{p^2}=F_p[t]/(t^2-g), represented by pairs u+v*t."""

    def __init__(self, p: int, nonsquare: int):
        self.p = p
        self.g = nonsquare % p
        self.q = p * p

    def add(self, a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return ((a[0] + b[0]) % self.p, (a[1] + b[1]) % self.p)

    def neg(self, a: tuple[int, int]) -> tuple[int, int]:
        return ((-a[0]) % self.p, (-a[1]) % self.p)

    def sub(self, a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return self.add(a, self.neg(b))

    def mul(self, a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return (
            (a[0] * b[0] + a[1] * b[1] * self.g) % self.p,
            (a[0] * b[1] + a[1] * b[0]) % self.p,
        )

    def inv(self, a: tuple[int, int]) -> tuple[int, int]:
        den = (a[0] * a[0] - a[1] * a[1] * self.g) % self.p
        if den == 0:
            raise ZeroDivisionError("zero inverse")
        den_inv = pow(den, self.p - 2, self.p)
        return (a[0] * den_inv % self.p, -a[1] * den_inv % self.p)

    def div(self, a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return self.mul(a, self.inv(b))

    def pow(self, a: tuple[int, int], exponent: int) -> tuple[int, int]:
        out = (1, 0)
        base = a
        while exponent:
            if exponent & 1:
                out = self.mul(out, base)
            base = self.mul(base, base)
            exponent >>= 1
        return out

    def elems(self) -> list[tuple[int, int]]:
        return [(u, v) for u in range(self.p) for v in range(self.p)]

    def generator(self) -> tuple[int, int]:
        for candidate in self.elems():
            if candidate == (0, 0):
                continue
            if all(self.pow(candidate, d) != (1, 0) for d in range(1, self.q - 1)):
                return candidate
        raise RuntimeError(f"no generator found for F_{self.q}")


def mu_subgroup(field: GFp2, n: int) -> list[tuple[int, int]]:
    gen = field.generator()
    omega = field.pow(gen, (field.q - 1) // n)
    return [field.pow(omega, i) for i in range(n)]


def tmap(field: GFp2, xs: tuple[tuple[int, int], ...], x):
    """Map xs[0],xs[1],xs[2] to infinity,0,1."""
    x1, x2, x3 = xs
    if x == x1:
        return INF
    scale = field.div(field.sub(x3, x1), field.sub(x3, x2))
    return field.mul(scale, field.div(field.sub(x, x2), field.sub(x, x1)))


def inv_tmap(field: GFp2, ys: tuple[tuple[int, int], ...], tau):
    """Inverse of the map sending ys[0],ys[1],ys[2] to infinity,0,1."""
    y1, y2, y3 = ys
    if tau is INF:
        return y1
    scale = field.div(field.sub(y3, y1), field.sub(y3, y2))
    den = field.sub(tau, scale)
    if den == (0, 0):
        return INF
    return field.div(field.sub(field.mul(tau, y1), field.mul(scale, y2)), den)


def mobius_image(field: GFp2, xs: tuple[tuple[int, int], ...], ys: tuple[tuple[int, int], ...], x):
    return inv_tmap(field, ys, tmap(field, xs, x))


def stabilizer_size_by_triples(field: GFp2, n: int) -> int:
    domain = mu_subgroup(field, n)
    domain_set = set(domain)
    source = tuple(domain[:3])
    count = 0
    for target in permutations(domain, 3):
        if {mobius_image(field, source, target, x) for x in domain} == domain_set:
            count += 1
    return count


def row(field_name: str, p: int, nonsquare: int, n: int, expected_stabilizer: int, kind: str) -> dict:
    field = GFp2(p, nonsquare)
    stabilizer_size = stabilizer_size_by_triples(field, n)
    dihedral_size = 2 * n
    wild_congruence = (n - 1) % p == 0
    check(
        f"{field_name} n={n}: stabilizer size",
        stabilizer_size == expected_stabilizer,
        f"|stab|={stabilizer_size}, expected={expected_stabilizer}",
    )
    if kind == "wild_subfield_circle":
        check(
            f"{field_name} n={n}: larger than dihedral",
            stabilizer_size > dihedral_size,
            f"|Dih|={dihedral_size}",
        )
        check(
            f"{field_name} n={n}: subfield-circle size p+1",
            n == p + 1 and expected_stabilizer == p * (p * p - 1),
            f"p={p}",
        )
    else:
        check(
            f"{field_name} n={n}: equals dihedral",
            stabilizer_size == dihedral_size,
            f"|Dih|={dihedral_size}",
        )
        check(
            f"{field_name} n={n}: easy tame congruence",
            not wild_congruence,
            f"p={p}, n-1={n - 1}",
        )
    return {
        "field": field_name,
        "n": n,
        "char": p,
        "kind": kind,
        "stabilizer_size": stabilizer_size,
        "dihedral_size": dihedral_size,
        "wild_congruence_p_divides_n_minus_1": wild_congruence,
    }


def main() -> None:
    rows = [
        row("F_9", 3, 2, 4, 24, "wild_subfield_circle"),
        row("F_25", 5, 2, 4, 8, "tame_dihedral"),
        row("F_25", 5, 2, 8, 16, "tame_dihedral"),
        row("F_49", 7, 3, 8, 336, "wild_subfield_circle"),
        row("F_49", 7, 3, 16, 32, "tame_dihedral"),
    ]
    result = {
        "node": "f_dih_subgroup_completeness",
        "task": "P2",
        "status": "CONDITIONAL: tame proof; wild subfield-circle domains are genuine exceptions",
        "named_condition": "p2_no_wild_subfield_circle_domain",
        "checks": NCHECK,
        "rows": rows,
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
        for name in FAILS:
            print("  -", name)
        sys.exit(1)

    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} P2 subgroup-completeness checks")


if __name__ == "__main__":
    main()
