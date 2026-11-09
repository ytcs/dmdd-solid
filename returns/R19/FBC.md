# R19 / FBC: full-band carrier cascade in silicon (stage 1)

Brief: briefs/R19/FBC.md. Code and small tables: code/FBC/ (checks.py **13/13 PASS**). Caches (rate, pair and seed
tables, 1.8 GB): /root/work/FBC/. Every number below is [CALC] in this sense: code/FBC/ holds the scripts, data/ holds
the tables, and checks.py holds the controls. Book values are read through state/CORRECTIONS.md and the SOTA
"Book-phase corrections"; neither touches Ch18. Run by Claude (LLM); not refereed.

## Result
1. **Pair energy and Fano factor without a fitted constant.** The full-band cascade gives **ε_eh = 4.13 eV
   [3.92, 4.47]** and **F_eh = 0.114 [0.110, 0.114] ± 0.002 (MC)**. Measured: 3.749 eV and 0.119 ± 0.002 at 123 K (book
   18.2/18.4). The book's calibrated model gives 3.749 and 0.114. The deformation-potential couplings are the
   Jacoboni–Reggiani literature values, not fitted. ε_eh comes out 10 % high and depends on the screening and the
   phonon couplings. F_eh is the same in every variant (0.110–0.114) and stays below the measured 0.119, as the book
   finds. The low F_eh therefore comes from the structure of the model, not from its calibration.
2. **P(N|ω), 2–20 eV, for the DM seed (heavy and light mediator, halo-averaged) and the photon seed** (tables in §5).
   P(N ≥ 2) at 5 eV is **0.111 [0.056, 0.155]**. The book's energy-only cascade gives 0.169, so the step model
   overcounts the two-pair bin by **9.0× [6.5, 17.7]**, against 5.9× in the book. Below 4.5 eV, phonon emission
   suppresses ionization more strongly than in the energy-only model: P(N ≥ 2) at 4.5 eV is 0.042 against 0.119.
3. **The computed electron/hole split removes 94 % of the α_RK ambiguity.** Inside the book's cascade, TV(α_RK = 1,
   α_RK = ∞) reaches up to 0.50 between 4.4 and 13 eV. The spread among the computed splits (heavy/light mediator ×
   two band calibrations) is ≤ 0.029. The book's EPM q₀ seed and the halo-averaged full-band split differ by ≤ 0.035.
4. **Valley and momentum memory is not resolved above MC noise.** Comparing the full run with the energy-only reduction
   of the same kernels gives TV ≤ 0.015, against 0.013 between two independent MC runs. This holds within the
   deformation-potential phonon model, which randomises k (§7).
5. **mK phonon competition.** Phonon emission decides everything near threshold. Without phonon emission, P(N ≥ 2)
   would be 0.99 at 4 eV instead of 0.008. Going from mK to 123 K (adding phonon absorption at fixed E_g) changes
   P(N) by TV ≤ 0.016, which is MC noise.
6. **Photon vs DM seed.** In the full-band cascade the two differ by up to **0.078 (at 10 eV)**; the book quotes ≤ 0.062.
   The photon/DM ratio of P(N ≥ 2) at 5 eV is 0.99; the book gives 1.12.
7. **Model distances (max over 4.4–21 eV; full-band DM heavy seed vs model).**

   | model | as in the book (A_AB = 5.674) | recalibrated to the full-band ε (A_AB = 12.31) |
   |---|---|---|
   | energy-only cascade, book DM seed | 0.26 [0.13, 0.45] | 0.16 (at 6.75 eV) |
   | energy-only cascade, computed split | 0.24 | 0.14 (at 7.5 eV); ≤ 0.04 for ω ≥ 10 eV |
   | R–K α_RK = 1 | 0.28 | 0.10 |
   | R–K α_RK = ∞ | 0.57 | 0.45 |
   | step model | 0.89 (at 5.0 eV) | 0.78 |

## 1. Bands
The book EPM is used as is (book/figscripts/ch03/epm.py, Cohen–Bergstresser local, a = 5.43 Å, ECUT = 21 (2π/a)²,
113 plane waves; the same model as WE 8.7, seeds18_3.py, si_fcrys/elf11_7). Two calibrations to E_g = 1.160 eV:
- **refit (primary):** V_S(3, 8, 11) = (−0.2343, 0.0558, 0.0676) Ry instead of (−0.21, 0.04, 0.08). Least squares
  on E_g (weight 10), L1c, Γ15c, X4v, Γ1v.
- **scissor (variant):** the book's form factors, with conduction bands shifted rigidly by +0.3364 eV.

