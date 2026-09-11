"""All small-normalization spectral/eta prices at unchanged source allowances."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
OLD = NODE.parent/"rate_half_mca_regular_terminal_low_image_degree_frontier/certificate.json"
OLD_PIN = "6d5677e763c53bd135cbf244f75c3e974bf97e21a4cee285a53d3ac561332f4e"
R,D = 1048576,67472
SCOPE = dict(original_error_rank=12,actual_P2_rank=19,J=[9965,21499],
             original_shared_dimension=11,anchors=8,terminal_dimension=3,
             pencil_free=True,raw_cutoffs=[1,2],image_degrees=[2,3,4,5],spectra=[0,1,2,3],
             normalization_ceiling="floor((J1-1)/10), from the original dimension11 carrier",
             primitive_degree="kappa=eta*nu+1, actual full-gcd degree",
             slack="every v>=0, not assumed saturated",
             spectral_capacity="old full profile degree ceiling, not improved silently",
             original_weights_unchanged=True,remaining_pencil_free_requires_actual_degree_jump=True,
             segre_coordinates="branch weighted; generic centres are not actual anchors",
             anchor_guard_globally_affordable=False,whole_constant_upper_tail_open=True,
             source_maximum=272127061148955779,B_star=274980728111395087,near=134944,
             whole_degree_closed=False,rank19_closed=False,prize_closed=False)


def need(ok,why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(data):
    return (json.dumps(data,indent=2)+"\n").encode()


def price(row,e,t,eta,allowance):
    h = (row["J"][1]-1)//10
    k = row["kappa_max"]
    m = int(Q(*map(int,allowance))/(R-D+t))+1
    q1 = (R-row["original_constant_gate"])//(D+1-t)
    qbar = (R-k+2)//(D-k+2-t)
    need(2*q1<=qbar and eta*h+1<=k,"old degree/capacity envelope")
    c2 = (0,2*qbar,2*(qbar+q1),3*qbar)[e]
    pairs,g = m*(m-1)//2,(eta-1)*(eta-2)//2
    z0,z1 = 2*m*(D+1-t)-(R+1),eta*(2*m-1-c2)
    u,v = eta+2*g,eta+8*pairs
    c,b,a = z0*z0-(R+1)**2,2*z0*z1-(R+1)*(u+v),z1*z1-u*v
    endpoints = [a*x*x+b*x+c for x in (1,h)]
    vertex = 4*a*c-b*b if a>0 and 2*a<=-b<=2*a*h else None
    positive_z = [z0+z1*x for x in (1,h)]
    derivatives = [2*(2*m-1)*(z0+z1*x)-2*(R+1)-(u+v)*x for x in (1,h)]
    need(min(endpoints)>0 and (vertex is None or vertex>0) and min(positive_z)>0,
         "strict all-nu energy price")
    need(min(derivatives)>=0,"all-v extension")
    return dict(e=e,t=t,eta=eta,nu=[1,h],M=m,allowance=allowance,
                original_pair_weight=R-D+t,q1=q1,qbar=qbar,root_cost_twice=c2,
                branch_budget=g,pair_budget=pairs,energy_coefficients=[c,b,a],
                energy_endpoints=endpoints,vertex_discriminant=vertex,
                positive_Z_endpoints=positive_z,v_derivative_endpoints=derivatives,
                v2=4*m*(m-1),paid_terminal_weight=(m-1)*(R-D+t))


def build():
    raw = OLD.read_bytes()
    need(sha(raw)==OLD_PIN,"inherited image certificate custody")
    old = json.loads(raw)
    need(len(old["profiles"])==13,"profile inventory")
    entries,shards = [],{}
    next_j,count = 9965,0
    for row in old["profiles"]:
        need(row["J"][0]==next_j and row["kappa_max"]==row["J"][1]-8,"consecutive source degrees")
        next_j = row["J"][1]+1
        prices = [price(row,e,t,eta,row["spectra"][e]["cutoffs"][t-1]["allowance"])
                  for e in range(4) for eta in range(2,6) for t in (1,2)]
        count += len(prices)
        shard = dict(schema="inherited-normalization-profile-v1",J=row["J"],
                     old_certificate_sha256=OLD_PIN,prices=prices)
        name = str(row["J"][0])+".json"
        shards[name] = encode(shard)
        entries.append(dict(path=name,sha256=sha(shards[name]),J=row["J"],
                            normalization_ceiling=(row["J"][1]-1)//10))
    need(next_j==21500 and count==416,"complete original interval and prices")
    index = dict(schema="inherited-normalization-frontier-v1",scope=SCOPE,
                 old_certificate_sha256=OLD_PIN,profiles=entries,profile_count=13,
                 exact_prices=count,all_jump_free_pencil_free_paths_paid=True)
    return index,shards


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args = parser.parse_args()
    index,shards = build()
    target = NODE/"certificates"
    if args.write:
        target.mkdir(exist_ok=True)
        for name,data in shards.items():
            (target/name).write_bytes(data)
        (target/"index.json").write_bytes(encode(index))
    need((target/"index.json").read_bytes()==encode(index),"stored index")
    for name,data in shards.items():
        need((target/name).read_bytes()==data,"stored shard")
    print("PASS416 exact eta2..5 spectral/raw prices, every nu and v; original allowances unchanged")
    print("CAPS",[r["normalization_ceiling"] for r in index["profiles"]])
    print("INDEX",sha(encode(index)))
    print("Excess forces an ACTUAL nonbirational anchor; selection schedule and constant tail remain open")


if __name__ == "__main__":
    main()
