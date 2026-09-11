"""Tiny exact conic controls over F_101; no official-source enumeration."""
P = 101


def need(ok, why):
    if not ok:
        raise ValueError(why)


def trim(a):
    a = [x % P for x in a]
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a


def add(a,b,scale=1):
    return trim([(a[i] if i<len(a) else 0)+scale*(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])


def mul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def divide(a,b):
    a,b = trim(a),trim(b)
    need(b != [0], "zero polynomial divisor")
    q = [0]*max(1,len(a)-len(b)+1)
    while a != [0] and len(a)>=len(b):
        d,c = len(a)-len(b),a[-1]*pow(b[-1],-1,P) % P
        q[d] = c
        a = add(a,[0]*d+[c*x for x in b],-1)
    return trim(q),a


def gcd(a,b):
    while b != [0]:
        a,b = b,divide(a,b)[1]
    return trim([x*pow(a[-1],-1,P) for x in a]) if a != [0] else [0]


def rank(rows):
    a = [[x % P for x in row] for row in rows]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:
            continue
        a[r],a[pivot] = a[pivot],a[r]
        inv = pow(a[r][j],-1,P)
        a[r] = [x*inv % P for x in a[r]]
        for i in range(len(a)):
            if i != r:
                scale = a[i][j]
                a[i] = [(x-scale*y) % P for x,y in zip(a[i],a[r])]
        r += 1
    return r


def proj(v):
    v = tuple(x % P for x in v)
    inv = pow(next(x for x in v if x),-1,P)
    return tuple(x*inv % P for x in v)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b)) % P


def ev(a,z,degree=None):
    if z is None:
        return a[degree] if degree<len(a) else 0
    return sum(x*pow(z,i,P) for i,x in enumerate(a)) % P


def fixture(name,t,expected):
    ell = [[1],[0,1],[0,0,1]]
    right = [trim([t[i][j] for i in range(3)]) for j in range(3)]
    cross = [add(mul(ell[i],right[j]),mul(ell[j],right[i]),-1)
             for i,j in ((1,2),(2,0),(0,1))]
    common = gcd(gcd(cross[0],cross[1]),cross[2])
    infinity = 4-max(len(a)-1 for a in cross if a != [0])
    chi = 4-(len(common)-1)-infinity
    need(chi==expected, "kernel degree control")
    reduced = [divide(a,common)[0] for a in cross]
    need(rank([a+[0]*(chi+1-len(a)) for a in reduced])==3, "pencil-free coefficient rank")
    bases, directions = [], {}
    for z in list(range(P))+[None]:
        l = (0,0,1) if z is None else (1,z,z*z % P)
        lt = [sum(l[i]*t[i][j] for i in range(3)) % P for j in range(3)]
        d = proj([ev(a,z,chi) for a in reduced])
        if rank([l,lt])==1:
            bases.append((z,l,d))
        elif chi==2:
            need(d not in directions.values(), "double-conic direction injectivity")
            directions[z] = d
    if chi==2:
        need(len(bases)<=2, "rank-one base count")
        for z,l,d in bases:
            need(dot(l,d)==0, "limiting direction in invariant plane")
            need(sum(dot(l,v)==0 for v in directions.values())<=1, "one other nonbase plane fibre")
    print("PASS",name,"chi",chi,"base divisor degree",4-chi,"rational bases",len(bases))
    return reduced


def main():
    nilpotent = [[0,1,0],[0,0,2],[0,0,0]]
    fixture("nilpotent",nilpotent,2)
    fixture("split",[[0,0,0],[0,1,0],[0,0,3]],2)
    fixture("cubic kernel",[[0,0,0],[1,2,3],[4,5,6]],3)
    fixture("quartic kernel",[[0,1,2],[3,4,5],[6,7,8]],4)
    p,q = [0,0,1],[1,0,1]
    carrier = [mul(q,q),mul(p,q),mul(p,p)]
    bases = 0
    heights = set()
    for x in range(P):
        px,qx = ev(p,x),ev(q,x)
        if qx==0:
            bases += 1
            continue
        z = px*pow(qx,-1,P) % P
        y = [z*z,-2*z,1]
        ty = [dot(row,y) for row in nilpotent]
        f,g = [0],[0]
        for a,b,u in zip(y,ty,carrier):
            f,g = add(f,[a*c for c in u]),add(g,[b*c for c in u])
        need(ev(f,x)==ev(g,x)==0, "actual collision in composed carrier")
        common = gcd(f,g)
        heights.add(max(len(divide(f,common)[0]),len(divide(g,common)[0]))-1)
    need(bases==2 and heights=={2}, "actual degree-two height and rank-one fibre")
    print("PASS coprime composition P=X^2,Q=X^2+1; actual collision height2; two base coordinates")
    print("Conic evaluation alone does NOT imply conic kernel; universal proof is written")


if __name__ == "__main__":
    main()
