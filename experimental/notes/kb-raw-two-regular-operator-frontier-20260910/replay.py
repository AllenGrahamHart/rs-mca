"""Replay the frozen raw-two projection and regular operator extension offline."""

import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
MANIFEST_HASH = "05224b61e5b914ef799e1718ce6308d74f04e7d9de0c39a03d5f761b4df4a3c6"
PARENT = "ff28dfa41606dd73bd65a5442855fa577566cb35"
ROOTS = [
    "rate_half_mca_raw_two_quadratic_normal_payment",
    "rate_half_mca_raw_two_projection_regular_frontier",
    "pair_space_regular_projection_anchor",
    "rate_half_mca_regular_operator_terminal_reduction"
]
SUPPLIERS = {
    "low-core-flat-source-cumulative-20260908": "656b342982896233bf8f906b6ba93aae785c9179414d02f982f47b095a60027b",
    "kb-parameter-graph-spread-20260908": "b93f34d83b297e4370a4d6cb3b949432f99ebb4293b059fc7a926fd6b427ce1c",
    "kb-low-defect-rank-filtration-20260909": "bc3b337d2c369a06ab82d5d6d5a2fa8f9edfe2931f34e0244b94345286d42645",
    "kb-raw-mass-cubic-interval-20260909": "375c15045f34386d787b559a8705fc1c1f66653ce5a6568630a2d0f79ee75bbc",
    "kb-low-pair-pencil-payment-20260909": "c17dcfa6c844ceb0ae5f1a5bd578f4edd7b58d10048ae317528bfd37ebad43ce",
    "kb-dominant-pencil-rank-eleven-20260909": "8177b2bf76089547514d9d84f111eed4ada89d62c029bfa47e267ee6299f7416",
    "kb-shared-carrier-rank-fifteen-20260909": "f998e2205389157690fae7f3387aedc6cd6602a1135b2066283d552e9dd1829e",
    "kb-low-defect-hyperplanes-quadrics-20260910": "e36c4d33ba2357fe313a3788d6f46ea5da7b1b1d2438b796febd914d611e72d3",
    "kb-low-pair-projection-frontier-20260910": "01a2397889f1df87b3885fd66f192bd1af2236bfb4ea67ad7a747e1752c2a4fe",
    "kb-high44-pair-rank-extension-20260910": "233dc3d60a09b03ecb9b1101600703b30e2942106e424fff9acd1762b05a11ef",
    "kb-min-envelope-low-defect-rank-20260910": "36395ad03690b56a49e052c564cb7422b446799c4e1dc9f09eb67cb2332dfa34",
    "kb-source-bound-integer-compression-rank18-20260910": "b75350a4f7e40db3b403eedccdccc60114b828811f37ddce3d62c2479f4a6676"
}
SCOPE = json.loads(r'''{
    "lane": "K3 / DIRECT",
    "object": "MCA",
    "agreement": 1116048,
    "field": "2130706433^6",
    "original_error_rank": 12,
    "shared_carrier_dimension": 11,
    "J": [
        9965,
        21499
    ],
    "B_star": "274980728111395087",
    "near": 134944,
    "quadratic": {
        "graph_bound": "252231263277797075",
        "contained_lines_bound": "252214244730017023",
        "outside_low_labels_min": "34124197250397019",
        "raw_max": 2,
        "basis_support_parameter": 7
    },
    "deficient_projection_source_bound": "274462040894062110",
    "surviving_actual_P2_ranks": [
        19,
        22
    ],
    "generic_projection": "full over F(z); not realized-image coverage",
    "finite_rank_drop_maxima": [
        3,
        2,
        1,
        0
    ],
    "operator_terminals": [
        [
            19,
            8,
            3
        ],
        [
            20,
            9,
            2
        ],
        [
            21,
            10,
            1
        ],
        [
            22,
            11,
            0
        ]
    ],
    "weight_factor": "product_(j=1)^(r-11) (1048576+j)/(67472-t+j), t=1,2",
    "strict_anchor_guard": "pair rank > shared dimension; annihilator-of-generic-kernel exclusion",
    "original_weights_unchanged": true,
    "affordable_regular_terminal_bound": false,
    "higher_raw_and_near_included_once": true,
    "active_v4_atom": false,
    "whole_degree_closed": false,
    "prize_closed": false
}''')


