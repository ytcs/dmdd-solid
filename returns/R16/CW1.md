# R16 / CW1: closure of LE-24 … LE-47, LE-178, LE-179 (electronic sector, excitons, M1 window boundaries, PAER screening)

Brief: campaign/paer/briefs/R16/CW1.md. Ledger: state/LOOSE-ENDS.md §1 rows LE-24–LE-47, LE-178, LE-179 (§2 group CW1). Sources read: returns/R8/WP1-v3.md (§2–§11, R9
clean-up), returns/R8/WP3-v3.md (Part I, §3–§8, §10, §12, §14), returns/R3/X1.md, X2.md, returns/R15/COMP-PAER.md (final), returns/R15/COMP-PH.md (Si final, Ge
placeholders), returns/R12/WP7-B1-v2.md §8, §13, LIMITS.md (L3, L8, L9, L9b), CONVENTIONS.md (incl. R8/R13/R16/R17 amendments), NOTATION.md (collision checks),
CONTROLS.md, code/ENV.md. No referee report was read. Nothing committed; no other file edited.
**Checks:** code/CW1/checks.py, **32/32 PASS** (≈ 3 s, one core, no QE calls). **[CALC] runs** (single-core, outside the heavy lock, each < 20 s; the lock was held
by COMP-PH-Ge-phgrid): QE 7.6 pw.x, PBE, SG15 **Si_ONCV_PBE-1.2.upf** (scalar) and **Si_ONCV_PBE_FR-1.1.upf** (SOC), a_exp = 10.2631 bohr (and a_PBE = 10.3507 bohr
for one check), ecut 40 Ry with a 60 Ry repeat (vertices change ≤ 2%), SCF 8³; nscf at the unfolded k + q, wavefunctions matched by Miller index (exact within the
common G-sphere for NC pseudopotentials; 40 vs 60 Ry agree ≤ 2%). Inputs code/CW1/inputs/ (fork layout copies in inputs/fork/), scripts code/CW1/scripts/, outputs code/CW1/out/*.json; work dirs /root/work/CW1/.
The COMP-PH Wannier TB (/root/work/COMP-PH/Si/wan/Si_hr.dat, a_PBE, 8 sp³ WFs, 14³; gzip copies with _wsvec.dat committed in code/CW1/out/ so the Wannier-derived
numbers keep a [CALC] chain; sha256 of Si_hr.dat 35552c44b7d6c259…) and the COMP-PH 8³ force constants were read, not modified. Controls passed: C10a
on-axis zero (CW1-C9), C5 kinematics via [E13] (C4–C8), new mirror selection rules (C11–C13), COMP-PH anchor (C5).
**Literature:** literature/papers-CW1/ (2011.12765 fetched [FT]; PDF deleted, HTML kept). arXiv IDs cited here, all verified against the arXiv API: 2011.12765,
1202.3454, 1608.01994, 1705.04245, 2302.08085, 2507.14345, 2510.25835.
**Deliverable rule** (STATEMENT, user 2026-11-01): a compute row is closed by a derivation of the quantity and a specification a reader can follow. Every formulated
row carries a **Spec** block: what is computed, its expansion level τ (WP0 §6.1), method, convergence parameters, pitfalls, cost; fork layout per code/ENV.md.

## 0. Closure table

| Row | Item (short) | Status | Where | One-line result |
|---|---|---|---|---|
| LE-24 | [E13] ab initio thresholds, masses | CLOSED-AS-EXACT-GAP (Si part CLOSED) | §1 | Si first ZPL **0.400–0.405 MeV** [CALC] (off axis, {001} mirror plane; on-axis 0.415 is not the minimum); M_x = 1.19 m_e [CALC]; Ge formulated |
| LE-25 | (2̄00) vertex, ∇_kρ_cv | CLOSED | §2 | (2̄00) vertex Σ_v\|ρ\|² = 0.150 [CALC], **not small**; allowed-size ZPL opens at **≈ 0.50 MeV** (ratio ≈ 2), leads robustly from ≈ 0.51; 0.62 fallback withdrawn |
| LE-26 | ZPL/PAER ratio [E14], two-channel band | CLOSED-AS-EXACT-GAP | §3 | ϖ̄_II = 0.016 / 0.13 / 0.35 at ε_ex = E_x^b / 50 / 100 meV (vertex [CALC], PAER [E]); PAER leads to ≈ 0.42–0.44; two-channel ≈ 0.44–0.51 MeV |
| LE-27 | Si TA on/off axis; (2̄00) LO; LA-kink SOC | CLOSED | §4 | TA crossover 1.35 keV (COMP-PH, adopted); (2̄00) LO minimum **off axis** [CALC] → p̄_on = 3; SOC piece → §13 |
| LE-28 | finite-q BSE beyond TDA | CLOSED-AS-EXACT-GAP | §5 | TDA error on L = [ε₁/ε₁^{TDA}]² − 1 ≈ +100% at \|q\| ≈ 0.7 Å⁻¹ [E]; consistent hybrid rule; spec |
| LE-29 | exciton dispersion, anisotropic masses | CLOSED | §6 | E_x(Q) = E^{ZP}_min(Q) − E_x^b[μ(Q)]; masses and Dresselhaus parameters [CALC]; hole off Γ at the optimum; spec |
| LE-30 | exciton–phonon replicas (W.14) | CLOSED-AS-EXACT-GAP | §7 | completeness reduced to the two-pair intermediate sector; W → 0 limit [D]; spec |
| LE-31 | G-X8 crystal exciton Migdal | CLOSED | §8 | (X8.1) with p-resolved BSE line strengths; spec in WP3 G6 style |
| LE-32 | Frenkel / self-trapped excitons NaI | CLOSED-AS-EXACT-GAP | §9 | Franck–Condon (Huang–Rhys) dressing of [E7] (CW1.9); S_HR and BSE inputs = gap; spec |
| LE-33 | G7 4-component no-pair response | CLOSED-AS-EXACT-GAP | §10 | FW to O(m⁻²) [D], next order ~10⁻⁶ for Ge 3d; 2% bound kept; code = gap |
| LE-34 | triplet beyond IP | CLOSED-AS-EXACT-GAP | §11 | ladder equals singlet ladder up to the exchange term O((a/a_x)³) [D, sketch]; interim ×1.3–2 justified; spec |
| LE-35 | LFE of j_T, in-medium 𝒪₈; L3 | CLOSED-AS-EXACT-GAP | §12 | mixed-block formula (CW1.12); L3 factor stated as interval 8–39 [E]; spec |
| LE-36 | SOC near edges | CLOSED-AS-EXACT-GAP (Si part CLOSED) | §13 | Si SOC-lifted vertex [CALC]: 1.6×10⁻⁶ on axis (WP1's 4% amplitude → 0.3%), 1.3×10⁻⁴ at the true optimum; Ge spec |
| LE-37 | plasmon → phonon branching | CLOSED | §14 | branching = sideband/ZPL ratio at ω_pl (CW1.14), 10⁻³–10⁻² [E]; no DM-produced plasmon in Si |
| LE-38 | G10 IP library tables | CLOSED | §15 | 12 functions + R⁰_{GG′} defined; spec with PT-zero diagnostics |
| LE-39 | G11 S₄, S₆, S₈ | CLOSED-AS-EXACT-GAP | §16 | spec exists (WP1 §8 G11); projection and diagnostics stated |
| LE-40 | X2-N1 1D contact-kernel model | CLOSED | §17 | model, both sides of the comparison and exact benchmarks (CW1-C31); spec |
| LE-41 | X2-N2/N3 Route S in Si | CLOSED-AS-EXACT-GAP | §18 | supercell sizes, ZG sampling, cost; envelope [0.4, 1.8] kept |
| LE-42 | X2-N4 ε̃⁻¹_{G0}(q,ω) → δ_LF | CLOSED | §19 | δ_LF formula (CW1.19); primitive-cell spec (cheap) |
| LE-43 | δρ^V unrestricted band sum | CLOSED | §20 | Kubo (Matsubara) form (CW1.20) derived; one-electron unrestricted sum differs by ΔF (O(1) for intraband intermediates): claim withdrawn |
| LE-44 | ALDA k_xc pair term | CLOSED | §21 | k_xc = (8/27)C_x n^{−5/3}; term ≲ 5% of the pair term, ≲ 2.5% of L^{PA} [E] |
| LE-45 | L9b(c) ALP/SOC | CLOSED | §22 | WP1-v3 §2.5 [D] confirmed; spin-sum identity checked (CW1-C22) |
| LE-46 | σ₁ T-transfer to mK | CLOSED | §23 | inverse transfer (CW1.23) exact for branch spectra; uncorrected 77 K data ×2.6/1.9/1.5/1.3 at 15/25/50/100 meV |
| LE-47 | C8 GaAs decoy window | CLOSED-AS-EXACT-GAP | §24 | parabolic [E]: PAER edge 0.435, L-valley ZPL 0.51 MeV → band ≈ 0.43–0.51 (not 0.4–0.9); band-structure spec |
| LE-178 | non-adiabatic AHC | CLOSED | §25 | formula (CW1.25); Si ZPR_g −56 meV [FT 2011.12765]; non-adiabatic intraband term ≈ 0.2 meV [E]; window impact ≤ 0.002 MeV |
| LE-179 | X1 residual tags | CLOSED | §26 | D^n symmetric at extrema [D]; D/c ≈ 300 keV ≫ q [E→D with CALC c]; piezo log irrelevant in the window [D] |

Counts: CLOSED 15, CLOSED-AS-EXACT-GAP 11 (LE-24 and LE-36: Si part CLOSED, Ge part an exact gap), CANNOT-CLOSE 0.

---
## 1. LE-24: ab initio zero-phonon thresholds [E13]; band masses; Ge
**Item.** Replace the parabolic [E] Si thresholds (0.42 (0.40–0.44) forbidden class, ≈ 0.54 allowed) and the Ge 0.32–0.36 MeV by ab initio E^{ZP}(q); settle the
pair mass (1.41 vs 1.19 m_e) and Q_w. COMP-PAER (a_exp, 400 directions, 40³ trilinear grid) gave 0.405–0.408 MeV; COMP-PH (a_PBE, Wannier, five directions) gave
0.4154 MeV. Both are final; they disagree by 0.01 MeV, and the cause had to be found.

**1.1 The threshold as a joint minimum [D].** A zero-phonon final state of total (unreduced) momentum q has lowest energy E^{ZP}(q) = min_k[ε_c(k+q) − ε_v(k)]
(continuum) or that minus E_x^b (1s line). By [E13] the channel opens at m_χ^{ZP} = min_q |q|²/[2(|q|v_max − E^{ZP}(q))]. The function m(q, E) is increasing in E
at fixed q, so

  m_χ^{ZP} = min_{q, k} |q|² / {2[|q|v_max − ε_c(k+q) + ε_v(k)]},                                                                                          (CW1.1)

an unconstrained minimum over six variables (three for q, three for the hole k). Restricting q̂ to a few directions, or k to the valence maximum, gives an upper
bound. This is the form evaluated here (scripts/emin_fast.py, 21 Nelder–Mead starts, Wannier TB of COMP-PH, scissor to E_g(0) = 1.170 eV).

**1.2 Result [CALC].** The minimum is **off the [100] valley axis**: |q| = 1.293 keV, q̂ tilted by ϑ_ZP = 0.181 rad in a {001} plane containing the axis; the hole
sits at k_v = (0.126, −0.107, 0)·2π/a, 0.061 eV below the VBM, in the flat heavy-hole direction (m_hh[110] = 2.5 m_e, §6); the electron sits at
(0.688, −0.004, 0)·2π/a, on the valley axis 0.17·2π/a short of k_c. Values (CW1-C4…C7):
| evaluation | m_χ^{ZP} continuum (MeV) | note |
|---|---|---|
| Wannier, a_PBE, joint (q,k) minimum | 0.3997 | 18 of 21 starts; E^{ZP} = 1.3355 eV |
| DFT (QE nscf) at that point, a_PBE | 0.4019 | E = 1.3469 eV (Wannier interpolation +11 meV) |
| DFT at the same fractional point, a_exp | 0.4046 | E = 1.3546 eV; not re-minimised (upper end) |
| on-axis local optimum (Wannier) | 0.4150 | reproduces COMP-PH 0.4154 (CW1-C5) |
So **m_χ^{ZP} = 0.400–0.405 MeV** (continuum); the spread is the lattice constant (a_PBE vs a_exp) plus the interpolation error. The 1s line lowers the onset by
m·E_x^b/(|q|v_max − E) = 0.0028 MeV (2p: 0.0007): bound-line onset **0.397–0.402 MeV**. Reconciliation: COMP-PH's 0.4154 is the on-axis value, an upper bound
(five directions miss the off-axis valley in θ); COMP-PAER's 0.405–0.408 at a_exp with 400 directions agrees at its lower end with the a_exp number here, its upper
end being the trilinear-grid bias it reported. The angular scan (CW1-C5) shows why: at |q| = 1.2–1.48 keV the [100] axis is a local **maximum** of E^{ZP}(q̂),
with minima at ϑ ≈ 0.13–0.22 rad in the {001} planes, 14–107 meV lower than on axis (deeper minima in {001} than in {011}). Curvatures at the optimum:
β^{ZP}_θ = 2.47 eV/rad² (in plane), β^{ZP}_z = 3.70 eV/rad² (out of plane). The (2̄00)-class edge is §2.

**1.3 Band masses [CALC] (masses.py, CW1-C1–C3).** PBE, a_exp, no SOC: k_c = 0.843 X; m_l = 0.923, m_t = 0.194; holes m_lh[100] = 0.168, m_hh[100] = 0.264 (×2),
[110]: 0.108, 0.265, 2.50; [111]: 0.096, 0.655 (×2) (m_e). Along the valley axis the pair translational mass is **M_x = m_l + m_hh[100] = 1.19 m_e**: WP1-v3's value
is confirmed; WP3-v3's 1.41 m_e used an angle-averaged (density-of-states) heavy-hole mass, which is the wrong object for a pair moving along [100]. Q_w at
δ₀ = 0.3 eV (WP3 (C30a)) = **0.311 Å⁻¹** (0.340 with 1.41). Dresselhaus inverse-mass parameters (no SOC, units 1/m_e): L = 5.96, M = 3.79, N = 8.88 (spread 0.18
between the [110] and [111] determinations, i.e. the nonparabolicity at δk = 0.01–0.03·2π/a). The parabolic [E13] table of WP1 cannot see the off-axis
optimum: it assumes the hole at Γ. This is the main physics correction of this row.

**1.4 Ge [CLOSED-AS-EXACT-GAP; numbers flagged].** COMP-PH Ge results are placeholders (FAILED-CONTROL band order at PBE). Strongest derived statement: (CW1.1)
holds unchanged; the parabolic interim 0.32 (0.32–0.36) MeV [E] is an **upper bound only if the minimum is on the L axis**, and the Si lesson (a warped heavy hole
moves the optimum off axis and lowers m by ≈ 4%) applies to Ge as well, whose Γ₈ heavy hole is more anisotropic. Missing step: E^{ZP}(q) from quasiparticle
bands. **Spec.** What: E_c(k+q) − E_v(k) on the joint (q,k) space, then (CW1.1) per class (L valley G′ = 0 and its Umklapp copies; Γ direct). τ: `nB=0|ng=1|X=QP
bands` (no screening needed for a threshold). Method: COMP-PH §6.2 inputs (formulated/Ge-HSE-SOC: HSE06 + SOC, Ge_ONCV_PBE_FR-1.0, a_exp, 8³ full grid, nqx 4³,
ecutfock 160 Ry; Wannier 16 spinor sp³ WFs, frozen window VBM + 3 eV), then code/CW1/scripts/emin_fast.py with nv = 8 spinor bands and kc → L. Convergence: Wannier
band error ≤ 10 meV up to 1 eV above the CBM (check against the HSE nscf at 10 random k); E^{ZP} at the optimum vs a direct HSE nscf at (k_v, k_v + q) (as done
here for Si, ≤ 10 meV). Control: L₆ below Γ₇⁻ and E_g(L) within 0.1 eV of 0.744 eV before the scissor. Pitfalls: PBE inverts L/Γ (COMP-PH IF-5); a scissor on
PBE bands is ill-defined; the mirror rule of §2.2 applies with σ_d planes, which are in T_d (no glide phase), so whether the threshold is allowed must be checked
at the true optimum, not on the L axis. Cost: 20–60 h CPU, 4–8 GB (COMP-PH §6.2) plus < 1 h for the minimisation.

## 2. LE-25: the (2̄00) Umklapp vertex, ∇_kρ_cv, and which zero-phonon class leads
**Item.** WP1-v3 hedged "allowed ZPL leads above 0.54 MeV only if |ρ_cv^{(2̄00)}| ≳ η_PA^{1/2}|ρ^{ref}|, otherwise from 0.62 MeV ((1̄11))", because the (200)
Fourier component of the diamond potential vanishes.

**2.1 Vertices [CALC] (vertex.py, vertex_pair.py; 40 and 60 Ry agree to ≤ 2%).** ρ_cv(k_v, q) = ⟨ψ_{c,k_v+q}|e^{iq·r}|ψ_{v,k_v}⟩ with k_v + q unfolded:
| quantity | value | control |
|---|---|---|
| G′ = 0, on axis, extremum (q = k_c x̂): Σ_v\|ρ_c₁v\|² | < 10⁻²¹ | C10a zero (CW1-C9) |
| (2̄00) class at its extremum (q = (k_c − 2)x̂, \|q\| = 2.64 keV): Σ_v\|ρ_c₁v\|² | **0.150** (60 Ry 0.150) | — |
| (2̄00) at the pair optimum, q = −(1.00, 1.05, 1.10)X | 0.157, 0.156, 0.154 — **light hole only**, heavy holes < 10⁻²¹ | multiplicity 1 (CW1-C11) |
| (1̄11) class at its extremum | 0.037 | — |
| G′ = 0 transverse gradient \|∂_{k⊥}ρ\| at the extremum / at the 1.39 keV on-axis pair | 0.40 Å / 0.25 Å | linear (CW1-C14) |
| G′ = 0 transverse q-gradient \|∂_{q⊥}ρ\| (hole relaxed) at 1.39 keV | 2.21 Å | — |
The (2̄00) vertex is **not small**: it is the size of an ordinary allowed vertex (for scale, the four-band sum Σ|ρ|² at |q| = 1.155 Å⁻¹ is 0.45). The vanishing (200)
potential component suppresses only a nearly-free-electron estimate; the vertex involves all Fourier components of both Bloch functions. On the
axis it lives entirely in the light hole (Δ₂′), as the multiplicity-1 rule B₂ ⊗ (B₂ ⊕ E) ∋ A₁ of WP1-v3 §3.2(c) requires.

**2.2 A second selection rule: the {001} mirror [D, checked].** For q and k_v in a {001} plane containing the valley axis, the mirror σ_z is a symmetry of the
pair. σ_z ∈ O_h∖T_d carries the translation t_d, so for G′ = 0 the operator phase is 1 and the vertex is allowed only between states of equal σ_z parity; for
G′ = (2̄00) the phase is e^{−iG′·t_d} = −1 and the rule inverts. At the §1.2 optimum the top (heavy) hole is σ_z-odd relative to the Δ₁-like electron:
**its G′ = 0 vertex vanishes** (3×10⁻¹⁴; the second valence band, 0.39 eV deeper, has 0.064) (CW1-C12). Off the plane the vertex grows linearly:
|∂_{q_z}ρ| = 1.38 Å, |∂_{k_z}ρ| = 0.31 Å. So the "second class" of WP1 is not an on-axis accident: the first zero-phonon final state is second class by the mirror, and
remains so at the true off-axis optimum. In the (2̄00) class the same mirror makes the top hole **allowed**: at the (2̄00) edge, |ρ|² = 0.0095 (on the X face,
c₁), 0.024–0.036 at 0.02–0.10·2π/a inside the class (vertex_U200opt.json; CW1-C13).

**2.3 Where the allowed-size channel opens [CALC].** With (CW1.1) restricted to the (2̄00) class (unfolded electron beyond the X face, k_{v,x} + q_x ≤ −1·2π/a), the
minimum sits on the X face: **m_χ = 0.4992 MeV** at |q| = 1.83 keV (a_PBE, Wannier; DFT pair energy at that point 5 meV lower, i.e. ≈ 0.498), with the hole at
|k_v| = 0.26·2π/a (CW1-C8). COMP-PAER's 0.547 MeV used a nearest-pocket class assignment on its 40³ grid; with the class defined by the unfolded electron momentum, the
allowed-size channel opens earlier, on the X face. **Decision (LE-25):** ZPL/PAER (ε₂ units, same (q,ω); ratio.json; §3 for the model) = 2.4 / 2.2 / 1.6 at ε_ex = 1 / 14.7 / 100 meV on the X face
(m_χ = 0.498 MeV), 10 / 10 / 6 at 0.05·2π/a inside the class (reached from m_χ ≤ 0.508 MeV at the same hole k), 10²–10⁵ on the axis ((2̄00), light hole, 0.547 MeV).
The vertex is [CALC]; the PAER side is COMP-PAER's (P.1) [E ×/÷10], so the decision is [E] with a [CALC] input: at the opening the two are comparable (≈ 2, inside
the PAER band), from ≈ 0.51 MeV the ZPL leads by ≥ 10. **The IF-6 hedge is removed: an allowed-size zero-phonon channel opens at ≈ 0.50 MeV and leads robustly from
≈ 0.51 MeV; the "otherwise from 0.62 MeV ((1̄11))" fallback is withdrawn.**

## 3. LE-26: forbidden-class ZPL against PAER [E14]; the two-channel band
**Item.** WP1-v3 [E14] (ϖ_II ≈ 0.03–2 at the edge, 0.2–15 at ε_ex = 0.1 eV) used ℓ_∇ = 1–3 Å relative to an unspecified ρ^{ref} and a transferred η_PA. Close with
S^{PA} on the same (q,ω) points.

**3.1 Comparison in ε₂ units [D].** Both channels are screened by the same external 1/ε₁(q,ω)² at the same (q,ω) (CONVENTIONS §7; WP3 (M.13)–(M.14), G = 0
head), so the ratio is that of the proper ε₂ = (2πα/q²)S. Zero-phonon side: [E8] (Wannier–Mott continuum at fixed q, μ_x = 0.108 m_e from a_x = 4.9 nm,
E_x^b = 14.7 meV), with J(ε) = (2μ_x)^{3/2}√ε/(4π²):

  allowed: S_I = 4π|ρ|²J(ε)𝒮_F(ε);   second class: S_II = 4π|∂ρ|²(2μ_xε/3)J(ε)𝒮_F(ε)(1 + ζ_S²).                                                                (CW1.3)

PAER side: COMP-PAER (P.1), ε₂^{PA}(q,ω) = ε₂^{PA,opt}(ω)𝔉_ρ(q), with 𝔉_ρ extended here to |q| = 1.155–1.34 Å⁻¹ ([CALC] proxy: 0.0172, 0.0121, 0.0104). Above E_min(q)
PAER is outside the window, so this is the DC-convention value (WP3 (M.10)) of a model built inside it: an extrapolation, stated. Angle average at fixed |q| over the 24
equivalent minima (6 valleys × 2 mirror planes × ±ϑ), with E^{ZP} = E₀ + β_θϑ² + β_zφ² and |ρ|² = |∂_{q_z}ρ|²|q|²φ² + |∂_{k_z}ρ|²k_z²:

  S̄_II = 24[(π|∂_{q_z}ρ|²|q|²/(2β_z√(β_θβ_z)))∫₀^ε u J(ε−u)𝒮_F du + (π/√(β_θβ_z))∫₀^ε |∂_{k_z}ρ|²(2μ_x(ε−u)/3)J𝒮_F(1 + ζ_S²) du]          (CW1.4)

(cone integral checked against a direct 2-D quadrature, CW1-C17). Validity: the cones must not overlap, ε ≲ β_θϑ_ZP² ≈ 0.08 eV; above, (CW1.4) overcounts. Bias: the isotropic μ_x = 0.108 m_e ignores that the hole at the
optimum sits in the 2.5 m_e direction; the local reduced-mass tensor has a larger density-of-states mass, so J, and ϖ̄_II, are underestimated by ≈ ×1.3–1.6 [E]
(inside the PAER band and opposite to the 𝔉_ρ bias below).

**3.2 Numbers (ratio.py) [vertex CALC, PAER E].**
| ε_ex | 1 meV | 14.7 meV | 50 meV | 0.1 eV | 0.2 eV |
|---|---|---|---|---|---|
| pointwise, at the mirror-plane optimum (k_z term) | 0.011 | 0.018 | 0.028 | 0.036 | 0.043 |
| same, SOC-lifted piece (§13) | 0.10 | 0.085 | 0.061 | 0.044 | 0.028 |
| **ϖ̄_II, angle-averaged, (CW1.4)** | 1×10⁻⁴ | **0.016** | **0.13** | **0.35** | ≤ 0.83 (overcount) |
| angle-averaged SOC piece | 2×10⁻⁴ | 0.002 | 0.006 | 0.008 | 0.010 |
| on-axis pointwise (old geometry, q = 1.39 keV) | 0.013 | 0.022 | — | 0.046 | 0.066 at 0.5 eV |
WP1's central 0.3–2 is replaced by values 10–50× smaller near the edge. Uncertainty: the PAER side carries ×/÷10 (COMP-PAER §5); its main term, the 𝔉_ρ proxy, is
more plausibly a lower estimate (COMP-PAER §1), so the ratios above are more plausibly upper estimates.

**3.3 In m_χ [E].** At the optimum |q| the largest reachable excess energy is ε_ex^{max}(m_χ) = |q|v_max − |q|²/2m_χ − E₀ = 0.05, 0.10, 0.19 eV at m_χ = 0.41, 0.42,
0.44 MeV (CW1-C19), and the ZPL-open region is a small part of the PAER-reachable (q,ω) set (most PAER weight sits below E_min(q)). Since ϖ̄_II ≤ 0.35 for
ε_ex ≤ 0.1 eV (≈ 1 with the PAER band at 𝔉_ρ/3), **PAER leads the integrated electronic rate at least to ≈ 0.42 MeV, centrally to ≈ 0.44 MeV**; 0.44–0.51 MeV is a
two-channel region (the allowed-size ZPL opens at ≈ 0.50, comparable to PAER); from ≈ 0.51 MeV the allowed-size ZPL leads (§2.3). **Exact remaining gap:** the integrated crossover needs S^{PA}(q,ω) from the amplitude, not
(P.1), on the same grid. **Spec:** COMP-PAER §8 tier H stage 6 (fork layout code/COMP-PAER/tierH/Si), with the output grid extended to the mirror-plane cones:
|q| = 1.2–1.9 keV, ϑ ≤ 0.4 rad in {001} and {011}, φ ≤ 0.15 rad out of plane, ω from E_min(q) − 0.3 eV to E_min + 0.3 eV (DC convention outside the window, WP3
(M.10), with the O4 d11 edge shell reported separately); then dℛ^{X0}_II/dℛ^{X+} by (M.6) with [E8]/(CW1.3) on the same bins. τ: `nB=0|ng=2|X=RPA+LFE|K=1ph-inc` for
PAER, `nB=0|ng=0|X=Wannier-Mott` for the ZPL. Pitfall: the ZPL vertex must be evaluated with the top hole at k_v(q), not at Γ (§1.2). Cost: as tier H (≈ 1 GPU-day).

## 4. LE-27: location of the PAER minima (Si TA on/off axis; (2̄00) LO; LA-kink SOC)
**TA (O-WP3-9) [CALC, COMP-PH §4, adopted].** With the computed angular curvature γ_ω(Q) of the lowest TA, the dispersive criterion of WP3-v3 §M3(b),
γ_ω(d_K) > −(|K_pk|/2|q|)r(d_K), puts the crossover at |q| ≈ 1.35 keV, not 0.8–1.0 keV [E]; the window low-mass end (|q| ≈ 0.9 keV at 0.337 MeV) is on axis. Closed by
citation; the owed text is below. **(2̄00)-class LO [CALC] (lo_gamma.py on the COMP-PH 8³ force constants).** For Q* = K_pk − q near Γ the LO branch falls with |Q|
(ω₀ = 62.17 → 61.78 meV from 0.03 to 0.25 Å⁻¹) and its angular curvature is negative in both tilt planes (γ_ω = −3×10⁻⁴ … −0.02). Both terms of the (M.7a)
coefficient are then negative, so the axis is a **maximum** of the LO threshold at every |q| of that class (CW1-C21): the LO minimum is off axis, where the vertex
is generic, and **p̄_on(LO, (2̄00)) = 3**, not 4. This class lies above 0.5 MeV, where the allowed ZPL leads (§2.3), so it does not move the window. **SOC admixture of
the LA kink:** §13 (≲ 10⁻⁴ relative weight [E], from the computed on-axis SOC lift).

## 5. LE-28: finite-q BSE beyond TDA
**Strongest derived statement [D].** In the BSE pair space at total momentum q, the full (coupling) Hamiltonian differs from TDA by the resonant–antiresonant
block. The long-range exchange v_C(q+G) in that block carries the external screening of the DM vertex (WP1 [E7]: the exchange makes S the screened L). In the
macroscopic (head) approximation, dropping the antiresonant poles keeps only (E_λ − ω)⁻¹ in ε₁ − 1. For a single Penn-type oscillator E₀:

  (ε₁^{TDA} − 1)/(ε₁ − 1) = (E₀ + ω)/(2E₀),   L^{TDA}/L ≈ [ε₁/ε₁^{TDA}]²   (ε₂ unchanged at ω > 0).                                                            (CW1.5)

With E₀ = 4.8 eV, ω = 1.3 eV and ε₁(0.7 Å⁻¹) ≈ 5.5 (COMP-PAER Cappellini model), ε₁^{TDA} ≈ 3.9 and **TDA overstates L by ≈ ×2** in the PAER-window q range [E].
The factor tends to 1 as q → ∞ (ε₁ → 1) and is largest near q → 0. **Rule [D]:** a TDA BSE may be used for the proper ε₂ (excitonic line shapes, bound lines), but
the external screening must then come from the full RPA+LFE ε₁ (no double counting: the head is removed from the BSE exchange). Equivalently, run full coupling.
**Exact remaining gap:** a beyond-TDA finite-q BSE run for Si/Ge. Interim Δ^τ_BSE ∈ [+0.3, +1.0]×S (type M) plus bound lines (type A) is kept, with the second-class
bound-line amplitudes now from §2.2 (mirror-plane vertex, |∂_{q_z}ρ|, |∂_{k_z}ρ|). **Spec:** WP1-v3 §8 G5 unchanged (QE → G₀W₀ → finite-Q BSE, 4 VB × 12 CB, 8³
coarse kernel interpolated to 24³, Haydock ≈ 200 iterations, coupling on, f-sum check < 1%, ≈ 10³ node-h), plus two items: (i) report S^{TDA} and S^{full} at |q| =
0.5, 0.7, 1.0, 1.4 keV to test (CW1.5); (ii) evaluate the pair basis around the §1.2 optimum (hole off Γ), not only at the band extrema.

## 6. LE-29: exciton dispersion and the hydrogenic series with ab initio masses
**Derived statement [D, effective mass].** For total momentum Q the pair minimum sits at (k_v(Q), k_v(Q) + Q) of (CW1.1). Expanding ε_c − ε_v to second order
there gives a reduced-mass tensor μ(Q)⁻¹ = ∇²ε_c(k_v + Q) − ∇²ε_v(k_v) (Hessians). The exciton band is

  E_x(Q) = E^{ZP}_min(Q) − E_x^b[μ(Q), ε_∞],                                                                                                                      (CW1.6)

with E_x^b from the anisotropic hydrogenic problem (Lipari–Baldereschi; variational in the Kohn–Luttinger form for an axial μ). The new point: at the [E13] optimum the
hole is **not** at Γ (§1.2), so μ(Q) varies along the dispersion. Along the axis it uses m_l, m_t and the [100] hole masses; at the optimum it uses the heavy hole
at k_v ≈ 0.165·2π/a. E^{ZP}_min(Q) along Γ–X on both sides of X and across the {001} planes is tabulated in out/emin_fast.json (scan) and emin_qstar.json. Inputs
[CALC] (§1.3): m_l, m_t, hole masses, and Dresselhaus parameters L = 5.96, M = 3.79, N = 8.88 (no SOC; with SOC add Δ_SO = 48.6 meV PBE, §13). Exciton binding
14.7 meV (Si) remains the literature value [E, memory]. **Spec** (effective-mass run, optional): Hessians of the Wannier bands at (k_v(Q), k_v(Q) + Q) for Q on
the scan grid (finite differences, step 0.005·2π/a); E_x^b by a 3-D variational anisotropic hydrogen (basis of 30 anisotropic Gaussians) with static ε_∞ = 11.7
[measured]; output E_x(Q) and the 1s/2p weights; convergence: E_x^b to 0.1 meV vs basis size; pitfall: degenerate heavy/light holes near Γ need the 6 × 6 k·p
(SOC) form, not scalar masses. Cost: minutes. τ: `X=Wannier-Mott(static ε_∞)`. The BSE route is §5.

## 7. LE-30: exciton–phonon replicas (W.14) and their completeness
**Strongest derived statement [D].** (W.14) is the exciton-basis form of the PAER amplitude. Two limits hold: (i) **W → 0** (no e–h interaction) with A^λ = δ_{λ,cvk}:
the first family becomes path A + D and the second B + C of WP3 §M2, provided the λ′ sums run over the complete one-pair space at P and at Q; then (W.14) = (M.1)
exactly. (ii) In TDA with the one-pair basis complete, the λ′ sum is a resolution of the identity on that space. The unrestricted-sum (Pauli) theorem of (M.1),
however, also used intermediate states with **two pairs** (path C/D: the phonon creates a second pair whose hole is then filled). In the exciton picture these are
biexciton-continuum states, absent from (W.14). **Exact remaining gap:** a proof that the two-pair sector reduces to the one-pair Z-graph terms at the BSE level
(true at W = 0 by the M2 theorem; open with W). Leading size [E]: the two-pair correction differs from its W = 0 value by O(E_x^b/E_g) ≈ 1%. **Spec:** WP3-v3 §8 G5
(finite-momentum BSE at the pocket set P ≈ 0.85X and, per §1.2, at P = q* + Q* with the hole off Γ; EPW g on the same U(k); g^x by 1705.04245 Eq. (49); ≈ 10³ k
per pocket; ≈ 10⁴ CPU-h), with the control: run (W.14) with W switched off and compare to (M.1) on the same grid (≤ 1%).

## 8. LE-31: G-X8 crystal exciton Migdal
**Quantity [D].** (X8.1) (WP7-B1-v2 §8): the exciton-line part of S^{ee}_{GG′}(p,ω_e) = (4π/V)Σ_λρ_{λ0}(p+G)*ρ_{λ0}(p+G′)δ(ω_e − E_λ(p_r)),
ρ_{λ0}(p+G) = Σ_{cvk}A^{λ*}_{cvk}ρ̃_cv(k,p+G), inserted into the Migdal convolution WP3-v3 (W.5). Needed: the line strengths ρ_{λ0}(p+G) (including the G ≠ G′
cross terms) and energies E_λ(p_r) for p **over the whole BZ and G shells**, because (W.5) integrates the electronic momentum p against the lattice response at
q − p, not only near p → 0. **Spec (WP3 G6 style):** (i) finite-p BSE (§5 machinery; TDA allowed for the proper lines, external screening from RPA+LFE) on an 8³ IBZ p grid plus
G-shells to |p| ≤ 5 keV (≈ 60 irreducible p after O_h); 3 lowest exciton bands, Haydock for the oscillator strength of each line; (ii) interpolate f_λ(p), E_λ(p);
(iii) convolve with S^{GS}_κκ from phonopy by (W.5) with ω_e on the lines; (iv) control: the p → 0 limit reproduces the optical exciton strength; Σ_λ f_λ(p) plus
the continuum obeys the f-sum (CONVENTIONS §6) to 1%. Outputs: P^{Mig}_λ(q) per line. τ: `X=BSE(TDA lines)+RPA head`. Cost: ≈ 1 node-h per p → ≈ 60–100
node-h. Pitfall: the Migdal boost operator is e^{ip·Σr} with **unreduced** p; Umklapp copies (p + G) carry the same exciton band with different strengths.

## 9. LE-32: Frenkel and self-trapped excitons in NaI
**Formula [D under linear coupling, harmonic lattice, Condon approximation].** For a localized (Frenkel) exciton λ coupled linearly to phonons with Huang–Rhys
factor S_HR and mean frequency ω̄ (single effective mode), the DM creates λ vertically (Franck–Condon), and the zero-phonon line of [E7] is dressed:

  S_λ(q,ω) = |ρ_{λ0}(q)|² Σ_{n≥0} e^{−S_HR}(S_HR^n/n!) 2πδ(ω − E_λ − nω̄)  →  Gaussian of mean E_λ + S_HRω̄ and variance S_HRω̄² for S_HR ≫ 1 (T = 0).              (CW1.9)

Self-trapping is the relaxation after creation: the exciton relaxes by the reorganisation energy S_HRω̄ to the STE, which decays radiatively or non-radiatively;
that belongs to the cascade (WP5), not to the creation vertex. The first moment of (CW1.9) equals that of the bare line + S_HRω̄, the Lamb–Mössbauer
displacement, consistent with WP3 (W.12). The Frenkel vertex ρ_{λ0}(q) is atomic-like (I⁻ 5p → Na⁺/I 6s-like) for |q| ≫ 1/a_x. **Exact remaining gap:** S_HR, ω̄
and ρ_{λ0}(q) for NaI. **Spec:** (i) finite-q BSE for NaI (§5; Na 2p/I 4d semicore excluded or frozen; 6³ → 18³ interpolated; 2507.14345 is the DM precedent and
its NaI BSE the cross-check); (ii) S_HR from a constrained-DFT (ΔSCF) or TDDFT excited-state relaxation of the STE in a 64–216-atom supercell (V_k-centre +
electron), S_HR = ΔE_relax/ω̄ with ω̄ from the projected phonon DOS; (iii) (CW1.9) with the multimode generalisation. τ: `X=BSE ⊗ FC(S_HR)`. Pitfalls: hybrid
functional needed for hole localisation (PBE delocalises the V_k centre); spin-orbit of I (≈ 0.9 eV) splits the exciton. Cost: ≈ 10³ CPU-h (supercell relaxations dominate).

## 10. LE-33: G7, no crystal 4-component response with no-pair projection
**Strongest derived statement [D, WP1-v3 §5.2–5.3].** The FW reduction to O(1/m_e²) gives every operator correction; the next order is O(⟨p²⟩²/m_e⁴) ≈
(Z_effα)⁴ ≈ 10⁻⁶ for the Ge 3d shell (⟨p²⟩/m_e² ≈ 10⁻³), so a ZORA + SOC (two-component) crystal response with picture-change-corrected operators misses
only (i) that O(m_e⁻⁴) remainder and (ii) the no-pair projection error, which is O(α²) for valence and O((Z_κα)²) ≤ 0.055 only for Ge 1s, unreachable for halo DM
(WP1-v3 §5.4). The ≤ 2% bound for Ge 3d (SO split/binding = 0.58/29.5) stands as the conservative statement; the ≈ 10⁻³ estimate is its central value. **Missing
step:** a crystal 4-component finite-q response code. Spec as WP1-v3 §8 G7 (FLAPW with SOC or PAW with core reconstruction; Ge 3d binding spread PBE/HSE/G₀W₀/ΔSCF
as a nuisance; core-level BSE at finite q; q ≤ 30 keV, ω ≤ 200 eV, 12³ k). Control: (E11) relativistic f-sum shift −0.58% (Ge) reproduced to 0.1%.

## 11. LE-34: triplet channel beyond IP in insulators
**Derived statement [D, sketch].** For spin-flip (triplet) excitations the BSE kernel is the direct term only: H^T = (ε_c − ε_v)δ − W (no exchange 2v̄), while the
singlet has H^S = (ε_c − ε_v)δ − W + 2v̄. For a Wannier–Mott exciton the exchange matrix element is v̄ ∝ |φ(0)|²|ρ_cv|²v(G≠0) ≈ E_x^b(a/a_x)³ × O(1), with
a/a_x ≈ 0.11 in Si: so **the triplet ladder equals the singlet ladder up to O((a/a_x)³) ≈ 10⁻³ relative** (the singlet–triplet splitting in Si is sub-meV),
apart from the long-range part v(q) of the singlet exchange, which is the external screening (§5) and is absent from the triplet by construction. Hence the
interim "singlet Sommerfeld ×1.3–2 near the edge" for spin operators (IF-13) is justified at O((a/a_x)³), and the triplet bound lines sit at the singlet energies
within that accuracy. The adiabatic f_xc^T adds ≲ +10–20% (WP1-v3 §2.4, upper bound). **Exact remaining gap:** the triplet response with W and f_xc^T at keV q.
**Spec:** R̃_s = R⁰ + R⁰(4f_xc^T − W_ladder)R̃_s (normalisation of [E6]); inputs: the full IP matrix R⁰_{GG′} (LE-38 library) and the §5 BSE run with the exchange
switched off; output S_{s^zs^z}(q,ω) for 𝒪₄-type couplings; control: at W = 0, f_xc = 0 it reproduces ¼S^{IP}_nn ([E6]). Cost: marginal on top of §5.

## 12. LE-35: local-field screening of j_T, in-medium 𝒪₈; LIMITS L3
**Quantity [D, RPA+LFE].** With the Dyson equation R = R⁰ + R⁰v_C R on the joint index set {n(q+G)} ∪ {j_T(q)} (the current enters only as an external row),

  S_{ab}^{scr}(q,ω) = S_{ab}^{IP} + Σ_{G,G′} [R⁰_{a,G} v_C(q+G) (ε^{-1})_{GG′} R⁰_{G′,b}]_{anti-Hermitian part}·(−2),   a, b ∈ {n, j_T1, j_T2}.               (CW1.12)

For a = b = j_T the correction needs the mixed block R⁰_{j_T,n(q+G)}: at G = 0 it vanishes for q̂ on a 3- or 4-fold axis (transverse current orthogonal to a
longitudinal density in the cubic little group) and is otherwise O(LFE). This is the "screened through local fields" statement of WP1-v3 §2.3, now as a formula:
δ_LF^{jT} ≡ ΔS_{j_Tj_T}/S_{j_Tj_T}, sized 10–30% [E]. **L3 factor:** the recast factor for 2510.25835's 𝒪₈ is "≥ 12× with medium enhancement, IP 20–30" (WP1-v3
IF-14). Composing the IP range with δ_LF^{jT} ∈ [−0.3, +0.3] gives the stated interval **8–39** [E]; the factor is no longer "unresolved" in kind, only in value.
**Spec:** G10 library run (§15) with the mixed blocks output; evaluate (CW1.12) on the QCDark2-like grid; report δ_LF^{jT}(|q|,ω) and the 𝒪₂, 𝒪₅, 𝒪₈ recast ratios.
Pitfall: the transverse current needs the non-local commutator i[V_NL, r] (WP3 C1); omitting it biases j_T by ≈ 10% in Si.

## 13. LE-36: SOC near the edges (Si on-axis vertex, Ge mixing)
**Si [CALC] (QE noncollinear + lspinorb, Si_ONCV_PBE_FR-1.1, 40 Ry, a_exp; vertex_soc.py).** Δ_SO(Γ) = 48.6 meV (PBE; exp. 44 meV). With spinor states,
ρ = Σ_{G,σ}c*_{m,k+q}(G,σ)c_{n,k}(G,σ). Scalar-equivalent vertices (Kramers-pair sum / 2): on the axis (extremum and the 1.39 keV pair) **1.6×10⁻⁶ and 2.6×10⁻⁶**,
i.e. 0.3% in amplitude relative to the allowed (2̄00) size 0.15. WP1-v3's "≈ 4% amplitude" overestimates the on-axis lift by ≈ 10 (the lift needs conduction-band
SOC, which is small at Δ). At the true (mirror-plane) optimum the lift is **1.3×10⁻⁴** (4.5% amplitude relative to the allowed partner 0.064, which is only
0.39 eV away there). Effect on the window: the SOC piece of ϖ̄_II is ≤ 0.01 (§3.2). The LA-kink SOC admixture (WP3 §M3 table, "~2×10⁻³") concerns the PAER amplitude
(g × ρ structure), not ρ alone; transferring the computed state-mixing magnitude gives a relative weight ≲ 10⁻⁴ [E, informed by the CALC vertex]. **Ge [CLOSED-AS-EXACT-GAP].** WP1-v3's ≲ 10% mixing near the Ge edge stays [E]: PBE+SOC has the wrong band
order (COMP-PH IF-5), so the vertex at the L-valley optimum needs HSE+SOC wavefunctions. **Spec:** COMP-PAER tierH/Ge scf.in (SOC, 60 Ry) with an HSE06 nscf
(COMP-PH §6.2) at the (k_v, k_v + q) points from the §1.4 minimisation; vertex_soc.py unchanged (spinor Miller matching). Fork inputs for the Si run:
code/CW1/inputs/fork/Si-soc/. Pitfall: compare Kramers-pair sums, never single spinor bands (gauge). Cost: < 1 h CPU after the HSE SCF.

## 14. LE-37: plasmon → phonon branching (X+)
**Derived statement [D for the definition, E for the size].** A bulk plasmon in Si is a pole of 1/ε at ω_pl ≈ 16.6 eV embedded in the interband continuum; its decay
products are the final states of the improper response at (q, ω_pl). Splitting by phonon number (WP0 Theorem D sectors), the phonon-assisted branching is

  B_pl^{X+}(q) = L^{X+}(q, ω_pl)/L(q, ω_pl) = ε₂^{X+}(q, ω_pl)/ε₂(q, ω_pl)   (common |ε|² cancels),                                                                (CW1.14)

the PAER sideband fraction of the absorptive part at ω_pl, outside the window (DC convention). WP3's C3 estimate gives sideband/ZPL ≈ (⟨|g|⟩/ΔE)² ≈ 10⁻³–10⁻² where the
first-order channel is open, so **B_pl^{X+} ≈ 10⁻³–10⁻²** [E]. Relevance: halo DM does not produce bulk plasmons in Si (WP1-v3 §4.2: q ≥ ω_p/v_max = 6.3 keV > q_c), so
the branching enters only through plasmons made by other channels (Migdal, nuclear recoil). **Spec (optional):** tier-H stage 6 at ω = 15–18 eV, |q| ≤ 2 keV (DC
convention, edge-shell excluded); output B_pl^{X+}(q). Pitfall: at ω_pl the X0 continuum is O(1), so the fp/DC split (WP3 (M.10)) must use Γ_Λ₀ of the hot pairs.

## 15. LE-38: G10 IP response library (12 functions, R⁰_{GG′})
**Quantity [D, WP1-v3 §2.6].** Per (q,ω), for PT-symmetric Si/Ge: the screened singlet block on {n, j_T1, j_T2} (6 real functions: S_nn, S_{nj_T} (2), S_{j_Tj_T}
(3 symmetric)) and the IP singlet block (6), which fixes the IP triplet block (×¼). Plus the full IP matrix R⁰_{GG′}(q,ω) for the triplet ladder (§11) and the LFE
screening (§12, §19). Diagnostics (PT zeros): Im S_{nj_T}, the antisymmetric jj part < 10⁻³ of the real parts. **Spec.** What: the 12 functions on a (|q|, q̂, ω)
grid plus R⁰_{GG′}. τ: `X=IP ⊕ RPA+LFE`, `nB=0`. Method: QE PBE + scissor (40–60 Ry SG15, as here), vertices ρ_cv(k, q+G) by Miller matching (as vertex.py),
current vertex ⟨c|½{p, e^{iq·r}}|v⟩/m_e plus the non-local commutator correction; RPA+LFE Dyson on G ≤ 8αm_e. Grids (QCDark2-like): 10³ k (nosym, unfolded),
|q| ≤ 25αm_e in 0.1αm_e steps, 30 q̂ (C₄ᵥ wedge), ω ≤ 50 eV in 0.05 eV; 60 bands (f-sum ≥ 0.95 with the commutator term, CONTROLS C4, COMP-PAER IF-CP-4).
Convergence: k 8³ → 12³ change < 3% on S_nn at |q| = 1 keV; G-cutoff 6 → 8αm_e < 1%. Pitfall: the plane-wave f-sum with NC PPs reaches only 0.89 at 100 bands
without the non-local term (COMP-PAER C4). Output: versioned tables (HDF5) for WP6. Cost: ≈ 50–100 CPU-h (Si), ×4 with SOC (Ge).

## 16. LE-39: G11 electronic anisotropy S₄, S₆, S₈
**Statement [D, WP1-v3 §6.1].** Odd ℓ vanish identically (TR); in O_h and T_d the first anisotropic multipole is ℓ = 4. The quantities are S_ℓ(|q|,ω) =
∫dq̂ K^{cub}_ℓ(q̂)S(q,ω) for ℓ = 4, 6, 8. The ab initio E_min(q̂) anisotropy of §1.2 (14–107 meV between axis and {001} minima at 1.2–1.5 keV) shows the near-edge
S₄ is not small there. **Exact remaining gap:** the full-q RPA+LFE run. **Spec:** WP1-v3 §8 G11 (GPAW/QCDark2/BerkeleyGW, projection on K^{cub}_ℓ to ℓ = 8; diagnostics
|S_{1m}|, |S_{2m}|, |S_{3m}|/S₀₀ < 10⁻³), with the q̂ grid of §15 (Lebedev 110 points suffice to ℓ = 8 exactly). Cost: the §15 run (shared).

## 17. LE-40: X2-N1, the 1D two-band contact-kernel benchmark
**Quantity [D].** In 1D with two bands, a contact kernel v(K) = v₀ for |K| < K_c, a classical phonon field u(t) = u₀cos(ω_Q t) at wavevector Q, and the DM probe
φ e^{i(qx − ωt)}, compute the second-order induced density at (P = q + Q, ω_f = ω − ω_Q) two ways: (a) **frequency domain**, |M̃|²/|M|² from X2 (2.2) with
ε̃⁻¹(q,ω), W(P,ω_f) and the KS triangle T (2.1); (b) **real time**, TDH propagation of the density matrix with both perturbations, extracting the Fourier
component at (P, ω_f) of δn(t) and dividing by φu₀. Exact benchmarks: (i) rigid coupling g = −u∂_xV: Λ = O(ω_Q/ω) (X2 frame theorem); (ii) coherent-potential
coupling (M_f′ = Uρ_f′ for all f′): M̃ = M/ε(P,ω_f) exactly (CW1-C31); (iii) generic intracell coupling: Λ = O(1 − 1/ε(P)). **Spec:** N_k = 2000–8000 k points,
two cosine bands (gap 1, width 2), K_c = 0.5 BZ, v₀ scanned so that ε(P) = 1.5–4; real-time RK4, Δt = 0.01/E_g, T_total ≥ 200/E_g, adiabatic switch-on;
convergence: |M̃|² stable to 10⁻³ under N_k ×2 and Δt/2. Output: Λ(P) for the three couplings; pass criterion: (a) and (b) agree to 10⁻³. Cost: minutes (Python,
numpy). Pitfall: on-shell residues cannot be compared in a finite ring (X2 §9); use the continuum (large N_k) and a small damping η → 0 extrapolation.

## 18. LE-41: X2-N2/N3, Route S in Si (δ_LF, δ_pair at q = 0 and 0.5/1/2 keV)
**Quantity [D, X2 §8].** L(q,ω) = ⟨Im[−ε̃⁻¹_sc]_{q,q}⟩_ZG unfolded, with RPA local fields in the supercell G-basis, minus the same run with independent particles plus a
scalar 1/ε(q,ω): the difference gives δ_LF + δ_pair at that q; a third run with the supercell LFE restricted to the primitive G-set gives δ_LF alone. **Spec.**
Supercells: conventional cubic n × n × n with n = 3 (216 atoms; q-mesh spacing 0.39 Å⁻¹, reaching 0, 0.77, 1.16 keV) and n = 4 (512 atoms; spacing 0.29 Å⁻¹:
0, 0.57, 1.15, 1.72 keV); ZG displacements from the 8³ DFPT force constants (COMP-PH), two antithetic configurations, T = 0. τ: `nB=0|ng=2|X=RPA+LFE(sc)` (ZG is the
adiabatic quadrature, WP3 (W.11); the ω_Q correction (W.12) is applied afterwards). Method: QE PBE + scissor → yambo RPA+LFE (or turbo_eels Liouville–Lanczos,
which scales better), G cutoff 3 Ry for LFE, bands to E_F + 30 eV. Convergence: δ_LF + δ_pair stable to 5% under n = 3 → 4 at q = 1.15 keV; k-sampling Γ-only vs 2³
in the supercell. Output: Λ(q) at the listed q, the test Λ(q) ≈ Λ(0) [C → D or refuted]. Cost [E]: n = 3 ≈ 2×10³ CPU-h, n = 4 ≈ 2×10⁴ CPU-h (GPU fork: hours to
a day). The envelope [0.4, 1.8] on L^{PA} stays until the run.

## 19. LE-42: X2-N4, ε̃⁻¹_{G0}(q,ω) in the window → δ_LF
**Quantity [D].** From X2 (2.2), the external local-field correction alone is

  1 + δ_LF(q,ω) = ⟨⟨|M^{(2)}[ρ̃]|²⟩⟩/⟨⟨|M^{(2)}[ρ/ε_M]|²⟩⟩,   ρ̃ = Σ_G (ε̃⁻¹)_{G0}(q,ω)ρ(q+G),   ε_M = 1/(ε̃⁻¹)₀₀.                                                    (CW1.19)

A model-independent lower-level proxy, needing no amplitude: 1 + δ_LF^{(0)} = Σ_cv|Σ_G(ε̃⁻¹)_{G0}ρ_cv(q+G)|²/Σ_cv|ρ_cv(q)/ε_M|² on the ZPL vertices at the same
(q,ω). **Spec:** primitive cell, RPA+LFE ε̃_{GG′}(q,ω) for q on the §15 grid in the window (ω = 1.2–1.6 eV), 40 bands, G cutoff 4 Ry (≈ 60 G), 12³ k; turbo_eels
(Lanczos, both head and wings) or yambo; output (ε̃⁻¹)_{G0} and δ_LF^{(0)}(q,ω). Convergence: G cutoff 3 → 5 Ry < 1%. Cost: ≈ 10 CPU-h; fits the box (optional run).

## 20. LE-43: δρ^V (virtual-phonon vertex) and the per-diagram f-sum compensation
**Item.** WP3-v3 §M5 (4): the unrestricted one-electron band sum for the O(g²) vertex correction to the zero-phonon vertex is unproven [C]; per-diagram compensation [C].
**Kubo (Matsubara) form [D; independent particles + linear e–ph coupling, harmonic phonons, one phonon line].** The vertex rung has one phonon line D(iν) =
2ω_Q/((iν)² − ω_Q²) and two internal fermion lines m (between the c-leg phonon vertex and ρ) and m′ (between ρ and the v-leg phonon vertex):

  δρ^V_cv(k,q) = (1/N)Σ_{Qν}Σ_{m,m′} g_{cm}(k+q,−Q) ρ_{mm′}(k−Q,q) g_{m′v}(k,−Q) F_{mm′},   F_{mm′} = T Σ_{iν} D(iν) G_m(z_c − iν) G_m′(z_v − iν).

With 1/(ab) = (1/a − 1/b)/(b − a) and the one-line sum T Σ D G(z − iν) = (n_Q + 1 − f)/(z − ε − ω_Q) + (n_Q + f)/(z − ε + ω_Q) (the Fan form, WP3 §5 AHC Eq. (157)),

  F_{mm′} = {(n+1−f_m)/(a−ω_Q) + (n+f_m)/(a+ω_Q) − (n+1−f_m′)/(b−ω_Q) − (n+f_m′)/(b+ω_Q)}/(b − a),   a = z_c − ε_m, b = z_v − ε_m′,                              (CW1.20)

continued to the on-shell external energies z_c = ε_c, z_v = ε_v. At T = 0 with f_m = f_m′ = 0 this is exactly the one-electron Rayleigh–Schrödinger form
1/((a − ω_Q)(b − ω_Q)) with unrestricted m, m′. The difference is

  ΔF_{mm′} = {f_m[1/(a+ω_Q) − 1/(a−ω_Q)] − f_m′[1/(b+ω_Q) − 1/(b−ω_Q)]}/(b − a)   (T = 0):

it vanishes as ω_Q → 0 at fixed non-zero a, b, but **not** when an occupied intermediate state is near the hole leg (m′ in the valence band at k − Q, |b| =
|ε_v − ε_m′| ~ ω_Q), the "phonon absorbed by another sea electron" ordering of REF-A/REF-B. So the f-free one-electron sum is **not** an identity: it holds to O(ω_Q/|b|),
which is O(1) for intraband-like intermediates. **Closure:** (CW1.20) is the definition to compute (well defined, gauge-covariant with the shared U(k) of CONVENTIONS
§4); the "unrestricted band sum" claim of §M5 (4) is withdrawn and replaced by (CW1.20). **Aggregate statement kept [D]:** 𝓜₁(SE-p + SE-h + V) = −𝓜₁^{SB} (WP3
(M.11)) holds for the sum; the per-diagram split stays [C]. **Spec (validation):** D2-N1 1D ring exact diagonalisation (two bands, 8–12 sites, one SSH phonon mode,
Lanczos): extract the zero-phonon weight at O(λ²) by fitting λ = 10⁻³–10⁻²; pass: ED = (CW1.20) to 10⁻⁶ relative; the f-free form must fail by ΔF. Cost: minutes.

## 21. LE-44: the ALDA k_xc pair term (§M7)
**Derived statement.** With LDA exchange e_x = −C_x n^{4/3}: f_x = −(4/9)C_x n^{−2/3}, **k_xc = (8/27)C_x n^{−5/3} = −(2/3)f_x/n** [D] (CW1-C27). The extra source
in (M.13) is Σ_Gρ_cv(P+G)(ε̃⁻¹k_xc[δn_qδn_Q])_G, and the pair term is Σρ W T with W = ε̃⁻¹(v_C + f_xc). Their ratio at the pinned P (|P| ≈ 1 Å⁻¹):
|term_kxc/term_pair| ≈ (2/3)|f_x(P)/v_C(P)|·|δn_qδn_Q/(n δn^{(2)})|. The first factor is (P/2k_F)² ≈ 0.08 (CW1-C28; X2 §3). The second is O(1) in the HEG (the
quadratic response χ^{(2)} ~ χ²/n). So the ALDA term is **≲ 5% of the pair term, ≲ 2.5% of L^{PA}** given |δ_pair| ≤ 0.5 [E]. It is inside the [0.4, 1.8] envelope and
no separate nuisance is needed. **Spec (optional):** Route S (§18) run twice, RPA and ALDA kernels; the difference minus the f_xc-in-W part is the k_xc term.

## 22. LE-45: L9b(c), ALP vertex and SOC
WP1-v3 §2.5 [D] confirms WP3's L9b(c): the ALP NLO vertex is 2tr J_e = Σ½{σ·p/m_e, e^{ik·r}}; at SOC = 0, unpolarised, Σ_{ss′}|⟨s′|σ·p|s⟩|² = 2|p|² (checked
symbolically, CW1-C22), so the spin-summed PA amplitude equals the velocity form and 1608.01994 Eq. (10) holds for X+ with the proper σ₁^{PA}. It is triplet-channel
(no Hartree local fields, no e–h exchange); the singlet–triplet difference is O((a/a_x)³) by §11 plus the LFE of the singlet (≲ 10% in Si [E]). With SOC the
identity fails at O(Δ_SO/ΔE); the computed Si scale is ≲ 10⁻⁴ in weight near the edge (§13). CLOSED.

## 23. LE-46: temperature transfer of data-driven σ₁ (77/300 K → mK)
**Formula [D, WP3-v3 §4(b), made invertible].** With T-independent branch spectra 𝒜_ν and the gap shift ΔE_g(T) = E_g(T) − E_g(0) < 0:

  σ₁^{X+}(ω;T) = Σ_ν[(n_ν(T) + 1)𝒜_ν(ω − ω_ν − ΔE_g(T)) + n_ν(T)𝒜_ν(ω + ω_ν − ΔE_g(T))],                                                                      (CW1.23)

linear in {𝒜_ν}. Given data at T_d, n_ν(T_d) and ΔE_g(T_d), the 𝒜_ν follow by a linear (triangular) solve on the ω grid; then σ₁(ω; mK) = Σ_ν𝒜_ν(ω − ω_ν). The inverse
is exact for branch-resolved data (CW1-C24 recovers the mK spectrum to 10⁻⁴). For Si at 77 K: n_TA = 0.065, ΔE_g ≈ −4 meV (Varshni [E]). **Size of the
uncorrected error** (TA-branch p_on = 2 synthetic edge, an upper bound because the dominant TO branch has n_TO(77 K) ≈ 2×10⁻⁴): ×2.6, ×1.9, ×1.46, ×1.28 at 15, 25, 50,
100 meV above E_g + ω_TA. On the TO-dominated part of the edge only the gap shift acts, (1 + |ΔE_g|/x)² for p_on = 2: ×1.17 at x = 50 meV, ×1.08 at 100 meV. So "O(1) within ≈ 20–25 meV" of WP3 IF-14 is the region where the factor exceeds 2; a +30–50% residual persists to 50–100 meV. Branch
weights: TA and TO replicas are resolved in the 20 K Macfarlane data (COMP-PAER §1); use those, or COMP-PAER's ε₂^{PA}(T) once tier H runs. **Spec:** digitised
branch-resolved spectra (TA, TO; LO, LA where resolved) at T_d; Varshni ΔE_g(T) [lit.]; solve (CW1.23); propagate the digitisation error (±25%). Cost: none.

## 24. LE-47: CONTROLS C8, the GaAs decoy window
**Derived statement [D for the conditions, E for the numbers].** In a direct-gap crystal the zero-phonon pair at small q needs E_dir + q²/2M_x ≤ qv − q²/2m_χ; with
M_x = m_e* + m_hh = 0.58 m_e the left side always wins: max_q(qv_max − q²/2M_x) = M_xv_max²/2 = 1.04 eV < E_dir = 1.519 eV, so **the Γ-valley ZPL is unreachable at
small q for any m_χ** (as for Ge Γ, WP1 §R1). PAER reaches the Γ pair with the phonon absorbing q (P ≈ 0): m_χ^{PA} ≈ 2(E_dir + ω_TA)/v_max² = **0.435 MeV**. The
first ZPLs come from the L valley (E_L = 1.71 eV, |K_L| = 0.96 Å⁻¹; parabolic M_L = 2.41 m_e [UNVERIFIED masses]): **0.511 MeV**; X valley 0.599; vertical Umklapp at
|G₁₁₁| = 3.8 keV: 0.800 MeV (CW1-C29). So the PAER-leading GaAs band is **≈ 0.43–0.51 MeV** [E], narrower than SOTA's "0.4–0.9"; the Si lesson (§1.2) says the true L
edge is lower still (heavy-hole warping), so 0.51 is an upper bound on the band's top. C8's requirement ("PAER a small correction above E_dir") holds pointwise
wherever a ZPL is open (C3). **Exact remaining gap:** the band-structure check. **Spec:** COMP-PH formulated/GaAs (140 Ry SG15 Ga with 3d, a_exp; PBE is nearly
metallic → HSE06 or a k-dependent scissor fitted to Γ/L/X = 1.52/1.71/1.98 eV, with SOC for the hole), Wannier sp³ 8 WFs (16 spinor), then emin_fast.py per class
(Γ, L, X, Umklapp copies) and the PAER edge from E_dir + min_ν ω_ν(Q = −q) with 4³→6³ DFPT phonons (lpolar, Fröhlich). τ: `nB=0|ng=1,2|X=QP bands` (threshold only).
Cost: ≈ 10–20 h CPU (HSE) or 2 h (scissor). Output: C8 window [CALC].

## 25. LE-178: non-adiabatic AHC (zero-point renormalisation beyond adiabatic)
**Formula [D].** The Fan self-energy at the band energy (non-adiabatic, NA) minus its adiabatic form (ω_Q dropped from the denominators) is, per state n at T = 0,

  ΔZPR_n ≡ ZPR_n^{NA} − ZPR_n^{ad} = (1/N)Σ_{Qνm}|g_{mnν}(k,Q)|²[1/(ε_n − ε_m − s_mω_Q) − 1/(ε_n − ε_m)],   s_m = +1 (m empty), −1 (m occupied).                        (CW1.25)

Interband terms are O(ω_Q/|ε_n − ε_m|) relative. The intraband optical term (m = n, deformation potential D₀, parabolic mass m*) is singular in the adiabatic limit:
Ω|g₀|²∫d³Q/(2π)³[2m*/Q² − 1/(Q²/2m* + ω₀)] contributes ΔZPR = Ω|g₀|²(2m*)^{3/2}√ω₀/(4π), a √ω₀ non-analyticity (CW1-C30). For Si the Δ₁ conduction minimum has
no intravalley optical deformation potential (symmetry) and the valence D₀ ≈ 5 eV/Å [E, memory] gives |g₀| ≈ D₀ℓ₀ ≈ 0.12 eV and **ΔZPR ≈ 0.2 meV**; acoustic
intraband terms change by O(m*c/Q_typ) → negligible; no Fröhlich term (non-polar). **Literature [FT]:** Miglio et al. 2011.12765, Table S5: non-adiabatic AHC
ZPR_g = −56 meV (Si), −33 meV (Ge); main text: the adiabatic-supercell approach describes "more covalent materials (C, Si, Ge, AlSb, AlAs)" well, the large
non-adiabatic effects being in infrared-active (polar) materials. So in Si the non-adiabatic correction is ≲ 1 meV (≲ 2% of ZPR_g) [E]. **Window impact:** the
campaign uses the measured E_g(0) (which contains the full ZPR) and a rigid scissor; the residual is the k-dependence of the ZPR over the reached pair states
(≤ 0.2 eV above the edges), bounded by ≲ 10 meV [E], i.e. ≤ 0.002 MeV on m_χ^{ZP} (dm/dE = 0.19 MeV/eV at the optimum). CLOSED.

