# App. E second pass, part 2: consistency of E.21–E.27 with the accepted book

Scope: tex/appE/E-21.tex to E-27.tex against accepted Chs 1–22, SPINE App. E rows, state/DC-RESULTS.md.
Method: every \cref in E-21..27 resolved against all \label in tex/ (all resolve); every `app:E.2[1-7]` pointer in tex/ch* read
in context; numbers recomputed by hand where cheap. BANNED-TERMS.txt regex run over all seven files: no hits.
Verdicts: CHECKED (agrees), WRONG (disagrees with governing source; correction given), GAP (missing or under-specified).

## Summary of findings that need a tex change

| # | location | verdict | correction (governing source) |
|---|---|---|---|
| 1 | E-24 l.3 | WRONG | model Fano factor is 2.4σ low (0.114 vs 0.119 ± 0.002), not "two standard deviations"; ε is fitted exactly (3.749), not "to 1 %" (Ch18 tab:18-pairs, s18-summary) |
| 2 | E-24 l.3 | WRONG | DFT full-band 3.10 eV is 14 % below 3.6 eV, not 15 % (s18-4 l.172); cite Sect. III and "time-dependent density-functional loss function" as s18-4 l.16 does |
| 3 | E-24 l.25 | WRONG | uses A_AB = 5.2 and the R–K plane 1.7E_g + 0.084A + 1.3; book uses one constant set, A_AB = 5.703 eV³, secant slope ∂ε/∂A = 0.076 eV⁻² (s18-4 l.11, l.64) |
| 4 | E-24 l.9 | WRONG | Si loss-function peak is 16.4 eV (sec:4.4); 16.6 eV is the free-electron ω_p |
| 5 | E-25 l.17 | WRONG | ε₀ = 11.4 (liquid He, sec:7.4, used by s20-1 l.142), so n_s = 6.3 to 12.6×10⁴ cm⁻², not 11.7 and 6.5–12.9×10⁴ |
| 6 | E-25 l.9 | WRONG | exciton field ionization at E_x^b/(e a_x) = 3.5×10⁴ V/cm (s18-5 l.72), not "about 4×10⁴" |
| 7 | E-25 l.3, l.92 | WRONG pointer | the readout verdicts are no longer in sec:20.5 (subsection cut); they live in the Chapter 20 Summary (s20-summary l.13) |
| 8 | E-26 l.17 | WRONG | says the vector-operator defect is "open"; Ch10 states it is bounded: free vertex low by at least 1/r (1.7 for Xe 1s at 56.5 keV), transverse current only raises it, only the (Zα)² part has unknown sign (s10-9 l.176, l.232; tab:22-gaps "bounded") |
| 9 | E-26 l.17 | WRONG (number) | (Zα)² ≈ 0.16 for Xe K; Ch10/22 print 0.13. Arithmetic (54/137.04)² = 0.155 favors E-26; one side must change, Ch10.9 l.176, l.232 and Ch22 l.56 if 0.155 is adopted |
| 10 | E-26 l.15 | WRONG | expansion must keep the ω term: 1 − 2(m_χ² − 2m_χω)/m_med² + … (s10-9 l.178) |
| 11 | E-26 l.9 | WRONG | relativistic shift for Cu is computed, not "estimated": −1.97×10⁻² in d ln a/d ln α (Si −2.2×10⁻⁴), nuclear-mass term −1.12×10⁻³ (Cu), −0.86×10⁻³ (Si), pasteka2019 Table II (s11-8 l.186); the shift enters d ln a/d ln α, not both derivatives |
| 12 | E-21 l.38 | WRONG | "plain amplitude falls as p⁻¹⁰": the amplitude falls as \|p − q\|⁻⁵, its square as \|p − q\|⁻¹⁰ (s16-3 l.38); 10 eV maximum is 740 (s16-3), say "up to 740" |
| 13 | E-21 l.45 | WRONG (term) | Ch16.3 and eq:2.2-fermi call 7.3/3.4/2.6 the Fermi factor; E-21 says "Sommerfeld factor" |
| 14 | E-23 l.11 | WRONG | Qb@ll is itself a plane-wave code with real-time TDDFT; "plane-wave codes ... have no production real-time module" contradicts the list |
| 15 | E-23 l.17 | WRONG | quantum–classical boundary is 0.41 eV (s19-1 l.83, s19-summary), not "about 0.3 eV" |
| 16 | E.15 l.56 (outside range, per brief) | WRONG | "reuses the HSE06 run with spin–orbit coupling of app:E.14": E.14 now records that HSE06+SOC fails the order check; reword to bands that pass the E.14 check (GW the next route) |
| 17 | E.1 l.147 (outside range, per brief) | WRONG | "needs a hybrid functional or a quasiparticle calculation": HSE06 at fraction 0.25 inverts Γ and L in Ge; say a quasiparticle calculation, or any band set that passes the order, gap and mass check of app:E.14 |

