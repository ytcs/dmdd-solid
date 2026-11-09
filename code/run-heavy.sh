#!/usr/bin/env bash
# Serialise heavy computations on the 4-core box: every QE/EPW (or other >1-core) job goes through this lock.
# Usage: code/run-heavy.sh <label> <command...>   e.g. run-heavy.sh SI-PH mpirun -np 4 ph.x -in si.ph.in
set -euo pipefail
LABEL="$1"; shift
LOCK=/root/heavy.lock; LOG=/root/heavy.log
export PATH=/root/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1 OMPI_ALLOW_RUN_AS_ROOT=1 OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
exec 9>"$LOCK"
echo "$(date -Is) WAIT  $LABEL" >> "$LOG"
flock 9
echo "$(date -Is) START $LABEL" >> "$LOG"
t0=$(date +%s); set +e; "$@"; rc=$?; set -e
echo "$(date -Is) END   $LABEL rc=$rc wall=$(( $(date +%s)-t0 ))s" >> "$LOG"
exit $rc
