"""Exact finite branch arithmetic, not certification of source transport."""


def check(ok, message):
    if not ok:
        raise ValueError(message)


def verify(residual=(1016577, 1038635), total=274979661975561635):
    K, n, near = 1048576, 2097152, 134944
    paid = [(0, 793576, 273540953998915577),
            (793577, 878576, 270992495272115150),
            (878577, 1016576, 274929007493481160),
            (1038636, 1043775, 274979661975561635),
            (1043776, n, 100000000000134944)]
    intervals = sorted([(a, b) for a, b, _ in paid]+[residual])
    check(intervals[0][0] == 0 and intervals[-1][1] == n, "complete g domain")
    check(all(a <= b for a, b in intervals), "nonempty intervals")
    check(all(x[1]+1 == y[0] for x, y in zip(intervals, intervals[1:])),
          "disjoint exhaustive original-core partition")
    check((K-residual[1], K-residual[0]) == (9941, 31999), "unpaid child interval")
    check((K-1016576, K-878577) == (32000, 169999), "complete-core/high child transport")
    check((K-1043775, K-1038636) == (4801, 9940), "lower child transport")
    check(residual[1]-residual[0]+1 == 22059, "residual cardinality")
    check(30059-22059 == 39999-32000+1 == 8000, "new whole-source degree interval")
    check(total == max([value for _, _, value in paid]+[156765527508803240]),
          "maximum of whole-source bounds")
    budget = 2130706433**6//2**128
    check(budget == 274980728111395087, "original field budget")
    check(budget-total == 1066135833452, "original reserve")
    check(near == 2*67472 and 3*67472 <= K, "near theorem gate")
    check(2*500 < 67472, "canonical selection gate")


def main():
    verify()
    mutations = [((1016576, 1038635), 274979661975561635),
                 ((1016578, 1038635), 274979661975561635),
                 ((1016577, 1038634), 274979661975561635),
                 ((1016577, 1038636), 274979661975561635),
                 ((1016577, 1038635), 274979661975561634),
                 ((1016577, 1038635), 274979661975561636)]
    for residual, total in mutations:
        try:
            verify(residual, total)
        except ValueError:
            pass
        else:
            raise ValueError("accepted interval/budget mutation")
    verify_receiver_gates()
    print("PASS: exact original-g partition, child intervals, one near and field reserve")
    print("PASS: six boundary/budget mutations rejected; original rank-twelve residual J=9941..31999")
    print("The source bridge is a hand proof, not certified by this arithmetic check")


def verify_receiver_gates():
    def residual_fiber_gate(j, a):
        return 14000 <= j <= 31999 and a >= j-2000
    controls = ((14000, 12000, True), (14000, 11999, False),
                (13999, 13989, False), (25000, 24990, True),
                (10000, 9990, False), (31999, 29999, True),
                (31999, 29998, False), (32000, 30000, False),
                (9941, 9931, False), (52999, 52989, False),
                (53000, 52990, False))
    for j, a, expected in controls:
        check(residual_fiber_gate(j, a) == expected, "exact remaining receiver-fiber gate")
    check(max(248408859318207582, 272112051300507362) < 274979661975561635,
          "new source classes fit existing original maximum")
    print("PASS: eleven residual fiber-gate controls; J>=32000 handled by the whole interval")


if __name__ == "__main__":
    main()
