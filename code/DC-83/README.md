# DC-83 rerun record
CMPMC main 6c79904 (descendant of 3d43a02), g++ 16.2.1, Release, `cmake -DBUILD_TESTING=ON`; ctest 19/19 passed, test_g4cmp_import skipped (external data).
out/ holds the stdout of tests/test_kaplan, test_pair_breaking, test_luke_ntl and examples/phonon_benchmark 5000. Reference: code/CMPMC-AUD/out/sota/.
The repo's tests replaced code/CMPMC-AUD/tests/ after the public-release restructure, so the comparison is against those binaries, not a recompile of the audit tests.
