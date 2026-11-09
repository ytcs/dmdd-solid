# R15 / COMP-PH: ground-state, phonon and dielectric inputs for Si and Ge, and the ab initio PAER window

ID: COMP-PH. Brief: briefs/R15/COMP-PH.md. **Coordinator rescope (2026-11-01, mid-task):** finish Si and Ge only; the small-cell survivor Γ-DFPT
batch (diamond, 3C-SiC, GaAs, LiF, NaF, 4H-SiC, Al₂O₃) is **FORMULATED**, not run (§6). Code, inputs, small outputs and the convergence record are in
code/COMP-PH/. Work directories are in /root/work/COMP-PH/. Every heavy job ran through code/run-heavy.sh; the gate record is code/COMP-PH/gate.md (§7).
Stack: conda-forge QE 7.6 (pw.x, ph.x, q2r.x, matdyn.x, pw2wannier90.x, wannier90.x already in the env: no env additions). Pseudopotentials: SG15 ONCV PBE
scalar-relativistic **Si_ONCV_PBE-1.2.upf** (4 e), **Ge_ONCV_PBE-1.2.upf** (14 e, 3d in valence). Every number below is [CALC] unless tagged otherwise.

## 0. Results at a glance
| item | Si | Ge | control |
|---|---|---|---|
| lattice used | a_PBE = 5.4773 Å (relaxed; exp 5.431, +0.85%) | a_exp = 5.658 Å (PBE-relaxed Ge is metallic, §3.1) | stated |
| PBE gap, CBM | indirect 0.602 eV, CBM at k_c = 0.840 X on Δ; direct Γ 2.549 eV | **wrong ordering**: Γ₂′ 0.047 eV below L₁ 0.191 eV (no SOC) | Si PASS; Ge **FAILED-CONTROL** |
| scissor Δ_sc | +0.568 eV to E_g(0 K) = 1.170 eV | undefined (Γ below L); E_g = 0.744 eV used as data | — |
| ε_∞ (DFPT, LFE) | 13.04 (a_exp, k 18³); 13.20 (a_PBE, k 14³) | ≈ 2×10⁴ (near-metallic PBE) | Si **FAILED-CONTROL** (+11% vs 11.7; tolerance 10%); Ge **FAILED-CONTROL** |
| phonons vs INS (Γ, X, L; 8 values) | 7/8 within 5%, systematic −2.5…−4.1%; L_LO −5.4% | 6/8 within 2.3%; **TA −13.5% (X), −11.6% (L)** | Si PASS except L_LO (FAILED-CONTROL, marginal) |
| ω_TA(Q*) on the window optimum | **14.72 meV** at \|Q*\| = 0.510 Å⁻¹ ([100], q* = 0.90 keV) | **6.82 meV** at \|Q*\| = 0.678 Å⁻¹ from L (q* = 0.56 keV), minimum off axis (ϑ ≈ 0.10) | C5 kinematics: §4 |
| PAER edge (WP6-v3 (3.1′)) | continuum **0.3374 MeV**; exciton replica **0.3332 MeV** | continuum **0.2138 MeV**; replica 0.2127 MeV (TA soft: INS-scaled 0.2141) | brackets of WP6-v3 (0.333–0.339) reproduced |
| ZPL kinematic edge m_ZPL | **0.4154 MeV** (q = 1.39 keV, E_min = 1.355 eV) | FORMULATED (HSE+SOC, §6.2) | anchor m(\|K_pk\|) = 0.473 vs 0.474 [D] PASS |
| window FOM Δm/m (WP8-F §2.7(b)) | 0.448 (E_min^{ZPL}(q*) = 1.715 eV, min over 5 q̂; [100] alone 1.851 → 0.563) | FORMULATED | — |
| TA minimum on/off axis (O-WP3-9) | on axis to \|q\| ≈ 1.35 keV (not 0.8–1.0 keV [E]); γ_ω computed | off axis at every \|q\| sampled (ϑ = 0.05–0.15), as WP3-v3 §M3(e) | — |

