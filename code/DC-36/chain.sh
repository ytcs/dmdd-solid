#!/bin/bash
# wait for production jobs; never more than 2 python workers
PY=/home/ytc/paer-work/mamba/envs/qe/bin/python
export OMP_NUM_THREADS=1
cd /home/ytc/Projects/bm-paer/campaign/paer/code
while pgrep -f 'python run_for[c]e' >/dev/null; do sleep 15; done
(cd DC-36; $PY run_var.py > run_var.log 2>&1)
while pgrep -f 'python recas[t]' >/dev/null || pgrep -f 'python run_reac[h]' >/dev/null; do sleep 15; done
(cd DC-49; $PY typo_check.py > typo_check.log 2>&1; $PY ideal_check.py > ideal_check.log 2>&1)
(cd DC-54; $PY fig3_check.py > fig3_check.log 2>&1)
echo chain-done