## 26. LE-179: X1 residual tags
(i) **Symmetric D^n [D].** A rigid rotation of crystal and electron by the antisymmetric ω changes the band energy at the lab-frame label k by
δε = ∇ε·(ωk) = v_n·(ωk) (CW1-C25), so the antisymmetric part of the lab-frame slope Ξ^n is a velocity term, already contained in v_n ⊗ P_n of (X2). The comoving
D^n couples to strain only and is symmetric. At band extrema (v_n = 0), the only place (X1) is used in the window, the antisymmetric part vanishes identically.
Tag [C] → [D]. (ii) **Magnitudes [E, with CALC c].** With Ξ_u ≈ 8.6 eV (Si conduction, [UNVERIFIED]) and c_LA = 8.18 km/s [CALC, COMP-PH], D/c ≈ 300 keV ≫ q ≤ 2 keV
(CW1-C26): the deformation terms dominate the soft limit by two orders, as X1 stated. **Spec** for [CALC] D^n: frozen strain ±0.5% (six components) on the
2-atom cell with internal relaxation (Kleinman ζ), band energies at k_c and Γ referenced to the average electrostatic potential plus a slab line-up for absolute
values (only D^c − D^v enters (X1) at extrema, so the line-up is needed only for single-band checks); C7b control. Fork: a 2-atom scf/nscf as inputs/fork/Si-vertex
with celldm and positions strained. Cost: minutes. (iii) **Piezo log [D].** Si and Ge are centrosymmetric: no piezo coupling. In GaAs the BN log of X1 §9 arises
only where the ZPL is open; inside the PAER window the soft region is kinematically empty (X1 result 2). Relevance is therefore limited to the inclusive ZPL
line shape near E_dir in the C8 decoy (§24), which is not a PAER quantity. Tag [C] → [D] for "irrelevant inside the window".