## 1. Convergence (tolerances fixed before reading the scans)
Tolerances: total energy ≤ 1 meV/atom, pressure ≤ 0.5 kbar, ω_Γ ≤ 0.1 meV (≈ 1 cm⁻¹), ε_∞ ≤ 1%, interpolated ω_TA(Q*) ≤ 0.3 meV between successive q grids.
| quantity | scan | result | chosen |
|---|---|---|---|
| Si ecut (8³ k, a_exp) | 30–120 Ry | 50: 0.71 meV/at, 60: 0.14, 70: 0.02; P within 0.1 kbar from 50 Ry | **60 Ry** |
| Si ω_Γ vs ecut | 60 / 80 Ry | 501.19 / 501.16 cm⁻¹ (0.005 meV) | 60 Ry |
| Si k (60 Ry) | 4–14 | 8→10: 1.6 meV/at; 10→12: 0.3; 12→14: 0.06 | SCF/relax 12³; DFPT 8³ (ω_Γ k8 vs k10: 0.3 cm⁻¹) |
| Si ε_∞ vs k (Γ-centred) | 8, 10, 12, 14 (a_PBE); 14, 18 (a_exp) | 14.36, 13.57, 13.29, 13.20; 13.09, 13.04 | k 18³ (residual ≲ 0.3%) |
| Si q grid | 4³, 6³, 8³ (8, 16, 29 q) | ω_TA(0.510 Å⁻¹) 14.45 / 14.81 / 14.72 meV; Γ, X, L on-grid, identical | **8³** (Δ 6³→8³ = 0.09 meV) |
| Si sound speeds vs q grid | 4³, 6³, 8³ | c_TA[100] 4.93, 5.49, 5.63 km/s; c_LA[100] 8.28, 8.18, 8.18 | c_LA converged; **c_TA not converged** (2.5% step 6³→8³) |
| Si lattice | a_PBE vs a_exp (4³ q) | a_exp: optical within 1.6% of INS but TA −8% (X, L); a_PBE: all branches −2.5…−5.4% | **a_PBE** for phonons (TA is the window branch); ε_∞ quoted at both |
| Si Wannier (8 sp³, 16 bands, froz VBM+4 eV) | 10³ vs 14³ k, ws_distance | E_g 0.609 → 0.6038 (DFT 0.602); k_c 0.79 → 0.855 (DFT 0.842) | 14³; E_min error ±5 meV (from the CBM offset) |
| Ge ecut (8³ k) | 30–120 Ry | 60: 3.1 meV/at, 70: 0.49, 80: 0.22 | **80 Ry**; ω_Γ 60 vs 80: 296.96 / 298.05 cm⁻¹ (0.37%) |
| Ge k (DFPT) | 8 vs 10 at Γ | ω_Γ k8 / k10: 298.05 / 297.36 cm⁻¹ (0.09 meV); ε_∞ 2.2×10⁴ / 1.2×10⁴ (not convergent) | 8³ |
| Ge q grid | 4³ run (7589 s, 8 q: 16 min/q average); 6³ FORMULATED (16 q ≈ 4 h > gate) | — | 4³ (q-grid error assigned from Si: ±0.4 meV on ω_TA) |
Records: code/COMP-PH/conv/ (conv_ecut_*.json, chain_Si.log, chain_Ge.log), out/Si_phG_*.out, out/Si_ph_q{4,6,8,4aexp}/.

