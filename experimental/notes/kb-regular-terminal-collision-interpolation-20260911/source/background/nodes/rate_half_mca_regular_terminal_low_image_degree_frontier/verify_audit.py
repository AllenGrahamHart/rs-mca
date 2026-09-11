"""Independent exact product-rank and original-incidence audit; no primary imports."""
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

NODE=Path(__file__).resolve().parent
PARENT=NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN="6d5677e763c53bd135cbf244f75c3e974bf97e21a4cee285a53d3ac561332f4e"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
CAPACITY_PIN="4c8ddb8396ce996e92fba3e12d6d96e87867668161e2cbbe710bf3de2dac501f"
R,D=1048576,67472
RANGES=[(9965,10964),(10965,11964),(11965,12964),(12965,13364),(13365,13964),
        (13965,14964),(14965,15964),(15965,16964),(16965,17964),(17965,18964),
        (18965,19964),(19965,20964),(20965,21499)]
SCOPE=dict(original_error_rank=12,actual_P2_rank=19,J=[9965,21499],anchors=8,
           terminal_dimension=3,pencil_free=True,eigenvalues_field="original F",
           raw_cutoffs=[1,2],image_degree="primitive homogeneous equation, not map degree or kappa",
           interpolation_rank="actual degree-ell product space, not all ternary forms",
           collision_cost="sum binom(r_p,2)<=binom(M,2), disjoint actual unordered pairs",
           pullback="nonzero polynomial with every actual multiplicity retained",
           primitive_degree="all 3..J1-8; actual degree and full polynomial gcd",
           degree_slack="every v>=0 retained",original_weights_unchanged=True,
           available_weight_maximum=272127061148955779,B_star=274980728111395087,near=134944,
           generic_fibre_used=False,finite_fibre_cap_assumed=False,
           whole_constant_upper_tail_open=True,rank19_closed=False,whole_degree_closed=False,
           prize_closed=False)

def need(ok,why):
    if not ok:
        raise ValueError(why)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def parents():
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"parent index custody")
    index=json.loads(raw)
    cap=NODE.parent/"rate_half_mca_regular_terminal_eigen_capacity_frontier/certificates/index.json"
    need(sha(cap.read_bytes())==CAPACITY_PIN,"capacity custody")
    out=[]
    maximum=0
    need(len(index["profiles"])==13,"parent coverage")
    for ref,ends in zip(index["profiles"],RANGES):
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent profile custody")
        p=json.loads(raw)
        need(p["J"]==list(ends),"parent degree interval")
        price=Q(p["mass_floor"],3)
        for t,den in ((1,2),(2,6)):
            factor=Q(1)
            for j in range(1,9):
                factor*=Q(R+j,D-t+j)
            price+=factor*Q(*map(int,p["terminals"][t-1]))/den
        value=price.numerator//price.denominator+134944
        need(value==p["weighted_envelope"]<=272127061148955779,"unchanged original weight envelope")
        maximum=max(maximum,value)
        out.append(dict(J=p["J"],allowances=p["terminals"],gate=p["heights"][0]["gate"],sha256=ref["sha256"]))
    need(maximum==272127061148955779,"unchanged maximum")
    return out

def values(m,t,e,eta,ell,k,g,allowance):
    q1=(R-g)//(D+1-t)
    qbar=(R-k+2)//(D-k+2-t)
    root_cost=(Q(0),Q(qbar),Q(qbar+q1),Q(3*qbar,2))[e]
    rank=comb(ell+2,2)-(comb(ell-eta+2,2) if ell>=eta else 0)
    lower=Q(m*(D+k-t))
    upper=Q(R+k)+(k-1)*(root_cost+ell)
    return dict(t=t,allowance=allowance,original_pair_weight=R-D+t,M=m,
                unordered_pair_budget=comb(m,2),ell=ell,product_rank=rank,q1=q1,qbar=qbar,
                root_cost_twice=int(2*root_cost),incidence_lower_twice=int(2*lower),
                incidence_upper_twice=int(2*upper),gap_twice=int(2*(lower-upper)),
                kappa_slope_twice=int(2*(m-1-ell-root_cost)),v_slope_twice=2*(m-1),
                paid_pair_cap=m-1,paid_terminal_weight=(m-1)*(R-D+t))

