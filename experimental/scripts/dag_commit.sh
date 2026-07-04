#!/bin/bash
# Atomic DAG commit: validate (gate) -> rebuild derived artifacts -> commit.
# Usage: dag_commit.sh "commit message"
set -e
cd "$(dirname "$0")/../.."
ERRS=$(python3 experimental/scripts/verify_prize_dag.py 2>&1 | grep -c "declared\|ERROR" || true)
[ "$ERRS" != "0" ] && { echo "BLOCKED: validator errors"; exit 1; }
python3 experimental/scripts/build_critical_orbit.py
git add experimental/data/prize-dag/ experimental/notes/ experimental/scripts/ experimental/data/certificates/
git commit -q -m "$1

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
echo "committed with derived artifacts current"
