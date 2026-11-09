# R18 / DC-2-gw benchmark (partial): Yambo cost levers. Timing data, not physics

Pre-registration: code/DC-2-gw/PREREG.md. Ge PBE+SOC, 80 Ry, k 4³, double precision, 3 MPI ranks, on a loaded box (10-rank LDA running), so times are upper bounds. Yambo reads this start as metallic (bands 27–30 partly filled): QP energies below are not results. 3 of 7 planned variants; stopped by user request to free the machine.

| variant | wall | HF | χ | Σc | mean QP shift vs 200 bands | spread, bands 28–31 |
|---|---|---|---|---|---|---|
| 200 bands, 6 Ry | 79 min | 25 min | 29 min | 25 min | – | – |
| 100 bands, 6 Ry | 49 min | 10 min | 25 min | 12 min | 0.229 eV | 0.084 eV |
| 100 bands, 6 Ry, BG terminator | ≈ 56 min (stage sum) | 11 min | 31 min | 15 min | 0.077 eV | 0.056 eV |

- BG terminator cuts the level error threefold at about 15% more time than plain 100 bands. Gap-relevant spread improves less. 200 bands is itself unconverged, so these are not absolute errors.
- HF(REDUX) reads 18 min in the 200-band run, but in the 100-band run it reads 11m17 against a 10m25 HF stage, so this timer is not a clean subset of its stage. The "third of the run is waiting" I reported is therefore unreliable, and contention was not separated from imbalance. Rerun on a quiet machine before concluding.
- EXXRLvcs (29603, full) untested. Single vs double precision untested. MPI layout untested.
- p2y reads conda QE HDF5 wavefunctions correctly.