| quantity | measured (quoted) | raw CB | scissor | refit |
|---|---|---|---|---|
| E_g (eV), CBM position | 1.17 (4 K); 1.160 used; 0.85 X | 0.824, 0.853 X | 1.160 | 1.160, 0.845 X |
| X1c, L1c (eV) | ≈1.3, 2.04 | 0.95, 1.88 | 1.29, 2.22 | 1.29, **2.04** |
| Γ15c, Γ2′c (eV) | 3.34, 4.15 | 3.42, 3.88 | 3.76, 4.22 | **3.39**, 3.85 (−0.30) |
| X4v, L3′v, Γ1v (eV) | −2.9, −1.2, −12.5 ± 0.6 | −3.00, −1.25, −12.64 | same | −3.01, −1.26, −12.61 |
| m_l, m_t (m_e) | 0.916, 0.191 | 0.872, 0.184 | same | **0.919, 0.199** |
| m_hh[100], m_hh[111] | 0.29, 0.73 | 0.282, 0.703 | same | 0.279, 0.689 |
| m_lh[100], m_lh[111] | 0.20, 0.14 | 0.159, 0.095 | same | 0.157, 0.094 |

Measured values are from standard tables and Kotani–van Schilfgaarde Table I (arXiv:0812.2923 [FT]). The model has no
SOC: Δ_so = 44 meV is ignored, which is why the light-hole masses come out low. The calculation keeps 20 bands
(4 valence and 16 conduction). The highest of them (band 20) has its minimum at 21.8 eV (refit; 21.7 eV scissor),
above E_g + 20.6 eV, so every state up to 20 eV above either band edge is included.
- **Grid.** A Γ-centred 12³ grid (1728 points, 72 irreducible). Bands are diagonalised on the irreducible wedge and
  rotated with the 48 space-group operations {R|t}; 36 of these are non-symmorphic, with t found from the potential.
  E(Rk) = E(k) holds exactly (C1). The fixed G-sphere basis is not translation-invariant, and diagonalising at
  arbitrary representatives gave asymmetries up to 0.14 eV at zone-face ties. The same basis splits the sticking
  bands on the zone faces by ≤ 0.06 eV, which is the residual in C4.
- **Basis convergence.** At ECUT 21 the energies at k on the zone faces are converged to ≤ 0.035 eV (bands 1–5), 0.16 eV
  (band 16) and 0.26 eV (band 20), measured against ECUT 40. The refit was done at ECUT 21. I report this as a
  residual band error.

## 2. Impact-ionization rate W_ii(n,k)
**Direct term.** The golden rule with a static diagonal screened Coulomb interaction w(q) = 4πe²/(ε(q)q²) and the
Kane spin sum. Crystal momentum is conserved on the grid, with every Umklapp in the G set |G|² ≤ 8 (27 vectors around
the shortest p). The rate factorises exactly (ii.py):

Γ_D(n₁k₁) = (4π/ħΩ²) N⁻¹ Σ_p Σ_n₁′ Σ_GG′ A_G A*_G′ S^pair_GG′(p, ω), with
- A_G = w(|p+G|) ρ_n₁′n₁(k₁, −(p+G)), the carrier vertex;
- S^pair_GG′ = N⁻¹ Σ_{k₂vc} ρ_cv(k₂, p+G) ρ*_cv(k₂, p+G′) δ(ω − ε_c(k₂+p) + ε_v(k₂)).

S^pair is computed on the irreducible p and rotated with the non-symmorphic phase e^{i(G_a−G_b)·t}. This is the GW
out-scattering rate of book eq:18.1-ii, including the G ≠ G′ interference, for a model W. The delta function is
represented by 0.05 eV linear binning and a Gaussian with σ = 0.10 eV. Holes are treated with the same formula: the
active valence electron (v′, k₁+p) fills the hole.

**Exchange (exch.py).** Uniformly sampled ordered configurations (k₂, p), with all band triples. The spin sums give

  Γ_full = (2π/ħ) Σ_ord [|M_D|² + |M_E|² − Re M_D M_E*] δ,  Γ_D = (4π/ħ) Σ_ord |M_D|² δ.

The ratio R_x = Γ_full/Γ_D is 1/2 for a contact interaction and 1 when M_E is negligible. Kotani–van Schilfgaarde
(Eq. (5) and the text after it [FT]) state 0.75 as the extreme. Their count omits the identical-particle factor; with
it the extreme is 0.5. Values (pooled over 1 eV, 400 samples × 72 k; the ratio was not computed separately for each
screening variant):

| E above edge (eV) | 2.5 | 3 | 4 | 6 | 10 | 15 |
|---|---|---|---|---|---|---|
| R_x electrons | 1.12 (noisy; variant 0.81) | 0.84 | 0.77 | 0.71 | 0.66 | 0.67 |
| R_x holes | 0.73 | 0.64 | 0.61 | 0.65 | 0.54 | 0.51 |

The sampled direct rate reproduces the factorised one to 0.99 (electrons) and 1.02 (holes), pooled over 3–18 eV and
3–12 eV (C5).

