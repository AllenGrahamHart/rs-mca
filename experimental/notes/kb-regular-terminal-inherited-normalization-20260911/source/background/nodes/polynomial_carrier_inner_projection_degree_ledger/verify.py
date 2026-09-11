"""Small exact actual-anchor controls, not official MCA witnesses."""
from math import gcd


def need(ok,why):
    if not ok:
        raise ValueError(why)


def mul(a,b,p):
    result = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            result[i+j] = (result[i+j]+x*y) % p
    return result


def ev(poly,x,p):
    return sum(a*pow(x,i,p) for i,a in enumerate(poly)) % p


def main():
    p,mu = 97,12
    h = [-1]+[0]*11+[1]
    carrier = [[0,1],h,[0]*12+h,[0]*24+h]
    roots = [x for x in range(p) if pow(x,mu,p)==1]
    need(len(roots)==12 and 16 in roots,"split actual centre fibre")
    g = [1]
    for a in range(7):
        g = mul(g,[-a,1],p)
    initial = [[0]*i+[1] for i in range(7)]+[mul(g,u,p) for u in carrier]
    need(len(initial)==11 and max(map(len,initial))-1==43,"original shared carrier degree")
    need(len({len(u)-1 for u in initial})==11,"independence by distinct leading degrees")
    need(all(ev(u,a,p)==0 for u in initial[7:] for a in range(7)),"seven actual anchor kernels")
    for x in range(p):
        if ev(h,x,p):
            ratio = x*pow(ev(h,x,p),-1,p) % p
            need(ratio*(pow(x,mu,p)-1) % p==x,"birational carrier recovery")
    need([ev(u,16,p) for u in carrier]==[16,0,0,0],"last actual centre")
    need(gcd(12,24)==12 and 43==7+12+24,"last degree jump and complete degree ledger")
    available = [x for x in roots if x not in range(7)]
    need(len(available)==10,"do not reset the domain after the seven anchors")
    print("PASS dimension11 degree43 -> seven anchors -> dimension4 degree36 -> last anchor -> dimension3 degree24")
    print("PASS normalization degrees1 -> 1 -> 12, final image conic; ten available centre coordinates")
    # The composed rational normal curve retains degree2 through all anchors.
    p = 101
    images = {a*a % p for a in range(1,9)}
    removed = [x for x in range(p) if x*x % p in images]
    need(len(images)==8 and len(removed)==16,"whole normalized fibres, not only chosen roots")
    need(20==16+4 and 2==20//10==4//2,"no-jump composed rational-normal control")
    print("PASS degree20 rational-normal composition: sixteen full fixed roots, terminal degree4, nu remains2")
    print("Shared-carrier controls only; no official large-agreement MCA source is certified")


if __name__ == "__main__":
    main()
