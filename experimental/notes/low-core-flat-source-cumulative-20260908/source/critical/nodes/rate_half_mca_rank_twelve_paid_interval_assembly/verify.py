"""Exact finite branch arithmetic, not certification of source transport."""


def check(ok, message):
    if not ok:
        raise ValueError(message)


def verify(residual=(1025577, 1038635), total=274979661975561635):
    K, n, near = 1048576, 2097152, 134944
    paid = [(0, 793576, 273540953998915577),
            (793577, 878576, 270992495272115150),
            (878577, 1025576, 274929007493481160),
            (1038636, 1043775, 274979661975561635),
            (1043776, n, 100000000000134944)]
    intervals = sorted([(a, b) for a, b, _ in paid]+[residual])
    check(intervals[0][0] == 0 and intervals[-1][1] == n, "complete g domain")
    check(all(a <= b for a, b in intervals), "nonempty intervals")
    check(all(x[1]+1 == y[0] for x, y in zip(intervals, intervals[1:])),
          "disjoint exhaustive original-core partition")
    check((K-residual[1], K-residual[0]) == (9941, 22999), "unpaid child interval")
    check((K-1025576, K-878577) == (23000, 169999), "whole-interval child transport")
    check((K-1043775, K-1038636) == (4801, 9940), "lower child transport")
    check(residual[1]-residual[0]+1 == 13059, "residual cardinality")
    check(14059-13059 == 23999-23000+1 == 1000, "new whole-source degree interval")
    check(total == max([value for _, _, value in paid]+[156765527508803240]),
          "maximum of whole-source bounds")
    budget = 2130706433**6//2**128
    check(budget == 274980728111395087, "original field budget")
    check(budget-total == 1066135833452, "original reserve")
    check(near == 2*67472 and 3*67472 <= K, "near theorem gate")
    check(2*500 < 67472, "canonical selection gate")


def main():
    verify()
    mutations = [((1025576, 1038635), 274979661975561635),
                 ((1025578, 1038635), 274979661975561635),
                 ((1025577, 1038634), 274979661975561635),
                 ((1025577, 1038636), 274979661975561635),
                 ((1025577, 1038635), 274979661975561634),
                 ((1025577, 1038635), 274979661975561636)]
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
    verify_rank_eight_gate()
    verify_first_excess_interval()
    verify_quantitative_interval()
    verify_rank_profile_interval()
    verify_two_cost_interval()
    verify_clustered_arc_gate()
    print("PASS: exact original-g partition, child intervals, one near and field reserve")
    print("PASS: six boundary/budget mutations rejected; original rank-twelve residual J=9941..22999")
    print("The source bridge is a hand proof, not certified by this arithmetic check")


def verify_receiver_gates():
    def residual_fiber_gate(j, a):
        return 14000 <= j <= 22999 and a >= j-2000
    controls = ((14000, 12000, True), (14000, 11999, False),
                (13999, 13989, False), (21000, 20990, True),
                (10000, 9990, False), (22999, 20999, True),
                (22999, 20998, False), (23000, 21000, False),
                (9941, 9931, False), (52999, 52989, False),
                (53000, 52990, False))
    for j, a, expected in controls:
        check(residual_fiber_gate(j, a) == expected, "exact remaining receiver-fiber gate")
    check(max(248408859318207582, 272112051300507362) < 274979661975561635,
          "new source classes fit existing original maximum")
    print("PASS: eleven residual fiber-gate controls; J>=23000 handled by the whole interval")


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
    print("PASS: twelve old density/rank controls; supplier full scope retained")


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


def verify_rank_eight_gate():
    def gate(J, rank, size):
        return 23000 <= J <= 29999 and 1 <= rank <= 10 and 8*size <= rank*(J-3)
    controls = ((23000,8,22997,True), (23000,7,22996,False),
                (29999,8,29996,True), (29999,9,29997,True),
                (29999,10,29998,True), (27000,7,23622,True),
                (27000,7,23623,False), (29999,7,26246,True),
                (29999,7,26247,False), (22999,8,22996,False),
                (30000,8,29997,False), (23000,11,23000,False))
    for J,rank,size,expected in controls:
        check(gate(J,rank,size)==expected, "new exact integer density gate")
    for rank in (8,9,10):
        check((rank-8)*23000+88-11*rank>=0, "all maximizing ranks >=8 paid")
    total=274977202549132026
    check(total<274979661975561635 and 2130706433**6//2**128-total==3525562263061,
          "new total below original maximum with reserve")
    print("PASS: twelve stronger density controls; every maximizing rank >=8 excluded")


