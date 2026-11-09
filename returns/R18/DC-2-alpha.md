# R18 / DC-2-alpha: Ge bands by DFT+α. Fit passes, dispersion fails: the route is closed

Pre-registration and amendments: code/DC-2-alpha/PREREG.md. Records: code/DC-2-alpha/. Stock QE 7.6, PBE + SOC, PseudoDojo FR standard Ge, 80 Ry, k 8³, a_exp, `HUBBARD ortho-atomic` with `U Ge-4s 1.0d-8` and `ALPHA Ge-4s 1.0` by restart.

## Result
**DFT+α with stock QE reaches the measured Ge valley energies and order but not the band curvature, so by the pre-registered rule these bands are not used for the Ge window.** The Ge window stays [E]. DC-2 stays closed as FAILED-CONTROL (returns/R18/DC-2.md).

| test | calculated | target | verdict |
|---|---|---|---|
| fit: E_g(L) | 0.749 eV | 0.744 ± 0.05 | PASS (fitted) |
| fit: E_g(Γ) | 0.918 eV | 0.89 ± 0.05 | PASS (fitted) |
| T1: Δ_SO | 0.295 eV | 0.29 ± 0.03 | PASS, weak: does not depend on α |
| T2 as written: X point | 1.014 eV | 0.87 ± 0.08 | FAILED (target misidentified the Δ minimum; recorded as failed) |
| T2′: Δ minimum | 0.826 eV at 0.80 X (direct DFT) | 0.87 ± 0.08 | PASS, but ≈ 0.1 eV below 0.92 eV implied by L + 0.18 (arXiv:1010.0961) |
| **T3: m_t** | **0.101** direct; 0.099 Wannier | 0.082 ± 0.010 | **FAILED, +23%** |
| **T3: m_Γ** | **0.053** direct; 0.049 Wannier | 0.038 ± 0.005 | **FAILED, +39%** |
| T3: m_l | ≈ 1.8 ± 0.2 direct; 2.72 Wannier | 1.59 ± 0.15 | marginal on direct, FAILED on Wannier |

Direct masses: finite differences of DFT eigenvalues at h = 0.02, 0.04 × 2π/a, Richardson to h → 0, code/DC-2-alpha/direct_mass.py. Eigenvalues print to 0.1 meV, which limits m_l. Mass targets are from the stand-in's pre-registration; they are the standard measured values, not re-read from a primary source here.

## Wannier quality, separately
The Wannier fit also misses its own floor: spread 37.99 Å² against 28.99 Å² for the PBE+SOC reference. Grid-point edges agree to < 1 meV, but off-grid the Δ minimum is 0.795 eV at 0.84 X against direct 0.826 eV at 0.80 X: 31 meV, six times the ±5 meV floor. 8³ is not enough for these bands; the Si work needed 14³.

## Reading
The shift moves 4s-like states without restoring the k·p coupling, which is a plausible cause of too-heavy masses at corrected gaps; this was not tested. Not tried, by pre-registration: a second parameter, valley-selective scissors, rescaled masses. Whether the mass error matters at the size of the window was not computed, because the rule stops the route first.

## What remains
The paper's α = 1.4 does not transfer (its projector differs: at α = 1.4 here Γ 1.30, L 1.02). α = 1.0 here is not a value to reuse. Parameter-free Ge bands still need GW (INF-1). A Ge window from measured valley energies and masses (k·p) would be a different, explicitly empirical route, not done.

Useful by-product: Hubbard ALPHA on a 4s projector with SOC works in stock QE by the two-step restart above.

Run by Claude (LLM); not refereed. A negative result on a pre-registered rule, so no referee was run.
