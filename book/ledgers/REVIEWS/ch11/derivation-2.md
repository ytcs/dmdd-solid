# Ch11 derivation review, part 2 (s11-5 … s11-9)
Isolated derivation check. My scripts are in the session scratchpad (`rv/s1*.py`–`s5.py`). They are independent re-implementations from the cached data: the PBE DOS in `figscripts/ch05/fig5_2_data.npz`, `lat11_7.npz`, and the logs `sap11_7.log` and `we11_8.log` for the quantities that need EPM or QE runs. No QE runs were made. Halo: App. A.8 (v0 = 238, vesc = 544, vE = 250.5 km/s, ρχ = 0.3). Sources were read from the arXiv HTML. No PDFs were kept; the converted text is in the scratchpad.
Verdicts: CHECKED / WRONG / GAP. A correction is given only where one is needed.

## Summary of non-CHECKED items
1. **WRONG – s11-6 l.99 (lim:11.6a box sentence), l.102.** The ratio g₂₉/g_ph at the optical-band edge peaks at **2.05 at 57.3 meV**, not 1.78 at 57.4. Between 60 and 63 meV its minimum is **0.59, at 60.7 meV**, not 0.72. My grid is the raw 0.25 cm⁻¹ DOS. The writer's own `limit11_6a.log` gives "max |D_29/D−1| below 60 meV: 1.0402", i.e. 2.04, which confirms this. The printed 1.78 and 0.72 look like point samples (0.7243 at 62.0 meV in the log). Fix: "rises to about 2 at the edge, 57.3 meV … falls to 0.6 near 61 meV"; in the box, "errs by up to a factor of 2". Alternatively, state the smoothing used and requote.
2. **GAP – s11-5 l.31, WE 11.mkpeak l.102, s11-9 table.** The range "−0.14 to +0.08 %" for the kinetic energy pairs (λ₃, λ₄) = (0.01, 2.5e-4) and (0.006, 2e-4). The source gives only the ranges λ₃ = 6e-3 to 1e-2 and λ₄ = (2–3)e-4, unpaired (2309.10839 Sect. IV). Over the corners of those ranges, the exact diagonalization and Eq. (65) give **−0.20 % to +0.20 %**: (0.01, 2e-4) → 0.99802 and (0.006, 3e-4) → 1.00203. State the pairing, or quote ±0.2 %. Then σ_ω moves ≤ 0.09 meV. No conclusion changes: still < 10⁻³, and the cumulative changes by ≤ 2.5e-4.
3. **GAP – s11-5 l.18 ("The first three hold at any temperature").** All five moments hold at any T, with thermal averages, for a time-reversal-invariant H. Use a real eigenbasis and A_i = H − E_i. Then ⟨i|δD A_i² δD|i⟩ = ‖[H,δD]|i⟩‖² and the mixed terms cancel as at T = 0. Harmonic check: c₄ = E_R ω₀³ coth(ω₀/2T). Fix: "They hold at any temperature with thermal averages", or justify restricting the claim to three.
4. **GAP – s11-5 l.61 ("the exact solution gives 18λ₃²k⁴").** The number is correct: my exact value is 18.06 at λ₃ = 1e-4, k = 3e-3. The sentence before it suggests a two-kick, one-vertex amplitude. That amplitude alone gives **24λ₃²k⁴** (sympy: −½k²⟨3̃|x²|0̃⟩ = −2√6 λ₃k²). The remaining **−6** comes from interference between the O(λ₃²k) one-kick amplitude and the harmonic three-kick amplitude k³/√6. Add half a sentence so that a reader who redoes the count does not get 24.
5. **WRONG (minor) – s11-7 l.101.** For a vertical c axis at 45°N, P₂ sweeps from 0.997 to **−0.497**, not −0.495.
6. **GAP – s11-7 l.110, sapphire above 1 meV.** The 0.6 % along-vs-across difference is the *one-phonon* rate (fig11_7.log: 1.0039/0.9981). A_day = 0.48 % is for *all phonons* above 1 meV (sap11_7.log `w1_all`: R(c)/R(⊥) = 1.0097, A = 0.0048). One phonon alone gives A = 0.29 %. Fix: "differ by 1.0 % (0.6 % for one phonon)", or quote A_day = 0.29 % for one phonon.
7. **WRONG (minor) – s11-7 l.79.** "at q = 1.79 q_BZ, at the shell |G₁₁₁| = 3.95 keV" conflates two values: G₁₁₁ = 3.954 keV is **1.76** q_BZ (q_BZ = 2.248 keV). The minimum S₄/S₀ = −0.356 is at 1.785 q_BZ = 4.01 keV (lat11_7.npz). Fix: "just beyond the shell |G₁₁₁| = 3.95 keV, at q = 1.79 q_BZ". Separately, S₆/S₀ of the two-phonon weight reaches 0.103, so "at most 0.1" should read "about 0.1". Beyond 5 q_BZ the one-phonon |S₄|max = 0.18 and |S₆|max = 0.37: "0.2 to 0.4" holds only loosely.
8. **WRONG (minor) – s11-7 WE 11.daily l.130.** For [001] along the Earth's axis, the lattice amplitude is **0.06 %** (we11_8.log: Si_lat 0.0006), not 0.05 %.
9. **WRONG (minor) – s11-9 l.89.** At 80 keV the Markov–Krein band for the weight above 100 meV is **[0.19, 0.94]**, not 0.95 (my value is 0.944; the harmonic value 0.578 checks).
10. **Notation/convention drift – s11-8 l.116, t_coh.** NOTATION (row t_coh) and Sect. 8.2 give the estimate 1/(m_φv₀²); s11-8 defines t_coh = 2π/(m_φv₀²) = 6.6 ms at 1 μeV. That is a **2π drift**: with 1/(m v₀²) the value is 1.05 ms. The editor must pick one. Either 8.2's "1 ns at 1 eV" (which is 1/(mv₀²)) changes to 6.6 ns, or 11.8 drops the 2π.
11. **Notation GAP – NOTATION.md.** These first uses in s11-5…8 have no NOTATION row: Υ_ℓ (halo multipole); h_mod; f_sh; δ^M_i; 𝔟_i, 𝔟̄, σ_𝔟; h_iso; r_L; λ₃, λ₄; q_×; A_day; 𝔔, 𝔔_p, 𝔔_DM, 𝔔_eff; 𝒢^φ_κ; x_{κi}; g_i(ω); M_n, L₀, r_n, U_n; ℓ_lat, δ_E, h_E. **Clash:** Υ_ℓ (11.7 halo multipole) against **Υ_m** (8.6 zero-phonon-pair vertex correction, NOTATION l.742). Rename one, or add a clash entry. Check against `ledgers/check_notation.py`.
12. **GAP – s11-5 l.74.** The claim that Campbell-Deem et al. find the anharmonic term "larger than the harmonic term … by orders of magnitude in GaAs at 10 meV [Fig. 2]" cannot be checked from their text. Their text says only that the on-shell resonance dominates where it is accessible, and that both scale as q⁴ in the inset. The claim rests on reading the figure. Say "near the on-shell LA resonance", or read the figure at the citation audit.