**Screening.** Four models:
- "cap", primary: Cappellini et al., PRB 47, 9892 (1993), static, ε₀ = 11.7; the form is quoted, not read;
- "resta": Resta, PRB 16, 2717 (1977), static; the form is quoted;
- "rpa0": diagonal RPA on the same bands, static. Im ε = (2πv/Ω)S^pair_GG, then Kramers–Kronig, with the f-sum
  remainder placed at 26.8 eV. It gives ε(0.18 Å⁻¹) = 9.6 against 10.5 for cap (C3);
- "rpaw": the same RPA evaluated at the transferred ω (dynamic).

Shell-averaged direct rates Γ_D (s⁻¹) on the refit bands, for E above the band edge; the MC multiplies them by R_x:

| E (eV) | e: cap | resta | rpa0 | rpaw | h: cap | resta | rpaw |
|---|---|---|---|---|---|---|---|
| 2.0 | 1.0e11 | 4.4e10 | 6.9e10 | 6.5e10 | 5.0e10 | 2.2e10 | 3.3e10 |
| 3.0 | 3.1e12 | 1.4e12 | 2.3e12 | 1.9e12 | 4.4e12 | 2.0e12 | 2.7e12 |
| 4.0 | 3.4e13 | 1.6e13 | 2.7e13 | 1.8e13 | 4.5e13 | 2.0e13 | 2.5e13 |
| 5.0 | 1.6e14 | 7.3e13 | 1.2e14 | 7.0e13 | 3.1e14 | 1.5e14 | 1.4e14 |
| 8.0 | 1.6e15 | 7.4e14 | 1.3e15 | 5.9e14 | 2.9e15 | 1.3e15 | 1.2e15 |
| 15.0 | 3.9e15 | 1.8e15 | 2.9e15 | 2.3e15 | — (valence width 12.6 eV) | | |

- **k dependence.** The 10–90 % range of the electron rate is a factor 50 at 2 eV, 3.7 at 3 eV and 1.7 at 5 eV, which
  is the scatter Kotani's Fig. 2 shows.
- **Keldysh/Kane forms.** Fitting P(E − E_th)^a over 1.4–6 eV gives P = 3.4 × 10¹¹ s⁻¹, a = 4.65, E_th = 1.17 eV for
  electrons, and P = 2.4 × 10¹¹ s⁻¹, a = 5.3, E_th = 1.15 eV for holes. The Keldysh exponent 2 and the random-k
  exponent 7/2 are both too low. The often-quoted Si soft-threshold exponent ≈ 4.6 (Cartier et al. 1993, as used in
  full-band MC) is [UNVERIFIED].
- **Kotani GW (arXiv:0812.2923 Fig. 2, read by eye from the figure [FT]).** About 1e11, 5e12, 3e13 and 5e13 s⁻¹ at 2,
  3, 4 and 5 eV. Ours, cap × R_x: 1.1e11, 2.6e12, 2.6e13 and 1.1e14, so they agree within ×2.3. Sano–Yoshii (EPP, as
  plotted by Kotani) are about ×2 above GW.
- **Nielsen et al. 2023 (PRB 108 155203, arXiv:2308.03893 [FT]) is a GaN study and gives no Si rates.** For Si,
  Nielsen–Fischetti 2026 (arXiv:2610.16949 [FT]) find that the shell-averaged ionization rate (GW/BSE loss function)
  crosses the phonon rate at 5.24 eV, with A ≈ 4 for 5–13 eV. Ours crosses at **4.72 eV** (cap; 5.12 resta, 4.81 rpa0,
  5.46 rpaw); for holes, 4.42–4.51 eV. Inverting book eq:18.1-randomk on our shell averages gives A_e(E) = 7.8, 12.5,
  4.1, 1.9, 1.7 and 1.9 eV³ at 2.5, 3, 4, 5, 6 and 10 eV (cap). It is far from constant below 5 eV, and the hole
  values are 3–4× lower above 5 eV.
- **1 % point.** p_ii = 1 % is reached at 2.38 eV for electrons and 2.61 eV for holes (cap), the soft threshold of the
  full band; the random-k model has θ_ii = 1, i.e. 1.16 eV.

## 3. Phonon emission W_ph at T → 0 (phonon.py)
The deformation-potential full-band model uses the Jacoboni–Reggiani Si set (RMP 55, 645 (1983), as quoted by standard
open sources; not read [UNVERIFIED values]):
- electrons: intervalley (meV, 10⁸ eV/cm, Z) g-TA (12, 0.5, 1), g-LA (18.5, 0.8, 1), g-LO (61.2, 11, 1), f-TA
  (19, 0.3, 4), f-LA (47.4, 2, 4), f-TO (59, 2, 4); acoustic Ξ = 9 eV;