GAPs (spec under-specified against what a chapter says it supplies, or a DC result not stated):
G1 E-24 Ge route; G2 E-24 GaAs ε∞; G3 E-24 library tail law; G4 E-24 Richardson order; G5 E-24 marks; G6 E-24 pair separations;
G7 E-21 donor U coefficients and 3.60 keV line; G8 E-21 R̃²ᴰ, r₀ and tube excitons; G9 E-23 HSE arm in Ge; G10 E-22 Born-limit
acceptance; G11 E-25 interface acceptance; G12 E-26 axioelectric caveats. Details in the per-section lists.

## E.21 Dopants, color centers and small targets

- l.3 pointers sec:16.2–16.6 → CHECKED (each section points back to app:E.21: s16-2 l.46, l.202; s16-3 l.31, l.65, l.133; s16-4 l.99; s16-5 l.44, l.108; s16-6 l.30–32, l.115, l.123).
- l.3, l.14 NV ZPL 1.945 eV, singlet 1.19 eV → CHECKED (s16-6 l.123, doherty2013).
- l.18 donor densities 10¹⁸ and 1.8×10¹⁸, n_D/n_c 0.3–0.6 → CHECKED (s16-5 l.104, n_c ≈ 3×10¹⁸).
- l.18 k₀ = 0.85(2π/a) = 1.94 keV; 3.88, 0.685, 2.74, 2.33 keV → CHECKED arithmetic. GAP (G7a): Ch16.5 l.44 lists three opposite-valley momenta, 0.685, 3.60 and 3.88 keV; E-21 omits 3.60 keV. Add it.
- l.18 "All are reached by MeV-scale dark matter" → GAP (minor): Ch16.5 gives the thresholds, 130 keV at 0.685 keV and 441 keV at 2.33 keV; quote them.
- l.20 output → GAP (G7b): Ch16.5 l.44 says the line strengths need the coefficients 𝒰_{j'j}(G) from the Bloch functions at the minima "(app:E.21)", and Ch16.9 l.40 lists "the valley-orbit coefficients of a donor" as specified. E-21 computes f^loc_D from those Bloch functions but never names 𝒰_{j'j}(G) as an output. Add it, with the same Bloch functions and grid.
- l.22 Du et al. 3q̃ for 3q̃², factors 0.6–1.5 over 0.02–10 MeV → CHECKED (s16-5 l.37: 1.47, 0.91, 0.59, 0.56). No novelty wording → CHECKED.
- l.26 tan 2θ_CT formula → CHECKED (s16-4 l.93).
- l.32–34 low-dimensional tables, N_ch = 4 → CHECKED (s16-2 l.71). GAP (G8): Ch16.2 l.46 says app:E.21 specifies "how R̃²ᴰ, r₀ and the corresponding tables for tubes and stacks are computed"; E-21 does not name R̃²ᴰ or r₀ among its quantities. Ch16.9 l.40 also says the excitons of a semiconducting tube are specified; E-21 has only RPA on projected bands, no ladder for tubes. Either add the two outputs and a BSE (or ladder) step for semiconducting tubes, or change the chapter pointers.
- l.38 OPW ratio, Clementi–Raimondi 1.568/a₀, 0.4–4.3 at 50–100 eV → CHECKED (s16-3 l.38). See #12 for the falloff law.
- l.45 Fermi factor 7.3, 3.4, 2.6 → CHECKED values (s16-3 l.62, l.65); name, see #13.
- l.49–51 ionic color centers, yield factors, tagged neutrons at 10 mK and 5.9 keV X-rays → CHECKED (s16-6 l.30–32, l.125).
- l.51 ΔSCF with HSE/PBE0 for LiF, NaF, MgO, LiH → CHECKED; no DC result bears on wide-gap halide hybrids.
- l.55–57 bond breaking, ~10² keV momenta → CHECKED (s16-6 l.93, H₂ q_min 134 keV).
- Executability, units → CHECKED: eq:E.21-gamma and eq:E.21-ROPW dimensionless as stated; costs consistent with table.

