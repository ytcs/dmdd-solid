# Ch14 post-revision check (isolated verifier, 2026-11-06)

Scope: tex/ch14/*.tex (incl. s14-summary), appD/D-38, the revised lines of appE/E-26 and E-20, ch11/s11-8 and ch08/s8-2, figscripts/ch14 logs, review ledgers and rulings R1–R10. Light Python/sympy only (scratch scripts, nothing in the repo). No tex or script edited.

**Verdict: ACCEPT WITH FIXES** (all fixes are minor wording/caption edits; no number is wrong).

## 1. R2, neutron no-go

- **Model-independent statement: CONFIRMED.** Every magnetic amplitude contains the electron spin (and orbital current) density only through its part transverse to q. Nuclear and Schwinger terms couple to charge, not to s_e. So at a given q no neutron measurement, polarized or not, reaches q̂·S·q̂ or the mixed elements. The symmetry argument (elements that fix q̂ preserve the transverse/longitudinal split, and equivalent wavevectors repeat the same equation) is correct.
- **eq:14.4-Glat: CONFIRMED, with one CONCERN.** For one magnetic ion per primitive cell, e^{iG·R_j} = 1, so s_e(k+G) = F(|k+G|) Σ_j e^{ik·R_j} S_j and S(k+G) = |F|² S^lat(k). This holds for the dipole-approximation scalar form factor with isotropic g.
  - CONCERN: the Debye–Waller factor is e^{-2W(k+G)}, which changes with G. It is a known scalar that belongs beside |F|², not "included" in S^lat(k). Fix: write |F^mag(|k+G|)|² e^{-2W(k+G)} S^lat_ab(k), or say that the DW factor is taken at k+G alongside the form factor.
- **Rank argument: CONFIRMED.** Each G gives the row (1−n_x², 1−n_y², 1−n_z², −2n_xn_y, −2n_xn_z, −2n_yn_z) acting on the six symmetric components.
  - I redid it symbolically (sympy, exact) at k = 0: the four (111)-type directions plus (200) and (020) give rank 6. So do (111)×4 + (200) + (002), and (111)×4 + (200) + (220).
  - we14_4.log (rank 6 at small k ≠ 0; reconstruction error 7e-16) agrees. The text's "four (111) + two (200)" is right, and stays right as k → 0.
- **O₆/O₁₀/ALP consistency: CONFIRMED, with a wording CONCERN.** s14-4 ("data at one q say nothing"; closing "not measurable without a model, but follow within the localized-moment model"), the key-result box, the Summary, nuisance row 15 and F-row l.450 all agree.
  - CONCERN: the box says no experiment measures the longitudinal element "without a model of the spin density". The 14.4.3 opener then says spin-rotation symmetry supplies it "at one q, without a model of the spin density". These two only reconcile because the isotropy route uses a Hamiltonian hypothesis (SOC and dipolar coupling neglected), which is not a crystal symmetry. R2 asks for "model-independently, no measurement".
  - Fix: in the box, write "Without a model of the magnet (of the spin density within the cell, or the spin-isotropy hypothesis of Sect. 14.4.3)…". In the 14.4.3 opener, write "…without a model of the spin density, at the price of a hypothesis on the Hamiltonian".

## 2. R7, Neyman construction

- **1.99 (median): CONFIRMED, and reproducible from the text alone.** For one bin, Q_obs is the background median, b ln 2.
  - Rayleigh: 1 − exp(−ln2/(1+s)) = 0.05 gives s/b = 12.513.
  - Fixed amplitude: ncx2.cdf(2 ln2; 2, 2s) = 0.05 gives s/b = 3.166.
  - √(12.513/3.166) = 1.988.
- **2.73 (detection threshold): CONFIRMED.** With Q_obs = b ln 20, s/b = 57.40 and 7.72, giving 2.727. I could not check that Centers et al.'s frequentist 2.7 uses the detection-threshold convention (the script comment says it does; source not opened). The numerical match is exact.
- **Multi-bin numbers: CONFIRMED.** I built my own SHM line (v0 238, v_esc 544, v_E 250.5) with a Fejér window, bins of 2π/t_int and one bin on the peak.
  - Δω_eq t_coh = 2.6747 and peak 0.579 ✓.
  - At t_coh: N_eff 1.20 and ratio 1.752 (book 1.758; grid-level difference). At 100 t_coh: 1.015 ✓.
  - 0.1 s → 1 s factor 3.47 (book 3.46) ✓. Hour → day 2.239 (book 2.24) ✓. Fixed/Rayleigh at 1 h: 1.0005 (< 0.1 %) ✓.
  - 3447 and 82 730 coherence times ✓ (t_coh = 1.0444 s).
- **CONCERN (reproducibility from the text).** The construction paragraph (s14-6 l.161) leaves out three inputs that the multi-bin numbers (1.76, 3.46, 23 t_coh) depend on:
  - (i) the bin width 2π/t_int, with one bin centred on the line peak (stated only in the fig:14-6 periodogram caption);
  - (ii) that the total signal is s = σ²_sig t_int at every record length (stated at l.151 for one bin only);
  - (iii) that Q_obs is the median of Gamma(N_eff, b).
  - Add one clause for each. limit14_6c.log is complete (41 lines).
- **8-site cluster (s14-3 l.159): CONFIRMED and reproducible.** I wrote an independent ED: cube corners, 12 bonds, XXZ, S^z_tot = 0 sector (dim 1107 and 8092). ⟨(S^x_tot)²⟩/4 relative to LSWT |S|√((Δ−1)/(Δ+1)) is 0.849 (|S| = 1) and 0.911 (|S| = 3/2) at ω_A = ω_E. LSWT mapping ω_E = 3J|S|, ω_A = 3J|S|(Δ−1) ✓. The 5–23 % for |S| = 3/2 matches ed14_3.log.
  - CONCERN: "below ω_A ≈ 0.3 ω_E its two lowest states mix" is true for |S| = 3/2 (splitting 0.5 % of ω_AFMR at 0.3). For |S| = 1 the 1 % criterion already fails at 0.5 (1.5 %), which is why the panel starts at 0.7. Fix: "(0.3 for |S| = 3/2, about 0.6 for |S| = 1)".

## 3. MnF₂ 4π fix: CONFIRMED

- M_sub = 5 μ_B/(a²c) = 5·9.274e-24 A m²/78.6 Å³ = 590 kA/m, so μ₀M_sub = 0.741 T.
- Vaidya's 47.7 kA/m × 4π = 599 kA/m (0.753 T). Their number is M/4π (the Gaussian 4πM convention), not an SI M.
- ω_M = 2μ_B μ₀M = 85.8 µeV and ω_E = 2μ_B B_E = 5.447 meV, so ω_M/ω_E = 1.58e-2. "1.6e-2" ✓. The order-of-magnitude shape shift ~N χ_⊥ ~ ω_M/ω_E is physically sound.
- Downstream numbers do not involve ω_M and are unchanged and correct:
  - ω_AFMR 1.021 meV; weight factor 0.0929; 0.232 per pair; B_sf 8.75 T; lower mode 0.009 meV at B_sf.
  - Refit ω_A = 0.110 meV: 1.100 meV, factor 0.100, 0.250 per pair, B_sf 9.41 T.
  - 1.1 meV ↔ 9.50 T ✓.
  - Per mass vs YIG 0.738/0.794 ✓.
  - Peak-rate ratio 7.2e-3 and 2.6e-2 s⁻¹kg⁻¹ for both sets ✓ (|S|ω_A/ω_AFMR² equal to 0.1 %).
- Limit Check 14.3a(b) is untouched by the fix. The square sits at the fitted ω_A/ω_E = 0.0174 (refit 0.020) and is far inside the gray band either way.
  - Optional: write "fitted fields" in the lim:14.3a caption, as the fig:14-lines caption does.
- Nuisance and F rows quote 1.6e-2 ✓. No 1.3e-3 or 47.7 is left in tex.

## 4. R1: CONFIRMED

- No "at least" or "bound" wording for ΔS/|S| in 14.1, 14.2, D.38, the Summary, the nuisance table ("est.") or the F row. The phrase "not a bound" is deliberate and fine.
- D.38 algebra rechecked:
  - Half-sum ⟨S⁺S⁻ + S⁻S⁺⟩/2 = |S| + 2|S|ΔS − ΔS − 2ΔS², with ⟨n²⟩ = ΔS(1 + 2ΔS) by Wick (no on-site anomalous term).
  - (|S|−ΔS)(1+2ΔS) + ΔS(1+ΔS) = |S|(1+2ΔS) − ΔS² ✓.
- Convergence: the differences 1.08e-4 and 4.97e-5 have ratio 2.17, against 2.16 for n⁻². The extrapolation gives 0.0785 ✓.
- WE: 1.066, (1.066 + 0.0846)/1.157 = 0.995 ✓.

## 5. R4: CONFIRMED, with one CONCERN

- t_coh = 1/(m v₀²) everywhere. The numbers check: 1.044 s at 1 neV, 1.04 ms and 249 m at 1 µeV, 0.10 ms at 10 µeV, ~1 ns at 1 eV, 87 ms at 12 neV. The 2π variant is quoted only as other papers' convention (6.6 s).
- Places checked: s14-6 l.25–28, s14-3 l.75, E-26 l.3, s11-8 l.116, s8-2 l.81.
- The golden-rule rule (mean needs t ≫ min(t_coh, 1/Γ); a single record needs t ≫ t_coh) agrees in s14-3 l.80, s14-6 l.35–41, the s14-6 opener (²⁰⁷Pb T₂ = 16.7 ms ≪ t_coh), s8-2 l.35 and l.81, and the Summary.
- CONCERN (E-26 l.7): it states only the min() condition, then "For shorter records … single Rayleigh amplitude … t^{-1/2}". For 1/Γ_T < t_int < t_coh the mean is golden-rule, but the drive is still one amplitude and the scaling is still t^{-1/2}.
  - Fix: add "a single record matches it only for t_int ≫ t_coh; below t_coh the drive is one Rayleigh amplitude and the sensitivity scales as t_int^{-1/2}".
  - Γ_T → Γ_tg in E-26 is already owed (LOOSE-ENDS f).

## 6. Spot checks

- **R5: CONFIRMED.**
  - Two-magnon factor 5.12 and edge 7.29 keV (fastest J₁+J₂ c = 1.364e-4), 1.46 keV ✓.
  - X-point zero: A = B = 6J₂ − 2J₁ = 116.8 meV, and w ∝ √(A−B) → 0 ✓.
  - M_sw = 1/(2D_sw) = 3.25 MeV ✓. De Broglie 2π/(m v_E) = 148 m ✓.
  - YIG 2π/a = 1002 eV, inscribed radius 708 eV, 134 keV ✓. p_n(120 meV) = 15.0 keV ✓.
  - ⟨v⊥²⟩ = 1.33e-6 and daily factor 0.47 ✓. 1/Γ_M = 6.6 µs ✓. Aybas 1.9 nT measured / 2.9 nT equilibrium ✓. 14.5 "0.2 MeV" ✓.
- **R6: CONFIRMED.** Γ_M is called an assumed value (14.3, WE, table). 4.54 meV is attributed "used by Hutchings and Samuelsen, quoted by dos Santos". "hexaferrite" is gone. Sm³⁺ is flagged as fragile (J = 7/2 close above). The Alves absorption trigger and boosted fraction are worded as ruled.
- **R8: CONFIRMED.** s14-summary.tex is input last and uses \section*{Summary}, and holds both tables. There are no "??" in Ch14.
- **R9: one residual.** The fig:14-2 caption (s14-2 l.44) still writes (Ω/2π)S^(2m), where the key result uses Ω_ion. Fix: Ω → Ω_ion. ω_M is gone from s14-5, Γ_T from Ch14, and Δ (gap) from s14-2 ✓.
- **Summary and nuisance table against the final sections: CONFIRMED,** with one CONCERN.
  - Values checked: 0.024/42, 3.2e3 near 3 MeV, 7.8 %/7.3 %/0.995, 5.1, 3.6 s⁻¹kg⁻¹, ~0.1|S| MnF₂, 0.83/0.73, ×1.44, 0.973, 1.99/2.73, 1.76/1.015, 13/6.5/1 t_coh, u_sp 3.8e-4 (π/(Γ_inh T₂) ✓), 30 %, 2.2 MeV, 0.082 near 1.4 keV.
  - CONCERN: the GaAs row reads "0.07 (another dynamical matrix)", which states a cause that R3 replaced. Fix: "0.07 (Matas et al.; a single Cartesian component gives 0.062, a possible origin)".

## Fixes required for acceptance (all minor)

1. s14-4 key-result box and 14.4.3 opener: make clear that the isotropy route is also a hypothesis (§1).
2. eq:14.4-Glat: put the Debye–Waller factor at k+G beside |F|² (§1).
3. s14-6 l.161: state the bin width and placement, s = σ²t_int, and Q_obs = median of Gamma(N_eff, b) (§2).
4. s14-3 l.159: the ordering threshold depends on |S| (0.3 for 3/2, ~0.6 for 1) (§2).
5. E-26 l.7: add the single-record condition and tie the t^{-1/2} scaling to t_int < t_coh (§5).
6. s14-2 fig:14-2 caption: Ω → Ω_ion (§6).
7. Nuisance table GaAs row: drop "another dynamical matrix" in favour of the R3 wording (§6).

Optional: say "fitted fields" in the lim:14.3a(b) caption for the MnF₂ square.