def need(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_file(root, relative):
    need(isinstance(relative, str), "path type")
    path = PurePosixPath(relative)
    need(not path.is_absolute() and ".." not in path.parts and str(path) == relative,
         "canonical relative path")
    need(not any((root/Path(*path.parts[:i])).is_symlink()
                 for i in range(1, len(path.parts)+1)), "source symlink")
    target = root/path
    need(target.resolve().is_relative_to(root.resolve()) and target.is_file()
         and target.stat().st_size < 1024*1024, "missing/escaping/oversized source")
    return target.read_bytes()


def suppliers():
    sources, graph = {}, {}
    for packet, pin in SUPPLIERS.items():
        folder = ROOT.parent/packet
        data = checked_file(folder, "SOURCE_MANIFEST.json")
        need(digest(data) == pin, "changed supplier manifest")
        manifest = json.loads(data)
        # Later pinned packets supersede older interval-assembly snapshots.
        graph.update(manifest.get("requirements", manifest.get("interval_extension_requirements", {})))
        for row in manifest["files"]:
            key = packet, row["path"]
            need(key not in sources and row["path"].startswith("source/"), "supplier identity")
            data = checked_file(folder, row["path"])
            need(digest(data) == row["sha256"], "changed published source")
            sources[key] = data
    need(len(sources) == 1100, "published source inventory")
    return sources, graph


def validate(manifest, published, credited):
    need(manifest["schema"] == "kb-raw-two-regular-operator-frontier-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot pins")
    need(manifest["supplier_manifests"] == SUPPLIERS and manifest["scope"] == SCOPE,
         "supplier pins and theorem scope")
    need(manifest["inherited_proof_documents_compared"] == 313
         and manifest["published_source_hashes_checked"] == 1100, "comparison inventory")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 38, "new source inventory")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT/"source").rglob("*") if p.is_file()}
    need(actual == set(files), "missing/unlisted source")
    sources = {}
    for relative, row in files.items():
        need(relative == "source/"+row["origin_path"], "origin path")
        path = PurePosixPath(row["origin_path"])
        need(len(path.parts) == 4 and path.parts[:2] == ("background", "nodes")
             and path.parts[2] in ROOTS, "unexpected source")
        data = checked_file(ROOT, relative)
        need(digest(data) == row["sha256"], "changed new source")
        sources[relative] = data
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 50656, "new source size")
    documents = {}
    for row in manifest["inherited_sources"]:
        key = row["node"], row["filename"]
        need(key not in documents, "duplicate inherited document")
        data = published[row["packet"], row["path"]]
        parts = PurePosixPath(row["path"]).parts
        need(parts[0] == "source" and parts[2] == "nodes" and parts[3] == row["node"]
             and "/".join(parts[4:]) == row["filename"], "inherited identity")
        need(digest(data) == row["sha256"], "inherited document pin")
        documents[key] = data
    need(len(documents) == 313, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 107 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
         "closure inventory")
    for name, deps in graph.items():
        if name not in ROOTS:
            need(deps == credited[name], "inherited dependency drift")
            need(all((name, f) in documents for f in ("statement.md", "proof.md")),
                 "missing inherited proof")
            continue
        prefix = "source/background/nodes/"+name+"/"
        data = sources[prefix+"node.json"]
        need(digest(data) == manifest["origin_node_manifest_sha256"][name], "new node provenance")
        node = json.loads(data)
        need(node["node"]["id"] == name and node["node"]["status"] == "PROVED"
             and [e["from"] for e in node["requires"]] == deps, "new node status/graph")
        need(all(prefix+f in sources for f in ("statement.md", "proof.md")), "missing new proof")
    active, done = set(), set()

    def visit(name):
        need(name not in active, "dependency cycle")
        if name in done:
            return
        active.add(name)
        for child in graph[name]:
            visit(child)
        active.remove(name)
        done.add(name)

    for name in ROOTS:
        visit(name)
    need(done == set(graph), "unreachable dependency")
    return sources


