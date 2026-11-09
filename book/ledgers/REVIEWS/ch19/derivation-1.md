# Ch19 part 1 (ch19.tex, s19-1, s19-2, s19-3): derivation check (isolated)

Reviewer: derivation verifier (long-form-writing SKILL §5), 2026-11-06.
Method: sympy for every algebraic step (scratch `alg.py`); independent numerics for every printed number (`num.py`, `osc.py`); an independent Thomas–Fermi cross-section and an independent solver of eq:19.3-simple (`lind.py`, `solve.py`, `sweep.py`); an independent Mermin stopping calculation (`merm.py`); an RPA friction check (`fric.py`). All scripts are in the session scratchpad `rev19/`. Figscript logs (rec19, yield19_2, lind19_3, bethe19_3) were compared line by line. No QE runs. Sources fetched with lit.py into sources/review-ch19/ (PDFs deleted afterwards): 2303.02196, 2001.06503, 2209.04503, 1412.3028, 2405.10405, 1803.02903, 1001.3322, 1805.01568, PDG 2024 rev. 34 (pdg.lbl.gov), PDG Si atomic-properties page. Not fetchable (not on arXiv or open): holmstrom2008threshold, loferski1958radiation, lindhard1963integral, lewin1996review, zener1932non. Their values were checked only against sec:7.4 and Sorensen/Sarkis.

Verdicts: CHECKED = reproduced; WRONG = error, with the correction; GAP = correct as far as it goes, but a missing step, condition or caveat changes what the sentence claims.