---
## Symbols introduced/used
| symbol | meaning | status |
|---|---|---|
| ϑ_ZP | tilt of q̂ from the valley axis at the [E13] optimum (Si: 0.181 rad, {001} plane) | **new** |
| β^{ZP}_θ, β^{ZP}_z | in-plane / out-of-plane angular curvatures of E^{ZP}_min at the optimum (eV/rad²) | **new** |
| ϖ̄_II | angle-averaged forbidden-class ZPL/PAER ratio at fixed \|q\| (CW1.4) | **new** (ϖ_II = WP1 pointwise) |
| ε_ex^{max}(m_χ) | largest reachable excess energy above E_min at the optimum \|q\| | **new** |
| δ_LF^{jT}, δ_LF^{(0)} | LFE correction of the transverse current (CW1.12); vertex-level proxy of δ_LF (CW1.19) | **new** |
| ΔZPR_n | non-adiabatic minus adiabatic Fan ZPR (CW1.25) | **new** |
| B_pl^{X+} | plasmon phonon-assisted branching (CW1.14) | **new** |
| m_χ^{ZP}, m_χ^{PA}, E^{ZP}(q), E_min(q), K_pk, Q*, Q_w, M_x, μ_x, a_x, E_x^b, ζ_S, 𝒮_F, ρ_mn(k,q), 𝔉_ρ, f_win, ε₂^{PA,opt}, Δ_SO, S_HR, ℓ_Q, g, Ξ^n, D^n, ω_ν, ε_∞, L, S, R⁰, W^{scr}, 𝔗, Λ | as NOTATION v4, WP1-v3, WP3-v3, X1, X2, COMP-PAER, COMP-PH | used |
Notes: m_ZPL (COMP-PH) ≡ m_χ^{ZP} (WP1, NOTATION) for the continuum; this return uses m_χ^{ZP}. The Dresselhaus inverse masses are written L, M, N only in §1.3/§6
as named constants (not symbols; L, M, N keep their NOTATION meanings elsewhere).

