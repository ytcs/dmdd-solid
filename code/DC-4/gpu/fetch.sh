#!/usr/bin/env bash
set -e
mkdir -p /root/pseudo /root/dl; cd /root/dl
curl -sSL -o sg15.tgz http://www.quantum-simulation.org/potentials/sg15_oncv/sg15_oncv_upf_2020-02-06.tar.gz
echo "3f3bd74aa5d6e0b038218a6051bb99ed9469dc03d0f05b3ec8a523f0f7a7dff0  sg15.tgz" | sha256sum -c -
tar -xzf sg15.tgz; cp $(find . -name 'Ge_ONCV_PBE-1.2.upf' | head -1) /root/pseudo/
curl -sSLf -o lda.tgz https://www.pseudo-dojo.org/pseudos/nc-sr-04_pw_standard_upf.tgz
mkdir -p lda; tar -xzf lda.tgz -C lda; cp $(find lda -name 'Ge.upf' | head -1) /root/pseudo/Ge_LDA_dojo.upf
ls -la /root/pseudo
