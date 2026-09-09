"""Exact two-parameter source prices and tiny affine-carrier controls."""

from fractions import Fraction as F


def need(ok, message):
    if not ok:
        raise ValueError(message)


def rank(rows):
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    pivot = 0
    for col in range(len(matrix[0])):
        selected = next((i for i in range(pivot, len(matrix)) if matrix[i][col] % 5), None)
        if selected is None:
            continue
        matrix[pivot], matrix[selected] = matrix[selected], matrix[pivot]
        inverse = pow(matrix[pivot][col] % 5, -1, 5)
        matrix[pivot] = [x*inverse % 5 for x in matrix[pivot]]
        for i in range(len(matrix)):
            if i != pivot:
                factor = matrix[i][col]
                matrix[i] = [(a-factor*b) % 5 for a, b in zip(matrix[i], matrix[pivot])]
        pivot += 1
    return pivot


def carrier_controls():
    pairs = [((a, 0, 1), (0, b, 1)) for a, b in ((0, 0), (1, 0), (0, 1), (1, 1))]
    for a0, b0 in pairs:
        first = [tuple((x-y) % 5 for x, y in zip(a, a0)) for a, b in pairs]
        second = [tuple((x-y) % 5 for x, y in zip(b, b0)) for a, b in pairs]
        need(rank(first+second) == 2 and rank([a+b for a, b in zip(first, second)]) == 2,
             "base-point invariant pair and shared ranks")
        need(max(rank(first), rank(second)) == 1, "maximum component rank undercharges the shared sum")
        need(rank(first+second+[b0]) == 3, "affine offset need not belong to the direction carrier")
    return len(pairs)


def bound(s, r, t, terminal):
    q = F(1)
    while r > s:
        excess = r-s
        need(67472-t+excess > 0 and s > 0, "guarded positive anchor")
        q *= F(1048576+excess, 67472-t+excess)
        r, s = r-2, s-1
    need((r, s) == terminal, "exact terminal ranks")
    if r == 0:
        return q
    c, p, h = F(528576, 67473-t), F(781095, 85474-t), F(1027079, 45975-t)
    need(1 <= c <= p and h <= p*p and h*p <= c**3, "both three-dimensional child gates")
    return q*c**3


def main():
    need(11 <= 9965 and 18 <= 2*9 and 17 <= 2*10, "auxiliary embeddings")
    expected = ((9, 18, (0, 0), [52853517316, 52860567481], 238911770855075395),
                (10, 17, (3, 3), [105235509453, 105251107155], 273174666855895812))
    for s, r, terminal, floors_expected, price in expected:
        total, floors = F(613022127444579907, 3), []
        for t in (1, 2):
            count = bound(s, r, t, terminal)
            floors.append(int(count))
            total += F(981104+t, t*(t+1))*count
        branch = int(total)+134944
        need(floors == floors_expected and branch == price, "exact shared-rank price")
        whole = branch if s == 9 else max(branch, 274138707278280353)
        need(whole < 274980728111395087, "strict original-source reserve")
        print("PASS shared/pair", (s, r), "PAIR FLOORS", floors, "BRANCH", branch, "WHOLE", whole)
    survivors = [(s, r) for s in range(12) for r in range(2*s+1)
                 if not (s <= 9 or (s <= 10 and r <= 17) or r <= 15)]
    need(survivors == [(10, r) for r in range(18, 21)]+[(11, r) for r in range(16, 23)], "exhaustive survivor alternatives")
    print("PASS", carrier_controls(), "base-point/offset controls; surviving rank pairs", survivors)
    print("Original source rank and V are unchanged; unrestricted rows and both Prizes remain open")


if __name__ == "__main__":
    main()