## 2. Si
**2.1 Ground state and bands.** vc-relax (60 Ry, 12³): a_PBE = 10.3507 bohr = 5.4773 Å. Bands (L–Γ–X–W–K–Γ, 171 k; Δ line 0.76–0.90 X step 0.005):
E_g^{PBE} = 0.602 eV, VBM Γ₂₅′, CBM Δ₁ at **k_c = 0.840 ± 0.003 X** (DFT minimum on the 0.005 grid; parabolic vertex 0.839; 0.842 used in §4, immaterial), X₁c − VBM 0.743 eV, L₁c 1.426 eV,
direct Γ₂₅′→Γ₁₅ 2.549 eV. Scissor **Δ_sc = +0.568 eV** to E_g(0 K) = 1.170 eV (WP6-v3; CONVENTIONS default "measured E_g(T_op)"). With k_c, the
pocket vector is |K_pk| = 0.842 × 2π/a_PBE = 0.966 Å⁻¹ = 1.906 keV (G′ = 0 class). Literature k_c ≈ 0.85 X (WP3-v3 [UNVERIFIED]): agrees to 1%.
**2.2 ε_∞.** DFPT with local fields (ph.x epsil). Converged in k at a_exp: **13.04**; at a_PBE 13.20 (k 14³, still −0.1/step). Measured 11.7 (WP8-U [FT] row,
2008.08560 / 1901.07569 "ε₀"; non-polar so ε₀ = ε_∞): +11%, outside the 10% WP8-F need → **FAILED-CONTROL** (the PBE gap underestimate; a scissor
or hybrid ε_∞ is not computed). Z* before ASR −0.089 e per atom (sum-rule violation), 0 after ASR (symmetry PASS). Use the measured 11.7 for screening; the [CALC] value is a diagnostic only.
**2.3 Phonons vs INS (CONTROL).** Pre-registered criterion: |Δω/ω| ≤ 5% at Γ, X, L against Nilsson & Nelin, PRB 6, 3777 (1972) (DOI verified via lit.py,
literature/papers-COMP-PH/; the eight numbers are the standard tabulation **[UNVERIFIED: not re-read from the PDF]**, room temperature).
| point | calc (THz / meV) 8³, a_PBE | INS (THz) | dev | a_exp (4³) dev |
|---|---|---|---|---|
| Γ_O | 15.03 / 62.17 | 15.53 | −3.2% | −0.8% |
| X_TA | 4.33 / 17.92 | 4.49 | −3.5% | −8.5% |
| X_LA | 11.96 / 49.46 | 12.32 | −2.9% | −0.5% |
| X_TO | 13.33 / 55.13 | 13.90 | −4.1% | −0.4% |
| L_TA | 3.30 / 13.63 | 3.43 | −3.9% | −8.0% |
| L_LA | 11.06 / 45.76 | 11.35 | −2.5% | −1.6% |
| L_LO | 11.92 / 49.28 | 12.60 | **−5.4%** | −1.5% |
| L_TO | 14.25 / 58.92 | 14.68 | −3.0% | +0.1% |
Verdict: PASS for 7/8 at a_PBE; L_LO **FAILED-CONTROL** (marginal, 0.4% over). The a_PBE run is uniformly soft by ≈ 3.5% (lattice expansion); the a_exp run fixes the
optical branches but softens TA by 8% (Si TA has negative Grüneisen parameters), so no single lattice passes everything; the window branch (TA) is better at a_PBE.
ω_max = 62.17 meV (INS 64.2). Dispersion: out/Si_ph_q8/path.freq (Γ–X–W–K–Γ–L).
**2.4 Sound speeds (acoustic slopes, Q = 0.005–0.02 × 2π/a, linear to 0.1%).** 8³ grid, km/s, calc vs elastic-constant values from C^{el} = 165.7/63.9/79.6 GPa
(WP3-v3 §M3(e) [E]): c_LA[100] 8.18 (8.43, −3.0%), c_TA[100] 5.63 (5.85, −3.8%), c_LA[111] 9.04 (9.36, −3.4%), c_TA[111] 4.92 (5.09, −3.3%), slow
c_TA[110] 4.53 (4.67, −3.0%). c_TA moved +2.5% from 6³ to 8³: the slopes are FT-interpolation-limited; quote ±3% (convergence note in the CSV).

