"""Exact finite branch arithmetic, not certification of source transport."""


def check(ok, message):
    if not ok:
        raise ValueError(message)


def verify(residual=(1018577, 1038635), total=274979661975561635):
    K, n, near = 1048576, 2097152, 134944
    paid = [(0, 793576, 273540953998915577),
            (793577, 878576, 270992495272115150),
            (878577, 1018576, 274929007493481160),
            (1038636, 1043775, 274979661975561635),
            (1043776, n, 100000000000134944)]
    intervals = sorted([(a, b) for a, b, _ in paid]+[residual])
    check(intervals[0][0] == 0 and intervals[-1][1] == n, "complete g domain")
    check(all(a <= b for a, b in intervals), "nonempty intervals")
    check(all(x[1]+1 == y[0] for x, y in zip(intervals, intervals[1:])),
          "disjoint exhaustive original-core partition")
    check((K-residual[1], K-residual[0]) == (9941, 29999), "unpaid child interval")
    check((K-1018576, K-878577) == (30000, 169999), "refined quotient-density/high child transport")
    check((K-1043775, K-1038636) == (4801, 9940), "lower child transport")
    check(residual[1]-residual[0]+1 == 20059, "residual cardinality")
    check(22059-20059 == 31999-30000+1 == 2000, "new whole-source degree interval")
    check(total == max([value for _, _, value in paid]+[156765527508803240]),
          "maximum of whole-source bounds")
    budget = 2130706433**6//2**128
    check(budget == 274980728111395087, "original field budget")
    check(budget-total == 1066135833452, "original reserve")
    check(near == 2*67472 and 3*67472 <= K, "near theorem gate")
    check(2*500 < 67472, "canonical selection gate")


def main():
    verify()
    mutations = [((1018576, 1038635), 274979661975561635),
                 ((1018578, 1038635), 274979661975561635),
                 ((1018577, 1038634), 274979661975561635),
                 ((1018577, 1038636), 274979661975561635),
                 ((1018577, 1038635), 274979661975561634),
                 ((1018577, 1038635), 274979661975561636)]
    for residual, total in mutations:
        try:
            verify(residual, total)
        except ValueError:
            pass
        else:
            raise ValueError("accepted interval/budget mutation")
    verify_receiver_gates()
    verify_density_gates()
    verify_dense_core_mass()
    print("PASS: exact original-g partition, child intervals, one near and field reserve")
    print("PASS: six boundary/budget mutations rejected; original rank-twelve residual J=9941..29999")
    print("The source bridge is a hand proof, not certified by this arithmetic check")


def verify_receiver_gates():
    def residual_fiber_gate(j, a):
        return 14000 <= j <= 29999 and a >= j-2000
    controls = ((14000, 12000, True), (14000, 11999, False),
                (13999, 13989, False), (25000, 24990, True),
                (10000, 9990, False), (29999, 27999, True),
                (29999, 27998, False), (30000, 28000, False),
                (9941, 9931, False), (52999, 52989, False),
                (53000, 52990, False))
    for j, a, expected in controls:
        check(residual_fiber_gate(j, a) == expected, "exact remaining receiver-fiber gate")
    check(max(248408859318207582, 272112051300507362) < 274979661975561635,
          "new source classes fit existing original maximum")
    print("PASS: eleven residual fiber-gate controls; J>=30000 handled by the whole interval")


def verify_density_gates():
    def gate(k, rank, size):
        return 23000 <= k <= 29999 and 1 <= rank <= 10 and 30*size <= rank*(k+67466)
    controls = ((23000,8,22997,True), (23000,7,22996,False),
                (24537,8,24534,True), (24538,8,24535,False),
                (28916,9,28914,True), (28917,9,28915,False),
                (29999,10,29998,True), (23014,3,9048,True),
                (23014,3,9049,False), (22999,10,22998,False),
                (30000,10,29999,False), (23000,11,23000,False))
    for k,rank,size,expected in controls:
        check(gate(k,rank,size)==expected, "bounded-density source gate")
    check(268913508505087358 < 274979661975561635, "new class below original maximum")
    print("PASS: twelve density/rank boundary controls; J interval unchanged")


def verify_dense_core_mass():
    budget=2130706433**6//2**128
    comparison=268913508505087358
    mass=6933965264351691
    check(7*(mass-1)<=8*(budget-comparison)<7*mass,"least dense-core mass integer")
    for t in (8,9):
        check((10-t)*29999<=67466+111-11*t,"all large core-flag ranks excluded")
    check(29999-((29999+67484)//4+1)==5628,"rank-seven auxiliary degree")
    check(7*(102451841872190189-1)<=8*(budget-185335366473228672)
          <7*102451841872190189,"pointwise endpoint mass")
    print("PASS: original-label dense-core mass and rank/degree boundaries; no upper census")


if __name__ == "__main__":
    main()
