"""Offline, bounded replay of graded-anchor and nonconstant-pencil payments."""

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
MANIFEST_HASH = "5386cd171d87beaf998dfb78bf45ae096b7e2014163f7093788ab1981c2a2cf6"
PARENT = "bf84251a1937e98fdb7c6d3937f8ef5b64ae37d1"
PRIOR = "kb-regular-terminal-inherited-normalization-20260911"
HELPER_HASH = "bffee0f60910035e2b9a94e4980b50d021d7ae9d532b4debded55218b48f453c"
ROOTS = ["rational_curve_inner_projection_multiplicity_budget","pair_space_graded_inner_projection_incidence","rate_half_mca_pencil_free_penultimate_payment","pair_space_nonconstant_pencil_regular_children","rate_half_mca_nonconstant_pencil_penultimate_payment","rate_half_mca_inherited_normalization_frontier"]
SCOPE = dict(
    lane="K3 / DIRECT", object="MCA", agreement=1116048,
    field="2130706433^6", target_epsilon="2^-128",
    original_error_rank=12, shared_carrier_dimension=11, J=[9965,21499],
    actual_P2_rank=19, anchors=8, penultimate_pair_shared=[5,4],
    B_star="274980728111395087", near=134944, raw_cutoffs=[1,2],
    local_allowance_antecedent="Residual original source AFTER the proved whole-source pencil alternatives are removed",
    whole_source_alternatives="Use their whole-source bounds and combine by MAXIMUM, never addition",
    normalization_ceiling="H=floor((J1-1)/10), ranging1096..2149 over13 profiles",
    full_divisor_budget="sum binom(m_P+mu_P-1,2)<=binom(d-r+1,2)",
    geometric_guard="rational nondegenerate C in P^r, r>=3; characteristic0 or p>degree",
    graded_anchor="Omega<=c*((N-D)*b0+D*T)/(A-D), N>=A>D, T=max(eta-1)*(C_eta-b0)_+",
    penultimate_allowance="1048577*L_t/(67473-t)",
    pencil_free_small_normalization_paid=True,
    nonconstant_plane_small_normalization_paid=True,
    quadric_exception="Only cone vertex can jump; its regular rank-two child retains the nonconstant plane and is paid",
    maximal_nonconstant_pencil="dimension s-1 in shared s survives EVERY remaining regular anchor",
    maximal_pencil_normalization_cap_required=False,
    original_source_class="Generic-regular P2 rank19 enclosure containing a nonconstant10-dimensional pencil",
    source_class_bound="272127061148955779", source_class_reserve="2853666962439308",
    profiles=13, graded_prices=26, child_certificates=1208,
    child_methods=dict(interpolation=1052, branch_energy=124, plane_occupancy=32),
    minimum_graded_numerator_gap="150824210815976004/43409",
    prefix_factor_checks=208,
    remaining_small_normalization="constant-direction pencil planes exist, but NO nonconstant pencil plane",
    remaining_large_normalization="nu>H; image degree3..9; actual jump among first7 anchors; NO nonconstant3 pencil",
    original_weights_unchanged=True, higher_raw_and_near_included_once=True,
    actual_plane_occupation_assumed=False,
    scope_amendment_files=["statement.md","claim_contract.md","node.json"],
    all_rank19_sources_covered=False, rank19_closed=False, active_v4_atom=False,
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
    need(len(published) == 1410, "inherited source inventory")
    return prior, published, graph, dict(pins, **{PRIOR: branch.MANIFEST_HASH})


def validate(manifest, prior, published, credited, pins):
    need(manifest["schema"] == "kb-penultimate-graded-pencil-payment-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == pins, "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 394
         and manifest["published_source_hashes_checked"] == 1410, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 98, "new file inventory")
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
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 861537,
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
    need(len(documents) == 394, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 129 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
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
    amendment_node = ROOTS[-1]
    old_files = {path: data for (packet, path), data in published.items() if packet == PRIOR}
    changes = []
    for relative, old in old_files.items():
        parts = PurePosixPath(relative).parts
        if parts[3] != amendment_node:
            continue
        need(relative in sources, "amended supplier incomplete")
        if sources[relative] != old:
            changes.append(dict(node=amendment_node, filename="/".join(parts[4:]),
                                previous_packet=PRIOR, previous_path=relative,
                                previous_sha256=digest(old), sha256=digest(sources[relative])))
    need({row["filename"] for row in changes} ==
         {"statement.md","claim_contract.md","node.json"}, "amendment scope")
    need(sorted(manifest["scope_amendments"], key=lambda r:r["filename"]) ==
         sorted(changes, key=lambda r:r["filename"]), "amendment ledger")
    need(graph[amendment_node] == credited[amendment_node], "amended dependency drift")
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
                       "supplier_manifests": {}, "inherited_sources": [], "source_bytes": 0, "scope_amendments": []}.items():
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
    print("PASS 1508 listed source hashes; 394 inherited proof documents; 129-node acyclic closure;",
          mutations(manifest, prior, published, graph, pins), "malformed manifests rejected", flush=True)
    print("PASS exactly three declared source-scope amendments; older frozen files unchanged", flush=True)

    # Resolve only the focused runtime from the already validated frozen suppliers.
    selected = [
        "rate_half_mca_regular_rational_plane_terminal_bounds",
        "pair_space_regular_projection_anchor",
        "polynomial_carrier_inner_projection_degree_ledger",
        "rational_curve_inner_projection_branch_budget",
    ]
    extra = [
        ("rate_half_mca_regular_terminal_low_image_degree_frontier", "certificate.json"),
        ("list_padded_johnson_dimension_descent", "compiler.py"),
        ("rate_half_mca_coupled_pair_rank_frontier", "verify_audit.py"),
        ("rate_half_mca_coupled_pair_rank_frontier", "source_certificate.json"),
        ("rate_half_mca_coupled_pair_rank_frontier", "gate_certificate.json"),
        ("rate_half_mca_coupled_pair_rank_frontier", "compression_certificate.json"),
    ]
    borrowed = {}
    for (_, relative), data in published.items():
        parts = PurePosixPath(relative).parts
        if len(parts) < 5 or parts[:3] != ("source", "background", "nodes"):
            continue
        if parts[3] in selected or (parts[3], "/".join(parts[4:])) in extra:
            need(relative not in borrowed or borrowed[relative] == data, "runtime conflict")
            borrowed[relative] = data
    need(not set(borrowed).intersection(sources), "runtime collision")
    checks = [(name, "verify.py") for name in ROOTS[:5]]
    checks.insert(3, (ROOTS[2], "verify_audit.py"))
    checks += [
        (ROOTS[-1], "verify.py"),
        (ROOTS[-1], "verify_audit.py"),
        ("rate_half_mca_regular_rational_plane_terminal_bounds", "verify_audit.py"),
        ("polynomial_carrier_inner_projection_degree_ledger", "verify.py"),
        ("rational_curve_inner_projection_branch_budget", "verify.py"),
    ]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-penultimate-graded-pencil-") as temp:
        runtime = Path(temp)
        for relative, data in {**borrowed, **sources}.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for name, filename in checks:
            path = runtime/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS six new and five inherited focused checks from frozen sources")
    print("Other inherited arithmetic not freshly replayed; external mathematical review due")
    print("Constant-plane-only and earlier high-normalization residuals remain; both Prizes open")


if __name__ == "__main__":
    main()