## 3. Ge
**3.1 Gap check (decides the route).** SCF + bands at a_exp (80 Ry, 10³, 20 bands): VBM Γ₂₅′; Γ₂′ at +0.047 eV, L₁ at +0.191 eV, X₁ at +0.755 eV. PBE
without SOC therefore has a **direct Γ gap of 0.047 eV below the L valley** (experiment: L 0.744 < Γ 0.89 eV). The PBE-relaxed lattice (larger) would close
it. Decision: Ge phonons at **a_exp** (insulating, ph.x runs); the band ordering and gap are **FAILED-CONTROL**; a scissor cannot repair the L/Γ order, so
E_min^{ZPL}(q) for Ge is **FORMULATED** with HSE06+SOC (§6.2). The L valley position is fixed by symmetry (k_c = L), so K_pk = (½,½,½)2π/a = 0.962 Å⁻¹ =
1.897 keV needs no band calculation. ε_∞(PBE) ≈ 2.2×10⁴ (k 8³): metallic-like, **FAILED-CONTROL**; use measured 16.0. Z* before ASR −0.97 e per atom (large sum-rule violation, consistent with the near-metallic ε), 0 after ASR.
**3.2 Phonons vs INS** (Nilsson & Nelin, PRB 3, 364 (1971), 80 K; DOI verified; numbers [UNVERIFIED] as in §2.3):
| point | calc (THz / meV) 4³, a_exp | INS (THz) | dev |
|---|---|---|---|
| Γ_O | 8.94 / 36.95 | 9.12 | −2.0% |
| X_TA | 2.06 / 8.52 | 2.38 | **−13.5%** |
| X_LA | 7.10 / 29.34 | 7.14 | −0.6% |
| X_TO | 8.16 / 33.76 | 8.17 | −0.1% |
| L_TA | 1.65 / 6.80 | 1.86 | **−11.6%** |
| L_LA | 6.48 / 26.78 | 6.63 | −2.3% |
| L_LO | 7.24 / 29.96 | 7.27 | −0.4% |
| L_TO | 8.57 / 35.45 | 8.55 | +0.3% |
Verdict: optical and LA PASS (≤ 2.3%); **TA FAILED-CONTROL**. X_TA is the raw ph.x eigenvalue at the on-grid X point (2.059 THz, identical to matdyn), and the Γ acoustic ASR violation is only 9.3 cm⁻¹, so neither interpolation nor asr='crystal' causes it. Sound speeds (4³; elastic values from
C^{el} = 128.5/48.3/66.8 GPa, ρ = 5.323 g/cm³, WP3-v3 [E]): c_LA[100] 5.01 (4.91), c_LA[111] 5.40 (5.55); c_TA[100] 2.88 (3.54), c_TA[111] 2.50 (3.03), slow c_TA[110] 2.28 (2.74). At 4³ these slopes are
**unusable either way** (the Si 4³ control was −16% on c_TA, −3.8% at 8³); only the on-grid TA deficit is physics. Cause **unresolved** between the
near-metallic PBE state (Γ₂′ at 0.047 eV over-screening the shear modes) and k-convergence of TA at k 8³ with a 47 meV gap (the k8→k10 test probed only
Γ_O); next test: single-q ph.x at X with k 12³ (≈ 45 min), then the §6.2 HSE+SOC route. ω_max = 36.95 meV (INS 37.7).
**3.3 ω_ν(Q*) and edges.** Grid as §4 with axis [111]. At the edge optimum q* = 0.56 keV: |Q*| = 0.678 Å⁻¹ on axis, on-axis ω_TA = 6.83 meV, ω_LA = 22.1 meV;
the q̂-minimised TA is 6.82 meV at ϑ ≈ 0.10 (off axis at every |q| on the grid, ϑ = 0.05–0.15, as the conical [111] TA axis requires). Edges (3.1′),
E_g = 0.744 eV: **continuum 0.2138 MeV**, **replica 0.2127 MeV** (E_x^b = 4.0 meV [E]); floors 0.21186 / 0.21072 MeV. Because TA is 12–14% soft (§3.2), the
INS-scaled ω_TA(Q*) ≈ 7.7 meV (WP6-v3: 7.5 [E]) and continuum 0.2141 MeV; the edge moves by ≤ 0.0003 MeV either way. γ_ω of the lowest TA about [111]:
out/Ge_ph_q4/gamma.json (tilt planes as Si, small-Q −0.88). E_min^{ZPL}(q) and m_ZPL: FORMULATED (§6.2).