- holes: optical (63 meV, 6 × 10⁸ eV/cm), acoustic Ξ = 5 eV;
- ρ = 2.329 g/cm³, u_l = 9.04 × 10⁵ cm/s.

Intervalley and optical modes give W_j = (Z_j/Z_tot)πD_j² g_t(E − ħω_j)/(ρω_j), with g_t the total DOS of the EPM bands
(28³ grid). The final state is random on the shell, which is exact for a q-independent coupling. Acoustic emission at
T = 0 is quasi-elastic, with q ≤ min(2m_d v/ħ, π/a) and the label kept. The total W_ph is 1.2 × 10¹⁴ s⁻¹ (e, 2 eV),
1.7 × 10¹⁴ (e, 3 eV), 1.1 × 10¹⁴ (e, 5 eV), 1.3–1.5 × 10¹⁴ (h, 2–3 eV) and 1.8 × 10¹³ (h, 5 eV, in the valence-DOS
dip). The g-LO mode carries about 75 % of the electron optical emission rate and 78 % of its energy-loss rate, which is close to the book's single 63 meV phonon.
The **finite-T variant** (123 K: emission × (n+1), absorption × n) changes nothing (§6). **DFPT/EPW couplings are
stage 2.**

## 4. Seeds (seeds.py, photon_fine.py)
- **DM seed.** The book's seed machinery (density vertex, folding, Gaussian 0.1 eV), with independent-particle,
  unscreened weights |ρ_cv(k₂, q)|² δ(ω − Δε). The halo average uses the CONVENTIONS §8 rate weight q F_DM² η(v_min),
  SHM with v_E = 250.5 km/s, m_χ = 100 MeV, for F_DM = 1 (heavy) and (αm_e/q)² (light). The q integral has 1500
  sampled grid vectors in 25 radial bins over 0.25–4.0 (2π/a), i.e. 0.57–9.1 keV, with an ECUT 36 basis for the
  vertex. Every seed carrier carries its grid label (k, band), which is what the momentum memory needs.
- **Photon seed.** Vertical pairs weighted by |r_cv|² = |p_cv|²/Δε², polarisation-averaged. The 12³ photon seed has
  sampling noise up to TV 0.09 inside the energy-only cascade, so the photon numbers use a 28³ split with labels drawn
  at random on the shell (memory is negligible, §6). It is defined only above the direct edge (ω ≳ 3.4 eV).
- **q → 0 check.** The DM vertex reduces to the optical vertex to 0.3 % (C10).

| ω (eV) | DM heavy: ⟨E_e⟩, P(x>½), P(x<¼ or >¾) | DM light | photon (12³) | book q₀ seed (5 eV, quoted) |
|---|---|---|---|---|
| 5 | 2.00, 0.56, 0.25 | 1.91, 0.51, 0.26 | 2.07, 0.42, 0.43 | 2.08, 0.574, 0.259 |
| 10 | 5.62, 0.78, 0.44 | 5.27, 0.71, 0.43 | 5.19, 0.81, 0.15 | — |
| 20 | 15.99, 0.97, 0.87 | 15.95, 0.97, 0.87 | 13.30, 0.92, 0.44 | — |

Above about 13 eV the electron takes most of the energy, because the hole is confined to the 12.6 eV valence band and
the valence DOS is small at 4–6 eV. The heavy and light seeds differ by ≤ 0.008 inside the energy-only cascade.

## 5. Cascade (mc.py, run_mc.py)
**Monte Carlo.** Each carrier has an exact continuous energy and a grid label (k, n) within ±0.05 eV. At each step
p_ii = R_xΓ_D(label)/(R_xΓ_D + W_ph(E)). Then:
- a phonon emission puts the carrier on a random state of the new shell (acoustic emission keeps k);
- an ionization draws (p, n₁′) from the carrier's own golden-rule table, rotated from the wedge. The pair (k₂, v, c)
  at that p and ω is drawn with weight Σ_G |w|²|ρ_cv|²; the carrier–pair G interference is dropped in this choice
  only. The three products are rescaled to E − E_g.

The prompt cascade ends when every carrier has E < E_g, and the residual kinetic energy then thermalises. For the
ε_eh/F_eh runs (ω = 25–100 eV), electrons above 19.5 eV ionise with probability 1 and split E − E_g with the
band-DOS density g_e g_e g_h. This rule is sized by the variant "hefree".
- **Energy identity.** ω = N E_g + E_ph + E_res is asserted per event to 10⁻⁹ eV in every run.
- **Engine check.** In book mode the MC reproduces casc18_3's generating function to TV ≤ 0.0023 (C9).
- **Statistics.** 2 × 10⁴ events per ω and seed; ε_eh and F_eh use 4 × 10⁴ one-sided events at 25, 50 and 100 eV.

**P(N|ω), primary (refit, cap, JR, R_x); DM heavy seed.** Entries are P(1)…P(6); light and photon are given where they
differ.

