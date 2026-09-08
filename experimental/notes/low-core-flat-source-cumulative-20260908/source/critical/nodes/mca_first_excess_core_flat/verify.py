"""Small actual polynomial controls for the least excess rank and its caps."""

import importlib.util
from itertools import combinations
from pathlib import Path

path = Path(__file__).resolve().parents[1]/"mca_balanced_basis_under_flat_density/verify.py"
spec = importlib.util.spec_from_file_location("balanced_controls", path)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
need, rank = b.need, b.rank


def excess(n, s, t, size):
    return 1 <= t <= s-2 and (s-t)*size > n


def selected(n, k, s, t, inside, flats, rows, p):
    need(excess(n, s, t, len(inside)), "strict excess")
    need(rank([rows[i] for i in inside], p) == t, "spanned complete flat")
    need(len(inside) <= k-s+t, "polynomial root capacity")
    need(all(len(a) <= n//(s-j) for j, a in flats if j < t),
         "ALL lower-rank flat caps from minimality")


def actual(p, k, points, polys, expected_rank, deficient=False):
    rows = b.c.rows_for(polys, points, p)
    n, s = len(rows), len(polys)
    need(n > k >= s >= 3 and rank(rows, p) == s
         and all(any(row) for row in rows), "actual nonzero polynomial source")
    flats = set()
    for t in range(1, s-1):
        for chosen in combinations(range(n), t):
            basis = [rows[i] for i in chosen]
            if rank(basis, p) != t:
                continue
            inside = tuple(i for i, row in enumerate(rows) if rank(basis+[row], p) == t)
            flats.add((t, inside))
    choices = sorted((t, a) for t, a in flats if excess(n, s, t, len(a)))
    basis_count, bound = b.c.basis_count(rows, p, s), b.product(n-k, k, s)
    need(basis_count >= bound or choices, "balanced count or first excess")
    need((choices[0][0] if choices else None) == expected_rank, "declared least rank")
    if deficient:
        need(basis_count < bound, "actual deficient product")
    mutations = 0
    if choices:
        first_rank = choices[0][0]
        for t, inside in choices:
            if t == first_rank:
                selected(n, k, s, t, inside, flats, rows, p)
            else:
                try:
                    selected(n, k, s, t, inside, flats, rows, p)
                except ValueError:
                    mutations += 1
                else:
                    raise ValueError("nonminimal excess rank accepted")
    print("PASS actual", (p, k, n, s), "bases", basis_count, "product", bound,
          "complete spanned flats", len(flats), "first rank", expected_rank,
          "nonminimal choices rejected", mutations)
    return basis_count >= bound, bool(choices), mutations


def main():
    mono = lambda k, powers: [tuple(int(i == v) for i in range(k)) for v in powers]
    actual(17, 4, list(range(9)), mono(4, range(4)), None)
    actual(23, 7, [x % 23 for x in range(-8, 9) if x], mono(7, (0, 2, 4, 6)), None)
    loc = b.c.locator(range(10), 17)
    p3 = [[1]+[0]*11, loc+[0], [0]+loc]
    actual(17, 12, list(range(13)), p3, 1, True)
    p4 = [[1]+[0]*12]+[[0]*i+loc+[0]*(2-i) for i in range(3)]
    _, _, mutations = actual(17, 13, list(range(14)), p4, 1, True)
    both = actual(17, 12, list(range(13)), [p3[0], [0, 1]+[0]*10, p3[1], p3[2]], 2)
    need(both[:2] == (True, True) and mutations > 0, "overlap and minimality exercised")
    for n, s, t in ((12, 4, 1), (13, 4, 2), (95466, 11, 7)):
        floor = n//(s-t)
        need(not excess(n, s, t, floor) and excess(n, s, t, floor+1), "strict integer onset")
    need(not excess(12, 4, 3, 100) and not excess(12, 4, 0, 100), "permitted rank range")
    print("PASS five actual controls, nonexclusive alternative and strict-boundary mutations")
    print("Spanned-flat controls supplement the universal hand proof; no received-line census")


if __name__ == "__main__":
    main()
