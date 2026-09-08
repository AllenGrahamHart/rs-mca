"""Independent integer/binomial audit; imports no primary or other verifier."""

from math import comb


def ceil_div(a, b):
    return -(-a // b)


def verify():
    r, d, near = 1048576, 67472, 134944
    c = max(ceil_div(132*comb(r+j, 12), (d+j)*comb(d+10, 10))
            for j in (4801, 169999))
    assert c == 23067643444721720934
    # The ten consecutive factors are expressed by a ratio of binomial coefficients.
    w_num, w_den = 84*(d+4)*comb(d+3, 10), (d+11)*comb(d+10, 10)
    a_num, a_den = 12*d, d+11
    assert w_num < 84*w_den and 12*84 < d+1
    budget = 2130706433**6 // 2**128
    total = c*w_den//w_num+near
    assert total == 274928364476952114 and budget-total == 52363634442973
    assert (total-near)*w_num <= c*w_den < (total-near+1)*w_num
    difference = w_num*a_den-a_num*w_den
    assert difference > 0
    numerator = c*w_den*a_den+difference*50371450079970
    denominator = w_num*a_den
    rank_total = numerator//denominator+near
    assert rank_total == 274971532963425180
    assert budget-rank_total == 9195147969907
    mass_num = (w_num*(budget-near+1)-c*w_den)*a_den
    low = ceil_div(mass_num, difference)
    assert low == 61100872739557
    assert (low-1)*difference < mass_num <= low*difference
    assert not numerator < (rank_total-near)*denominator
    assert not low*difference < mass_num
    assert 12*d*500 >= 5999*(d+11)
    assert 6468*125 < 12*(d+1)
    simple = 500*c//41952+near
    simple_rank = (500*c+35953*50371450079970)//41952+near
    assert simple == 274929007493481160 < budget
    assert simple_rank == 274972175989493869 < budget
    assert budget-simple_rank == 8552121901218
    assert ceil_div(41952*(budget-near+1)-500*c, 35953) == 60350551072932 > 50371450079970
    print("PASS: independent seven-margin, small-rank and mass certificates")
    print("PASS: short integer relaxation with coefficients 5999,41952,500")


if __name__ == "__main__":
    verify()