## 4. The PAER window inputs (G-F5) on a stated grid
**Grid (defined here; §M3–§M4 give none, IF-1):** |q| = 0.40–2.00 keV in steps of 0.02 keV; q̂ tilted from the pocket axis K̂_pk ([100] Si, [111] Ge) by
ϑ = 0–0.7 rad (step 0.05) at seven azimuths 0–π/2 (covers the {001} and {011} tilt planes); Q* = K_pk − q (G′ = 0 class, the one that reaches the edge;
the (2̄00) class starts at |q| > 2.28 keV, outside the grid). E_th(|q|) = E_g + min_{q̂,ν} ω_ν(Q*) (continuum) and E_g − E_x^b + min ω (replica), E_x^b = 14.7 meV
(Si), 4.0 meV (Ge, inferred from WP6-v3's 0.7475 − 0.0075 eV [E]). m_min from WP6-v3 (3.1′) with v_max = 794.5 km/s. Geometry uses the a_PBE zone; at a_exp |K_pk| and |Q*| are +0.85% (0.518 vs 0.510 Å⁻¹ at q*), Δω_TA ≲ 0.15 meV. The tilt term ½(m_c + m_h)|∇ω|²
(WP3-v3 §M3(a), ≈ 0.14 meV for Si TA) is not included: it lowers the edge by ≈ 4×10⁻⁵ MeV.
**Si (8³ q, a_PBE).** On-axis branch energies (meV) at the optimum region:
| \|q\| (keV) | \|Q*\| (Å⁻¹) | ω_TA | ω_LA | min_{q̂}ω_TA | E_min^{ZPL} [100] / min of 5 q̂ (eV) |
|---|---|---|---|---|---|
| 0.80 | 0.558 | 15.42 | 28.35 | 15.42 (axis) | 1.983 / 1.837 |
| 0.86 | 0.530 | 15.03 | 27.06 | 15.03 | 1.904 / 1.764 |
| **0.90** | **0.510** | **14.72** | **26.12** | 14.72 | 1.851 / **1.715** ([210]) |
| 1.00 | 0.457 | 13.81 | 23.62 | 13.81 | 1.728 / 1.616 |
| 1.20 | 0.355 | 11.63 | 18.64 | 11.63 | 1.508 / 1.486 |
| 1.40 | 0.254 | 8.84 | 13.49 | 8.83 (ϑ = 0.05) | 1.351 / 1.351 |
Edges: **continuum 0.3374 MeV** (q* = 0.90 keV; 4³/6³/8³ and a_exp: 0.3373–0.3374), **replica 0.3332 MeV** (q* = 0.88 keV; 0.3331–0.3333), floors
2E_g/v_max² = 0.33317 and 2E_x/v_max² = 0.32899 MeV (reproduce WP6-v3). The replica edge sits **0.00006 MeV above** the 0.3332 continuum floor, deciding
WP6-v3's "at or below 0.3332, undecided": **at, not below** (ω_TA(Q*) = 14.7 > E_x^b = 14.7 meV within 0.1 meV — the difference is below the INS systematic,
so the ordering of replica edge vs continuum floor stays a ±0.0002 MeV statement). With TA scaled up by the INS offset (+3.5%): 15.2 meV, continuum 0.3378,
replica 0.3334 MeV. **ω_TA(Q*) = 14.7 ± 0.2 (numerical) +0.5/−0 (INS systematic) meV**, vs WP6-v3's 13.5 ± 1.5 [E]: inside the [E] bracket, upper half.
**Kinematic ZPL edge:** E_min^{ZPL}(|q|) = min over k and over five q̂ ([100], [110], [111], [210], [211]) of ε_c(k+q) − ε_v(k), PBE + Δ_sc, Wannier 14³;
for |q| ≲ 1.3 keV the [210] direction is lowest, above it [100]; five directions bound min_{q̂} from above (a finer q̂ search may lower E_min by tens of meV at |q| < 1.3 keV, not at the m_ZPL optimum where [100] wins). m_ZPL = min_q q²/[2(qv_max − E_min(q))] = **0.4154 MeV** at q = 1.39 keV (E_min = 1.355 eV): this is the
kinematic onset of S^{(1)} with all vertices allowed and coincides with WP6-v3's "forbidden-class" ZPL ≈ 0.42 [E]; the allowed/forbidden split is a matrix-element
statement not computed here. Anchor: at |q| = |K_pk| the code returns E_min = 1.1735 eV (E_g + 3.5 meV Wannier residual), m = 0.473 MeV vs 0.474 [D] (C18): PASS.
Ab initio **Si PAER-only window: 0.3332 (replica) / 0.3374 (continuum) – 0.4154 MeV**; window FOM Δm/m = 0.448 at q* with the q̂-minimised E_min^{ZPL}(q*) = 1.715 eV (0.563 on the [100] axis alone) (WP8-F §2.7(b)).
**On/off-axis (O-WP3-9).** The q̂ minimisation keeps the TA minimum on the [100] axis up to |q| ≈ 1.35 keV; above, it moves to ϑ ≈ 0.05 rad. Angular
curvature γ_ω of the lowest TA about [100] (gamma.py, 8³): (001) tilt −0.88, −0.77, −0.56, −0.27, +0.08, +0.47 at |Q| = 0.1…0.6 Å⁻¹ (small-Q value vs
elasticity −0.96: PBE C^{el} consistent); (011) tilt −0.65 → −0.38. With r ≈ 0.95–0.8, the WP3-v3 criterion γ_ω > −(|K_pk|/2|q|)r gives the crossover where
γ(001) at d_K ≈ 0.25 Å⁻¹ (≈ −0.66) meets −0.64: |q| ≈ 1.35 keV, as found numerically. The [E] crossover 0.8–1.0 keV (WP3-v3 §M3(e)) is replaced; the
window optimum (0.9 keV) is on axis either way, so WP6-v3's edge statement stands.