## Interface flags
- **IF-CW1-1 (WP3 §M9, WP1 IF-6/6b, WP6 (3.1′)/IF6-10, M1/SOTA, paper):** Si window statements change (owed text OC-1…OC-4): PAER-only to 0.397–0.402 (1s) /
  0.400–0.405 (continuum) MeV; PAER-leading to ≈ 0.42–0.44; two-channel ≈ 0.44–0.51; allowed-size ZPL opens at ≈ 0.50 MeV (comparable) and leads from ≈ 0.51 MeV.
- **IF-CW1-2 (COMP-PH Ge, §6.2 owner):** Ge thresholds must use the joint (q,k) minimisation (CW1.1) (scripts/emin_fast.py) and check the σ_d mirror rule at the
  optimum; the parabolic 0.32–0.36 MeV is not a reliable bracket.
- **IF-CW1-3 (WP8-F G-F5, COMP-PH §4 window FOM):** E^{ZPL}_min(q* = 0.90 keV) minimised over q̂ and k is **1.697 eV** at ϑ = 0.34 rad (emin_qstar.json; Wannier,
  a_PBE), not 1.715 (five directions); recompute Δm/m (WP8-F §2.7(b)).
- **IF-CW1-4 (COMP-PAER tier H owner):** stage 6 output grid must include the {001} mirror-plane cones (§3.3) and the X-face (2̄00) edge; ZPL vertices with the
  hole at k_v(q).