def verify_first_excess_interval():
    for J, expected in ((27999,False),(28000,True),(29999,True),(30000,False)):
        check((28000<=J<=29999)==expected,"first-excess interval endpoints")
    K, total = 1048576, 273019482620216244
    check((K-29999,K-28000)==(1018577,1020576),"newly paid ORIGINAL core interval")
    check(248408859318207582<total<274929007493481160,"source-fiber and old union included")
    check(2130706433**6//2**128-total==1961245491178843,"first-excess source reserve")
    print("PASS: first-excess interval transport, four endpoint controls and whole-source union")


def verify_quantitative_interval():
    for J, expected in ((26499,False),(26500,True),(27999,True),(28000,False)):
        check((26500<=J<=27999)==expected, "quantitative interval endpoints")
    K, total = 1048576, 272896493994028693
    check((K-27999,K-26500)==(1020577,1022076), "new original core interval")
    check(2130706433**6//2**128-total==2084234117366394, "quantitative reserve")
    check(246756107210901806<total<274929007493481160, "whole-source alternatives")
    for J, b, expected in ((22999,22989,False),(23000,18300,True),
                           (23000,18299,False),(52999,48299,True),
                           (52999,48298,False),(53000,48300,False)):
        check((23000<=J<=52999 and b>=J-4700)==expected, "historical full supplier fiber gate")
    print("PASS: quantitative interval and six full-scope fiber controls; no remaining4700 gate")


def verify_rank_profile_interval():
    for J, expected in ((23999,False),(24000,True),(26499,True),(26500,False)):
        check((24000<=J<=26499)==expected, "rank-profile interval endpoints")
    K, total = 1048576, 273123695048315164
    check((K-26499,K-24000)==(1022077,1024576), "new original core interval")
    check(2130706433**6//2**128-total==1857033063079923, "rank-profile reserve")
    check(246756107210901806<total<274929007493481160, "whole-source union")
    print("PASS: rank-profile interval transport, four endpoints and original reserve")


def verify_two_cost_interval():
    for J, expected in ((22999,False),(23000,True),(23999,True),(24000,False)):
        check((23000<=J<=23999)==expected, "two-cost interval endpoints")
    K, total = 1048576, 274846585959022192
    check((K-23999,K-23000)==(1024577,1025576), "new original core interval")
    check(2130706433**6//2**128-total==134142152372895, "two-cost interval reserve")
    check(265879110627611677<total<274929007493481160, "whole-source union")
    for J, b, expected in ((20999,20989,False),(21000,15000,True),
                           (21000,14999,False),(22999,16999,True),
                           (22999,16998,False),(23000,17000,False)):
        check((21000<=J<=22999 and b>=J-6000)==expected, "remaining6000 fiber gate")
    check(266180883463176443<274979661975561635, "additional class fits original maximum")
    check(max(9941,23000)>min(22999,29999), "old density/mass scopes miss entire residual")
    check(22999<23000<=52999<=169999, "full4700/8000 scopes subsumed by paid union")
    print("PASS: two-cost interval, six remaining6000 controls; old density/mass scope entirely subsumed")


def verify_clustered_arc_gate():
    def gate(j, fibers, largest, arc):
        return 20481<=j<=22999 and fibers<=560 and largest<=2048 and arc
    controls = ((20481,560,2048,True,True),(22999,560,2048,True,True),
                (20480,560,2048,True,False),(23000,560,2048,True,False),
                (20481,561,2048,True,False),(20481,560,2049,True,False),
                (20481,560,2048,False,False),(20481,523,2048,True,True))
    for j,f,h,a,expected in controls:
        check(gate(j,f,h,a)==expected, "actual clustered-arc source gate")
    total = 274545534639685994
    check(total<274979661975561635, "whole-line alternative below main maximum")
    check(2130706433**6//2**128-total==435193471709093, "clustered-arc reserve")
    check((1048576-22999,1048576-20481)==(1025577,1028095), "original core scope")
    check(9941<=20481<=22999, "source class inside unchanged degree residual")
    print("PASS: eight clustered-arc controls and original-source transport; not an entire J interval")


if __name__ == "__main__":
    main()