def validate(data,prior):
    keys={"schema","scope","parent_index_sha256","capacity_index_sha256","profiles",
          "profile_count","spectral_gate_count","cutoff_count","uniform_image_thresholds",
          "maximum_surviving_image_degree","minimum_gap_twice","maximum_interpolant_degree"}
    need(set(data)==keys and data["schema"]=="regular-low-image-degree-frontier-v1","schema")
    need(json.dumps(data["scope"],sort_keys=True)==json.dumps(SCOPE,sort_keys=True),"scope and types")
    need(data["parent_index_sha256"]==PARENT_PIN and data["capacity_index_sha256"]==CAPACITY_PIN,
         "required source pins")
    need(data["profile_count"]==13 and data["spectral_gate_count"]==52 and data["cutoff_count"]==104,
         "count pins")
    need(len(data["profiles"])==13,"profile inventory")
    uniform=[0]*4
    gaps=[]
    degrees=[]
    for row,parent,ends in zip(data["profiles"],prior,RANGES):
        need(set(row)=={"J","parent_sha256","kappa_max","original_constant_gate","spectra"}
             and row["J"]==list(ends)==parent["J"],"profile shape and interval")
        k,g=row["kappa_max"],row["original_constant_gate"]
        need(type(k) is int and k==ends[1]-8 and type(g) is int and g==parent["gate"]
             and row["parent_sha256"]==parent["sha256"],"original degree and pencil gate")
        need(len(row["spectra"])==4,"all original-field spectra")
        for e,spectrum in enumerate(row["spectra"]):
            need(set(spectrum)=={"e","eta0","cutoffs"} and type(spectrum["e"]) is int
                 and spectrum["e"]==e,"spectral identity")
            eta=spectrum["eta0"]
            need(type(eta) is int and eta>=2 and len(spectrum["cutoffs"])==2,"image degree and cutoffs")
            uniform[e]=max(uniform[e],eta)
            for t,cut in enumerate(spectrum["cutoffs"],1):
                need(cut["allowance"]==parent["allowances"][t-1],"unchanged rational allowance")
                need(all(type(value) is int for key,value in cut.items() if key!="allowance"),
                     "exact integer record")
                m,ell=cut["M"],cut["ell"]
                top,bottom=map(int,cut["allowance"])
                need(m>=2 and (m-1)*(R-D+t)*bottom<=top<m*(R-D+t)*bottom,
                     "first unaffordable actual pair count")
                need(ell>=m-1 and ell>=0,"whole-primitive-degree monotonicity")
                expected=values(m,t,e,eta,ell,k,g,cut["allowance"])
                need(cut==expected,"independent rank/incidence reconstruction")
                need(cut["product_rank"]>cut["unordered_pair_budget"],"nonzero pullback product rank")
                need(2*cut["q1"]<=cut["qbar"],"spectral root capacity")
                need(cut["kappa_slope_twice"]<=0<cut["v_slope_twice"],"all-gcd and degree-slack transfer")
                need(cut["gap_twice"]>0,"strict original incidence price")
                need(cut["paid_terminal_weight"]*bottom<=top,"original terminal allowance")
                gaps.append(cut["gap_twice"])
                degrees.append(ell)
    need(uniform==data["uniform_image_thresholds"]==[9,10,11,11],"whole-gap image thresholds")
    need(data["maximum_surviving_image_degree"]==max(uniform)-1==10,"correct residual endpoint")
    need(data["minimum_gap_twice"]==min(gaps)==7140 and data["maximum_interpolant_degree"]==max(degrees)==207,
         "exact aggregate margins")
    return len(gaps)

def mutations(data,prior):
    count=0
    def reject(bad,reason=None):
        nonlocal count
        try:
            validate(bad,prior)
        except (ValueError,KeyError,TypeError) as error:
            if reason is not None:
                need(str(error)==reason,"wrong mutation rejection: "+str(error))
            count+=1
            return
        raise ValueError("accepted malformed incidence claim")
    for key in SCOPE:
        bad=copy.deepcopy(data)
        bad["scope"][key]=None
        reject(bad)
    for key,value in (("schema","wrong"),("parent_index_sha256","0"*64),
                      ("capacity_index_sha256","0"*64),("profiles",[]),("cutoff_count",0),
                      ("maximum_surviving_image_degree",11),("minimum_gap_twice",1)):
        bad=copy.deepcopy(data)
        bad[key]=value
        reject(bad)
    for mode in ("interval-hole","source-pin","source-gate","kappa","spectrum-hole","eta-bool",
                 "reset-weight","wrong-M","ambient-rank","pair-cost","root-charge","allowance",
                 "slack-sign","lower-eta-recomputed","smaller-ell-recomputed"):
        bad=copy.deepcopy(data)
        row=bad["profiles"][-1]
        spectrum=row["spectra"][1]
        cut=spectrum["cutoffs"][1]
        if mode=="interval-hole": row["J"][0]+=1
        elif mode=="source-pin": row["parent_sha256"]="0"*64
        elif mode=="source-gate": row["original_constant_gate"]+=1
        elif mode=="kappa": row["kappa_max"]-=1
        elif mode=="spectrum-hole": row["spectra"].pop()
        elif mode=="eta-bool": spectrum["eta0"]=True
        elif mode=="reset-weight": cut["original_pair_weight"]-=8
        elif mode=="wrong-M": cut["M"]-=1
        elif mode=="ambient-rank": cut["product_rank"]=comb(cut["ell"]+2,2)
        elif mode=="pair-cost": cut["unordered_pair_budget"]=cut["M"]-1
        elif mode=="root-charge": cut["root_cost_twice"]=0
        elif mode=="allowance": cut["allowance"][0]=str(int(cut["allowance"][0])+1)
        elif mode=="slack-sign": cut["v_slope_twice"]*=-1
        else:
            if mode=="lower-eta-recomputed": spectrum["eta0"]-=1
            for i,old in enumerate(spectrum["cutoffs"]):
                eta=spectrum["eta0"]
                ell=old["ell"]-1
                if mode=="lower-eta-recomputed":
                    ell=old["ell"]
                    while comb(ell+2,2)-comb(ell-eta+2,2)<=comb(old["M"],2):
                        ell+=1
                spectrum["cutoffs"][i]=values(old["M"],i+1,1,eta,ell,row["kappa_max"],
                                               row["original_constant_gate"],old["allowance"])
        expected="strict original incidence price" if mode=="lower-eta-recomputed" else None
        if mode=="smaller-ell-recomputed": expected="nonzero pullback product rank"
        reject(bad,expected)
    return count

def main():
    raw=(NODE/"certificate.json").read_bytes()
    need(sha(raw)==PIN,"certificate custody")
    data=json.loads(raw)
    prior=parents()
    checks=validate(data,prior)
    rejected=mutations(data,prior)
    print("PASS independent",checks,"product-rank and strict original-incidence prices")
    print("PASS",rejected,"mutations; fully recomputed lower eta and smaller ell rejected at their mathematical gates")
    print("All primitive degrees, gcds and degree slack covered; uniform image thresholds [9,10,11,11]")
    print("Eta<=10, whole-constant upper tail and both Prize problems remain open")

if __name__=="__main__":
    main()
