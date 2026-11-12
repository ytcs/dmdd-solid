# Ab initio environment for the figure scripts

Only the scripts that rerun Quantum ESPRESSO need this (book/figscripts/ch03/qe_ch03.py, w90_verify.py, fig3_11_w90.py and
book/figscripts/ch05/*_qe.sh, fig5_4_epsk.sh). All other figure scripts read cached data next to them.

- Install: `bash book/tools/qe/setup-env.sh` (micromamba, conda-forge `qe=7.6` with OpenMPI, OpenBLAS, FFTW, ScaLAPACK; SG15 ONCV
  pseudopotentials, scalar-relativistic, version 1.2 where available).
- Run each heavy job through `book/tools/qe/run-heavy.sh <LABEL> <command…>`; it serializes jobs with a lock file and sets PATH
  to the environment. Use `mpirun -np <cores>` with OMP_NUM_THREADS=1.
- Work directories (outdir, *.save) go outside the repository; commit only inputs, scripts and small outputs.