| ω | P(1) | P(2) | P(3) | P(4) | P(5) | P(6) | ⟨N⟩ [band] | photon (28³ split) ⟨N⟩, P(≥2) | book DM ⟨N⟩ |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 1.000 | 0 | | | | | 1.000 | — (below the direct edge) | 1.001 |
| 4 | 0.992 | 0.008 | | | | | 1.008 [1.005, 1.016] | — | 1.037 |
| 4.5 | 0.958 | 0.042 | | | | | 1.042 [1.021, 1.067] | 1.032, 0.032 | 1.119 |
| 5 | 0.889 | 0.111 | | | | | 1.111 [1.056, 1.155] | 1.109, 0.109 | 1.169 |
| 6 | 0.624 | 0.376 | 0.001 | | | | 1.38 [1.24, 1.47] | 1.33, 0.327 | 1.44 |
| 7 | 0.313 | 0.674 | 0.012 | | | | 1.70 [1.53, 1.81] | 1.69 | 1.79 |
| 8 | 0.066 | 0.843 | 0.091 | | | | 2.03 [1.86, 2.13] | 2.03 | 2.13 |
| 10 | 0 | 0.613 | 0.377 | 0.010 | | | 2.40 [2.25, 2.50] | 2.48 | 2.63 |
| 12 | | 0.236 | 0.643 | 0.120 | 0.001 | | 2.89 [2.67, 3.05] | 2.95 | 3.19 |
| 15 | | 0.007 | 0.412 | 0.503 | 0.077 | 0.001 | 3.65 [3.38, 3.84] | 3.67 | 3.99 |
| 20 | | | 0.015 | 0.316 | 0.501 | 0.159 | 4.83 [4.47, 5.08] | 4.81 | 5.32 |

Full curves (0.25 eV grid; heavy, light, photon; all variants) are in code/FBC/data/summary.json, derived.json and
mc_*.npz. The DM light seed differs from the heavy one by TV ≤ 0.014 at every ω.

**ε_eh, F_eh and the energy partition** (one-sided seeds; slopes over 50→100 eV, cross-checked 25→50: 4.113 eV):

| | full band (primary) | book (18.2/18.4) |
|---|---|---|
| ε_eh | 4.130 ± 0.003 (MC) [3.92, 4.47] eV | 3.749 (fitted) |
| F_eh | 0.114 ± 0.002 [0.110, 0.114] | 0.114 (measured 0.119 ± 0.002) |
| b_N | 0.43 [0.36, 0.43] | 0.35 |
| partition at 100 eV: pairs / phonons above threshold / residual kinetic | **28.6 % / 27.5 % / 43.9 %** | 30.9 / 24.8 / 44.3 % |
| per pair: E_g + E_ph + E_res | 1.16 + 1.12 + 1.78 eV | 1.160 + 0.928 + 1.661 |
| 𝒱_< + 𝒱_> + 2𝒱_<> (at 100 eV, not slopes) | 0.106 + 0.345 − 0.339 = 0.111 | 0.092 + 0.291 − 0.269 = 0.114 |

At 10 and 20 eV the DM seed partitions as 27.8/27.5/44.7 % and 28.0/27.9/44.0 %.

## 6. Comparisons
**Against the book's energy-only cascade (casc18_3, A_AB = 5.674, E_g = 1.160), R–K and the step model.**
TV(full-band DM heavy, model):

| ω | book DM seed | R–K α=1 | R–K α=∞ | step | P(≥2): full / book / α=1 / α=∞ / step |
|---|---|---|---|---|---|
| 4.5 | 0.076 | 0.117 | 0.039 | 0.042 | 0.042 / 0.119 / — / — / 0 |
| 5 | 0.059 | 0.207 | 0.091 | 0.889 | **0.111 / 0.169 / 0.317 / 0.019 / 1** |
| 6 | 0.059 | 0.266 | 0.235 | 0.624 | 0.376 / 0.435 |
| 8 | 0.089 | 0.114 | 0.357 | 0.157 | 0.934 / 0.945 |
| 10 | 0.200 | 0.253 | 0.568 | 0.623 | |
| 15 | 0.192 | 0.204 | 0.150 | 0.497 | |
| 20 | 0.230 | 0.238 | 0.216 | 0.841 | |

**Matched comparison.** The as-is distances above 9 eV come mostly from the 10 % gap in ε_eh. I therefore
recalibrated the book cascade to the full-band ε_eh: A_AB = 12.31 eV³ gives 4.130 eV (slope over 20–40 E_g; the same
estimator returns 3.747 at 5.674). This leaves the structural part (matched.py):