- **IF-CW1-5 (WP6 nuisances, IF-3 of WP1):** Si second-class bound-line amplitudes use the mirror-plane vertex (|∂_{q_z}ρ| = 1.38 Å, |∂_{k_z}ρ| = 0.31 Å) and the
  SOC-lifted 1.3×10⁻⁴; the on-axis (n_H² − 1)/(3πa_x⁵n_H⁵) form is the on-axis special case.
- **IF-CW1-6 (CW8 bookkeeping):** LE-24…47, 178, 179 statuses per §0; G2, G5, G7, G10, G11 and Cat. §12.1–12.3, §12.7 rows of LOOSE-ENDS §1b lose their CW1 pending.

## Owed corrections (target → exact replacement text; not applied here)
- **OC-1 LIMITS L8 (Note/action, ✎R16 clause)** → "✎R16/CW1: Si window [CALC]: PAER-only 0.333 (replica) / 0.3374 (continuum) – 0.397–0.402 (1s) / 0.400–0.405
  (continuum ZPL) MeV, the first ZPL off the valley axis in a {001} mirror plane and second class by the mirror (CW1 §1–§2); PAER leads to ≈ 0.42–0.44 MeV,
  two-channel ≈ 0.44–0.51, allowed-size ZPL ((2̄00) class, X face) opens at ≈ 0.50 MeV and leads from ≈ 0.51 MeV [E, vertex CALC]; 0.547 MeV is the nearest-pocket (2̄00) value; rate/reach [E] only (L8-N2)".
