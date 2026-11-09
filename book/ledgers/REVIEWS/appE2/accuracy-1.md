# App. E.14–E.20 accuracy review, part 1 (isolated)

Scope: tex/appE/E-14.tex … E-20.tex, checked against state/DEFERRED-COMPUTE.md (the DC items on each section's SPINE writer-only list), state/SOTA.md,
state/LOOSE-ENDS.md, ledgers/SEAMS/E-e.md and E-f.md (read in full; E-e says costs follow the ledger rule "h on 4 cores × 4", so items 1–2 below are slips,
not choices), and the primary specs they name (returns/R15/COMP-PAER §7–9, COMP-PH §3–6; returns/R16/CW1, CW2, CW3,
CW4, CW7 and their errata). Nothing was run except short arithmetic and a lattice-vector count. The tex was not edited.
Verdicts: CHECKED = agrees with the record and is dimensionally sound; WRONG = contradicts the record or arithmetic (correction given); GAP = ambiguous, or
the record is internally split; MISSING = something a computing group needs that is absent.

## Summary of blocking items (fix before acceptance)
1. E.14 Cost: density-vertex stage given as "of order 50 to 70 core-hours"; the record has 2–3 days on 4 cores = 200–300 core-h (DC-1). WRONG.
2. E.14 Germanium window: "20 to 60 core-hours"; the record has 20–60 h on the 4-core box = 80–240 core-h (DC-2, COMP-PH §6.2). WRONG.
3. E.14 Neutron-scaled onsets "0.3334 and 0.3378 MeV": copied from COMP-PH §4, but they contradict the text's own rule δm = 2δω/v_max². WRONG (see E.14-7).
4. E.14 The text never says which calculation covers the replica shell 0.3332–0.3374 MeV that it treats as the onset (DC-1 starts the ω grid at E_x + ω_TA). GAP.
5. E.15 Resonant-only versus TDA. The text keeps CW1 §5 wording that CW1-errata E-10 corrected. The pass criterion is missing. WRONG.
6. E.17 "about 4000 reciprocal-lattice vectors" for |Q+G| ≤ 20 keV. A direct count gives 725 (Si) and 821 (Ge) per Q. WRONG (the source CW2 §4 is also wrong).
7. E.18 S(q;ω_l,ω_e) "in eV² per cell": a joint density in two frequencies per cell has units eV⁻² per cell (DC-25). WRONG.

## E.14 Phonon-assisted electron recoil (DC-1…8, 97)
- E.14-1, the known case: "allowed-size zero-phonon line opens near 0.50 MeV" (line 63). CHECKED. It matches SOTA l.641 and LE-25 (CW1-L3: allowed-size
  (2̄00)-class ZPL opens at ≈ 0.50, ZPL/PAER 2.4–7.0, leads from ≈ 0.51; the old 0.547 is the nearest-pocket value and is withdrawn, as is 0.62). The text keeps
  all four quantities apart:
  (a) PAER onset 0.3332 (replica) / 0.3374 MeV (free pair), §"The onset, verified".
  (b) First zero-phonon edge 0.405–0.408 MeV (best 0.407). It is the joint minimum, off the axis.
  (c) Second heavy-hole cone, 0.415–0.420 MeV.
  (d) X-face allowed-size edge, ≈ 0.50 MeV.
  The 0.405 lower end of the opening sentence is also correct. Optional clarity edit: the 0.405–0.408 state is in the symmetry-suppressed (second, glide) class, so its
  vertex is small. Say so in one clause where 0.50 is introduced, so that a reader does not ask why the "first" zero-phonon state does not lead.
  Note: DC-1 ("window 0.333–0.408"), DC-5 ("above 0.547 MeV") and DC-6 ("0.408–0.547") are stale against SOTA. The tex correctly follows SOTA.
- E.14-2 Bins: |q| 0.25–1.25 Å⁻¹ (0.49–2.47 keV), 21 values, 30 directions, 630 targets, ≈ 1800 unfolded. CHECKED (DC-1; COMP-PAER §8).
- E.14-3 ω range (line 7): "ω from the onset E_g + ω_TA(Q*)". GAP. A free-pair amplitude at n_g = 2 with no excitons has no weight below E_g + ω_TA, so the
  grid start is right for this chain. But DC-1 starts at E_x + ω_TA, and the section quotes the replica edge 0.3332 MeV as the onset. Correction: state which
  calculation supplies the replica shell (the E.15 bound-line/Wannier–Mott envelope times the free-pair amplitude), and that the two are matched at E_g + ω_TA.
- E.14-4 Sternheimer remainder (line 52): "for the momentum transfers of this window, |q| ≲ 0.5 αm_e, it is a correction". GAP. 0.5 αm_e = 1.86 keV, but the grid
  runs to 2.47 keV, and the zero-phonon cones of §"Zero-phonon rates" run to 1.9 keV. DC-1 and COMP-PAER §8 specify the remainder "for the Bethe-ridge part at
  |q| > 0.5 αm_e". Correction: "it is a correction below |q| ≈ 0.5 αm_e ≈ 1.9 keV and must be carried in full on the upper bins (1.9–2.5 keV)".
- E.14-5 Table parameters (PBE, 5.431 Å, 60 Ry, 12³, 8³ with 29 irreducible points, 18 WFs to +40 eV, ≤ 10 meV to +10 eV, 2 %/5 % vertex tests, 60³→120³ tetrahedra,
  5 % per bin). CHECKED (COMP-PAER §8 stage table). The 8³ versus 4³ artifact (≤ 1.5 meV): CHECKED (COMP-PAER l.32, IF-CP-5).
- E.14-6 Controls C1, C2, C6 (8-atom cell, ±0.005 Å), C7 (10⁻²…10⁻⁴·2π/a, 3 directions), symmetry zeros, C8 GaAs. CHECKED (DC-1, DC-8; COMP-PAER §8).
  GaAs PAER-leading band 0.43–0.51 MeV [parabolic]: CHECKED (CW1 §24, LE-47).
- E.14-7 Onset (lines 69–71). Several numbers are correct: E_g 1.170 eV, E_x^b 14.7 meV, ω_TA(Q*) 14.72 meV at |Q*| = 0.510 Å⁻¹, 0.3332/0.3374 MeV, the rule
  2δω/v_max² = 8.5×10⁻⁵ MeV for 0.3 meV, and the neutron and lattice-constant statements (1.6 %, 8 %, 3.5 %). CHECKED: COMP-PH §2, §4, and my arithmetic with
  v_max = 794.5 km/s.
  WRONG: the neutron-scaled variant, "ω_TA ≈ 15.2 meV and onsets 0.3334 and 0.3378 MeV". By the text's own rule, +0.48 meV moves the edge by
  +1.4×10⁻⁴ MeV, giving 0.3333 (replica) and 0.3375 (continuum). The envelope theorem gives the same shift, because ∂m/∂E_th = m/(qv − E) = 2/v_max² at the
  optimum. COMP-PH §4 carries the inconsistent 0.3378. Correction: "onsets ≈ 0.3333 and 0.3375 MeV". Alternatively, keep 0.3378 only after a recomputation
  shows a q*-shift effect; the Ge analogue in COMP-PH §3.3 obeys the linear rule (+0.9 meV gives +0.0003 MeV).
- E.14-8 First ZPL edge: 0.405–0.408, best 0.407, six-variable joint minimum, 0.415 on-axis bound. CHECKED (SOTA l.638; CW1-errata E-1).
- E.14-9 Zero-phonon side. CHECKED (CW1 §3.3; CW1-errata E-15(2), IF-CW1-4): cones 1.2–1.9 keV, ϑ ≤ 0.4 rad, 0.15 rad out of plane, ±0.3 eV; hole 0.061 eV below
  the VBM; Σ|ρ|² = 0.150; SOC +15.5 meV; stencil 0.02→0.01; angle 0.01→0.005 rad; ratio stable to 5 % under 1.5× bins; < 1 core-h.
- E.14-10 Germanium bands and phonons: HSE06, ecutfock 160 Ry, nqx 4³, 8³ nosym, 16 spinor WFs, 20 d bands excluded, VBM+3 eV, L-below-Γ control within 0.1 eV of
  0.744 eV; TA −13.5 %/−11.6 % at 80 K, optical ≤ 2.3 %; 12³ test at X ≈ 3 core-h; ≤ 0.0003 MeV. CHECKED (DC-2, DC-4; COMP-PH §3, §6).
  Cost of the 6³ run, "about 17 core-hours". GAP. DC-4 gives ≈ 14 core-h (13 min per q); COMP-PH §6.3 gives 16 min per q, ≈ 4 h on the box ≈ 16 core-h. Use 14–16.
  Wording (line 79): "PBE … puts Γ 0.047 eV above … the reverse of the measured order, with the indirect gap at L, 0.744 eV, below the direct gap at Γ, 0.89 eV". This
  reads as if PBE gave 0.744/0.89. Correction: "…the reverse of the measured order, in which the indirect gap at L (0.744 eV) lies below the direct gap at Γ (0.89 eV)".
- E.14-11 Germanium rate: 36 WFs, 120 spinor bands, 14 e⁻, ×4–8, 400–800 core-h. CHECKED (DC-3; COMP-PAER §9).
- E.14-12 GaAs. M_x v_max²/2 = 1.04 eV for 0.58 m_e, 140 Ry, scissor fit 1.52/1.71/1.98 eV: as in CW1 §24.
  GAP (physics): 1.52 and 1.98 eV are T → 0 values (Γ 1.519, X 1.981), but 1.71 eV is the 300 K L-valley energy. The low-temperature L minimum is ≈ 1.81–1.82 eV
  (Aspnes 1976; Vurgaftman et al. 2001, from memory, not fetched). A scissor fitted to mixed temperatures misplaces the L-class edge, which sets the top of
  the GaAs band (0.511 MeV). Correction: use the T → 0 set 1.519/1.815/1.981 eV, or state the temperature. Flag to the record owner (CW1 §24 carries the same set).
  Window cost, "about 2 core-hours with the scissor and 10 to 20 with the hybrid". GAP: CW1 §24 says "≈ 10–20 h CPU (HSE) or 2 h (scissor)"; DC-8 gives
  0.3–1.5 h on the box. If "h CPU" is wall time on the 4-core box (the DC convention), the figures are 8 and 40–80 core-h. State the basis.
- E.14-13 f-sum section. CHECKED (COMP-PAER C4, IF-CP-4; CW1 l.306 for "60 bands ≥ 0.95 with the commutator term"): 0.81 (16 bands) → 0.89 (100 bands) at
  0.1–0.5 Å⁻¹ (the source has 0.78–0.81 / 0.88–0.89).
  Eq. (E.14-remainder): correct (P⊥ commutes with H(k+q); dimensions are energy).
  Decomposition q·v^g + q²/2m + δ_NL: correct for a nonlocal V_NL.
- E.14-14 Cost. Stage 2: 8 min × (1.5)^1.5 × (1.5)³ × 29 ≈ 24 h on 4 cores ≈ 100 core-h. CHECKED.
  Stage 5 (density vertices), "two to three days of processor time, of order 50 to 70 core-hours". WRONG: 2–3 days on 4 cores = 200–300 core-h (DC-1;
  COMP-PAER §8), and it is the dominant CPU stage. Correction: "two to three days on four cores, 200 to 300 core-hours".
  Stage 6: the text's ≈ 10¹⁶ flop follows App. E.5 (worked count, accepted), while DC-1 and COMP-PAER §8 give ≈ 10¹⁴ flop (10¹⁰–10¹¹ per bin × 2×10³ bins). GAP: the
  book is internally consistent with E.5, and the record is two orders lower. Keep E.5's count, but the total ("a few hundred core-hours plus an accelerator-day")
  should then be stated as an E.5 estimate. DC-1 gives 300–450 core-h + 2–10 GPU-h, and CW1 §3.3 gives ≈ 1 GPU-day. After the stage-5 fix the CPU total is
  ≈ 400–500 core-h.

## E.15 Excitons and core states (DC-9…13, 16)
- E.15-1 TDA paragraph and Eq. (E.15-tda). WRONG (superseded). CW1-errata E-10: (CW1.5) is the error of a resonant-only ε₁, not of the TDA. A standard (retarded) TDA
  keeps both ±E_λ poles, takes ε₁ by Kramers–Kronig and has no ×2 error. The remaining coupling-block error is O(K_LF/(Δ + K_LF)) ≈ 10 % on the proper ε₂, so
  "ε₂ unchanged" is also superseded.
  The arithmetic is right as a resonant-only estimate: ratio (E₀+ω)/2E₀ = 0.635, ε₁^res = 3.86, L ratio ≈ 2.0. The fix is wording plus the test.
  Corrections:
  (i) in the estimate paragraph and Eq. (E.15-tda) only: "the resonant-only form (one time ordering)", not "the resonant form" or "TDA". The opening
  sentence (published DM runs used the TDA) stays, but it must not be tied to the ×2 claim;
  (ii) add "a retarded TDA has no such error; the remaining coupling error is ≈ 10 % on ε₂";
  (iii) the test (line 31) becomes: report S^{TDA,ret}, S^{full} and S^{res-only} at 0.5, 0.7, 1.0, 1.4 keV; pass |S^{TDA,ret}/S^{full} − 1| ≤ 0.15. The pass
  criterion is MISSING in the tex.
- E.15-2 BSE grids. CHECKED (DC-9; CW1 §5): 4 VB × 12 CB, 8³ → 24³, 24,576 pairs ≈ 10 GB, 6.6×10⁵ pairs, 7 TB, 200 Haydock, 10³ momenta, 10³ node-h ≈ 3×10⁴ core-h,
  a_x 4.9 nm, 1/(3a_x) = 0.007 Å⁻¹, 24³ spacing 0.08 Å⁻¹ (|b|/24 = 2.004/24), f-sum < 1 %, q < 3αm_e, 14.7 meV.
- E.15-3 Dispersion. CHECKED (CW1 §6): Hessian step 0.005·2π/a, 30 Gaussians, 0.1 meV, ε_∞ 11.7, six-band k·p, Δ_SO 44 meV, minutes.
- E.15-4 Replicas and the ED chain test. CHECKED (DC-10; CW1 §7; CW1-errata E-15): 10³ k per pocket, 10⁴ core-h, 0.3332 MeV, N = 8–12, g 10⁻³–10⁻², 10⁻⁶ at W = 0,
  W/E_g 0.05–0.3, ~E_x^b/E_g ≈ 1 % (14.7/1170 = 1.3 %), N⁴ basis, residual 10⁻¹⁰.
- E.15-5 Exciton Migdal. CHECKED against CW1 §8 (8³ IBZ + shells to 5 keV, ≈ 60 points, 3 bands, 20 lines, 50 G, 10³ → 8×10³, ≈ 1 node-h per p, 60–100 node-h).
  GAP: DC-11 gives 10⁴ core-h; 60–100 node-h × 32 = 2–3×10³ core-h. The text follows CW1; the record should be aligned.
- E.15-6 Self-trapped excitons. CHECKED (CW1 §9 + errata E-15): Huang–Rhys form, Gaussian limit, α = 0.25/0.40, 64–216 atoms, 10 %/20 %, I SOC ≈ 0.9 eV.
  Cost "about 10³ core-hours" matches CW1 §9. GAP: DC-12 gives 10⁴–10⁵ [E-DC]. The DC cost has no source basis; note it for the record owner.
- E.15-7 Core levels. CHECKED (DC-13; CW1 §10; errata E-15): ZORA/FLAPW, (Z_eff α)⁴ ≈ 10⁻⁶, ≤ 2 % bound, central 10⁻³, 29.5 eV, −0.58 % to 0.1 %,
  12³→16³ < 0.05 %/2 %.
  GAP (cross-section consistency): E.15 calls −0.58 % "the relativistic f-sum shift … for germanium", while E.16 gives the total for Ge as −0.73 % (CW3 §3.2).
  SOTA l.140 confirms that −0.58 % is the mass–velocity part −(5/3)⟨T⟩/m. Correction in E.15: "the mass–velocity shift of the f-sum rule, −0.58 %".
- E.15-8 SOC at the edges. CHECKED (CW1 §13; CW1-errata E-12, E-15): 3.6×10⁻⁶ (Γ₈ quartet sum), 1.3×10⁻⁴ mirror, Ge ≲ 10 % [E], 60→80 Ry < 2 %, ecutfock 120→160,
  nqx 3³→4³ < 10 meV, < 1 core-h.

## E.16 Electronic response libraries (DC-14, 15, 17, 28, 39, 40, 54, 88)
- E.16-1 Library. CHECKED (DC-14; CW1 §15 l.306–308): 12 real functions (PT symmetry), 10³ k, |q| ≤ 25 αm_e in steps of 0.1 αm_e, 30 directions, ω ≤ 50 eV in 0.05 eV
  steps, 60 bands, 8³→12³ < 3 %, 6→8 αm_e < 1 %, f-sum ≥ 95 %, PT zeros < 10⁻³, nonlocal-current bias ≈ 10 %.
  Cost 50–100 core-h (Si), ×4 (Ge): matches CW1. GAP: DC-14 gives 10³–10⁴ [E-DC, "not estimated in the source"], which is stale against CW1.
- E.16-2 j_T local-field screening "estimated at 10 to 30 %". CHECKED (WP1-v3 l.136; CW1 l.273). The 8–39 interval was withdrawn (CW1-errata E-11), and the tex
  correctly does not quote it. Triplet ladder O((a/a_x)³) ≈ 10⁻³: CHECKED (CW1 §11).
- E.16-3 Anisotropy. CHECKED (DC-15; CW1-errata E-15 LE-39): Lebedev 110 → 230 → 434 (degrees 17/25/35), 1 % on S₄,₆,₈, cone grid, 14–107 meV at 0.13–0.34 rad,
  ℓ = 1, 2, 3 < 10⁻³.
- E.16-4 Local fields in the window. CHECKED (DC-17; CW1 §16–17; CW1-errata E-15 LE-41):
  model: 2000–8000 k, gap 1, width 2, half-zone cutoff, ε(P) 1.5–4, RK4 0.01/E_g, ≥ 200/E_g, 10⁻³;
  supercell momenta (n = 3: 0.76/1.08/1.32/1.52 keV; n = 4: 0.57/0.81/0.99/1.14 keV; first shared nonzero |q| = 2π/a = 2.28 keV, verified);
  convergence tests n = 2→4 at 1.14 keV and interpolated n = 3/4 within 5 %; 3 Ry, E_F + 30 eV, Γ vs 2³;
  costs 10²/2×10³/2×10⁴ core-h; δ_LF^(0) of Eq. (E.16-dLF) (equals 1 without local fields, checked), 40 bands, 12³, 4 Ry (≈ 60 G), 3→5 Ry < 1 %, ≈ 10 core-h.
- E.16-5 Loss functions. CHECKED (DC-28): semicore list, f-sum 2 %, ∫L/ω⁴ < 1 %, E_g/20, bound (π/2)ω_p²/E_g⁵ (valid because ω ≥ E_g on the support).
  Cost "tens to a hundred core-h (two-atom), several hundred (ten-atom)" is within DC-28's 10²–10³ per material.
- E.16-6 Relativistic f-sum. CHECKED (DC-39; CW3 §3.2; CW3-errata V5): −0.23 % (Si), −0.73 % (Ge); δ_oo ≈ 0.27 δ_mv gives 21 % of the total (0.27/1.27, checked);
  1.8×10⁻³ (Si mass–velocity) is consistent with −0.23 % total; X2C, cc-pwCV5Z, 10⁻⁴, 10⁻³, 50/a₀, 10 core-h.
- E.16-7 Static step. CHECKED (DC-40; CW3 §3.3): Ω_{P,e} = 0.51 eV, recomputed as ω_pe(14 e⁻/atom) × (14 m_e/M_Si)^{1/2} = 31.1 eV × 0.0165;
  Ω/c_L = 18 keV; (18.2)² ≈ 3×10² at 1 keV; 1×1×N with N = 2…8, 1 %, 2 %, 10² core-h. The small-q limit of Eq. (E.16-step) reduces to Ω²/(c_Lq)² (checked).
- E.16-8 Kinetic row. CHECKED (DC-88; CW7 §6, (CW7-155)): the 1/(4m_e⁴) prefactor (𝒯 = p²/2m_e²); the sum rule ⟨(∇V)²⟩/(2m_e³) (CW7 derivation via p² = 2m(H − V));
  80 Ry, 24³, 20 meV; minutes / one accelerator-hour.
  Minor GAP: the tex says to compute ⟨c|p²|v⟩ directly "rather than as Σ_m p_cm·p_mv", while (CW7-155b) defines it as that sum. Both are the same object; say
  "equivalent to Σ_m p_cm·p_mv over all bands including the core, which converges slowly".
- E.16-9 Boosted recast. CHECKED (DC-54; CW4 §18): (1 − ω²/q²)² ≥ 0.98 for v_χ ≤ 0.1, reproduce to 5 %, iη scan, form factor at q² − ω². Citation liang2025plasmon =
  2401.11971 fetched: it is the cosmic-ray-boosted plasmon paper, with Si and Ge detectors, as the text says.

## E.17 Lattice libraries (DC-18…23, 29, 33…35, 91…96, 98)
- E.17-1 Base. CHECKED (DC-19): 80 Ry, 12³, 8³, 10⁻¹⁶, 0.1 meV between 6³ and 8³, INS 5 %, PBE 0.7–1 %/2–4 %, 25/60/60 core-h.
- E.17-2 Deformation tensors. CHECKED (DC-18): ±0.5 %, symmetric at the extrema, D/c ≈ 9 eV/(8.2 km/s) = 329 keV ≈ 300 keV (checked). DC-18 cost 5–20 core-h versus
  "minutes": GAP, minor.
- E.17-3 Multiphonon library. CHECKED (DC-21; CW2 §10): 400 log points from 0.1 to 300 keV, 0.1 meV to 1 eV, T ∈ {10 mK, 1 K, 77 K}, x_R > 16, 48³ tetrahedra,
  ≈ 300 lines, Einstein test 10⁻⁵, f-sum 10⁻⁴, t_max ≥ 20π/δω, incoherent ℓ ≥ 4 < 10⁻⁶.
- E.17-4 Eq. (E.17-Wn): GAP (units). Its 1/(n!Ω) prefactor (as in CW2.3; SEAM E-e gives 𝔚 units 1/Ω) makes 𝔚 a per-volume weight. But the same section
  states S in "eV⁻¹ per cell", for which ∫dω S/2π is dimensionless per cell. Fix: either say "S^(n) per unit volume" at Eq. (E.17-Wn), or drop the 1/Ω.
  Coherent two-phonon, Eqs. (E.17-Bkk), (E.17-Wn), otherwise CHECKED (DC-20; CW2 §1–2): the n-th Taylor term of e^{C} at t = 0. The T = 0 decay ΔR⁻² (FT of 1/Q) gives
  absolute convergence for n ≥ 2 and divergence for n = 1. 40 log q values, 0.5 meV bins, 40 Å, 48³, 0.25 meV, 32³→48³→64³ within 2 %, a few core-h. Lebedev 590 is
  exact to degree 41 (true). Si ℓ = 4 at 2.2 % and ℓ = 6 at 0.02 % (CW2 l.281): CHECKED.
- E.17-5 Charge vertex at large q. WRONG: "about 4000 reciprocal-lattice vectors" for |Q+G| ≤ 20 keV. An explicit count on the fcc reciprocal lattice gives 725 (Si,
  a = 5.431 Å) and 821 (Ge/GaAs, a ≈ 5.65 Å) G vectors per Q. 4000 may count the (κ, α) components (725 × 6 ≈ 4350). Correction: "about 700–800 reciprocal-lattice
  vectors per Q (Si, Ge)", and notify the CW2 §4 owner.
  CHECKED: ecutrho ≥ 65 Ry for |G|max = 30 keV (CW2-errata E-5(b) supersedes the old ≈ 260 Ry); PAW aliasing above ≈ 10 keV; 216 atoms, ±0.01 Å; sum rule 10⁻³;
  core polarization by Dalgarno–Lewis; costs.
- E.17-6 eκ factor. CHECKED (DC-23; CW2-errata E-6, E-7): valence anisotropy ≤ 1.3×10⁻³; finite-nucleus contact density +8 % (Si), +37–45 % (Ge/Ga/As); r_min ≤ R/100;
  nuclear model < 1 %; 10⁻⁵; 10 core-h.
- E.17-7 PIMD. CHECKED (DC-29): P ≈ 250 at 10 K (64 meV/0.862 meV/0.3 = 248), PIGLET 16–32, 50–100 K, 3σ, ≥ 10⁶ steps, 10³ core-h.
- E.17-8 Isotope Hessians and two-phonon ε₂. CHECKED (DC-33; CW2 §18; CW2-errata E-9): 4096 atoms (8³ × 8), 12,288 dof, 13,824 atoms, +9 % at 50 meV, 2 %;
  displacements ±0.005/0.01/0.02 Å with linearity < 2 %; 293 K reproduction to 20 % in 40–60 meV; 1.2×10² and 2×10³ core-h.
- E.17-9 Dynamical Born charges. CHECKED (DC-35; CW2 §15): |ΔZ*| ≤ 0.90(ω/1 eV)² against Z*(0) ≈ 2.1; η 10–20 meV; sum rules; ≈ 50 core-h per batch.
- E.17-10 GaAs near-cancellation. CHECKED (DC-34; CW2-errata E-10), recomputed: Z/M = 0.4446 and 0.4405; d = −1.33×10⁻³ at Z* = 2.16, ε_∞ = 10.9; +10 % gives 41 %;
  2.4 %. Eq. (E.17-lst) is dimensionally correct and gives Z*/ε_∞ from ω_L² − ω_T² = Z*²e²/(ε_∞ μΩ). Strictly, that relation combines LST with the mode-sum for
  ε₀ − ε_∞; "through the Lyddane–Sachs–Teller relation" is acceptable shorthand.
- E.17-11 Batch table. CHECKED (DC-91; COMP-PH §6.1, converted at 4 cores): 2-atom cells 2–20 core-h, GaAs 20–25, 4H-SiC 40–80, Al₂O₃ 120–240.
  CHECKED: Si ε_∞ +11 %; soft modes (< 20 cm⁻¹ flag); U by linear response; CsI PBE/PBEsol (DC-93); phono3py 10³–10⁴ core-h; Ge ×10 spread (DC-96); QHA with five
  volumes, Si negative expansion below ≈ 120 K (DC-98).
- E.17-12 MISSING (executability): DC-92 (CaWO₄, Li₂MoO₄: 1.2–5.4×10³ core-h), DC-94 (magnetic DFT+U DFPT: 1.1×10⁴–10⁵, YIG dominant), DC-95 (23 further survivors:
  10³–5×10³) and DC-98 (5×10³–2.5×10⁴) have no cost in the tex. One line per item, or a "remaining batch" row in tab:E17-batch, would close this.

## E.18 Migdal and non-adiabatic quantities (DC-24…27)
- E.18-1 Drag masses. CHECKED (DC-24; CW2 §8): 14 m_e/M_Si = 2.73×10⁻⁴; P_Mig ≤ E_R δM/(M E_g) gives E_R ≤ 4.3 eV (Si, E_g = 1.17) and 3.1 eV (Ge, δM/M = 2.42×10⁻⁴,
  E_g = 0.744), both checked. Eq. (E.18-sth): one Δ⁻¹ per solve gives Δ⁻², Δ⁻³, Δ⁻⁴ (checked). The Φ^el(iω) slope gives δM. Trace N_e m_e; 12³→16³ within 1 %;
  75/180 core-h; GaAs zero-field transverse rule.
- E.18-2 Crystal Migdal rate. WRONG units: "S(q;ω_l,ω_e) in eV² per cell". DC-25 gives eV⁻² per cell (a density in two frequencies). Correction: "in eV⁻² per cell".
  CHECKED: p ≤ 30 keV, ω_e ≤ 100 eV, impulse bracket at 10⁻², 50³ per shell (CW2 §14); |G| ≤ 4→6 a₀⁻¹ ≈ 292→987 plane waves in Si (counted); 16 MB, 2000 ω, 32 GB;
  8³→12³; 10³ core-h; adams2023measuring = 2210.04917 (DC-25 neutron calibration).
- E.18-3 Wannier ratio. CHECKED (DC-26; CW4 §19 + errata A3(c)): 2W/ω + W²/ω² = 1.56 at 20 eV and 0.25 at 100 eV for W = 12 eV; bare vertex screened at ω_e; 16³ k;
  ASR 10⁻³; 10³ core-h.
- E.18-4 Couplings not ∝ mass. CHECKED (DC-27; CW2 §24): |G| ≤ 6(2π/a) contains ≈ 226 G (counted); |S_bas|² = 0, 2, 4 for (200), (111), (220); < 1 MB per ω; 2 %; 12³;
  10² core-h.

## E.19 Anharmonic, disordered and quantum solids (DC-30…32, 36, 37)
- E.19-1 Quantum crystals. CHECKED (DC-30; CW2 §5, §23; CW2-errata E-12): supercell atom counts 320/1080/2560 and 512/1728; P ≈ 80 for SrTiO₃ at 50 K
  (100/4.31/0.3 = 77); 80 ps for 0.5 meV (20π × 0.658 ps·meV/0.5); He at 21 cm³/mol, P = 64→128, N = 180→432; MK band 2/3 at the peak, (ω − ω̄)⁻⁴ tail.
  The "eV²" units of S_self follow the book's per-volume convention (cf. Fig. 4.x caption, S⁰ in m_e k_F); DC-30's eV⁻¹ is per cell. CHECKED, but use one convention.
  Prose defect (line 23): "The self-consistent harmonic ladder costs about 10² for the self-consistent harmonic ladder, 10³ for helium at melting and 10⁴ per
  pressure". Correction: "The self-consistent harmonic ladder costs about 10² core-hours per material, path-integral helium at melting about 10³, and
  high-pressure helium about 10⁴ per pressure."
- E.19-2 Weak anharmonicity. CHECKED: "n_A = 2" agrees with the editor ruling (NOTATION l.1115); DC-31's "n_A = 1 (η²)" is the older counting. 128 atoms,
  ≈ 300 runs, 5 Å; 384³ × 8 B = 0.45 GB (checked); 3³→4³, 4→5 Å, 24³→32³; first-order Φ³ vanishes (the TR argument is sound); 10³–10⁴ core-h.
- E.19-3 Glass models. CHECKED (DC-32): 648–5184 atoms, ≥ 5 quenches, 192–648-atom subcells, 15552² × 8 B = 1.9 GB, 4×10¹² flop, 1728 vs 5184 within 5 %, ≥ 4 nm,
  ΣZ* = 0, 2πc/L ≈ 3–4 meV (checked with c_T ≈ 3.75 km/s), 10⁴/10³/10² core-h. In Eq. (E.19-CIR), B^IR = S″/(2c²) (checked).
- E.19-4 Random medium. CHECKED (DC-36; CW2 §22; WP7-B2-v2 l.166): σ_crit 1.2×10⁻³⁸ cm² at 20 eV and v = 10⁻³; R_slab = 2R/(1+R); ρ_χv² ≈ 4.8×10⁻¹¹ Pa;
  λ_dB ≈ 62 μm; Eq. (E.19-wall) is dimensionally a pressure.
- E.19-5 Chiral branching. CHECKED (DC-37; CW2 §25; CW2-errata E-11): 10×10×20, 10⁵ versus 10³ core-h, 27 Stevens parameters (5+9+13), ±0.01 Å, linearity
  0.005–0.02 Å, 0.5–2 core-h per geometry.

## E.20 Magnetic, superconducting and Dirac targets (DC-41…46, 48…50)
- E.20-1 Al BCS. CHECKED (DC-41; CW4 §1, §8): 2v_F/(πv_max) = 1.63 at v_max/v_F = 0.39; case-I pair-creation factor ½[1 − (ξξ′ − Δ²)/EE′] (Tinkham convention);
  10⁻³ tests; 2609.06423 Eq. (7) (gan2026mean, bib eprint matches).
- E.20-2 a-WSi. CHECKED (DC-42; CW4 §2): 2π/25 Å = 0.50 keV; cost sum 1.6×10⁴–1.6×10⁵ (checked); ε⁻¹₀₀, not 1/ε₀₀.
- E.20-3 Holstein. CHECKED (DC-50): EPW grids (Al 60³/30³, Nb 40³/20³), T_c within 10 %, 5 %, 20 %, transport weight, 10³ core-h.
- E.20-4 Magnets, two-magnon, form factors. CHECKED (DC-43…45): ΔS = 0.078 gives 0.146/0.049/0.029 (recomputed); 30³–40³; 3×10⁷ ops per q; 1 % sum rules;
  10²/10³–5×10³/< 10 core-h per ion; 1/⟨r⟩_4f ≈ 3 keV.
- E.20-5 Optical activity. CHECKED (DC-46): 16³→24³ within 5 %, Si odd part zero, nonlocal commutator, 10³–10⁴ core-h.
- E.20-6 ZrTe₅. Checked against CW4 §6, CW4-errata A6, A7 and the fetched 1708.08929 Table 1 and 1910.02091 Table 2:
  ε_bg = 25.3 is the harmonic mean of Hochberg's κ = (187.5, 9.8, 90.9). Verified: 3/Σκ⁻¹ = 25.3.
  The axis factors 9.5×10⁴/431/1.6×10⁴ are Geilhufe's κ = (308.4, 20.75, 126.1) squared, also verified.
  Ry_D = 0.15 meV and a_D = 1.96×10³ Å recomputed; 37 × 1/a_D; factors 1600/6.3 at ε_bg = 40 and 640/5.0 at 25.3; G₀W₀ 10⁴ core-h.
  GAP (notation): the tex's α̃ ≈ 0.22 is α/(ε_bg v_D), while the record (CW4 (6.1), errata A6) quotes α̃ = 0.44 with Ry_D = Δ_D(α̃/g_deg)²/4.
  The numbers agree (SEAM E-f: "computed in the book's α̃"), but E.20 never states that α̃ = α/(ε_bg v_D). Add it, and align with 16.1 when written.

## Executability: what a computing group would still need
- E.14: the inputs of stages 1–4 exist (code/COMP-PAER/tierH/{Si,Ge}). The text never says that stages 5–6 and the quadrupole file are new code to write.
  It names them, but not that they are unwritten. Add "not in any public code; a few hundred lines on top of EPW".
- E.14/E.16/E.17: the memory and disk figures are in the record but absent from the tex: E.14 Ge 4–8 GB (present); E.16 Route-S n = 4 memory (missing); E.17 base
  (missing). Minor.
- E.17-12 (above): missing costs for DC-92, 94, 95, 98.
- E.15 TDA pass criterion missing (E.15-1).
- E.16 library: no pass threshold for the f-sum with the PAW/all-electron cross-check (the 95 % rule is for norm-conserving + commutator). Optional.

## Internal labels and banned terms
Grep of E-14…E-20 for DC-, LE-, CW#, WP, COMP-, [CALC], [E], [D], [C], XG-, IF-, CMPMC, GAP-EF and every regex in BANNED-TERMS.txt: no hits. CHECKED.

## Cited values against fetchable sources
- liang2025plasmon (2401.11971): fetched. It treats cosmic-ray-boosted DM with plasmons in Si and Ge. CHECKED.
- hochberg2018detection (1708.08929): fetched, Table 1 and l.1103–1105. κ harmonic mean 25.3. CHECKED.
- geilhufe2020dirac (1910.02091): fetched. Table 2 ZrTe₅ κ = 308.4/20.75/126.1, Δ = 11.8 meV, Eqs. (3.13)–(3.14) present. CHECKED.
- shaklee1970valley (14.7 meV), macfarlane1958fine (20 K), nilsson1971/1972: bib consistent with the use; values from the record (papers paywalled, not on arXiv).
- adams2023measuring = 2210.04917; gan2026mean = 2609.06423; liang2020describing = 1912.13484 (diamond Wannier Migdal): bib keys match the record's identifiers.
- Fetched PDFs/HTML of this review (2401.11971, 1708.08929, 1910.02091) were deleted. Other files in sources/review-appE2/ belong to other reviews and were left.