| | 5 eV | 6 | 8 | 10 | 12 | 15 | 20 eV | max (4.4–21) |
|---|---|---|---|---|---|---|---|---|
| energy-only, book DM seed | 0.020 | 0.115 | 0.125 | 0.005 | 0.051 | 0.035 | 0.020 | 0.161 (6.75) |
| energy-only, computed split | 0.019 | 0.084 | 0.113 | 0.015 | 0.027 | 0.039 | 0.020 | 0.141 (7.5) |
| R–K α=1 | 0.072 | 0.094 | 0.054 | 0.059 | 0.022 | 0.016 | 0.022 | 0.102 |
| R–K α=∞ | 0.102 | 0.306 | 0.396 | 0.343 | 0.238 | 0.089 | 0.049 | 0.450 |
| step (ε = 4.13) | 0.111 | 0.624 | 0.157 | 0.623 | 0.357 | 0.497 | 0.498 | 0.780 |

The matched energy-only cascade puts P(≥2) at 5 eV at 0.090 (book seed) or 0.092 (computed split), against 0.111 for
the full band. The residual 0.11–0.16 at 6–8 eV comes from the shape of the rate ratio. The full-band p_ii is softer
just above threshold (1 % at 2.4 eV, against 1.16 eV in random-k) and steeper above it: A(E) falls from 12.5 to
1.7 eV³ between 3 and 6 eV. A single constant cannot reproduce both.

**Other items in §6 of the brief:**
- **α_RK spread.** The book cascade's max TV(α=1, α=∞) over 4.4–13 eV is 0.498. The computed splits (heavy, light;
  refit, scissor) span ≤ 0.029, which removes **94 % [median over ω 96 %]**. TV(computed heavy split, book q₀ seed) in
  the same cascade is ≤ 0.035 (at 17 eV); at 5/10/15 eV it is 0.003/0.019/0.012.
- **Valley/momentum memory.** TV(full, energy-only reduction of the same kernels) is ≤ 0.015 (heavy) and ≤ 0.012
  (photon) at every ω; independent MC repetitions differ by ≤ 0.013. ε_eh changes by 4.130 → 4.126 and F_eh by 0.114
  → 0.112. The fresh, k-labelled carriers make 0.94 of the 1.40 extra pairs at 10 eV (nfirst), yet the outcome does
  not depend on their k. The likely reason is that the seed's states are spread over the shell much as a random draw
  would be, with W_ii spread ≤ ×4 above 3 eV. **Bound: ≤ 0.015 TV, not resolved.**
- **mK phonon competition.** Without phonon emission, P(≥2) is 0.18/0.52/0.89/0.99/1.00 at 2.5/3/3.5/4/4.5 eV; with
  emission it is 0.000/0.000/0.002/0.008/0.042. The mean at 5 eV drops from 2.67 to 1.11. Phonon absorption at 123 K
  (fixed E_g) changes P(N) by TV ≤ 0.016, at noise level; mK and 123 K differ only through E_g(T) (1.160 → 1.17).
- **Photon vs DM.** In the full band (28³ photon split, heavy DM seed) the max TV is 0.078 at 10 eV (0.049 at 6,
  0.020 at 8, 0.017 at 15, 0.013 at 20 eV). In the energy-only cascade with the same splits the max is 0.053 at 10 eV;
  the book quotes ≤ 0.062. The P(≥2) ratio (photon/DM) at 5 eV is 0.99 here and 1.12 in the book.

## 7. Uncertainty bands
Each band is the envelope over the variants, plus MC error. The variants are: screening (resta, rpa0, rpaw); phonon
couplings D² × 0.6 and × 1.6 (Ξ scaled with √); band calibration (scissor); exchange (R_x = 1; threshold R_x = 0.81);
high-energy rule (free-particle DOS); repetition (independent MC). I chose the ×0.6–1.6 range on D² to cover the spread
between published deformation-potential sets and DFPT full-band rates. I have not read those sources (see the
[UNVERIFIED] tags above).

| headline | primary | screening | phonon D² | bands | exchange | high-E rule | MC | envelope |
|---|---|---|---|---|---|---|---|---|
| ε_eh (eV) | 4.130 | 4.25–4.47 | 3.92–4.32 | 4.14 | 4.03–4.17 | 4.10 | ±0.003 | **3.92–4.47** |
| F_eh | 0.114 | 0.110–0.112 | 0.110–0.114 | 0.114 | 0.111–0.113 | 0.110 | ±0.002 | **0.110–0.114** |
| P(≥2), 5 eV | 0.111 | 0.056–0.082 | 0.074–0.155 | 0.109 | 0.094–0.121 | — | ±0.002 | **0.056–0.155** |
| step overcount, 5 eV | 9.0 | 12.3–17.7 | 6.5–13.6 | 9.2 | 8.3–10.7 | — | ±0.2 | **6.5–17.7** |
| ⟨N⟩ 10 eV | 2.40 | 2.25–2.34 | 2.31–2.50 | 2.42 | 2.37–2.44 | — | ±0.004 | **2.25–2.50** |
| max TV vs book (as-is) | 0.26 | 0.33–0.45 | 0.13–0.36 | 0.27 | 0.21–0.28 | — | ±0.01 | **0.13–0.45** |
| max TV vs step | 0.89 | 0.92–0.94 | 0.85–0.93 | 0.89 | 0.88–0.91 | — | — | **0.85–0.94** |
| memory TV | ≤ 0.015 | — | — | — | — | — | 0.013 | ≤ 0.015 |
| photon–DM max TV | 0.078 | not run | not run | — | — | — | ±0.013 | 0.078 ± 0.013 (+ ≤ 0.02 seed grid) |
| α_RK spread removed | 94 % | — | — | incl. | — | — | — | ≥ 94 % |

