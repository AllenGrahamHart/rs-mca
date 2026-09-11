"""Offline bounded replay of grouped receiver-conditioned original-source bounds."""

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
MANIFEST_HASH = "e6b1399a5fb0646bf417abafa065fea72454345b5009778e05a98f15c6d830ce"
PARENT = "3e97eb8bc65acfc3f6ce3d88aed56b3a6de96238"
PRIOR = "kb-raw-one-rank-nineteen-source-tail-20260911"
HELPER_HASH = "e7291f047e48b42ae6fad27652201f16a7928af1fcc95823413944c1e93491d9"
ROOTS = ['rate_half_mca_dense_conic_receiver_payment',
 'mca_canonical_small_colour_defect_bank',
 'rate_half_mca_small_colour_source_payment',
 'rate_half_mca_bounded_colour_source_payment',
 'mca_receiver_colour_profile_core_basis',
 'rate_half_mca_sparse_heavy_colour_source_payment']
SCOPE = {'schema': 'receiver-conditioned-source-bounds-v1',
 'lane': 'K3 / DIRECT',
 'object': 'MCA',
 'field': '2130706433^6',
 'n': 2097152,
 'k': 1048576,
 'agreement': 1116048,
 'target_epsilon': '2^-128',
 'B_star': '274980728111395087',
 'original_error_rank_before_reselection': 12,
 'J': [9965, 21499],
 'covered_J_integers': 11535,
 'shared_dimension': 11,
 'unit': 'Entire original distinct bad-slope set',
 'quantifier': 'Every original post-near source at its printed receiver condition; colour proofs '
               'reselect inside the fixed frame',
 'P1_P2_rank_restriction': False,
 'dense_conic': {'nonsingular': True,
                 'coefficient_field': 'F(X)',
                 'weighted_degree_max': '2J',
                 'receiver_exceptions_max': 276035,
                 'bound': '274980278712737789',
                 'reserve': '449398657298',
                 'primitive_degree_one_lift_proved': True},
 'small_bank': {'class_size_max': 43,
                'coordinate_mass_max': 53067,
                'bound': '274978354983575055',
                'reserve': '2373127820032'},
 'bounded_colours': [{'class_size_max': 2,
                      'singleton_coordinates_max': 1717,
                      'bound': '274979228268047446',
                      'reserve': '1499843347641'},
                     {'class_size_max': 43,
                      'singleton_coordinates_max': 1465,
                      'bound': '274977964220092532',
                      'reserve': '2763891302555'},
                     {'class_size_max': 286,
                      'singleton_coordinates_max': 0,
                      'bound': '274980091354143171',
                      'reserve': '636757251916'}],
 'sparse_heavy_colours': [{'heavy_class_size_gt': 43,
                           'heavy_coordinates_max': 3000,
                           'singleton_coordinates_max': 824,
                           'bound': '274980301923454583',
                           'reserve': '426187940504'},
                          {'heavy_class_size_gt': 43,
                           'heavy_coordinates_max': 4639,
                           'singleton_coordinates_max': 0,
                           'bound': '274979909180000584',
                           'reserve': '818931394503'}],
 'colour_partition': 'Nonzero projective V-evaluation fibre plus normalized receiver pair',
 'colour_units': 'Coordinates, not classes',
 'canonical_reselection': 'Receiver, carrier, degree and finite labels fixed',
 'original_rank_retested_after_reselection': False,
 'original_near_once': 134944,
 'colour_zero_labels_global_max': 21488,
 'resource_copies_per_application': 1,
 'profiles_use_actual_class_sizes': True,
 'trimmed_core_allocation_is_lower_relaxation': True,
 'profile_inequality_universally_below_budget': False,
 'universal_receiver_cover': False,
 'alternative_source_bounds_combine': 'MAXIMUM, not addition',
 'new_lemmas': ['mca_canonical_small_colour_defect_bank', 'mca_receiver_colour_profile_core_basis'],
 'all_original_rank12_sources_closed': False,
 'higher_original_error_ranks_closed': False,
 'ordinary_LIST_closed': False,
 'active_v4_atom': False,
 'adjacent_safe_row_closed': False,
 'unsafe_adjacent_recipe_claim': False,
 'prize_closed': False}


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
    need(len(published) == 1741, "inherited source inventory")
    return prior, published, graph, dict(pins, **{PRIOR: branch.MANIFEST_HASH})


def validate(manifest, prior, published, credited, pins):
    need(manifest["schema"] == "kb-receiver-conditioned-source-bounds-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == pins, "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 49
         and manifest["published_source_hashes_checked"] == 1741, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 63, "new file inventory")
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
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 177434,
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
    need(len(documents) == 49, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 22 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
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
            bad["requirements"][ROOTS[0]].append(ROOTS[0])
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
    print("PASS 1804 listed source hashes; 49 inherited proof documents; 22-node acyclic closure;",
          mutations(manifest, prior, published, graph, pins), "malformed manifests rejected", flush=True)

    # Earlier amendments were checked by their own frozen custody validators.
    runtime_sources = {}
    for (_, relative), data in published.items():
        parts = PurePosixPath(relative).parts
        if (len(parts) >= 5 and parts[0] == "source" and parts[2] == "nodes"
                and parts[3] in manifest["requirements"]):
            runtime_sources[relative] = data
    need(not set(runtime_sources).intersection(sources), "new node runtime collision")
    runtime_sources.update(sources)
    checks = [('background', 'rate_half_mca_dense_conic_receiver_payment', 'verify.py'),
 ('background', 'rate_half_mca_dense_conic_receiver_payment', 'verify_audit.py'),
 ('background', 'mca_canonical_small_colour_defect_bank', 'verify.py'),
 ('background', 'rate_half_mca_small_colour_source_payment', 'verify.py'),
 ('background', 'rate_half_mca_small_colour_source_payment', 'verify_audit.py'),
 ('background', 'rate_half_mca_bounded_colour_source_payment', 'verify.py'),
 ('background', 'rate_half_mca_bounded_colour_source_payment', 'verify_audit.py'),
 ('background', 'mca_receiver_colour_profile_core_basis', 'verify.py'),
 ('background', 'rate_half_mca_sparse_heavy_colour_source_payment', 'verify.py'),
 ('background', 'rate_half_mca_sparse_heavy_colour_source_payment', 'verify_audit.py'),
 ('background', 'rate_half_mca_min_envelope_raw_mass', 'verify_audit.py'),
 ('background', 'list_padded_johnson_dimension_descent', 'verify_joint_small.py'),
 ('critical', 'mca_low_core_quadratic_graph_payment', 'verify_moving_parabola.py')]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-receiver-source-") as temp:
        runtime = Path(temp)
        for relative, data in runtime_sources.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for section, name, filename in checks:
            path = runtime/"source"/section/"nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS ten new and three inherited focused checks from frozen sources")
    print("Other inherited arithmetic not freshly replayed; external mathematical review due")
    print("Four receiver-conditioned source bounds and two colour lemmas; no universal cover or Prize closure")


if __name__ == "__main__":
    main()