## Summary of non-CHECKED items (details below)
1. WRONG: s19-3 WE we:19-lnI. The "\SI{174}{eV}, normalized to the exact (π/2)ω_p²" variant depends on the unit chosen for ω. So do "the L shell carries two thirds of ln Ī" and "the valence a sixth".
2. GAP (PRIORITY): s19-3, the 13 % soft-collision band is a one-sided, two-point sensitivity. It is not a model uncertainty, and it moves steeply with the continuation exponent.
3. GAP: s19-3, eq:19.3-asym. The ε^{1/6} law follows from the assumed x^{1/3} continuation. The TF-impulse cross-section itself steepens towards x^{1/2}.
4. WRONG (minor): s19-2, "the free-gas fraction vanishes at E_R,th". It vanishes at 336 eV, and it is 0.069 at 352 eV, as the text itself says two lines later. The same error is in the Fig. 19.2(b) caption.
5. WRONG (minor): s19-1 WE, "shortest phonon period of 67 fs". The value is 64.5 fs (measured ω_opt 64.1 meV) or 65.0 fs (PBE 63.6 meV). The conclusion is unchanged.
6. GAP (minor): the Migdal pairs per event (1.69) come from the energy-only cascade. The full-band cascade of sec:18.3-fullband gives fewer two-pair events near 5 eV, and the gap conventions do not match (1.11 vs 1.16 eV). The robust bracket is 2.3–4.4×10⁻⁴.
7. GAP (minor): 1.6° is the rms deflection per transverse component. The rms polar angle is √2 larger (2.3°).
8. GAP (minor): s19-1 l.7 "3 % at 500 eV" is the soft-limit value. With the exact bracket (×0.62, sec:12.3-validity) it is 1.9 %. Ch12 s12-1 l.133 has the same wording.
9. NOTATION: bare ℓ is used as a path length in 19.3, against the Lindhard logarithm ℓ(w). About 30 new symbols of 19.1–19.3 have no NOTATION row.
10. Campaign state: SOTA still says 352/**395** eV in several entries; the book's 399 eV is right with the book's inputs. No superseded value is used in these sections. Nothing in DC-RESULTS or returns/R18 bears on them.

## ch19.tex (opening)
- l.2: m_χ = 200 MeV → E_R,max = 21.15 eV; v_N = 12.05 km/s; bond (2.352 Å) crossed in 19.5 fs ("within 20 fs"): CHECKED.

## s19-1 Nuclear recoil on the BO surface
### Hand-over (PRIORITY: Wigner, eq:11.4-IA)
- l.15 phase e^{iq(X−y/2)}e^{−iq(X+y/2)} = e^{−iq·y}: CHECKED (sympy).
- eq:19.1-wigner W_+ = W_0|_{p_I→p_I−q}: CHECKED. The momentum of the struck nucleus is raised by q, with the Wigner convention of l.13.
- l.22: the Weyl symbol of T(p̂)+V(X̂) is the classical H: CHECKED.
- eq:19.1-dH: (p'+q)²/2M − p'²/2M = E_R + q·p'/M, with p' the pre-kick momentum: CHECKED (sympy).
- Keyresult, "reproduces eq:11.4-IA with exact mean and width; misses c₃": CHECKED. The deposit is a function of p_I alone. Its distribution over the momentum marginal 𝔣_κ is eq:11.4-IA term by term, and it holds for any state, since the momentum marginal of a Wigner function is a true distribution even where W is negative. Mean E_R. Variance (q/M)²⟨p_∥²⟩ = E_R⟨ω⟩ with ⟨p_∥²⟩ = M⟨ω⟩/2, which equals the exact second moment. The third cumulant of the ensemble is q³⟨p_∥³⟩/M³ = 0, against the exact c₃ = (q²/2M²)⟨∂²V⟩ of eq:D.32-c3, so c₃ is missed. Its share of the peak shape scales as c₃/σ³ ∝ E_R/E_R^{3/2} = x_R^{−1/2}: CHECKED against eq:11.4-IA's 1/q.
- l.31 "quantum corrections small above about 0.4 eV": CHECKED (0.406 eV, below).
- l.101 "classical propagation of a Wigner ensemble is exact for a quadratic Hamiltonian": CHECKED. The Moyal bracket reduces to the Poisson bracket.

### Smooth step and direction (PRIORITY: σ_ω 0.72 eV, 1.6°)
- l.33: σ_ω = (12.5 × 0.0409)^{1/2} = 0.7150 eV, 5.72 % of 12.5 eV: CHECKED. This is NOTATION's (4E_R E^kin_κ)^{1/2} with E^kin_κ = ⟨ω⟩/4 = 10.23 meV.
- l.33 direction scatter (E^kin_κ/E_R)^{1/2} = 0.0286 rad = 1.64°: CHECKED, but it is per transverse component (E^kin_κ is the kinetic energy along one axis, NOTATION row 877). GAP: say "rms deflection in each transverse plane, 1.6° (2.3° in polar angle)".
- eq:19.1-Ed and the step width "about 0.7 eV": CHECKED as an estimate. It assumes p_FP is sharp in the deposited energy; the text says the position spread adds to it.
- l.38: the measured 12.9 ± 0.6 eV is consistent with sec:7.4. Source not fetchable.

### Regimes (PRIORITY: boundaries and m_χ)
- λ_dB/ℓ_R = πω/E_R, independent of mass: CHECKED (sympy).
- 3Φ⁽²⁾/|Φ⁽³⁾| = 3×13.6/41.5 = 0.983 Å (sec:5.7): CHECKED.
- WE cage stiffness M⟨ω⟩² = 11.239 eV Å⁻²: CHECKED.
- Classical boundary πω/√0.1 = 0.4063 eV, x_R = 9.93: CHECKED. At 1 eV, λ_dB = 0.0542 Å, ℓ_R = 0.4218 Å, ratio² = 0.0165: CHECKED.
- Harmonic boundary ℓ_R = 0.3109 Å → 0.5432 eV; η_R²(1 eV) = 0.184: CHECKED.
- 12.5 eV: ℓ_R = 1.491 Å, v_N = 9.267 km/s, bond crossing 25.4 fs, 306 phonons: CHECKED.
- "less than half the shortest phonon period of 67 fs": WRONG (minor). 67 fs comes from App E.11's "15 THz". Silicon's top phonon is ω_opt = 64.1 meV measured (s5-7 l.78), period 64.5 fs (PBE 63.6 meV: 65.0 fs). Write "65 fs"; 25 fs is still below half of it. Fix App E.11 l.68 too.
- Massey at 20 eV: ξ_M = 15.16, e^{−ξ} = 2.6×10⁻⁷: CHECKED. ξ_M = ln10 at 867 eV and ξ_M = 1 at 4.60 keV: CHECKED. l.134: e^{−ξ}(12.5 eV) = 4.7×10⁻⁹ (printed 5×10⁻⁹): CHECKED.
- m_χ from eq:1.3-ERmax (v_max = 2.650×10⁻³): 27.5 / 31.8 / 153.5 / 261.5 MeV / 1.336 GeV for 0.406 / 0.543 / 12.5 / 36 / 867 eV: CHECKED (28/32/154/262 MeV/1.3 GeV). l.134 "below about 150 MeV": CHECKED.
- Fig. 19.1 caption: head-on closest approach 1.487 Å (20 eV) and 0.828 Å (200 eV) with ZBL at E_cm = E/2; first bond at 200 eV in 6.3 fs: CHECKED.
- l.103: 3⟨ω⟩/4 = 30.7 meV per atom (ZPE 123 meV per two-atom cell); 4096 atoms → 125.6 eV: CHECKED. Bartók 2018 "within at most 7 %" of DFT formation energies is in Sect. III E: CHECKED.
- l.105, harmonic acceptance test: energy per mode |q·e_κs|²/2NM_κ, summing to E_R: CHECKED. It is exact quantum mechanically as well, since e^{iq·X} on the ground state gives a coherent state with ⟨Δn_s⟩ω_s = |q·e|²/2NM.
- l.111: barrier 0.1 eV at 10 mK, exponent 1.16×10⁵: CHECKED.
- l.7: 1 − P_Mig: 9.7×10⁻⁴ at 16 eV: CHECKED. "3 % at 500 eV": soft-limit value (3.03 %). GAP: with the exact bracket factor 0.62 that s19-2 l.122 itself quotes, it is 1.9 %. Write "2–3 %" or "1.9 % with the exact bracket" here and in s12-1 l.133.

### Partition (PRIORITY: eq:19.1-partition, eq:19.1-heat)
- eq:19.1-partition: CHECKED. Energy conservation per trajectory gives ω − ω_e = [E^ad_min(end) − E^ad_min(perf)] + [E_vib(end) − ZPE(perf)] = E_st + E_lat, with E_lat as defined (ΔZPE inside E_lat).
- eq:19.1-heat follows from ω_e = N_eh E_g + E^casc_heat (eq:18.1-energy): CHECKED. The electronic-deposit limit reduces to eq:18.1-energy: CHECKED.
- l.130 "a close Frenkel pair keeps about half of the lowest threshold": 6.8–7.5 eV against 12.5 eV is 54–60 %. CHECKED as "about half"; matches sec:7.4.

## s19-2 Electronic excitation by the recoil
- l.3: 100 eV → v_N = 26.2 km/s, v_F/v_N = 79.9; 0.102×100/3.8 = 2.68 pairs; m_χ(100 eV) = 0.439 GeV: CHECKED.
- l.7: ω = k·v_N − k²/2M ≤ kv_N: CHECKED.
- eq:19.2-transfer: the crossing of ω = kv_N with ω_− = k²/2m − kv_F gives k = 2m(v_N+v_F) and ω_max = 2mv_N(v_N+v_F). Moving-wall form ½m[(v_F+2v_N)² − v_F²]: identical (sympy). CHECKED.
- eq:19.2-Eth (PRIORITY): M v_th²/2 with v_th = E_g/(2mv_F) equals (M/m)E_g²/(16E_F) (sympy): CHECKED. Si: n_e = 0.199761 Å⁻³, k_F = 1.80847 Å⁻¹ = 3.5686 keV, E_F = 12.461 eV, v_F = 6.9836×10⁻³ = 2094 km/s, v_th = 1.6393×10⁻⁴ = 49.15 km/s, M/m = 51197, E_g²/16E_F = 6.866×10⁻³ eV, E_R,th = 351.5 eV = 300 E_g: CHECKED. Ge (a = 5.658 Å, E_g = 0.744 eV): k_F = 1.7359 Å⁻¹, E_F = 11.481 eV, M/m = 132396, E_R,th = 399.0 eV: CHECKED.
- Quadratic root ½[(v_F² + 2E_g/m)^{1/2} − v_F] (sympy): CHECKED. With it, 335.9 eV (−4.44 %) and 386.5 eV (−3.11 %): CHECKED.
- WE: v_N(100 eV) = 8.743×10⁻⁵ and ω_max = 0.632 eV: CHECKED. m_χ(352 eV) = 0.835 GeV: CHECKED.
- eq:19.2-pmin p ≥ E_g/2v_N − m v_N (sympy): CHECKED. At 100 eV, p_min = 3.368 Å⁻¹ = 1.862 k_F: CHECKED.
- l.49 "In the free gas the fraction 1 − (p_min/k_F)³ … vanishes at E_R,th": WRONG. At E_R,th (v_N² dropped), p_min = k_F − m v_th < k_F, so the fraction is 0.069 there (the text prints 0.07 at l.51). It vanishes where p_min = k_F, which is the v_N²-kept threshold, 336 eV. Fix: "vanishes at the threshold with v_N² kept, \SI{336}{eV}". Same fix in the Fig. 19.2(b) caption ("which vanishes at E_R,th").
- EPM promotable fraction (PRIORITY): the method was read (yield19_2 epm_momentum/frac_above). The plane-wave weights Σ_bands|c_{k+G}|² are normalized over a 10³ grid and the fraction counts |k+G| > p_min. Values 0.2345 / 0.0221 / 0.00338 beyond 1, 1.5, 2 k_F, and 0.270 / 0.0469 / 5.58×10⁻³ / 3.9×10⁻⁴ at 352/200/100/50 eV, match the log: CHECKED. Not recomputed independently (EPM code reused).
  - GAP (minor): at 50 eV, p_min = 4.78 Å⁻¹ lies within 10 % of the basis cutoff 5.30 Å⁻¹. The 4×10⁻⁴ is therefore limited by basis truncation as well as by the smooth pseudo-orbitals. Add "and by the plane-wave cutoff" to the understatement clause, or drop the 50 eV value.
- l.53: σ_ω(100 eV) = 2.02 eV: CHECKED.
- l.59 ξ_M = 6.78 / 3.61 / 2.14 at 100 / 352 / 1000 eV: CHECKED.
- eq:19.2-LZ (PRIORITY): Vutha (1001.3322) gives P = exp(−2πΩ²/Δ̇), with Ω the off-diagonal coupling and Δ̇ the sweep rate of the diabatic energy difference, as the probability of the diabatic (non-adiabatic) passage. With Ω = h_LZ and Δ̇ = v|ΔF_LZ| this is eq:19.2-LZ: CHECKED. Double passage with averaged phase, 2P(1−P): CHECKED.
- Born parameter (PRIORITY): Z α/v_F = 14.63 (Si), 34.84 (Ge): CHECKED. GAP (minor): the bare charge overstates the ion's charge, which its own electrons screen. The conclusion (non-perturbative) does not depend on it, since α/v_F = 1.04 per unit charge already. Suggest adding "even a unit charge gives α/v_F ≈ 1".
- l.78 cascade means: ω/3.749 = 0.520, 0.774 (2.9 eV), 1.056 (3.96), 1.600 (6.0): CHECKED. The n̄ values 1.000/1.049/1.645 are taken from the log, as cascade output.
- l.89: b_N ≤ 0.35 is 1.3 % of 26.7 pairs: CHECKED.
- l.91: Albakry: 55.7 keV beam, 4 mm, E_t = E_r + n_eh eV with ε = 3.8 eV (Eq. (1)): CHECKED. With 3.749, 1 − 3.749/3.8 = 1.34 %: CHECKED.
- l.100: Lindhard 0.1529 at 100 eV against 0.102 (×1.50); 0.188/0.136 = 1.38 at 0.46 keV: CHECKED. Kavner: 254 eVnr, 64 ± 8 eVee, 77 K, 25 ± 3 % against 14.3 % (κ = 0.157, Table IV): CHECKED. Book k_L(Ge) = 0.1573: CHECKED.
- Albakry Table II, all six Y and F values and the fit B = 0.261 with Y_10keV = 0.302 pinned to Lindhard: CHECKED.
- eq:19.2-FNR (law of total variance; sympy): CHECKED. At 3.91 keV: ⟨E_el⟩ = 922.8 eV and σ = 170.4 eV = 18.5 %; F_NR/F_eh = 70.6: CHECKED.
- Migdal part (PRIORITY): ΔY = (3.8/100)×6.068×10⁻³×1.694 = 3.906×10⁻⁴; ×1.924 → 4.436×10⁻⁴. Shares 0.38 % (100 eV) and 0.29 % (0.46 keV); 1/260: CHECKED. Soft-limit E_R independence (dP/dω ∝ v_N² ∝ E_R): CHECKED. P_Mig = 6.07×10⁻³ matches s12-3/s12-4. Bracket factors 0.93/0.62 match s12-3 l.101. The 0.6 % lattice weight: CHECKED.
  - GAP: n̄ near ω_e ≈ 4–8 eV is cascade-model dependent. Sec:18.3-fullband shows that the full-band cascade puts fewer events in the two-pair bin than the energy-only cascade used here. Also, P_Mig is integrated from the 1.11 eV scissor gap of the ch12 tables, while cascade_nbar returns 0 below E_g = 1.16 eV. Neither changes "almost entirely collisional". The model-free bracket, n̄ ≥ 1 per event, gives ΔY ≥ 2.3×10⁻⁴, so quote "2.3–4.4×10⁻⁴ (0.2–0.4 %)", or state that 1.69 is the energy-only cascade value. No conflict with CORRECTIONS l.654 (the step model is not used).
- l.126: e^{−ξ} 1.13×10⁻³ (100 eV) → 2.6×10⁻⁷ (20 eV); the Migdal factor of 5: CHECKED.

## s19-3 Stopping of slow ions
- l.9: v_N(1 keV) = 2.765×10⁻⁴ = v_F/25.3: CHECKED.
- a_L = 0.8853a₀/(√2 Z^{1/3}) = 0.13745 Å (Sorensen Sect. II A; Sarkis 2020 the same): CHECKED.
- eq:19.3-reduced: ε = a M₂E/[Z₁Z₂e²(M₁+M₂)] → a E/(2Z²e²) for equal masses. c_L = 0.024350 keV⁻¹ against 11.5 Z^{−7/3} = 0.024344; ε = 1 at 41.07 keV; ε(1 keV) = 0.0243: CHECKED.
- T_n = E sin²(θ/2) (γ = 1): CHECKED. eq:19.3-dsigma ↔ Sarkis 2023 Eq. (2) form πa² f(t^{1/2})dt/2t^{3/2}: CHECKED (dt = 2x dx).
- Impulse deflection θ = −ε⁻¹ dI/dβ with I = ∫₀^∞ (half line): CHECKED. The full-line integral is 2I, and E_cm = E/2 gives θ = −2Z²e²I'/(2E_cm a) = −I'/ε. x = −I'/2; f = 2x²β|dβ/dx|; Rutherford f = 1/2x: CHECKED.
- f peak 0.4306 at x = 0.140; s_n max 0.405 at ε = 0.30 (independent TF, φ'(0) = −1.588071): CHECKED. ("0.41" rounds 0.405.)
- eq:19.3-Se k_L = 0.133 Z^{2/3}A^{−1/2} = 0.1458 (Sarkis 2020 Eq. (4)): CHECKED. "Z^{1/6} = 1.55 inserted by hand" is Sarkis 2023 ("Scaling length"): CHECKED. Physical stopping 0.876 / 2.769 / 8.756 eV/Å: CHECKED (n_at = 0.04994 Å⁻³).
- l.32: proton at the speed of a 1 keV recoil: 0.32 eV/Å (Mermin, independent: 1173.7 v eV/Å); ×196 = 63.6 eV/Å; ratio to 2.77 eV/Å = 23: CHECKED. Note: pure RPA (Lindhard) gives 1113 v eV/Å (−5 %). "The same electron gas" means the Mermin model with γ = 0.1ω_p; say so at l.152.
- eq:19.3-basic and approximations (A)–(E) against Sarkis 2020 Eq. (3) and Sect. II: CHECKED. Sarkis's last term is φ̄_e(T_ei − U_ei), with binding; immaterial after (A).
- Expansion with (C), (E) and the separation (D) leading to eq:19.3-simple, and Sarkis Eq. (5) with t = x²: CHECKED.
- eq:19.3-asym (sympy, general exponent a): the RHS is (λC/2)ε^{p+a−1}∫s^{(a−3)/2}[1−(1−s)^p−s^p]ds, so p = 3/2 − a and y = Cε^{1/2−a}. For a = 1/3: p = 7/6, J = 0.47423, 2/(λJ) = 3.288 (λ = 1.2828): CHECKED.
  - GAP (PRIORITY-related): the law depends on the continuation. The TF-impulse f has a local slope of 0.363–0.365 at x = 2×10⁻³ and 0.42 at 10⁻⁵, and tends to 1/2 (φ_TF ∝ r⁻³, so V ∝ r⁻⁴, so m = 1/4). For a = 1/2, S_n ∝ ε^{1/2} like S_e, and y tends to a nonzero constant as ε → 0 (J → 0). "Falls only as the sixth root" is therefore a property of Lindhard's m = 1/3 power law, not of the screened TF cross-section. Add: "with the x^{1/3} continuation (Lindhard's m = 1/3); the Thomas–Fermi tail itself, f ∝ x^{1/2}, would make S_n and S_e scale alike and keep y finite as ε → 0."
- Solver (PRIORITY): an independent implementation (own TF shooting, own impulse integral, Gauss–Legendre in ln s, affine solve for ν'(ε) at each step, 4000-point log grid) reproduces lind19_3. Main continuation y = 0.0968 / 0.1378 / 0.1576 / 0.2200 / 0.2713 / 0.4225 at 4.1 eV / 41 eV / 0.1 / 1 / 4 / 41 keV, against the log's 0.0967 / 0.1377 / – / 0.2198 / 0.2711 / 0.4224. Grid halving: 1.5×10⁻⁵. Fit/solution 0.970 (100 eV), 0.952 (1 keV), 0.951 (4 keV), 0.962 (41 keV). "3 % below 100 eV; 4–5 % below between 1 and 20 keV; 0.210 vs 0.220": CHECKED.
- 13 % band (PRIORITY: is it honest?): GAP. The number is reproduced: local slope 0.3628 gives ×1.132 at 1 keV and ×1.100 at 4 keV; my TF tail gives 0.3653 and ×1.145 / ×1.110. It is not a model-uncertainty band, for three reasons.
  (i) It is extremely sensitive to the exponent. y(1 keV) = 0.197 / 0.220 / 0.249 / 0.307 / 0.500 for a = 0.30 / 1/3 / 0.363 / 0.40 / 0.45, that is −11 % / 0 / +13 % / +39 % / +127 %. A 0.7 % change in the matched slope (0.3628 → 0.3653) moves the band from 13.2 % to 14.5 %.
  (ii) It is one-sided and two-point. Nothing places the truth between x^{1/3} and x^{0.363}: the TF cross-section's own continuation steepens towards 1/2, beyond the band, while binding and the lattice (Sarkis U, E_d) remove soft transfers altogether.
  (iii) Below ε ≈ 2×10⁻³ (E ≲ 82 eV) the whole cross-section of a slow secondary lies in the continued region.
  So "13 %" measures sensitivity to one arbitrary choice. Recommend wording such as "changing the continuation exponent from 1/3 to the local slope 0.363 raises y(1 keV) by 13 %; 0.30 lowers it by 11 % and 0.40 raises it by 39 %; the yield of a keV recoil is not determined by the binary model below x ≈ 2×10⁻³". Present the dark band as an illustrative sensitivity, not as "the spread of the model itself" (limit-box sentence l.73). The data deficit (8–38 %) still exceeds ±13 %, but not the a = 0.40 variant, so the comparison in l.73 should be softened.
- Limit box: data/fit 0.667 / 0.635 / 0.724 / 0.616 / 0.729 / 0.918 → deficits 8–38 %: CHECKED. ε ≥ 0.1 ↔ E ≥ 4.11 keV and "Lindhard describes Si up to ε ≳ 0.1 (4 keV)" (Sarkis 2020 Sect. II): CHECKED.
- l.82: Sarkis constant binding: x_min = (ε c_L U)^{1/2} ↔ t_min = uε (Sarkis Eq. (9), App. A): CHECKED. U = 0.15 ± 0.06 keV, C₀ = 9.1×10⁻³, C₁ = 3.33×10⁻⁵ (Table III), k = 0.161 (Table IV): CHECKED. Zero of the Eq. (13) ansatz at 297.6 eV: CHECKED. Minor: "vanishes for E_R ≤ 2U" (300 eV) and "reaches zero at 298 eV" differ by the C₀, C₁ terms; say "near 2U".
- Sarkis 2023: U_FP = 23.6 eV, 102 points from 0.68 keV to 3 MeV, χ²/dof = 1870/101, Arista–Ziegler with ξ_e = 1.26, straggling added: CHECKED. Z₁ = 12 with ZBL length gives C = 0.02684 keV⁻¹, ×1.102 ("10 % higher"): CHECKED.
- l.84 Sarkis Eq. (9) term −½kε^{3/2}ν'' from T̄_n = ε/2 (App. B): CHECKED as quoted. The book's objection, that under (D) the cross term vanishes, is logically correct.
- l.84: 0.88 eV/Å at 100 eV; 5.6×10⁻³: CHECKED.
- Bethe derivation (eq:19.3-bethe, eq:19.3-lnI): the exchange of integration order is verified symbolically with a test function. The prefactor (2Z²α/πv²)(π/2)ω_p² = 4πZ²α²n_e/(mv²) (sympy), with q₀ cancelling: CHECKED. Consistent with eq:4.4-dEdx as printed in s4-4.
- PDG: Eq. (34.5) bracket ½ln(2mβ²γ²W_max/I²) − β² with W_max = 2mβ²γ² gives ln(2mv²/I) + O(v⁴); the ln γ² ≈ β² cancels −β² (sympy): CHECKED. "Geometric average … weighted by oscillator strength" is in 34.2.1: CHECKED. "0.01 < β < 0.05 no satisfactory theory" is in 34.2.6, and shell/Barkas/Bloch corrections to ≈ β = 0.05: CHECKED. Si I = 173.0 eV and ħω_p = 31.05 eV (PDG page): CHECKED.
- WE we:19-lnI, oscillator: ln Ī_val = 3.0115, Ī = 20.32 eV (+16.8 %); Γ = 2 eV → 18.98 eV; f-sum shares 0.885 / 0.078 / 0.024: CHECKED (independent quadrature).
- WE, core: ω_p(14 e) = 31.049 eV, (π/2)ω_p² = 1514.3 eV²; w_j ln ω_j = 0.832 + 3.340 + 0.910 = 5.082 → 161 eV: CHECKED (arithmetic; the tabulated data were not reloaded).
  - WRONG: "Normalized instead to the exact (π/2)ω_p², the same data give 174 eV." With a normalization S ≠ ∫ωL, ln Ī = S⁻¹∫ωL ln ω is not invariant under a change of the unit of ω. The same operation gives 174.1 eV in eV, 167.3 in Ry, 165.6 in Ha and 156.8 eV in keV. The data determine Ī = 161 eV (rescaling L to the exact f-sum leaves this unchanged). Fix: drop the 174 eV variant and the "inside this range" clause. Write "Ī = 161 eV, 7 % below the adopted 173.0 eV; the tabulated spectrum overshoots the f-sum by 1.5 %, a measure of its error."
  - WRONG (same cause): "The eight L-shell electrons carry two thirds of ln Ī … the valence … a sixth." These shares of ln(Ī/1 eV) depend on the unit: in keV the shares are 0.60 / 0.47 / −0.07. Unit-free statement: the L shell holds 61 % of the oscillator strength at a log-mean energy of 246 eV. Relative to Ī, w_j ln(ω_j/Ī) = −0.59 (valence), +0.26 (L), +0.34 (K), so the K shell raises Ī as much as the L shell. Suggested: "the L shell holds 61 % of the oscillator strength and the valence electrons 28 %; without the core shells Ī would be the 19.5 eV of the valence band." The editor note "L shell 2/3" should be withdrawn.
- l.139: 1 MeV proton 2mv² = 2178 eV (12.6 Ī), α/v = 0.158; 10 keV Si: 0.781 eV (4.5×10⁻³ Ī), 116.8: CHECKED.
- Limit Check 19.3b and the Bethe validity (PRIORITY: 1.84 v_F): an independent Mermin (γ = 0.1ω_p) stopping gives full/Bethe = 0.903 at 1.84 v_F, 0.950 at 2.27 v_F and 0.992 at 4.3 v_F, with Ī_model = 17.91 eV (Drude q→0, f-sum 1.0000): CHECKED. The friction 1173.7–1174.1 eV/Å per unit v up to 0.1 v_F (0.04 %): CHECKED. The zero of the Bethe log at 0.599 v_F: CHECKED. Recoils at 0.0125–0.125 v_F with Born 1168–117: CHECKED.

## NOTATION and conventions
- σ_ω, E^kin_κ, x_R (⟨ω⟩ = 40.9 meV, arithmetic mean), k_L, ϵ_L (\epsilon, as NOTATION requires), g_L, y_L, T_d, Ī, Y_q, E_R,th, E_st, p_FP, E_heat: consistent. No factor-2, π or sign drift found. Wigner, Fourier and LZ conventions are internally consistent (checked above).
- Drift: s19-3 l.25 and l.49 use bare ℓ for the path length ("ρ_L = πa_L²n_at ℓ", "(dE/dℓ)_e"), against NOTATION's ℓ(w) Lindhard logarithm. Editor note 19.1 renamed the Massey ℓ for this very reason. Use x (as eq:19.3-bethe does) or s_path.
- Missing rows (none in NOTATION.md): ℓ_R, η_R, λ_dB, ξ_M, ℓ_int, E_lat, t_pr, 𝒲_0/𝒲_+, ê_I, ω_max, v_{N,th}, p_min, h_LZ, ΔF_LZ, P_LZ, b_imp, E_coll, 𝒩_exc, n̄(ω_e) (n̄ exists in 18.1 as the mean pair number, which is consistent), ΔY_q^Mig, E_el (row exists as 6.1 "electronic energy", so add the 19.2 meaning or decorate it), F_NR (row says 20.5; first use is now 19.2), a_L, c_L, θ_s, T_n, x_L, f_LSS, β/I(β)/ζ (local), s_n (distinct from s_{n,ℓ} of 11.7), ρ_L, λ_L, J (local), ϵ_d, T_d^{(e)}, U, w_j/ω_j (local). The CORRECTIONS l.154 campaign name ξ_Mas is not used; the book's ξ_M needs its row.
- E^kin_κ is per axis (NOTATION 877); see the 1.6° GAP above.

## Campaign state, CORRECTIONS, DC-RESULTS
- ⟨ω⟩ = 40.9 meV used throughout (CORRECTIONS ruling; no 45 meV): CHECKED.
- Binary thresholds: the book's 352/399 eV (336/387 eV with v_N²) are correct with the book's inputs. SOTA.md still says "≈352/395 eV" (l.111, 251, 302, 349), and the editor note flags SPINE LO(i) and E.23 l.3/27 (395). Update those; the 395 comes from a slightly different Ge input. No superseded value appears in s19-1 to s19-3.
- CORRECTIONS l.360 (2303.02196 Eq. (1) books the phonon energy as E_r) agrees with s19-2 l.91: CHECKED.
- CORRECTIONS l.646 (the diagonal Migdal form is valid in the impulse regime): the 100–460 eV recoils of the Migdal part of Y_q are in that regime. No change.
- DC-RESULTS: DC-67 (Si ε 3.7468 eV, F 0.11398; library not releasable). The book quotes the measured ε_eh = 3.749 eV and F_eh = 0.119 and uses its own casc18_4, not P_casc_lib, so the restriction is respected. The 0.06 % difference in ε does not change the 1.3 % in l.91. No other DC row and nothing in returns/R18 (DC-2, 36, 41, 49, 54, 67, 83, 91, 93) bears on 19.1–19.3.

## Editor-note items for these sections (all re-verified above)
19.1 Wigner hand-over, mean, width and missed c₃: CHECKED. σ_ω 0.72 eV: CHECKED. 1.6°: CHECKED, per-component GAP. Boundaries and m_χ: CHECKED. Partition identities: CHECKED. 19.2 binary threshold 352/399 (336/387): CHECKED. EPM 0.56 %: CHECKED (log; cutoff GAP at 50 eV). LZ kernel: CHECKED. Born ~15: CHECKED. Migdal ΔY 3.9–4.4×10⁻⁴: CHECKED with cascade-model GAP. 19.3 solver: CHECKED (independent). 13 % band: GAP (not honest as a band). Bethe 1.84 v_F: CHECKED (independent). Si Ī: 20.3 and 161 CHECKED; 174 and "L shell 2/3" WRONG (unit-dependent). thomas1925zahl is not cited in s19-3 (thomas1927calculation and fermi1928statistische are used for TF): CHECKED. The Lindhard 1963 credit and Lindhard–Scharff via Sarkis 2023: as stated. Limit Check box numbering was not checked (build matter, outside a derivation review).
