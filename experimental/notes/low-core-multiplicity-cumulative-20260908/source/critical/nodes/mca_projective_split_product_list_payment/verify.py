"""Tiny exact controls, not a certificate of the universal geometry."""

from math import comb


def require(ok, label):
    if not ok:
        raise ValueError(label)


def case_bounds(s, exponent, n, degree_bound, agreement):
    require(s >= 1 and exponent >= 1, "positive dimension/exponent")
    require(s <= degree_bound <= agreement <= n, "list range")
    q_floor = (n - degree_bound + 1) // (agreement - degree_bound + 1)
    return (
        comb(2 * s, s) * exponent**s,
        comb(2 * s - 1, s - 1) * exponent**s,
        comb(2 * s - 1, s) * exponent**s,
        q_floor * comb(2 * s - 2, s - 1) * exponent ** (s - 1),
    )


def multiply(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] = (out[i + j] + a * b) % 7
    return tuple(out)


def product(f, g):
    return multiply(f, multiply(g, multiply(g, g)))


def controls():
    rhs = {
        (0, 0): (0, 0, 0, 0, 1),
        (1, 0): (0, 0, 0, 1, 1),
        (0, 1): (0, 1, 3, 3, 1),
        (1, 1): (1, 4, 6, 4, 1),
    }
    found = {}
    for offsets, target in rhs.items():
        found[offsets] = [
            (a, b) for a in range(7) for b in range(7)
            if product((offsets[0], a), (offsets[1], b)) == target
        ]
    require({key: len(value) for key, value in found.items()} ==
            {(0, 0): 6, (1, 0): 3, (0, 1): 1, (1, 1): 1},
            "four affine-scaling controls")
    receiver = [(0, 0)]
    for t in range(1, 7):
        mu = 1 if t <= 3 else 2
        receiver.append((pow(mu, -3, 7) * t % 7, mu * t % 7))
    rich = [
        (a, b) for a, b in found[0, 0]
        if sum((a * t % 7, b * t % 7) == receiver[t]
               for t in range(7)) >= 4
    ]
    require(len(rich) == 2 and case_bounds(1, 3, 7, 2, 4)[3] == 2,
            "common-zero per-class incidence is sharp")
    pole_pairs = [
        (a, b) for a in range(7) for b in range(7)
        if product((1, 0, a), (0, b)) == (0, 0, 0, 1, 0, 1)
    ]
    require(len(pole_pairs) == 3, "rational offset retains original pairs")


def verify():
    for j in (4801, 8656, 9526, 169999):
        bounds = case_bounds(11, 3, 1048576 + j, j, 66972 + j)
        require(bounds == (124965162504, 62482581252, 62482581252,
                           163644855660), "finite four-case bounds")
    require(1048577 // 66973 == 15, "integer per-class cap")
    base = 23067643444721720934 // 5500 + 134944
    total = base + 981604 * (max(bounds) + 64)
    budget = 2130706433**6 // 2**128
    require(base == 4194116990084347, "single HIGH and near base")
    require(total == 164828561948185643, "source total including off-curve")
    require(budget - total == 110152166163209444, "positive exact reserve")
    require(total < 274979661975561635 < budget, "kernel alternative")
    old_pairs = 4**21 * 1048577 // 66973
    require(base + 981604 * old_pairs == 67596414259023532871 > budget,
            "old generic degree price fails even without exceptions")
    for args in ((0, 3, 7, 2, 4), (1, 0, 7, 2, 4),
                 (1, 3, 7, 5, 4), (1, 3, 7, 2, 8)):
        try:
            case_bounds(*args)
        except ValueError:
            continue
        raise ValueError("invalid list contract accepted")
    controls()
    print("PASS: four offset bounds, exact LOW/HIGH/near ledger, five F7 controls")
    print("PASS: four invalid arithmetic contracts rejected; geometry is hand-proved")


if __name__ == "__main__":
    verify()
