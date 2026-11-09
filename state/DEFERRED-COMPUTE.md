# DEFERRED-COMPUTE: the authoritative work list of deferred computations (R17, 2026-11-01)

**Note (2026-11-02, App. E.14–E.27 revision).** Rows aligned with the revised book text: DC-1/5/6 window values (PAER-only window to the first zero-phonon edge 0.407 MeV; allowed-size (2̄00) edge ≈ 0.50 MeV distinguished; 0.547/0.62 withdrawn); DC-1 flop count ≈ 10¹⁶ (App. E.5) and total cost; DC-11, DC-12, DC-14 costs as in App. E.15/E.16; DC-22 G count ≈ 725 (Si) / 821 (Ge, GaAs). Shared lattice setting for every item: PBE, SG15, 60 Ry, measured a (Si 5.431, Ge 5.658, GaAs 5.653 Å); one Si DFPT run (12³ k, 8³ q) ≈ 100 core-h (App. E.17).

Brief: /home/user/dmdd-solid/briefs/R17/DEFERRED-COMPUTE.md. User directive (2026-11-01): "derive and specify now, compute later". This ledger lists every computation the campaign
specified but did not run, deduplicated, with absolute paths, so that an agent new to the campaign can run each item from its own section. Nothing here was run.

**How to use it.** Each DC-n section names (i) the physics, (ii) the exact quantity and units, (iii) the method and approximation level, (iv) the convergence
parameters and the acceptance test (the CONTROLS.md case where one applies; otherwise the pre-registered test of the source spec), (v) the pitfalls, (vi) where the
result goes back. The source spec named in the summary table is authoritative where this ledger abbreviates it; always read it before running.

**Environment rules that apply to every item** (/home/user/dmdd-solid/code/ENV.md): over-limit jobs (> 3 h wall or > 12 GB on the 4-core box) target the campaign fork
github.com/ytcs/qe-rtsc (branch rtsc, GPU) with inputs in the rtsc/bench layout (`@PSEUDO@`, SG15 ONCV PBE v1.2 via rtsc/pseudo.sh, stages of rtsc/bench/run-fork.sh); in the box,
every heavy job goes through /home/user/dmdd-solid/code/run-heavy.sh; work directories under /root/work/<ID>/ only; results tagged [CALC] only with inputs, pseudopotentials, the
convergence record and the passed control committed under /home/user/dmdd-solid/code/<ID>/. CMPMC numbers: /home/user/cmpmc main ≥ 3d43a02, only modules marked PASS in
/home/user/dmdd-solid/returns/R15/CMPMC-AUD.md §4, patched paths only, presets quoted with file:line.