- **OC-2 WP1-v3 §3.4 "Summary for WP3/WP6" and IF-6 v3 cell** → "Si zero-phonon line opens at 0.400–0.405 MeV (continuum; 1s 0.397–0.402) [CALC, CW1 §1], off
  the valley axis (ϑ_ZP = 0.18 rad, {001} plane, hole off Γ), second class by the σ_z mirror; an allowed-size zero-phonon channel ((2̄00) class, X face, |ρ|² ≈
  0.01–0.04) opens at ≈ 0.50 MeV and leads from ≈ 0.51 MeV; the (2̄00) vertex is not small (Σ_v|ρ|² = 0.150 at its extremum, light hole) [CALC, CW1 §2]; Ge: formulated (CW1 §1.4)."
  Delete "it leads only if |ρ_cv^{(2̄00)}| ≳ η_PA^{1/2}|ρ_cv^{ref}| [E, open …], otherwise the reliably allowed class starts at ≈ 0.62 MeV ((1̄11))" in §3.4, §3.7, IF-6
  and R9 N1.
- **OC-3 WP1-v3 §3.7 table [E14] and IF-6b** → replace the ϖ_II table by "ϖ̄_II (angle-averaged, CW1 (CW1.4)) = 0.016 / 0.13 / 0.35 at ε_ex = E_x^b / 50 / 100 meV;
  pointwise at the optimum 0.01–0.04 (k_rel) + 0.03–0.10 (SOC) [vertex CALC, PAER E ×/÷10]" and the interim sentence by "PAER leads the integrated electronic rate
  to ≈ 0.42–0.44 MeV; two-channel ≈ 0.44–0.51; allowed-size ZPL opens at ≈ 0.50 and leads from ≈ 0.51 MeV (CW1 §3.3)".
