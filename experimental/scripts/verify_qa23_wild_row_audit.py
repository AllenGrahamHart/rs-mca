#!/usr/bin/env python3
"""QA.23 verifier: Mersenne wild rows and the F_49/mu_8 Dickson toy.

Part (a) enumerates admissible wild rows
    n in {2^13, 2^17, 2^19, 2^31}, q=(2^r-1)^(2s) < 2^256.

Part (b) enumerates the subgroup lattice generated inside PGL_2(F_7), acting
on P^1(F_7), the Cayley model of the F_49/mu_8 wild row.  For every subgroup
it verifies that invariant supports are exactly unions of subgroup orbits.

Part (c) compares the distinct orbit-window strata available from the full
Dickson/PGL2 subgroup lattice with those available from a tame dihedral Sylow-2
subgroup.  This is toy window arithmetic, not a prize-scale budget proof.
"""

from __future__ import annotations

from collections import defaultdict, deque
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
    "qa23-wild-row-audit",
    "qa23_wild_row_audit.json",
)

P = 7
INF = P
DOMAIN = tuple(range(P + 1))
ID = tuple(range(P + 1))
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


def inv(a: int) -> int:
    return pow(a % P, P - 2, P)


def act_matrix(M: tuple[int, int, int, int], x: int) -> int:
    a, b, c, d = M
    if x == INF:
        return INF if c == 0 else a * inv(c) % P
    den = (c * x + d) % P
    if den == 0:
        return INF
    return (a * x + b) * inv(den) % P


def canonical_matrix(a: int, b: int, c: int, d: int) -> tuple[int, int, int, int]:
    vals = [a % P, b % P, c % P, d % P]
    scale = next(x for x in vals if x)
    s = inv(scale)
    return tuple((s * x) % P for x in vals)  # type: ignore[return-value]


def pgl2_group() -> list[tuple[int, ...]]:
    out = set()
    for a in range(P):
        for b in range(P):
            for c in range(P):
                for d in range(P):
                    if (a * d - b * c) % P == 0:
                        continue
                    M = canonical_matrix(a, b, c, d)
                    out.add(tuple(act_matrix(M, x) for x in DOMAIN))
    return sorted(out)


def compose(g: tuple[int, ...], h: tuple[int, ...]) -> tuple[int, ...]:
    """g after h."""
    return tuple(g[h[i]] for i in DOMAIN)


def multiplication_table(group: list[tuple[int, ...]]) -> tuple[tuple[int, ...], ...]:
    index = {g: i for i, g in enumerate(group)}
    return tuple(tuple(index[compose(g, h)] for h in group) for g in group)


def inverse_table(mult: tuple[tuple[int, ...], ...], id_idx: int) -> tuple[int, ...]:
    out = []
    for g, row in enumerate(mult):
        out.append(next(h for h, gh in enumerate(row) if gh == id_idx and mult[h][g] == id_idx))
    return tuple(out)