**Convergence** (checks C7, C11):
- 12³ vs 10³ shell rates: DOS-weighted mean |ln ratio| is 0.027 (e) and 0.051 (h). The worst windows are e ×1.12
  and h ×1.49, both at 4–5 eV, where the valence DOS dips.
- G shells 11 vs 8 (n = 8): ≤ 4 %.
- MC: independent runs agree to TV ≤ 0.013.

The P(≥2) band at 5 eV is dominated by screening and phonon coupling, and ε_eh by screening. Neither has a fitted
constant, so the measured ε_eh = 3.749 eV is reproduced within the band only at its lower edge (D² × 0.6 gives 3.92).

**What stage 2 must supply:**
1. GW-level rates: quasiparticle bands instead of the EPM; the full ε⁻¹_GG′(q, ω) with local fields instead of the
   diagonal static W; the z_qp factor. Screening alone moves ε_eh by +0.12 to +0.34 eV.
2. DFPT/EPW electron–phonon couplings g_mnν(k, Q), which would remove the ×0.6–1.6 D² range and the random-k phonon
   final state. The memory bound of §6 holds only within the deformation-potential model.
3. Excitonic final states for the seeds (BSE) and exciton formation at the end of the cascade.
4. The carrier–pair G interference in the choice of the pair; tetrahedron integration or 16³+ grids at 4–6 eV for
   holes; R_x near threshold, which is noisy below 3 eV.
5. All-electron vertices for the DM seed at |q| > 9 keV (the pseudo wave functions cut the large-q tail).
6. Ge and GaAs with SOC: the GaAs Fröhlich term in W and the subtraction from g^S (book 18.1).

**CPU.** About 3 CPU-h, including about 0.6 CPU-h lost to oversubscribed BLAS threads in early runs. Per item:
ii.py 12³ ≈ 6 min/run, exch ≈ 5, seeds ≈ 10, the MC ≈ 3–6 min per configuration.

## Literature
- [FT] arXiv:0812.2923 (Kotani–van Schilfgaarde), 2308.03893 (Nielsen et al., GaN), 2610.16949 (Nielsen–Fischetti),
  2004.10709 (Ramanathan–Kurinsky; definitions only, cross-checked against book 18.3).
- [UNVERIFIED]/quoted values: the Jacoboni–Reggiani couplings, the Cappellini and Resta screening forms, the measured
  band energies and masses (via standard tables and 0812.2923 Table I), and the Cartier/Fischetti–Laux exponent.
- PDFs have been deleted from literature/papers-FBC/; the html and txt copies are kept.

## Symbols introduced/used
- Used, NOTATION v4: ε_eh, F_eh, b_N, B_h (12.6 eV in these bands; book 12 eV), θ_ii, P_casc / P(N_eh|q,ω) written
  P(N|ω), Γ_ii, Γ_ph, ρ_mn(k,q) (CONVENTIONS §4), v_C, η(v_min), F_DM, 𝒱_<, 𝒱_>, 𝒱_<> (2𝒞_<> in NOTATION §EF),
  A_AB (= 𝒜_ph of NOTATION §EF; book symbol kept), α_RK (book 18.3).
- New:
  - **W_ii(n,k)**: the full-band ionization rate, R_x Γ_D.
  - **Γ_D**: the spin-summed direct term.
  - **R_x**: the Kane exchange factor Γ_full/Γ_D.
  - **S^pair_GG′(p,ω)**: the pair spectral matrix. It is not S_ab: it carries no coupling rows and is −Im χ⁰ up to
    2π/Ω.
  - **W_ph(n,k) → W_j(E)**: the per-mode emission rates.
  - **d_TV**: the total-variation distance (book 18.3).
  - **A(E)**: the inverted random-k ratio of the full-band kernels.
  - **nfirst**: ionizations made by first-generation (k-labelled) carriers.

## Interface flags (what Ch18 should change)
- IF-FBC-1 (18.1 key result, "exchange ... absent"): give its size. The Kane exchange factor R_x is 0.66–0.84 for
  electrons and 0.51–0.65 for holes above 3 eV. It is not "at most 0.75" (Kotani): with the identical-particle count
  the floor is 0.5. Dropping it lowers ε_eh by 0.10 eV.
