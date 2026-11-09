#!/usr/bin/env bash
# Rebuild the ab initio environment in a fresh container (see code/ENV.md). Idempotent.
set -euo pipefail
cd /root
[ -x bin/micromamba ] || curl -sSL https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xj bin/micromamba
export MAMBA_ROOT_PREFIX=/root/mamba
[ -x /root/mamba/envs/qe/bin/pw.x ] || ./bin/micromamba create -y -q -n qe -c conda-forge qe=7.6 openmpi
if [ ! -d /root/pseudo/sg15 ]; then
  curl -sSL -o sg15.tgz http://www.quantum-simulation.org/potentials/sg15_oncv/sg15_oncv_upf_2020-02-06.tar.gz
  echo "3f3bd74aa5d6e0b038218a6051bb99ed9469dc03d0f05b3ec8a523f0f7a7dff0  sg15.tgz" | sha256sum -c -
  mkdir -p /root/pseudo/sg15 && tar -xzf sg15.tgz -C /root/pseudo/sg15
fi
# The Ubuntu apt package quantum-espresso 6.7 aborts at start-up ("buffer overflow detected"): never use /usr/bin/pw.x.
dpkg -s quantum-espresso >/dev/null 2>&1 && apt-get remove -y -qq quantum-espresso || true
echo "env ready: /root/mamba/envs/qe/bin (QE 7.6), /root/pseudo/sg15"
