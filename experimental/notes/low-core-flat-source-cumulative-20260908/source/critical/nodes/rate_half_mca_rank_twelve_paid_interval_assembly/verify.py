"""Exact finite branch arithmetic, not certification of source transport."""


def check(ok, message):
    if not ok:
        raise ValueError(message)


def verify(residual=(995577, 1038635), total=274979661975561635):
    K, n, near = 1048576, 2097152, 134944
    paid = [(0, 793576, 273540953998915577),
            (793577, 878576, 270992495272115150),
            (878577, 995576, 274929007493481160),
            (1038636, 1043775, 274979661975561635),
            (1043776, n, 100000000000134944)]
    intervals = sorted([(a, b) for a, b, _ in paid]+[residual])
    check(intervals[0][0] == 0 and intervals[-1][1] == n, "complete g domain")
    check(all(a <= b for a, b in intervals), "nonempty intervals")
    check(all(x[1]+1 == y[0] for x, y in zip(intervals, intervals[1:])),
          "disjoint exhaustive original-core partition")
    check((K-residual[1], K-residual[0]) == (9941, 52999), "unpaid child interval")
    check((K-995576, K-878577) == (53000, 169999), "contraction/high child transport")
    check((K-1043775, K-1038636) == (4801, 9940), "lower child transport")
    check(residual[1]-residual[0]+1 == 43059, "residual cardinality")
    check(total == max([value for _, _, value in paid]+[156765527508803240]),
          "maximum of whole-source bounds")
    budget = 2130706433**6//2**128
    check(budget == 274980728111395087, "original field budget")
    check(budget-total == 1066135833452, "original reserve")
    check(near == 2*67472 and 3*67472 <= K, "near theorem gate")
    check(2*500 < 67472, "canonical selection gate")


def main():
    verify()
    mutations = [((995576, 1038635), 274979661975561635),
                 ((995578, 1038635), 274979661975561635),
                 ((995577, 1038634), 274979661975561635),
                 ((995577, 1038636), 274979661975561635),
                 ((995577, 1038635), 274979661975561634),
                 ((995577, 1038635), 274979661975561636)]
    for residual, total in mutations:
        try:
            verify(residual, total)
        except ValueError:
            pass
        else:
            raise ValueError("accepted interval/budget mutation")
    print("PASS: exact original-g partition, child intervals, one near and field reserve")
    print("PASS: six boundary/budget mutations rejected; original rank-twelve residual J=9941..52999")
    print("The source bridge is a hand proof, not certified by this arithmetic check")


if __name__ == "__main__":
    main()