**Cost conventions.** core-h = CPU core-hours (the sources' "CPU-h", "CPU·h" and "core-h" are read as core-hours; "h on the 4-core box" × 4). GPU-h as quoted. node-h converted at
32 cores/node where a source gives node-h. Every cost is the source's [E] unless marked **[E-DC]**, which means the source gives none and this ledger supplies an order-of-
magnitude estimate (basis stated). Ranges are lo–hi.

**Priorities.** P1 = narrative-critical (a number the book's framing depends on, or a correctness gate for numbers already quoted); P2 = completes a channel, a ranking row or a
quoted limit; P3 = refinement, scope statement or an exact-gap remainder.

## 0. Sources swept
- /home/user/dmdd-solid/state/LOOSE-ENDS.md: every compute-formulate and compute-in-box row (LE-16, 17, 24–27 in-box; all compute-formulate rows) and every CLOSED-AS-EXACT-GAP row whose missing step is a computation; crosswalk in §6.
- Specs in the returns: WP0–WP6 v3 (/home/user/dmdd-solid/returns/R8/), WP5-v4 (/home/user/dmdd-solid/returns/R13/WP5-v4.md §2, §3.4, §9), WP7-{B1,B2,D,T}-v2 and WP7-E-v3 (/home/user/dmdd-solid/returns/R12/), GAP-EF-v2 §4.3, §5 + errata R-13 (/home/user/dmdd-solid/returns/R16/), COMP-PAER §8–§9 and /home/user/dmdd-solid/code/COMP-PAER/tierH/, COMP-PH §6 and /home/user/dmdd-solid/code/COMP-PH/formulated/, CW2–CW7 + errata (/home/user/dmdd-solid/returns/R16/) with /home/user/dmdd-solid/code/CW2/inputs/, /home/user/dmdd-solid/code/CW3/fork/, /home/user/dmdd-solid/code/CW5/LE-128/, /home/user/dmdd-solid/code/CW5/LE-137/; WP8-R-v2 / CW6 CMPMC run specs; WP8-F-v3 G-F2, G-F5, G-F6; WP5-AUD §3.1, §4 (B-1, B-2); WP8-S-v2 §6; /home/user/dmdd-solid/returns/R17/WP8-errata.md §4, §14–§15; X2 §10; WP3-v3 §M10, §8; WP1-v3 §8, §10.
- Owed data: /home/user/dmdd-solid/returns/R16/WP8-U-table-v4.csv (778 GAP rows; the DFT/DFPT-fillable properties are DC items, the rest are listed in §7), /home/user/dmdd-solid/state/DATA-ADDENDA.csv (supersedes Al, Ir C_ij and YIG a).
- Infrastructure: https://github.com/ytcs/qe-rtsc/issues/1 (read 2026-11-01: OPEN, no comments), /home/user/cmpmc/DESIGN_NOTES.md and VALIDATION.md, CMPMC-DEV §6, CMPMC-AUD §6; Kaplan-buffer bug (CMPMC-DEV f61d710, IF-DEV-5).
- **CW1 returned after this ledger was compiled (returns/R16/CW1.md + CW1-errata.md): DC-5 and DC-6 are done at [E] level and DC-7's LE-27 part is done; the remaining tier-H parts stay deferred** (LE-24…47, 178, 179 are OPEN-pending): its compute rows are taken here from their primary specs (WP1-v3 §8, WP3-v3 §M10/§8, X2 §10, X1 §10). The CW1 derivation/spec closure itself is still owed; this ledger does not replace it.
- **COMP-PH Ge is incomplete**: /home/user/dmdd-solid/returns/R15/COMP-PH.md carries unfilled placeholders (GE_TABLE, GE_WIN, GE_INS, GE_WTA, GE_MPAER, GE_AXIS, GE_CTRL, GE_QCONV, GE_K, GE_T, GE_LIMITS); LE-16 is OPEN. Treated as DC-4.

## 1. Summary table

| ID | quantity | material(s) | why it matters (book section / narrative) | code | spec location | inputs ready? | depends on | cost estimate (source) | priority |
|---|---|---|---|---|---|---|---|---|---|
| DC-1 | Si PAER loss function L^PA(q,ω) from the full (M.1) amplitude, then rate dℛ/dω and reach σ̄_e^95 (tier H, T6) | Si | Ch 13 headline (M1 tier H): replaces the [E, ×/÷10] rate/reach of COMP-PAER §5–6 by [CALC]; independent C1 test; LE-17, IF-CP-6 | QE fork: QE fork (pw/ph) + EPW + new stages 5–6 (rtsc/sth Sternheimer) + RPA+LFE ε̃⁻¹ (Yambo/BerkeleyGW or Route S) | /home/user/dmdd-solid/returns/R15/COMP-PAER.md §8 (stage table, controls, cost); WP3 formulas /home/user/dmdd-solid/returns/R8/WP3-v3.md §M10, (M.1), (M.13)–(M.14), (M.18) | /home/user/dmdd-solid/code/COMP-PAER/tierH/Si/{scf,ph,nscf,epw}.in (stages 1–4 ready); stages 5–6: to write (INF-2, INF-3); quadrupole.fmt: to write (INF-4) | INF-2, INF-3, INF-4, INF-1 (ε̃⁻¹ with LFE); DC-17 (δ_LF, δ_pair envelope) feeds the pair/LFE term | stage 2 ≈ 24 h on 4 cores (≈ 100 core-h); stage 3 ≈ 1 h; stage 4 ≈ 2–4 h; stage 5 ≈ 2–3 days on 4 cores (≈ 200–300 core-h, dominant); stage 6 ≈ 10¹⁶ flop (App. E.5 count; COMP-PAER §8 had ≈ 10¹⁴), ¼ h to a few h on 1 GPU; ≈ 350–450 core-h + accelerator hours (App. E.14 tab:E14-params) | P1 |
| DC-2 | Ge zero-phonon kinematic edge E_min^ZPL(q), PAER edge and window m_χ^PA, m_ZPL (HSE06+SOC Wannier bands) | Ge | Ch 13 and Ch 17 (Ge is ER-floor rank 1, 0.210 MeV): the Ge window is still [E] (≈ 0.213–0.32 MeV); LE-24 Ge part; COMP-PH IF-5 | QE fork: QE fork (pw.x HSE06 noncollinear SOC) + Wannier90 + code/COMP-PH/{emin,phwin}.py | /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.2; /home/user/dmdd-solid/returns/R15/COMP-PAER.md §9 (window as §4, classes L valleys, C₃ᵥ) | /home/user/dmdd-solid/code/COMP-PH/formulated/Ge-HSE-SOC/{scf.in, Ge.win, pw2wan.in} (fill @VBM_PLUS_…@ from scf.out); Ge force constants from DC-4 | DC-4 (Ge 6³ phonons for ω_ν(Q*)); no new code | 20–60 h on the 4-core box, 4–8 GB (≈ 80–240 core-h); GPU fork: hours; 80–240 core-h + 1–5 GPU-h (COMP-PH §6.2) | P1 |
| DC-3 | Ge PAER tier H rate and reach (as DC-1 with SOC and L-valley classes) | Ge | Ch 13 Ge rate/reach (currently none beyond [E] edges); completes the PAER channel for the second running example | QE fork: QE fork + EPW (SOC, 36 WFs) + stages 5–6 + HSE06 or G₀W₀ band corrections | /home/user/dmdd-solid/returns/R15/COMP-PAER.md §9 | /home/user/dmdd-solid/code/COMP-PAER/tierH/Ge/{scf,ph,nscf,epw}.in (ready: FR-1.0, SOC, 60 Ry, k 12³, q 8³, 120 spinor bands) | DC-2 (quasiparticle band order), DC-1 (pipeline validated on Si), INF-2, INF-3, INF-4 | ≈ 4–8 days on 4 CPU cores (≈ 400–800 core-h); one GPU node: hours; 400–800 core-h + 2–10 GPU-h (COMP-PAER §9) | P2 |
| DC-4 | Ge DFPT on a 6³ q grid, and the Ge results COMP-PH left as placeholders (GE_TABLE, GE_WIN, GE_INS, GE_WTA, GE_MPAER, GE_AXIS, GE_CTRL, GE_QCONV, GE_K) | Ge | LE-16 is still OPEN: COMP-PH returned Ge with unfilled placeholders; Ge phonons vs INS (control), ω_TA(Q*) and the Ge PAER edge feed Ch 13 and DC-2 | QE fork: QE 7.6 ph.x/q2r/matdyn (box) + code/COMP-PH/{chain,phwin,gamma}.py | /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.3, §3.2–§3.3, §5 | /home/user/dmdd-solid/code/COMP-PH/chain.py (phgrid, 80 Ry, k 8³, a_exp 5.658 Å); Ge 4³ run in /home/user/dmdd-solid/code/COMP-PH/out | none | 16 q at the measured 13 min/q ≈ 3.5 h on the 4-core box (≈ 14 core-h); 14 core-h (COMP-PH §6.3) | P1 |
| DC-5 | Magnitude of the Si (2̄00) Umklapp density vertex \|ρ_cv(k,q+G)\| and ∇_kρ_cv at the conduction extremum | Si | LE-25 (narrative-critical): decides whether the allowed-size (2̄00) ZPL leads above its X-face edge ≈ 0.50 MeV (0.547 and 0.62 withdrawn; CW1: Σ|ρ|² = 0.150, allowed size) (T5 close; WP1-v3 IF-6 hedge) | QE fork: QE pw.x nscf + code/COMP-PAER/scripts/formfactor.py (extended to q+G) | /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 exciton spec (ii), §10 item 1; LOOSE-ENDS LE-25 | to write (adapt /home/user/dmdd-solid/code/COMP-PAER/inputs/nscf_rho.in and formfactor.py to the X pockets and G = (2̄00)) | none | minutes (COMP-PAER jobs 4/4b of the same kind: 11–27 s); < 1 core-h; <1–1 core-h ([E-DC] scaled from COMP-PAER §2 jobs 4, 4b) | P1 |
| DC-6 | Forbidden-ZPL / PAER ratio ϖ_II [E14] at the Si edge and +0.1 eV, from S^PA on WP1's (q,ω) grid | Si | LE-26 (narrative-critical): sizes the two-channel band from 0.407 MeV to the allowed-size edge ≈ 0.50 MeV in which PAER still leads near the lower end (T5 close) | QE fork: DC-1 stage-6 output + WP1 zero-phonon S^(1) on the same grid | /home/user/dmdd-solid/returns/R8/WP1-v3.md IF-6b, §8 exciton spec (iii); /home/user/dmdd-solid/returns/R8/WP3-v3.md §M9 (2) | DC-1 outputs; WP1 zero-phonon tables: to write | DC-1, DC-5 | negligible beyond DC-1; 0–1 core-h ([E-DC]) | P1 |
| DC-7 | Si window residuals: SOC admixture of the LA kink and (2̄00)-class LO minimum on axis (LE-27 remainder); finer q̂ search of E_min^ZPL for \|q\| < 1.3 keV | Si | LE-27; COMP-PH §4 note (five q̂ bound min_q̂ from above); fixes p̄_on table entries for WP6 | QE fork: QE noncollinear SOC small cell + code/COMP-PH/{emin,gamma}.py | /home/user/dmdd-solid/returns/R8/WP3-v3.md §R1, §M3; /home/user/dmdd-solid/returns/R15/COMP-PH.md §4 (On/off-axis) | to write (COMP-PH Si inputs + Si_ONCV_PBE_FR) | none | a few core-h (box); 2–10 core-h ([E-DC]) | P3 |
| DC-8 | CONTROLS C8 GaAs decoy: GaAs bands + [E13]-type window scan, then the tier-H pipeline with lpolar (Fröhlich) | GaAs | LE-47; CONTROLS C8 (OPEN since R2; SOTA 'Amendments owed'): PAER must be a small correction in a direct-gap crystal except at m_χ ≈ 0.4–0.9 MeV | QE fork: QE fork + EPW (lpolar) + stages 5–6 | /home/user/dmdd-solid/returns/R15/COMP-PAER.md §8 (C8 with the same pipeline); /home/user/dmdd-solid/returns/R8/WP3-v3.md §M9 C8 | /home/user/dmdd-solid/code/COMP-PH/formulated/GaAs/ (ground state, 140 Ry); tier-H GaAs inputs: to write | DC-1 (pipeline), DC-91 (GaAs Γ-DFPT, Z*, ε_∞), INF-2, INF-3, INF-4 | bands: 0.3–1.5 h box; tier H ≈ DC-1 scale; 300–460 core-h + 2–10 GPU-h ([E-DC] scaled from COMP-PAER §8 and COMP-PH §6.1) | P2 |
| DC-9 | Finite-q BSE beyond TDA for Si/Ge with bound lines; exciton dispersion along Γ–X (both sides) and Γ–L; hydrogenic series with ab initio anisotropic masses | Si, Ge | LE-28, LE-29 (G5, Cat. §12.3): replaces the interim Δ^τ_BSE ∈ [+0.3, +1.0]×S (type M) and the type-A bound lines in Ch 10/13 | BerkeleyGW-or-fork-GW: QE → G₀W₀ → finite-Q BSE (BerkeleyGW finite-Q, Yambo q ≠ 0, or exciting); Haydock/Lanczos | /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 G5 and exciton spec (i), (iv); §10 items 1–2 | to write | INF-1 | ≈ 10³ node-h [E] (≈ 3×10⁴ core-h at 32 cores/node); 1×10⁴–3.2×10⁴ core-h (WP1-v3 §8 G5 (node-h; conversion [E-DC])) | P2 |
| DC-10 | Exciton–phonon replicas (W.14): converged finite-P BSE at the pocket set with EPW g^x | Si, Ge | LE-30 (G5, Cat. §12.3): (W.14) completeness is [C]; replica weights at the PAER edge (Ch 13) | BerkeleyGW-or-fork-GW: finite-P BSE + EPW g on the same U(k); g^x by 1705.04245 Eq. (49) | /home/user/dmdd-solid/returns/R8/WP3-v3.md §8 G5 | to write | INF-1, DC-9 | ≈ 10⁴ CPU-h; 1×10⁴ core-h (WP3-v3 §8 G5) | P3 |
| DC-11 | Crystal exciton Migdal (G-X8): finite-p BSE over the BZ inside the G6 code path | Si, Ge | LE-31; WP7-B1-v2 §8 X8 (Migdal electronic excitation without ionisation, Ch 12) | BerkeleyGW-or-fork-GW: finite-p BSE (p 8³–12³, G ≤ 50, λ ≤ 20 per p) in the DC-25 path; atoms by GRASP2018/MCHF | /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §8 (Computation specification) | to write | INF-1, DC-25 | ≈ 1 node-h per p, 60–100 node-h; 2–3×10³ core-h (CW1 §8; App. E.15) | P3 |
| DC-12 | Frenkel / self-trapped excitons in NaI (localisation, binding, release) | NaI | LE-32 (CW1, OPEN-pending): NaI exciton physics in Ch 16/18 | other: constrained-occupation hybrid DFT (QE HSE/PBE0) + BSE; method shared with DC-73 | /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 'Remaining gaps'; method as /home/user/dmdd-solid/returns/R16/CW5.md §4.1 (STE by constrained hybrid DFT) | to write | INF-1 (BSE); CW1 formula pointer still owed | ≈ 10⁴ core-h (216-atom hybrid + I SOC relaxations dominate), ×2 with the TDDFT check; 1×10⁴–2×10⁴ core-h (App. E.15; [E-DC] basis) | P3 |
| DC-13 | G7 core and relativistic response: Ge 3d, Ga 3d, Si 2p core-level finite-q BSE with SOC (ZORA/FLAPW) | Ge, GaAs, Si | LE-33 (G7): interim ~10⁻³ (≤ 2%) for Ge 3d; Ch 10 core contributions | other: all-electron FLAPW (exciting or WIEN2k) with SOC, or PAW + core reconstruction | /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 G7 | to write | INF-1, INF-6 | not estimated in the source; 1000–1×10⁴ core-h ([E-DC]) | P3 |
| DC-14 | Non-density operator library: G10 IP response tables (12 real functions Si/Ge) with exported R⁰_GG′; LFE screening of j_T and in-medium 𝒪₈ ratio; triplet channel beyond IP (ladder + f_xc^T) | Si, Ge | LE-34, LE-35, LE-38 (G10): L3 '≥ 12× (IP 20–30), factor UNRESOLVED' for 2510.25835 𝒪₅/𝒪₈; Ch 10 and Ch 21 recasts | other: QE + EXCEED-DM-type IP module (vertices ρ_cv, ⟨c\|½{p,e^{iq·r}}\|v⟩ with the non-local commutator), RPA+LFE Dyson with mixed blocks, triplet ladder | /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 G10, §10 items 4–5; IF-10, IF-13, IF-14 | to write | INF-9 (IP vertex module), INF-1 (ladder) | ≈ 10³ core-h Si, ×4 Ge (bubble ≈ 10¹⁶ ops; Dyson by iterative solve for the needed right-hand sides, not full inversion; full R⁰_GG′ (≈ 2300 G at 8αm_e, ≈ 600 TB on the full grid) stored only on a coarse subset at 4αm_e, ≈ 10 GB) (App. E.16) | P2 |
| DC-15 | G11 electronic anisotropy S₄, S₆, S₈(\|q\|, ω): full-q RPA+LFE ELF projected on cubic harmonics | Si, Ge, GaAs | LE-39 (G11): daily-modulation amplitude for a site latitude (Ch 17, Ch 21) | other: GPAW, QCDark2 or BerkeleyGW full-q RPA+LFE | /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 G11 | to write | INF-1 | not estimated in the source; 1000–1×10⁴ core-h ([E-DC]) | P3 |
| DC-16 | SOC mixing near the Ge edge and the SOC-lifted Si on-axis vertex | Si, Ge | LE-36: interim ≲ 10% (Ge) and ≈ 4% amplitude (Si) [E] | QE fork: QE noncollinear small cell (box) | /home/user/dmdd-solid/returns/R8/WP1-v3.md §10 item 6; LOOSE-ENDS LE-36 | to write (FR SG15) | DC-2 (Ge bands; Si part needs nothing) | small cell, box; 4–20 core-h ([E-DC]) | P3 |
| DC-17 | X2 numerics: N1 1D two-band contact-kernel model vs real-time TDH; N2/N3 Si Route S (ZG supercell, RPA local fields) at q = 0 and 0.5/1/2 keV (δ_LF, δ_pair, Λ(q)); N4 ε̃⁻¹_G0(q,ω) in the window | Si (N1: model) | LE-40, LE-41, LE-42 (and LE-44 ALDA k_xc size): narrows the pair/local-field envelope [0.4, 1.8] that enters the PAER rate (Ch 13) and LIMITS L8 | QE fork: N1: python script; N2–N4: QE supercells + RPA-LFE (turbo_eels, Yambo, or own code) | /home/user/dmdd-solid/returns/R3/X2.md §8 (Route S), §10 N1–N4; /home/user/dmdd-solid/returns/R8/WP3-v3.md §M10 routes | to write | N1 none; N2–N4: INF-1 (RPA+LFE) or Route-S code | N1 minutes; N2–N4 not estimated in the source (ZG supercells 4³–6³, WP3-v3 §8 G2: 10¹⁰–10¹¹ flop + supercells, CPU); 1000–1×10⁴ core-h ([E-DC]; WP3-v3 §8 G2 order) | P2 |
| DC-18 | X1 residual tags: frozen-strain deformation tensors D^n for Si (symmetric D^n under rotations, D/c_ν ≫ q, piezo-log relevance) | Si | LE-179 | QE fork: DFPT or finite strain (pw.x) | /home/user/dmdd-solid/returns/R3/X1.md §10 status table; LOOSE-ENDS LE-179 | to write | none | box; 5–20 core-h ([E-DC]) | P3 |
| DC-19 | Shared harmonic stack A: DFPT force constants, eigenpairs, per-atom PDOS, B_κ, Z*, ε_∞ at 80 Ry on an 8³ q grid (experimental a; PBE vc-relax partner) | Si, Ge, GaAs | Base input of CW2 rows (LE-48, 55, 57, 60, 65, 67) and of DC-21/25/35; Ch 5, Ch 11 | QE fork: pw.x → ph.x (8³) → q2r.x → matdyn.x | /home/user/dmdd-solid/returns/R16/CW2.md §0b stack A | /home/user/dmdd-solid/code/CW2/inputs/{Si,Ge,GaAs}/{scf,ph,q2r,matdyn_dos,matdyn_modes}.in (+ README) | none; COMP-PH outputs replace the Si/Ge part when converged at 80 Ry | Si ≈ 25, Ge ≈ 60, GaAs ≈ 60 CPU·h; 145 core-h (CW2 §0b) | P2 |
| DC-20 | Coherent two-phonon S^(2)_coh(q,q̂,ω) at q < q_BZ and rate-level ℛ₂, ℛ₃ (CW2.1)–(CW2.3) | Si (then Ge, GaAs) | LE-48, LE-49 table flags (incoherent-approximation error at n_ph ≥ 2); Ch 11 | other: python/Fortran module on stack-A eigenpairs (48³) | /home/user/dmdd-solid/returns/R16/CW2.md §1, §2 | DC-19 outputs; module: to write | DC-19, INF-9 | ≈ 2×10⁹ evaluations, a few CPU·h after stage A; 2–5 core-h (CW2 §1) | P3 |
| DC-21 | G3 multiphonon library tables S(q,q̂,ω), P_ph(n_ph\|q,ω), ρ^ph_κν, f_coh, ℛ_n (HDF5) and G11 lattice anisotropy S_ℓm (Lebedev 590) | Si, Ge, GaAs (then survivors) | LE-57, LE-60: the NR multiphonon channel library (Ch 11, Ch 19) and the prediction S_{ℓ≥4} = 0 in the incoherent part | other: new ≈ 300-line (3.5) module on stack-A PDOS (48³ tetrahedra) | /home/user/dmdd-solid/returns/R16/CW2.md §10, §13 | DC-19; module: to write | DC-19, INF-9, DC-20 (flags) | tables minutes after stage A; 1–2 core-h (CW2 §10) | P2 |
| DC-22 | Valence charge deformation Δ_κα(Q+G) at q ≫ q_BZ (\|Q+G\| ≤ 20 keV) and core polarisation Δ^core_κ(q) (L4 add-on 𝒵_κα(Q+G)) | Si, Ge, GaAs | LE-51 (CLOSED-AS-EXACT-GAP: two missing computational steps) | QE fork: ph.x fildrho + PAW AE reconstruction or LAPW finite-displacement supercells; Dalgarno–Lewis on ld1.x cores | /home/user/dmdd-solid/returns/R16/CW2.md §4 + /home/user/dmdd-solid/returns/R16/CW2-errata.md E-5 (ecutrho ≥ 65 Ry, one-centre transforms, core sub-spec (d)) | ph.in of /home/user/dmdd-solid/code/CW2/inputs/* (drho kept); AE supercells: to write | DC-19, INF-6 | DFPT add-on negligible; AE supercells ≈ 2 × 50 CPU·h; core polarisation minutes; 100–110 core-h (CW2 §4; CW2-errata E-5) | P3 |
| DC-23 | Finite-q eκ factor Δ𝓃_κ(q,q̂) beyond hydrogenic 1s²: crystal valence AE density and finite-nucleus Dirac 𝓃_e(R_κ) | Si, Ge, GaAs | LE-56 (CEG: steps 1–2 open), LE-54 relativistic scoping (E^Mig_3 with ⟨𝓃_e⟩_ρnuc) | other: PAW pp.x plot_num=21 minus atomic core or LAPW; GRASP2018/DIRAC or patched ld1.x | /home/user/dmdd-solid/returns/R16/CW2.md §9; /home/user/dmdd-solid/returns/R16/CW2-errata.md E-6, E-7 | /home/user/dmdd-solid/code/CW2/atomic_contact.py, atomic_contact_errata.py (atomic part done); crystal part: to write | INF-6 | ≈ 10 CPU·h (crystal); minutes per atom (Dirac); 10–12 core-h (CW2 §9; CW2-errata E-7) | P3 |
| DC-24 | Drag mass δM_κ, inverse moments ℐ₂–ℐ₄, C_κ and P_Mig(E_R) by frequency-dependent Sternheimer | Si, Ge, GaAs | LE-55: P_Mig ≤ 10⁻³ validation; replaces [E] δM (Si 2.7, Ge 2.4 ×10⁻⁴); Ch 12 | QE fork: ph.x + mixed E(ω)–u response at imaginary ω (rtsc/sth batched shifted solves) | /home/user/dmdd-solid/returns/R16/CW2.md §8, §0b stack C | to write (stack-C patch) | DC-19, INF-5 | ≈ 3× a DFPT (≈ 75 CPU·h Si; Ge, GaAs ≈ 3 × 60); 75–435 core-h (CW2 §8 (Ge/GaAs scaled from §0b)) | P2 |
| DC-25 | G6 Migdal single code path: all-electron RPA+LFE S^ee_GG′(p,ω_e) (p ≤ 30 keV, ω_e ≤ 100 eV) convolved with S^GS_κκ; quenching-subtraction kernel; T2/LFE band (also the Wannier branch of WP7-B1 X6) | Si, Ge | LE-61 (G6); WP7-B1-v2 §7 spec; Ch 12 Migdal rate with one code for L7a–d | BerkeleyGW-or-fork-GW: GPAW AE or Yambo/BerkeleyGW with semicore; DC-21 tables; impulse-bracket convolution | /home/user/dmdd-solid/returns/R16/CW2.md §14; /home/user/dmdd-solid/returns/R8/WP3-v3.md §8 G6; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §7 | to write | INF-1, INF-6, DC-21 | ≈ 10³ CPU·h; 1000 core-h (CW2 §14; WP3-v3 §8) | P2 |
| DC-26 | Non-rigid Wannier correction ratio 𝔯_W(q,ω_e) = \|A^DFPT\|²/\|A^(H_W)\|² with the bare ∇_RV screened by RPA+LFE at ω_e | Si, Ge, diamond | LE-115 (CEG, G-X6/LB1-8): the X6 type-M nuisance | EPW: ph.x bare perturbation → Wannier90 MLWFs (k 16³) on one U(k) → EPW-style interpolation; RPA+LFE screening | /home/user/dmdd-solid/returns/R16/CW4.md §19 + /home/user/dmdd-solid/returns/R16/CW4-errata.md A3(c) (bare vertex, dynamical screening) | to write | INF-1, DC-25 | 10³ CPU-h (GPU fork); 1000 core-h (CW4 §19) | P3 |
| DC-27 | X10 valence amplitude for c_κ not ∝ M_κ: S^ee_GG′(k → 0, ω) for \|G\| ≤ 6(2π/a), ω from E_g to 100 eV + core edges, contracted with (CW2.26) | Si (diamond-structure) | LE-71 (B2-L9): scalar–nucleon couplings not proportional to mass (Ch 11/16) | BerkeleyGW-or-fork-GW: Yambo/BerkeleyGW χ_GG′(q→0,ω) or QE turbo_eels at q = G | /home/user/dmdd-solid/returns/R16/CW2.md §24 | to write | INF-1 | ≈ 10² CPU·h; 100 core-h (CW2 §24) | P3 |
| DC-28 | Loss function L(k,ω) = Im[−(ε⁻¹)₀₀] (RPA+LFE, scissor/GW gap, semicore) for every survivor, \|k\| ≤ 5 keV, ω ∈ [E_g, 5ω_p]; 𝓠_Mig,κ and w_acc⟨1/ω⟩ | all 42-pool survivors (WP8-U v4) | WP8-S-v2 §6 item 1; WP8-errata §15; GAP:L_eps2_data (38 materials): the Migdal row of Ch 17 cannot be ranked without it | BerkeleyGW-or-fork-GW: QE scf → dense nscf → χ⁰_GG′ (Yambo/BerkeleyGW or fork) → Dyson (RPA; ALDA rung) | /home/user/dmdd-solid/returns/R17/WP8-errata.md §15 | to write (COMP-PH layout) | INF-1; DC-91/94/96/97 ground states | not estimated in the source; 4000–4×10⁴ core-h ([E-DC] 10²–10³ core-h per material × ≈ 40) | P2 |
| DC-29 | G3 PIMD inputs: nuclear momentum distribution 𝔫_κ(p), E^kin_q̂, ⟨∂²_q̂E^ad_0⟩ (= 𝔨₃^GS), 𝔨₄ pieces | Si, Ge | LE-58 (exact GS moments (CW2.10) anchoring the impulse/multiphonon tables and the anharmonic template) | MD-MLIP: i-PI + MLIP (MACE/NequIP on PBE or SCAN), 216-atom cells | /home/user/dmdd-solid/returns/R16/CW2.md §11, §0b stack D | to write | INF-7 | ≈ 10³ CPU·h; 1000 core-h (CW2 §11) | P3 |
| DC-30 | Non-perturbative anharmonicity and quantum crystals: TRPMD/CMD/SSCHA/TDEP F_s(q,t), S_self(q,ω) for soft-mode and light-atom targets; solid ⁴He moments and band (PIMD, Aziz potential); solid He SSCHA Φ_eff at 1–40 GPa | KTaO₃, SrTiO₃, LiH, solid He | LE-52 (CEG), LE-70 (L11 remainder), WP7-B2-v2 §4 (L11); Ch 11 scope statements | MD-MLIP: i-PI (TRPMD/CMD) + MLIP; SSCHA/TD-SCHA; TDEP; Aziz He–He | /home/user/dmdd-solid/returns/R16/CW2.md §5, §23 + /home/user/dmdd-solid/returns/R16/CW2-errata.md E-12; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §4 | to write | INF-7 (MLIPs for the oxides/LiH) | MLIP 1080 atoms × 80 beads × 4×10⁵ steps ≈ 10³–10⁴ CPU·h per (material, T); SSCHA ≈ 10²; He PIMD ≈ 10³; WP7-B2 He ≈ 10⁴ CPU·h; 1.5×10⁴–5×10⁴ core-h (CW2-errata E-12; CW2 §23; WP7-B2-v2 §4 (sum over 4 targets [E-DC])) | P3 |
| DC-31 | G13 / G-F2 anharmonic nuisance template: phono3py fc3 (4×4×4, 128 atoms), hiPhive/TDEP fc4, bubble spectral function, W₃/W₄ contour sums, Δ^τ_A(q,ω) | Si (then Ge, GaAs) | LE-59; WP8-F G-F2 (type-T anharmonic spread of the multiphonon FOM at ω_th ≳ ω_max) | other: phono3py + hiPhive/TDEP on QE supercells; PIMD anchor DC-29 | /home/user/dmdd-solid/returns/R16/CW2.md §12 | to write | INF-12, DC-19, DC-29 | ≈ 300 supercell DFT runs + ≈ 10³ CPU·h for the mode sums; 1000–1×10⁴ core-h (CW2 §12 (supercell runs [E-DC] up to 10⁴)) | P2 |
| DC-32 | Glass models: melt-quench MLIP glasses (648–5184 atoms, ≥ 5 quenches), full Hessians, Z*_I; amorphous S_dist at n_ph = 2, 3 (CW2.12′); IR coefficients A^IR, B^IR of C^IR = A + Bω²; disorder D_I, C^IR (WP7-B2 §2) | a-SiO₂, a-Si, SiN_x | LE-53, LE-64; WP7-B2-v2 §2 (A7/L10); Ch 16 amorphous targets | MD-MLIP: LAMMPS + MLIP; phonopy Γ-only; DFPT Z* on 192–648-atom subcells or charge-equilibration MLIP | /home/user/dmdd-solid/returns/R16/CW2.md §6, §17; /home/user/dmdd-solid/returns/R16/CW2-errata.md E-8; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §2 | to write | INF-13 (glass MLIP), INF-9 | MD ≈ 10⁴ CPU·h (WP7-B2); ≈ 10² per model after MD; DFPT Z* ≈ 10³ CPU·h; 1.1×10⁴–1.2×10⁴ core-h (CW2 §6, §17; WP7-B2-v2 §2) | P3 |
| DC-33 | Isotope B−L channel: Γ_iso(ω) exactly from isotope-resolved Hessians (4096-atom natural-Si supercells, 10 realisations); T = 0 two-phonon ε₂(ω) of Si from ∂Z*/∂u | Si | LE-65, LE-66 (CEG: T = 0 ε₂ or cold data missing); Ch 11/16 isotope channel (Γ_iso/Γ_EM ≥ 6.3×10³) | QE fork: stack-A IFCs + dense diagonalisation / KPM; DFPT epsil in ±u supercells (64, 216 atoms) | /home/user/dmdd-solid/returns/R16/CW2.md §18, §19 + /home/user/dmdd-solid/returns/R16/CW2-errata.md E-9 | to write | DC-19 | Γ_iso ≈ 10 CPU·h; ε₂: 64 atoms 6 × ≈ 20 ≈ 1.2×10², 216 atoms 2 × ≈ 10³ ≈ 2×10³ CPU·h; 130–2010 core-h (CW2 §18; CW2-errata E-9) | P3 |
| DC-34 | GaAs electron-scalar single-phonon rate as a near-cancellation: DFPT Z*, ε_∞ to ≲ 1% with LST data; PhonoDark-abs with vertex Z_κ − Z*_κ and the mixing term; Γ^ph_ν from phono3py | GaAs | LE-67 (A4/B2-L1), WP7-B2-v2 §1: d = −1.33×10⁻³; 2308.06314 Fig. 2 ≈ 9× high (LE-68); Ch 11 | QE fork: QE/Abinit DFPT + PhonoDark-abs (patched) + phono3py | /home/user/dmdd-solid/returns/R16/CW2.md §20 + CW2-errata E-10; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §1 | /home/user/dmdd-solid/code/CW2/inputs/GaAs/ (DFPT); [FT] low-T ω_L, ω_T, ε_∞, a: to collect | DC-19, INF-12 | DFPT ≈ 10² CPU·h; fc3 10³–10⁴ CPU·h; 1100–1×10⁴ core-h (WP7-B2-v2 §1) | P2 |
| DC-35 | Crystal NR bremsstrahlung: Z*_κ(ω) at zero macroscopic field for ω ∈ [0.05, E_g], n_r(ω), dℛ/dω_γdω_ph by (W.13) | GaAs (Si, Ge) | LE-62 (Cat. §12.4): GaAs 10³–10⁴× atomic [E], relevance [C] | QE fork: TDDFPT mixed E(ω)–u response (zstar_eu generalised, rtsc/sth) | /home/user/dmdd-solid/returns/R16/CW2.md §15; /home/user/dmdd-solid/returns/R8/WP3-v3.md §8 Bremsstrahlung | to write | INF-5, DC-19, DC-21 | ≈ 2× a DFPT per frequency batch (≈ 50 CPU·h GaAs); 50–500 core-h (CW2 §15 (batches [E-DC])) | P3 |
| DC-36 | Reflection/refraction force above σ_crit for the MICROSCOPE cylinders (CW2.25) and the DWBA for density fluctuations ⟨δnδn⟩ | Pt/Ti cylinders; random media | LE-69 (B2-L4), WP7-B2-v2 §3: any bound from this channel stays [C] until run | other: ≈ 300-line transfer-matrix + 4D Monte-Carlo code (box) | /home/user/dmdd-solid/returns/R16/CW2.md §22; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §3 | to write; ⟨δnδn⟩ from SAXS/USAXS data | none | CPU minutes; <1–1 core-h (CW2 §22) | P3 |
| DC-37 | κ_URF in MOF cells (three-phonon branching with angular-momentum labels, (CW2.27′)) and giant-moment 4f orbit–lattice amplitudes ∂⟨s_e,L⟩/∂u (CASSCF-SO on embedded clusters) | chiral MOFs; SMMs | LE-72 (CEG, both halves), WP7-B2-v2 §7 (L9/S8) | other: phono3py fc3 (DFT or MLIP), sparse solve; CASSCF-SO | /home/user/dmdd-solid/returns/R16/CW2.md §25 + /home/user/dmdd-solid/returns/R16/CW2-errata.md E-11 | to write | INF-12, INF-7 | fc3 ≈ 10⁵ CPU·h (DFT) or ≈ 10³ (MLIP); giant moments 0.5–2 CPU·h × 6N_cl ≈ 10²–10³ per site; 1100–1×10⁵ core-h (CW2 §25; CW2-errata E-11) | P3 |
| DC-38 | Γ_Λ₀/δ map over (q, ω), Fano coefficient c_ν^F(Λ₀), K_ν ≥ 0 test, d11 edge-shell and onset-shell masks | GaAs (and Si) | LE-76; IF-R8-10 'nobody supplies the GaAs Γ/δ map' (WP5-v4 R7, R7′; O4 §9; OW0-10): θ_𝔉 in GaAs currently uses only \|ΔP\| ≤ 2π max\|c^F\|; Ch 18 Fano term | EPW: QE fork (FR SOC) DFPT 6³ + EPW elecselfen (fine q 100³, 13824 shell k) + the WP3 response code (c^F from M^(2)) | /home/user/dmdd-solid/returns/R16/CW3.md §2.3 + /home/user/dmdd-solid/returns/R16/CW3-errata.md §1.4 (onset shells, pitfall (6)) | /home/user/dmdd-solid/code/CW3/fork/{GaAs-LE76,Si-LE76}/{scf,ph,nscf,epw}.in, /home/user/dmdd-solid/code/CW3/fork/mk_shell_k.py (reset fermi_energy and dis_froz_max from scf/nscf output) | c^F part: INF-3 (WP3 response code); Γ part: none | GaAs FR DFPT ≈ 3–6×10² core-h (≈ 5–10 GPU-h); EPW self-energy ≈ 10⁴ core-h (≈ 30–60 GPU-h); Si ≈ 1/10; 1.1×10⁴–1.2×10⁴ core-h + 39–77 GPU-h (CW3 §2.3) | P2 |
| DC-39 | All-electron orbit–orbit f-sum shift δ_oo(q) (CW3.3) and total δ_rel = δ_mv + δ_oo | Si, Ge | LE-78 (OW0-15): replaces the Thomas–Fermi [E] −0.23% (Si), −0.73% (Ge) in WP1 [E11], WP6, L17 | other: pyscf X2C-HF (sfx2c1e), uncontracted ANO-RCC/cc-pwCV5Z; PAW crystal valence correction | /home/user/dmdd-solid/returns/R16/CW3.md §3.2 + CW3-errata V5 | to write | crystal part only: INF-6 | minutes per atom (fits the box); crystal correction ≈ 10 core-h; 10–11 core-h (CW3 §3.2) | P3 |
| DC-40 | Relaxed electron-channel static step 1 − ε_e⁻¹(q,0) = clamped step + 𝒢_GS(q) (CW3.4) with the electron-following charge Z^(e)_κ(q) from frozen-phonon supercells | Si, GaAs | LE-83 (L17): the relaxed-channel bound; [E] ≳ 10² at 1 keV | QE fork: pw.x + pp.x frozen-phonon supercells (Si 1×1×N, N = 2…8) or DFPT induced density | /home/user/dmdd-solid/returns/R16/CW3.md §3.3 + /home/user/dmdd-solid/returns/R16/CW3-errata.md §1.5 | to write | DC-19 (phonons); clamped step from DC-28 | ≈ 10² core-h (fits the box in parts); 100 core-h (CW3 §3.3) | P3 |
| DC-41 | Al BCS response: GRPA vertex 𝔳_GRPA(q,ω) on the WP4 [4.2] grid; full Im ε^BCS, its KK transform and the 𝔰_BCS-corrected L^BCS table | Al | LE-97, LE-104, LE-157 (SC nuisance mask; replaces 'exclude y ≲ 3.5'); WP5 R5; Ch 15 | other: 2-D quadrature (Gauss–Legendre in μ, adaptive ξ) + log-grid KK (box) | /home/user/dmdd-solid/returns/R16/CW4.md §1, §8 | to write (inputs N(0), v_F, Δ_BCS only) | none | CPU-minutes (fits the box); <1–1 core-h (CW4 §1, §8) | P2 |
| DC-42 | Amorphous WSi: ⟨L⟩(q,ω) from RPA+LFE on MLIP-quenched cells, Kubo–Greenwood σ₁, and Δ_BCS inhomogeneity P_Δ by BdG | a-W_xSi_{1−x} | LE-98 (RG2; G9 film item): the only route to a WSi correction (Ch 15) | MD-MLIP: MACE/DeePMD on AIMD → QE scf/nscf → Yambo/BerkeleyGW ε_GG′ → Wannier90 TB + attractive-U BdG | /home/user/dmdd-solid/returns/R16/CW4.md §2 | to write | INF-13, INF-1 | MLIP training 10³; DFT 10³–10⁴ per quench (≥ 5); RPA 10⁴–10⁵ total; BdG 10² CPU-h; 1.6×10⁴–1.6×10⁵ core-h (CW4 §2 (5 quenches)) | P3 |
| DC-43 | Magnon sector: two-magnon S^(2m)(q,ω) with the 1/S ladder and bound states (RG3); LSWT beyond Larmor (anisotropic, dipolar, AFM; demag) for absorption; magnon FOM r_2m and ΔS | YIG, NiO, MnF₂, α-RuCl₃ (benchmarks) | LE-99 (CEG), LE-116, LE-156; WP7-B2-v2 §5 (S2); Ch 14 | other: SpinW/Sunny (Colpa) + linear solve of (3.1) on 30³–40³ k | /home/user/dmdd-solid/returns/R16/CW4.md §3, §20; /home/user/dmdd-solid/returns/R16/CW7.md §7; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §5 | to write | DC-44 (exchange inputs) | ≈ 10² CPU-h (YIG, 20 sublattices); LSWT ≪ 1 CPU-h per target; S^(2m) ≈ 3×10⁷ operations per q; 100–110 core-h (CW4 §3, §20; CW7 §7) | P2 |
| DC-44 | Magnet inputs from DFT+U: exchange J^ex (four-state or TB2J), single-ion anisotropy, g tensors where no INS/ESR fit exists | YIG, NiO, MnO, Cr₂O₃, NiPS₃ | 'YIG and the magnets' owed data (brief); inputs of DC-43 and of the MAG FOM in Ch 14/17 | QE fork: QE DFT+U (hp.x for U) + TB2J on Wannier functions | /home/user/dmdd-solid/returns/R16/CW4.md §3 (Method), §20 | to write; YIG a = 12.3750 Å from /home/user/dmdd-solid/state/DATA-ADDENDA.csv | none | DFT+U inputs ≈ 10³ CPU-h (YIG); smaller cells less; 1000–5000 core-h (CW4 §3 (other magnets [E-DC])) | P2 |
| DC-45 | Non-dipole orbital magnetic form factors ⟨j_K(q)⟩ (K = 0…6) and multiplet-projected matrix elements for SOC ions | SOC ions of the WP8-U survivors | LE-103 (RG8); F^mag(q) of the MAG FOM (CW7 §7 (c)) | other: GRASP Dirac–Fock or QE DFT+U Wannier projections (_FR) + sympy Racah algebra | /home/user/dmdd-solid/returns/R16/CW4.md §7 | to write | none | < 10 CPU-h per ion; 10–60 core-h (CW4 §7 (≈ 6 ions [E-DC])) | P3 |
| DC-46 | Finite-q optical activity 𝒢_OA(q,ω) and S_{j^αj^β}(±q,ω) with SOC (current vertex with the non-local commutator) | Te or α-SiO₂; one magnetoelectric target | LE-100 (RG4): chiral and nonreciprocal responses (Ch 16) | other: QE noncollinear → EXCEED-DM-type IP code extended to the current vertex → Yambo LFE | /home/user/dmdd-solid/returns/R16/CW4.md §4 | to write | INF-9, INF-1 | ≈ 10³–10⁴ CPU-h per target; 2000–2×10⁴ core-h (CW4 §4) | P3 |
| DC-47 | Finite-q multiplet transition densities \|⟨F\|ñ_e(q)\|I⟩\|² for the NV⁻ manifold (QDET/CRPA + CI) | diamond NV⁻ | LE-101 (RG5; Cat. §12.5) | other: QE PBE/HSE 512–1000-atom supercells + WEST QDET + full CI + new γ^FI × plane-wave form-factor module | /home/user/dmdd-solid/returns/R16/CW4.md §5 | to write | none | 10⁵ CPU-h (HSE + WEST); 1×10⁵ core-h (CW4 §5) | P3 |
| DC-48 | Anisotropic massive-Dirac ZrTe₅: G₀W₀ (SOC) fit of k·p parameters and ε_bg,ii; analytic Elliott–Sommerfeld threshold; model BSE on a log-graded radial k grid; beyond-ladder spread | ZrTe₅ (Bi₂Se₃ ε_bg) | LE-102 (CEG; step (4) has no controlled method), GAP:eps_bg (ZrTe₅, Bi₂Se₃); Ch 16 Dirac targets | BerkeleyGW-or-fork-GW: QE + Yambo G₀W₀ SOC (12-atom cell, 12×12×4 + refinement); model codes (box) | /home/user/dmdd-solid/returns/R16/CW4-errata.md A12 (replaces CW4 §6) | to write | INF-1 | model and analytic stages CPU-minutes; G₀W₀ 10⁴ CPU-h (GPU fork); 1×10⁴ core-h (CW4-errata A12) | P3 |
| DC-49 | Re-plot of the 1708.08929 / 1910.02091 scattering and absorption reaches with ε_bg², ε_bg and the 0.55–0.62 charge renormalisation | ZrTe₅, BNQ-TTF, Yb₃PbO | LE-105 (RG10; LIMITS L16 're-plot'): corrected literature limits in Ch 16/21 | other: re-implementation of 1910.02091 Eqs. (3.13)–(3.14) (box) | /home/user/dmdd-solid/returns/R16/CW4.md §9 | their Tables 1–2; code: to write | none | CPU-minutes (fits the box); <1–1 core-h (CW4 §9) | P2 |
| DC-50 | Superconducting Holstein absorption σ₁^{S,(2,1)}(ω) with Eliashberg spectral functions (EPW α²F, α²F_tr) | Al, Nb | LE-108 (G-A2), WP7-B1-v2 §9 (A2): dark-photon/ALP absorption in SC sensors (Ch 15) | EPW: QE → ph (8³) → EPW (Al k 60³/q 30³; Nb 40³/20³) → eliashberg (Padé or real axis) → (A2.2) integral | /home/user/dmdd-solid/returns/R16/CW4.md §12; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §9 | to write | none | 10³ CPU-h (GPU fork); 1000 core-h (CW4 §12; WP7-B1-v2 §9) | P3 |
| DC-51 | Disorder-averaged donor response ⟨S^D(q,ω)⟩ of Si:P near the impurity band (multivalley EMT tight binding, 10⁴–10⁵ sites) with DFT central-cell check; impact number of the 2212.04504 misprint | Si:P (n_D = 10¹⁸, 1.8×10¹⁸ cm⁻³) | LE-109 (G-A6), WP7-B1-v2 §10 (A6 dopant absorption); Ch 16 | other: Lanczos/KPM on Hubbard–Anderson TB; QE 1000–4000-atom Si:P clusters | /home/user/dmdd-solid/returns/R16/CW4.md §13; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §10 | to write | none | 10³ CPU-h (TB); DFT clusters 10⁴ CPU-h; impact number minutes; 1.1×10⁴ core-h (CW4 §13) | P3 |
| DC-52 | Molecular crystals: periodic GW-BSE vs Frenkel/Hückel/PPP transition densities, charge-transfer weight θ²_CT, Frenkel form-factor tables (frenkel-ff) | anthracene, t-stilbene | LE-112 (G-E5), WP7-B1-v2 §2 (E5 Frenkel excitons); Ch 16 | BerkeleyGW-or-fork-GW: QE + Yambo/BerkeleyGW G₀W₀+BSE (50–100 atoms, k 4³, 200 bands); PySCF/ORCA molecular TDDFT; new frenkel-ff module | /home/user/dmdd-solid/returns/R16/CW4.md §16; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §2 | to write (CSD structures) | INF-1, INF-9 | 10³–10⁴ CPU-h per crystal; periodic BSE 10³–10⁴; tables ≈ 10 CPU-h; 2000–3×10⁴ core-h (CW4 §16; WP7-B1-v2 §2) | P3 |
| DC-53 | Graphene/CNT vacuum ejection: rate-weighted OPW factor R_OPW(E_kin) with all occupied orbitals; FSI with screened-hole scattering states; low-D RPA tables (lowd-rpa) for sheets, tubes, stacks, quantum dots | graphene, CNT, layered stacks, QDs | LE-113 (G-E12), WP7-B1-v2 §3–§6 (E8, E9, E10, E12); Ch 16 low-dimensional targets | other: QE + Wannier90 MLWFs + FFT overlaps; lowd-rpa module; EFA solver; Yambo slab cutoff cross-check | /home/user/dmdd-solid/returns/R16/CW4-errata.md A2; /home/user/dmdd-solid/returns/R16/CW4.md §17; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §3–§6 | to write | INF-9 | OPW CPU-minutes; FSI CPU-hours; lowd-rpa < 1 CPU-h + 10²–10³ DFT bubbles; QD clusters 10⁴; ejection 10²; 100–1.2×10⁴ core-h (CW4-errata A2; WP7-B1-v2 §3–§6) | P3 |
| DC-54 | Recast of 2401.11971 (CRDM) limits with the exact density-row ratio (1 − ω²/Q²)² and the transverse row | Si, Ge | LE-114 (G-I5, LB1-13): impact on 2401.11971 UNRESOLVED until run; Ch 21 | other: re-implementation of their Eqs. (4)–(6) + transverse term (box) | /home/user/dmdd-solid/returns/R16/CW4.md §18 + CW4-errata A4 | their CRDM flux tables; code: to write | none | CPU-hours (fits the box); 1–10 core-h (CW4 §18) | P3 |
| DC-55 | Ohmic electron-bath coupling α_ohm of tunnelling defects from eigenphases of S_R S_L† (CW5-6) | crowdion in W, H in Nb, TLS in Al/AlOx, WSi | LE-127 (G-T1): α_ohm is a prerequisite for every normal-metal host (WP7-T-v2 §4.6); Ch 16 defects | QE fork: route 2: QE PBE supercells (54/128/250 atoms, SG15 W semicore) + Slater-determinant overlaps; route 1: KKR (JuKKR/AkaiKKR) | /home/user/dmdd-solid/returns/R16/CW5.md §3.1 + CW5-errata A21 | to write (rtsc layout) | DC-56 (relaxed end states) | route 2 ≈ 10³ GPU-h per defect; 4000 GPU-h (CW5 §3.1 (4 defects [E-DC])) | P3 |
| DC-56 | Release paths of eV-scale defects: Huang–Rhys S_HR,k, E_reorg, λ_eff along the MEP, ring-polymer instanton action; production catalogue (50 paths/material) and KMC rates ℛ_rel(E,t,T); ΔSCF charge-state variant | Si, Ge close Frenkel pairs; Al SIA | LE-128 (pilot), LE-129 (frozen verdicts now OPEN, CEG), LE-147 (carrier-driven reactions); WP7-T-v2 §4.6; Ch 19/20 delayed release | QE fork: QE pw.x/neb.x (64-atom pilot) + phonopy Hessians + i-PI instantons on the MLIP; KMC | /home/user/dmdd-solid/returns/R16/CW5.md §3.2–§3.3, §4.4; /home/user/dmdd-solid/returns/R12/WP7-T-v2.md §4.6 | /home/user/dmdd-solid/code/CW5/LE-128/{scf.in, neb.in, notes.txt} (pilot); production: to write | INF-7 (MLIP end states, instantons), DC-61 (quench protocol, shared E^conf table) | pilot ≈ 900 SCFs ≈ 30 h on the 4-core box (≈ 120 core-h) or ≈ 2 GPU-h; production ≈ 10⁴–10⁵ GPU-h; 120 core-h + 1×10⁴–1×10⁵ GPU-h (CW5 §3.2; WP7-T-v2 §4.6) | P2 |
| DC-57 | Crowdion in W (Peierls profile, polaron narrowing S_pol, FK mass, strain interaction with the parent vacancy) and Al ⟨100⟩ dumbbell / cluster 1D glide | W, Al | LE-134 (G-T6, L31); WP7-T-v2 §3.4 | QE fork: QE PBE 250-atom bcc CI-NEB + Hessians; MLIP-MD 10–100 K + instantons | /home/user/dmdd-solid/returns/R16/CW5.md §3.8; /home/user/dmdd-solid/returns/R12/WP7-T-v2.md §3.4 | to write | INF-7 | ≈ 10⁵ CPU-h per material; 2×10⁵ core-h (CW5 §3.8; WP7-T-v2 §3.4) | P3 |
| DC-58 | DM–TLS core vertex 𝔣^def_e(q) = ⟨R\|n_e(q)\|R⟩ − ⟨L\|n_e(q)\|L⟩ for real a-SiO₂ TLS (Method A: two SCFs; Method B: one Γ ph.x) | a-SiO₂ | LE-137 (replaces the rigid-ion f = Z_O = 8 in the DM–TLS rate, LIMITS 'Numbers carried') | QE fork: QE pw.x/ph.x 216-atom cells (rtsc layout) | /home/user/dmdd-solid/returns/R16/CW5.md §3.10 + CW5-errata A34 | /home/user/dmdd-solid/code/CW5/LE-137/{scf.in, ph.in, notes.txt} | DC-59 (NEB-identified TLS from MLIP glasses) | Method A ≈ 1 GPU-h per SCF, 10² TLS ≈ 2×10² GPU-h; Method B ≈ 10×; 200–2000 GPU-h (CW5 §3.10) | P3 |
| DC-59 | TLS ensemble sampling: landscape filtering / swap-MC on MLIP glasses (≳ 10⁸ minimum pairs), NEB, λ_P, γ^def, 𝐩^def; tls_response tables ΩS̄^def | a-SiO₂, AlOx, a-WSi | WP7-T-v2 §2.7 (TLS as DM targets, Ch 16); input of DC-58 | MD-MLIP: MLIP glasses (10³–10⁴-atom cells, ≳ 10⁴ quenches) + NEB + new tls_response module | /home/user/dmdd-solid/returns/R12/WP7-T-v2.md §2.7 | to write | INF-13, INF-9 | 10⁵–10⁶ GPU-h (sampling), < 10 CPU-h (tables); 10 core-h + 1×10⁵–1×10⁶ GPU-h (WP7-T-v2 §2.7) | P3 |
| DC-60 | Close-collision electronic excitation kernel dP/dω_e(b_imp, E_coll) for Si–Si, Ge–Ge collisions (E_coll 50 eV–5 keV) with the xc nuisance θ_LZ | Si, Ge | LE-140 (WP5 R3), WP5-v4 §3.4 electronic channel: G3 charge channel below E_R,th (Ch 19) | other: real-time TDDFT Ehrenfest (Qb@ll, Octopus or SALMON; QE has none) + HSE subset + surface hopping + MRCI Landau–Zener | /home/user/dmdd-solid/returns/R16/CW5.md §2.4; /home/user/dmdd-solid/returns/R13/WP5-v4.md §3.4 | to write | INF-8 | ≈ 10⁶ core-h; 1×10⁶ core-h (CW5 §2.4; WP5-v4 §3.4) | P2 |
| DC-61 | NR partition tables P(ℋ, E_st, N_eh \| E_R, r̂_R, T), anisotropic E_d(r̂_R) and P_FP, created-phonon spectra (WP5-AUD B-1), E_st with the quench protocol and one shared E^conf table (G-E3) | Si, Ge (then survivors: GAP:E_st1_p_surv, GAP:y_ion_QF) | WP5-v4 §3.4 (G3), LE-3/G-E3 (open as a computation), LE-5/LE-120 inputs; Ch 19 low-energy nuclear recoils | MD-MLIP: MLIP (ACE/MACE/NequIP on ~10⁴ PBE/SCAN configs, ZBL-spliced) MD; BO-DFT-MD check | /home/user/dmdd-solid/returns/R13/WP5-v4.md §3.4; /home/user/dmdd-solid/returns/R14/WP5-AUD.md §3.1 (protocol), §4 B-1 | to write | INF-7 | E_d ≈ 3×10⁴ MLIP runs ≈ 10³ GPU-h; check 20 directions BO-DFT-MD ≈ 10⁵ core-h; tables 10⁴–10⁵ GPU-h (per material); 2×10⁵ core-h + 2.2×10⁴–2×10⁵ GPU-h (WP5-v4 §3.4 (×2 materials [E-DC])) | P2 |
| DC-62 | Charge yield below E_R,th (B-2): P(N_eh \| E_R, r̂_R, T) on [20 eV, 1 keV], 𝔶(E_R), F_NR(E_R), P(N_eh = 0) | Si (validation 2303.02196), Ge (2405.10405) | LIMITS L43 (OPEN, B-2 not computed); LE-6 (G-R4); Ch 19 headline NR yield | MD-MLIP: MLIP-MD trajectories with stochastic excitation events from DC-60, converted by P_n(ω_e) of DC-63 | /home/user/dmdd-solid/returns/R14/WP5-AUD.md §4 B-2 + /home/user/dmdd-solid/returns/R16/CW5-errata.md A5 (≥ 1112 trajectories for 6%) | to write | DC-60, DC-61, DC-63 | not estimated in the source (trajectories inside the MLIP-MD budget); 1000–5000 GPU-h ([E-DC]) | P2 |
| DC-63 | Ab initio hot-carrier cascade: G₀W₀ bands, full-frequency ε⁻¹_GG′(p,ω) to 60–100 eV, ii kernel (W1′), EPW e–ph kernel, full-band cascade → P_n(q,ω,T), ε_eh, F_eh, decomposition (EF7) | Si, Ge, GaAs | WP5-v4 §2 (G1 closure) and the validation half of GAP-EF-v2 §5; GAP:F_eh, GAP:eps_eh (GaAs); qe-rtsc issue #1; Ch 18 ionization yield | BerkeleyGW-or-fork-GW: QE + BerkeleyGW (epsilon, sigma) or qe-rtsc GW path; EPW; INF-14 cascade solver | /home/user/dmdd-solid/returns/R13/WP5-v4.md §2; /home/user/dmdd-solid/returns/R16/GAP-EF-v2.md §5 + /home/user/dmdd-solid/returns/R16/GAP-EF-v2-errata.md R-13 | to write | INF-1, INF-4 (quadrupoles), INF-14 | per material: W^scr 10⁴–10⁵, ii kernel 10⁴–10⁵, EPW ≈ 10⁴ core-h (GAP-EF §5 quotes 10⁴–10⁵ per material in total); 9×10⁴–6.3×10⁵ core-h (WP5-v4 §2) | P2 |
| DC-64 | Ab initio ε_eh and F_eh for wide-gap and polar survivors (priority Al₂O₃, CaWO₄, LiF, NaF; then 4H-SiC F, C, 3C-SiC, GaN, AlN, TeO₂) | Al₂O₃, CaWO₄, LiF, NaF, 4H-SiC, C, 3C-SiC, GaN, AlN, TeO₂ | GAP-EF-v2 §5 'Recommendation' (no measurement exists; first ab initio F_eh would be new); EF-LIT GAP; qe-rtsc issue #1 priority table; Ch 17/18 | BerkeleyGW-or-fork-GW: as DC-63 + BSE for LiF/NaF excitons; SOC for W | /home/user/dmdd-solid/returns/R16/GAP-EF-v2.md §5 'Per material', 'Recommendation'; https://github.com/ytcs/qe-rtsc/issues/1 | to write | DC-63 (pipeline validated on Si), INF-1, INF-14, DC-68 (exciton parameters for halides) | oxides ≈ 10⁵ core-h each; LiF, NaF 10⁴–10⁵ each (+BSE); C, SiC, GaN, AlN ×2 of Si (2×10⁴–2×10⁵ each); 4.2×10⁵–1.5×10⁶ core-h (GAP-EF-v2 §5; qe-rtsc issue #1) | P2 |
| DC-65 | Energy dependence ζ(E) of the ii-rate ratio Γ_ii^NEGF/Γ_ii^(W1) (G₀W₀ Im Σ with and without Z_kn, + SOSEX) and its effect on F_eh through (EF7) | Si | LE-138 (CEG; WP5 R1) | BerkeleyGW-or-fork-GW: BerkeleyGW G₀W₀ full-frequency + SOSEX; GAP-EF solver | /home/user/dmdd-solid/returns/R16/CW5.md §2.2 + CW5-errata A15, §C | to write | INF-1, DC-63 | ≈ 3×10⁴ core-h; 3×10⁴ core-h (CW5 §2.2) | P3 |
| DC-66 | k-resolved osc_k m_k(E) and w_mem(E) for Si between 3 and 8 eV (bound (CW5-1) on the energy-only reduction) | Si | LE-139 (CEG; WP5 R2): θ_{R-k} bounded instead of estimated | EPW: k-resolved n_gen = 2 subset of DC-63 (EPW + GW rates) | /home/user/dmdd-solid/returns/R16/CW5.md §2.3 + CW5-errata §C | DC-63 outputs | DC-63 | not estimated in the source (≥ 200 k samples × ≥ 10³ cascades per bin); 1000–1×10⁴ core-h ([E-DC]) | P3 |
| DC-67 | Semi-analytic cascade library: P_casc(N \| x_e, x_h; θ) tables for every Λ-sector and survivor (cascade_gf.py), and the GAP-EF(-v2) rerun on ω₀-commensurate grids | 27–42 survivors | LE-153 (OW6-3, CW7 §4); IF-EW-1 (ω₀,eff quantisation bias +1.3% in Si ε_eh at h = 0.02); Ch 18 WP6 yield option | other: /home/user/dmdd-solid/code/CW7/cascade_gf.py; /home/user/dmdd-solid/code/GAP-EF-v2/{cascade,model,predict}.py | /home/user/dmdd-solid/returns/R16/CW7.md §4; /home/user/dmdd-solid/returns/R17/WP8-errata.md §14 / IF-EW-1 | ready (code exists) | none | seconds per material and θ; minutes on the box for 5 θ × 27 survivors; <1–1 core-h (CW7 §4) | P2 |
| DC-68 | Exciton and capture parameter set: G₀W₀+BSE E_x^b, a_x, oscillator strengths; D⁰X/A⁰X central-cell DFT; cascade-capture σ_cap(E,T,ℰ_b) with EPW rates; deep-level multiphonon capture; the CW5 rate set {k_FX, k_FT, k_XB,j, k_B↓,j, η_X, η_B,j, C_X, γ_XX, C_A(mK)} | Si, Ge (then LiF, NaF, Al₂O₃, CaWO₄) | LE-141 (CEG: missing input = a rate set), LE-14 (IF-E9), WP7-E-v3 G-E10 and §7 Traps; GAP:E_x_b (36 materials); Ch 18 gap-energy heat | BerkeleyGW-or-fork-GW: BerkeleyGW/Yambo GW+BSE (double-grid, 10⁴–10⁵ k for Si/Ge); QE 216 → 512-atom defect cells; EPW | /home/user/dmdd-solid/returns/R16/GAP-EF-v2.md §4.3; /home/user/dmdd-solid/returns/R16/CW5.md §2.5 + CW5-errata §C (LE-141); /home/user/dmdd-solid/returns/R12/WP7-E-v3.md §7 (Traps) | to write | INF-1 | BSE 10³–10⁴ core-h (semiconductors), 10⁴ (oxides); capture ~10⁵ CPU-h per material; 6.4×10⁵–6.6×10⁵ core-h (GAP-EF-v2 §4.3; WP7-E-v3 §7 (6 materials [E-DC])) | P2 |
| DC-69 | Event-level charge/exciton kinetics: exciton/EHD rate equations, drift–trap transport with history n_j(t), athermal emission, μ_F-referenced E_trap, E_es; windowed Y_H(t_win) and η^φ_NR tables | Si, Ge | WP7-E-v3 §7 (Exciton/EHD kinetics, Drift–trap transport, Windowed partition); Ch 18–20 | CMPMC: CMPMC transport_charges (P5, P6) + new exciton module (INF-11) + trap kinetics (DESIGN_NOTES §5) | /home/user/dmdd-solid/returns/R12/WP7-E-v3.md §7; /home/user/cmpmc/DESIGN_NOTES.md §5 | to write | INF-10 (item 5), INF-11, DC-68, DC-61, DC-81 | ≲ 10³ CPU-h per set; 1000–1×10⁴ core-h (WP7-E-v3 §7 (sets [E-DC])) | P2 |
| DC-70 | Dense tracks: EMC-MD with P³M Coulomb among carriers (θ_dense, ΔF_NR) and MLIP-MD + two-temperature model for Ge thermal spikes | Si, Ge | LE-142 (WP5 R8) | MD-MLIP: EMC-MD (P³M) + MLIP-MD + TTM (g_ep from EPW) | /home/user/dmdd-solid/returns/R16/CW5.md §2.6 | to write | INF-7, DC-63, DC-72 (cascade cells) | ≈ 10⁴ GPU-h (MD) + 10³ CPU-h (EMC); 1000 core-h + 1×10⁴ GPU-h (CW5 §2.6) | P3 |
| DC-71 | Track recombination and the plasma phase: drift–diffusion–Poisson with Auger, exciton formation and SRH on the track geometry; f_A(E_R, ℰ_b), plasma time, Ramo delay | Si, Ge | LE-146 (G-E5) | other: 2D axisymmetric drift–diffusion–Poisson FEM (mesh ≤ 1 nm) | /home/user/dmdd-solid/returns/R16/CW5.md §4.3 | to write | DC-68 (exciton rates), DC-72 (track geometry) | ≲ 10³ CPU-h; 100–1000 core-h (CW5 §4.3) | P3 |
| DC-72 | Amorphous-pocket size distribution P(N_a \| E_R, r̂_R) and recrystallisation barrier spectrum from MLIP cascades | Si, Ge | LE-148 (G-E8): visible LEE rate ℛ_vis (WP7-E-v3 (b′)); Ch 19/20 | MD-MLIP: MLIP-MD (ZBL-spliced) 10⁵–10⁶ atoms, 10–50 ps; NEB/accelerated MD on 10² pockets | /home/user/dmdd-solid/returns/R16/CW5.md §4.5 | to write | INF-7, DC-61 (quench protocol) | ≈ 10⁴–10⁵ GPU-h; 1×10⁴–1×10⁵ GPU-h (CW5 §4.5) | P3 |
| DC-73 | Ionic targets and colour centres: STE and F–H adiabatic surfaces (constrained hybrid DFT), p_FH(T) at mK, p_surv of close F–H pairs, E_d(r̂) of the anion sublattice, F-band cross sections | LiF, NaF, MgO, LiH (NaI shares the method) | LE-144 (CEG, two steps), LE-151 (CEG, two steps), WP7-B2-v2 §9 (D2); Ch 16/19 | QE fork: QE HSE/PBE0 ΔSCF (64 → 216 atoms) + decoherence-corrected FSSH + MLIP/DFT MD + kMC + BSE | /home/user/dmdd-solid/returns/R16/CW5.md §4.1 + CW5-errata §C (LE-144, LE-151); /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §9 | to write | INF-7, INF-1 (BSE) | ≈ 10⁵ CPU·h (STE → F–H surface hopping) per material; 1×10⁵–3×10⁵ core-h (WP7-B2-v2 §9 (materials [E-DC])) | P3 |
| DC-74 | Low-energy-excess model inputs: FEM cooldown stress U_el per component with (Γ_min, Γ_max); cured-epoxy and interface MLIP event-energy law; avalanche branching b_br by KMC on the release catalogue driven by phonon-MC pulses | Si/Ge crystals in holders with glue | LE-145 (CEG, two steps), LE-131 (CEG, b_br), WP8-F G-F3 (no predictive LEE rate); Ch 20 low-energy excess | other: FEM (thermo-elastic) + ACE/NequIP epoxy MLIP (10⁶ atoms) + KMC + CMPMC phonon pulses | /home/user/dmdd-solid/returns/R16/CW5.md §3.5, §4.2 + CW5-errata §C (LE-131, LE-145) | to write (C_ij(T), α(T) data for crystal, glue, holder) | INF-10 (CMPMC transport), DC-56 (catalogue) | not estimated in the source; 100–1000 core-h + 1000–1×10⁴ GPU-h ([E-DC]) | P2 |
| DC-75 | Mark sufficiency test of (H-E6): ΔP between full and mark-resampled microstates | Si | LE-149 (CEG) | CMPMC: DC-69 event simulation with common random numbers | /home/user/dmdd-solid/returns/R16/CW5.md §4.6 + CW5-errata A32, §C | to write | DC-69 | 2×10⁴ trajectories per seed class (no CPU estimate in the source); 100–1000 core-h ([E-DC]) | P3 |
| DC-76 | Athermal emission Γ^em_j (phonon ionisation of D⁰/A⁰ and H⁻-like D⁻/A⁺, impact ionisation σ_ii(u)) and space-charge nonlinearity ξ_SC(t) over an exposure history | Si, Ge | LE-122 (CEG; G-E6, L33, L34) | CMPMC: closed-form effective-mass cross sections + QE 216-atom Si:P central cell + CMPMC trapping extended by DESIGN_NOTES §5 + run-sequence driver | /home/user/dmdd-solid/returns/R16/CW6.md §6 + /home/user/dmdd-solid/returns/R16/CW6-errata.md (§6 replacement row) | to write (rtsc layout for the central cell) | INF-10 (item 5) | (1) and (3) minutes; central cell ≈ 10³ CPU-h; item 5 ≈ 1 week implementation; 1000 core-h (CW6 §6) | P3 |
| DC-77 | Bond breaking in molecular solids: S_int, S_CM, cage-escape p_esc by MLIP MD (10³ trajectories per (E_int, r̂)) | molecular crystals (D5) | WP7-B2-v2 §10 (D5); LE-151 D5 half | MD-MLIP: Morse/ab initio potentials, phonopy/PIMD, MLIP MD | /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §10 | to write | INF-7 | ≈ 10³ CPU·h; 1000 core-h (WP7-B2-v2 §10) | P3 |
| DC-78 | Collection kernels 𝒦_1, 𝒦_2(f; r_ev) for a stated geometry, then ζ_O, ζ_gap, σ_pos, r_coll by (CW6-1) | Si 1×1×0.4 cm (2012.12430, two TES arrays); 1-cm CDMS-like Ge cylinder | LE-118 (G-R1; IF-R4: route (d) needs ζ_O ≥ 0.24 at σ_pos = 0.05); WP8-R-v2 G-R1; Ch 20 sensors | CMPMC: CMPMC main ≥ 3d43a02: transport (Octahedral kinematics, P1/P2 decay, P8 surfaces with campaign p_spec/p_diff/p_anh, KaplanFilm subgap_absorption = 0), transport_charges (P5, P6) | /home/user/dmdd-solid/returns/R16/CW6.md §2 + /home/user/dmdd-solid/returns/R16/CW6-errata.md A15 | to write (geometry from 2012.12430 App. A; isotropic AMM table of WP8-R-v2 §3.2 until item 2) | INF-10 (DESIGN_NOTES items 1, 2 for full validity); DC-83 (gate) | box first pass 1-D depth grid at 10³ phonons/cell ≈ 0.44 h; 10⁴ per cell ≈ 4.44 h; full 3-D ≈ 35.6 h on 4 threads (per geometry); 4–285 core-h (CW6-errata A15) | P2 |
| DC-79 | Gap-energy release site–spectrum: exciton diffusion π_ℓ(z,t) with surface loss S_surf, per-channel spectra s_ℓ(f), then ζ_gap and its timing distribution | Si, Ge | LE-119 (CEG: two missing inputs); θ_gap if timing is used; Ch 20 | CMPMC: 1-D implicit finite-difference exciton diffusion + CMPMC transport with time-tagged sources | /home/user/dmdd-solid/returns/R16/CW6.md §3 + CW6-errata (§3 replacement row) | to write | DC-68 (rates), DC-78 (kernels), INF-11 | diffusion solve seconds; transport = DC-78 kernels (no new run); 0–1 core-h (CW6 §3) | P3 |
| DC-80 | Created-phonon spectra (WP5-AUD B-1) propagated to the sensors: ΔO_obs(t) and arrival spectra for ER and NR at E_R ∈ {50, 100, 300, 1000} eV; Δ_soft in (CW6-2) | Si (then Ge) | LE-120 (G-R3): f_s and the NR optical share are [E] until run; Ch 20 | CMPMC: convolution with DC-78 kernels; direct check with CMPMC transport after DESIGN_NOTES §7 | /home/user/dmdd-solid/returns/R16/CW6.md §4 | B-1 tables from DC-61; kernels from DC-78 | DC-61, DC-78; INF-10 (item 7) for the direct check | convolution negligible; direct CMPMC check ≈ 10⁸ steps per seed set (minutes); <1–1 core-h (CW6 §4) | P2 |
| DC-81 | Collection efficiencies ϵ_prim^NR, ϵ_prim^ER, ϵ_NTL, ϵ_gap and hence δ_coll (CW6-3), r_coll for the 1803.02903 Si ZIP and the 1805.09942 Ge iZIP | Si, Ge | LE-121 (G-E4, IF-E7, IF-R3): separates E_st from collection in η^φ_NR = 0.952 and f_DF (L38 degeneracy); Ch 19/20 | CMPMC: CMPMC transport_charges (P5, P6), transport, KaplanFilm, ElectrodeFilm/BulkDebye release with explicit μ_F; Geant4 source maps (external) | /home/user/dmdd-solid/returns/R16/CW6.md §5 + CW6-errata A6–A7 | to write (QET coverage from the CDMS II design; source maps) | INF-10 (item 2); item 3 done in CMPMC-DEV c43569b; DC-78 | ≈ 10¹¹ steps ≈ 2 h on 4 threads per geometry; 16 core-h (CW6 §5) | P2 |
| DC-82 | Anisotropic welded AMM t_ν(θ,φ) for Al(111)/Si(001) and W/Si with thin-film interference; τ_l(ω) for d = 40–600 nm (film elastic constants from DFT or [FT]) | Al/Si, W/Si | LE-123 (RG7, L40); CMPMC DESIGN_NOTES §2; Ch 15/20 | CMPMC: CMPMC interface_transmission (anisotropic upgrade) + KaplanFilm (CW6-4); QE vc-relax strain–stress for Al | /home/user/dmdd-solid/returns/R16/CW6.md §7; /home/user/cmpmc/DESIGN_NOTES.md §2 | Al, Ir C_ij [FT] in /home/user/dmdd-solid/state/DATA-ADDENDA.csv; QE inputs: to write | INF-10 (item 2) | small (box-runnable); Al elastic constants ≈ 0.5 h box; 2–10 core-h (CW6 §7) | P3 |
| DC-83 | Kaplan-buffer recheck of R15-era CMPMC numbers at CMPMC main ≥ 3d43a02 (fix f61d710): CMPMC-AUD T8 η_pb (no loss 4.5Δ, 6Δ, 10–100Δ; 600 nm film 3, 5, 10, 40Δ; surrogate cavity), T11 benchmark energy closure, IF-AUD-5 NTL ⟨E_Luke⟩ | Al film on Ge/Si (CMPMC presets) | IF-DEV-5 (buffer silently dropped entries above ~130Δ; closure checks blind); numbers quoted in WP8-R-v2 §3.3, L41, AUD-L4, IF-AUD-2; prerequisite gate for every CMPMC [CALC] | CMPMC: CMPMC ctest (test_kaplan, test_pair_breaking, test_luke_ntl) + examples/phonon_benchmark | /home/user/dmdd-solid/returns/R16/CMPMC-DEV.md §3 (f61d710), IF-DEV-5; /home/user/dmdd-solid/returns/R15/CMPMC-AUD.md §1.4, §2 T8/T11, IF-AUD-2, IF-AUD-5 | ready: /home/user/dmdd-solid/code/CMPMC-AUD/tests/, /home/user/dmdd-solid/code/CMPMC-AUD/out/sota/ (R15 reference output to diff), /home/user/cmpmc/tests/ | none | tests ≤ 15 s each; benchmark 5000 events minutes on 4 threads; <1–1 core-h (CMPMC-AUD §2 (test times)) | P1 |
| DC-84 | Coherent-field regime inputs: GIPAW shielding/EFG, E*_I; elastic and piezoelectric tensors (DFPT) for BAR modes; dln a/dln α and dln a/dln m_e from scaled-constant DFT; multiferroic LSWT/TDDFT+SOC (T ≪ T_CM) | NMR (CASPEr) targets, BAR quartz/sapphire, multiferroics | WP7-D-v2 §1.10 (S4, S9, A9, §10(ii)); Ch 16/21 coherent detection | QE fork: QE GIPAW, ph.x elastic/piezo, scaled-constant DFT; new LSWT/TDDFT+SOC module | /home/user/dmdd-solid/returns/R12/WP7-D-v2.md §1.10 | to write | none (multiferroic LSWT/TDDFT+SOC module is new code) | seconds per (m_φ, t_int) once tabulated; DFT 10²–10⁴ core-h; multiferroic ~10³ core-h; 100–1×10⁴ core-h (WP7-D-v2 §1.10) | P3 |
| DC-85 | Fermionic absorption χ + target → ν̃ + excitation: all-electron S_nn, S_{J_TJ_T} along ω = m_χ − q for m_χ ∈ [E_g, 1 MeV] (spin-orbital convention fixed in the table header) | Si, Ge (crystals); atoms by DHF | WP7-D-v2 §2.6 (A10); Ch 16 | other: DHF orbitals (q ≳ m_e/3) + high-q all-electron PAW (crystals); WP2 L6 S^GS for nuclei | /home/user/dmdd-solid/returns/R12/WP7-D-v2.md §2.6 | to write | INF-6 | nuclei negligible; electrons 10⁴–10⁵ core-h per crystal; 2×10⁴–2×10⁵ core-h (WP7-D-v2 §2.6 (2 crystals [E-DC])) | P3 |
| DC-86 | Two-insertion processes: pair absorption S_OO(k ≈ 0, 2m_χ) with 𝔇^pair, dark Compton (J^(sh)(p_z), n_r), Barkas term with an HEG R^(2) + LDA map | Si, Ge, electron gas | WP7-D-v2 §3.7 (A11, §11.9); Ch 16 | other: new R^(2) module (HEG quadratic response + LDA) + L9b tables | /home/user/dmdd-solid/returns/R12/WP7-D-v2.md §3.7 | to write | DC-14 (L9b-type tables) | minutes; R^(2) 10² core-h; 100 core-h (WP7-D-v2 §3.7) | P3 |
| DC-87 | Halo-independent directional bound (G8′): stream matrix 𝔎_i(w_k) on 768 HEALPix × 100 speeds × 24 phases and the LP per m_χ (HiGHS) | Si, Ge (any q̂-resolved library) | LE-152 (OW6-1): conservative halo-independent bound for directional responses (Ch 21) | other: GPU sweep over the q-vector-resolved library + HiGHS LP | /home/user/dmdd-solid/returns/R16/CW7.md §3 + CW7-errata §1.3 | q̂-resolved S(q,ω;Λ) from DC-1/DC-15 (nosym nscf on the full zone) | DC-1, DC-15 | ≈ 2×10¹² multiply-adds per m_χ (a GPU job); LP seconds; 0–1 core-h + 10–100 GPU-h (CW7 §3 (GPU-h [E-DC] for ≈ 50 masses)) | P3 |
| DC-88 | Scalar-absorption kinetic row: Im R⁰_𝒯𝒯(0,ω) (direct kinetic route + PAW one-centre correction), then RPA+LFE R̃_𝒯𝒯 | Si (box), 10-atom oxides (fork) | LE-155 (G-F1, WP8-F scalar row); Ch 16/17 | QE fork: rtsc/bench scf → dense nscf (≥ 24³) → matrix elements | /home/user/dmdd-solid/returns/R16/CW7.md §6 | to write | none | Si-size cells minutes on the box; 10-atom oxides ≈ 1 GPU-hour each on the fork; <1–1 core-h + 5–10 GPU-h (CW7 §6) | P3 |
| DC-89 | Cosmogenic sea-level production rates per nuclide (ACTIVIA; Geant4 Shielding or TALYS for ³H, ⁷Be) and sub-keV rate density with EC line fractions | 34 survivors without measured rates (all but Si, Ge, NaI, Te) | LE-177; GAP:cosmo_production (34), GAP:S4_cosmo (35); WP8-S-v2 §6 item 5 (b_bg for the background-limited ranking, Ch 17) | other: ACTIVIA + Geant4 10⁸ primaries | /home/user/dmdd-solid/returns/R16/CW7.md §11 | compositions and isotopic abundances: /home/user/dmdd-solid/returns/R16/WP8-U-table-v4.csv; code: to set up | none | ACTIVIA seconds per material; Geant4 10⁸ primaries ≈ 1–3 CPU-h per material; 34–102 core-h (CW7 §11) | P2 |
| DC-90 | Spin-dependent nucleon FOM class (G-F6): per-isotope ⟨S_p⟩, ⟨S_n⟩ from ≥ 2 shell-model interactions and the incoherent SD one-phonon response from DFPT partial DOS D_κ(ω) | odd-A isotopes of the survivors | WP8-F-v3 G-F6 (two missing steps); Ch 17 | QE fork: shell-model codes (external) + qe-rtsc scf → ph.x → matdyn projected DOS | /home/user/dmdd-solid/returns/R16/WP8-F-v3.md §7 (G-F6) | isotope list: v4 `isotopes[El]` rows of /home/user/dmdd-solid/returns/R16/WP8-U-table-v4.csv | DC-91, DC-95 (DOS) | not estimated in the source; 10–100 core-h ([E-DC]) | P3 |
| DC-91 | Small-cell survivor Γ-DFPT batch: relax, ε_∞, ε₀ (dynmat.x), Z*, ω_TO, ω_LO, then ph 4³ → 6³ for slopes, sound speeds, ω_max, phonon DOS | C, 3C-SiC, GaAs, LiF, NaF, 4H-SiC, Al₂O₃ | COMP-PH survivor batch 'specified, not run' (brief); LE-16 small-cell part; GAP:Zstar_tensor, eps_0_DFT_vetted (3C-SiC failed IR run), phonon_DOS cells; inputs for DC-8, DC-28, DC-64 | QE fork: pw.x → ph.x (epsil) → dynmat.x, q2r.x, matdyn.x (rtsc/bench layout) | /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.1 | /home/user/dmdd-solid/code/COMP-PH/formulated/{C,SiC-3C,GaAs,LiF,NaF,SiC-4H,Al2O3}/{relax,scf,phG,ph,q2r,matdyn}.in (cutoffs: C 100, 3C 90, GaAs 140, LiF 90, NaF 90, 4H 90, Al₂O₃ 100 Ry) | none | 2-atom cells 0.3–1.5 h each, 4H-SiC 10–20 h, Al₂O₃ 30–60 h on this box, ≤ 6 GB (≈ 170–350 core-h); GPU fork: minutes to ~1 h each; 170–350 core-h + 1–7 GPU-h (COMP-PH §6.1) | P2 |
| DC-92 | CaWO₄ and Li₂MoO₄ dielectric and lattice data: ε₀, ε_∞, Z* tensors, ω_TO/ω_LO mode sums (ω_T,min), elastic tensors, sound speeds, θ_D, ω_max, n_e/ω_p | CaWO₄, Li₂MoO₄ | brief 'owed data' item; GAP:eps0_omegaLO_TO, eps_0, Z*, Zstar_tensor, omega_L/T, c_dir, c_sound, theta_D, omega_max (Li₂MoO₄ ranked only in Migdal; CaWO₄ POL row empty); WP8-S-v2 §6 item 4 | QE fork: QE pw.x/ph.x (W semicore; SOC check for W), dynmat.x, strain–stress | /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.1 recipe applied to these cells; /home/user/dmdd-solid/returns/R16/WP8-S-v2.md §6 item 4 | to write (scale from /home/user/dmdd-solid/code/COMP-PH/formulated/Al2O3/) | none | not estimated in the source (CaWO₄ 6 atoms primitive, Li₂MoO₄ 42 atoms rhombohedral); 1200–5400 core-h ([E-DC] scaled from COMP-PH §6.1 (Al₂O₃ 30–60 h)) | P2 |
| DC-93 | CsI elastic constants C₁₁, C₁₂, C₄₄ (finite strain or DFPT) to replace the [E] B-floor model | CsI | brief 'CsI elastic constants'; WP8-errata §4 (1910.10716 c_LA lies below the bulk-modulus floor; CsI leads the 42-pool NR-heavy row on an [E]-driven model, FOM 3.89); WP8-S-v2 §6 item 2 | QE fork: QE vc-relax + strain–stress (2-atom CsCl cell) | /home/user/dmdd-solid/returns/R17/WP8-errata.md §4, §3 item 2; method as /home/user/dmdd-solid/returns/R16/CW6.md §7 (strain–stress) | to write | none | box (2-atom cubic cell); not estimated in the source; 2–10 core-h ([E-DC]) | P2 |
| DC-94 | Magnetic survivors' dielectric and lattice data by DFT+U DFPT: ε₀, ε_∞, Z*, ω_TO/ω_LO, elastic tensors (positive-definite), θ_D, ω_max | YIG, NiO, MnO, Cr₂O₃, NiPS₃ | brief 'YIG and the magnets'; GAP:eps_0, eps_inf, Z*, omega_L/T, c_dir (MnO DB tensor not positive definite), theta_D, omega_max; YIG a now [DB] 12.3750 Å (DATA-ADDENDA) | QE fork: QE DFT+U (hp.x) ph.x; magnetic cells | no dedicated spec; recipe of /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.1 with DFT+U; WP8-U-v3 §4 GAP rows | to write (YIG a from /home/user/dmdd-solid/state/DATA-ADDENDA.csv) | DC-44 (U and magnetic ground state) | not estimated in the source (YIG 80-atom primitive dominates); 1.1×10⁴–1×10⁵ core-h ([E-DC]) | P3 |
| DC-95 | Remaining survivors' DFPT batch for DFT-fillable GAP cells: Z* tensors, ε₀ (vetted), ω_T/ω_L, phonon DOS, directional sound speeds, ω_max | NaI, NaCl, CsI (dielectric), MgO, MgF₂, CaF₂, ZnO, ZnS, GaN, AlN, GaSb, SiO₂-q, TeO₂, LiAlO₂, SrTiO₃, PbTe, PbS, PbSe, Bi₂Se₃, ZrTe₅, SiC-6H, cBN, hBN | WP8-U-table-v4 GAP cells (GAP:Zstar_tensor 33, phonon_DOS 38, omega_L 25, omega_T 20, eps_0_DFT_vetted 12, c_dir 7); WP8-S-v2 §6 item 4 (ω_T,min for TeO₂, h-BN, SiO₂-q, MgF₂) | QE fork: QE pw/ph/dynmat/matdyn (rtsc/bench layout) | recipe of /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.1; vetting rule WP8-U-v3 V2/V5′ | to write | none | not estimated in the source; 1000–5000 core-h ([E-DC] scaled from COMP-PH §6.1) | P3 |
| DC-96 | Phonon lifetimes (three-phonon linewidths) for the survivors | 35 survivors (GAP:ph_lifetime) | WP8-U GAP:ph_lifetime; phonon memory loss (WP8-R-v2 §2.5: Al₂O₃ mixing hypothesis fails; CMPMC 𝒜_anh inputs) | other: phono3py fc3 on QE supercells (or MLIP fc3) | no dedicated spec; method of /home/user/dmdd-solid/returns/R16/CW2.md §12 (fc3) and /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §1 (3×3×3 fc3, 10³–10⁴ CPU·h) | to write | INF-12, DC-91/94/97 | 10³–10⁴ CPU·h per material (WP7-B2-v2 §1 scale); 3.5×10⁴–3.5×10⁵ core-h ([E-DC] from WP7-B2-v2 §1) | P3 |
| DC-97 | Per-survivor PAER/ZPL window inputs: E_min(q), band masses m_eff, ω_TA(Q*) and EPW-class g at Q* (GW/HSE where PBE fails) | 36 survivors (GAP:E_min_q, GAP:EPW_g_omegaTA_Qstar, GAP:m_eff) | WP8-U GAP cells; WP8-F G-F5 for survivors beyond Si/Ge; window FOM Δm/m in Ch 17. The v4 table still lists Si and Ge under GAP:E_min_q: Si is filled from COMP-PH/COMP-PAER [CALC] with no new run, Ge once DC-4 and DC-2 land | QE fork: COMP-PAER window pipeline (window.py, paedge.py) + COMP-PH emin.py; HSE/G₀W₀ where the PBE band order fails | method of /home/user/dmdd-solid/returns/R15/COMP-PAER.md §1, §4 and /home/user/dmdd-solid/returns/R15/COMP-PH.md §4 | to write per material; scripts in /home/user/dmdd-solid/code/COMP-PAER/scripts and /home/user/dmdd-solid/code/COMP-PH | DC-91/94/96/97 (phonons); DC-2 route for PBE-failing cells | Si window run 12.7 min DFPT + 1.5 min nscf (box); not estimated per material; 100–1000 core-h ([E-DC] scaled from COMP-PAER §2 job 3) | P3 |
| DC-98 | Integrated thermal contraction ∫Δα_th dT (300 K → mK) by quasi-harmonic DFPT | 38 survivors (GAP:alpha_th_integral) | WP8-U GAP:alpha_th_integral (cooldown stress input of DC-74 and the WP8-F property list) | QE fork: QHA: DFPT at ≈ 5 volumes per material (phonopy-qha) | no dedicated spec; WP8-U-v3 §1.3 property list | to write | DC-91/94/96/97 | not estimated in the source; 5000–2.5×10⁴ core-h ([E-DC] ≈ 5× the DFPT batches) | P3 |

## 2. Items

### A. Electronic sector and PAER

#### DC-1. Si PAER loss function L^PA(q,ω) from the full (M.1) amplitude, then rate dℛ/dω and reach σ̄_e^95 (tier H, T6) (Si; P1)
- **Physics.** Phonon-assisted electron recoil in the Si window 0.333–0.407 MeV (PAER onset 0.3332 replica / 0.3374 free pair; first zero-phonon edge 0.405–0.408, best 0.407, a glide-class state with small vertex; the allowed-size (2̄00) X-face edge ≈ 0.50 MeV is a distinct quantity), where PAER is the only electron-recoil channel; the amplitude is second order (one density vertex, one e–ph vertex) with all four time orderings and unrestricted intermediate bands.
- **Quantity and units.** L^PA(q,ω) dimensionless per (|q|, q̂, ω) bin, |q| 0.25–1.25 Å⁻¹ (step 0.05, 30 directions in the C₄ᵥ wedge), free-pair amplitude from E_g+ω_TA(Q*) to E_min(q) − δ_w; the replica shell 0.3332–0.3374 MeV comes from the E.15 exciton envelope × the same amplitude, matched at E_g+ω_TA; rate in events kg⁻¹ yr⁻¹ per σ̄_e (cm²); reach σ̄_e^95 (cm²) at 1 kg·yr, 3 events.
- **Method and approximation level.** τ = nB=0|ng=2|X=RPA+LFE|K=1ph; PBE + scissor (+0.613 eV) bands, DFPT g in the Wannier gauge with the O(Q) part kept (ASR on the dynamical matrix only), dynamical quadrupoles in the long-range g, Wannier ρ_mn(k,q) on the same U(k), Sternheimer remainder (a correction below |q| ≈ 0.5 αm_e ≈ 1.9 keV, carried in full on the 1.9–2.5 keV bins), pair term W^scr(P,ω_f)𝔗 at P ≈ 0.85X, tetrahedra on 60³→120³ pocket grids, σ → 0. Code: QE fork (pw/ph) + EPW + new stages 5–6 (rtsc/sth Sternheimer) + RPA+LFE ε̃⁻¹ (Yambo/BerkeleyGW or Route S).
- **Convergence and acceptance.** 5% in L per (q,ω) bin; δ_pair, δ_LF reported separately; band interpolation ≤ 10 meV to +10 eV; N_W 18 → 26; Wannier vs direct ρ ≤ 2% at 5 off-grid k; g(Q*) vs direct ph.x ≤ 5% at 3 off-grid Q. CONTROLS C1 (|q| = 10⁻³ Å⁻¹ vs EPW indabs and Macfarlane 20 K α), C2 (g → 0 flag), C4 (f-sum + non-local term, extrapolated in N_m; IF-CP-4), C5 (already PASS), C6 (8-atom frozen phonon at X, ±0.005 Å vs (M.12)), C7a–e (|Q| = 10⁻²…10⁻⁴·2π/a, 3 directions), on-axis LA zero (G′ = 0) and LO zero (2̄00).
- **Pitfalls.** g and ρ must share one gauge U(k) or the m-sum acquires random phases; never zero g at Q → 0 (ASR only on D); 4³ DFPT puts ω_TA(0.85X) ≥ ω_TA(X) (IF-CP-5: use ≥ 6³, here 8³); the [E] 𝔉_ρ proxy is not a lower bound on the computed L; the edge region 0.333–0.35 MeV has an exponentiated threshold error.
- **Result goes to.** Ch 13 (window, rate, reach; T5/T6); returns: supersedes COMP-PAER §5–6 and LIMITS L8-N2; DONE M1 tier H; state/SOTA C8 row; feeds DC-6 (ϖ_II) and DC-87 (q̂-resolved library).
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R15/COMP-PAER.md §8 (stage table, controls, cost); WP3 formulas /home/user/dmdd-solid/returns/R8/WP3-v3.md §M10, (M.1), (M.13)–(M.14), (M.18) · inputs: /home/user/dmdd-solid/code/COMP-PAER/tierH/Si/{scf,ph,nscf,epw}.in (stages 1–4 ready); stages 5–6: to write (INF-2, INF-3); quadrupole.fmt: to write (INF-4) · depends: INF-2, INF-3, INF-4, INF-1 (ε̃⁻¹ with LFE); DC-17 (δ_LF, δ_pair envelope) feeds the pair/LFE term.

#### DC-2. Ge zero-phonon kinematic edge E_min^ZPL(q), PAER edge and window m_χ^PA, m_ZPL (HSE06+SOC Wannier bands) (Ge; P1)
- **Physics.** The Ge PAER-only band lies between the PAER edge (E_g + ω(Q*)) and the first reachable zero-phonon state at the L valleys; PBE without SOC puts Γ below L (FAILED-CONTROL), so only hybrid+SOC bands give the edge.
- **Quantity and units.** E_min^ZPL(|q|) in eV on |q| = 0.40–2.00 keV (step 0.02), five q̂; m_χ^PA, m_χ^ZP (MeV, 10⁻⁴ resolution); window FOM Δm/m.
- **Method and approximation level.** HSE06 (ecutfock 160 Ry, nqx 4³), noncollinear SOC, Ge_ONCV_PBE_FR-1.0.upf, 8³ full grid nosym; 16 spinor sp³ WFs, 20 d bands excluded, frozen window VBM+3 eV; emin.py with spinor nv = 8; phwin.py with the Ge IFCs. Code: QE fork (pw.x HSE06 noncollinear SOC) + Wannier90 + code/COMP-PH/{emin,phwin}.py.
- **Convergence and acceptance.** Control (pre-registered): L below Γ, E_g(L) within 0.1 eV of 0.744 eV before scissor; E_dir 0.89 eV; anchor m(|K_pk|) analogous to Si C18; CONTROLS C5 kinematics.
- **Pitfalls.** A scissor on PBE bands cannot repair the L/Γ order; Wannier residual at the CBM sets a ±5 meV floor on E_min; q̂ set of five directions is an upper bound on min_q̂.
- **Result goes to.** Ch 13 Ge window; WP6-v3 (3.1′) Ge edges; LIMITS (COMP-PH 'Ge PAER edge GE_LIMITS' placeholder row); WP8-U GAP:E_min_q (Ge).
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.2; /home/user/dmdd-solid/returns/R15/COMP-PAER.md §9 (window as §4, classes L valleys, C₃ᵥ) · inputs: /home/user/dmdd-solid/code/COMP-PH/formulated/Ge-HSE-SOC/{scf.in, Ge.win, pw2wan.in} (fill @VBM_PLUS_…@ from scf.out); Ge force constants from DC-4 · depends: DC-4 (Ge 6³ phonons for ω_ν(Q*)); no new code.

#### DC-3. Ge PAER tier H rate and reach (as DC-1 with SOC and L-valley classes) (Ge; P2)
- **Physics.** As DC-1 for Ge: L-valley pockets, all branches allowed, plus the Γ-valley direct channel above ≈ 3 MeV only.
- **Quantity and units.** As DC-1 (L^PA, rate, σ̄_e^95) on the Ge window from DC-2.
- **Method and approximation level.** e–ph from PBE at the HSE-corrected band order; target E_g(0) = 0.744 eV (L), E_dir 0.89 eV; otherwise DC-1. Code: QE fork + EPW (SOC, 36 WFs) + stages 5–6 + HSE06 or G₀W₀ band corrections.
- **Convergence and acceptance.** DC-1 controls C1 (Macfarlane Ge indirect edge, to be fetched), C2, C4, C6, C7; band order control of DC-2.
- **Pitfalls.** SOC doubles the basis and ×4–8 the DFPT stage; Γ₈⁺ hole needs SOC; Ge 3d semicore in valence (14 e).
- **Result goes to.** Ch 13 Ge; LIMITS new Ge row; WP8-F G-F5 (Ge).
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R15/COMP-PAER.md §9 · inputs: /home/user/dmdd-solid/code/COMP-PAER/tierH/Ge/{scf,ph,nscf,epw}.in (ready: FR-1.0, SOC, 60 Ry, k 12³, q 8³, 120 spinor bands) · depends: DC-2 (quasiparticle band order), DC-1 (pipeline validated on Si), INF-2, INF-3, INF-4.

#### DC-4. Ge DFPT on a 6³ q grid, and the Ge results COMP-PH left as placeholders (GE_TABLE, GE_WIN, GE_INS, GE_WTA, GE_MPAER, GE_AXIS, GE_CTRL, GE_QCONV, GE_K) (Ge; P1)
- **Physics.** Ge acoustic branches set the PAER edge E_g + ω_TA(Q*); the INS comparison is the pre-registered phonon control.
- **Quantity and units.** ω_ν at Γ, X, L (THz/meV) vs Nilsson & Nelin PRB 3, 364 (1971); ω_TA(Q*) (meV) on the window grid; q-grid convergence Δω_TA(Q*) (meV).
- **Method and approximation level.** PBE, SG15 Ge_ONCV_PBE-1.2 (3d in valence), 80 Ry, a_exp, DFPT 6³ → q2r → matdyn asr='crystal'. Code: QE 7.6 ph.x/q2r/matdyn (box) + code/COMP-PH/{chain,phwin,gamma}.py.
- **Convergence and acceptance.** Tolerance fixed in COMP-PH §1: ω_TA(Q*) change ≤ 0.3 meV between 4³ and 6³; INS 5% at Γ/X/L (CONTROLS phonon control, COMP-PH §5); ASR zero.
- **Pitfalls.** PBE-relaxed Ge is metallic: phonons must stay at a_exp; split the run into ≤ 3 h jobs if run in the box (run-heavy.sh lock).
- **Result goes to.** Fill the placeholders in returns/R15/COMP-PH.md via a new return (returns are never edited) and code/COMP-PH/properties.csv; closes LE-16 for Ge; input to DC-2.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.3, §3.2–§3.3, §5 · inputs: /home/user/dmdd-solid/code/COMP-PH/chain.py (phgrid, 80 Ry, k 8³, a_exp 5.658 Å); Ge 4³ run in /home/user/dmdd-solid/code/COMP-PH/out · depends: none.

#### DC-5. Magnitude of the Si (2̄00) Umklapp density vertex |ρ_cv(k,q+G)| and ∇_kρ_cv at the conduction extremum (Si; P1)
- **Physics.** Above its X-face edge ≈ 0.50 MeV (the allowed-size zero-phonon line; distinct from the first zero-phonon edge 0.407 MeV, a glide-class state) the (2̄00) class is symmetry-allowed on axis, but its vertex may be small; its size and gradient decide which channel leads.
- **Quantity and units.** |ρ_cv(k_v=Γ, k_c≈0.85X; q+G)|² (dimensionless) vs |q|, and ℓ_∇ = |∇_kρ_cv|/|ρ_cv| (Å) at the extremum.
- **Method and approximation level.** PBE NC wavefunctions (SG15, 40–60 Ry) on k and k+q(+G) sets matched by Miller index; plane waves common to both sets; cubic averaging over equivalent pockets. Code: QE pw.x nscf + code/COMP-PAER/scripts/formfactor.py (extended to q+G).
- **Convergence and acceptance.** Symmetry zeros: on-axis LA (G′ = 0) and the §M3(d) LO zero; convergence in ecut (40 → 60 Ry) and bands (16 → 30) to 2%; C4 f-sum diagnostic as in COMP-PAER §7.
- **Pitfalls.** NC pseudo-wavefunctions are unreliable above q_c ≈ 10 keV (not reached here); use unreduced q (CONVENTIONS §2).
- **Result goes to.** Ch 13 §window close; WP1-v3 IF-6 / WP3-v3 §M9 replacement text; LIMITS L8-N1 note.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 exciton spec (ii), §10 item 1; LOOSE-ENDS LE-25 · inputs: to write (adapt /home/user/dmdd-solid/code/COMP-PAER/inputs/nscf_rho.in and formfactor.py to the X pockets and G = (2̄00)) · depends: none.

#### DC-6. Forbidden-ZPL / PAER ratio ϖ_II [E14] at the Si edge and +0.1 eV, from S^PA on WP1's (q,ω) grid (Si; P1)
- **Physics.** Between the first zero-phonon edge 0.407 MeV and the allowed-size (2̄00) edge ≈ 0.50 MeV both the symmetry-forbidden ZPL and PAER are open; their ratio decides which channel the book calls leading.
- **Quantity and units.** ϖ_II(m_χ) = ℛ_ZPL/ℛ_PAER (dimensionless) at the edge and at ε_ex = +0.1 eV.
- **Method and approximation level.** Both rates from one band structure, one gauge and the same (q,ω) bins; η_PA no longer transferred from data. Code: DC-1 stage-6 output + WP1 zero-phonon S^(1) on the same grid.
- **Convergence and acceptance.** C3 (first-order open: sideband O(g²) relative where ZPL allowed) checked numerically; consistency with WP1 [E14] band 0.03–2 (edge).
- **Pitfalls.** Do not mix the [E] 𝔉_ρ rate with a [CALC] ZPL.
- **Result goes to.** Ch 13; WP3-v3 §M9 (2); WP6 two-channel band; LIMITS.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP1-v3.md IF-6b, §8 exciton spec (iii); /home/user/dmdd-solid/returns/R8/WP3-v3.md §M9 (2) · inputs: DC-1 outputs; WP1 zero-phonon tables: to write · depends: DC-1, DC-5.

#### DC-7. Si window residuals: SOC admixture of the LA kink and (2̄00)-class LO minimum on axis (LE-27 remainder); finer q̂ search of E_min^ZPL for |q| < 1.3 keV (Si; P3)
- **Physics.** Exponents p̄_on of the rate at the edge depend on vertex zeros that SOC can lift; the window optimum depends on min over q̂.
- **Quantity and units.** SOC-induced LA vertex amplitude (relative), LO minimum location ϑ (rad), E_min^ZPL(|q|) (eV) on a Fibonacci q̂ set.
- **Method and approximation level.** PBE+SOC Si 2-atom; 100–400 q̂ directions; reuse COMP-PH 8³ phonons. Code: QE noncollinear SOC small cell + code/COMP-PH/{emin,gamma}.py.
- **Convergence and acceptance.** E_min over 400 directions vs the five-direction value; criterion (M.7a) as in COMP-PH §4; C5.
- **Pitfalls.** Si split-off 44 meV: SOC effects ≈ 4% amplitude [E]; keep a_PBE vs a_exp systematic stated.
- **Result goes to.** WP3 §M3 final table, WP6 p̄_on; Ch 13.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP3-v3.md §R1, §M3; /home/user/dmdd-solid/returns/R15/COMP-PH.md §4 (On/off-axis) · inputs: to write (COMP-PH Si inputs + Si_ONCV_PBE_FR) · depends: none.

#### DC-8. CONTROLS C8 GaAs decoy: GaAs bands + [E13]-type window scan, then the tier-H pipeline with lpolar (Fröhlich) (GaAs; P2)
- **Physics.** Decoy control: in a direct-gap crystal the zero-phonon channel is open almost everywhere, so PAER can lead only in a narrow mass band.
- **Quantity and units.** GaAs window (MeV), PAER/ZPL rate ratio per m_χ.
- **Method and approximation level.** As DC-1 with lpolar = .true., Fröhlich g^L, Z*/ε_∞ from DC-91; PBE run at a_exp after checking the Γ gap (PBE GaAs nearly metallic). Code: QE fork + EPW (lpolar) + stages 5–6.
- **Convergence and acceptance.** C8 pass criterion as stated in CONTROLS; C5.
- **Pitfalls.** GaAs needs 140 Ry with SG15 Ga (3d); polar divergence without lpolar; scissor + valley offsets consistently (CW3 pitfall).
- **Result goes to.** CONTROLS C8 status; SOTA R2 table; Ch 13 decoy paragraph.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R15/COMP-PAER.md §8 (C8 with the same pipeline); /home/user/dmdd-solid/returns/R8/WP3-v3.md §M9 C8 · inputs: /home/user/dmdd-solid/code/COMP-PH/formulated/GaAs/ (ground state, 140 Ry); tier-H GaAs inputs: to write · depends: DC-1 (pipeline), DC-91 (GaAs Γ-DFPT, Z*, ε_∞), INF-2, INF-3, INF-4.

#### DC-9. Finite-q BSE beyond TDA for Si/Ge with bound lines; exciton dispersion along Γ–X (both sides) and Γ–L; hydrogenic series with ab initio anisotropic masses (Si, Ge; P2)
- **Physics.** Electron–hole attraction near the gap redistributes weight into bound lines and enhances the continuum edge (Sommerfeld); TDA misses the coupling term at finite q.
- **Quantity and units.** L(q,ω) on (q̂, |q|, ω) bins for q ≤ 10 keV, ω ≤ E_g+10 eV; Δ^τ_BSE (type M); bound-line energies/weights; E_x(P) dispersion (meV).
- **Method and approximation level.** 4 VB (Ge + 3d) × 12 CB; coarse 8³ kernel interpolated to 24³ with matrix-free products (the 7 TB dense kernel is never stored); ≈ 200 Lanczos iterations; ≈ 10³ (q_r, G) points after O_h; bound lines added by [E8] with ab initio μ_x, ε_∞, ρ_cv, ∇_kρ_cv. Code: QE → G₀W₀ → finite-Q BSE (BerkeleyGW finite-Q, Yambo q ≠ 0, or exciting); Haydock/Lanczos.
- **Convergence and acceptance.** Non-TDA coupling checked by the f-sum to < 1%; validation Si NIXS/EELS at q < 3αm_e; Si/Ge free-exciton binding (Si 14.7 meV).
- **Pitfalls.** Storing the fine kernel; excitons need k spacing ≲ 1/(3a_x); the S^BSE ⊕ S^RPA+LFE strip matching.
- **Result goes to.** Ch 4.9, Ch 10, Ch 13 (bound lines in the PAER window); WP6 Δ^τ_BSE nuisance; LIMITS G5 rows.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 G5 and exciton spec (i), (iv); §10 items 1–2 · inputs: to write · depends: INF-1.

#### DC-10. Exciton–phonon replicas (W.14): converged finite-P BSE at the pocket set with EPW g^x (Si, Ge; P3)
- **Physics.** Phonon replicas of excitons at E_x + ω_ν(Q*) sit below the free-pair PAER edge.
- **Quantity and units.** replica strengths per branch (dimensionless) and line positions (meV) at P ≈ 0.85X.
- **Method and approximation level.** ~10³ k per pocket (a_x ≈ 5 nm); practical route Wannier–Mott × EPW M_free as a cross-check. Code: finite-P BSE + EPW g on the same U(k); g^x by 1705.04245 Eq. (49).
- **Convergence and acceptance.** Wannier–Mott limit; replica edge 0.3332 MeV (COMP-PH) reproduced.
- **Pitfalls.** Gauge consistency of g and BSE eigenvectors.
- **Result goes to.** Ch 13; WP3 (W.14) status [C] → [CALC].
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP3-v3.md §8 G5 · inputs: to write · depends: INF-1, DC-9.

#### DC-11. Crystal exciton Migdal (G-X8): finite-p BSE over the BZ inside the G6 code path (Si, Ge; P3)
- **Physics.** A nuclear kick can leave the crystal in a bound exciton instead of ionising it.
- **Quantity and units.** exciton-line weights per p (dimensionless) and E_λ(p) (eV).
- **Method and approximation level.** BSE inside the G6 Migdal path. Code: finite-p BSE (p 8³–12³, G ≤ 50, λ ≤ 20 per p) in the DC-25 path; atoms by GRASP2018/MCHF.
- **Convergence and acceptance.** line weights vs the [E8] Wannier–Mott limit; stable to 5% under k-mesh doubling (10³ → 8×10³ per pocket) and band doubling.
- **Pitfalls.** Boost mass m_A vs m_N at O(Zm_e/M).
- **Result goes to.** Ch 12; WP7-B1 G-X8.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §8 (Computation specification) · inputs: to write · depends: INF-1, DC-25.

#### DC-12. Frenkel / self-trapped excitons in NaI (localisation, binding, release) (NaI; P3)
- **Physics.** In alkali halides the exciton self-traps (V_k + e), which changes the energy bookkeeping relative to free pairs.
- **Quantity and units.** STE binding/relaxation energies (eV); on/off-centre geometry.
- **Method and approximation level.** hybrid DFT (α = 0.25 and 0.40), 64 → 216-atom cells. Code: constrained-occupation hybrid DFT (QE HSE/PBE0) + BSE; method shared with DC-73.
- **Convergence and acceptance.** STE luminescence energies vs data; hybrid-fraction spread reported.
- **Pitfalls.** STE localisation depends on the hybrid fraction.
- **Result goes to.** Ch 16, Ch 18; WP1 gap list.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 'Remaining gaps'; method as /home/user/dmdd-solid/returns/R16/CW5.md §4.1 (STE by constrained hybrid DFT) · inputs: to write · depends: INF-1 (BSE); CW1 formula pointer still owed.

#### DC-13. G7 core and relativistic response: Ge 3d, Ga 3d, Si 2p core-level finite-q BSE with SOC (ZORA/FLAPW) (Ge, GaAs, Si; P3)
- **Physics.** Semicore d shells contribute to L(q,ω) at 30–200 eV; relativistic operators enter at O(α²).
- **Quantity and units.** L_core(q,ω), q ≤ 30 keV, ω ≤ 200 eV; 3d₅/₂/3d₃/₂ resolved.
- **Method and approximation level.** ZORA + SOC (no crystal 4-component no-pair code exists: that remainder stays an exact gap); 3d binding spread PBE/HSE06/G₀W₀/ΔSCF as nuisance (target 29.5 eV); 12³ k. Code: all-electron FLAPW (exciting or WIEN2k) with SOC, or PAW + core reconstruction.
- **Convergence and acceptance.** [E11] f-sum shift check; 3d binding vs 29.5 eV.
- **Pitfalls.** 4-component projection unavailable.
- **Result goes to.** Ch 10; LIMITS G7.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 G7 · inputs: to write · depends: INF-1, INF-6.

#### DC-14. Non-density operator library: G10 IP response tables (12 real functions Si/Ge) with exported R⁰_GG′; LFE screening of j_T and in-medium 𝒪₈ ratio; triplet channel beyond IP (ladder + f_xc^T) (Si, Ge; P2)
- **Physics.** Spin- and velocity-dependent DM operators couple to currents and spins, whose screening differs from the density's.
- **Quantity and units.** 12 real response functions per (q,ω) (Si/Ge), R⁰_GG′; 𝒪₈ in-medium/IP ratio (dimensionless).
- **Method and approximation level.** IP + RPA+LFE (mixed R̃_{j_T,n}); triplet W^scr ladder + f_xc^T; 10³ k, q ≤ 25αm_e, LFE cutoff ≈ 8αm_e. Code: QE + EXCEED-DM-type IP module (vertices ρ_cv, ⟨c|½{p,e^{iq·r}}|v⟩ with the non-local commutator), RPA+LFE Dyson with mixed blocks, triplet ladder.
- **Convergence and acceptance.** PT-zero diagnostics: Im S_{nj_T}, S^anti_{j_Tj_T} < 10⁻³ of the real parts in Si/Ge.
- **Pitfalls.** Missing non-local commutator in the current vertex; unscreened spins.
- **Result goes to.** Ch 10; LIMITS L3 factor resolved or interval; WP6 library schema (IF-10).
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 G10, §10 items 4–5; IF-10, IF-13, IF-14 · inputs: to write · depends: INF-9 (IP vertex module), INF-1 (ladder).

#### DC-15. G11 electronic anisotropy S₄, S₆, S₈(|q|, ω): full-q RPA+LFE ELF projected on cubic harmonics (Si, Ge, GaAs; P3)
- **Physics.** Crystal anisotropy of the loss function makes the rate depend on the halo direction.
- **Quantity and units.** S_ℓ(|q|,ω), ℓ = 0, 4, 6, 8 (relative to S₀₀).
- **Method and approximation level.** RPA+LFE on a Lebedev q̂ grid, projection on K^cub_ℓ. Code: GPAW, QCDark2 or BerkeleyGW full-q RPA+LFE.
- **Convergence and acceptance.** |S₁ₘ|, |S₂ₘ|, |S₃ₘ|/S₀₀ < 10⁻³.
- **Pitfalls.** Projecting δ-like lines without ω bins.
- **Result goes to.** Ch 17; WP6 G11 library.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP1-v3.md §8 G11 · inputs: to write · depends: INF-1.

#### DC-16. SOC mixing near the Ge edge and the SOC-lifted Si on-axis vertex (Si, Ge; P3)
- **Physics.** SOC mixes spin into the band edges and lifts symmetry zeros of the density vertex.
- **Quantity and units.** relative amplitude changes (dimensionless).
- **Method and approximation level.** PBE+SOC vs PBE vertices at the extrema. Code: QE noncollinear small cell (box).
- **Convergence and acceptance.** Si result → 0 as SOC → 0; Ge edge ordering control of DC-2.
- **Pitfalls.** Ge PBE band order (use DC-2 bands).
- **Result goes to.** WP1 §10; Ch 10.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R8/WP1-v3.md §10 item 6; LOOSE-ENDS LE-36 · inputs: to write (FR SG15) · depends: DC-2 (Ge bands; Si part needs nothing).

#### DC-17. X2 numerics: N1 1D two-band contact-kernel model vs real-time TDH; N2/N3 Si Route S (ZG supercell, RPA local fields) at q = 0 and 0.5/1/2 keV (δ_LF, δ_pair, Λ(q)); N4 ε̃⁻¹_G0(q,ω) in the window (Si (N1: model); P2)
- **Physics.** The phonon-assisted amplitude is screened by local fields and by a pair channel (Coulomb lines carrying P = Q); their signs are not derived.
- **Quantity and units.** Λ(q) = |M̃|²/|M|², δ_LF, δ_pair (dimensionless) at q = 0, 0.5, 1, 2 keV.
- **Method and approximation level.** Route S: frozen-phonon/ZG supercell, RPA local fields in the supercell G basis, unfolded to unreduced q; IP + scalar-ε run gives δ_LF + δ_pair by difference; ALDA as a second rung (LE-44). Code: N1: python script; N2–N4: QE supercells + RPA-LFE (turbo_eels, Yambo, or own code).
- **Convergence and acceptance.** N1: Λ = O(ω_Q) rigid vs O(1 − 1/ε(P)) intracell; N2: optics vs measured absorption; test Λ(q) ≈ Λ(0).
- **Pitfalls.** Supercell must contain Q*; unreduced-q unfolding.
- **Result goes to.** Ch 13 screening; WP3 §M7 envelope; LIMITS L8; X2 [C] items.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R3/X2.md §8 (Route S), §10 N1–N4; /home/user/dmdd-solid/returns/R8/WP3-v3.md §M10 routes · inputs: to write · depends: N1 none; N2–N4: INF-1 (RPA+LFE) or Route-S code.

#### DC-18. X1 residual tags: frozen-strain deformation tensors D^n for Si (symmetric D^n under rotations, D/c_ν ≫ q, piezo-log relevance) (Si; P3)
- **Physics.** Soft-acoustic limit of the PAER amplitude depends on band deformation potentials.
- **Quantity and units.** D^n_αβ (eV) per band/valley.
- **Method and approximation level.** finite strain ±0.5%, PBE. Code: DFPT or finite strain (pw.x).
- **Convergence and acceptance.** known Si deformation potentials (Ξ_u ≈ 8.6–9 eV) [E].
- **Pitfalls.** valley degeneracy under strain.
- **Result goes to.** X1 tags → [CALC]; Ch 13 C7.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R3/X1.md §10 status table; LOOSE-ENDS LE-179 · inputs: to write · depends: none.

### B. Lattice, Migdal, anharmonicity, disorder

#### DC-19. Shared harmonic stack A: DFPT force constants, eigenpairs, per-atom PDOS, B_κ, Z*, ε_∞ at 80 Ry on an 8³ q grid (experimental a; PBE vc-relax partner) (Si, Ge, GaAs; P2)
- **Physics.** One harmonic lattice per material, used by every lattice channel.
- **Quantity and units.** Φ_κκ′(ΔR), ω_Qν (meV), e_κν, D_κ(ω), B_κ (Å²), Z* (e), ε_∞.
- **Method and approximation level.** SG15 v1.2, 80 Ry, 12³ k, tr2_ph 10⁻¹⁶, epsil for GaAs, fildrho/fildvscf kept; asr='crystal'. Code: pw.x → ph.x (8³) → q2r.x → matdyn.x.
- **Convergence and acceptance.** ω to 0.1 meV under 6³ → 8³ q; INS 5% (COMP-PH control); GaAs ε_∞ 10.9, Z̄* 2.27 vs [FT] rows.
- **Pitfalls.** PBE a 0.7–1% large softens phonons 2–4%; polar GaAs needs the non-analytic term; phase convention e^{iQ·R} with e^{iq·r_κ} at unreduced q.
- **Result goes to.** Ch 5.4; CW2 rows; WP8-U phonon_DOS (Si, Ge, GaAs).
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §0b stack A · inputs: /home/user/dmdd-solid/code/CW2/inputs/{Si,Ge,GaAs}/{scf,ph,q2r,matdyn_dos,matdyn_modes}.in (+ README) · depends: none; COMP-PH outputs replace the Si/Ge part when converged at 80 Ry.

#### DC-20. Coherent two-phonon S^(2)_coh(q,q̂,ω) at q < q_BZ and rate-level ℛ₂, ℛ₃ (CW2.1)–(CW2.3) (Si (then Ge, GaAs); P3)
- **Physics.** At q below the zone boundary two-phonon emission is coherent and the incoherent approximation fails pointwise.
- **Quantity and units.** S^(2)_coh (eV⁻¹ per cell) on 40 log |q| ∈ [0.2,10] keV × ≈ 20 directions, 0.5 meV bins.
- **Method and approximation level.** B_κκ′(ΔR) to 40 Å by FFT; Q₁ sum on 48³, Gaussian σ = 0.25 meV. Code: python/Fortran module on stack-A eigenpairs (48³).
- **Convergence and acceptance.** 32³ → 48³ → 64³ until bins change < 2%; ℛ_n changes < 10⁻³ in the real-space radius.
- **Pitfalls.** Q = 0 acoustic point: exclude and add the analytic small sphere; unreduced-q phase; never the real-space form at T > 0.
- **Result goes to.** Ch 11; LIMITS WP2 rows; DC-21 flagged cells.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §1, §2 · inputs: DC-19 outputs; module: to write · depends: DC-19, INF-9.

#### DC-21. G3 multiphonon library tables S(q,q̂,ω), P_ph(n_ph|q,ω), ρ^ph_κν, f_coh, ℛ_n (HDF5) and G11 lattice anisotropy S_ℓm (Lebedev 590) (Si, Ge, GaAs (then survivors); P2)
- **Physics.** Nuclear recoils at q ≫ q_BZ excite many phonons; the incoherent sum gives the response library.
- **Quantity and units.** S (eV⁻¹), P_ph, ρ^ph; q ∈ [0.1, 300] keV (400 log), ω ∈ [0, 1 eV] at 0.1 meV; T ∈ {10 mK, 1 K, 77 K}.
- **Method and approximation level.** K = multi-inc + coherent n = 1; IA Gaussian with Edgeworth 𝔨₃, 𝔨₄ above x_R > 16. Code: new ≈ 300-line (3.5) module on stack-A PDOS (48³ tetrahedra).
- **Convergence and acceptance.** f-sum (3.4′) to 10⁻⁴ per q; FFT t_max ≥ 20π/δω; |S_{ℓ≥4}|/S₀₀ < 10⁻⁶ incoherent.
- **Pitfalls.** 2W with (2n+1); remove the Bragg δ analytically; (1 − P_Mig)S^GS[M + δM]; species-resolved 2W for GaAs.
- **Result goes to.** Ch 11, Ch 19; WP6 library; DC-80 (NR birth spectra x_R ≲ 1).
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §10, §13 · inputs: DC-19; module: to write · depends: DC-19, INF-9, DC-20 (flags).

#### DC-22. Valence charge deformation Δ_κα(Q+G) at q ≫ q_BZ (|Q+G| ≤ 20 keV) and core polarisation Δ^core_κ(q) (L4 add-on 𝒵_κα(Q+G)) (Si, Ge, GaAs; P3)
- **Physics.** Whether the electron cloud follows a displaced nucleus at high q decides the effective nuclear form factor of the one-phonon vertex.
- **Quantity and units.** Δ_κα(Q+G) (e per unit displacement) for |Q+G| ≤ 20 keV, ≈ 725 reciprocal-lattice vectors per Q in Si and 821 in Ge/GaAs (direct count; CW2 §4's ≈ 4000 is withdrawn), Δ^core(q).
- **Method and approximation level.** (i) |q| ≲ 10 keV from DFPT δρ minus q f^at; (ii) ±0.01 Å AE densities in 216-atom cells. Code: ph.x fildrho + PAW AE reconstruction or LAPW finite-displacement supercells; Dalgarno–Lewis on ld1.x cores.
- **Convergence and acceptance.** (CW2.9) translational sum rule to 10⁻³; ±u linearity; ℓ = 1 core sum rule = core dipole polarisability.
- **Pitfalls.** pseudo δρ above q_c is an artefact; gridded PAW AE density aliases above ≈ 10 keV; frozen-core PAW gives Δ^core ≡ 0.
- **Result goes to.** Ch 11 (L4); LIMITS L4 add-on.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §4 + /home/user/dmdd-solid/returns/R16/CW2-errata.md E-5 (ecutrho ≥ 65 Ry, one-centre transforms, core sub-spec (d)) · inputs: ph.in of /home/user/dmdd-solid/code/CW2/inputs/* (drho kept); AE supercells: to write · depends: DC-19, INF-6.

#### DC-23. Finite-q eκ factor Δ𝓃_κ(q,q̂) beyond hydrogenic 1s²: crystal valence AE density and finite-nucleus Dirac 𝓃_e(R_κ) (Si, Ge, GaAs; P3)
- **Physics.** The electron density at the nucleus and its q-dependence correct the nuclear–electron cross term.
- **Quantity and units.** Δ𝓃_κ(q) relative to 𝓃_e(0) (a₀⁻³).
- **Method and approximation level.** AE PBE, |G| ≤ 40 a₀⁻¹, Lebedev angular grid. Code: PAW pp.x plot_num=21 minus atomic core or LAPW; GRASP2018/DIRAC or patched ld1.x.
- **Convergence and acceptance.** Δ𝓃^val changes < 10⁻⁵𝓃_e(0) under |G| and augmentation radius; r_min ≤ R^nuc/100.
- **Pitfalls.** NC densities unusable; never apply the relativistic ratio on an NR 𝓃_e(R).
- **Result goes to.** Ch 12; WP2 (5.2″), WP3 J8.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §9; /home/user/dmdd-solid/returns/R16/CW2-errata.md E-6, E-7 · inputs: /home/user/dmdd-solid/code/CW2/atomic_contact.py, atomic_contact_errata.py (atomic part done); crystal part: to write · depends: INF-6.

#### DC-24. Drag mass δM_κ, inverse moments ℐ₂–ℐ₄, C_κ and P_Mig(E_R) by frequency-dependent Sternheimer (Si, Ge, GaAs; P2)
- **Physics.** Electrons dragged by a moving nucleus add mass and set the Migdal probability.
- **Quantity and units.** δM_κ (m_e), P_Mig (dimensionless).
- **Method and approximation level.** RPA SCF ΔV, harmonic, BZ average over 8³ Q; core N_core m_e added exactly. Code: ph.x + mixed E(ω)–u response at imaginary ω (rtsc/sth batched shifted solves).
- **Convergence and acceptance.** δM to 1% in k (12³ → 16³); trace Σδ M = N_e m_e per cell (J3); P_Mig ≤ E_R(δM/M)/E_g.
- **Pitfalls.** exclude the macroscopic field at Q = 0 in GaAs; KS-pair vs many-body ℐ_k.
- **Result goes to.** Ch 12; WP3 J3; LIMITS L7.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §8, §0b stack C · inputs: to write (stack-C patch) · depends: DC-19, INF-5.

#### DC-25. G6 Migdal single code path: all-electron RPA+LFE S^ee_GG′(p,ω_e) (p ≤ 30 keV, ω_e ≤ 100 eV) convolved with S^GS_κκ; quenching-subtraction kernel; T2/LFE band (also the Wannier branch of WP7-B1 X6) (Si, Ge; P2)
- **Physics.** The Migdal rate is the convolution of the electronic response at the kick momentum with the lattice recoil response.
- **Quantity and units.** S^X_κκ(q; ω_ph, ω_e) (eV⁻² per cell).
- **Method and approximation level.** τ n_B = leading non-adiabatic, T1–T3 (Condon, GS vibrational final states, RPA+LFE). Code: GPAW AE or Yambo/BerkeleyGW with semicore; DC-21 tables; impulse-bracket convolution.
- **Convergence and acceptance.** closure tests (a) E^Mig_3 = (CW2.13); (b) δM moment = (CW2.14)/(CW2.15), Σ = N_e m_e; (c) P_Mig bound; (d) neutron calibration 2210.04917; LFE |G| ≤ 4 → 6 a₀⁻¹, k 8³ → 12³.
- **Pitfalls.** never add (W.5) to a bare-mass unit-weight S^GS; diagonal-only ε⁻¹ is an O(1) error; valence-only Z_κ(p) misses the core ω³ moment.
- **Result goes to.** Ch 12; LIMITS L7a–d; WP8-S Migdal row.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §14; /home/user/dmdd-solid/returns/R8/WP3-v3.md §8 G6; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §7 · inputs: to write · depends: INF-1, INF-6, DC-21.

#### DC-26. Non-rigid Wannier correction ratio 𝔯_W(q,ω_e) = |A^DFPT|²/|A^(H_W)|² with the bare ∇_RV screened by RPA+LFE at ω_e (Si, Ge, diamond; P3)
- **Physics.** The Wannier picture of Migdal treats electrons as rigidly following the nucleus; the true vertex uses the full potential derivative.
- **Quantity and units.** 𝔯_W (dimensionless) per q.
- **Method and approximation level.** leading non-adiabatic Migdal (T0), clamped-nuclei final states. Code: ph.x bare perturbation → Wannier90 MLWFs (k 16³) on one U(k) → EPW-style interpolation; RPA+LFE screening.
- **Convergence and acceptance.** ASR Σ∂_RV^scf = −Σ∇V_KS to 10⁻³ (static, gauge/k-mesh check); δM sum rule (J3).
- **Pitfalls.** static dvscf mixes screening and non-rigidity (report as a labelled variant); non-local i[V_NL, r].
- **Result goes to.** Ch 12; LIMITS LB1-8.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §19 + /home/user/dmdd-solid/returns/R16/CW4-errata.md A3(c) (bare vertex, dynamical screening) · inputs: to write · depends: INF-1, DC-25.

#### DC-27. X10 valence amplitude for c_κ not ∝ M_κ: S^ee_GG′(k → 0, ω) for |G| ≤ 6(2π/a), ω from E_g to 100 eV + core edges, contracted with (CW2.26) (Si (diamond-structure); P3)
- **Physics.** When DM couples to nuclei not in proportion to mass, the lattice acquires an Umklapp-only electronic channel.
- **Quantity and units.** Γ per model δc̃_κ (rate units).
- **Method and approximation level.** RPA+LFE (then ALDA), clamped nuclei. Code: Yambo/BerkeleyGW χ_GG′(q→0,ω) or QE turbo_eels at q = G.
- **Convergence and acceptance.** LFE size until Γ changes < 2%; k 12³; reduces to (B2.8.2) for c ∝ M; (200) channel vanishes (C17).
- **Pitfalls.** diagonal-only ε misses all Umklapp terms; G = 0 uses the improper S^ee.
- **Result goes to.** WP7-B2 X10; Ch 11.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §24 · inputs: to write · depends: INF-1.

#### DC-28. Loss function L(k,ω) = Im[−(ε⁻¹)₀₀] (RPA+LFE, scissor/GW gap, semicore) for every survivor, |k| ≤ 5 keV, ω ∈ [E_g, 5ω_p]; 𝓠_Mig,κ and w_acc⟨1/ω⟩ (all 42-pool survivors (WP8-U v4); P2)
- **Physics.** The Migdal yield is set by the inverse fourth moment of the crystal loss function near the gap.
- **Quantity and units.** L(k,ω) dimensionless; 𝓠_Mig,κ, ∫𝓠dω per κ.
- **Method and approximation level.** RPA+LFE with full ε_GG′; TDDFT-ALDA cross-check; semicore within 5ω_p (Ga 3d, Ge 3d, W 5p/4f, Pb 5d, Te 4d, Cs 5p, I 4d, Mo 4p). Code: QE scf → dense nscf → χ⁰_GG′ (Yambo/BerkeleyGW or fork) → Dyson (RPA; ALDA rung).
- **Convergence and acceptance.** f-sum ∫ωL = (π/2)ω_p² to ≤ 2%; ∫L/ω⁴ to < 1% under bands, k-mesh doubling, G cutoff; broadening δ ≤ E_g/20 extrapolated to 0.
- **Pitfalls.** missing semicore biases ∫L/ω⁴ low; scissor moves the E_g⁻⁵-weighted onset; average over k̂; unreduced k above q_BZ; excitonic weight (BSE rung bounds it); X_pole < 1 possible.
- **Result goes to.** Ch 12, Ch 17 (Migdal ranking); WP8-U GAP:L_eps2_data cells; WP8-S X_pole prior replaced.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R17/WP8-errata.md §15 · inputs: to write (COMP-PH layout) · depends: INF-1; DC-91/94/96/97 ground states.

#### DC-29. G3 PIMD inputs: nuclear momentum distribution 𝔫_κ(p), E^kin_q̂, ⟨∂²_q̂E^ad_0⟩ (= 𝔨₃^GS), 𝔨₄ pieces (Si, Ge; P3)
- **Physics.** Quantum nuclear motion sets the width of the impulse peak at large q.
- **Quantity and units.** 𝔫(p) (Å³), E^kin (meV), curvature (eV/Å²), 𝔨₄.
- **Method and approximation level.** PIMD, centroid-virial and open-path estimators; PIGLET (P ≈ 16–32) or P with βω_max/P ≲ 0.3; T = 50–100 K corrected to T → 0 with the harmonic difference. Code: i-PI + MLIP (MACE/NequIP on PBE or SCAN), 216-atom cells.
- **Convergence and acceptance.** < 1% statistical error; MLIP validated on displaced configurations to 3σ of the PIMD distribution.
- **Pitfalls.** open-path ⟨P⁴⟩ noisy (≥ 10⁶ steps); MLIP extrapolation biases 𝔨₄.
- **Result goes to.** Ch 11, Ch 19; DC-21 Edgeworth inputs; DC-31 anchor.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §11, §0b stack D · inputs: to write · depends: INF-7.

#### DC-30. Non-perturbative anharmonicity and quantum crystals: TRPMD/CMD/SSCHA/TDEP F_s(q,t), S_self(q,ω) for soft-mode and light-atom targets; solid ⁴He moments and band (PIMD, Aziz potential); solid He SSCHA Φ_eff at 1–40 GPa (KTaO₃, SrTiO₃, LiH, solid He; P3)
- **Physics.** Where anharmonicity is not small, the multiphonon expansion fails and only exact static moments bound the response.
- **Quantity and units.** moments 𝓂₀–𝓂₄; S_self(q,ω) (eV⁻¹); Markov–Krein CDF band.
- **Method and approximation level.** approximate quantum dynamics validated against exact PIMD moments (CW2.10)–(CW2.11). Code: i-PI (TRPMD/CMD) + MLIP; SSCHA/TD-SCHA; TDEP; Aziz He–He.
- **Convergence and acceptance.** every approximate S tested against the moment band; P 64 → 128, N 180 → 432 (He).
- **Pitfalls.** RPMD/CMD exact only for first moments; tunnelling splittings missed; Bose exchange to be checked once for He.
- **Result goes to.** Ch 11 (scope); LIMITS L11, LE-52 gap text.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §5, §23 + /home/user/dmdd-solid/returns/R16/CW2-errata.md E-12; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §4 · inputs: to write · depends: INF-7 (MLIPs for the oxides/LiH).

#### DC-31. G13 / G-F2 anharmonic nuisance template: phono3py fc3 (4×4×4, 128 atoms), hiPhive/TDEP fc4, bubble spectral function, W₃/W₄ contour sums, Δ^τ_A(q,ω) (Si (then Ge, GaAs); P2)
- **Physics.** Cubic and quartic anharmonicity broaden and shift multiphonon spectra above the one-phonon band.
- **Quantity and units.** Δ^τ_A(q,ω) relative correction; type-T nuisance width.
- **Method and approximation level.** n_A = 1 (η²_anh), T-renormalised; full spectral function (not on-shell linewidths). Code: phono3py + hiPhive/TDEP on QE supercells; PIMD anchor DC-29.
- **Convergence and acceptance.** 3×3×3 → 4×4×4, cutoff 4 → 5 Å, 24³ → 32³; first-order Φ³ term must vanish numerically.
- **Pitfalls.** M-type nuisances break (6.1); phono3py linewidths are on-shell.
- **Result goes to.** Ch 5.7, Ch 11; WP8-F G-F2; WP6 type-T row.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §12 · inputs: to write · depends: INF-12, DC-19, DC-29.

#### DC-32. Glass models: melt-quench MLIP glasses (648–5184 atoms, ≥ 5 quenches), full Hessians, Z*_I; amorphous S_dist at n_ph = 2, 3 (CW2.12′); IR coefficients A^IR, B^IR of C^IR = A + Bω²; disorder D_I, C^IR (WP7-B2 §2) (a-SiO₂, a-Si, SiN_x; P3)
- **Physics.** In glasses the dynamic structure factor needs configurational averages of displacement correlations and site-charge fluctuations.
- **Quantity and units.** 𝔚^(n)_dist(q), S^(n)_dist(q,ω); A^IR, B^IR.
- **Method and approximation level.** harmonic, ref = glass; (CW2.12′) with ⟨|b|²⟩, ⟨|τ|²⟩, ⟨b·τ·b⟩ binned. Code: LAMMPS + MLIP; phonopy Γ-only; DFPT Z* on 192–648-atom subcells or charge-equilibration MLIP.
- **Convergence and acceptance.** g₂ and moments 1728 vs 5184 atoms to 5%; L ≥ 4 nm; Σ_I Z*_I = 0 per configuration.
- **Pitfalls.** finite-size gap 2πc/L removes the lowest modes; locally neutral charge model forces A^IR = 0; quench-rate dependence is type M.
- **Result goes to.** Ch 16; LIMITS B2-L3.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §6, §17; /home/user/dmdd-solid/returns/R16/CW2-errata.md E-8; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §2 · inputs: to write · depends: INF-13 (glass MLIP), INF-9.

#### DC-33. Isotope B−L channel: Γ_iso(ω) exactly from isotope-resolved Hessians (4096-atom natural-Si supercells, 10 realisations); T = 0 two-phonon ε₂(ω) of Si from ∂Z*/∂u (Si; P3)
- **Physics.** Isotope mass disorder couples a B−L vector to the lattice; the competing EM absorption needs the low-T two-phonon ε₂.
- **Quantity and units.** Γ_iso(ω) (s⁻¹ per coupling²); ε₂(ω) at T = 0.
- **Method and approximation level.** harmonic, exact isotope disorder; second-order dipole ∂Z*/∂u with two-phonon joint DOS (sum weights only). Code: stack-A IFCs + dense diagonalisation / KPM; DFPT epsil in ±u supercells (64, 216 atoms).
- **Convergence and acceptance.** 10 → 20 realisations, 4096 → 13824 atoms to 2%; reproduce the measured 293 K curve (Deinzer–Strauch) to ≤ 20% in 40–60 meV before using T = 0.
- **Pitfalls.** subtract M_Iϑ̄ with mass-weighted ϑ̄; Si selection rules suppress many pairs.
- **Result goes to.** Ch 11; WP7-B2 isotope channel; LIMITS 'Numbers carried'.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §18, §19 + /home/user/dmdd-solid/returns/R16/CW2-errata.md E-9 · inputs: to write · depends: DC-19.

#### DC-34. GaAs electron-scalar single-phonon rate as a near-cancellation: DFPT Z*, ε_∞ to ≲ 1% with LST data; PhonoDark-abs with vertex Z_κ − Z*_κ and the mixing term; Γ^ph_ν from phono3py (GaAs; P2)
- **Physics.** For an electron-coupled scalar the electronic and ionic contributions to the LO residue nearly cancel in GaAs.
- **Quantity and units.** rate ℛ(m_φ) with its sensitivity band.
- **Method and approximation level.** one consistent Z* and ε_∞ in vertex and mixing term. Code: QE/Abinit DFPT + PhonoDark-abs (patched) + phono3py.
- **Convergence and acceptance.** Z*, ε_∞ to 1%; ω_ν to 0.1 meV; Γ^ph to 10%.
- **Pitfalls.** rigid-ion Q_j changes d by 3×; Ga isotope disorder adds a broadband channel.
- **Result goes to.** Ch 11; LIMITS B2-L1.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §20 + CW2-errata E-10; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §1 · inputs: /home/user/dmdd-solid/code/CW2/inputs/GaAs/ (DFPT); [FT] low-T ω_L, ω_T, ε_∞, a: to collect · depends: DC-19, INF-12.

#### DC-35. Crystal NR bremsstrahlung: Z*_κ(ω) at zero macroscopic field for ω ∈ [0.05, E_g], n_r(ω), dℛ/dω_γdω_ph by (W.13) (GaAs (Si, Ge); P3)
- **Physics.** A recoiling ion in a polar crystal radiates through its dynamical Born charge.
- **Quantity and units.** Z*_κ(ω) (e), dℛ/dω_γdω_ph.
- **Method and approximation level.** RPA then ALDA; scissor to the measured gap; imaginary-axis fits; η = 10–20 meV near E_g. Code: TDDFPT mixed E(ω)–u response (zstar_eu generalised, rtsc/sth).
- **Convergence and acceptance.** Z*(0), ε_∞ vs static DFPT to 1%; Σ_κZ*(ω) → 0 (ω → 0) and → ΣZ_κ (ω → ∞); η → 0 extrapolation.
- **Pitfalls.** PBE gap misplaces the resonance; macroscopic-field response double counts the photon line.
- **Result goes to.** Ch 11/12; WP3 (W.13) relevance.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §15; /home/user/dmdd-solid/returns/R8/WP3-v3.md §8 Bremsstrahlung · inputs: to write · depends: INF-5, DC-19, DC-21.

#### DC-36. Reflection/refraction force above σ_crit for the MICROSCOPE cylinders (CW2.25) and the DWBA for density fluctuations ⟨δnδn⟩ (Pt/Ti cylinders; random media; P3)
- **Physics.** Strongly interacting DM reflects coherently off macroscopic bodies, exerting a wind force.
- **Quantity and units.** Δa(σ_χN, m_χ) (m s⁻²).
- **Method and approximation level.** optical potential, specular faces, 1D transfer matrices along local normals. Code: ≈ 300-line transfer-matrix + 4D Monte-Carlo code (box).
- **Convergence and acceptance.** Born regime reproduces WP7-B2 (B2.3.2).
- **Pitfalls.** λ_dB-scale roughness makes reflection diffuse; multiple reflections between nested cylinders.
- **Result goes to.** Ch 16/21 (literature bound status); LIMITS B2-L4.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §22; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §3 · inputs: to write; ⟨δnδn⟩ from SAXS/USAXS data · depends: none.

#### DC-37. κ_URF in MOF cells (three-phonon branching with angular-momentum labels, (CW2.27′)) and giant-moment 4f orbit–lattice amplitudes ∂⟨s_e,L⟩/∂u (CASSCF-SO on embedded clusters) (chiral MOFs; SMMs; P3)
- **Physics.** Chiral phonons carry angular momentum; its survival through decay sets the URF signal.
- **Quantity and units.** Γ_{λ→λ′λ″} (s⁻¹), κ_URF (dimensionless).
- **Method and approximation level.** FGR three-phonon, harmonic L^ph. Code: phono3py fc3 (DFT or MLIP), sparse solve; CASSCF-SO.
- **Convergence and acceptance.** grid, fc3 cutoff, smearing; t_obs sensitivity.
- **Pitfalls.** L^ph gauge-dependent in degenerate subspaces; recompute labels per daughter.
- **Result goes to.** Ch 16; LIMITS B2-L8.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW2.md §25 + /home/user/dmdd-solid/returns/R16/CW2-errata.md E-11 · inputs: to write · depends: INF-12, INF-7.

### C. Fano/edge shell and WP0 extensions

#### DC-38. Γ_Λ₀/δ map over (q, ω), Fano coefficient c_ν^F(Λ₀), K_ν ≥ 0 test, d11 edge-shell and onset-shell masks (GaAs (and Si); P2)
- **Physics.** Near the window edge an X0 seed hybridises with the phonon-assisted continuum; the Fano coefficient is perturbatively valid only where Γ/δ is small.
- **Quantity and units.** Γ_n(k) (meV), δ_Λ₀ (meV), Γ/δ on the WP3 §M10 grid; c_ν^F (dimensionless); K_ν; masks.
- **Method and approximation level.** n_g = 2 on-shell Fan–Migdal width, harmonic, DFPT-screened g, KS bands + scissor/valley offsets; T = 10 K; 16 spinor WFs (GaAs), 8 sp³ (Si). Code: QE fork (FR SOC) DFPT 6³ + EPW elecselfen (fine q 100³, 13824 shell k) + the WP3 response code (c^F from M^(2)).
- **Convergence and acceptance.** Γ_n(k) to 5% under fine q 80³ → 100³ (GaAs), 40³ → 60³ (Si); degaussw 10 → 5 → 2.5 meV; band interpolation < 10 meV within 3 eV; c^F to 10% under m-sum truncation; Si must return c^F = 0 (O4-d7).
- **Pitfalls.** PBE GaAs L, X valleys too low and gap ≈ 0.5 eV (scissor + valley offsets consistently); lpolar mandatory; one gauge for ρ, g, a^off; Kramers matrix form; identical σ in Γ and S^{X+}; absolute fermi_energy/dis_froz_max placeholders.
- **Result goes to.** Ch 18 (Fano term); WP5 (W15)/θ_𝔉; O4 §9; LIMITS L-Fano.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW3.md §2.3 + /home/user/dmdd-solid/returns/R16/CW3-errata.md §1.4 (onset shells, pitfall (6)) · inputs: /home/user/dmdd-solid/code/CW3/fork/{GaAs-LE76,Si-LE76}/{scf,ph,nscf,epw}.in, /home/user/dmdd-solid/code/CW3/fork/mk_shell_k.py (reset fermi_energy and dis_froz_max from scf/nscf output) · depends: c^F part: INF-3 (WP3 response code); Γ part: none.

#### DC-39. All-electron orbit–orbit f-sum shift δ_oo(q) (CW3.3) and total δ_rel = δ_mv + δ_oo (Si, Ge; P3)
- **Physics.** Breit–Pauli orbit–orbit terms shift the f-sum rule at O(α²⟨p²⟩/m²).
- **Quantity and units.** δ_oo(q) (relative), q ∈ [1, 100] keV.
- **Method and approximation level.** HF static pair density 𝒮_st(k) in momentum space. Code: pyscf X2C-HF (sfx2c1e), uncontracted ANO-RCC/cc-pwCV5Z; PAW crystal valence correction.
- **Convergence and acceptance.** E_ee to 10⁻⁴ under cardinal 4 → 5; k integral to 10⁻³ (radial grid to 50/a₀ for Ge 1s).
- **Pitfalls.** never subtract the uniform Hartree term by hand; core cusp needs tight exponents; include δ_mv and δ_oo together.
- **Result goes to.** Ch 4.3; WP0 (4.6″); WP1 [E11]; LIMITS L17.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW3.md §3.2 + CW3-errata V5 · inputs: to write · depends: crystal part only: INF-6.

#### DC-40. Relaxed electron-channel static step 1 − ε_e⁻¹(q,0) = clamped step + 𝒢_GS(q) (CW3.4) with the electron-following charge Z^(e)_κ(q) from frozen-phonon supercells (Si, GaAs; P3)
- **Physics.** An electron-only probe compresses neutral matter: the lattice term diverges as 1/q².
- **Quantity and units.** 𝒢_GS(q) and Z^(e)_κ(q) (e).
- **Method and approximation level.** adiabatic, harmonic, one phonon, DFPT-screened; clamped term RPA+LFE. Code: pw.x + pp.x frozen-phonon supercells (Si 1×1×N, N = 2…8) or DFPT induced density.
- **Convergence and acceptance.** Z^(e) to 1%; 𝒢_GS to 2% under q-grid refinement; q → 0 against Ω²_{P,e}/(c_Lq)².
- **Pitfalls.** add frozen cores back; ASR violations give spurious divergences; unreduced q.
- **Result goes to.** Ch 4.4/8; LIMITS L17′.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW3.md §3.3 + /home/user/dmdd-solid/returns/R16/CW3-errata.md §1.5 · inputs: to write · depends: DC-19 (phonons); clamped step from DC-28.

### D. Spin, superconducting, Dirac, low-dimensional and molecular targets

#### DC-41. Al BCS response: GRPA vertex 𝔳_GRPA(q,ω) on the WP4 [4.2] grid; full Im ε^BCS, its KK transform and the 𝔰_BCS-corrected L^BCS table (Al; P2)
- **Physics.** Superconducting gap changes the electron loss function near 2Δ; the conserving (GRPA) vertex restores the Goldstone cancellation.
- **Quantity and units.** 𝔳_GRPA (dimensionless); L^BCS(q,ω) on y = ω/Δ ∈ [2, 50], qv_F/Δ up to 10³.
- **Method and approximation level.** clean BCS, RPA + pairing ladder, quasiclassical; Lindhard normal state incl. ω′ > qv_F. Code: 2-D quadrature (Gauss–Legendre in μ, adaptive ξ) + log-grid KK (box).
- **Convergence and acceptance.** 𝔳 to 10⁻³ under grid doubling; KK tail < 10⁻³ of Re ε; reproduces WP4-K2 and 2609.06423 Eq. (7) with the ladder off.
- **Pitfalls.** sign of i0 on the second pole; Π^N₂₂(0,0) from the same cutoff; never mix bare and GRPA bubbles between Im and Re.
- **Result goes to.** Ch 15; WP6 SC row (type-Δ nuisance); LIMITS L15.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §1, §8 · inputs: to write (inputs N(0), v_F, Δ_BCS only) · depends: none.

#### DC-42. Amorphous WSi: ⟨L⟩(q,ω) from RPA+LFE on MLIP-quenched cells, Kubo–Greenwood σ₁, and Δ_BCS inhomogeneity P_Δ by BdG (a-W_xSi_{1−x}; P3)
- **Physics.** Disorder in a superconducting film changes both the loss function and the local gap.
- **Quantity and units.** ⟨L⟩(q,ω) for q = 0.5–5 keV, ω = 2Δ–50 eV; P_Δ.
- **Method and approximation level.** τ nB=0|X=RPA+LFE; ref = glass; BdG with U fitted to the film T_c. Code: MACE/DeePMD on AIMD → QE scf/nscf → Yambo/BerkeleyGW ε_GG′ → Wannier90 TB + attractive-U BdG.
- **Convergence and acceptance.** ⟨L⟩ to 5% across quenches and 512 → 1000 atoms; f-sum per q to 2%; σ₁ vs film ellipsometry/sheet resistance.
- **Pitfalls.** no RTA/Mermin anywhere (K31); semicore W ≳ 35 eV; keep ε⁻¹₀₀, not 1/ε₀₀.
- **Result goes to.** Ch 15; LIMITS G9 (RG2).
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §2 · inputs: to write · depends: INF-13, INF-1.

#### DC-43. Magnon sector: two-magnon S^(2m)(q,ω) with the 1/S ladder and bound states (RG3); LSWT beyond Larmor (anisotropic, dipolar, AFM; demag) for absorption; magnon FOM r_2m and ΔS (YIG, NiO, MnF₂, α-RuCl₃ (benchmarks); P2)
- **Physics.** Magnon final-state interactions and bound states change two-magnon emission; anisotropy and dipolar fields move the uniform mode.
- **Quantity and units.** S^(2m)(q,ω) (eV⁻¹); bound-state energies (meV) and weights; ω_ν(k→0), ℰ^α_ν(0).
- **Method and approximation level.** ref = LSWT + pair ladder (cubic vertex for noncollinear order); Ewald dipolar with the Polder–Kittel shape limit. Code: SpinW/Sunny (Colpa) + linear solve of (3.1) on 30³–40³ k.
- **Convergence and acceptance.** ⟨𝐒²⟩ sum rule to 1%; bound-state energy to 1% under N_k doubling; FM limit reproduces (B2.5.2)–(B2.5.3); two-sublattice test (20.1).
- **Pitfalls.** |𝐒| = ½ uncontrolled; k → 0 and shape limits do not commute; Colpa needs a positive-definite boson matrix.
- **Result goes to.** Ch 14; WP6 magnon row (LE-156); LIMITS B2-L6.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §3, §20; /home/user/dmdd-solid/returns/R16/CW7.md §7; /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §5 · inputs: to write · depends: DC-44 (exchange inputs).

#### DC-44. Magnet inputs from DFT+U: exchange J^ex (four-state or TB2J), single-ion anisotropy, g tensors where no INS/ESR fit exists (YIG, NiO, MnO, Cr₂O₃, NiPS₃; P2)
- **Physics.** Spin-wave dispersions follow from the exchange constants; measured fits are absent for several survivors.
- **Quantity and units.** J_ij (meV), D (meV), g.
- **Method and approximation level.** DFT+U with linear-response U; magnetic unit cell. Code: QE DFT+U (hp.x for U) + TB2J on Wannier functions.
- **Convergence and acceptance.** reproduce measured T_N/T_C and the INS magnon band where available.
- **Pitfalls.** U dependence (report spread); orbital moments in Cr³⁺/Ni²⁺.
- **Result goes to.** Ch 14; WP8-U magnet rows.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §3 (Method), §20 · inputs: to write; YIG a = 12.3750 Å from /home/user/dmdd-solid/state/DATA-ADDENDA.csv · depends: none.

#### DC-45. Non-dipole orbital magnetic form factors ⟨j_K(q)⟩ (K = 0…6) and multiplet-projected matrix elements for SOC ions (SOC ions of the WP8-U survivors; P3)
- **Physics.** Orbital moments of SOC ions scatter with non-dipole form factors at large q.
- **Quantity and units.** ⟨j_K(q)⟩ (dimensionless).
- **Method and approximation level.** single ion, ground J multiplet, crystal field within J. Code: GRASP Dirac–Fock or QE DFT+U Wannier projections (_FR) + sympy Racah algebra.
- **Convergence and acceptance.** ⟨j₀(0)⟩ = 1; orbital-moment sum rules to 10⁻³; tabulated dipole form factors to 2% for q ≤ 1 keV.
- **Pitfalls.** DM operator couples to the orbital current, not ℓ×density.
- **Result goes to.** Ch 14; WP8-U F^mag column.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §7 · inputs: to write · depends: none.

#### DC-46. Finite-q optical activity 𝒢_OA(q,ω) and S_{j^αj^β}(±q,ω) with SOC (current vertex with the non-local commutator) (Te or α-SiO₂; one magnetoelectric target; P3)
- **Physics.** In chiral crystals the response has a part odd in q.
- **Quantity and units.** 𝒢_OA (dimensionless), q ≤ 10 keV, ω ≤ 50 eV.
- **Method and approximation level.** X=RPA+LFE longitudinal; transverse IP+LFE; SOC (_FR). Code: QE noncollinear → EXCEED-DM-type IP code extended to the current vertex → Yambo LFE.
- **Convergence and acceptance.** odd part vanishes in a centrosymmetric control (Si); k 16³–24³ until odd part changes < 5%; linear order vs DFPT gyrotropy.
- **Pitfalls.** sign of q convention (CONVENTIONS §3); gauge at ±q.
- **Result goes to.** Ch 16; LIMITS RG4.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §4 · inputs: to write · depends: INF-9, INF-1.

#### DC-47. Finite-q multiplet transition densities |⟨F|ñ_e(q)|I⟩|² for the NV⁻ manifold (QDET/CRPA + CI) (diamond NV⁻; P3)
- **Physics.** Colour-centre multiplets are correlated few-electron states; DM excites them through the density.
- **Quantity and units.** |⟨F|ñ(q)|I⟩|² on |q| ∈ [0.5, 30] keV × 590 directions.
- **Method and approximation level.** Condon, active space 4–6 orbitals. Code: QE PBE/HSE 512–1000-atom supercells + WEST QDET + full CI + new γ^FI × plane-wave form-factor module.
- **Convergence and acceptance.** multiplet energies to 0.05 eV vs ZPL and ¹E–¹A₁ data; 5% under active-space and supercell enlargement.
- **Pitfalls.** QDET double counting; ³A₂/³E orbital relaxation; q_max below the SG15 pseudisation cutoff (≈ 25 keV for C).
- **Result goes to.** Ch 16; LIMITS RG5.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §5 · inputs: to write · depends: none.

#### DC-48. Anisotropic massive-Dirac ZrTe₅: G₀W₀ (SOC) fit of k·p parameters and ε_bg,ii; analytic Elliott–Sommerfeld threshold; model BSE on a log-graded radial k grid; beyond-ladder spread (ZrTe₅ (Bi₂Se₃ ε_bg); P3)
- **Physics.** Coulomb attraction in a small-gap Dirac material at α̃ ~ 1 creates a Rydberg series below 2Δ_D.
- **Quantity and units.** L(q,ω) for |q| ≤ Λ_D, 2Δ_D ≤ √𝓈 ≤ 2Δ_D + 50 meV; Ry_D, bound-state energies.
- **Method and approximation level.** static-screened ladder on G₀W₀-corrected k·p bands; remote bands only in ε_bg. Code: QE + Yambo G₀W₀ SOC (12-atom cell, 12×12×4 + refinement); model codes (box).
- **Convergence and acceptance.** Ry_D and first three bound states to 5% under k_min → k_min/2; continuum to 2% across matching; model f-sum to 10⁻³.
- **Pitfalls.** uniform grids give a spurious 'no bound state'; ε_bg double counting; ε₀ vs ε_∞ choice stated.
- **Result goes to.** Ch 16; WP8-U eps_bg cells; LIMITS RG6.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4-errata.md A12 (replaces CW4 §6) · inputs: to write · depends: INF-1.

#### DC-49. Re-plot of the 1708.08929 / 1910.02091 scattering and absorption reaches with ε_bg², ε_bg and the 0.55–0.62 charge renormalisation (ZrTe₅, BNQ-TTF, Yb₃PbO; P2)
- **Physics.** Published Dirac-material reaches used the wrong screening factor.
- **Quantity and units.** σ̄_lim^URF = σ̄_lim^src·N_src/N_URF vs m_χ.
- **Method and approximation level.** their model, only the screening rule changed. Code: re-implementation of 1910.02091 Eqs. (3.13)–(3.14) (box).
- **Convergence and acceptance.** reproduce the published curve with their rule to 5% first.
- **Pitfalls.** their typo q_x²v_{F,z}²; half-gap reading of Δ (LE-106).
- **Result goes to.** Ch 16, Ch 21; LIMITS L16.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §9 · inputs: their Tables 1–2; code: to write · depends: none.

#### DC-50. Superconducting Holstein absorption σ₁^{S,(2,1)}(ω) with Eliashberg spectral functions (EPW α²F, α²F_tr) (Al, Nb; P3)
- **Physics.** Above 2Δ a photon-like excitation is absorbed by breaking a pair with phonon emission.
- **Quantity and units.** σ₁(ω)/σ_N.
- **Method and approximation level.** n_g = 2, sector (2,1), isotropic Eliashberg. Code: QE → ph (8³) → EPW (Al k 60³/q 30³; Nb 40³/20³) → eliashberg (Padé or real axis) → (A2.2) integral.
- **Convergence and acceptance.** T_c within 10% with one μ*; σ₁ to 5% under fine-grid doubling; σ₁^N vs Al optical data to 20%.
- **Pitfalls.** Padé artefacts near 2Δ; transport weight (1 − cos θ), not α²F.
- **Result goes to.** Ch 15; LIMITS LB1-10.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §12; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §9 · inputs: to write · depends: none.

#### DC-51. Disorder-averaged donor response ⟨S^D(q,ω)⟩ of Si:P near the impurity band (multivalley EMT tight binding, 10⁴–10⁵ sites) with DFT central-cell check; impact number of the 2212.04504 misprint (Si:P (n_D = 10¹⁸, 1.8×10¹⁸ cm⁻³); P3)
- **Physics.** Near the metal–insulator transition donor clusters and valley–orbit lines reshape the dopant response.
- **Quantity and units.** ⟨S^D(q,ω)⟩ (eV⁻¹ per donor).
- **Method and approximation level.** Poisson donor positions, Hartree mean field, host screening (1.2); 100 realisations. Code: Lanczos/KPM on Hubbard–Anderson TB; QE 1000–4000-atom Si:P clusters.
- **Convergence and acceptance.** S to 5% under N and realisations; TRK sum per donor.
- **Pitfalls.** single-valley envelopes miss interference; compensation changes occupation.
- **Result goes to.** Ch 16; LIMITS LB1-11.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §13; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §10 · inputs: to write · depends: none.

#### DC-52. Molecular crystals: periodic GW-BSE vs Frenkel/Hückel/PPP transition densities, charge-transfer weight θ²_CT, Frenkel form-factor tables (frenkel-ff) (anthracene, t-stilbene; P3)
- **Physics.** Molecular-crystal excitons are Frenkel-like but mix with charge-transfer states.
- **Quantity and units.** ΩS(q,ω) tables (|q| ≤ 30 keV × 590 directions); max|Δ|f|²|/|f|².
- **Method and approximation level.** periodic BSE with intermolecular overlap vs zero-overlap Frenkel truncation. Code: QE + Yambo/BerkeleyGW G₀W₀+BSE (50–100 atoms, k 4³, 200 bands); PySCF/ORCA molecular TDDFT; new frenkel-ff module.
- **Convergence and acceptance.** exciton energies to 50 meV under band/k doubling; partial f-sum per molecule to 2%.
- **Pitfalls.** vdW geometry; PPP fails for σ electrons at q ≳ 10 keV.
- **Result goes to.** Ch 16; LIMITS WP7-B1 E5.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §16; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §2 · inputs: to write (CSD structures) · depends: INF-1, INF-9.

#### DC-53. Graphene/CNT vacuum ejection: rate-weighted OPW factor R_OPW(E_kin) with all occupied orbitals; FSI with screened-hole scattering states; low-D RPA tables (lowd-rpa) for sheets, tubes, stacks, quantum dots (graphene, CNT, layered stacks, QDs; P3)
- **Physics.** Low-dimensional targets have their own Coulomb kernels, plasmons and ejection channels.
- **Quantity and units.** R_OPW (dimensionless); S(q_∥,q_z,ω); S^QD(q,ω).
- **Method and approximation level.** frozen orbitals, single orthogonalised continuum; d = 1, 2 RPA with arbitrary v_C^(d). Code: QE + Wannier90 MLWFs + FFT overlaps; lowd-rpa module; EFA solver; Yambo slab cutoff cross-check.
- **Convergence and acceptance.** R_OPW to 1% under direction and q-grid doubling; orthogonality to 10⁻⁶; projected sum rule (C2d) to 10⁻³; Dirac check C6a to 10⁻⁴.
- **Pitfalls.** 1s overlap from an AE orbital; do not multiply OPW by a Sommerfeld factor without a common final state.
- **Result goes to.** Ch 16; LIMITS LB1-6.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4-errata.md A2; /home/user/dmdd-solid/returns/R16/CW4.md §17; /home/user/dmdd-solid/returns/R12/WP7-B1-v2.md §3–§6 · inputs: to write · depends: INF-9.

#### DC-54. Recast of 2401.11971 (CRDM) limits with the exact density-row ratio (1 − ω²/Q²)² and the transverse row (Si, Ge; P3)
- **Physics.** For relativistic DM the longitudinal response must be evaluated off the light cone and the transverse row adds.
- **Quantity and units.** R_URF/R_src per target and flux.
- **Method and approximation level.** their ε_L (RPA); ε_T Lindhard-transverse. Code: re-implementation of their Eqs. (4)–(6) + transverse term (box).
- **Convergence and acceptance.** reproduce their Fig. 3 with their Eq. (5) to 5% first.
- **Pitfalls.** Cherenkov-type pole (iη scan); F_DM at Q² − ω².
- **Result goes to.** Ch 21; LIMITS LB1-13.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW4.md §18 + CW4-errata A4 · inputs: their CRDM flux tables; code: to write · depends: none.

### E. Defects, TLS, cascades, yields, low-energy excess

#### DC-55. Ohmic electron-bath coupling α_ohm of tunnelling defects from eigenphases of S_R S_L† (CW5-6) (crowdion in W, H in Nb, TLS in Al/AlOx, WSi; P3)
- **Physics.** A defect that changes configuration shakes the Fermi sea (orthogonality catastrophe), damping its tunnelling.
- **Quantity and units.** α_ohm (dimensionless).
- **Method and approximation level.** Anderson overlap ln|⟨Ψ_L|Ψ_R⟩| vs ln L, α = −slope. Code: route 2: QE PBE supercells (54/128/250 atoms, SG15 W semicore) + Slater-determinant overlaps; route 1: KKR (JuKKR/AkaiKKR).
- **Convergence and acceptance.** Born limit α = 4(N_σVΩ)² (per-spin DOS); 1D chain check (CW5-C8).
- **Pitfalls.** k-sampling and smearing destroy the orthogonality catastrophe (fixed occupations); identical host relaxation; per-spin DOS.
- **Result goes to.** Ch 16; LIMITS L44.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §3.1 + CW5-errata A21 · inputs: to write (rtsc layout) · depends: DC-56 (relaxed end states).

#### DC-56. Release paths of eV-scale defects: Huang–Rhys S_HR,k, E_reorg, λ_eff along the MEP, ring-polymer instanton action; production catalogue (50 paths/material) and KMC rates ℛ_rel(E,t,T); ΔSCF charge-state variant (Si, Ge close Frenkel pairs; Al SIA; P2)
- **Physics.** Whether stored defect energy relaxes at mK depends on tunnelling exponents and the reorganisation of local modes.
- **Quantity and units.** S_HR,k (dimensionless), E_reorg (meV), λ_eff, 𝒮_inst; ℛ_rel(E,t,T) (s⁻¹).
- **Method and approximation level.** harmonic about each minimum; CI-NEB 9 images to 5 meV/Å; FFT line shape; T → 0 instanton. Code: QE pw.x/neb.x (64-atom pilot) + phonopy Hessians + i-PI instantons on the MLIP; KMC.
- **Convergence and acceptance.** ecut 30/40/50 Ry, k 2³ vs 3³; 216-atom repeat for one path; 50 paths checked against DFT; θ_λ, θ_S nuisances.
- **Pitfalls.** charged close pairs need finite-size corrections; same quench and E^conf table as p_st (T-1 (ii)); end-state assignment.
- **Result goes to.** Ch 19/20; WP7-T verdicts (LE-129); LIMITS L44–L46.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §3.2–§3.3, §4.4; /home/user/dmdd-solid/returns/R12/WP7-T-v2.md §4.6 · inputs: /home/user/dmdd-solid/code/CW5/LE-128/{scf.in, neb.in, notes.txt} (pilot); production: to write · depends: INF-7 (MLIP end states, instantons), DC-61 (quench protocol, shared E^conf table).

#### DC-57. Crowdion in W (Peierls profile, polaron narrowing S_pol, FK mass, strain interaction with the parent vacancy) and Al ⟨100⟩ dumbbell / cluster 1D glide (W, Al; P3)
- **Physics.** Crowdions can move coherently at mK if phonon and electron dressing leave a finite band.
- **Quantity and units.** V_P (meV), W_eff, S_pol(T), R₀.
- **Method and approximation level.** linear coupling, FK mapping. Code: QE PBE 250-atom bcc CI-NEB + Hessians; MLIP-MD 10–100 K + instantons.
- **Convergence and acceptance.** k/smearing noise < 0.1 meV/cell; sinusoidal NEB profile check.
- **Pitfalls.** meV barriers need fixed-smearing differences on identical meshes.
- **Result goes to.** Ch 16; LIMITS L31.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §3.8; /home/user/dmdd-solid/returns/R12/WP7-T-v2.md §3.4 · inputs: to write · depends: INF-7.

#### DC-58. DM–TLS core vertex 𝔣^def_e(q) = ⟨R|n_e(q)|R⟩ − ⟨L|n_e(q)|L⟩ for real a-SiO₂ TLS (Method A: two SCFs; Method B: one Γ ph.x) (a-SiO₂; P3)
- **Physics.** A TLS couples to DM through the change in electron density between its two configurations.
- **Quantity and units.** ⟨|𝔣^def_e(q)|²⟩ (e²) on the WP7-T §2.7 q grid; Re(a*B).
- **Method and approximation level.** GS density row, adiabatic, scr = DFPT (no extra ε⁻¹). Code: QE pw.x/ph.x 216-atom cells (rtsc layout).
- **Convergence and acceptance.** 𝔣 to 2% under ecut +10 Ry and 216 → 648 atoms; ⟨|𝔣|²⟩ to 10% over ≥ 10² TLS.
- **Pitfalls.** below 2π/L add −iq·Δ𝐩_e(1 − 1/ε_∞) analytically; never rebuild δρ from Z*; K_POINTS automatic 1 1 1 (not gamma) for ph.x.
- **Result goes to.** Ch 16 TLS; LIMITS DM–TLS row.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §3.10 + CW5-errata A34 · inputs: /home/user/dmdd-solid/code/CW5/LE-137/{scf.in, ph.in, notes.txt} · depends: DC-59 (NEB-identified TLS from MLIP glasses).

#### DC-59. TLS ensemble sampling: landscape filtering / swap-MC on MLIP glasses (≳ 10⁸ minimum pairs), NEB, λ_P, γ^def, 𝐩^def; tls_response tables ΩS̄^def (a-SiO₂, AlOx, a-WSi; P3)
- **Physics.** Tunnelling two-level systems in glasses absorb at µeV–meV energies.
- **Quantity and units.** ΩS̄^def(q,ω) on Lebedev ≥ 590 × 60 log|q| × 50 ω.
- **Method and approximation level.** STM-like ensemble from the computed landscape; Hadamard fp by subtraction. Code: MLIP glasses (10³–10⁴-atom cells, ≳ 10⁴ quenches) + NEB + new tls_response module.
- **Convergence and acceptance.** ensemble average to 1%; fp stable to 10⁻³.
- **Pitfalls.** ≳ 10³ TLS per energy decade needs ≳ 10⁸ pairs.
- **Result goes to.** Ch 16; WP7-T tables.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R12/WP7-T-v2.md §2.7 · inputs: to write · depends: INF-13, INF-9.

#### DC-60. Close-collision electronic excitation kernel dP/dω_e(b_imp, E_coll) for Si–Si, Ge–Ge collisions (E_coll 50 eV–5 keV) with the xc nuisance θ_LZ (Si, Ge; P2)
- **Physics.** Below the binary threshold, electronic excitation in a low-energy recoil comes from quasi-molecular level crossings.
- **Quantity and units.** dP/dω_e (eV⁻¹) per (b_imp, E_coll).
- **Method and approximation level.** classical nuclei, TDDFT electrons; projection on GS conduction manifold at t ≈ 20 fs; 64–216 atoms; 20–50 trajectories per point. Code: real-time TDDFT Ehrenfest (Qb@ll, Octopus or SALMON; QE has none) + HSE subset + surface hopping + MRCI Landau–Zener.
- **Convergence and acceptance.** time step ≤ 2 as; grid ≤ 0.2 Å; wake does not re-enter (≥ 15 Å); θ_LZ from HSE/surface hopping/LZ spread.
- **Pitfalls.** adiabatic xc misplaces crossings; Ehrenfest gives means, use projection statistics; switch off MD electronic friction where the kernel acts.
- **Result goes to.** Ch 19; WP5 R3 gap; DC-62.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §2.4; /home/user/dmdd-solid/returns/R13/WP5-v4.md §3.4 · inputs: to write · depends: INF-8.

#### DC-61. NR partition tables P(ℋ, E_st, N_eh | E_R, r̂_R, T), anisotropic E_d(r̂_R) and P_FP, created-phonon spectra (WP5-AUD B-1), E_st with the quench protocol and one shared E^conf table (G-E3) (Si, Ge (then survivors: GAP:E_st1_p_surv, GAP:y_ion_QF); P2)
- **Physics.** A nuclear recoil splits its energy between heat, stored defect energy and ionisation.
- **Quantity and units.** tables on E_R ∈ [1 eV, 10 keV] (40 log) × 100 directions × 100 seeds; dℋ/dω_ph branch-resolved on 0.5 meV.
- **Method and approximation level.** MLIP-MD 10³–10⁵ atoms, 1–10 ps, boundary thermostat; quench by FIRE at fixed cell; ΔZPE from Hessians, booked in ℋ_ph. Code: MLIP (ACE/MACE/NequIP on ~10⁴ PBE/SCAN configs, ZBL-spliced) MD; BO-DFT-MD check.
- **Convergence and acceptance.** force error ≤ 50 meV/Å, energy ≤ 3 meV/atom; E_d bisection to 0.5 eV; created-minus-absorbed spectrum reproduces WP2 (3.6) for x_R ≲ 1; anharmonic residual ≤ 10%; θ_PES from MLIP vs DFT.
- **Pitfalls.** never take E^conf(𝔅₀) from the sampled R_I(0) (138 eV per 4096 atoms); thermostat energy must be recorded with its spectrum.
- **Result goes to.** Ch 19; WP5-v4 L22; LIMITS L36–L38, L43; WP8-U E_st1_p_surv, y_ion_QF cells.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R13/WP5-v4.md §3.4; /home/user/dmdd-solid/returns/R14/WP5-AUD.md §3.1 (protocol), §4 B-1 · inputs: to write · depends: INF-7.

#### DC-62. Charge yield below E_R,th (B-2): P(N_eh | E_R, r̂_R, T) on [20 eV, 1 keV], 𝔶(E_R), F_NR(E_R), P(N_eh = 0) (Si (validation 2303.02196), Ge (2405.10405); P2)
- **Physics.** The ionisation yield of sub-keV nuclear recoils is set by non-adiabatic channels the Lindhard model does not contain.
- **Quantity and units.** 𝔶(E_R) dimensionless, F_NR, P(0), Corr(N_eh, ℋ).
- **Method and approximation level.** three channels flagged (binary, Landau–Zener, momentum-tail linear response); law of total variance. Code: MLIP-MD trajectories with stochastic excitation events from DC-60, converted by P_n(ω_e) of DC-63.
- **Convergence and acceptance.** ≥ 25 log points dense around E_R,th = 352/395 eV; ≥ 1112 trajectories per point; validation (not fit) to 2303.02196 Table II (0.10/0.22/0.46 keV).
- **Pitfalls.** never ω_e/ε_eh^γ; their Y uses the L37 truncation.
- **Result goes to.** Ch 19; LIMITS L43; WP8-R created-charge yield.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R14/WP5-AUD.md §4 B-2 + /home/user/dmdd-solid/returns/R16/CW5-errata.md A5 (≥ 1112 trajectories for 6%) · inputs: to write · depends: DC-60, DC-61, DC-63.

#### DC-63. Ab initio hot-carrier cascade: G₀W₀ bands, full-frequency ε⁻¹_GG′(p,ω) to 60–100 eV, ii kernel (W1′), EPW e–ph kernel, full-band cascade → P_n(q,ω,T), ε_eh, F_eh, decomposition (EF7) (Si, Ge, GaAs; P2)
- **Physics.** The pair-creation energy and Fano factor follow from the competition of impact ionisation and phonon emission over the whole cascade.
- **Quantity and units.** ε_eh (eV), F_eh; P_n on ω ∈ [E_g, 50 eV] (50 meV), |q| ∈ [0, 25αm_e], 5 temperatures.
- **Method and approximation level.** G₀W₀ QPs (θ_GW), RPA+LFE, DFPT g with WP5-cp1–cp3; energy-only reduction for n_gen ≥ 2 (θ_{R-k}); k-resolved first generation with law-of-total-variance estimator; plasmon channel explicit. Code: QE + BerkeleyGW (epsilon, sigma) or qe-rtsc GW path; EPW; INF-14 cascade solver.
- **Convergence and acceptance.** (c1) bin halving |Δε|/ε < 10⁻³, |ΔF|/F < 3×10⁻³; (c2) energy cap; (c3) asymptote windows < 10⁻⁴; (c4) k-mesh; (c5) identities; N_s until SE(F)/F < 0.5%. Validation gate: Si ε_eh = 3.749 ± 0.001 eV, F = 0.119 ± 0.002 (2004.11499), Si quantum yield 3–8 eV and 50–1500 eV, Ge ε_eh(77 K).
- **Pitfalls.** ω₀ on the grid (integer bins to < 1%); Z_kn applied once; no mixed DFT/QP energies.
- **Result goes to.** Ch 18; GAP-EF-v2 predictions replaced; LIMITS L23, L-EF rows; WP8-U ε_eh/F_eh cells.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R13/WP5-v4.md §2; /home/user/dmdd-solid/returns/R16/GAP-EF-v2.md §5 + /home/user/dmdd-solid/returns/R16/GAP-EF-v2-errata.md R-13 · inputs: to write · depends: INF-1, INF-4 (quadrupoles), INF-14.

#### DC-64. Ab initio ε_eh and F_eh for wide-gap and polar survivors (priority Al₂O₃, CaWO₄, LiF, NaF; then 4H-SiC F, C, 3C-SiC, GaN, AlN, TeO₂) (Al₂O₃, CaWO₄, LiF, NaF, 4H-SiC, C, 3C-SiC, GaN, AlN, TeO₂; P2)
- **Physics.** Where the universal-𝒜_ph model is least trustworthy (polar, stiff lattices) only the full calculation gives ε_eh and F.
- **Quantity and units.** ε_eh (eV), F_eh per material.
- **Method and approximation level.** as DC-63; Fröhlich g^L, cp1–cp3 for polar cells. Code: as DC-63 + BSE for LiF/NaF excitons; SOC for W.
- **Convergence and acceptance.** DC-63 Si gate passed first; the GAP-EF-v2 residual table (+16% Si … +39% β-Ga₂O₃) as the accuracy reference.
- **Pitfalls.** exciton-dominated halides: ledger pair vs cascade quantum (GE-4).
- **Result goes to.** Ch 17, Ch 18; WP8-U GAP:eps_eh, GAP:F_eh cells; GAP-EF GE-2.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/GAP-EF-v2.md §5 'Per material', 'Recommendation'; https://github.com/ytcs/qe-rtsc/issues/1 · inputs: to write · depends: DC-63 (pipeline validated on Si), INF-1, INF-14, DC-68 (exciton parameters for halides).

#### DC-65. Energy dependence ζ(E) of the ii-rate ratio Γ_ii^NEGF/Γ_ii^(W1) (G₀W₀ Im Σ with and without Z_kn, + SOSEX) and its effect on F_eh through (EF7) (Si; P3)
- **Physics.** Beyond first order in W the impact-ionisation rate definition is ambiguous; only its energy dependence matters after calibration.
- **Quantity and units.** ζ(E) on 50 meV bins, E_th^ii to ≈ 10 eV.
- **Method and approximation level.** N_G ≈ 250, 200 empty bands, full-frequency ε⁻¹, 10³ k per bin. Code: BerkeleyGW G₀W₀ full-frequency + SOSEX; GAP-EF solver.
- **Convergence and acceptance.** ζ(E) to 2% per bin under N_G 250 → 350, bands 200 → 400, k 10³ → 2×10³; SOSEX reported separately.
- **Pitfalls.** Z_kn applied once.
- **Result goes to.** Ch 18; WP5 R1.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §2.2 + CW5-errata A15, §C · inputs: to write · depends: INF-1, DC-63.

#### DC-66. k-resolved osc_k m_k(E) and w_mem(E) for Si between 3 and 8 eV (bound (CW5-1) on the energy-only reduction) (Si; P3)
- **Physics.** The energy-only cascade reduction is exact only if momentum is randomised between energy-changing events.
- **Quantity and units.** osc_k m_k(E), w_mem(E) on 50 meV bins.
- **Method and approximation level.** (H-BGK), first order in w_mem. Code: k-resolved n_gen = 2 subset of DC-63 (EPW + GW rates).
- **Convergence and acceptance.** osc to 10% under k samples 200 → 400 and cascades 10³ → 4×10³.
- **Pitfalls.** max − min of noisy estimates is biased up: use the 5–95% range; Γ_k and Γ_E from one EPW/GW run.
- **Result goes to.** Ch 18; WP5 R2.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §2.3 + CW5-errata §C · inputs: DC-63 outputs · depends: DC-63.

#### DC-67. Semi-analytic cascade library: P_casc(N | x_e, x_h; θ) tables for every Λ-sector and survivor (cascade_gf.py), and the GAP-EF(-v2) rerun on ω₀-commensurate grids (27–42 survivors; P2)
- **Physics.** The discrete cascade model gives the full N_eh distribution, not only its moments.
- **Quantity and units.** P_casc(N|·) tables; corrected ε_eh, F predictions.
- **Method and approximation level.** energy-only (H-EF1), random-k ii, one phonon mode, universal 𝒜_ph. Code: /home/user/dmdd-solid/code/CW7/cascade_gf.py; /home/user/dmdd-solid/code/GAP-EF-v2/{cascade,model,predict}.py.
- **Convergence and acceptance.** CW7 checks C6–C8 (Richardson h/2, ⟨N|Λ⟩); ω₀ commensurate to < 1% (GAP-EF-v2 pitfall p1).
- **Pitfalls.** Φ_t = 0 at x = E_g; aliasing in z; seed dependence of b_N.
- **Result goes to.** Ch 18; WP6 P_casc; WP8-U GAP-EF predictions.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW7.md §4; /home/user/dmdd-solid/returns/R17/WP8-errata.md §14 / IF-EW-1 · inputs: ready (code exists) · depends: none.

#### DC-68. Exciton and capture parameter set: G₀W₀+BSE E_x^b, a_x, oscillator strengths; D⁰X/A⁰X central-cell DFT; cascade-capture σ_cap(E,T,ℰ_b) with EPW rates; deep-level multiphonon capture; the CW5 rate set {k_FX, k_FT, k_XB,j, k_B↓,j, η_X, η_B,j, C_X, γ_XX, C_A(mK)} (Si, Ge (then LiF, NaF, Al₂O₃, CaWO₄); P2)
- **Physics.** At mK the gap energy is released through excitons, shallow traps and luminescence on time scales that decide what a calorimeter sees in its window.
- **Quantity and units.** E_x^b (meV), a_x (nm), C_X(T) (cm³ s⁻¹), σ_cap (cm²), rates (s⁻¹) at 10, 20, 50 mK.
- **Method and approximation level.** G₀W₀+BSE (4–8 v × 4–8 c; polaronic correction when E_x^b ~ ω_LO); effective-mass + central-cell; cascade-capture theory with acoustic/optical emission. Code: BerkeleyGW/Yambo GW+BSE (double-grid, 10⁴–10⁵ k for Si/Ge); QE 216 → 512-atom defect cells; EPW.
- **Convergence and acceptance.** Si/Ge free-exciton binding (E_x^b(Si) stays [UNVERIFIED]); LiF, NaCl exciton peaks; levels to 1 meV under 8³ → 12³; central-cell binding to 10%; rate changes > 10% across 10–50 mK reported as T-dependence.
- **Pitfalls.** name the bimolecular channel (formation vs loss); exciton temperature ≠ lattice temperature at mK; geometry regime of the dense-track law.
- **Result goes to.** Ch 18; WP7-E (E1); WP8-U E_x_b cells; DC-69, DC-79.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/GAP-EF-v2.md §4.3; /home/user/dmdd-solid/returns/R16/CW5.md §2.5 + CW5-errata §C (LE-141); /home/user/dmdd-solid/returns/R12/WP7-E-v3.md §7 (Traps) · inputs: to write · depends: INF-1.

#### DC-69. Event-level charge/exciton kinetics: exciton/EHD rate equations, drift–trap transport with history n_j(t), athermal emission, μ_F-referenced E_trap, E_es; windowed Y_H(t_win) and η^φ_NR tables (Si, Ge; P2)
- **Physics.** The measured charge and heat depend on what happens to pairs and excitons during the readout window.
- **Quantity and units.** P(N^meas, E_stored(t_win) | E_R, r̂_R, ℰ_b, t_win, T); Y_H(t_win) for t_win ∈ {1 µs, 100 µs, 10 ms, 1 s}, E_thr ∈ {0.3, 1, 3, 16} eV.
- **Method and approximation level.** rate equations + G4CMP-class drift; field ionisation ≳ 4×10⁴ V/cm. Code: CMPMC transport_charges (P5, P6) + new exciton module (INF-11) + trap kinetics (DESIGN_NOTES §5).
- **Convergence and acceptance.** validation 1803.02903 (η^φ_NR = 0.952) and 1805.09942 (f_DF); Hecht limit (E10) at constant σ.
- **Pitfalls.** computable only with G-E4 (DC-81) and G-E6 (DC-76).
- **Result goes to.** Ch 18–20; WP7-E §7.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R12/WP7-E-v3.md §7; /home/user/cmpmc/DESIGN_NOTES.md §5 · inputs: to write · depends: INF-10 (item 5), INF-11, DC-68, DC-61, DC-81.

#### DC-70. Dense tracks: EMC-MD with P³M Coulomb among carriers (θ_dense, ΔF_NR) and MLIP-MD + two-temperature model for Ge thermal spikes (Si, Ge; P3)
- **Physics.** At keV energies carriers in a dense track interact, breaking the independent-subtree assumption.
- **Quantity and units.** θ_dense = P(N_eh|E_R)_int/P(N_eh|E_R)_(B2); ΔF_NR.
- **Method and approximation level.** Boltzmann carrier–carrier term; beyond-Markov ion transport. Code: EMC-MD (P³M) + MLIP-MD + TTM (g_ep from EPW).
- **Convergence and acceptance.** EMC-MD 0.1 fs, P³M ≤ 1 nm, ≥ 10³ tracks; TTM grid ≤ 1 nm.
- **Pitfalls.** electronic stopping friction and DC-60 kernel must not both act; thermostat must not absorb spike heat early.
- **Result goes to.** Ch 18/19; WP5 R8.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §2.6 · inputs: to write · depends: INF-7, DC-63, DC-72 (cascade cells).

#### DC-71. Track recombination and the plasma phase: drift–diffusion–Poisson with Auger, exciton formation and SRH on the track geometry; f_A(E_R, ℰ_b), plasma time, Ramo delay (Si, Ge; P3)
- **Physics.** The carrier plasma of a dense track shields the field and loses carriers by Auger recombination.
- **Quantity and units.** f_A (dimensionless), plasma time (ns).
- **Method and approximation level.** (H-p1)–(H-p3) beyond first order. Code: 2D axisymmetric drift–diffusion–Poisson FEM (mesh ≤ 1 nm).
- **Convergence and acceptance.** reduces to (CW5-10) for f_A ≪ 0.1; field ramp 0–250 V/cm.
- **Pitfalls.** C_A at mK [UNVERIFIED].
- **Result goes to.** Ch 18; WP7-E G-E5.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §4.3 · inputs: to write · depends: DC-68 (exciton rates), DC-72 (track geometry).

#### DC-72. Amorphous-pocket size distribution P(N_a | E_R, r̂_R) and recrystallisation barrier spectrum from MLIP cascades (Si, Ge; P3)
- **Physics.** Nuclear cascades leave amorphous pockets whose later recrystallisation releases stored energy.
- **Quantity and units.** P(N_a|E_R), barrier spectrum (eV).
- **Method and approximation level.** ≥ 10³ cascades per energy at E_R = 0.2–20 keV. Code: MLIP-MD (ZBL-spliced) 10⁵–10⁶ atoms, 10–50 ps; NEB/accelerated MD on 10² pockets.
- **Convergence and acceptance.** two cluster thresholds reported; TTM coupling for Ge.
- **Pitfalls.** cluster definition changes N_a by ~2×; one E^conf table with E_st.
- **Result goes to.** Ch 19/20; WP7-E G-E8.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §4.5 · inputs: to write · depends: INF-7, DC-61 (quench protocol).

#### DC-73. Ionic targets and colour centres: STE and F–H adiabatic surfaces (constrained hybrid DFT), p_FH(T) at mK, p_surv of close F–H pairs, E_d(r̂) of the anion sublattice, F-band cross sections (LiF, NaF, MgO, LiH (NaI shares the method); P3)
- **Physics.** In ionic crystals electronic energy can be stored as Frenkel defects via self-trapped excitons.
- **Quantity and units.** p_FH(T), p_surv, Y_CC(E_R) tables.
- **Method and approximation level.** hybrid fraction 0.25 → 0.40; ≥ 10³ FSSH trajectories. Code: QE HSE/PBE0 ΔSCF (64 → 216 atoms) + decoherence-corrected FSSH + MLIP/DFT MD + kMC + BSE.
- **Convergence and acceptance.** p_FH to ±10%; F–H separations to third neighbour.
- **Pitfalls.** STE on/off-centre depends on hybrid fraction; finite-size electrostatics for charged components; only athermal channel at mK.
- **Result goes to.** Ch 16/19; WP7-E G-E1; LIMITS B2-L10.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §4.1 + CW5-errata §C (LE-144, LE-151); /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §9 · inputs: to write · depends: INF-7, INF-1 (BSE).

#### DC-74. Low-energy-excess model inputs: FEM cooldown stress U_el per component with (Γ_min, Γ_max); cured-epoxy and interface MLIP event-energy law; avalanche branching b_br by KMC on the release catalogue driven by phonon-MC pulses (Si/Ge crystals in holders with glue; P2)
- **Physics.** Stress relaxation in holders and glue is the leading candidate for the low-energy excess.
- **Quantity and units.** U_rel (J), ln Γ spread; event-energy law p(E); b_br (dimensionless).
- **Method and approximation level.** FEM 300 K → 10 mK; MD for event energies, not rates; first-generation linear branching. Code: FEM (thermo-elastic) + ACE/NequIP epoxy MLIP (10⁶ atoms) + KMC + CMPMC phonon pulses.
- **Convergence and acceptance.** U_el to 5% under mesh ×2; event law stable 10⁶ → 4×10⁶ atoms; b_br to 10% under catalogue 50 → 100, packets 10⁵ → 4×10⁵, box L → 2L.
- **Pitfalls.** MD reaches ns only; glue structure depends on curing; incomplete catalogue biases b_br low; bath and pulse must not drive the same rate.
- **Result goes to.** Ch 20; WP7-E G-E2; WP8-F G-F3.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §3.5, §4.2 + CW5-errata §C (LE-131, LE-145) · inputs: to write (C_ij(T), α(T) data for crystal, glue, holder) · depends: INF-10 (CMPMC transport), DC-56 (catalogue).

#### DC-75. Mark sufficiency test of (H-E6): ΔP between full and mark-resampled microstates (Si; P3)
- **Physics.** The two-stage factorisation needs the prompt marks to carry all information the later stage uses.
- **Quantity and units.** ΔP in N^meas and E_sig (dimensionless).
- **Method and approximation level.** n_traj = 2p(1 − p)(z/ΔP)² per arm. Code: DC-69 event simulation with common random numbers.
- **Convergence and acceptance.** 2σ resolution ΔP = 0.01 at p = 0.5.
- **Pitfalls.** ΔP = 0 does not imply sufficiency.
- **Result goes to.** Ch 18; WP7-E G-E9.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW5.md §4.6 + CW5-errata A32, §C · inputs: to write · depends: DC-69.

#### DC-76. Athermal emission Γ^em_j (phonon ionisation of D⁰/A⁰ and H⁻-like D⁻/A⁺, impact ionisation σ_ii(u)) and space-charge nonlinearity ξ_SC(t) over an exposure history (Si, Ge; P3)
- **Physics.** Trapped charge distorts the field and is re-emitted athermally by phonons and hot carriers.
- **Quantity and units.** Γ^em_j (s⁻¹), ξ_SC (dimensionless).
- **Method and approximation level.** Fermi golden rule one-phonon absorption with Ξ; Born impact cross section; 1-D Poisson. Code: closed-form effective-mass cross sections + QE 216-atom Si:P central cell + CMPMC trapping extended by DESIGN_NOTES §5 + run-sequence driver.
- **Convergence and acceptance.** Poisson dz ≤ d/200; sequence length until ξ_SC saturates.
- **Pitfalls.** constant-λ trapping cannot produce history; flashing creates D⁻/A⁺ populations.
- **Result goes to.** Ch 20; WP7-E G-E6.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW6.md §6 + /home/user/dmdd-solid/returns/R16/CW6-errata.md (§6 replacement row) · inputs: to write (rtsc layout for the central cell) · depends: INF-10 (item 5).

#### DC-77. Bond breaking in molecular solids: S_int, S_CM, cage-escape p_esc by MLIP MD (10³ trajectories per (E_int, r̂)) (molecular crystals (D5); P3)
- **Physics.** DM can dissociate molecules in a crystal if the fragments escape the cage.
- **Quantity and units.** p_esc, p_diss(Λ).
- **Method and approximation level.** impulse limit with bound CM. Code: Morse/ab initio potentials, phonopy/PIMD, MLIP MD.
- **Convergence and acceptance.** ≥ 10³ trajectories per point.
- **Pitfalls.** recoil-free fraction ≈ 0.
- **Result goes to.** Ch 16.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §10 · inputs: to write · depends: INF-7.

### F. Phonon and charge transport (CMPMC)

#### DC-78. Collection kernels 𝒦_1, 𝒦_2(f; r_ev) for a stated geometry, then ζ_O, ζ_gap, σ_pos, r_coll by (CW6-1) (Si 1×1×0.4 cm (2012.12430, two TES arrays); 1-cm CDMS-like Ge cylinder; P2)
- **Physics.** Whether NR and ER can be told apart from phonon arrival patterns depends on how each population's spectrum is collected by each sensor.
- **Quantity and units.** 𝒦_s on f ∈ [0.1, 15] THz (40 log) × 8³ octant points; ζ_O, ζ_gap, σ_pos (dimensionless), r_coll.
- **Method and approximation level.** ballistic + anisotropic kinematics, ICA isotope and L-only f⁵ decay, lumped Kaplan film; monochromatic sources per f-bin (10⁴ phonons per cell); NTL at V_b = 2/4/10 V. Code: CMPMC main ≥ 3d43a02: transport (Octahedral kinematics, P1/P2 decay, P8 surfaces with campaign p_spec/p_diff/p_anh, KaplanFilm subgap_absorption = 0), transport_charges (P5, P6).
- **Convergence and acceptance.** ζ_O changes < 0.01 under f-grid refinement; statistics < 1%; surface coefficients over [AMM, DMM] (θ_ζ); Ge 𝒜_anh over its ×10 range; mean-field limit reproduces CW6-K7.
- **Pitfalls.** mean-field σ_pos = 0 is not a prediction; result depends on p_spec; legacy 921db93 NTL spectra 5–45% too hard; phonons trapped below 2Δ_Al are lost energy; DO NOT USE jump-to-ballistic, NEE, SoA/GPU, fast-chord.
- **Result goes to.** Ch 20; WP8-R route (d) verdict; LIMITS L39–L42; WP6 θ_ζ, θ_pos rows (LE-125).
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW6.md §2 + /home/user/dmdd-solid/returns/R16/CW6-errata.md A15 · inputs: to write (geometry from 2012.12430 App. A; isotropic AMM table of WP8-R-v2 §3.2 until item 2) · depends: INF-10 (DESIGN_NOTES items 1, 2 for full validity); DC-83 (gate).

#### DC-79. Gap-energy release site–spectrum: exciton diffusion π_ℓ(z,t) with surface loss S_surf, per-channel spectra s_ℓ(f), then ζ_gap and its timing distribution (Si, Ge; P3)
- **Physics.** Where and as what spectrum the gap energy is released decides whether it can be distinguished from primary phonons.
- **Quantity and units.** π̄_ℓ, ζ_gap (dimensionless), release-time distribution.
- **Method and approximation level.** drift–diffusion of neutral excitons; hard line at ω_op for recombination; Kaplan cascade for QP injection. Code: 1-D implicit finite-difference exciton diffusion + CMPMC transport with time-tagged sources.
- **Convergence and acceptance.** r_g to 10⁻³ under grid/time step; S_surf scan 10–10⁴ cm/s.
- **Pitfalls.** D_X and k_XB depend on the impurity census; droplets outside (CW5-4); luminescence is E_esc.
- **Result goes to.** Ch 20; WP8-R G-R2; WP6 θ_ζg, θ_Ssurf.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW6.md §3 + CW6-errata (§3 replacement row) · inputs: to write · depends: DC-68 (rates), DC-78 (kernels), INF-11.

#### DC-80. Created-phonon spectra (WP5-AUD B-1) propagated to the sensors: ΔO_obs(t) and arrival spectra for ER and NR at E_R ∈ {50, 100, 300, 1000} eV; Δ_soft in (CW6-2) (Si (then Ge); P2)
- **Physics.** Only the soft part of the birth spectrum survives to the sensors; its NR/ER difference is the phonon NR/ER signal.
- **Quantity and units.** ΔO_obs (dimensionless), Δ_soft.
- **Method and approximation level.** linear transport; birth spectra branch-resolved on 0.5 meV, ZPE subtracted. Code: convolution with DC-78 kernels; direct check with CMPMC transport after DESIGN_NOTES §7.
- **Convergence and acceptance.** B-1 grid 0.5 → 0.25 meV; f_m moved ×2 changes the bound by ≤ τ_h.
- **Pitfalls.** absorbed thermal phonons are negative sources (never clip); thermostat share with its own spectrum.
- **Result goes to.** Ch 20; WP8-R G-R3; SOTA statement LE-126.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW6.md §4 · inputs: B-1 tables from DC-61; kernels from DC-78 · depends: DC-61, DC-78; INF-10 (item 7) for the direct check.

#### DC-81. Collection efficiencies ϵ_prim^NR, ϵ_prim^ER, ϵ_NTL, ϵ_gap and hence δ_coll (CW6-3), r_coll for the 1803.02903 Si ZIP and the 1805.09942 Ge iZIP (Si, Ge; P2)
- **Physics.** NR and ER deposit energy in different populations that sensors collect with different efficiencies.
- **Quantity and units.** δ_coll, r_coll (dimensionless), ρ_g to ±0.02.
- **Method and approximation level.** LE-118 + HV drift, Luke emission, Linear/Quadratic IV in their fitted ranges, constant-λ trapping. Code: CMPMC transport_charges (P5, P6), transport, KaplanFilm, ElectrodeFilm/BulkDebye release with explicit μ_F; Geant4 source maps (external).
- **Convergence and acceptance.** 10⁵ events per population; two-bias Jacobian check (CW6 K8c–d).
- **Pitfalls.** IV Matrix and fast-chord DO NOT USE; legacy E_g/2 hit sets ρ_g by construction; iZIP surface source puts δ_coll^esc first.
- **Result goes to.** Ch 19/20; LIMITS L38; WP5 (W11′) κ_cal.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW6.md §5 + CW6-errata A6–A7 · inputs: to write (QET coverage from the CDMS II design; source maps) · depends: INF-10 (item 2); item 3 done in CMPMC-DEV c43569b; DC-78.

#### DC-82. Anisotropic welded AMM t_ν(θ,φ) for Al(111)/Si(001) and W/Si with thin-film interference; τ_l(ω) for d = 40–600 nm (film elastic constants from DFT or [FT]) (Al/Si, W/Si; P3)
- **Physics.** Phonon escape from a superconducting film back into the substrate controls pair-breaking efficiency.
- **Quantity and units.** t_ν(θ,φ), t̄_esc, τ_l (ns).
- **Method and approximation level.** 6×6 Christoffel boundary problem; transfer matrix for λ ≳ d. Code: CMPMC interface_transmission (anisotropic upgrade) + KaplanFilm (CW6-4); QE vc-relax strain–stress for Al.
- **Convergence and acceptance.** Σ = 1 to 10⁻¹⁴; isotropic limit = amm_psv; reciprocity identity (K5d); t̄ to 10⁻³ under the angular grid.
- **Pitfalls.** oxide/aSi interlayers dominate real interfaces; measured 0.3–0.55 is model-conditional.
- **Result goes to.** Ch 15/20; LIMITS L40, L41.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW6.md §7; /home/user/cmpmc/DESIGN_NOTES.md §2 · inputs: Al, Ir C_ij [FT] in /home/user/dmdd-solid/state/DATA-ADDENDA.csv; QE inputs: to write · depends: INF-10 (item 2).

#### DC-83. Kaplan-buffer recheck of R15-era CMPMC numbers at CMPMC main ≥ 3d43a02 (fix f61d710): CMPMC-AUD T8 η_pb (no loss 4.5Δ, 6Δ, 10–100Δ; 600 nm film 3, 5, 10, 40Δ; surrogate cavity), T11 benchmark energy closure, IF-AUD-5 NTL ⟨E_Luke⟩ (Al film on Ge/Si (CMPMC presets); P1)
- **Physics.** The R15 audit values were produced before the buffer fix; any cascade with film phonons above ≈ 130Δ (Ge prompt phonons 35.7 meV ≈ 206Δ_Al) lost up to 7% of its energy unseen.
- **Quantity and units.** η_pb(Ω/Δ) at the listed points; energy closure per event; ⟨E_Luke⟩ (meV).
- **Method and approximation level.** rerun the R15 test drivers and the benchmark at 3d43a02; diff against out/sota. Code: CMPMC ctest (test_kaplan, test_pair_breaking, test_luke_ntl) + examples/phonon_benchmark.
- **Convergence and acceptance.** closure ≤ 3×10⁻¹⁵ per event at 50–350Δ (test_pair_breaking (f)); values within statistical error of R15 for Ω ≲ 100Δ, else replaced; the benchmark's 9.70/14.29 eV SoA deposit is the known SoA defect, not this bug.
- **Pitfalls.** compare like for like (same seeds, same loss model); report any η_pb change > 0.005 to WP8-R L41. Scope boundary: the CMPMC-DEV tests were already rerun at 3d43a02 (ctest 16/16); this item covers only the R15 CMPMC-AUD outputs (code/CMPMC-AUD/out/sota/) and the WP8-R-v2 §3.3 / L41 / AUD-L4 numbers quoted from them.
- **Result goes to.** WP8-R L41, AUD-L4 status; SOTA cross-cutting block; code/ENV.md gate line.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CMPMC-DEV.md §3 (f61d710), IF-DEV-5; /home/user/dmdd-solid/returns/R15/CMPMC-AUD.md §1.4, §2 T8/T11, IF-AUD-2, IF-AUD-5 · inputs: ready: /home/user/dmdd-solid/code/CMPMC-AUD/tests/, /home/user/dmdd-solid/code/CMPMC-AUD/out/sota/ (R15 reference output to diff), /home/user/cmpmc/tests/ · depends: none.

### G. Coherent fields, fermionic absorption, two insertions

#### DC-84. Coherent-field regime inputs: GIPAW shielding/EFG, E*_I; elastic and piezoelectric tensors (DFPT) for BAR modes; dln a/dln α and dln a/dln m_e from scaled-constant DFT; multiferroic LSWT/TDDFT+SOC (T ≪ T_CM) (NMR (CASPEr) targets, BAR quartz/sapphire, multiferroics; P3)
- **Physics.** Ultralight DM acts as a coherent classical field driving spins, strains or constants.
- **Quantity and units.** per-target response coefficients (shielding ppm, d_ij pC/N, dln a/dln α).
- **Method and approximation level.** Kubo linear response; windowed form below the coherence time. Code: QE GIPAW, ph.x elastic/piezo, scaled-constant DFT; new LSWT/TDDFT+SOC module.
- **Convergence and acceptance.** TS_A to 1% under halving δω; FEM ω_n to 0.1%.
- **Pitfalls.** regime test first: t_int vs min(t_coh, 1/Γ_T); near T_CM no URF route (gap).
- **Result goes to.** Ch 16/21; LIMITS L-D rows.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R12/WP7-D-v2.md §1.10 · inputs: to write · depends: none (multiferroic LSWT/TDDFT+SOC module is new code).

#### DC-85. Fermionic absorption χ + target → ν̃ + excitation: all-electron S_nn, S_{J_TJ_T} along ω = m_χ − q for m_χ ∈ [E_g, 1 MeV] (spin-orbital convention fixed in the table header) (Si, Ge (crystals); atoms by DHF; P3)
- **Physics.** Fermionic DM can be absorbed by converting into a neutrino-like state, depositing m_χ at fixed q.
- **Quantity and units.** dℛ/dω per operator (V, S, A).
- **Method and approximation level.** first Born, relativistic norm. Code: DHF orbitals (q ≳ m_e/3) + high-q all-electron PAW (crystals); WP2 L6 S^GS for nuclei.
- **Convergence and acceptance.** width to 1% in ⟨p²_κ⟩; electron spectra to 2% in PAW augmentation.
- **Pitfalls.** spin-orbital convention must match §2.4(b).
- **Result goes to.** Ch 16; LIMITS L-D2.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R12/WP7-D-v2.md §2.6 · inputs: to write · depends: INF-6.

#### DC-86. Two-insertion processes: pair absorption S_OO(k ≈ 0, 2m_χ) with 𝔇^pair, dark Compton (J^(sh)(p_z), n_r), Barkas term with an HEG R^(2) + LDA map (Si, Ge, electron gas; P3)
- **Physics.** Second-order processes (two DM insertions) open channels forbidden at first order.
- **Quantity and units.** rates and spectra per process.
- **Method and approximation level.** as WP7-D §3. Code: new R^(2) module (HEG quadratic response + LDA) + L9b tables.
- **Convergence and acceptance.** dark Compton ω′ ∈ m_V(1 ± 0.1), 100 points, 32 angles; 3D velocity quadrature 20³.
- **Pitfalls.** 𝔇^pair velocity moments over f⊗f.
- **Result goes to.** Ch 16; LIMITS L-D rows.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R12/WP7-D-v2.md §3.7 · inputs: to write · depends: DC-14 (L9b-type tables).

### H. Uncertainty, figures of merit, backgrounds

#### DC-87. Halo-independent directional bound (G8′): stream matrix 𝔎_i(w_k) on 768 HEALPix × 100 speeds × 24 phases and the LP per m_χ (HiGHS) (Si, Ge (any q̂-resolved library); P3)
- **Physics.** A rate bound valid for every halo velocity distribution is a linear program over streams.
- **Quantity and units.** Φ_max per bin and m_χ.
- **Method and approximation level.** library at the τ* string of each target. Code: GPU sweep over the q-vector-resolved library + HiGHS LP.
- **Convergence and acceptance.** refine around the ≤ N_b optimal atoms; dual certificate Σλ_i𝔎_i ≥ φ; two grid levels.
- **Pitfalls.** support constraint lives in the galactic frame; Bonferroni per bin; (H2) test on the library.
- **Result goes to.** Ch 21; LIMITS L-H1.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW7.md §3 + CW7-errata §1.3 · inputs: q̂-resolved S(q,ω;Λ) from DC-1/DC-15 (nosym nscf on the full zone) · depends: DC-1, DC-15.

#### DC-88. Scalar-absorption kinetic row: Im R⁰_𝒯𝒯(0,ω) (direct kinetic route + PAW one-centre correction), then RPA+LFE R̃_𝒯𝒯 (Si (box), 10-atom oxides (fork); P3)
- **Physics.** Scalar DM coupled to electron kinetic energy absorbs through the 𝒯_e row, not the density.
- **Quantity and units.** Im R⁰_𝒯𝒯(0,ω) (eV⁻¹ per cell).
- **Method and approximation level.** IP then RPA+LFE; in-gap needs the n_g = 2 row (WP3). Code: rtsc/bench scf → dense nscf (≥ 24³) → matrix elements.
- **Convergence and acceptance.** (CW7-155) valence-restricted sum rule (not the f-sum); ecut ≥ 80 Ry (SG15 Si).
- **Pitfalls.** NC pseudo-wavefunctions miss core oscillations (PAW/AE check); 𝒯 is canonical, not m²v·v.
- **Result goes to.** Ch 16/17; WP8-F scalar row.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW7.md §6 · inputs: to write · depends: none.

#### DC-89. Cosmogenic sea-level production rates per nuclide (ACTIVIA; Geant4 Shielding or TALYS for ³H, ⁷Be) and sub-keV rate density with EC line fractions (34 survivors without measured rates (all but Si, Ge, NaI, Te); P2)
- **Physics.** Activation during surface exposure produces long-lived nuclides whose decays populate the sub-keV region.
- **Quantity and units.** R per nuclide (atoms kg⁻¹ d⁻¹); 𝓇^cos_<1 (kg⁻¹ d⁻¹ keV⁻¹).
- **Method and approximation level.** semi-empirical cross sections × sea-level n, p spectra; exposure history. Code: ACTIVIA + Geant4 10⁸ primaries.
- **Convergence and acceptance.** reproduce Si (2007.10584) and Ge (1607.04560) measured rates within errors before use.
- **Pitfalls.** ³H/⁷Be from ACTIVIA off by factors; ³H out-diffusion in Si; K:L:M EC fractions needed.
- **Result goes to.** Ch 17 background-limited ranking; WP8-U cosmo cells.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/CW7.md §11 · inputs: compositions and isotopic abundances: /home/user/dmdd-solid/returns/R16/WP8-U-table-v4.csv; code: to set up · depends: none.

#### DC-90. Spin-dependent nucleon FOM class (G-F6): per-isotope ⟨S_p⟩, ⟨S_n⟩ from ≥ 2 shell-model interactions and the incoherent SD one-phonon response from DFPT partial DOS D_κ(ω) (odd-A isotopes of the survivors; P3)
- **Physics.** For unpolarised nuclear spins only the incoherent single-phonon response survives.
- **Quantity and units.** S^SD/ρ_T per isotope.
- **Method and approximation level.** incoherent, e^{−2W_κ}, T = 0. Code: shell-model codes (external) + qe-rtsc scf → ph.x → matdyn projected DOS.
- **Convergence and acceptance.** q-grid until ⟨ω⁻¹⟩_{D_κ} changes < 1%; DOS bin ≤ ω_th/4.
- **Pitfalls.** never reuse the coherent WP2 (2.2) with spin weights (zero); even-even isotopes contribute zero.
- **Result goes to.** Ch 17; WP8-F G-F6.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R16/WP8-F-v3.md §7 (G-F6) · inputs: isotope list: v4 `isotopes[El]` rows of /home/user/dmdd-solid/returns/R16/WP8-U-table-v4.csv · depends: DC-91, DC-95 (DOS).

### I. Owed material data (WP8-U v4 GAP cells)

#### DC-91. Small-cell survivor Γ-DFPT batch: relax, ε_∞, ε₀ (dynmat.x), Z*, ω_TO, ω_LO, then ph 4³ → 6³ for slopes, sound speeds, ω_max, phonon DOS (C, 3C-SiC, GaAs, LiF, NaF, 4H-SiC, Al₂O₃; P2)
- **Physics.** Dielectric and phonon properties set the polar (POL), Migdal and NR channels of these survivors.
- **Quantity and units.** ε_∞, ε₀, Z* tensors (e), ω_TO/ω_LO (meV), c_ν(q̂) (km/s), ω_max (meV), D_κ(ω).
- **Method and approximation level.** PBE, SG15 ONCV; relax → phG → ph 4³ → 6³. Code: pw.x → ph.x (epsil) → dynmat.x, q2r.x, matdyn.x (rtsc/bench layout).
- **Convergence and acceptance.** controls vs [FT] rows: GaAs ε_∞ 10.9, Z̄* 2.27; LiF 2.02/1.05; NaF 1.78/0.98; 3C-SiC ε_∞ 6.5, ε₀ 9.7, ω_T/ω_L 98.7/120.5 meV; diamond ω_L 163 meV; WP8-U vetting rule V2 (max IR mode ≥ 20 cm⁻¹).
- **Pitfalls.** PBE GaAs at a_PBE nearly metallic (a_exp, check Γ gap first); GaAs needs 140 Ry; PBE ε_∞ systematically high (Si +11%): keep measured ε for ranking (COMP-PH IF-4).
- **Result goes to.** WP8-U table cells; Ch 11/17; COMP-PH properties.csv.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.1 · inputs: /home/user/dmdd-solid/code/COMP-PH/formulated/{C,SiC-3C,GaAs,LiF,NaF,SiC-4H,Al2O3}/{relax,scf,phG,ph,q2r,matdyn}.in (cutoffs: C 100, 3C 90, GaAs 140, LiF 90, NaF 90, 4H 90, Al₂O₃ 100 Ry) · depends: none.

#### DC-92. CaWO₄ and Li₂MoO₄ dielectric and lattice data: ε₀, ε_∞, Z* tensors, ω_TO/ω_LO mode sums (ω_T,min), elastic tensors, sound speeds, θ_D, ω_max, n_e/ω_p (CaWO₄, Li₂MoO₄; P2)
- **Physics.** Both are CUPID/CRESST-class scintillating bolometers; without these numbers their polar and NR rows cannot be ranked.
- **Quantity and units.** as DC-91.
- **Method and approximation level.** as DC-91; measured values preferred where a full text exists (CaWO₄ C_ij secondary quote: primary to be read). Code: QE pw.x/ph.x (W semicore; SOC check for W), dynmat.x, strain–stress.
- **Convergence and acceptance.** CaWO₄ measured C_ij (WP8-errata §3); IR/Raman frequencies where found; LST consistency ε₀ω_T² = ε_∞ω_L² per axis.
- **Pitfalls.** non-cubic: per-axis ε pair (WP8-F-v3 §8 bracket validity); JARVIS shear-order swap (use Voigt order, V5′).
- **Result goes to.** WP8-U table; Ch 17 POL/NR rows.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.1 recipe applied to these cells; /home/user/dmdd-solid/returns/R16/WP8-S-v2.md §6 item 4 · inputs: to write (scale from /home/user/dmdd-solid/code/COMP-PH/formulated/Al2O3/) · depends: none.

#### DC-93. CsI elastic constants C₁₁, C₁₂, C₄₄ (finite strain or DFPT) to replace the [E] B-floor model (CsI; P2)
- **Physics.** The NR edge of a heavy target is set by its sound speeds, which need the full elastic tensor.
- **Quantity and units.** C_ij (GPa); c_LA(q̂), c_max (km/s).
- **Method and approximation level.** PBE and PBEsol (spread); vdW-free ionic solid. Code: QE vc-relax + strain–stress (2-atom CsCl cell).
- **Convergence and acceptance.** B vs measured 13.5 GPa [FT, secondary]; c_LA(q̂) ≥ √(B/ρ_T) floor; measured C_ij [FT] if found supersedes.
- **Pitfalls.** PBE overestimates the lattice constant of soft halides (report a_exp-strained values).
- **Result goes to.** Ch 17 NR-heavy ranking; WP8-S tier 1; WP8-U CsI rows.
- **Spec / inputs / depends.** /home/user/dmdd-solid/returns/R17/WP8-errata.md §4, §3 item 2; method as /home/user/dmdd-solid/returns/R16/CW6.md §7 (strain–stress) · inputs: to write · depends: none.

#### DC-94. Magnetic survivors' dielectric and lattice data by DFT+U DFPT: ε₀, ε_∞, Z*, ω_TO/ω_LO, elastic tensors (positive-definite), θ_D, ω_max (YIG, NiO, MnO, Cr₂O₃, NiPS₃; P3)
- **Physics.** Magnon targets also need their lattice and dielectric properties for the polar and NR channels and for screening.
- **Quantity and units.** as DC-91.
- **Method and approximation level.** DFT+U DFPT (QE supports ph.x with Hubbard U). Code: QE DFT+U (hp.x) ph.x; magnetic cells.
- **Convergence and acceptance.** measured T_N, magnetic moments, IR modes where available; elastic tensor positive definite.
- **Pitfalls.** U-dependence of ε and Z*; AFM cell doubling for NiO/MnO.
- **Result goes to.** WP8-U magnet rows; Ch 14/17.
- **Spec / inputs / depends.** no dedicated spec; recipe of /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.1 with DFT+U; WP8-U-v3 §4 GAP rows · inputs: to write (YIG a from /home/user/dmdd-solid/state/DATA-ADDENDA.csv) · depends: DC-44 (U and magnetic ground state).

#### DC-95. Remaining survivors' DFPT batch for DFT-fillable GAP cells: Z* tensors, ε₀ (vetted), ω_T/ω_L, phonon DOS, directional sound speeds, ω_max (NaI, NaCl, CsI (dielectric), MgO, MgF₂, CaF₂, ZnO, ZnS, GaN, AlN, GaSb, SiO₂-q, TeO₂, LiAlO₂, SrTiO₃, PbTe, PbS, PbSe, Bi₂Se₃, ZrTe₅, SiC-6H, cBN, hBN; P3)
- **Physics.** As DC-91 for the rest of the 42-pool.
- **Quantity and units.** as DC-91.
- **Method and approximation level.** as DC-91; soft-mode crystals (SrTiO₃, PbX) flagged: DFPT ε₀ unusable (CW7 LE-176), measured low-T ε₀ preferred. Code: QE pw/ph/dynmat/matdyn (rtsc/bench layout).
- **Convergence and acceptance.** vetting V2 (IR mode ≥ 20 cm⁻¹); LST per axis; [FT] values supersede.
- **Pitfalls.** soft TO modes; JARVIS shear-order swap; SOC for Pb, Bi, Te.
- **Result goes to.** WP8-U table; Ch 17.
- **Spec / inputs / depends.** recipe of /home/user/dmdd-solid/returns/R15/COMP-PH.md §6.1; vetting rule WP8-U-v3 V2/V5′ · inputs: to write · depends: none.

#### DC-96. Phonon lifetimes (three-phonon linewidths) for the survivors (35 survivors (GAP:ph_lifetime); P3)
- **Physics.** Anharmonic decay sets how fast phonon NR/ER information is lost.
- **Quantity and units.** Γ_ν(q) (THz), 𝒜_anh (s⁴).
- **Method and approximation level.** FGR three-phonon, on-shell. Code: phono3py fc3 on QE supercells (or MLIP fc3).
- **Convergence and acceptance.** supercell and cutoff convergence; Si 𝒜_anh vs Tamura/2408.04732 values.
- **Pitfalls.** Ge 𝒜_anh spread ×10 in the literature.
- **Result goes to.** WP8-U ph_lifetime; CMPMC presets; Ch 20.
- **Spec / inputs / depends.** no dedicated spec; method of /home/user/dmdd-solid/returns/R16/CW2.md §12 (fc3) and /home/user/dmdd-solid/returns/R12/WP7-B2-v2.md §1 (3×3×3 fc3, 10³–10⁴ CPU·h) · inputs: to write · depends: INF-12, DC-91/94/97.

#### DC-97. Per-survivor PAER/ZPL window inputs: E_min(q), band masses m_eff, ω_TA(Q*) and EPW-class g at Q* (GW/HSE where PBE fails) (36 survivors (GAP:E_min_q, GAP:EPW_g_omegaTA_Qstar, GAP:m_eff); P3)
- **Physics.** Each indirect-gap survivor may have its own PAER-only mass window.
- **Quantity and units.** E_min(q) (eV), m_χ^PA, m_χ^ZP (MeV), m_eff (m_e).
- **Method and approximation level.** PBE + scissor; Wannier interpolation; window theorem (M.9). Code: COMP-PAER window pipeline (window.py, paedge.py) + COMP-PH emin.py; HSE/G₀W₀ where the PBE band order fails.
- **Convergence and acceptance.** C5 kinematics; band order vs experiment (Ge lesson).
- **Pitfalls.** PBE fails band order in narrow-gap and d-electron cells.
- **Result goes to.** WP8-U cells; Ch 17 window FOM.
- **Spec / inputs / depends.** method of /home/user/dmdd-solid/returns/R15/COMP-PAER.md §1, §4 and /home/user/dmdd-solid/returns/R15/COMP-PH.md §4 · inputs: to write per material; scripts in /home/user/dmdd-solid/code/COMP-PAER/scripts and /home/user/dmdd-solid/code/COMP-PH · depends: DC-91/94/96/97 (phonons); DC-2 route for PBE-failing cells.

#### DC-98. Integrated thermal contraction ∫Δα_th dT (300 K → mK) by quasi-harmonic DFPT (38 survivors (GAP:alpha_th_integral); P3)
- **Physics.** Differential contraction between crystal and holder stores elastic energy that can later relax.
- **Quantity and units.** ∫α dT (dimensionless strain).
- **Method and approximation level.** quasi-harmonic, PBE/PBEsol spread. Code: QHA: DFPT at ≈ 5 volumes per material (phonopy-qha).
- **Convergence and acceptance.** measured α(T) where available (Si, Ge, Al₂O₃).
- **Pitfalls.** QHA fails near soft modes and for negative-expansion Si below 120 K (check sign).
- **Result goes to.** WP8-U cells; DC-74 FEM inputs.
- **Spec / inputs / depends.** no dedicated spec; WP8-U-v3 §1.3 property list · inputs: to write · depends: DC-91/94/96/97.

## 3. Missing infrastructure and the dependency graph

| INF | what is missing | state / how to close | source | blocks |
|---|---|---|---|---|
| INF-1 | GW and finite-q RPA+LFE response engine: G₀W₀ quasiparticles, full-frequency ε⁻¹_GG′(p,ω) to ≈ 100 eV, finite-Q BSE | Missing in the campaign fork (https://github.com/ytcs/qe-rtsc/issues/1, OPEN since 2026-11-01). Options in the issue: (a) BerkeleyGW interface (pw2bgw, GPU builds, wired into rtsc/bench); (b) native QE route (turbo_eels, or rtsc/sth extended to finite ω and G ≠ G′); (c) BSE via BerkeleyGW or Yambo. Record the licence (BerkeleyGW BSD, Yambo GPL) in the rtsc README before adoption. Benchmark gate from the issue: Si ε_eh = 3.75 eV, F_eh = 0.119. | issue #1; GAP-EF-v2 §5; WP5-v4 §2; code/ENV.md 'GW gap in qe-rtsc' | DC-1, DC-9, DC-10, DC-11, DC-12, DC-13, DC-14, DC-15, DC-17, DC-25, DC-26, DC-27, DC-28, DC-42, DC-46, DC-48, DC-52, DC-63, DC-64, DC-65, DC-68, DC-73 |
| INF-2 | PAER density vertex in the Wannier gauge (tier-H stage 5 'rho'): ρ_mn(k,q) on the coarse 12³ k grid per target q, rotated with the same U(k) to F^W(R,q) (M.18) | Code does not exist (COMP-PAER IF-CP-6: 'the critical path'). Needs one nscf at k+q per q, unfolding, EPW's U(k) matrices (write_u_matrices). Acceptance: Wannier vs direct ρ ≤ 2% at 5 off-grid k; ρ_nn(k,0) = 1 (with PAW augmentation if PAW is used). Alternative for q ≲ 0.5 αm_e: Wannier position-operator expansion. | COMP-PAER §8 stage 5; WP3-v3 §M10 (M.18) | DC-1, DC-3, DC-8 |
| INF-3 | PAER kernel (tier-H stage 6 'paer'): (M.1) with four paths and unrestricted m in the Wannier manifold, plane-wave Sternheimer remainder (rtsc/sth: (H − ε)\|∂ψ⟩ = −P^⊥∂V\|ψ⟩ contracted with e^{iq·r}), ε̃⁻¹_G0 with LFE, pair term W^scr(P,ω_f)𝔗, pocket sums with tetrahedra | Code does not exist. Also supplies M^(2) for the Fano coefficient c^F (DC-38 Γ/δ map) and the C-code side of O4. Acceptance: CONTROLS C1, C2, C4, C6, C7a–e, symmetry zeros (DC-1 section). | COMP-PAER §8 stage 6; WP3-v3 §M10; CW3 §2.3 | DC-1, DC-3, DC-8, DC-38 |
| INF-4 | Dynamical quadrupoles Q_κ,αβγ for the long-range e–ph vertex (also in non-polar Si) | QE has no long-wave DFPT; use ABINIT lw_qdrpl (or literature values) and write quadrupole.fmt for EPW. Acceptance: g(Q*) vs direct ph.x ≤ 5% at 3 off-grid Q. | COMP-PAER §8 stage 2; WP3-v3 §M10; WP5-v4 §2 (quadrupole corrections) | DC-1, DC-3, DC-8, DC-63 |
| INF-5 | Frequency-dependent mixed E(ω)–u DFPT (shifted Sternheimer at ±ω and imaginary ω) | ≈ 50-line patch of ph.x zstar_eu generalised to complex frequency; batched shifted solves are the use case of the fork's rtsc/sth. Acceptance: Z*(0), ε_∞ equal to static DFPT to 1%; acoustic sum rule at ω → 0. | CW2 §0b stack C; CW2 §8, §15 | DC-24, DC-35 |
| INF-6 | All-electron density stack: PAW AE reconstruction with one-centre (augmentation-sphere) radial transforms above ≈ 10 keV, or LAPW (Elk/WIEN2k); finite-nucleus Dirac atoms (GRASP2018/DIRAC or patched ld1.x) | Existing codes, not set up in the box; pslibrary PAW sets (not SG15) needed. Pitfall: gridded pp.x plot_num=21 aliases the core region. | CW2 §0b stack B; CW2-errata E-5, E-7 | DC-13, DC-22, DC-23, DC-25, DC-39, DC-85 |
| INF-7 | Machine-learned interatomic potentials for Si and Ge (ZBL-spliced below 1 Å; dimers to 0.5 Å, point defects, close pairs, amorphous, liquid, recoil snapshots) and for the oxides/LiH of DC-30 | Training ≈ 10⁴ DFT configurations (PBE and SCAN for spread); force error ≤ 50 meV/Å, energy ≤ 3 meV/atom; one MLIP, cell, boundary condition and E^conf reference for E_st, p_st, NEB end states and 𝒦^rel (WP5-AUD §3.1). Training cost is not estimated in the sources ([E-DC] 10⁴–10⁵ core-h DFT). | WP5-v4 §3.4 PES; WP5-AUD §3.1 | DC-29, DC-30, DC-37, DC-56, DC-57, DC-61, DC-70, DC-72, DC-73, DC-77 |
| INF-8 | Real-time TDDFT with Ehrenfest nuclei (and surface hopping) for close collisions | QE has no production real-time code: Qb@ll, Octopus or SALMON, with ZBL-hard semicore pseudopotentials for E_coll ≥ 1 keV. | CW5 §2.4; WP5-v4 §3.4 | DC-60 |
| INF-9 | Small response-library modules (new code): WP2 (3.5) multiphonon module (≈ 300 lines); coherent n_ph = 2 sum; IP vertex module with the current vertex and non-local commutator (EXCEED-DM type); tls_response; lowd-rpa; frenkel-ff; disorder/isotope module (≈ 250 lines); DM-side I5 module | Each is days of work; specified in the cited sections. | CW2 §1, §10; WP1-v3 §8 G10; WP7-T-v2 §2.7; WP7-B1-v2 §2–§6, §12; WP7-B2-v2 §2 | DC-14, DC-20, DC-21, DC-32, DC-46, DC-52, DC-53, DC-59 |
| INF-10 | CMPMC items not yet implemented (/home/user/cmpmc/DESIGN_NOTES.md): §1 Chang–Scalapino η_pb(Ω, τ_l/τ₀^φ, T) table (3 d); §2 anisotropic AMM + film interference (1–2 wk); §5 trap kinetics (E9)–(E12) with space charge (≈ 1 wk); §6 IV Matrix per-type Z_f (needs an [FT] Z_f source; 1 d after); §7 created-phonon spectrum spawn (M); §8 dispersive phonons and T-mode decay (L); §9 Rothwarf–Taylor bulk QP (M); §10 non-parabolic HV (S, needs α source); §11 sparse Voigt contraction for Exact kinematics (S); §12 SoA/GPU parity (M); §13 jump-to-ballistic Green's function (M); §14 k-space NEE (M); plus sourced AluminumFilm() constants (CMPMC-DEV §6 item 6) | Unvalidated modules (IV Matrix, bulk 3D-QP, jump-to-ballistic, NEE, SoA/GPU) throw unless allow_unvalidated; none may feed [CALC] (code/ENV.md gate: main ≥ 3d43a02, modules PASS in CMPMC-AUD §4). Item 3 (gap-energy phonons at electrodes) is DONE (c43569b). | CMPMC-DEV §1, §6; CMPMC-AUD §6; DESIGN_NOTES.md | DC-69, DC-74, DC-76, DC-78, DC-80, DC-81, DC-82 |
| INF-11 | Exciton / electron–hole-droplet kinetics module and history-dependent drift–trap transport (G4CMP/CMPMC do not model excitons) | Rate equations for n_eh, n_X, n_BX per impurity species and droplets; field dependence; luminescence branching; coupled to INF-10 §5. | WP7-E-v3 §7; CW6 §3 | DC-69, DC-79 |
| INF-12 | phono3py / hiPhive / TDEP installation (absent in the box: CW2 §12) | Pure installation; fc3 supercell runs then go through the fork. | CW2 §12 | DC-31, DC-34, DC-37, DC-96 |
| INF-13 | Glass models: melt-quench MLIPs for a-SiO₂, AlOx, a-WSi (and SiN_x, a-Si) and the landscape-filtering / swap-MC TLS sampler | 648–5184-atom cells, ≥ 5 quenches (≳ 10⁴ for TLS statistics). | CW2 §0b stack E; WP7-B2-v2 §2.5; WP7-T-v2 §2.7; CW4 §2 | DC-32, DC-42, DC-59 |
| INF-14 | Full-band cascade solver: deterministic upward sweep (EF3)–(EF4) on tabulated full-band iso-energy kernels + k-resolved first generation (law of total variance); extension of code/GAP-EF-v2 | New code; convergence criteria (c1)–(c5) of GAP-EF-v2-errata R-13; ω₀-commensurate grid (IF-EW-1). | GAP-EF-v2 §5 + errata R-13; WP5-v4 §2 'Cascade solve' | DC-63, DC-64 |

Item-to-item dependencies (A → B: B needs A's output):
```
DC-1   → DC-3, DC-6, DC-8, DC-87
DC-2   → DC-3, DC-16, DC-97
DC-4   → DC-2
DC-5   → DC-6
DC-9   → DC-10
DC-14  → DC-86
DC-15  → DC-87
DC-17  → DC-1
DC-19  → DC-20, DC-21, DC-22, DC-24, DC-31, DC-33, DC-34, DC-35, DC-40
DC-20  → DC-21
DC-21  → DC-25, DC-35
DC-25  → DC-11, DC-26
DC-28  → DC-40
DC-29  → DC-31
DC-44  → DC-43, DC-94
DC-56  → DC-55, DC-74
DC-59  → DC-58
DC-60  → DC-62
DC-61  → DC-56, DC-62, DC-69, DC-72, DC-80
DC-63  → DC-62, DC-64, DC-65, DC-66, DC-70
DC-68  → DC-64, DC-69, DC-71, DC-79
DC-69  → DC-75
DC-72  → DC-70, DC-71
DC-78  → DC-79, DC-80, DC-81
DC-81  → DC-69
DC-83  → DC-78
DC-91  → DC-8, DC-28, DC-90, DC-96, DC-97, DC-98
DC-95  → DC-90
```
Critical path for the P1 items:
```
INF-4 (quadrupoles) ─┐
INF-2 (Wannier ρ) ───┼─→ DC-1 Si tier H ─→ DC-6 ϖ_II ratio ─→ Ch 13 T5/T6
INF-3 (PAER kernel) ─┘        └─→ DC-8 GaAs C8 decoy, DC-3 Ge tier H, DC-38 Γ/δ map (c^F)
DC-4 Ge 6³ DFPT ─→ DC-2 Ge window (HSE06+SOC) ─→ DC-3 Ge tier H
DC-83 Kaplan-buffer recheck ─→ every CMPMC [CALC] (DC-78, DC-80, DC-81 …)
DC-5 Si Umklapp vertex: no blocker (box)
```

## 4. Recommended execution order
- **Phase 0: the box, now (hours in total; no new code):** DC-83, DC-4, DC-5, DC-67, DC-41, DC-49, DC-39, DC-36, DC-54, DC-16, DC-7, DC-18, DC-82, DC-93, DC-89. plus the 0.44-h first pass of DC-78 and X2-N1 of DC-17. DC-83 and DC-4 first: they gate P1 numbers already quoted.
- **Phase 1: P1 on the GPU pod (critical path):** DC-2, DC-1, DC-6, DC-8, DC-3. build INF-4, INF-2, INF-3 first (weeks of code); DC-2 can start as soon as DC-4 is done.
- **Phase 2: DFPT batches and lattice library (parallel with phase 1; fork or box in ≤ 3-h pieces):** DC-19, DC-91, DC-92, DC-95, DC-44, DC-94, DC-20, DC-21, DC-33, DC-22, DC-23, DC-38, DC-40, DC-97, DC-90, DC-24, DC-35, DC-34, DC-31, DC-96, DC-98. DC-24 and DC-35 after INF-5; DC-31, DC-34, DC-96 after INF-12.
- **Phase 3: GW/BSE/RPA+LFE (after INF-1 and INF-14):** DC-63, DC-65, DC-66, DC-64, DC-68, DC-28, DC-9, DC-10, DC-11, DC-25, DC-26, DC-27, DC-14, DC-15, DC-17, DC-48, DC-52, DC-13, DC-12, DC-46. run DC-63 (Si/Ge/GaAs) to its Si gate before DC-64; DC-68 before the halide part of DC-64.
- **Phase 4: MLIP / MD (after INF-7, INF-8, INF-13):** DC-61, DC-60, DC-62, DC-56, DC-55, DC-57, DC-72, DC-70, DC-71, DC-73, DC-77, DC-29, DC-30, DC-32, DC-59, DC-58, DC-42, DC-37.
- **Phase 5: CMPMC (after INF-10 §1, §2, §5 and INF-11):** DC-78, DC-81, DC-80, DC-69, DC-79, DC-76, DC-75, DC-74.
- **Phase 6: remaining P3 refinements:** DC-43, DC-45, DC-47, DC-50, DC-51, DC-53, DC-84, DC-85, DC-86, DC-87, DC-88.

## 5. Totals
- **Items:** 98 (P1 6 · P2 34 · P3 58).
- **By primary code:** QE fork 34 · other 29 · BerkeleyGW-or-fork-GW 12 · MD-MLIP 10 · CMPMC 9 · EPW 4.

| priority | core-h (lo–hi) | GPU-h (lo–hi) | items whose cost is [E-DC] |
|---|---|---|---|
| P1 | 394–707 | 3–15 | DC-5, DC-6 |
| P2 | 2.4×10⁶–4.1×10⁶ | 3.4×10⁴–3.2×10⁵ | DC-8, DC-14, DC-17, DC-28, DC-62, DC-74, DC-92, DC-93 |
| P3 | 6.1×10⁵–1.9×10⁶ | 1.2×10⁵–1.1×10⁶ | DC-7, DC-12, DC-13, DC-15, DC-16, DC-18, DC-66, DC-75, DC-87, DC-90, DC-94, DC-95, DC-96, DC-97, DC-98 |
| **all** | **3×10⁶–6×10⁶** | **1.6×10⁵–1.4×10⁶** | 25 items |

Of the total, source-quoted costs alone: 2.9×10⁶–5.3×10⁶ core-h and 1.6×10⁵–1.4×10⁶ GPU-h. Not included: infrastructure build effort (INF-1…14: weeks of code each for INF-1, 2, 3, 10, 14), MLIP training (INF-7, [E-DC] 10⁴–10⁵ core-h), and per-item human time. The dominant terms are the cascade/exciton/defect families (DC-60, 63, 64, 68, 57) and TLS sampling (DC-59).
P1 alone: 394–707 core-h + 3–15 GPU-h (DC-1, DC-2, DC-4, DC-5, DC-6, DC-83); its blockers are code, not compute: INF-2, INF-3 (do not exist), INF-4 (needs ABINIT), and DC-4 before DC-2.

## 6. Crosswalk: sources → DC items (deduplication record)
- LE-16 (COMP-PH; OPEN) → DC-4, DC-91, DC-2
- LE-17 (COMP-PAER tier H) → DC-1
- LE-24 (Si done by COMP-PAER/COMP-PH; Ge open) → DC-2, DC-97
- LE-25 → DC-5
- LE-26 → DC-6
- LE-27 (crossover done by COMP-PH; SOC/LO remainder) → DC-7
- LE-28, LE-29 → DC-9
- LE-30 → DC-10
- LE-31 → DC-11
- LE-32 → DC-12
- LE-33 → DC-13
- LE-34, LE-35, LE-38 → DC-14
- LE-36 → DC-16
- LE-39 → DC-15
- LE-40, 41, 42 (+ LE-44 ALDA size) → DC-17
- LE-46 (T-transfer; alternative via COMP-PAER ε₂^PA(T)) → DC-1
- LE-47 (CONTROLS C8) → DC-8
- LE-179 → DC-18
- LE-48, LE-49 → DC-20
- LE-51 (CEG) → DC-22
- LE-52 (CEG), LE-70 → DC-30
- LE-53, LE-64 → DC-32
- LE-54, LE-56 (CEG) → DC-23
- LE-55 → DC-24
- LE-57, LE-60 → DC-21
- LE-58 → DC-29
- LE-59 / G-F2 / G13 → DC-31
- LE-61 → DC-25
- LE-62 → DC-35
- LE-65, LE-66 (CEG) → DC-33
- LE-67 → DC-34
- LE-69 → DC-36
- LE-71 → DC-27
- LE-72 (CEG) → DC-37
- LE-76 / IF-R8-10 / WP5-v4 R7, R7′ / OW0-10 → DC-38
- LE-78 / OW0-15 → DC-39
- LE-83 / O5 → DC-40
- LE-97, LE-104, LE-157 → DC-41
- LE-98 (RG2) → DC-42
- LE-99 (CEG), LE-116, LE-156 → DC-43
- LE-100 → DC-46
- LE-101 → DC-47
- LE-102 (CEG) → DC-48
- LE-103 → DC-45
- LE-105 → DC-49
- LE-108 → DC-50
- LE-109 → DC-51
- LE-112 → DC-52
- LE-113 → DC-53
- LE-114 → DC-54
- LE-115 (CEG) → DC-26
- LE-127 → DC-55
- LE-128, LE-129 (CEG), LE-147 (CEG) → DC-56
- LE-131 (CEG), LE-145 (CEG) / G-F3 → DC-74
- LE-134 → DC-57
- LE-137 → DC-58
- LE-138 (CEG) → DC-65
- LE-139 (CEG) → DC-66
- LE-140 / WP5 R3 → DC-60
- LE-141 (CEG), LE-14 (CEG) / IF-E9 / G-E10 → DC-68
- LE-142 / WP5 R8 → DC-70
- LE-144 (CEG), LE-151 (CEG) → DC-73
- LE-146 → DC-71
- LE-148 → DC-72
- LE-149 (CEG) → DC-75
- LE-3 / G-E3 (open as a computation), LE-5 / B-1 → DC-61
- LE-6 / G-R4 / LIMITS L43 (B-2) → DC-62
- LE-13 / GAP-EF-v2 §5 / WP5-v4 §2 / qe-rtsc #1 → DC-63, DC-64
- LE-153 / OW6-3; IF-EW-1 → DC-67
- LE-118 (G-R1) → DC-78
- LE-119 (CEG) → DC-79
- LE-120 (G-R3) → DC-80
- LE-121 (G-E4) → DC-81
- LE-122 (CEG, G-E6) → DC-76
- LE-123 (RG7, L40) → DC-82
- IF-DEV-5 Kaplan buffer → DC-83
- LE-152 (G8′) → DC-87
- LE-155 (G-F1) → DC-88
- LE-177 → DC-89
- WP8-F G-F5 → DC-1, DC-2, DC-4, DC-97
- WP8-F G-F6 → DC-90
- WP8-S-v2 §6 item 1 / WP8-errata §15 → DC-28
- WP8-S-v2 §6 items 2, 4; WP8-errata §4 → DC-92, DC-93, DC-95
- WP7-T-v2 §2.7, §3.4, §4.6, §5.5 → DC-59, DC-57, DC-56, DC-61
- WP7-E-v3 §7 → DC-68, DC-69, DC-81
- WP7-B1-v2 §2–§12 → DC-52, DC-53, DC-25, DC-11, DC-50, DC-51
- WP7-B2-v2 §1–§10 → DC-34, DC-32, DC-33, DC-36, DC-30, DC-43, DC-37, DC-73, DC-77
- WP7-D-v2 §1.10, §2.6, §3.7 → DC-84, DC-85, DC-86
- COMP-PH §6.1 survivor batch → DC-91
- COMP-PH §6.2, §6.3 → DC-2, DC-4
- "CsI elastic constants" → DC-93
- "YIG and the magnets" → DC-44, DC-94, DC-43, DC-45
- "CaWO₄ and Li₂MoO₄ ε₀, ω_LO/TO, Z*" → DC-92
- WP8-U v4 GAP: Zstar_tensor, Z*, eps_0, eps_inf, omega_L/T, omega_max, c_dir, c_sound, theta_D, phonon_DOS, eps_0_DFT_vetted → DC-91, DC-92, DC-93, DC-94, DC-95
- GAP: E_min_q, EPW_g_omegaTA_Qstar, m_eff → DC-97
- GAP: E_x_b → DC-68
- GAP: eps_eh, F_eh, F_eh_v2 → DC-63, DC-64
- GAP: L_eps2_data → DC-28
- GAP: ph_lifetime → DC-96
- GAP: alpha_th_integral → DC-98
- GAP: E_st1_p_surv, y_ion_QF → DC-61, DC-62
- GAP: eps_bg → DC-48
- GAP: cosmo_production, S4_cosmo → DC-89

**Exact-gap rows whose missing step is not a computation (excluded):** LE-73, 74 (N-uniformity), 81, 82, 86, 92 (rigour/theory gaps of WP0/WP4/WP7-D); LE-117 (needs polarised-neutron data); LE-130 (film measurement). **Theory rows of CW1 (excluded):** LE-37, 43, 44 (size via DC-17), 45, 178. LE-63, 68, 85, 89, 93, 96 and the CW8 literature rows are closed literature checks.

## 7. Owed data that only a measurement or literature fetch can supply (not DC items)
- Low-T gaps E_g(T_op) of GaAs, GaSb, Ge (GAP:E_g_Top; decides Ge vs GaSb in the ER floor, WP8-S-v2 §6 item 3); measured E_g and ε_eh of TeO₂, Li₂MoO₄, γ-LiAlO₂ (item 6).
- Measured ε_eh/F of Al₂O₃, CaWO₄, LiF, NaF, diamond F, GaAs/CdTe ε_eh (GAP-EF-v2 GE-2, EF-LIT): DC-64 computes them; a measurement would validate.
- Measured C_ij for TeO₂ and CsI, the primary CaWO₄ source (WP8-errata §3); Li₂MoO₄ ρ (GAP:rho); LiF low-T ε₀ (WP8-S-v2 §6 item 4).
- tanδ₀ / P̄_STM per film (GAP:tan_delta0_PSTM, LE-130 three-measurement proposal, LE-136); ²¹⁰Pb/U/Th (process-dependent, GAP:Pb210_U_Th); ⁷⁶Ge specific activity; PbS/PbSe low-T ε₀.
- Al bulk Δ_BCS (LE-107 split); Si low-T in-band two-phonon α (LE-66, alternative to DC-33); INS PDFs Nilsson & Nelin PRB 6, 3777 and PRB 3, 364 (COMP-PH IF-7); Macfarlane Ge indirect edge (DC-3 C1); Jacoboni–Reggiani Z_f (INF-10 §6).
- Measurement proposals carried by exact gaps: η^φ_NR at two biases (LE-121), two-window Y_H (LE-141), tagged-neutron LiF F-centre counting (LE-151).


## Book-phase additions (2026-11-02, compute policy)
- Book figures currently drawn from labelled models that a first-principles replacement would improve (not required by the text):
  - Fig. 4.7 and Fig. 4.11: silicon RPA / local-field / ALDA loss and BSE absorption, currently from an empirical-pseudopotential model. Replace with QE + Yambo (BSE) at the representative PBE setting.
  - Fig. 6.6: aluminium α²F, currently a free-electron/empty-core model. Replace with EPW at a converged k/q grid, and check λ_ep ≈ 0.44 and ω_log ≈ 270 K.
  - Ge DFPT column of Table 5.1, absent because PBE is near-metallic at the measured a. Fill it with LDA or a hybrid functional at the measured a.
- Crystalline-Si Migdal drag mass δM_κ (8.6 uses the atomic estimate 14 m_e): compute it from DFT (Born-effective electronic mass per site).
- GaAs dynamical quadrupoles (piezoelectric acoustic contribution in 11.2; currently a rigid-Born-charge estimate): DFPT quadrupole calculation.
- Plasmon decay into e–h pairs plus phonons in Si (branching ratio; 10.3 estimates 10⁻³–10⁻²): second-order e–ph + RPA calculation.
- Ge 3d core-to-conduction crystal form factor (10.6; final-state treatment changes the 3d rate ~10×): all-electron/PAW crystal calculation.
- (book 11.9) GaAs core-electron kinetic-energy correction to the scalar phonon rate (~20 %, currently a parametric estimate in Table 11.1).
- (book Ch12, settles the G≠G′ open question; E.18 vs Berghaus et al.) **Off-diagonal ε⁻¹_{GG′} in the crystal Migdal rate, Si (then Ge).**
  - **Method:**
    - QE ground state, then an RPA χ⁰_{GG′}(q,ω) with local fields via Yambo, BerkeleyGW or GPAW; none is installed here, and QE 7.6 alone does not give the full matrix.
    - Use about a 12³ k-mesh, |G| cutoff of about 5 Ry, ω up to 50 eV, and q along three directions out to ~3 q_BZ.
    - Evaluate the Migdal rate of eq:12.1-joint/12.3 three ways: (i) the full matrix, including the q→q+G umklapp channels of the nuclear kick; (ii) the diagonal of ε⁻¹ only (the book's current form, Limit Check 12.3a); (iii) the plain 1/ε_{00}.
  - **Output:** the ratio (i)/(ii) as a function of m_χ and E_R, which becomes a row of tab:12-nuisances.
  - **Cost:** moderate, a few hundred core-hours; it is the largest item on this list.
  - **Cheaper bracket first:** a tight-binding or empirical-pseudopotential χ_{GG′} for Si (the 12.3 Wannier model), giving an order-of-magnitude answer in under an hour on this machine.
  - **Open data:** none tabulates off-diagonal ε⁻¹ for Migdal kinematics, so the compute policy allows this.
  - **Cheap bracket done (2026-11-03):** `book/figscripts/ch12/offdiag12.py` (+ `.log`), an empirical-pseudopotential RPA, the result block in `book/ledgers/REVIEWS/ch12/editor-notes.md`.
    - Result: (i)/(ii) = 1.38 at NK = 8, |G|² ≤ 19; extrapolated ≈ 1.2–1.3; band 1.1–1.45; flat in m_χ within 3 %; the off-diagonal elements raise the rate.
    - Validation: the model gives (iii)/(ii) = 1.19–1.27 against 1.35, i.e. 2/3 of the diagonal local-field effect.
    - Key finding: the struck-atom structure phase e^{i(G−G′)·X} is required (eq:12.3-FL is phase-free only with the origin on the atom). The G sum is not converged in the model up to |G|² = 35. The point-ion run shows that the drift is in the off-diagonal response at large G′, not in Z_ion; the lower edge of the band is an extrapolation, not a bound.
    - **The full calculation above stays open.** Converge the G sum with a realistic ion vertex (PAW or all-electron); this gives the number for tab:12-nuisances.
- (book Fig. 3.7a, user flag 2026-11-03) **Status 2026-11-03: cheap fix applied (EPM); first-principles replacement still open.** Panel (a) now uses the local Cohen–Bergstresser EPM (no SO) plus a −0.21 eV scissor (L 0.744, Γ₂′ 1.01, Δ 0.81 eV; figscripts/ch03/fig3_7.log), because the Chelikowsky–Cohen 1976 nonlocal/SO Ge parameters could not be obtained and verified (paper closed, erratum PRB 30, 4828). Swap in CC 1976 (gives Δ_SO, Γ ≈ 0.9) once the table is in hand. **Ge band structure is qualitatively wrong.** Plain PBE at the measured a closes the Ge gap and inverts the Γ ordering, so the figure misleads readers. Two fixes:
  - **Cheap, no QE:** redraw panel (a) from the nonlocal empirical pseudopotential of Chelikowsky & Cohen, PRB 14, 556 (1976), with spin–orbit, using the book's EPM code (Sect. 3.3, Figs. 4.7/4.11 model). It takes seconds and gives the correct indirect L gap and Γ ordering. Cite it, and label the panel "empirical pseudopotential" in the caption.
  - **First-principles:** reuse the HSE06+SOC Wannier bands of DC-2 once they exist.
  Until either is done, the caption should state that PBE underestimates the Ge gap and misorders Γ. (Done: the caption carries the PBE clause.) Check the caption and table text of 3.3 for consistency with Table 3.x.

## Unsized leading corrections (App. F)
Added 2026-11-03 (App. F layout pass): rows of tab:F-rows whose leading-correction column prints **unsized** because the book gives no number. Size each, then replace `\Fsize{unsized}` in tex/appF/F-rows.tex.
- **Fermionic absorption on electrons** (eq:10.9-ferm; no limit label): transverse-current row of the vector operator and the Dirac corrections, both O((Zα)²) for inner shells. Cheapest: existing script rerun (figscripts/ch10/fermi10_9.py, hydrogen-like 1s, add the Tr S_jTjT row) for the nonrelativistic part; Dirac part from a literature value (relativistic hydrogenic form factors). Prints in Sect. 10.9 (open item App. E.26).
- **In-medium decay of an excited state** (eq:10.9-vac, eq:10.9-decay; no limit label): local field at the particle (and finite-Q ε^T for the non-radiative part). Cheapest: analytic estimate (Lorentz/empty-cavity local-field factor for magnetic- and electric-dipole emission in a dielectric, evaluated with the measured ε of silicon in figscripts/ch10/decay10_9.py). Prints in Sect. 10.9 (finite-Q part App. E.16).
- **Wannier picture of the boost** (lim:12.3d): non-rigid vertex ∇V^scf + F_e P^W beyond rigid Wannier following. Cheapest: existing script rerun (figscripts/ch12/limit12_3d.py, tight-binding chain, with a self-consistent, bond-charge vertex) for a model size; the silicon number needs a new calculation (DFPT deformation potential projected on Wannier functions). Prints in Sect. 12.3 (open item App. E.18).
- **Linear mean yield** (eq:18.2-linear; no box): the o(ω) remainder (constant term b_N and the variance law) needs second-order renewal estimates for the branching cascade (open problem of Sect. 18.2). Cheapest: none analytic; numerically b_N = 0.35 (Si, one-sided seed, figscripts/ch18/num18_2.log) is known but not derived. Prints in Sect. 18.2.
| DC-book-14.3 | AFMR weight zero-point correction for |S| = 5/2 at ω_A/ω_E = 0.017 (MnF₂): beyond 8-site ED (5–23 % at |S| = 3/2 for larger ω_A/ω_E); needs larger-cluster ED/DMRG or 1/S series | Unsized leading correction | book 14.3 |
| DC-book-14.1 | Ratio W∥/W⊥ (two-magnon to one-magnon spin weight) beyond linear spin-wave in NiO: F row \Fsize{unsized}; ΔS/|S| bounds the one-magnon weight error from below only | Unsized leading correction (App. F) | book 14.1 |
| DC-book-14.1b | NiO biaxial two-constant anisotropy rate near the one-magnon edge (would replace the ×29 upper value of the one-constant gap model) | Optional refinement | book 14.1 |
| DC-book-15.4a | First-principles α²F_tr(Ω) for Al at low frequency (the free-electron model is off by ~1.25e4 from umklapp), for the phonon-assisted absorption rate within a few meV of 2Δ | Needed input | book 15.4 |
| DC-book-15.4b | Unsized F rows: Mattis–Bardeen impurity absorption; spin-current pair breaking (strong-coupling renormalization, factor ~0.52 if 1/(1+λ_tr) per current eigenvalue) | Unsized leading corrections (App. F) | book 15.4 |
| DC-book-15.2 | Strong-coupling (frequency-dependent gap) correction to the conserving edge response | Unsized | book 15.2 |
| DC-book-16.3 | 1D nanotube response beyond the linear-channel model (F row \Fsize{unsized}) | Unsized leading correction (App. F) | book 16.3 |
| DC-book-15.4c | Electron–electron (umklapp) absorption in Al near 1 meV; spin-current line shape (F₁ᵃ, triplet p-wave vertex); strong-coupling gap in scattering — all unsized | Unsized leading corrections (App. F) | book Ch15 |
| DC-book-16.4 | Molecular crystals: charge-transfer admixture and the gap to a periodic BSE calculation (F row unsized); anthracene with σ screening of 𝔍 | Unsized leading corrections (App. F) | book 16.4 |
| DC-book-16.4b | Data item: measured anthracene Davydov splitting for comparison with the model (31 meV) | Data | book 16.4 |
| DC-book-16.1 | DONE (book Ch16 post-check: the full NR row adopted as central) | — | book 16.1 |
| DC-book-16.5 | Local-field ratio 𝔣^loc_D of Si:P (E.21 specifies inputs) | Unsized | book 16.5 |
| DC-book-17.6 | Measured low-temperature elastic tensor of GaAs (data) to settle P(GaAs > Ge) in the single-phonon ranking (database tensors run ~4.8 % low) | Data item | book 17.6 |
| DC-book-12 | Coherent Migdal response for Si at 0.75 keV ≲ q ≲ 2 q_BZ with full lattice coherence and local fields (LE-188) | Unsized; affects the Migdal rate at 0.32–1 MeV | book Ch12/17 |
| DC-book-17a | Measured/DFPT elastic tensors of GaAs (P(GaAs ≻ Ge) 0.884 → 0.741) and TeO₂ (P(first) 0.968 → 0.781 at doubled width) | Data/compute | book 17.6 |
| DC-book-17b | Ge phonon DOS (multiphonon–Migdal crossover in Ge) | Data | book 17.1 |
| DC-book-17c | L(p, ω) near the gap at p of several keV for LiF, NaF, Ge (Migdal FOM; dispersion is a factor-2 nuisance); Ge core screening ε_core(0) for the pole factor | Compute | book 17.5 |
| DC-book-17d | Si one-phonon contours below 3.4 MeV carry the coherent correction of 11.3 (> 10 % below 18 keV): unsized in Fig. 17.2a | Unsized | book 17.1 |
| DC-book-19.2 | Charge yield of Si nuclear recoils below the binary threshold (0.1–3.9 keV) from a non-perturbative close-collision kernel (Born parameter ~15; Landau–Zener/TDDFT; App. E.23) vs data (F row \Fsize{unsized}) | Unsized leading correction | book 19.2 |
| DC-FBC-2 | Stage 2 of the Si full-band cascade: excitonic final states, GW-level impact-ionization rates, DFPT e–ph couplings for both carriers, photon-seed k-convergence; then Ge and GaAs with SOC. Stage 1: returns/R19/FBC-v2.md | Specified calculation | R19 |
| DC-book-19.5 | Gap-energy release law in dense NR tracks (exciton annihilation, Auger) and the two-bias inversion inputs: F rows \Fsize{unsized} | Unsized leading corrections (App. F) | book 19.5 |
| DC-book-20.1 | Luke emission into transverse phonons (leading correction to the golden-rule Luke rate) | Unsized | book 20.1 |