## E.22 Defects and two-level systems

- l.3, l.7 pointers sec:16.7, 16.8, 19.6, app:C.20 → CHECKED (s16-7 l.84, l.144, l.161, l.250; s16-8 l.37, l.114; s19-6 l.22, l.57, l.88, l.154, l.187).
- l.11 tungsten cells 54/128/250 atoms, ~2.1×10⁵ plane waves at 60 Ry, 2100 bands, 7 GB → CHECKED by hand (V = (5a)³, N_PW = Vk³/6π²).
- l.13 resonator fits K_b = 0.07, 0.11, α_ohm = 0.28, 0.44 → CHECKED (s16-8 l.35). GAP (G10): Ch16.8 l.35 shows 0.28 is the Born reading; beyond Born the same contact potential gives 0.19, and the measured rate needs a contact potential 32 % stronger. The acceptance test should compare the computed rate (or the computed α_ohm beyond Born) with the measured damping, not with α_ohm = 4K_b = 0.28.
- l.17 S_HR = ½ωΔQ², E_reorg → CHECKED (ħ = 1).
- l.25 ln(3.2×10²⁰) = 47.2, λ_tun ≤ 23.6, two-parabola 27.5, 14 % → CHECKED arithmetic and against s16-8 l.114, s19-6 l.187.
- l.27 384 displacements, ~900 SCF, 120 core-h → CHECKED.
- l.29 Poisson series eq:E.15-ste → CHECKED (correct target).
- l.33 W superconducting near 15 mK; Peierls barrier meV atomistic → CHECKED (s19-6 l.139, l.154).
- l.38 S_pol(0) = J₃ω_D²/2π, thermal πJ₃T²/3 → CHECKED.
- l.51 rigid oxygen, eight electrons, 1 Å; no further dielectric factor → CHECKED (s16-7 l.144, l.147). l.57 analytic small-q long-range piece is a cell artifact fix, consistent with Ch16.7.
- l.55 216 atoms a-SiO₂, 15 Å, 0.83 keV, 576 bands, 2.5 GB → CHECKED by hand.
- l.65 acoustic control P̄γ²/ρc² and tan δ₀ → CHECKED (s16-7 l.55, l.84, l.141).
- No banned terms; dimensions of displayed formulas → CHECKED.

## E.23 Nuclear-recoil partition and charge yield