## 11.5 Anharmonic and quantum-crystal corrections
- l.7 kick algebra, Eq. 11.5-moments: **CHECKED**. μ̄₂ = (q/M)²⟨p²⟩ = 4E_R E_kin. μ̄₃ = ½(q/M)²⟨[p,[H,p]]⟩ = (q²/2M²)⟨∂²V⟩. For μ̄₄: ⟨δD A²δD⟩ = (q/M)²⟨(∂V)²⟩, and ⟨p(p∂V+∂Vp)⟩ is real for a real ψ, so the mixed terms cancel. Harmonic check: Mω₀³/2 → E_Rω₀³ and the second term is 3μ̄₂². The temperature claim is item 3.
- l.22 three linear constraints and the evenness/odd-in-q selection rule (n_A = 2): **CHECKED**.
- Eq. 11.5-toy, "cubic energy at ℓ₀ is 4λ₃ × harmonic": **CHECKED**. Harmonic energy at ℓ₀ is ω₀/4, cubic is λ₃ω₀. The potential matches 2309.10839 Eq. (26)/(67), and Eq. (65) checks.
- Kinetic energy 1 − 44λ₃² + 12λ₄ against exact diagonalization: **CHECKED** (0.998631 vs 0.9986; 1.000828 vs 1.000816). The ranges are item 2.
- Eq. 11.5-anh: **CHECKED**. S = (1/Ω)Σc²(1/N)Σ|q·e|²/(2Mω_Q)·4ω_Q²γ/(ω²−ω_Q²)², which equals the printed (2π/Ω)(1/πM)ω_Qγ/(…)². The free limit −2ImD → 2πδ(ω−ω_Q) checks; FWHM γ at the pole checks. Campbell-Deem Eq. (13) has the two time orderings: **CHECKED**.
- First-order states and Eq. 11.5-two: **CHECKED** by sympy. |0̃⟩ = |0⟩ − λ₃(3|1⟩ + √(2/3)|3⟩); ⟨1|x³|2⟩ = 6√2; ⟨2̃|x|0̃⟩ = 2√2λ₃; weight 8λ₃²k² + k⁴/2; ratio 16λ₃²/k² (numerically 8.0015 at λ₃ = 2.5e-4).
- Numbers: **CHECKED**. (2Mω₀)^½ = 39.88 keV; q_× = 1.60 keV; at q_BZ, +50 % (λ₃ = 0.01) and +18 % (0.006). Three-phonon crossover √108 λ₃ → 4.14 keV. Exact ratios at q_BZ for n = 2, 3, 4: 1.50, 4.49, 27.1. Within 10 % above 5.1, 11.6 and 19.8 keV. The 3-phonon coefficient is item 4.
- Lin et al. claims (two orders of magnitude at a few MeV; agreement above 10 MeV; λ₃ = 6e-3–1e-2, λ₄ = (2–3)e-4; fits along (111) and (1,−2,1); ω₀ = 1/⟨ω⁻¹⟩): **CHECKED** against 2309.10839 Sect. IV and Conclusions. ⟨ω⁻¹⟩⁻¹ = 30.42 meV from the DOS.
- Markov–Krein, Gaussian Christoffel 2/(3+ξ⁴): **CHECKED** (Hermite orthonormal sum (3+ξ⁴)/2). Tail numerator standardized: 3.333 − 1 − 0.553² = 2.028: **CHECKED**.
- WE 11.mkpeak, all numbers: **CHECKED** by my own canonical-representation solver and FFT spectrum. σ = 88.4 meV; skew 0.553; kurtosis 3.333; nodes 59.8/191.1/371.3 meV; weights 0.191/0.670/0.139; band [0.191, 0.861]; F(E_R) = 0.537; ±σ bin [0.066, 0.996], true 0.683; ±2σ bin [0.777, 1], true 0.961; above 456.4 meV 5.58e-3 against band 3.35e-2; 10 % boundary ξ = −1.85 (27.6 meV vs "1.84, 28 meV"). At 50 keV the band is [0.209, 0.887]: **CHECKED**.
- Helium (cell-model table in limit11_5b.log; I did not re-solve it): internal consistency **CHECKED**. Quoted against Cazorla Table I: r_L = 0.12 at 2.0 GPa and 0.10 from 14.2 GPa: **CHECKED**. Aziz well 10.8 K and r_m = 2.967 Å: **CHECKED**. The "about a quarter" vs 0.23 in the model is as in editor note 11.5. (M_Si/M_H)^¼ = 2.30: **CHECKED**.

