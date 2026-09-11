"""Offline, bounded replay of the double-conic terminal payment."""

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
MANIFEST_HASH = "d4b34801f0d3d1ef8f6718e49a7c6efddf3ed5a9e3a6c0fb88969ff38cab4541"
PARENT = "cf6cd480113732d04314a93ffdbaff655b6dfd22"
PRIOR = "kb-regular-terminal-branch-genus-energy-20260911"
HELPER_HASH = "545f33a6cd29816f350b1d0904af2bb39353a313cf80920baa27ff1447aced13"
ROOTS = ["pair_space_conic_kernel_geometry",
         "conic_direction_subset_forest_bound",
         "rate_half_mca_double_conic_terminal_payment"]
SCOPE = dict(
    lane="K3 / DIRECT", object="MCA", agreement=1116048,
    field="2130706433^6", target_epsilon="2^-128",
    original_error_rank=12, shared_carrier_dimension=11, J=[9965,21499],
    actual_P2_rank=19, anchors=8, terminal_enclosure_dimension=3,
    B_star="274980728111395087", near=134944,
    terminal_bound_scope="Pencil-free regular3 terminals after proved original large-pencil source alternatives are removed",
    raw_cutoffs=[1,2], evaluation_image_degree=2, kernel_image_degree=2,
    primitive_degree="kappa=1+actual max degree(U0/G)=2nu+1",
    degree_slack="v=J-8-kappa-distinct nonanchor G roots, every v>=0",
    normalization_degree="nu=(kappa-1)/2, original-field conic parametrization",
    finite_fibre_bound="l_p<=nu, including ramification and inseparability",
    collision_height="nu for non-eigen actual collision directions",
    nonconstant_collision_line_caps=[6,7], rank_one_plane_cap=15,
    rank_one_fibre_incidence="at most30nu; other eigen roots retained",
    graph="distinct null-line trees: triangle-free, at most two common neighbours per triple",
    subset_cost="f(r)=s*r/M-1+binom(M-r,s)/binom(M,s)",
    incidence_price="M*A_v<=30nu+a*N_v+b*nu*K_s, a>=1 and b>=0",
    strict_reverse="positive affine nu/v gap for every actual primitive degree and slack",
    profiles=13, raw_prices=26, minimum_gap="271760328/2795",
    double_conic_class_paid=True, excessive_conic_kernel_degrees=[3,4],
    maximum_surviving_image_degree=5, whole_constant_unpaid_tail=[14965,21499],
    available_weight_test_maximum="272127061148955779",
    available_weight_test_reserve="2853666962439308",
    original_weights_unchanged=True, higher_raw_and_near_included_once=True,
    all_terminals_covered=False, rank19_closed=False, active_v4_atom=False,
    whole_degree_closed=False, prize_closed=False,
)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_prior():
    path = ROOT.parent/PRIOR/"replay.py"
    need(not path.is_symlink() and path.stat().st_size < 65536, "prior helper path")
    need(digest(path.read_bytes()) == HELPER_HASH, "prior helper pin")
    spec = importlib.util.spec_from_file_location("frozen_branch_custody", path)
    branch = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(branch)
    prior, published, graph, pins = branch.load_prior()
    raw = prior.checked_file(branch.ROOT, "SOURCE_MANIFEST.json")
    need(digest(raw) == branch.MANIFEST_HASH, "parent manifest pin")
    manifest = json.loads(raw)
    sources = branch.validate(manifest, prior, published, graph, pins)
    published.update({(PRIOR, path): data for path, data in sources.items()})
    graph.update(manifest["requirements"])
    need(len(published) == 1312, "inherited source inventory")
    return prior, published, graph, dict(pins, **{PRIOR: branch.MANIFEST_HASH})


def validate(manifest, prior, published, credited, pins):
    need(manifest["schema"] == "kb-regular-terminal-double-conic-payment-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == pins, "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 373
         and manifest["published_source_hashes_checked"] == 1312, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 48, "new file inventory")
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
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 122861,
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
    need(len(documents) == 373, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 121 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
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
    print("PASS 1360 listed hashes; 373 inherited documents; 121-node acyclic closure;",
          mutations(manifest, prior, published, graph, pins), "malformed manifests rejected", flush=True)
    inherited = ["pair_space_operator_branch_genus_energy",
                 "rate_half_mca_regular_terminal_genus_energy_frontier",
                 "pair_space_operator_eigen_root_incidence",
                 "rate_half_mca_regular_terminal_eigen_capacity_frontier",
                 "pair_space_operator_collision_interpolation",
                 "rate_half_mca_regular_terminal_low_image_degree_frontier"]
    terminal = "rate_half_mca_regular_rational_plane_terminal_bounds"
    borrowed = {}
    for (_, relative), data in published.items():
        parts = PurePosixPath(relative).parts
        if len(parts) >= 5 and parts[:3] == ("source", "background", "nodes") and parts[3] in inherited+[terminal]:
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
              (ROOTS[2], "verify.py"), (ROOTS[2], "verify_audit.py"),
              (inherited[0], "verify.py"), (inherited[1], "verify.py"),
              (inherited[1], "verify_audit.py"), (terminal, "verify_audit.py")]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-double-conic-payment-") as temp:
        runtime = Path(temp)
        for relative, data in {**borrowed, **sources}.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for name, filename in checks:
            path = runtime/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS four new and four inherited focused checks from frozen sources")
    print("Other inherited arithmetic not freshly replayed; independent mathematical review due")
    print("Conic kernel degrees3/4, image degrees3..5, constant upper tail and both Prizes remain open")


if __name__ == "__main__":
    main()
