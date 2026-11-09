# R18 / DC-2: Ge HSE06+SOC band edges. The pre-registered control FAILS

Spec: state/DEFERRED-COMPUTE.md DC-2; returns/R15/COMP-PH.md §6.2. Records: code/DC-2/.

## Result
**HSE06+SOC puts the Ge Γ valley below L, so the specified route cannot give the Ge PAER window.** The Wannier stage was not run. The Ge window stays [E] (≈ 0.213–0.32 MeV).

Control, scored as pre-registered (L below Γ; E_g(L) within 0.1 eV of 0.744 eV; E_dir 0.89 eV):
| criterion | production (k 8³, nqx 4) | densest (k 6³, nqx 6) | 1/n² extrapolation (nqx 4, 6; k differs slightly) [E] | verdict |
|---|---|---|---|---|
| L below Γ | Γ 0.691, L 0.831 | Γ 0.641, L 0.788 | Γ ≈ 0.60, L ≈ 0.76 | **FAILED-CONTROL** |
| E_g(L) vs 0.744 | +0.087 | +0.044 | ≈ +0.02 | PASS (production marginal) |
| E_dir vs 0.89 | −0.20 | −0.25 | ≈ −0.29 | **FAILED-CONTROL** |

## The failure is not numerical [CALC]
Γ − L stays between −0.09 and −0.15 eV across every variation, at a_exp = 5.658 Å unless stated (edges in eV above the VBM, code/DC-2/out/sweep/):
| variation | Γ | L | X |
|---|---|---|---|
| nqx 2, 4 (k 4³) | 1.129, 0.691 | 1.220, 0.822 | 1.847, 1.451 |
| nqx 3, 6 (k 6³) | 0.772, 0.641 | 0.918, 0.788 | 1.505, 1.438 |
| ecutfock 160 → 320 Ry (nqx 4) | 0.691 → 0.691 | 0.822 → 0.822 | 1.451 → 1.451 |
| PseudoDojo FR (independent; nqx 4) | 0.605 | 0.741 | 1.364 |
| PseudoDojo FR at a = 5.652 Å | 0.637 | 0.752 | 1.361 |
| SG15 v1.2 scalar-relativistic, no SOC (nqx 4; relative to VBM) | 0.796 | 0.931 | 1.562 |
| x_gamma_extrapolation off (nqx 4) | 0.756 | 0.884 | 1.511 |
| exxdiv none, extrapolation on (nqx 4) | 0.672 | 0.803 | 1.433 |

PBE+SOC here: L 0.093, X 0.649, Γ conduction state inside the valence band (edge printed as 0.0). The spec's `nqx` 4³ is under-converged by about 0.05–0.09 eV, a smaller effect than the failure.

Literature agrees: HSE at 0.25 mixing gives Γ-Γ 0.775, Γ-L 0.823 eV, with the order correcting only above 0.28 mixing at 17–34% gap error (Abdurrazaq et al., arXiv:2512.08857v1, QE, no SOC; preprint read in summary form, [UNVERIFIED] detail). The spec's assumption that "only hybrid+SOC bands give the edge" is therefore wrong for this functional.

## Deviations from spec, and what they mean
- SCF with symmetry (29 k) instead of the 512-k nosym run. Same edges: k 4³ and k 8³ at nqx 4 give Γ 0.691 in both, L 0.822 and 0.831.
- open_grid.x was validated for spinors but not used in production: Wannier bands via open_grid vs direct full-grid agree to 0.035 meV (stock CPU QE) and 0.024 meV (nvfortran build), Ge PBE+SOC, 40 Ry, 4³. That control is not an HSE test. Needs ≈ 87 GB at this grid.
- A QE performance bug was fixed (code/DC-2/exx_bp-noncolin-copy.patch): `exxbuff = exxbuff_d` inside the noncollinear (k, band) loops of PW/src/exx_bp.f90 copied the whole buffer per band. Moved after the loops, guarded by noncolin. Projected ≈ 7 h per exxinit → the production SCF took 33 min on one A40. Validation: small HSE+SOC case (30 Ry, k 4³, nqx 2), patched GPU vs stock CPU QE, total energy −281.23598598 Ry both, band edges equal to print precision. Agreement was not rechecked at production settings.

## Status
DC-2 stays open. Inputs for Ge IFCs (DC-4) are not used. Replacement route is a method change, to be pre-registered separately (DFT+α, see DC-RESULTS). Cost: 1 A40 × ≈ 3.6 h, ≈ $2.10.

Run by Claude (LLM); not refereed.