- l.3 E_R,th 352/399 eV; Y_q = 0.102 at 100 eV; Ge 254 eV, 25 ± 3 % → CHECKED (s19-2 l.3, l.100; SPINE Ch19 row).
- l.9 Massey numbers: v_N 11.7 km/s at 20 eV, ξ ≈ 15; 83 km/s, ξ ≈ 2 at 1 keV; E_g 1.17 eV → CHECKED arithmetic; gap is the 0 K value (tab:3-materials).
- l.11 Qb@ll statement → see #14. 216 atoms = 16.3 Å, 5.4×10⁵ grid points, 432 orbitals, 3.7 GB, 250 core-h per trajectory, ~10⁶ → CHECKED.
- l.13 hybrid arm → GAP (G9): DC-2 (and app:E.14 l.62) show HSE06 at fraction 0.25 inverts Γ and L in Ge, with the L gap correct. For the Ge–Ge kernel the HSE arm then measures the local-gap error with a known valley-order defect; say so, or state that the Ge HSE arm is a spread estimate only. Si unaffected.
- l.13 cost: 10 % subset × 30 → a few 10⁶ core-h → CHECKED.
- l.17 "controlled between about 0.3 eV and E_d" → see #15 (0.41 eV; E_d 12.5–36 eV by direction, s19-summary).
- l.17 partition grid 1 eV–10 keV → CHECKED (s19-1 l.132). t_pr 10–100 ps → CHECKED (s19-1 l.67, l.111).
- l.21 ZPE 123 meV per cell → 31 meV per atom, 126 eV in 4096 atoms → CHECKED (s5-3 l.75). "ten to thirty times a Frenkel pair": close pair 6.8–7.5 eV (s19-1 l.67) gives 17–19; acceptable but "about twenty times" would be exact.
- l.27–31 Y_q, F_NR values at 0.10/0.22/0.46 keV → CHECKED (s19-2 l.102; s19-4 l.64). n ≥ 1112 → CHECKED. The 3.8 eV per pair is the source convention and the text converts → CHECKED (book ε_eh 3.75 eV, ε_cal 3.82 eV for CDMS II only).
- l.29 conversion through P_casc of app:E.13/E.24, not division by ε_eh → CHECKED (s19-1 l.132).
- l.41–45 eq:E.23-fA: ∫d²ρ n³ = λ³/3π²s², f_A = Cλ²/(12π²Dr²), dimensionless → CHECKED.
- l.53 0.1 eV per atom, an estimate → CHECKED (s19-6 l.86).
- Pointers from Ch19/Ch16/Ch20/Ch22 to app:E.23 (s19-1 l.97, l.107, l.132; s19-2 l.80, l.128; s19-3 l.97; s19-4 l.20; s19-6 l.86, l.88; s16-6 l.55; s20-2 l.16; s22-1 l.47) → CHECKED, each matched by a subsection.

## E.24 Electron cascades