- **OC-4 WP3-v3 §M9 window bullets (1)–(3) and IF-8 v3 cell** → (1) "m_χ^{PA} ≲ m_χ < 0.400–0.405 MeV [CALC]"; (2) "0.40–0.51 MeV: PAER coexisting with the
  forbidden-class (mirror) ZPL, PAER leading to ≈ 0.42–0.44, ϖ̄_II per CW1 §3.2; the allowed-size ZPL opens at ≈ 0.50, comparable"; (3) "above ≈ 0.51 MeV the
  allowed-size ZPL ((2̄00) class) leads; PAER/ZPL ≲ 0.1 pointwise there, 10⁻²–10⁻⁵ on the axis".
- **OC-5 WP3-v3 §M3(c)** → "Si (M_x = m_l + m_hh[100] = 1.19 m_e [CALC, CW1 §1.3]; 1.41 m_e used a DOS heavy-hole mass and is withdrawn): Q_w = 0.31 Å⁻¹ at δ₀ = 0.3 eV".
- **OC-6 WP3-v3 §M3(e), §R1 and the p̄_on table** → "crossover |q| ≈ 1.35 keV [CALC, COMP-PH §4]; the window low-mass end is on axis"; table row "(2̄00) class: LO
  minimum off axis [CALC, CW1 §4] → p̄_on = 3 (TA, TO, LA, LO)"; LA kink: "SOC admixture ≲ 10⁻⁴ relative weight [E, from the CALC SOC vertex lift, CW1 §13]" (replaces "~2×10⁻³ [E]").