## 11.6 Nuclear spins and isotopes
- Eq. 11.6-random: **CHECKED** (average over disorder; |e|² gives g_I; 1/3 from isotropy → g/(6Mω)). Spin one-phonon term (q²/2Mω)g/3: **CHECKED**.
- Mass cancellation Σ√M e = 0 for any mass configuration: **CHECKED**.
- ALP vertex iω(g_ai m_φ/m_N)J, variance ω²(…)²J(J+1): **CHECKED**. Eq. 11.6-alp from Γ = S/2ω and ρ/(m ρ_T): **CHECKED**. It equals Bloch et al. Eq. (31) with g_pλ_j = g_ai/2m_N, D_j = g_i/3 and ξ_j as stated: **CHECKED** (2π·¼·⅓ = π/6). The footnote 5 isotope assumption: **CHECKED**.
- 29Si spin weight 3.42e-3; ⟨S_n⟩/⟨S_p⟩ ≈ 9.8 ("ten"); T(10 mK) = 0.86 μeV; p²⟨u²⟩ ~ 1–2e-18: **CHECKED**.
- Eq. 11.6-lifshitz (Dyson, g_i/g = (1−δ)ImG_i/ImG_h, ImG_h = πg/6M̄ω), Eq. 11.6-first h_iso = −1 − 2M̄ω²ReG_h, and the signs of the peak argument: **CHECKED** analytically.
- M̄ = 28.0855 u; δ = +0.0039, −0.0317, −0.0672; g_md = 2.007e-4; δ_c = 0.219 (M̄ω²ReG = −4.564 just above the band); 10 % boundary 55.04 meV = 0.865 ω_max; range below it 0.965–1.100; first order to 0.44 %; band-integral conservation: **CHECKED**. The edge values are item 1.
- Pair term (G² = ∂G/∂(M̄ω²)); Rayleigh width (π/2)g_md ω² g/3 = 2.51e-4 ω at 50 meV (equal to Tamura's (π/6)g ω² D): **CHECKED**.
- B−L split, ζ = g/e, Eq. 11.6-GEM: **CHECKED** against 11.8's Γ = ζ² m L.
- 𝔟_i, 𝔟̄ = 0.50235, σ_𝔟²/𝔟̄² = 1.879e-4, ⟨δ⟩_𝔟 = −0.0536; baryon-number variance 9.14e-11, ratio 2.06e6: **CHECKED**.
- Eq. 11.6-Giso, both lines (Γ = S/2ω, the fixed polarization on a cubic site): **CHECKED**.
- Eq. 11.6-Tbound, pair weight 1+n₁+n₂ and difference weight n₂−n₁: **CHECKED**. Monotone in T because x e^x/(e^x−1)² decreases.
- WE 11.iso: **CHECKED** throughout. Ω_at = 2.606e-9 eV⁻³; M̄σ² = 1.430e-12 eV⁻¹; g/3 = 15.92 eV⁻¹; Γ_iso host 1.372e-2, exact 1.481e-2 (+7.99 %); h(50) = −1.553; ε₂ = 7.42e-4; L = 5.42e-6; Γ_EM = 2.957e-6; ratio 5.01e3 (host 4.64e3). The ≈10 % digitization statement is present at the point of use, so editor ruling R3 is met. The 76 meV ratio of 17.3 and the figure range 2e2–1.4e4 match iso11/fig11_6 logs, but I did not recompute them from the α table.

## 11.7 Anisotropy and daily modulation
- Velocity integral, Radon transform of the truncated Maxwellian, Legendre series, addition theorem → Eq. 11.7-rate prefactor q dq/4π²: **CHECKED**. Υ₀ = η: **CHECKED** numerically (1.5297e-3 vs 1.5291e-3 at 300 km/s).
- Halo multipoles: **CHECKED** with my code. Υ₂/Υ₀ = 0.127/0.375/0.510/0.702; Υ₄/Υ₀ = −0.016/0.017/0.068/0.268; Υ₂/Υ₀(0) = −0.132; Υ₁/Υ₀(300) = −0.541; zeros at 196, 138 and 435 km/s; Gaussian width v₀/v_E = 0.950.
- Odd-part interference 2Im[(q·d)qqQ*] and both selection arguments: **CHECKED**. "Both broken" agrees with the editor note.
- Y^c₄: values 0.646 [100] and −0.430 [111]; path range −0.394 to 0.640 with the maximum at h = 0; factor √4π·0.517 = 1.831; polar mounting smaller by 6.1×: **CHECKED**. Item 5 for P₂.
- Eq. 11.7-dw (decomposition q·B·q = q²[b̄ + ⅔ΔbP₂]): **CHECKED**.
- A_day values: **CHECKED** against the logs (I did not rerun EPM or the lattice): 0.9/0.58/0.7/0.29 %; mass scan 0.77/0.13/0.18/0.04/0.01 %; best orientations 0.93/0.60. Sapphire 0.48/3.5/6.4 and 1.2/0.6 at 30 MeV; SiC 0.08/0.61/3.5 (sap11_7.log). My P₂-sweep recomputation from the R(c)/R(⊥) ratios reproduces 3.53 % and 6.37 %. Items 6 and 8.
- One-phonon S₄/S₀ = 0.028 (elastic), 0.025 (PBE, q ≤ 0.3 q_BZ), |S₆/S₀| = 0.026 at 0.7 q_BZ, S₆/S₀ = −0.485 at 2.90 q_BZ: **CHECKED** (lat11_7.npz/log). Item 7.
- q_BZ(sapphire) = 1.75 keV; edge 53 keV at 10 MeV; q_max(2 MeV) = 10.60 keV = 2.84 q₀; ω_max = 7.02 eV: **CHECKED**.
- Sources: Stratman halo (220/500/240) and 11 % in sapphire: **CHECKED**. Al-Adulrazzaq attribute the 5 eV sine to the dipole (Sect. III B text), so the book's correction is valid: **CHECKED**.

## 11.8 Absorption
- Eq. 11.8-Gamma (Γ = S/2ω, one-phonon normalization): **CHECKED**.
- Sherman–Morrison step, with b = (v_C q²/Ωε∞)^½ p: gives v_C x_a x_b/(ε∞ − v_C x): **CHECKED**.
- Eq. 11.8-shift: **CHECKED** term by term (sympy-style expansion by hand). The leftover real constant is v_Cχχ(ε∞ − v_Cx)/(ε∞ε) = v_Cχχ/ε∞.
- Electron shift: v_Cχ_eZ = ε∞ − 1, so the vertex is Z − Z*/ε∞ (Eq. 11.8-G). The charge and nucleon limits: **CHECKED**.
- Two-site collapse p μ^½ d; Eq. 11.8-Rscalar (division by the line weight πe²Z*²/2Ωμε∞²ω_L); photon-like bracket equal to 1: **CHECKED**. 240ζ and 395ζ: **CHECKED** (0.3028/1.264e-3 and 0.3028/7.672e-4). This matches Mitridate et al. Eqs. (42)–(43): g ≈ 4e-14 per κ = 1e-16.
- WE 11.gaas, all numbers: **CHECKED**. 0.444617/0.440460; 4.157e-3; 0.02769; −5.369e-3; d = −1.212e-3; ratios 3.43/4.43; μ = 36.115; bracket 0.2257, squared 0.0509. Cancellation at 0.1501. (2.16, 10.9): d = −1.330e-3, +20 %. The integrated rate scales as d², because L's line weight cancels the (ε∞/Z*)² of the bracket. **Rigid-ion factor 8.23 (PRIORITY): independently CHECKED.** Over Z* = 2.09–2.16 it runs 8.96–6.74. PBE: d = −7.5e-5 and a factor of 254. ±1 % gives ∓9 %. (ω_L/E_g)² = 5.7e-4. An 0.01 u shift moves d by 5.2 %.
- Mitridate source: electron numbers 28/36 appear in the text after Eq. (44); footnote 2 carries the Born-charge fix; widths are 1e-2 ω (Sect. III A); Eqs. (40)–(41) contain the electron mixing term −(g_e/e)ωq(1−ε∞). All **CHECKED**. That their projection reduces to Z − Q/ε∞ with Q = ±3 is consistent with Eq. (41) plus in-medium mixing. I did not re-derive it through their Eq. (7). It is a GAP of attribution only; it does not affect the factor.
- **Core kinetic-energy item (PRIORITY, R5): CHECKED as a parametric estimate.** Hartree–Fock total energies are Ga −1923.26 Ha and As −2234.24 Ha, so by the virial theorem T/m_e = 0.102 and 0.119. That gives Δd = +1.2e-4 per u, i.e. 10 % of |d|, and **the rate falls by ≈19 %**. The text's "about 0.1 electrons, d by a tenth, rate ~20 %" is right. Add the sign: the rate falls. This uses all electrons (core plus valence) and is non-relativistic, so it is still an estimate and DEFERRED-COMPUTE is appropriate. The R4 duplicate check: l.95 (Mitridate) and l.97 (core kinetic energy) are distinct paragraphs, with no duplicate in the current text.
- Line-centre reach: g = 3.08e-14 (rigid ions 1.07e-14) from R = 3.16e27 g² per kg·yr: **CHECKED**. Dark photon: ζ = 2.90e-17 (GaAs) and 1.02e-17 (sapphire); L_peak = 2I/πγ = 1.329; I_pol = 0.7586 meV; per-mass ratio 63.7: **CHECKED**. Polariton crossover 0.121 eV and 2600×: **CHECKED**.
- Eq. 11.8-shape (f_sh = 1, 3ε₀/(ε₀+2), ε₀): **CHECKED**.
- Mode normalization, polarization integral −4πr²/√(Mω), |⟨n|δH₀|0⟩|², Eq. 11.8-Pn and "32 = 2π·8·2/π": **CHECKED**. On resonance it equals Trickle Eqs. (7)–(8) (Trickle writes m²γ where the book has mω_nγ, which agree on resonance). Eq. (5) shielding: **CHECKED**.
- Eq. 11.8-Qeff, and the narrow limit (π/2)ω_nF = (π/2)|dη/dv|: **CHECKED**.
- **𝔔_DM = 1.341e6 at v = 256.0 km/s, shift 3.65e-7: CHECKED. "Prescription 1.8× too high at 𝔔_p = 𝔔_DM" (PRIORITY): independently CHECKED.** I get 𝔔_eff/𝔔_DM = 0.560 at the optimal tuning, i.e. 1.79×. The 10 % boundaries are 0.2 and 7.9. Also ⟨v²⟩^½ = 378.9 km/s.
- Numbers 12 neV, ~100 km, 100 m, 3.7 peV; uniformity up to 1.9e7 ω₁: **CHECKED**. t_coh = 6.6 ms is item 10.
- Eq. 11.8-h scaling: **CHECKED**. Pašteka Table 2: Cu −1.97e-2/−1.12e-3 and Si −2.17e-4/−8.56e-4 (printed −2.2e-4 and −0.86e-3): **CHECKED**.
- Eq. 11.8-drive; bar solution and free-end condition; Eq. 11.8-bar; low-frequency π²/24; one-mode M/2, force 2ω²hML/π², coefficient 4/π²; Σ_odd 4/(π²n⁴) = π²/24: **CHECKED**. limit11_8c values 0.4112/0.4053 and the 2.1 ω₁ boundary: **CHECKED** from the analytic forms.

## 11.9 Nuisance parameters
- Every number in the text and in WE 11.band30 matches we11_10(_400meV).log, and the arithmetic is **CHECKED**. 5260 → 14.4 per day; q_max = 159.0 keV; E_R = 0.483 eV; x_R = 11.8; ln(5260/4906)/0.0024 = 29; band 5.25–5.27e3; σ = 2.4e-3; 0.12 × (−0.069 %) = −8.2e-5; 2.2 × (−0.069 %) = −1.5e-3 (1/20 of 0.031); η² = 2.4e-3; η²ω_opt = 0.15 meV; (10 mK/293 K)² = 1.2e-9; 1/0.062 = 16; semilocal ε∞ 13.70/10.88 = 1.26 → (10.88/13.70)² = 0.63, i.e. −37 %. The 80 keV band is item 9.
- Table 11.1 rows agree with the text values. Rulings R1/R2 (illustrative WE parameters; the "upper template" label on the frequency rescale) are present. The core row should add the sign: the rate falls by ~20 % (see 11.8).
- Summary numbers: 0.53 keV; 16 meV LA; 0.28 keV free threshold and 21×; 237 K (⟨ω⟩/2 = 20.45 meV); 0.9/0.58 %; 5.0e3; 1.34e6. All **CHECKED**. The Part-1 summary items rest on part-1 review.

## PRIORITY / editor-note items for these sections
- Rigid-ion 8.2× (11.8): verified, 8.23.
- Resonator 1.8× (11.8): verified, 1.79.
- GaAs constants Z* = 2.11, ε∞ = 10.88 used throughout 11.8; E.17's 2.16/10.9 gives +20 %, as stated.
- Core kinetic ~10 % of d / ~20 % of the rate (11.8/11.9): verified parametrically. It is a decrease.
- 11.6 headline ≥ 5.0e3, PBE g/3 = 15.9, L = 5.42e-6, isotope +8.0 %: verified. The digitization caveat is present (R3).
- 11.5 n_A = 2 rate order: consistent with the evenness argument. The three-phonon coefficient is labelled fitted in 11.9.
- 11.7 "both" symmetries broken: done in the text.
- WE 11.10 (R1, R2): consistent.