- l.3 → see #1, #2. GAP (minor): the opening says no first-principles calculation reaches the silicon precision but omits the book's own full-band reference, 4.15 eV [3.95, 4.73] with a class systematic ≥ ±0.4 eV and 0.6 eV unexplained against Nielsen–Fischetti's 3.50 eV (s18-4 l.16, s18-summary). One sentence would tie the spec to Ch18.
- l.7 grid, temperatures, G₀W₀ + RPA, n_g = 2 → CHECKED against sec:18.1–18.4.
- l.9 Ge (and GaAs) bands → GAP (G1): G₀W₀ on Quantum ESPRESSO (PBE) ground states is prescribed for Ge with SOC without the check that app:E.14 l.62 now requires (L below Γ, both gaps within 0.1 eV, m*_⊥ at L and m_Γ). PBE makes Ge a metal at its own lattice constant (E.1 l.147); HSE06+SOC fails the check (DC-2); DFT+α fails the masses (DC-2-alpha). Require the E.14 check on the quasiparticle bands before any Ge cascade, and name the starting point.
- l.9 plasmon value → see #4.
- l.9 GaAs ionic part "from the Born charges and ε∞ (app:E.4)" → GAP (G2): DC-91 GaAs failed control (do not use computed ε∞ 21.8 or ω_LO); s5-5 l.132 says the measured LO–TO splitting is the safer input. State: measured ε∞ and Z*²/ε∞ from the splitting (0.194, s11-9 l.100) for GaAs.
- l.11 estimator and 8×10⁴ samples → CHECKED.
- l.13 Si validation 3.749 ± 0.001 eV, 0.119 ± 0.002 at 123 K → CHECKED (tab:18-pairs). Ge pair energy at 77 K an input → CHECKED (tab:18-pairs, E_g 0.735, 2.96 eV).
- l.15 memory 72×300²×200×16 B ≈ 21 GB → CHECKED.
- l.21 DFT full-band 7.3/7.8 (4H-SiC), 6.6/6.9 (3C-SiC), 16.7/18.0 (SiO₂) → CHECKED (tab:18-valid; 4H measured 7.83 ± 0.02). "a few to 15 % below" → fine for these three; Ch18 notes it does better than the model for diamond, 3C-SiC, GaN.
- l.25 z_qp argument → see #3. With the book set: ΔA_AB = 0.25×5.703 = 1.43 eV³, 0.076×1.43 = 0.11 eV, 2.9 %: the conclusion (≈3 %, removed by recalibration, s18-5 l.125) stands.
- l.36 w_mem → CHECKED against s18-1 l.104 (estimate Γ_E/Γ_k, E-24 specifies the bound).
- l.42–49 library: DC-67 (library not releasable; no tables quoted) → CHECKED, E-24 quotes no table. GAP (G3): DC-67 / REF-DC-67 §8 quotable facts are not stated where the spec matches to "the asymptotic Gaussian" at 20E_g: absolute pointwise error falls as C/x (Si C ≈ 0.24, x in units of E_g, so ≈1.2×10⁻² at 20E_g), relative skewness as x^{-1/2}; sample the lattice Gaussian at the integers (unit-bin integration adds 1/12 to the variance); add the Edgeworth terms beyond the table. Also state that the reader must return the exact value below θ_ii and add a row at the jump (the failure mode found).
- l.49 "Richardson-extrapolated from h and h/2" → GAP (G4): with phonons the error falls as h^{3/2}; extrapolate as f(h/2) + [f(h/2) − f(h)]/(2^{3/2} − 1) (app:D.43 l.74). As written a reader would use the h² formula.
- l.49 h = Eg/50, 20E_g, 12 meV of the 63 meV phonon → CHECKED (s21-6 l.17; 0.01×1.16 eV).
- l.42 library contents → GAP (G5): s21-6 l.17 says "the same tables carry the marks 𝔪 ... phonon spectrum, separate electron and hole counts, carrier positions and the stored energy". E-24 tabulates only P_casc. Specify the marks columns or change Ch21.6.
- l.53–57 exciton and capture → CHECKED: 14.7 meV (s4-9), binomial thinning ε → ε/(1 − f), F → (1 − f)F + f (algebra checked). GAP (G6): s18-5 l.72 says the cascade calculation must supply the end-of-cascade pair separations (against r_𝓔), and tab:22-gaps l.122 credits app:E.24 with "computed capture probability f(x), terminal-energy distribution and final pair separations". E-24 names the end-of-cascade energy distribution only implicitly and pair separations not at all. Add both outputs to the silicon cascade.
- Pointers from Ch18/Ch21/Ch22 (s18-1 l.104, l.137; s18-2 l.28; s18-3 l.7, l.34, l.110; s18-4 l.16, l.178; s18-5 l.72, l.121, l.125; s21-6 l.17, l.37, l.59; s21-7 l.49; s22-1 l.48–50) → CHECKED apart from G5, G6.

## E.25 Event-level transport

