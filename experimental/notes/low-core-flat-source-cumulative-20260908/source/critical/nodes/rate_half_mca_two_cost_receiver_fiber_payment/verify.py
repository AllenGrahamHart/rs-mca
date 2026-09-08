"""Exact two-cost receiver-fiber interval certificate; no source enumeration."""

from fractions import Fraction as F
import hashlib
import importlib.util
from math import prod
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/"rate_half_mca_fiber_contraction_interval/verify.py"
spec=importlib.util.spec_from_file_location("quadratic_certificate",path)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
R,d,D,H,NEAR=1048576,67472,67466,52999,134944
Q10=156765527508668296
Pd=prod(d+i for i in range(1,11))
P=prod(D+i for i in range(1,11))
W=F(10488,125)
GATES=((21000,6000),(23000,8000))
EXPECTED="5d958551756ddbc6abb9cd787ed8f3f887bc06087c9583fe335564df76f02804"


def need(ok,why):
    if not ok:
        raise ValueError(why)


def basis(J,a,theta):
    z=theta*a
    return (D+J-z)*prod(D+a+10-i-z for i in range(1,10))*(D+1+10*z)


def cover(rows,lo):
    need(rows and rows[0][0]==lo and rows[-1][1]==H,"full degree endpoints")
    need(all(a<=b for a,b in rows) and all(x[1]+1==y[0] for x,y in zip(rows,rows[1:])),
         "consecutive full degree cover")


def box(J0,J1,L,left,right,coefficients):
    a=J0-L
    aa,bb,cc=coefficients
    base=12*P*(aa+bb*J0+cc*J0*J0)
    high=(d+J0)*Pd*W
    light=min(high,max(base,12*min(basis(J0,a,F(0)),basis(J0,a,1-left))))
    heavy=min(high,max(base,12*min(basis(J0,a,left),basis(J0,a,right))))
    resource=prod(R+J1-i for i in range(12))
    heavy_cap=Q10+(1-left)*(J1-10)
    total=F(resource)/light+max(F(0),1-heavy/light)*heavy_cap+NEAR
    return light,heavy,total


def main():
    coefficients=old.ladder()
    need(all(x>=0 for x in coefficients),"increasing universal quadratic")
    need(H<D+1 and 9*D-10*H+199>0,"no kink and whole-a monotonicity")
    need(H<=65000 and 2130706433**6>=2*R,"quadratic and full-child scope")
    digest=hashlib.sha256()
    count=mutations=0
    peaks=[]
    for lo,L in GATES:
        rows=[(a,min(a+499,H)) for a in range(lo,H+1,500)]
        cover(rows,lo)
        peak=(F(0),None)
        for J0,J1 in rows:
            need(J0>L>=10,"actual positive fiber range")
            for i in range(16):
                left,right=F(16+i,32),F(17+i,32)
                light,heavy,total=box(J0,J1,L,left,right,coefficients)
                floor=total.__floor__()
                need(floor<=total<floor+1,"exact total floor")
                need(floor<274980728111395087,"entire source class paid")
                for wrong in (floor-1,floor+1):
                    need(not wrong<=total<wrong+1,"reject adjacent floor")
                    mutations+=1
                digest.update(f"{lo},{L},{J0},{J1},{i}:{light.numerator}/{light.denominator}:{heavy.numerator}/{heavy.denominator}:{total.numerator}/{total.denominator}\n".encode())
                if total>peak[0]:
                    peak=total,(J0,J1,i)
                count+=1
        peaks.append((lo,L,peak[0].__floor__(),peak[1]))
        for changed in (rows[1:],rows[:-1],rows+[rows[-1]],rows[:5]+rows[6:]):
            try:
                cover(changed,lo)
            except ValueError:
                pass
            else:
                raise ValueError("accepted broken degree cover")
        print("GATE",peaks[-1],flush=True)
    need(peaks==[(21000,6000,266180883463176443,(21000,21499,15)),
                 (23000,8000,265879110627611677,(23000,23499,15))],"exact two gate maxima")
    need(count==1984 and mutations==3968,"complete finite inventory")
    need(digest.hexdigest()==EXPECTED,"all exact box costs")
    print("TOTAL boxes",count,"wrong floors",mutations,"digest",digest.hexdigest(),flush=True)
    print("Proved source-class application needs the analytic box proof; not every carrier")


if __name__=="__main__":
    main()
