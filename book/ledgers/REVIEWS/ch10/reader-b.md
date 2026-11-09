# Chapter 10 mock-reader review: reader b (personas b and c)

Source: build/main.pdf (Nov 1 23:46) is older than every ch10 source (Nov 2), so I read tex/ch10/*.tex and appD/D-29.tex, D-30.tex linearly. Checked against Chs 1–8 only where Ch10 cites them (grep).
Checks: sympy/numpy in the scratchpad. These include a 4x4 Dirac-matrix evaluation of the dark-Compton amplitudes, the Lindhard plasmon zero, the halo tail and the series of eq. 10.8-series.

## Persona (b): particle physicist, QFT yes, solid state no

### Per section
**10.1 Crystal form factor.**
- Lost points: none blocking. Ch3–4 vocabulary (scissor, Umklapp, "head" of the bubble) carries the section; I followed it only because I had read those chapters.
- Reproduced: eq. 10.1-S0 (2π · spin 2 · Σ_k → V∫); eq. 10.1-rateiso from eq. 10.1-rate (∫dΩ δ = 2π/qv → q dq η/4π²); the box via eq. 10.1-fcrys with ρ_TΩ = M_cell; |f|² = q⁵Ωε₂/8π²α²m_e²; the WE prefactor 2.45e5 kg⁻¹yr⁻¹ (I get 2.453e5).
- Not reproduced: box text and caption say "kinematic edge, q = 0.55 q₀" at 5 eV and 10 MeV. Solving ω/q + q/2m_χ = v_max gives q = 1.96 keV = **0.525 q₀**; even the bin centre does not give 0.55.
- Pace: right. Outcome (derive the rate, convert the normalizations; the Griffin S⁰/2 and code-weight conversions check against D.29): yes.

**10.2 Screening, loss-function rate.**
- Lost point 1: 10.1 gives an IP rate of 1.60e5 with mean 6.0 eV; 10.2 gives "IP" 1.36e5 with mean 6.2 eV, and does not say these are two different tabulations. I thought I had erred until 10.10 explained the "tabulation spread". A one-clause forward pointer in 10.2 would fix it.
- Lost point 2: the last sentence of the relaxing-lattice paragraph ("the coupling carried by a unit volume, which vanishes for the charge, is c₁^(e)n_e here") is opaque.
- Reproduced: S = (2q²/e²)L and the prefactor 1/8π²α; Hölder K_n and eq. 10.2-bound (π/2 → 1/16π); the (0,1] eigenvalue argument, including the TDDFT condition (−R⁰)⁻¹ + f_xc > 0; S_ee^ac with its first and inverse moments; Ω_{P,e} = 0.514 eV, crossing at 18.3 keV, 3.3e2 at 1 keV; ω_p = 31.1 eV; r_s = 2.0; the Cappellini values 0.12 and 0.45.
- Pace: dense but fair. Outcomes (loss-function rate; why 2.3 is not 1/ε²; the bounds; why the bound fails for electrophilic mediators): yes.
- In my field: the dark-photon remark (vacuum ζ with the full response, not ζ_eff² on top of L) is correct and well put.

**10.3 Electron gas, plasmon.**
- Reproduced: k_TF² = 3ω_p²/v_F² and the static-limit low-ω L; Z_L and the first moment of the line; v_th = 9.53e-3 (2860 km/s; 2750 km/s quadratic); the quadratic cutoff 2.24 keV and 20.6 eV; the ω_p-fixed value 1.88 keV; the Lindhard q_c ≈ 2.60 keV and 24.8 eV (numerically); the Kurinsky logs 1.24 and 1.31; the Maxwell tail 3.7e-49 and 1.8e-53.
- Closest approach 14.7 eV at 1.34 keV: reproduced only with the exact Lindhard zero; the quadratic dispersion gives 14.5 eV at 1.72 keV. The text should say which dispersion it uses.
- Pace: the Z_L derivation is textbook for me but right for (a). Outcome (show the plasmon is unreachable, and by how much): yes.
- In my field: calling Z_L "the residue of the longitudinal photon propagator" is accurate.

**10.4 Spin, current, velocity couplings.**
- Reproduced: 17 rows and 289 elements; triplet = ¼ singlet spin trace; the optical ratio 2ω²|ε|²/q² (S_jj = 2ω²ε₂/e² per component); η₂ ≡ ∫f(v²−v_min²)/v with |v̄_T|² = v² − v_min² on the shell; the prefactor 1/16π² of eq. 10.4-O8; r > 4 → lower edge above 1; r_med 41–76, lower edge 29–60; the Catena dictionary (via D.30).
- Not reproduced:
  - WE 10-band: (√25.3 − 1)² = **16.24, not 16.3**. The "at least 16" downstream is fine.
  - The text says the half-width is below 10% "only for r < 2.4e-3". Solving 2√r/(1+r) < 0.1 gives **2.5e-3**, as D.30 states. The 2.4e-3 is the figure's different criterion, (√r+1)² ≤ 1.1; the two are mixed up.
- Lost point: O₁…O₁₅ are cited by number only; I flipped to Tab. 8.x for each one.
- Outcome (pick the rows for an operator, say which are screened, bound an uncomputed cross term): yes.

**10.5 Excitons at finite q.**
- Reproduced: line-sum continuity at the edge (1/(2πa_x³E_b) from both sides); ε = (6πζ(3))^{2/3}E_b = 8.0E_b (7.1E_b for 1s alone); 1/(πa_x³) = 4.3e-6 Å⁻³; R_n1 near the origin and |g·∇F|²; the 2p/1s suppression g²/32a_x²ρ² ≈ 1.4e-3; the Γ-function identity; the TDA ratio (E₀+ω)/2E₀ with the 3.4, 2.23 and 2.12 checks; the RPA/TDA static ratio (Δ+2K)/(Δ+K).
- Not reproduced: the Fermi factor "falls to 2.6 at 10E_b". 2πξ/(1−e^{−2πξ}) at ξ = 1/√10 is **2.30**. 2.6 is the value at ≈6.8E_b, i.e. the 1.27 eV of WE 10-xline, where 2.6 is correct.
- Too fast: the nonsymmorphic phase argument ("e^{−iq·τ₂} cancels that of the conduction state") and the Γ₂₅′ label, which Chs 1–8 never define (it is only glossed here). I followed the logic but could not verify it.
- Outcome (onset lines, second-class rule, TDA pitfall): yes, except the glide argument.

**10.6 Core and relativistic.**
- Reproduced: closure of eq. 10.6-Sat (∫p dp = 2kq); the near-opening N^acc (2√2/3) factor; S^at = q²Ωε₂/8π²α; openings 11.30 and 11.53 keV, masses 8.53 and 8.70 MeV; m_χ ≥ 25 MeV (19 at 13 keV) and the 10 MeV window 16–37 keV; screening 0.0128; q²/4m² at 11.3, 30 and 46 keV; ⟨v²⟩; δ_mv −1.83e-3 and −5.76e-3; the orbit–orbit double commutator (sign and 4/3); the FT of T_ij and its transversality; totals −0.24% and −0.76%; Dirac s-state factors 1.0009 and 1.13.
- In my field: the FW density vertex and ψ̄ψ → n − T/m (twice |ψ_B|² = T/m) are correct. "Ge, Sheng and Xing showed… the free-electron amplitude … can turn negative" is too terse: say it is the squared amplitude evaluated at bound kinematics.
- Outcome: yes.

**10.7 Absorption.**
- Reproduced: Γ_T/Γ_L = 1 + v²(2Re(1/ε) − 1) to first order; the WE numbers (|ε|² = 5.138, L = 0.2468, Π = 288 − 127i, 6.76, R = 1.52e33ζ² vs 7.83e33ζ², ζ = 4.4e-17 and 2.0e-17, v² term −1.7e-6); the ALP spin trace 3/4 and Γ_ALP; ALP/DP 1.6e-8; the E·B derivation, (ε⁻¹)†ε″ε⁻¹, B₀ = 1953 eV², ζ_eq = 1.95e-17, 0.58 events; the uniaxial identity eq. 10.7-aniso; [[p²,V],V] = −2|∇V|² and eq. 10.7-sumrule; "four orders" (ALP ≈ 2.5e25g² vs 9.8e29g²).
- Minor: |ε|² at 3 eV is 761 here and 770 in 10.4 (which quotes §8.4). Pick one, or say that 770 is the rounded-L value.
- Outcome: yes. In my field: the parity/handedness no-mixing argument for the pseudoscalar is right; Π_L = (ω² − p²)(1 − ε) gives m²ε exactly.

**10.8 Two insertions.**
- Reproduced: Thomson eq. 10.8-thomson (the 1/6π assembles); eq. 10.8-series (−15/4 vs −35/8; −17/4 with exact ω_γ); 0.29% at 100 keV, 1% and 10% at 165 and 516 keV; the phase space Γ = n|M|²ω_γ/16πm m_e(m+m_e) (√s = m + m_e, p_f = ω_γ); ξ = 44.81 and the cut share 0.99415; ⟨|v−v̄|²⟩^{1/2} = 403 km/s; g_eff = 1.28e-21; G_S = 1.37e6 G_F and Λ ≈ 0.25 GeV; the WE ALP numbers 1.34e-25, 2.46e-25 and 1.62e-25 cm²; the Si and Ge K thresholds at 45 and 118 keV.
- Independent check: I evaluated Σ|M|² for V e → γ e and for a e → γ e (vertex gγ⁵) with explicit Dirac matrices.
  - The vector |M|² = (4/3)e⁴ζ²(m²+2mm_e+2m_e²)/m_e(m+m_e) is correct to machine precision at x = 0.01–3.
  - **The book's eq. 10.8-alpC is correct at every x**, so the factor (m+2m_e)/(m+m_e) against the published form stands, as far as the trace goes. The NR seagull (derivative coupling) agreeing at leading order is consistent with the γ⁵ ↔ ∂γ⁵ equivalence for one ALP.
- Too slow for me: box quantization of φ (fine for (a)). Too fast: §10.8-rate's "the four-point function collapses to a two-point function" when the denominators are off shell; one sentence on why (a static polarizability vertex) would help.
- Outcome: yes.

**10.9 Inelastic, exothermic, boosted, fermionic.**
- Reproduced:
  - endothermic masses 0.60 and 3.2 MeV; the shell integral 4πm k* G and eq. 10.9-shell (prefactor 1/4π²α); the q_Δ⁻¹ edge;
  - ω_line, q_line and all WE 10-exo values (1.64/3.70/6.62/8.54 eV; 1.29–3.20 keV; v_max/v_Δ = 0.34/0.53/0.94/1.97);
  - the trace (2E−ω)² − Q²; the conserved-current split giving (1 − ω²/Q²); ω ≤ vQ, 2%, 9%; Cherenkov thresholds 0.28 and 0.15;
  - the fermionic traces k·p; the tensor D^{00}, D^{0i}, D^{ij}; (1 + ω/q)² = (m/q)²; eq. 10.9-ferm (both lines); the expansion of r (eq. 10.9-ratio); t = 2m_χω − m_χ²;
  - Γ_vac = μ²Δ³/π; n_r³ in a transparent medium; the n_r vs n_r³ argument.
- In my field: all correct. Two small points:
  - "up to the sign convention of the antisymmetric term" is honest. One line on why that term is dropped for a P-symmetric unmagnetized target would read better before the trace than after it.
  - Notation clash: n_g is the group index here (near eq. 10.9-decay) and the electron–phonon order of the truncation label (Tab. 10-nuisances, Ch8).
- Outcome: yes.

**10.10 Uncertainties.**
- Reproduced: ln(1+δ) = 0.247, 0.289, −0.078, 0.065; σ = 0.393, band 1.19–2.62e4, 93% of the variance; 1.65 with δ = 0.49; 2.27e4 at ϑ = 1; m_min 0.316 → 0.333 MeV; 8.5%.
- Outcome (build the band from the table): yes.

### Persona (b) summary
- Nothing blocks. Every derivation in my field checks, and the two published-formula corrections (ALP Compton, boosted density row) are sound.
- The solid-state load is heavy in 10.2 and 10.5; it is manageable only because Chs 3–4 are behind me.
- Condescension: none. The Dirac-trace identities (10.9) are spelled out more than I need, but they are not patronizing.
- **Verdict (b): MINOR GAPS.**

## Persona (c): condensed-matter theorist, DFT/MBPT yes, dark matter no

### Per section
**10.1.**
- Used before defined (for me): η, v_min, F_DM, σ̄_e, v_max, ρ_χ, and q₀ as "α m_e". All are defined in Ch1 and the text cites the equations; acceptable.
- In my field: scissor, PBE, 52 bands, 70 Ry and the PAW/all-electron caveat at q > 2q₀ are all stated correctly. The f-sum check (1.03 at q₀; 1.1–1.2 at small q; scissor ≈ 10%) is exactly the test I would ask for.
- Minor: 10.1 calls 1.11 eV "the room-temperature value", but 10.7 gives the gap at 300 K as 1.12 eV. Harmonize. Outcome: yes.

**10.2.**
- In my field: correct throughout. The (ε⁻¹)_GG ∈ (0,1] proof via eigenvalues of X(1−X)⁻¹ is clean; the r_s ≈ 5.25 compressibility remark and the Dolgov–Kirzhnits–Maksimov caveat are right. The explanation that a q = q_r + G density wave induces q_r charge, which local fields capture, is the right physics and well put.
- Too slow for me: the Hölder exposition (right for (a)). Outcome: yes.

**10.3.** Correct. The Mermin "fit parameter, not a collision rate" caveat is appreciated; so are the scissor pushing the plasmon up and the Landau damping in the residue. Outcome: yes.

**10.4.**
- In my field: PT reality, the spin-singlet/triplet block split and "triplet keeps K^d, loses K^x" are correct. The nonlocal-pseudopotential commutator on the current vertex (~10%) is a good catch.
- **Cross-chapter contradiction:** Ch8 Tab. (s8-4, row "Transverse current, spin current, T_e") puts the *spin current* and *T_e* in the local-fields-only class. 10.4 and D.30 (correctly, in my view) say the spin current, a triplet row, is not screened at all, and T_e, a scalar, is screened at the head. Ch8's own spin-density row already says "none". A reader who trusts the Ch8 table is misled; fix Ch8.
- Outcome: yes.

**10.5.**
- In my field: the Elliott/Wannier treatment, the second-class 2p rule and the TDA/retarded-TDA/coupling-block distinction are correct and unusually careful. The (a/a_x)³ ≈ 2e-3 exchange-splitting estimate is sound.
- **Suspect claim:** "NaI, whose optical exciton is bound about a thousand times more strongly than that of GaAs". GaAs E_b ≈ 4 meV, so ×1000 would be ≈ 4 eV, close to NaI's gap itself. Literature values for NaI are a few tenths of an eV, roughly ×100. Check the source or soften.
- Not reproduced: the Fermi factor 2.6 at 10E_b (see b). Outcome: yes.

**10.6.**
- In my field: the projector argument for core/valence separation is right and nicely basis-free. The Ge 3d doublet of 0.6 eV and flatness per j are correct, and the plane-wave non-orthogonality caveat is good.
- Too fast: the Dirac/FW machinery (§10.6-rel, eq. 10.6-oo). I followed it via Ch3 and App C.15 but could not check App C.15's vertex independently.
- Outcome: yes.

**10.7.**
- In my field: the 300 K vs mK edge discussion (n_TA = 0.97 at 300 K, edge 1.1736 eV) is correct and important. So are the parity rule of the kinetic row at Γ (Γ₂₅′ even, Γ₁₅ odd) and the polar-point-group argument (O_h, T_d, D_3d nonpolar; wurtzite polar).
- Lost point: the ALP coupling (g_aee/m_e)[(∇φ)·s + (∂_tφ)J] is quoted from eq. 8.1-alp without a reminder of what J^{αα} is physically; I had to go back.
- Outcome: yes.

**10.8.**
- Too fast for me: writing a Lagrangian with a derivative coupling as "H_int" (sign, and canonical-momentum subtleties of i φ†∂φ) passes without comment, as do "dimension-six operators" with an explicit m_e factor on the scalar.
- Lost point: the dark-Compton matrix-element step ("a standard Dirac trace… Hochberg et al. evaluated") is outside my field; I took "exact tree level" on trust. Persona (b)'s numerical check confirms it.
- Outcome: partly. I can reproduce the Thomson limit, the pair-absorption mapping and the WE numbers, but not the trace.

**10.9.**
- Lost point: the fermionic-absorption tensor (chirality projectors, ε^{μναβ} term "up to sign convention") is outside my field; the result D^{μν} is checkable once given. The boosted-DM flux (D_eff, line-of-sight integral) is stated, not derived; fine, since the book takes it from the literature.
- In my field: the Cherenkov window in transparent silicon and the transverse ε^T are correct. So is the n_r³ vs n_r Purcell-type argument, which I reproduced with DOS ∝ n²n_g and E² ∝ 1/(n n_g).
- Outcome: yes for the inelastic, exothermic and decay parts; partly for the fermionic part.

**10.10.**
- In my field: the rung-spread vs next-rung distinction is the right philosophy, and the 0.1 eV state-to-state QP spread is reasonable.
- **Unargued step:** the IP "tabulation spread" (+0.335) is applied multiplicatively to the RPA+LF central value. Whether an IP discrepancy concentrated at small q survives screening unchanged (screening is strongest exactly there) is not shown. Either evaluate the spread of the screened rates or say why the IP ratio is a fair proxy.
- Outcome: yes.

### Persona (c) summary
- No blocking item. The physics in my field is correct and often sharper than the DM literature it corrects.
- Dark-matter-side inputs (η, v_min, F_DM, operator numbers, boosted fluxes) are cited rather than recalled; that works only for a reader with Ch1/Ch8 open.
- Condescension: none. Hölder, Lindhard and the positivity proofs are over-explained for me but not patronizing.
- **Verdict (c): MINOR GAPS.**

## Consolidated fix list (all minor; none blocks later material)
1. 10.1 box/caption: kinematic edge at 5 eV, 10 MeV is 0.525 q₀, not 0.55 q₀.
2. 10.4 text: 2.4e-3 → 2.5e-3 (agree with D.30), or state the (√r+1)² ≤ 1.1 criterion of the figure.
3. WE 10-band: (5.03 − 1)² = 16.2, not 16.3.
4. 10.5: Fermi factor at 10E_b is 2.3 (2.6 is at ≈7E_b).
5. |ε(3 eV)|² is 761 (10.7) vs 770 (10.4 / Ch8).
6. Daily modulation is cited as §11.7 (10.1, 10.4, Tab. 10-nuisances) and as §1.2 (10.2); Ch1 says Ch10 treats it.
7. 10.2: flag that its IP rate (1.36e5) is a different tabulation from 10.1's (1.60e5); forward-point to §10.10.
8. Ch8 Tab. s8-4 lumps the spin current and T_e with the transverse current; 10.4 and D.30 contradict it.
9. NaI exciton binding "≈1000× GaAs": check.
10. n_g used for both the group index (10.9) and the label component (10.10).
11. 10.3 WE: say that 14.7 eV at 1.34 keV uses the exact Lindhard zero.
12. 10.10: justify carrying the IP tabulation spread onto the screened rate.
13. 1.11 eV "room-temperature value" (10.1) vs 1.12 eV at 300 K (10.7).

## Overall verdict: MINOR GAPS
Both personas would keep reading. Every derivation either can check reproduces, apart from the numerical slips above. The table- and model-derived rates cannot be checked without the data and were taken on trust.
