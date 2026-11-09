#!/usr/bin/env bash
# Compile and run the CMPMC audit tests against a given include tree.
# Usage: run_tests.sh <tag> <cmpmc-root> [test-name ...]
#   tag=ref  -> /home/user/ytcs/CMPMC (921db93, untouched), report-only (never fails)
#   tag=sota -> /home/user/cmpmc (branch paer-sota, patched)
# Builds in /root/cmpmc-aud-build/<tag>; outputs to code/CMPMC-AUD/out/<tag>/<test>.txt
set -uo pipefail
TAG=$1; ROOT=$2; shift 2
TESTS_DIR=/home/user/dmdd-solid/code/CMPMC-AUD/tests
OUT=/home/user/dmdd-solid/code/CMPMC-AUD/out/$TAG
B=/root/cmpmc-aud-build/$TAG; mkdir -p $B $OUT
EXTRA=""; [ "$TAG" = ref ] && EXTRA="-DCMPMC_AUDIT_REPORT_ONLY -DCMPMC_AUDIT_REF"
LIST=${*:-$(cd $TESTS_DIR && ls test_*.cpp | sed 's/.cpp//')}
for t in $LIST; do
  g++ -std=c++20 -O2 -march=native $EXTRA -I$TESTS_DIR -I$ROOT/include $TESTS_DIR/$t.cpp -o $B/$t -pthread 2> $B/$t.build.log \
    || { echo "BUILD FAIL $t"; tail -5 $B/$t.build.log; continue; }
  ( cd $B && timeout 1800 ./$t ) > $OUT/$t.txt 2>&1; echo "$t rc=$? $(tail -1 $OUT/$t.txt)"
done