- l.3 27 pairs at 3.75 eV → CHECKED (book ε_eh convention). Verdicts pointer → see #7.
- l.7 fields 0, 1, 4, 40 V/cm; thresholds 0.3–16 eV → CHECKED (s19-5 two-bias 4 and 40 V).
- l.9 → see #6.
- l.11 Y_ph = 0.952 (+0.009 −0.007, 95 %) at 4 V/cm; (6.08 ± 0.18) % → CHECKED (s19-5 l.159, l.178; s19-4 l.81).
- l.17 → see #5. 12.7 % trapping; 5 to 10 hours → CHECKED (s20-1 l.142). Notation: Ch20 writes n_sh and ξ_SC; E-25 writes n_s and "largest field change". Align.
- l.19 P donor 45 meV, 10.9 THz phonons below 1 ns (A_anh ν⁵ gives 0.88 ns) → CHECKED (s20-2 l.104; s22-2 l.138). 216-atom cell 1.6 nm → CHECKED.
- l.25 2p(1 − p)(z/ΔP)² = 2×10⁴ → CHECKED.
- l.37–43 kernels: 0.41–62 meV = 0.1–15 THz; 2Δ 3.0 and 0.36 meV; ϖ_O 0.02–0.39 for 4.7 down to 1.5 meV; loss 10⁻³ per bounce → CHECKED (s20-5 l.44, l.57; s20-summary l.36). 𝔯_coll final band 0.81–1.02 not quoted here; nothing contradicts it → CHECKED.
- l.55 ρ_g − 1 = 0.21, 0.048 beyond 0.006, ±0.02, two-bias inversion and third bias → CHECKED (s19-5 l.174, l.185, l.207).
- l.61 1.31 factor; l.63 37.7°, 56 %, E₃ form, 3–13 % (recomputed 3.0 % at 0.01, 13.4 % at 0.2), 0.3–0.55 as absorption probability → CHECKED (s20-3 l.37, l.78, l.109–116, l.130, l.146, l.161).
- l.61–63 interface → GAP (G11): the book uses one Al set, the 0 K isotropic (Voigt) constants 6.63/3.30 km/s at 2.70 g/cm³, giving t̄_esc 0.368 (acoustic), 0.282 (diffuse) (SPINE Ch20 row; s20-3). The spec offers "measurement or finite-strain DFT" without saying which; make the 0 K measured constants primary, require the isotropic limit to return 0.368/0.282, and use Ch20's [100]/[111] silicon-speed sensitivity (0.327–0.405, s20-3 l.155) as the bracket the anisotropic result must be compared with.
- l.67 Y_qp tests: 2Δ/E below 4Δ, asymptote 0.57–0.6, 200Δ for 36 meV Ge phonons → CHECKED (s20-4 l.77, l.111). Suggest also the book's own kinetic value 0.590 (max 0.600 at 5.46Δ) as the sharper target. Citation location: Ch20 cites guruswamy2014 [p. 2]; E-25 [Sect. I]; align.
- Costs: 2×10¹² steps / 140 core-h and 10¹¹ / 8 core-h imply the same ~4×10⁶ steps/s/core → CHECKED.
- Pointers from Ch18/19/20/22 (s18-5 l.94, l.121; s19-5 l.42, l.80, l.151, l.174, l.193, l.207, l.209; s19-6 l.88, l.183, l.198; s20-1 l.178, l.182; s20-2 l.34; s20-3 l.155; s20-5 l.28, l.80; s22-1 l.53–54; s22-2 l.132–142) → CHECKED; each has a matching subsection (film validation answers s20-1 l.182).
- Outside scope, noted only: s16-8 l.51 (Fig. caption) uses c_TA = 3.40 km/s and 2.73 g/cm³ for aluminum "(sec:15.4)", not the one 0 K set (3.30, 2.70) of Ch20.

## E.26 Coherent and second-order absorption

