"""Finite algebraic control; not an official MCA source experiment."""
def need(ok,why):
    if not ok:
        raise ValueError(why)


def cross(a,b,p):
    return tuple((a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3])%p for i in range(3))


def projective(a,p):
    first=next((x for x in a if x%p),None)
    need(first is not None,"nonzero projective vector")
    return tuple(x*pow(first,-1,p)%p for x in a)


def main():
    p=101
    hits=[]
    inverse_checks=0
    for x in range(p):
        v=(x**3-x)%p
        w=(x**4-x*x)%p
        ell=(1,v,w)
        d=cross(ell,(v,w,1),p)
        explicit=((v-w*w)%p,(v*w-1)%p,(w-v*v)%p)
        need(d==explicit and any(d),"polynomial kernel and joint rank2")
        if projective(d,p)==(0,1,0):
            hits.append(x)
        td=(d[2],d[0],d[1])
        recovered=cross(d,td,p)
        if any(recovered):
            need(projective(recovered,p)==ell,"projective inverse to the evaluation vector")
            if recovered[1]:
                need(recovered[2]*pow(recovered[1],-1,p)%p==x,"generic rational coordinate inverse")
                inverse_checks+=1
        need((v==0 and w==0)==(x in (0,1,100)),"joint intersection of candidate pairs")
    need(hits==[0,1,100] and inverse_checks>0,"exceptional fibre and nonempty inverse chart")
    need(p>7 and (8-1)%p!=0,"characteristic guard")
    print("PASS 101 everywhere-joint-rank2 coordinates; exact triple fibre",hits)
    print("PASS",inverse_checks,"rational inverse controls; degrees8/7/6 give pencil-freeness in the proof")
    print("No original large-agreement source, full-code badness or unsafe Prize witness constructed")


if __name__=="__main__":
    main()
