"""Exact original-source arithmetic for the nonconstant-pencil descent."""
from fractions import Fraction as Q
import hashlib
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
PARENT = NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R,D,B = 1048576,67472,274980728111395087


def need(ok,why):
    if not ok:
        raise ValueError(why)


def main():
    raw = (PARENT/"index.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest()==PIN,"original allowance index")
    refs = json.loads(raw)["profiles"]
    need(len(refs)==13,"thirteen original profiles")
    maximum,next_j,checks = 0,9965,0
    for ref in refs:
        need(ref["path"]==str(next_j)+".json","profile order")
        raw = (PARENT/ref["path"]).read_bytes()
        need(hashlib.sha256(raw).hexdigest()==ref["sha256"],"source profile pin")
        row = json.loads(raw)
        need(row["J"][0]==next_j,"original degree coverage")
        next_j = row["J"][1]+1
        total = Q(row["mass_floor"],3)
        for t,den in ((1,2),(2,6)):
            allowance = Q(*map(int,row["terminals"][t-1]))
            whole_factor = Q(prod(R+ell for ell in range(1,9)),
                             prod(D-t+ell for ell in range(1,9)))
            for j in range(8):
                s,r = 11-j,19-2*j
                need(r==2*s-3 and r>s,"regular prefix dimensions")
                future = Q(1)
                for i in range(j,8):
                    si,ri = 11-i,19-2*i
                    expected = Q(R+8-i,D-t+8-i)
                    for original_j in row["J"]:
                        bad = original_j+si-ri
                        need(0<=bad<D+original_j-t,"positive original denominator")
                        actual = Q(R+original_j-bad,D+original_j-t-bad)
                        need(actual==expected,"original J cancels, no shortened raw")
                    future *= expected
                direct = Q(prod(R+ell for ell in range(1,s-2)),
                           prod(D-t+ell for ell in range(1,s-2)))
                need(future==direct,"maximal-pencil remaining factors")
                past = Q(prod(R+8-i for i in range(j)),
                         prod(D-t+8-i for i in range(j)))
                need(past*future==whole_factor,"chronological exact composition")
                if j==7:
                    need(future==Q(1048577,67473-t),"same penultimate allowance")
                checks += 1
            total += whole_factor*allowance/den
        value = total.numerator//total.denominator+134944
        need(value==row["weighted_envelope"]<=272127061148955779<B,"original resource and near once")
        maximum = max(maximum,value)
    need(next_j==21500 and maximum==272127061148955779,"whole source range and maximum")
    need(max(270000000000000000,maximum)==maximum<B,
         "paid whole-source alternatives combine by maximum")
    need(270000000000000000+maximum>B,"adding alternative source caps is not valid payment")
    print("PASS",checks,"prefix-factor checks; original field/weights/allowances and thirteen profiles")
    print("MAXIMAL-PENCIL ORIGINAL-SOURCE CAP",maximum,"RESERVE",B-maximum)
    print("PASS exact residual/whole-source max composition; no new numeric certificate or scan")
    print("The geometry is a written proof; unrestricted rank19 and both Prizes remain open")


if __name__=="__main__":
    main()