- IF-FBC-2 (18.1-reductions, momentum memory): the first-generation memory computed with deformation-potential phonons
  is ≤ 0.015 in TV (not resolved). The energy-only reduction is justified at that level in Si, pending DFPT couplings.
  Replace "the error ... is an estimate" by this bound, with the caveat.
- IF-FBC-3 (18.3, the α_RK spread up to 0.39): a computed full-band, halo-averaged DM split removes ≥ 94 % of it. The
  book's EPM q₀ seed is within 0.035 of it, so the book's seed choice stands; the seed question is closed at the
  0.03 level.
- IF-FBC-4 (WE 18.3, "5.9 times"): with full-band kernels the step overcount at 5 eV is 9.0 [6.5, 17.7], and
  P(N ≥ 2, 5 eV) = 0.111 [0.056, 0.155] against 0.170. The book's 5.9 is a model value; add the band.
- IF-FBC-5 (18.3, photon vs DM ≤ 0.062): the full-band max is 0.078 ± 0.013 (at 10 eV). The P(≥2) ratio at 5 eV is
  0.99, not 1.12. The 12 % photon excess of WE 18.3 is not robust.
- IF-FBC-6 (18.4 "first-principles cascade would replace every model number"): stage 1 gives ε_eh = 4.13 [3.92, 4.47]
  eV and F_eh = 0.114 [0.110, 0.114] with literature couplings and no fit. F_eh is insensitive to every input and
  stays below 0.119, which supports the book's reading that the 2.5σ gap is structural. The equivalent A_AB of the
  full-band kernels is 12.3 eV³, not 5.674. The constant hides a soft threshold (p_ii = 1 % at 2.4 eV) and a steep
  rise; A(E) falls from 12.5 to 1.7 eV³ over 3–6 eV.
- IF-FBC-7 (18.1 phonon kernel at detector temperature): the mK (emission-only) cascade and the 123 K cascade agree to
  TV ≤ 0.016 at fixed E_g. Only E_g(T) matters.
- IF-FBC-8 (casc18_3.py, numerics): the roots-of-unity extraction with NZ = 32 aliases above about 60 eV. The slope
  over 50–100 eV gives F = 0.38 and ε_eh = 3.796, against 0.114 and 3.749 over 20–40 E_g. The book's use (≤ 51 eV) is
  safe; flag it for any reuse.
- IF-FBC-9 (sources): the brief's "Nielsen et al. 2023 PRB 108 155203" is a GaN study. Si full-band rates are in
  Nielsen–Fischetti arXiv:2610.16949 (crossing at 5.24 eV, A ≈ 4).

## Proposed LIMITS rows
| # | Formula (source) | Recovered as | Validity (this return) | Leading correction | Status |
|---|---|---|---|---|---|
| L-FBC1 | Energy-only random-k cascade, one constant A_AB (book 18.1–18.3; R–K 2004.10709 Eq. (8)) | iso-energy reduction of the full-band kernels with A(E) → const | after recalibration (A_AB = 12.3 eV³): TV ≤ 0.05 for ω ≥ 10 eV and ω ≤ 5 eV; 0.11–0.16 at 6–8 eV | energy shape of the rate ratio near threshold (soft onset at 2.4 eV, A(E) 12.5 → 1.7 eV³ over 3–6 eV) | [CALC], stage 1 |
| L-FBC2 | Step model 1 + ⌊(ω − E_g)/ε_eh⌋ (1509.01598 Eq. (5.1), book eq:18.3-step) | deterministic-price limit | ω < 4.4 eV only; TV 0.85–0.94 at 5 eV; overcount of P(≥2) at 5 eV 9.0 [6.5, 17.7] | full P(N), seed and phonon competition | [CALC] |
| L-FBC3 | R–K Beta split, α_RK = 1, ∞ (2004.10709 Eq. (7)) | seed-replacement limit | α = 1: TV ≤ 0.10 at matched ε (0.28 as-is); α = ∞ fails (0.45) for 5–14 eV | computed split (≥ 94 % of the α spread removed) | [CALC] |
| L-FBC4 | Kane/Keldysh threshold law W ∝ (E − E_th)^a | fit to the full-band shell average | a = 4.65 (e), 5.3 (h) over 1.4–6 eV; Keldysh a = 2 and random-k 7/2 fail | k scatter ×50 at 2 eV, ×1.7 at 5 eV | [CALC] |
| L-FBC5 | Energy-only reduction (book eq:18.1-isoenergy) | full-band MC vs shell-randomised MC | TV ≤ 0.015 for 2–20 eV (deformation-potential phonons) | DFPT couplings and anisotropic g (stage 2) | [CALC], bound |