## 5. Controls summary
| case | Si | Ge |
|---|---|---|
| INS dispersion, 5% at Γ/X/L (§2.3, §3.2) | 7/8 PASS; L_LO FAILED-CONTROL (−5.4%) | optical/LA 6/8 PASS; TA FAILED-CONTROL (−12…−14%; slopes −17…−19%) |
| ε_∞ within 10% of measured | FAILED-CONTROL (+11%) | FAILED-CONTROL (near-metallic PBE) |
| band topology (indirect, valley) | PASS (k_c 0.840 vs ~0.85) | FAILED-CONTROL (Γ below L) |
| Z* = 0 after ASR; raw acoustic ω(Γ) | PASS (raw Z* −0.09 e, ω 4.7 cm⁻¹) | PASS (raw Z* −0.97 e, ω 9.3 cm⁻¹) |
| C5 kinematics (CONTROLS): continuum PAER threshold E_g + ω_ν(Q*) − tilt, replica below E_g allowed | PASS: E_th(q) ≥ E_g on the whole grid, → E_g only at \|q\| → \|K_pk\| (0.11 meV at 1.90 keV); edges via (3.1′) | as Si |
| C18 anchor m(\|K_pk\|) = 0.474 MeV | PASS (0.473) | n/a |
C1–C4, C6–C8 (CONTROLS.md) concern the PAER amplitude, not these inputs: not applicable.

## 6. FORMULATED jobs (inputs in the qe-rtsc `rtsc/bench` layout: `@PSEUDO@`, outdir './', stage files scf.in → ph.in; run with rtsc/bench/phq.sh or the scf+ph stages of run-fork.sh; nscf/epw stages unused)
**6.1 Small-cell survivor batch** (code/COMP-PH/formulated/{C, SiC-3C, GaAs, LiF, NaF, SiC-4H, Al2O3}/: relax.in, scf.in, phG.in (Γ, epsil → ε_∞, ε₀ via
dynmat.x, Z*, ω_TO, ω_LO), ph.in (4³ q; 4×4×2 for 4H), q2r.in, matdyn.in (slopes along [100], [110], [111] → sound speeds, ω_max)). Cutoffs from the
ecut scans run here (code/COMP-PH/conv/conv_ecut_*.json, ≤ 1 meV/atom, ≤ 1 kbar): C 100, 3C-SiC 90, **GaAs 140** (Ga 3d: 25 meV/atom still missing at
100 Ry), LiF 90, NaF 90 Ry; 4H-SiC 90, Al₂O₃ 100 Ry (Al SG15 1.0 and 1.2 both carry 11 e). Plan: relax → copy celldm into scf.in → phG (ε_∞, Z*, LO–TO)
→ ph 4³ → 6³ for slopes. Controls: ε_∞ and ω_TO/ω_LO vs the [FT] rows of WP8-U-table.csv (GaAs ε_∞ 10.9, Z̄* 2.27; LiF 2.02/1.05; NaF 1.78/0.98; 3C-SiC
ε_∞ 6.5, ε₀ 9.7, ω_T/ω_L 98.7/120.5 meV; diamond ω_L 163 meV). Warnings: PBE GaAs at a_PBE is nearly metallic — run at a_exp and check the Γ gap first, as
for Ge. Cost (CPU, this box, from the Si timings scaled by N_el, ecut^{1.5}, nat²): 2-atom cells 0.5–6 h each with a 4³ q grid (GaAs at 140 Ry the largest; Γ-only runs 5–30 min), 4H-SiC 10–20 h, Al₂O₃ 30–60 h, ≤ 6 GB;
on the GPU fork minutes to ~1 h each.
**6.2 Ge E_min^{ZPL}(q)** (formulated/Ge-HSE-SOC/: scf.in HSE06, noncolin+SOC, Ge_ONCV_PBE_FR-1.0.upf, 8³ full grid nosym, nqx 4³, ecutfock 160;
Ge.win 16 spinor sp³ WFs, exclude 20 d bands, frozen window VBM+3 eV (fill @VBM_PLUS_…@ from scf.out); pw2wan.in). Then code/COMP-PH/emin.py (spinor
nv = 8) and phwin.py with the Ge fc. Control: L < Γ, E_g(L) within 0.1 eV of 0.744 before scissor. Cost 20–60 h CPU, 4–8 GB → over the gate.
**6.3 Ge DFPT 6³ q** (inputs as code/COMP-PH/chain.py phgrid, 80 Ry, k 8³, a_exp): 16 q at the measured 16 min/q ≈ 4 h → over the gate.