def mutations(manifest, published, credited):
    cases = []
    for key, value in {"schema": "wrong", "parent_commit": "0"*40, "snapshot_roots": [],
                       "supplier_manifests": {}, "inherited_sources": [], "source_bytes": 0}.items():
        bad = copy.deepcopy(manifest)
        bad[key] = value
        cases.append(bad)
    for key in SCOPE:
        bad = copy.deepcopy(manifest)
        bad["scope"][key] = None
        cases.append(bad)
    for key, value in (("path", "../../escape"), ("origin_path", "wrong"), ("sha256", "0"*64)):
        bad = copy.deepcopy(manifest)
        bad["files"][0][key] = value
        cases.append(bad)
    for mutation in ("duplicate", "missing", "cycle", "pin", "proof-pin"):
        bad = copy.deepcopy(manifest)
        if mutation == "duplicate":
            bad["files"].append(bad["files"][0])
        elif mutation == "missing":
            bad["files"].pop()
        elif mutation == "cycle":
            bad["requirements"][ROOTS[0]].append(ROOTS[-1])
        elif mutation == "pin":
            bad["origin_node_manifest_sha256"][ROOTS[0]] = "0"*64
        else:
            bad["inherited_sources"][0]["sha256"] = "0"*64
        cases.append(bad)
    for bad in cases:
        try:
            validate(bad, published, credited)
        except (ValueError, KeyError):
            continue
        raise ValueError("accepted malformed manifest")
    return len(cases)


def main():
    data = checked_file(ROOT, "SOURCE_MANIFEST.json")
    need(digest(data) == MANIFEST_HASH, "manifest pin")
    manifest = json.loads(data)
    published, credited = suppliers()
    sources = validate(manifest, published, credited)
    print("PASS 1138 listed hashes; 313 inherited proof documents; 107-node acyclic closure;",
          mutations(manifest, published, credited), "malformed manifests rejected", flush=True)
    borrowed = {}
    for name, filename in (("rate_half_mca_moving_normal_basis_payment", "verify.py"),
                           ("rate_half_mca_moving_normal_basis_payment", "verify_audit.py"),
                           ("mca_min_envelope_fiber_contraction", "polynomial.py"),
                           ("rate_half_mca_min_envelope_raw_mass", "verify.py"),
                           ("rate_half_mca_min_envelope_raw_mass", "verify_audit.py")):
        relative = "source/background/nodes/"+name+"/"+filename
        matches = [data for (_, path), data in published.items() if path == relative]
        need(matches and all(data == matches[0] for data in matches), "missing/drifted runtime supplier")
        borrowed[relative] = matches[0]
    need(not set(borrowed).intersection(sources), "runtime collision")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-regular-operator-") as temp:
        runtime = Path(temp)
        for relative, data in {**borrowed, **sources}.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        checks = [("background", name, f) for name in ROOTS for f in ("verify.py", "verify_audit.py")
                  if "source/background/nodes/"+name+"/"+f in sources]
        need(len(checks) == 5, "five new focused checks")
        checks += [("background", "rate_half_mca_moving_normal_basis_payment", "verify.py"),
                   ("background", "rate_half_mca_moving_normal_basis_payment", "verify_audit.py"),
                   ("background", "rate_half_mca_min_envelope_raw_mass", "verify.py"),
                   ("background", "rate_half_mca_min_envelope_raw_mass", "verify_audit.py")]
        for section, name, filename in checks:
            path = runtime/"source"/section/"nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS five new focused checks plus four inherited basis/resource checks")
    print("Other inherited arithmetic not freshly replayed; independent mathematical review due")
    print("Remaining pair ranks, full degree interval, active atoms and both Prize problems remain open")


if __name__ == "__main__":
    main()