- **OC-7 WP1-v3 §3.2(c) last bullet and §10 item 6** → "SOC lifts the Si on-axis zero to |ρ|² ≈ 2×10⁻⁶ (0.3% amplitude) and the mirror-plane zero to 1.3×10⁻⁴
  [CALC, CW1 §13]; Ge ≲ 10% [E] (formulated)".
- **OC-8 COMP-PH §0 row "ZPL kinematic edge" and §4 "m_ZPL = 0.4154 MeV"** → "0.4154 MeV is the on-axis local optimum; the joint (q,k) minimum is 0.400–0.405 MeV
  off axis (CW1 §1.2)"; and "the allowed/forbidden split … not computed here" → "computed in CW1 §2".
- **OC-9 COMP-PAER §0 item 1, §4 table, IF-CP-1** → "first zero-phonon final state 0.400–0.405 MeV (continuum) [CALC, CW1]" (was 0.405–0.408); "allowed class (2̄00):
  0.547 MeV (nearest-pocket assignment); the allowed-size channel opens at ≈ 0.50 MeV on the X face (CW1 §2.3)".
- **OC-10 LIMITS L9b note** → "1608.01994: uncorrected 77 K data overestimate the mK rate by > ×2 within ≈ 20 meV of E_g + ω_TA and by 30–50% at 50–100 meV
  (TA-branch bound); correct by the inverse transfer (CW1 (CW1.23))".
- **OC-11 LIMITS L3 note** → "𝒪₈ recast factor ≥ 12× (IP 20–30); with δ_LF^{jT} ∈ [−0.3, 0.3] the stated interval is 8–39 [E] (CW1 §12); 𝒪₂, 𝒪₅ also; 2 independent
  Catena responses in Si/Ge".
- **OC-12 SOTA "Amendments owed" C8 and CONTROLS C8 bracket** → "PAER-leading GaAs only at m_χ ≈ 0.43–0.51 MeV [E, parabolic; CW1 §24], full q integral; band-structure check formulated".

## Proposed LIMITS rows (return-local labels, CONVENTIONS §13 row 30)
| # | Owner | location | chain | status | note |
|---|---|---|---|---|---|
| CW1-L1 | CW1 | §1, (CW1.1) | [E13] as a joint (q,k) minimum on Wannier/DFT bands | CALC (Wannier TB committed as gz; DFT check at the optimum, CW1-C6; COMP-PH anchor) | Si m_χ^{ZP} 0.400–0.405 (1s 0.397–0.402) MeV; off axis, {001} plane |
| CW1-L2 | CW1 | §2.2 | σ_z mirror selection (O_h∖T_d, glide phase) | D, CALC-checked | G′ = 0 top-hole vertex zero in {001} planes; (2̄00) allowed |
| CW1-L3 | CW1 | §2.3 | (CW1.1) restricted to the (2̄00) class | CALC (edge); E (leading) | allowed-size ZPL opens ≈ 0.50, leads from ≈ 0.51 MeV; IF-6 hedge removed |
| CW1-L4 | CW1 | §3, (CW1.3)–(CW1.4) | [E8] ZPL vs COMP-PAER (P.1) in ε₂ units | E (vertex CALC, PAER ×/÷10) | ϖ̄_II table; PAER leads to ≈ 0.42–0.44 MeV |
| CW1-L5 | CW1 | §5, (CW1.5) | TDA vs coupling in the screened L | D (head), size E | TDA overstates L ≈ ×2 at 0.7 Å⁻¹ |
| CW1-L6 | CW1 | §13 | noncollinear QE vertex | CALC | Si SOC lift 2×10⁻⁶ (axis), 1.3×10⁻⁴ (mirror optimum) |
| CW1-L7 | CW1 | §23, (CW1.23) | WP3 §4(b) inverted | D | 77 K → mK transfer exact for branch-resolved data |
| CW1-L8 | CW1 | §24 | C8 parabolic scan | E | GaAs PAER-leading 0.43–0.51 MeV |
| CW1-L9 | CW1 | §25, (CW1.25) | AHC Fan, NA − adiabatic | D; size E; Si ZPR [FT 2011.12765] | Si ΔZPR ≲ 1 meV; window ≤ 0.002 MeV |