- l.3 t_coh = 1/(m v₀²) ≈ 1.04 ms, 249 m at 1 µeV with v₀ = 238 km/s → CHECKED (s1-2 l.21; s14-6 l.28).
- l.7 regime statement and scalings → CHECKED against s14-6.
- l.9 orientation factor 1, 3ε₀/(ε₀ + 2), ε₀ → CHECKED (s11-8 l.121). Lattice-constant benchmark −1 → CHECKED (eq:11.8-h). Copper shift → see #11.
- l.11 grid (1 + 3.5×10⁻⁶)m_φ (v_max ≈ 794 km/s) → CHECKED. 1.99 and 2.7, up to 10 → CHECKED (s14-6 l.159–173; 2.73 there).
- l.15 → see #10. l.17 → see #8, #9.
- l.21 pair absorption: 0.39 → 0.3 GeV cm⁻³ gives 0.59 → CHECKED (s10-8 l.30, factor 1.69). Thomson-limit form and σ_Th = e⁴/6πm_e² → CHECKED (eq:10.8-thomson). GAP (G12): the pseudoscalar route uses the axioelectric (spin-current) row; s10-8 l.51 and Ch15.4 attach caveats (measured σ₁ belongs to singlet pairs while the row creates triplets; spin–orbit spoils the factor ¾; the spin-current result holds under the three conditions of 15.4). Add one clause so the acceptance test is not read as validating the row itself.
- Pointers from Ch10/11/14/22 (s10-8 l.84, l.174; s10-9 l.182, l.232; s10-10 l.94; s11-8 l.177; s14-6 l.109; s22-1 l.73; s22-2 l.54–56) → CHECKED.

## E.27 Halo, background and nuclear-spin inputs

- l.7 notation map to sec:21.2 and app:C.12 (𝔎 = 𝗄, F = Ξ, 𝔥 = 𝖿, ξ = λ) → CHECKED (s21-2 l.13, l.22).
- l.13 at most as many streams as bins → CHECKED (s21-2 l.22).
- l.15 768 × 55 × 24 ≈ 10⁶ columns; ~4×10⁴ LP variables; 55 speeds to 544 km/s → CHECKED.
- l.17 single-bin relation N/inf_{v≥u₀}[v𝔎_i(v)] in the laboratory frame only; weak duality survives negative pieces, mass bound fails, sec:21.2-leak → CHECKED (s21-2 l.44; SPINE Ch21 row "one kernel relation").
- l.17 Bonferroni per-bin confidence → CHECKED: Ch21.2 l.24 uses the same union bound; it is not a second statistical construction (Ch21's single Neyman construction concerns the profiled nuisances).
- l.21 tritium: 124 ± 25 kg⁻¹ d⁻¹, 12.3 y, f_β 8.9 %, 0.17 and 11 → CHECKED (s21-7 l.104: 0.169, 11.0; recomputed). ²¹⁰Pb (724 per kg d keV per Bq/kg, 1.38 mBq/kg) is not quoted in E-27 and need not be.
- l.23 Ge tritium model span 27.7–210 → CHECKED as a source quote; Ch21.7 uses the measured 82.
- l.27–29 spin weights J(J+1)/3, c₄ with ⟨S_p⟩, ⟨S_n⟩; ²⁹Si 0.156/0.016, ⁷³Ge 0.439/0.031 (second interaction 0.450/0.006) → CHECKED (s8-1 l.119, l.124; s11-6 l.52, l.179).
- Pointers from Ch11/21/22 (s11-6 l.179; s11-9 l.27, l.33; s21-2 l.97; s21-6 l.21, l.40; s21-7 l.99, l.104, l.145; s22-2 l.148) → CHECKED.

## Compute record (DC-RESULTS) cross-check

- DC-2 / DC-2-alpha: E-21..27 never prescribe HSE06+SOC or DFT+α for Ge bands → CHECKED; but G1 (E-24 Ge G₀W₀ without the E.14 check) and G9 (E-23 HSE arm in Ge) remain; #16, #17 fix E.15 l.56 and E.1 l.147.
- DC-41: not used in E-21..27 → n/a.
- DC-67: no library table or accuracy number quoted → CHECKED; tail law missing (G3).
- DC-91: GaAs ε∞ 21.8 not quoted → CHECKED; route still points to computed ε∞ (G2).
- DC-93, DC-49/54/36: not used in E-21..27 → n/a.

## Process words and labels

- BANNED-TERMS regex over E-21..27: no matches. No DC-, LE-, XG-, CW, WP, [CALC], "thread", "brief", "audit" → CHECKED.
