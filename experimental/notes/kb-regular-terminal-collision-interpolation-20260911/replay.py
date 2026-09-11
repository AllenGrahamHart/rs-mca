"""Offline replay of the eigen-incidence and collision-interpolation extension."""

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
MANIFEST_HASH = "4becaac656ccdc6194d8fd2e588ab4c2c2cf0ecbdb359f5acfc3a6782fd78861"
PARENT = "f328d9fb39991cfa699216c826014c3dfd2c0ee1"
PRIOR = "kb-regular-terminal-rich-core-fibres-20260911"
HELPER_HASH = "7d369a3b2ac3253aaa15b7e7441b790f43240d286a5d4fcc302fa91433d398c6"
ROOTS = [
    "pair_space_operator_eigen_root_incidence",
    "rate_half_mca_regular_terminal_eigen_capacity_frontier",
    "pair_space_operator_collision_interpolation",
    "rate_half_mca_regular_terminal_low_image_degree_frontier"
]
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
  "actual_P2_rank": 19,
  "anchors": 8,
  "terminal_enclosure_dimension": 3,
  "B_star": "274980728111395087",
  "near": 134944,
  "terminal_bound_scope": "Pencil-free regular3 terminals after proved original large-pencil source alternatives are removed",
  "eigenvalues_field": "original F",
  "eigenspaces_max_dimension": 1,
  "spectral_counts": [
    0,
    1,
    2,
    3
  ],
  "primitive_degree": "kappa=1+actual max degree(U0/G), every 3..J1-8",
  "degree_slack": "v=J-8-kappa-distinct nonanchor G roots, every v>=0",
  "uniform_intersection_caps": [
    2108,
    1985,
    1948,
    1866
  ],
  "uniform_image_thresholds": [
    9,
    10,
    11,
    11
  ],
  "maximum_surviving_image_degree": 10,
  "image_degree": "primitive homogeneous equation, not polynomial degree or map multiplicity",
  "collision_condition_count": "C=sum binom(r_p,2)<=binom(M,2), disjoint chosen actual groups",
  "product_rank": "H_eta(ell)=binom(ell+2,2)-binom(ell-eta+2,2)",
  "low_image_constraint": "Every first-unaffordable M-subset has C>=H_eta(ell)",
  "profiles": 13,
  "spectral_gates_per_calibration": 52,
  "cutoff_tests_per_calibration": 104,
  "actual_core_witness": true,
  "original_evaluation_flat_rank": 9,
  "generic_degree_used": false,
  "joint_evaluation_rank_two_required": false,
  "whole_constant_unpaid_tail": [
    14965,
    21499
  ],
  "available_weight_test_maximum": "272127061148955779",
  "available_weight_test_reserve": "2853666962439308",
  "original_weights_unchanged": true,
  "higher_raw_and_near_included_once": true,
  "all_terminals_covered": false,
  "rank19_closed": false,
  "active_v4_atom": false,
  "whole_degree_closed": false,
  "prize_closed": false
}''')


def need(ok, why):
    if not ok:
        raise ValueError(why)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_prior():
    path = ROOT.parent/PRIOR/"replay.py"
    need(not path.is_symlink() and path.stat().st_size < 65536, "prior helper path")
    need(digest(path.read_bytes()) == HELPER_HASH, "prior helper pin")
    spec = importlib.util.spec_from_file_location("frozen_rich_core_custody", path)
    rich = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rich)
    prior, published, graph = rich.load_prior()
    raw = prior.checked_file(rich.ROOT, "SOURCE_MANIFEST.json")
    need(digest(raw) == rich.MANIFEST_HASH, "parent manifest pin")
    manifest = json.loads(raw)
    parent_sources = rich.validate(manifest, prior, published, graph)
    published.update({(PRIOR, path): data for path, data in parent_sources.items()})
    graph.update(manifest["requirements"])
    need(len(published) == 1216, "inherited source inventory")
    pins = dict(manifest["supplier_manifests"], **{PRIOR: rich.MANIFEST_HASH})
    return prior, published, graph, pins


def validate(manifest, prior, published, credited, supplier_pins):
    need(manifest["schema"] == "kb-regular-terminal-collision-interpolation-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == supplier_pins,
         "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 345
         and manifest["published_source_hashes_checked"] == 1216, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 59, "new file inventory")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT/"source").rglob("*") if p.is_file()}
    need(actual == set(files), "unlisted/missing source")
    sources = {}
    for relative, row in files.items():
        need(relative == "source/"+row["origin_path"], "origin identity")
        parts = PurePosixPath(row["origin_path"]).parts
        need(len(parts) >= 4 and parts[:2] == ("background", "nodes")
             and parts[2] in ROOTS, "source scope")
        data = prior.checked_file(ROOT, relative)
        need(digest(data) == row["sha256"], "new source pin")
        sources[relative] = data
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 733664,
         "source byte inventory")
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
    need(len(documents) == 345, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 116 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
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
             and [edge["from"] for edge in node["requires"]] == deps, "new node status/graph")
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


def mutations(manifest, prior, published, graph, pins):
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
    for mode in ("duplicate", "missing", "cycle", "pin", "proof-pin"):
        bad = copy.deepcopy(manifest)
        if mode == "duplicate":
            bad["files"].append(bad["files"][0])
        elif mode == "missing":
            bad["files"].pop()
        elif mode == "cycle":
            bad["requirements"][ROOTS[0]].append(ROOTS[1])
        elif mode == "pin":
            bad["origin_node_manifest_sha256"][ROOTS[0]] = "0"*64
        else:
            bad["inherited_sources"][0]["sha256"] = "0"*64
        cases.append(bad)
    for bad in cases:
        try:
            validate(bad, prior, published, graph, pins)
        except (ValueError, KeyError, TypeError):
            continue
        raise ValueError("accepted malformed manifest")
    return len(cases)


def main():
    prior, published, graph, pins = load_prior()
    raw = prior.checked_file(ROOT, "SOURCE_MANIFEST.json")
    need(digest(raw) == MANIFEST_HASH, "manifest pin")
    manifest = json.loads(raw)
    sources = validate(manifest, prior, published, graph, pins)
    print("PASS 1275 listed hashes; 345 inherited documents; 116-node acyclic closure;",
          mutations(manifest, prior, published, graph, pins), "malformed manifests rejected", flush=True)
    borrowed = {}
    terminal = "rate_half_mca_regular_rational_plane_terminal_bounds"
    for (packet, relative), data in published.items():
        parts = PurePosixPath(relative).parts
        if len(parts) >= 5 and parts[:3] == ("source", "background", "nodes") and parts[3] == terminal:
            need(relative not in borrowed or borrowed[relative] == data, "runtime conflict")
            borrowed[relative] = data
    for name, filename in (
        ("pair_space_operator_spectral_fibre_johnson", "verify.py"),
        ("rate_half_mca_regular_terminal_rich_fibre_frontier", "certificate.json"),
        ("list_padded_johnson_dimension_descent", "compiler.py"),
        ("rate_half_mca_coupled_pair_rank_frontier", "verify_audit.py"),
        ("rate_half_mca_coupled_pair_rank_frontier", "source_certificate.json"),
        ("rate_half_mca_coupled_pair_rank_frontier", "gate_certificate.json"),
        ("rate_half_mca_coupled_pair_rank_frontier", "compression_certificate.json"),
    ):
        relative = "source/background/nodes/"+name+"/"+filename
        matches = [data for (_, path), data in published.items() if path == relative]
        need(matches and all(data == matches[0] for data in matches), "runtime supplier")
        borrowed[relative] = matches[0]
    need(not set(borrowed).intersection(sources), "runtime collision")
    checks = [(ROOTS[0], "verify.py"), (ROOTS[1], "verify.py"),
              (ROOTS[1], "verify_audit.py"), (ROOTS[2], "verify.py"),
              (ROOTS[3], "verify.py"), (ROOTS[3], "verify_audit.py"),
              (terminal, "verify_audit.py")]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-collision-interpolation-") as temp:
        runtime = Path(temp)
        for relative, data in {**borrowed, **sources}.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for name, filename in checks:
            path = runtime/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS six new checks and the inherited rational-plane independent audit")
    print("Other inherited arithmetic not freshly replayed; independent mathematical review due")
    print("Low-image terminal classes, constant upper tail and both Prize problems remain open")


if __name__ == "__main__":
    main()
