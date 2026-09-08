"""Independent fixed-scale audit: branch formulas, prefix derivatives, polynomial steps."""

from functools import lru_cache
import hashlib
from math import comb, prod


N0, GAP, DC, CC = 1048576, 67472, 67466, 67467
UNIT, PRECISION = 8*27720*64*4, 2**128
CAPS = (981105, 4070947, 63264449, 983145945, 15278131113,
        231038329409, 3424826154478, 50371450079970,
        737012707696078, 10755802499540570)
EXPECTED = (261925431454675420, 242907143759668079,
            225655255580817422, 220471747439971004)
DIGESTS = (
    "8d75b09e52c77b49efef7d35152906afaf9615d6812783a6dcebb69f7e0443f5",
    "1fa689aad105afb8bd68753e3a27fc54cce6bf206b160d85f639a5c2f24724e1",
    "c759ee3312cafb8a1c032031957eb8e59c737af75e410fe90d317af71fd650f4",
    "8bab9ef29e113d834d30698ea054ad195e70c5edf620450b7126955e942f6466",
)


def check(ok, message):
    if not ok:
        raise ValueError(message)


def ceiling(n, d):
    check(d > 0, "positive audit denominator")
    return n//d+(n % d != 0)


@lru_cache(maxsize=8192)
def coefficients(d, e, rank):
    divisor = 2*(d+2)
    values = [PRECISION*d*(2*d+1)//divisor,
              PRECISION*(3*d+1)//divisor, PRECISION//divisor]
    x = min(e//2, 5000)
    check(3 <= rank <= e <= d, "audit quadratic scope")
    for target in range(4, rank+1):
        a,b,c = values
        m, h = target-1, d+target-1
        check(b >= d*c >= 0, "audit input contraction gate")
        # Compose q(((m-1)K+1)/m), then multiply by d+K.
        composed = [a*m*m+b*m+c, b*(m-1)*m+2*c*(m-1), c*(m-1)**2]
        u = [d*composed[0]]+[d*composed[i]+composed[i-1] for i in (1,2)]+[composed[2]]
        common = m*m*h
        value_at_m = sum(values[i]*m**i for i in range(3))
        spike = [h*(a-b+c)-m*value_at_m, h*(b-2*c)+value_at_m, h*c]
        remainder = u[2]-common*c
        check(remainder >= 0 and u[3] >= 0, "audit convex remainder")
        slope = u[1]+2*remainder*x+3*u[3]*x*x
        intercept = u[0]-remainder*x*x-2*u[3]*x**3
        candidate = [intercept//common, slope//common, c]
        overshoot = max(0, *(ceiling(h*sum(candidate[i]*k**i for i in range(3))
                                    -sum(spike[i]*k**i for i in range(3)), h)
                             for k in (target,e)))
        candidate[0] -= overshoot
        check(candidate[0]*common <= intercept and candidate[1]*common <= slope,
              "audit coefficientwise tangent floor")
        check(all(h*sum(candidate[i]*k**i for i in range(3)) <=
                  sum(spike[i]*k**i for i in range(3)) for k in (target,e)), "audit affine endpoint dominance")
        check(candidate[1] >= d*c, "audit next-step gate")
        values = candidate
    return tuple(values)


def quotient_basis(rank,d,e,k):
    check(rank <= k <= e <= d, "audit quotient hull")
    if rank < 3:
        return (d+k)*(d+1 if rank == 2 else 1)
    polynomial = coefficients(d,e,rank)
    value = sum(polynomial[i]*k**i for i in range(3))
    check(value > 0 and polynomial[1] >= 0, "audit increasing positive polynomial")
    return prod(range(d+1,d+rank))*value//PRECISION


def endpoint(J,j,r,u):
    bottom = j*(UNIT+(J-11)*(UNIT//(r+1)))
    top = (J-2001)*UNIT if j == r == 1 else j*(UNIT+(J-11)*(UNIT//r))
    check((top-bottom) % 8 == 0, "audit size grid")
    return bottom+(top-bottom)*u//8


def local_arrays(J,j,r,a,v):
    z, h = v*(a//64), a//j
    ell = 11-j
    outside = [(J+DC)*UNIT-z]
    for i in range(1,ell):
        outside.append((J+DC)*UNIT-z-i*h if j+i <= r else
                       (DC+ell-i)*UNIT+a-z)
    completion = [((J+DC)*UNIT-(10-i)*h if 10-i <= r else (CC+i)*UNIT)
                  for i in range(j)]
    return z, outside, completion


def cost(J0,J1,j,r,u,v):
    vertices = [(J,endpoint(J,j,r,edge)) for J in (J0,J1) for edge in (u,u+1)]
    low_a, high_a = min(a for J,a in vertices), max(a for J,a in vertices)
    zlo, zhi, hhi = v*(low_a//64),(v+1)*(high_a//64),high_a//j
    ell = 11-j
    kd = [J*UNIT-a for J,a in vertices]
    dk0, dk1 = min(kd)//UNIT, ceiling(max(kd),UNIT)
    gap = DC+(64-v-1)*(low_a//64)//UNIT
    lower_q = quotient_basis(ell,gap,dk1,dk0)
    factors = [min(local_arrays(J,j,r,a,0)[2][i] for J,a in vertices) for i in range(j)]
    check(zhi < CC*UNIT and zhi % 4 == 0, "audit positive tangent range")
    root = prod(x-zhi for x in factors)
    inner = root
    for calibration in range(5):
        q = calibration*(zhi//4)
        products, derivatives = [1],[0]
        for f in factors:
            products.append(products[-1]*(f-q))
            derivatives.append(derivatives[-1]*(f-q)+products[-2])
        coeff = [comb(11,b)*(products[j-b]+q*derivatives[j-b])
                 -(comb(11,b-1)*derivatives[j-b+1] if b>1 else 0)
                 for b in range(1,j+1)]
        tail = coeff.pop()
        for b in range(j-1,0,-1):
            multiplier = max(zlo-b*hhi,0) if tail>=0 else max(zhi-b*UNIT,0)
            tail = coeff.pop()+tail*multiplier
        inner = max(inner,root+tail*(zlo if tail>=0 else zhi))
    direct = root
    for b in range(1,j+1):
        direct += comb(11,b)*prod(max(zlo-i*hhi,0) for i in range(b))*prod(x-zhi+b*UNIT for x in factors[:j-b])
    inner = max(inner,direct)
    if j<=5:
        inner = max(inner,prod((CC+i)*UNIT-zlo for i in range(j))
                    +11*zlo*prod((CC+i)*UNIT for i in range(j-1)))
    inside_terms = [None]*(j+1)
    quotient_min = None
    for J,a in vertices:
        for occ in (v,v+1):
            z, outside, comp = local_arrays(J,j,r,a,occ)
            pp = prod(outside)
            quotient_min = pp if quotient_min is None else min(pp,quotient_min)
            for b in range(j+1):
                term = comb(11,b)*pp*prod(max(z-i*(a//j),0) for i in range(b))*prod(x-z+b*UNIT for x in comp[:j-b])
                inside_terms[b] = term if inside_terms[b] is None else min(term,inside_terms[b])
    hybrid = min(prod([(J+DC)*UNIT]+[
        (J+DC)*UNIT-i*(a//j) if i<=r else (DC+11-i)*UNIT for i in range(1,11)]) for J,a in vertices)
    basis = max(quotient_min*inner//UNIT**11, lower_q*inner//UNIT**j,
                sum(inside_terms)//UNIT**11, hybrid//UNIT**11)
    check(basis > 0, "audit basis positivity")
    return 12*basis


def audit(J0):
    J1 = J0+1999
    numerator = prod(range(N0+J1-11,N0+J1+1))
    high = (GAP+J0)*prod(range(GAP+1,GAP+11))*10488//125
    density = prod((J0+DC)*11-i*J0 for i in range(11))//11**11
    maximum = numerator//min(12*density,high)+134944
    digest = hashlib.sha256()
    record_boxes = source_boxes = mutations = 0
    for j in range(1,11):
        for r in range(j,11):
            for u in range(8):
                costs = []
                for v in range(64):
                    value = min(high,cost(J0,J1,j,r,u,v))
                    costs.append(value)
                    digest.update(f"C:{J0},{j},{r},{u},{v}:{value}\n".encode("ascii"))
                    record_boxes += 1
                for v in range(8):
                    den = 16*j
                    left, right = (2*j-1)*8+v, (2*j-1)*8+v+1
                    light_end = ((2*j-1)*8-v)*64//den
                    heavy_start, heavy_end = left*64//den, ceiling(right*64,den)
                    lower_l = min(costs[i] for i in range(64) if i<=light_end)
                    lower_h = min(costs[i] for i in range(64) if i+1>=heavy_start and i<=heavy_end)
                    a0,a1 = endpoint(J0,j,r,u+1),endpoint(J1,j,r,u+1)
                    qden = (GAP+J0)*UNIT*den-right*a0
                    qnum = ((N0+J0)*UNIT-a0)*den*CAPS[10-j]
                    en,ed = (den-left)*a1,den*UNIT
                    child = ceiling(qnum*ed+en*qden,qden*ed)
                    top = numerator+max(0,lower_l-lower_h)*child
                    quotient = top//lower_l
                    check(quotient*lower_l<=top<(quotient+1)*lower_l,"audit exact floor")
                    for delta in (-1,1):
                        wrong = quotient+delta
                        check(not wrong*lower_l<=top<(wrong+1)*lower_l,"wrong floor accepted")
                        mutations += 1
                    total = quotient+134944
                    source_boxes += 1
                    digest.update(f"S:{J0},{j},{r},{u},{v}:{total}\n".encode("ascii"))
                    maximum = max(maximum,total)
        print("AUDIT PREFIX",J0,"rank",j,"maximum",maximum,flush=True)
    check(maximum==EXPECTED[(J0-32000)//2000],"audit frozen maximum")
    check(digest.hexdigest()==DIGESTS[(J0-32000)//2000],"audit every record cost and source bound")
    check((record_boxes,source_boxes,mutations)==(28160,3520,7040),"audit full inventory")
    print("AUDIT INTERVAL",J0,"cap",maximum,"DIGEST",digest.hexdigest(),"mutations",mutations,flush=True)
    return digest.hexdigest()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start",type=int,choices=(32000,34000,36000,38000))
    args = parser.parse_args()
    for start in ([args.start] if args.start is not None else (32000,34000,36000,38000)):
        audit(start)
