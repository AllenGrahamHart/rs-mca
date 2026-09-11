"""Small diagnostic of charging the geometric envelope at the last anchor."""
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

NODE = Path(__file__).resolve().parent
PARENT = NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R,D,TARGET = 1048576,67472,274980728111395087


def need(ok,why):
    if not ok:
        raise ValueError(why)


def main():
    raw = (PARENT/"index.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest()==PIN,"parent custody")
    refs = json.loads(raw)["profiles"]
    need(len(refs)==13,"profile inventory")
    totals = []
    for ref in refs:
        raw = (PARENT/ref["path"]).read_bytes()
        need(hashlib.sha256(raw).hexdigest()==ref["sha256"],"parent shard")
        p = json.loads(raw)
        j = p["J"][1]
        h = (j-1)//10
        image_degree = j-8
        cutoff = h+1
        branch = min(image_degree-2*cutoff,max(1,cutoff-2))
        need(branch>=1,"nonempty degree-envelope case")
        bad = comb(image_degree-2,2)*branch//comb(branch+cutoff-1,2)
        total,original = Q(p["mass_floor"],3),Q(p["mass_floor"],3)
        for t,den in ((1,2),(2,6)):
            need(bad<D+1-t,"positive last-anchor denominator")
            factor = Q(1)
            for a in range(2,9):
                factor *= Q(R+a,D-t+a)
            allowance = Q(*map(int,p["terminals"][t-1]))
            original += factor*Q(R+1,D+1-t)*allowance/den
            total += factor*Q(R+1-bad,D+1-t-bad)*allowance/den
        need(original.numerator//original.denominator+134944==p["weighted_envelope"],
             "original envelope")
        price = total.numerator//total.denominator+134944
        need(price>TARGET,"diagnostic recipe unexpectedly affordable")
        totals.append(price)
        print(p["J"],"H",h,"last-anchor geometric envelope",bad,"source price",price)
    print("PASS all13 coarse last-anchor recipes exceed the target; minimum",min(totals))
    print("This is an allowance-recipe diagnostic, NOT a realized bad source or necessary anchor cost.")
    print("Actual exceptional coordinates may be much fewer; sharper joint source selection remains possible.")


if __name__=="__main__":
    main()
