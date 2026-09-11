"""Exact all-primitive-degree branch-energy prices, with inherited image payment."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
OLD = NODE.parent/"rate_half_mca_regular_terminal_low_image_degree_frontier/certificate.json"
OLD_PIN = "6d5677e763c53bd135cbf244f75c3e974bf97e21a4cee285a53d3ac561332f4e"
R, D = 1048576, 67472
GATES = [(4,5,5,6),(4,5,5,6),(4,4,5,5),(4,4,4,5),(3,4,4,4),
         (4,4,4,4),(4,4,5,5),(4,4,5,5),(4,5,5,5),(4,5,5,5),
         (4,5,5,5),(4,5,6,6),(4,5,6,6)]
SCOPE = dict(original_error_rank=12, actual_P2_rank=19, J=[9965,21499],
             anchors=8, terminal_dimension=3, pencil_free=True,
             eigenvalues_field="original F", raw_cutoffs=[1,2],
             primitive_degree="actual degree of U0/G, all eta+1<=kappa<=J1-8",
             degree_slack="every v>=0; original full gcd and unused degree retained",
             normalization_degree="nu=(kappa-1)/eta; finite flat normalization map",
             finite_fibre_bound="nu times geometric branch count, not nu alone",
             branch_budget="sum binom(b_p,2)<=binom(eta-1,2), from planarity",
             pair_budget="disjoint chosen actual groups, C<=binom(M,2)",
             squared_gate="Z>0 and Z^2>(N+2nu*g)(N+8nu*P)",
             coverage="new eta range up to old eta0-1; inherited payment above",
             original_weights_unchanged=True, whole_constant_upper_tail_open=True,
             available_weight_maximum=272127061148955779,
             B_star=274980728111395087, near=134944,
             rank19_closed=False, whole_degree_closed=False, prize_closed=False)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(data):
    return (json.dumps(data, indent=2)+"\n").encode()


def piece(eta, e, t, k, gate, allowance):
    weight = R-D+t
    m = int(Q(*map(int, allowance))/weight)+1
    p = m*(m-1)//2
    q1, qbar = (R-gate)//(D+1-t), (R-k+2)//(D-k+2-t)
    need(2*q1 <= qbar, "eigen-root capacity hypotheses")
    c2 = (0, 2*qbar, 2*(qbar+q1), 3*qbar)[e]
    g = (eta-1)*(eta-2)//2
    z0, z1 = 2*m*(D-t)+c2-R, 2*m-c2-1
    u0, u1 = eta*R-2*g, eta+2*g
    v0, v1 = eta*R-8*p, eta+8*p
    coeff = [eta*eta*z0*z0-u0*v0,
             2*eta*eta*z0*z1-u0*v1-u1*v0,
             eta*eta*z1*z1-u1*v1]
    c, b, a = coeff
    lo, hi = eta+1, k
    endpoints = [a*x*x+b*x+c for x in (lo, hi)]
    vertex = 4*a*c-b*b if a>0 and 2*a*lo<=-b<=2*a*hi else None
    positive_z = [z0+z1*x for x in (lo, hi)]
    v_derivatives = [2*eta*eta*(2*m-1)*(z0+z1*x)
                     -eta*(u0+v0+(u1+v1)*x) for x in (lo, hi)]
    need(min(positive_z)>0 and min(endpoints)>0
         and (vertex is None or vertex>0), "strict whole-kappa branch energy")
    need(min(v_derivatives)>=0, "all degree slack v>=0")
    return dict(eta=eta, t=t, kappa=[lo,hi], allowance=allowance,
                original_pair_weight=weight, M=m, P=p, q1=q1, qbar=qbar,
                root_cost_twice=c2, branch_budget=g, energy_coefficients=coeff,
                energy_endpoints=endpoints, vertex_discriminant=vertex,
                positive_Z_endpoints=positive_z, v_derivative_endpoints=v_derivatives,
                v2=4*eta*eta*m*(m-1), paid_terminal_weight=(m-1)*weight)


def build():
    raw = OLD.read_bytes()
    need(sha(raw)==OLD_PIN, "inherited image certificate custody")
    old = json.loads(raw)
    need(len(old["profiles"])==len(GATES)==13, "inherited profile inventory")
    shards, entries = {}, []
    count = improvements = 0
    for parent, gates in zip(old["profiles"], GATES):
        ends = parent["J"]
        k, gate = ends[1]-8, parent["original_constant_gate"]
        need(k==parent["kappa_max"], "original primitive degree ceiling")
        rows = []
        for spectrum, new in zip(parent["spectra"], gates):
            e, before = spectrum["e"], spectrum["eta0"]
            need(2<=new<=before, "combined image threshold")
            checks = [piece(eta,e,t,k,gate,spectrum["cutoffs"][t-1]["allowance"])
                      for eta in range(new,before) for t in (1,2)]
            count += len(checks)
            improvements += int(new<before)
            rows.append(dict(e=e, eta0=new, inherited_eta0=before, checks=checks))
        shard = dict(schema="regular-branch-energy-profile-v1", J=ends,
                     old_certificate_sha256=OLD_PIN, original_constant_gate=gate, spectra=rows)
        name = str(ends[0])+".json"
        shards[name] = encoded(shard)
        entries.append(dict(path=name,sha256=sha(shards[name]),J=ends,eta0=list(gates)))
    index = dict(schema="regular-branch-energy-frontier-v1", scope=SCOPE,
                 old_certificate_sha256=OLD_PIN, profiles=entries, profile_count=13,
                 spectral_gate_count=52, new_strict_prices=count,
                 improved_spectral_gates=improvements,
                 uniform_image_thresholds=[max(row[e] for row in GATES) for e in range(4)],
                 maximum_surviving_image_degree=5)
    return index, shards


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    index, shards = build()
    target = NODE/"certificates"
    if args.write:
        target.mkdir(exist_ok=True)
        for name, data in shards.items():
            (target/name).write_bytes(data)
        (target/"index.json").write_bytes(encoded(index))
    need((target/"index.json").read_bytes()==encoded(index), "stored index differs")
    for name, data in shards.items():
        need((target/name).read_bytes()==data, "stored profile differs")
    for row in index["profiles"]:
        print("COMBINED", row["J"], row["eta0"])
    print("PASS", index["new_strict_prices"], "new whole-kappa/all-v strict prices;",
          index["improved_spectral_gates"], "improved spectral gates")
    print("UNIFORM", index["uniform_image_thresholds"], "INDEX", sha(encoded(index)))
    print("Image degrees2..5 and whole constant upper tail remain; no rank19 or Prize closure")


if __name__ == "__main__":
    main()