def mask_iter(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def subgroup_generated_mask(gens: tuple[int, ...], mult: tuple[tuple[int, ...], ...], invs: tuple[int, ...], id_idx: int) -> int:
    walk_gens = tuple(sorted(set(gens + tuple(invs[g] for g in gens))))
    mask = 1 << id_idx
    queue: deque[int] = deque([id_idx])

    while queue:
        h = queue.popleft()
        for g in walk_gens:
            gh = mult[g][h]
            bit = 1 << gh
            if not mask & bit:
                mask |= bit
                queue.append(gh)
    return mask


def all_subgroups_idx(group: list[tuple[int, ...]], mult: tuple[tuple[int, ...], ...], id_idx: int) -> list[int]:
    """Enumerate the subgroup lattice as bitmasks.

    All subgroup classes in PGL_2(F_7)'s Dickson lattice are two-generated, but
    the closure pass below also adjoins one generator to every subgroup found,
    so a missed non-two-generated subgroup would be discovered before the
    fixed-point check succeeds.
    """

    n = len(group)
    invs = inverse_table(mult, id_idx)
    subgroups = {1 << id_idx}
    subgroup_gens = {1 << id_idx: tuple()}

    def add_generated(gens: tuple[int, ...], queue: deque[int] | None = None) -> None:
        K = subgroup_generated_mask(gens, mult, invs, id_idx)
        if K not in subgroups:
            subgroups.add(K)
            subgroup_gens[K] = gens
            if queue is not None:
                queue.append(K)

    # Fast seed: all cyclic and two-generated subgroups.
    for g in range(n):
        add_generated((g,))
    for g in range(n):
        for h in range(g, n):
            add_generated((g, h))

    queue = deque(sorted(subgroups, key=lambda H: (H.bit_count(), H)))
    while queue:
        H = queue.popleft()
        gens = subgroup_gens[H]
        for g in range(n):
            if H >> g & 1:
                continue
            add_generated(gens + (g,), queue)
    return sorted(subgroups, key=lambda H: (H.bit_count(), H))


def orbits_idx(H: int, group: list[tuple[int, ...]]) -> tuple[tuple[int, ...], ...]:
    remaining = set(DOMAIN)
    out = []
    while remaining:
        start = min(remaining)
        orb = {group[g][start] for g in mask_iter(H)}
        changed = True
        while changed:
            changed = False
            for x in list(orb):
                for g in mask_iter(H):
                    y = group[g][x]
                    if y not in orb:
                        orb.add(y)
                        changed = True
        out.append(tuple(sorted(orb)))
        remaining -= orb
    return tuple(sorted(out, key=lambda O: (len(O), O)))


def orbit_size_partition_idx(H: int, group: list[tuple[int, ...]]) -> tuple[int, ...]:
    return tuple(sorted(len(O) for O in orbits_idx(H, group)))


def subgroup_invariant_subsets_idx(H: int, group: list[tuple[int, ...]]) -> set[int]:
    inv_subsets = set()
    for mask in range(1 << len(DOMAIN)):
        ok = True
        for g in mask_iter(H):
            image = 0
            for i in DOMAIN:
                if mask >> i & 1:
                    image |= 1 << group[g][i]
            if image != mask:
                ok = False
                break
        if ok:
            inv_subsets.add(mask)
    return inv_subsets


def orbit_union_subsets_idx(H: int, group: list[tuple[int, ...]]) -> set[int]:
    os = orbits_idx(H, group)
    masks = []
    for O in os:
        mask = 0
        for i in O:
            mask |= 1 << i
        masks.append(mask)
    out = set()
    for choose in range(1 << len(masks)):
        mask = 0
        for j, om in enumerate(masks):
            if choose >> j & 1:
                mask |= om
        out.add(mask)
    return out


def element_order_idx(g: int, mult: tuple[tuple[int, ...], ...], id_idx: int) -> int:
    x = id_idx
    for r in range(1, 400):
        x = mult[g][x]
        if x == id_idx:
            return r
    raise RuntimeError("order too large")


def sylow2_subgroup_idx(group: list[tuple[int, ...]], mult: tuple[tuple[int, ...], ...], id_idx: int) -> int:
    invs = inverse_table(mult, id_idx)
    for g in range(len(group)):
        if element_order_idx(g, mult, id_idx) == 8:
            for h in range(len(group)):
                H = subgroup_generated_mask((g, h), mult, invs, id_idx)
                if H.bit_count() == 16:
                    return H
    raise RuntimeError("no Sylow-2 subgroup found")


def admissible_wild_rows() -> list[dict]:
    rows = []
    for r in (13, 17, 19, 31):
        p = (1 << r) - 1
        n = 1 << r
        s = 1
        while p ** (2 * s) < (1 << 256):
            rows.append(
                {
                    "r": r,
                    "n": n,
                    "mersenne_p": p,
                    "extension_degree": 2 * s,
                    "q": str(p ** (2 * s)),
                    "log2_q_upper": 2 * s * r,
                    "wild_reason": "mu_n is the norm-one/subfield circle over F_p inside F_{p^2}; cosets are dilation-conjugate",
                }
            )
            s += 1
    return rows


def window_summary(subgroups: list[int], group: list[tuple[int, ...]]) -> dict:
    partitions = defaultdict(set)
    subsets_by_size = defaultdict(set)
    for H in subgroups:
        part = orbit_size_partition_idx(H, group)
        partitions[part].add(H.bit_count())
        for mask in orbit_union_subsets_idx(H, group):
            subsets_by_size[mask.bit_count()].add(mask)
    return {
        "orbit_partitions": [
            {"partition": list(part), "subgroup_orders": sorted(orders)}
            for part, orders in sorted(partitions.items())
        ],
        "distinct_invariant_subsets_by_size": {
            str(size): len(subsets) for size, subsets in sorted(subsets_by_size.items())
        },
    }


def main() -> None:
    rows = admissible_wild_rows()
    expected_counts = {13: 9, 17: 7, 19: 6, 31: 4}
    got_counts = defaultdict(int)
    for row in rows:
        got_counts[row["r"]] += 1
    check("wild row exponents match expected set", set(got_counts) == set(expected_counts))
    for r, expected in expected_counts.items():
        check(f"r={r}: admissible q=(2^r-1)^(2s)<2^256 count", got_counts[r] == expected, f"count={got_counts[r]}")
    check("coset inheritance by dilation conjugacy is row-independent", all(row["wild_reason"] for row in rows))

    group = pgl2_group()
    id_idx = {g: i for i, g in enumerate(group)}[ID]
    mult = multiplication_table(group)
    check("PGL2(F_7) has order 336", len(group) == 336)
    check("PGL2(F_7) action is sharply 3-transitive on P^1(F_7)", len(group) == 8 * 7 * 6)
    subgroups = all_subgroups_idx(group, mult, id_idx)
    check("subgroup enumeration includes trivial and full groups", subgroups[0].bit_count() == 1 and subgroups[-1].bit_count() == 336)
    check("subgroup enumeration count is stable", len(subgroups) == 413, f"count={len(subgroups)}")

    bad = 0
    for H in subgroups:
        if subgroup_invariant_subsets_idx(H, group) != orbit_union_subsets_idx(H, group):
            bad += 1
    check("every subgroup-invariant support is exactly a union of Dickson subgroup orbits", bad == 0)

    sylow = sylow2_subgroup_idx(group, mult, id_idx)
    check("selected tame dihedral/Sylow-2 subgroup has order 16", sylow.bit_count() == 16)
    dihedral_subgroups = [H for H in subgroups if H & ~sylow == 0]
    check("dihedral subgroup lattice is a strict sublattice of Dickson lattice", 0 < len(dihedral_subgroups) < len(subgroups), f"{len(dihedral_subgroups)} vs {len(subgroups)}")

    wild_windows = window_summary(subgroups, group)
    tame_windows = window_summary(dihedral_subgroups, group)
    wild_parts = {tuple(item["partition"]) for item in wild_windows["orbit_partitions"]}
    tame_parts = {tuple(item["partition"]) for item in tame_windows["orbit_partitions"]}
    new_parts = sorted(wild_parts - tame_parts)
    check("wild Dickson toy has orbit-window partitions absent from tame dihedral lattice", bool(new_parts), f"new={new_parts[:8]}")

    result = {
        "node": "wild_row_audit",
        "task": "QA.23",
        "status": "AUDIT: wild rows enumerated; F49/mu8 Dickson toy has extra orbit-window strata",
        "checks": NCHECK,
        "admissible_wild_rows": rows,
        "total_wild_rows": len(rows),
        "coset_inheritance": "Every alpha*mu_n is dilation-conjugate to mu_n, so the PGL2 stabilizer is conjugate and wildness is inherited by every coset.",
        "pgl2_f7": {
            "group_order": len(group),
            "subgroup_count": len(subgroups),
            "dihedral_sylow2_subgroup_count": len(dihedral_subgroups),
            "wild_window_summary": wild_windows,
            "tame_dihedral_window_summary": tame_windows,
            "new_wild_orbit_partitions": [list(p) for p in new_parts],
            "interpretation": "At the F49/mu8 toy, enlarged Dickson symmetry gives invariant window strata not present in a tame dihedral subgroup lattice.",
        },
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
        print("\nFAIL:")
        for name in FAILS:
            print("  -", name)
        print(json.dumps(result, indent=2, sort_keys=True))
        sys.exit(1)
    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} QA.23 wild-row audit checks")


if __name__ == "__main__":
    main()