## 7. Cost-gate record (full table: code/COMP-PH/gate.md)
All run jobs: ≤ 2.1 h wall (Ge 4³ DFPT 7589 s, over its 40–70 min estimate but inside the 3 h gate), ≤ 0.1 GB RAM (largest: Si 8³ DFPT 4707 s; Ge 4³ DFPT 7589 s). Formulated: §6. The lock was shared with COMP-PAER and CMPMC jobs;
wall times include load (CPU/WALL ≈ 0.5 at peak). One run (Si Wannier nscf 14³) was cut by the usage-limit stop at 13:46 UTC and rerun from scratch.

## 8. Files
code/COMP-PH/: qe.py, chain.py (relax/scf/bands/DFPT driver), conv_ecut.py, conv_k.py, wan.py, emin.py, phwin.py, disp.py, sound.py, gamma.py,
xmlbands.py, mkformulated.py, build_csv.py, values.json, **properties.csv**, gate.md, conv/, inputs/, out/ (dyn files, force constants, frequency tables,
window JSONs, Wannier output), formulated/. literature/papers-COMP-PH/: lit.py records for the two INS papers (no PDFs).

## Symbols introduced/used
- **New:** a_PBE (PBE-relaxed lattice constant); Δ_sc (scissor shift to the measured gap); k_c (CBM position on the valley axis, units 2π/a);
  m_ZPL (kinematic zero-phonon mass edge, (3.1′) with E_min^{ZPL}); γ_ω(Q) as in WP3-v3 §M3(b) but evaluated per tilt plane, γ_ω^{(001)}, γ_ω^{(011)}.
- **Used:** E_g, E_x, E_x^b, E_min^{ZPL}(q), K_pk, Q*, q*, d_K, ω_ν(Q), ω_TA, ω_LA, c_LA, c_TA, ε_∞, ε₀, Z*, ω_TO, ω_LO, ω_max, v_max, m_min (WP6-v3 (3.1′)),
  G′ classes (WP3-v3 §M3(d)), Δm_PAER/m (WP8-F §2.7(b)).

## Interface flags
- IF-1 (WP3/WP6/WP8-F): the "PAER window grid" is defined here (§4); adopt or replace.
- IF-2 (WP6-v3 (3.1)(ii), WP8-F G-F5): Si edges now [CALC]: continuum 0.3374, replica 0.3332, ZPL kinematic 0.4154 MeV; ω_TA(Q*) = 14.7 meV replaces 13.5 ± 1.5 [E].
- IF-3 (WP3-v3 §M3(e), O-WP3-9): Si TA on-axis/off-axis crossover ≈ 1.35 keV (computed γ_ω), not 0.8–1.0 keV.
- IF-4 (WP8-U): PBE ε_∞ fails for Si (+11%) and Ge; keep measured ε as the ranking input; [CALC] ε_∞ only after a hybrid/scissor-corrected run.
- IF-5 (Ge, all users of DFT bands): PBE without SOC puts Γ below L in Ge at a_exp; any Ge band input needs HSE/GW+SOC (§6.2).
- IF-6 (WP8-U small cells): batch FORMULATED (§6.1); GaAs needs 140 Ry with SG15 Ga.
- IF-7 (controls): INS numbers are [UNVERIFIED] tabulations (DOIs verified); a PDF read of PRB 6, 3777 and PRB 3, 364 would close it.

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
- Si PAER continuum edge m_PAER = 0.3374 MeV [CALC] (±0.0004 incl. INS TA systematic); exciton replica 0.3332 MeV [CALC]; kinematic ZPL edge 0.4154 MeV [CALC].
- Si ω_TA(Q* = 0.510 Å⁻¹, [100]) = 14.7 ± 0.2 (+0.5) meV [CALC]; ω_LA = 26.1 meV [CALC].
- Ge PAER edge: continuum 0.2138 MeV [CALC] (TA FAILED-CONTROL; INS-scaled 0.2141), replica 0.2127 MeV [CALC/E: E_x^b inferred]; ω_TA(Q*) = 6.8 [CALC], 7.7 INS-scaled.
- Si window FOM Δm_PAER/m = 0.45 [CALC] (5-direction q̂ minimum; 0.56 on axis); Ge window FORMULATED.
