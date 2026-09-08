"""Small finite-field transport controls and constant-size exact row arithmetic."""

from itertools import product


P = 11


def interpolate(points, values, x):
    total = 0
    for i, xi in enumerate(points):
        term = values[i]
        for j, xj in enumerate(points):
            if i != j:
                term = term * (x - xj) * pow((xi - xj) % P, -1, P) % P
        total = (total + term) % P
    return total


def contained(xs, values, k):
    if k == 0:
        return all(v == 0 for v in values)
    if len(xs) <= k:
        return True
    return all(interpolate(xs[:k], values[:k], x) == v
               for x, v in zip(xs[k:], values[k:]))


def bad_subset(agreement, r1, k, m):
    if len(agreement) < m:
        return None
    base = agreement[:k]
    bad = next((x for x in agreement[k:]
                if interpolate(base, [r1[y] for y in base], x) != r1[x]), None)
    if bad is None:
        return None
    support = base + [bad]
    support += [x for x in agreement if x not in support][:m - len(support)]
    assert len(support) == m and not contained(support, [r1[x] for x in support], k)
    return support


def transport_controls():
    domain, k, m = list(range(10)), 4, 5
    assigned = (set(range(5)), set(range(3, 8)), {0, 1, 7, 8, 9})
    records_checked = anchors_checked = exceptional_incidences = 0
    for roots, seed in product(((0, 1), (2, 5), (0, 5), (8, 9)), range(3)):
        c1 = [((x - roots[0]) * (x - roots[1])) % P for x in domain]
        c2 = [x * c1[x] % P for x in domain]
        offset = [(2 * x**3 + seed) % P for x in domain]
        dirs = ([0] * 10, c1, c2)
        r0, r1 = [], []
        for x in domain:
            owners = [j for j in range(3) if x in assigned[j]]
            if len(owners) == 2:
                i, j = owners
                v = (dirs[i][x] - dirs[j][x]) * pow((i - j) % P, -1, P) % P
            else:
                v = (x * x + seed + 1) % P
            i = owners[0]
            r1.append(v)
            r0.append((offset[x] + dirs[i][x] - i * v) % P)
        records = []
        for gamma in range(P):
            for a, b in product(range(P), repeat=2):
                h = [(offset[x] + a * c1[x] + b * c2[x]) % P for x in domain]
                agreement = [x for x in domain if (r0[x] + gamma * r1[x] - h[x]) % P == 0]
                support = bad_subset(agreement, r1, k, m)
                if support is not None:
                    records.append((gamma, h, support))
                    break
        assert records
        zeros = [x for x in domain if c1[x] == c2[x] == 0]
        g = sum(r1[x] == 0 and r0[x] == offset[x] for x in zeros)
        tau = sum(r1[x] != 0 for x in zeros)
        assert g + tau <= len(zeros) <= k - 2
        outside_load = sum(x not in zeros for _, _, support in records for x in support)
        assert (m - g) * len(records) <= outside_load + tau
        exceptional_incidences += sum(x in zeros and r1[x] != 0
                                     for _, _, support in records for x in support)
        for x in domain:
            if x in zeros:
                continue
            incident = [(gamma, h, support) for gamma, h, support in records if x in support]
            rest = [y for y in domain if y != x]
            basis = c1 if c1[x] else c2
            beta = r1[x] * pow(basis[x], -1, P) % P
            alpha = (r0[x] - offset[x]) * pow(basis[x], -1, P) % P
            b0 = [beta * basis[y] % P for y in domain]
            a0 = [(offset[y] + alpha * basis[y]) % P for y in domain]
            assert a0[x] == r0[x] and b0[x] == r1[x]
            rr0 = {y: (r0[y] - a0[y]) * pow((y - x) % P, -1, P) % P for y in rest}
            rr1 = {y: (r1[y] - b0[y]) * pow((y - x) % P, -1, P) % P for y in rest}
            other = c2 if basis is c1 else c1
            lam = other[x] * pow(basis[x], -1, P) % P
            kernel = {y: (other[y] - lam * basis[y]) * pow((y - x) % P, -1, P) % P for y in rest}
            pivot = next(y for y in rest if kernel[y])
            for gamma, h, support in incident:
                child = {y: (h[y] - a0[y] - gamma * b0[y]) * pow((y - x) % P, -1, P) % P for y in rest}
                assert contained(rest, [child[y] for y in rest], k - 1)
                multiple = child[pivot] * pow(kernel[pivot], -1, P) % P
                assert all(child[y] == multiple * kernel[y] % P for y in rest)
                child_support = [y for y in support if y != x]
                assert len(child_support) == m - 1
                assert all((rr0[y] + gamma * rr1[y] - child[y]) % P == 0 for y in child_support)
                assert not contained(child_support, [rr1[y] for y in child_support], k - 1)
                anchors_checked += 1
        records_checked += len(records)
    assert exceptional_incidences > 0
    return records_checked, anchors_checked, exceptional_incidences


def main():
    records, anchors, exceptions = transport_controls()
    base_witnesses = 0
    for k, m in ((0, 3), (1, 3), (2, 4), (4, 5)):
        n = 8
        r0 = [0] * (m - 1) + [(-j) % P for j in range(n - m + 1)]
        r1 = [0] * (m - 1) + [1] * (n - m + 1)
        for gamma in range(n - m + 1):
            support = [x for x in range(n) if (r0[x] + gamma * r1[x]) % P == 0]
            assert len(support) == m and not contained(support, [r1[x] for x in support], k)
            base_witnesses += 1
    envelopes = 0
    for r in range(1, 13):
        for d in range(1, r + 1):
            for k in range(1, 9):
                for s in range(1, k + 1):
                    for z in range(k - s + 1):
                        for g in range(z + 1):
                            for u in (1, 2, 7):
                                assert ((r + k - z) * u + z - g) * (d + s) <= (r + s) * u * (d + k - g)
                                envelopes += 1
    r, d, budget = 1048576, 67472, 274980728111395087
    u = 4070947
    expected = (63264449, 983145945, 15278131113, 237419535554,
                3689407679988, 57331172265517, 890879518951761,
                13843347021828845, 215108323408189165)
    for s, value in zip(range(2, 11), expected):
        num, den = (r + s) * u, d + s
        u = num // den
        assert u == value and den * u <= num < den * (u + 1)
    total = u + 2 * d
    assert total == 215108323408324109 < budget
    assert budget - total == 59872404703070978
    assert 254610000000134943 - total == 39501676591810834
    assert (r + 11) * u // (d + 11) == 3342468347844980987 > budget
    print(f'PASS: {records} actual selected records; {anchors} exact proper transports; '
          f'{exceptions} exceptional-zero incidences; {base_witnesses} rank-zero witnesses; '
          f'{envelopes} rational envelope controls; all nine cap integers. '
          f'Rank-eleven total {total}, slack {budget-total}; rank twelve NOT paid.')


if __name__ == '__main__':
    main()
