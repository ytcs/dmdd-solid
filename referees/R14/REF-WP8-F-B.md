# R14 referee REF-WP8-F-B (hostile, isolated): returns/R13/WP8-F.md

Scope: the return, `code/WP8-F/checks.py` (rerun: **39/39 PASS, ≈ 2 s**, reproduced), and only the inputs the brief allows: returns/R8/*-v3, R12 WP7-T-v2 and
WP7-E-v3 (quotes), R13/WP5-v4 (ε_eh only), CONVENTIONS, NOTATION, CONTROLS, DONE, LIMITS, STATEMENT. Full texts fetched with lit.py into
literature/papers-r14-REF-WP8-F-B/ (PDFs deleted): 1807.10291 (v1), 1910.08092, 1706.05818, 2506.06568, 2205.02250. JARVIS OPTIMADE queried live
(chemical_formula_reduced filter) for Si, Ge, GaAs, SiC, Al₂O₃, AlN, GaN, MgO, NaI, NiO, CsI, Y₃Fe₅O₁₂. Checks in this report: sympy/numpy, < 1 s.

## Verdict table
| # | Main claim | Verdict | Reason (details in §§1–8) |
|---|---|---|---|
| V1 | (1.1)–(1.2): rate FOM = material functional S̄/ρ_T × kinematic factor 𝒦 = qF²η/(4π²), as a limit of tr[𝔇ᵀS] | STANDS WITH CORRECTION | η/(2q) and prefactor agree with WP0-v3 (3.4) and CONVENTIONS §8; but 𝒦 ∝ η holds only for v-independent 𝔇 (𝔇^{(1)} = 𝔇^{(2)} = 0). Rows with v_T dependence (𝒪₃, 𝒪₇, 𝒪₈, …) need other halo moments (§1) |
| V2 | (1.2) edge vocabulary; near-edge log-sensitivity ≈ 132 | STANDS WITH CORRECTION | Edges agree with WP6-v3 (3.1)/(3.1′). 132 is right for the continuum (p̄_on = 3) at 1.05 m_min, which is the edge of the 1–5% validity window. The Si exciton replica has p̄_on = 3/2 (WP6-v3 table), so ≈ 101 there. §2.7(e) applies "p̄_on = 3" to all of PAER |
| V3 | ER-ρ (2.1a) q-weights; f-sum ceiling; Z/A ∈ [0.40, 0.50] "for inorganic targets" | STANDS WITH CORRECTION | (2.1a) re-derived. The Z/A range holds for the 12 listed targets only: Pb 0.396, Bi 0.397, U 0.387, LiH 0.503, H₂O 0.555. "𝓡_ER,heavy ∝ (Z/A)·w_acc" is not derived: the heavy weight is ∫dω L (no ω), the f-sum is ∫dω ωL, so a ⟨1/ω⟩_acc factor is missing |
| V4 | ER-light FOM "is the optical ELF per mass" | STANDS WITH CORRECTION | Correct as a reduction under the stated slow-variation hypothesis. But the ∫dq/q weight puts ≳ ½ of the log at q ≳ 1 keV for m_χ ≳ 0.5 MeV, where L(q,ω) ≠ L(0,ω) in Si. Downgrade to [E] above ≈ 0.5 MeV |
| V5 | ABS: FOM_A′ = L(0,m_φ)/ρ_T; ALP ∝ m_φ²ε₂/ρ_T; scalar Im Π_φφ/ρ_T; polarisation average; SC and Dirac statements | STANDS | Matches WP0-v3 (3.5)–(3.6) and L9b/L16; C11 re-derived. Exception: ALP–photon (V5b) |
| V5b | "ALP in B₀: FOM_A′ applies, × B₀²" | STANDS WITH CORRECTION | WP0-v3 (2.9): Γ = g²B₀²Im[−1/ε_∥]/m_φ, so the rate per mass is ρ_φg²B₀²L_∥/(ρ_Tm_φ²): × B₀²/m_φ², with L along B₀ (not polarisation-averaged) |
| V6 | NR-1ph (2.3a): per-mass coherent LA = πq/(m_u²c_LA), A- and composition-free | STANDS WITH CORRECTION | Algebra is right, and equals 2205.02250 Eq. (30) per mass [FT, CONFIRMED]. But (i) the optical-branch statement is wrong (§2); (ii) §0's "(A₁ − A₂)²-suppressed" is wrong; (iii) the per-mass formula and the §5.1 scalar hold for the heavy mediator only at m_χ ≲ 0.1–1 MeV, not over the claimed 10 keV–10 MeV |
| V7 | (2.3b) m_min^{ac} = ω_th/(2c_LA(v_max − c_LA)); c_L table | STANDS | Re-derived (C2). DB inputs CONFIRMED for Si, GaAs, Ge, SiC, Al₂O₃, NaI. Diamond (JVASP-91) was not re-pulled |
| V7b | "DB c_T–c_L of GaAs (2.9–4.8) brackets c_s ∼ 4000 m/s (1807.10291 p.6)" (C12a) | FALLS | The source says "the **longitudinal** sound speed is c_s ∼ 4000 m/s" [FT p.6]. The right comparison is c_L(DB) = 4.82 vs 4.0 km/s: +20%. Bracketing with c_T is meaningless, and §5.2's "bracket FT 4.0" goes with it |
| V8 | NR-mph/impulse (2.4): first moment composition-free; zeroth moment ∝ ⟨A⟩; Poisson tail; free-NR edges | STANDS WITH CORRECTION | Moments re-derived (C1c); 104/137/220 MeV reproduced. "Impulse FOM per mass ∝ A" holds only well above threshold: E_R ≥ E_th cuts q ≥ √(2M_κE_th), which favours light nuclei near the edge. State this |
| V9 | POL (2.5a/b): 𝓡_pol ∝ 𝓘_pol/ρ_T; diatomic closed form; GaAs ≤ 0.144, sapphire 9.40 meV cm³/g; edges | STANDS WITH CORRECTION | (2.5b) and LST re-derived (C3). But 𝓡_pol = ∫dω L ln(q₊/q₋(ω))·η̄, not 𝓘_pol (sapphire branches differ by 15% at 1 MeV). "≤ 0.144" is not a bound: 34 meV is a DFT histogram range, and LST with the same FT ε forces ω_LO/ω_TO = 1.088; with ω_TO ≈ 33.3 meV [UNVERIFIED] this gives ≈ 0.153 and ≈ 10.3 keV (§3) |
| V10 | (8.1) KK bracket; DB-only brackets for Al₂O₃, AlN, MgO, GaN | STANDS WITH CORRECTION | Lossless single-axis proof is valid (re-derived). The DB application is not: the JARVIS `…max_dielectric_electronic/_ionic` fields are (by their naming) tensor maxima, not one principal axis, and the IR-mode range spans all polarisations, so for uniaxial Al₂O₃, AlN, GaN the "bracket" is heuristic. Only cubic MgO is rigorous |
| V11 | MAG (2.6): 𝓃_S/ρ_T scaling; edges "for gapless FM/AFM by the same algebra as (2.3b) [D]" | STANDS WITH CORRECTION | FM magnons are quadratic (ω = 𝔇_sw q²), not linear. (2.3b) applies to AFM (linear) branches only. FM: q ≤ v/(𝔇_sw + 1/2m_χ) gives a different m_min |
| V12 | PAER window, edges, onset exponent | STANDS | Agrees with WP6-v3 (3.1) table and consequences (ii)–(iii); see V2 for the replica exponent |
| V13 | Migdal (2.7), L-F3: 𝓡_Mig ∝ (A_κ²/M_κ³)μ_N⁴/μ_n²·Z_κ²𝓜_Mig; "Z_κ²/A_κ per mass, light nuclei win"; 10 MeV–1 GeV | STANDS WITH CORRECTION | Correct for elemental targets only. Compounds: ∝ Σ_κZ_κ(k)²/A_cell (§4). The regime label m_n ≪ m_χ is wrong for the dominant range and is not needed for the material scaling. A hypothesis ω ≪ μ_Nv²/2 is missing. The lower mass end is ≈ 17–21 MeV (impulse onset), not 10 MeV |
| V14 | TLS/defects/LEE proxies (§2.8) | STANDS | Quotes agree with L29, L32, L36 (as corrected), L38, WP7-T-v2 §2.4 (3.7×10⁻², [E ×3]) and WP7-E-v3 §3.3 (2.7 eV, N_a ≳ 270) |
| V15 | §3 reach scalars 𝓩_0, 𝓩_B, systematics floor | STANDS WITH CORRECTION | 𝓩_0 and 𝓩_B are right in the s ≪ b limit. The floor "σ_lim → Z f_sys b_bg/𝓡" is off by ΔE_ROI if b_bg is a rate density per energy, as §3 defines it. "σ_lim = 2.303/(𝓩_0MT)" omits the flux/σ̄ conversion (ρ_χπ/(m_χμ²)) that is excluded from 𝓡 by (1.2). C10d is tautological |
| V16 | §5.1/5.2 WP8-U property list "complete" | STANDS WITH CORRECTION | Missing items (§6): nuclear spin content (SD nucleon couplings), dynamical quadrupoles 𝒬_κ (Si/Ge POL), Ω/q_BZ (validity of (2.3a)), SOC strength (ALP, spin rows), Δ_χ (inelastic/exothermic class absent), phonon-assisted intra-cell geometry r_κ (optical NR-1ph) |
| V17 | §5.3 JARVIS vetting claims ("DB is wrong/unusable") | values CONFIRMED; rule (i) "MBJ within ≈ 10%" REFUTED | GaAs, NiO, MgO, NaI, CsI/YIG CONFIRMED live. The return's own pull refutes MBJ ≈ 10%: Ge 0.606 vs 0.744 eV (−19%), GaAs 1.321 vs ≈ 1.52 [UNVERIFIED] (−13%). Under-reported: NaI JVASP-1996 (0.28 cm⁻¹) and SiC JVASP-8158 (3.39 cm⁻¹) also fail rule (ii). GaAs gap 0.085 eV is "near-metallic", not "metallic" |
| V18 | FT quotes and provenance tags (§2.1(d), §2.3, §2.5, §6) | STANDS WITH CORRECTION | All numbers CONFIRMED against full text. Corrections: Eq. (40) is on PDF p.30, not p.31; the HTML vs PDF equation numbering of 1807.10291 is mixed (L-F2 "Eq. (32)" is HTML numbering = PDF Eq. (22)); sapphire ρ_T = 3.98 is untagged; ³H half-life is [FT] in 2506.06568 p.1 |
| V19 | Proposed LIMITS rows L-F1, L-F2, L-F3 | L-F1 and L-F2 STAND WITH CORRECTION; L-F3 STANDS WITH CORRECTION | §7 |

---
## 1. Factorisation and the rate FOM (V1)
Re-derived from WP0-v3 (3.4). For isotropic S̄: ∫d³v f δ(ω − ω_q) = η/(2q) (CONVENTIONS §8) and ∫d³q/(2π)³ → ∫q²dq/(2π²). This gives (1.2) and
𝒦 = qF²η/(4π²). With |𝒱|² = πσ̄_e/μ² it reproduces CONVENTIONS §8's (ρ_χσ̄_e/(4πm_χρ_Tμ²))∫q dq F²ηS̄ exactly. (2.1a) follows (q²L/(2πα) inserted; checked).
**Correction.** (1.2) assumes 𝔇_aa = |𝒱_a|²F²(q). By WP0-v3 (2.3) and WP6 (1.2), 𝔇 = 𝔇^{(0)} + 𝔇^{(1)}·v_T + v_T·𝔇^{(2)}·v_T. For any row with 𝔇^{(1,2)} ≠ 0 the velocity
integral is not η but a transverse moment (∫f v_T²δ, i.e. the WP6 (1.3) ξ-type functional). So 𝒦_a is operator-specific, and FOMs for 𝒪₃/𝒪₇/𝒪₈-type couplings
cannot be ranked with the 𝒦 of (1.2). Add "v-independent 𝔇" to the hypotheses of (1.2), and define 𝒦_a^{(2)} for the others. The non-diagonal tr[𝔇ᵀS] remark
(index order) is consistent with WP0-v3 A-V2.

## 2. Single-phonon nuclear FOM (V6, V7b; L-F1)
(i) The C1a/C1b algebra is right. With e_κ = √(M_κ/M_cell)q̂, c_κ = A_κ and M_κ = A_κm_u, (2π/Ω)|Σ_κA_κq·e_κ/√M_κ|²/(2ω)·Ω/M_cell = πq/(m_u²c_LA).
**2205.02250 Eq. (30)** [FT, p.8]: S_LA ≈ 2π(Σ_dA_d)q²/(Ω_c2m_pω_LA)δ(ω − ω_LA)Θ(ω_LO − ω), with the acoustic eigenvector Eq. (27) √A_d/√ΣA k̂. Divided by
ρ_T = M_cell/Ω_c this is exactly (2.3a) (m_p ↔ m_u). CONFIRMED. L-F1 should cite Eq. (30) and keep its Θ(ω_LO − ω) cut (the source's guard against
overcounting the LA branch near the zone edge).
(ii) **Optical branch: wrong.** The return says it couples "through (A₁/M₁ − A₂/M₂)-type combinations, ≈ 0 for c_κ ∝ M_κ … reopens through Umklapp". That
is true only at q = 0. WP2-v3 (2.2) keeps the intra-cell phase e^{iq·r_κ}, and at q ≪ q_BZ the leading optical term comes from it. 2205.02250 Eq. (31) [FT]:
S_LO ≈ (2π/Ω_c)q⁴a²A₁A₂/(32ω_LOm_p(A₁ + A₂))δ(ω − ω_LO), "from averaging over angles … (q·r₂)² ≈ q²a²/16". This term is O(q⁴a²) and
composition-dependent (A₁A₂/A_cell). It is not zero, and not Umklapp. C1a sets the phases to 1, so it cannot see this. The §0 table's "optical
(A₁ − A₂)²-suppressed" contradicts both §2.3 and the source (it would predict large optical coupling in NaI).
(iii) **Validity range.** 1910.08092 p.30 [FT] says: "For m_χ = 1 MeV and 10 MeV, Umklapp processes dominate the rate in the heavy mediator case". 2205.02250
p.8 [FT] says q leaves the 1BZ for m_χ ≳ 1 MeV and that (30) "applies across the entire DM mass range" only for the massless mediator. So the A-free
per-mass FOM π/(m_u²c_LA) of §5.1 holds (a) for the light mediator at all m_χ above the edge, and (b) for the heavy mediator only at m_χ ≲ 0.1–1 MeV (Si
q_BZ ≈ 2.3 keV ⇒ q_max = 2m_χv_max < q_BZ for m_χ ≲ 0.43 MeV). Above that the incoherent, composition-dependent form (2205.02250 Eq. (33)) governs. §2.3(e)
already quotes the Umklapp dominance; §5.1 must carry the restriction.
(iv) **V7b.** 1807.10291 p.6 [FT, HTML and PDF agree]: "the longitudinal sound speed is c_s ∼ 4000 m/s in GaAs and c_s ∼ 10⁴ m/s in sapphire". The return
drops "longitudinal" and brackets the value with c_T…c_L. The like-for-like comparison is c_L^{DB} = 4.82 vs 4.0 km/s (+20%, at the edge of the return's own
20% need), and sapphire c_L^{DB} = 10.77 vs ∼10 (+8%). C12a tests nothing; replace it with |c_L^{DB}/c_L^{FT} − 1| and report 20%.
(v) "Opposite roles of c_LA": both the rate coefficient and the edge scale as 1/c_LA (higher rate, but worse edge, for soft lattices). The wording is fine, but
"rate ∝ 1/c_LA" also needs m_χ well above the edge: the q-range [ω_th/c_LA, 2m_χ(v − c_LA)] depends on c_LA near m_min^{ac}.

## 3. Polar FOM and the KK bracket (V9, V10; L-F2)
(i) (2.5b) re-derived: ε₀ − ε_∞ = e²Z*²/(Ωμω_T²) (HL), ω_L² = ω_T² + e²Z*²/(Ωμε_∞), so ω_L(1/ε_∞ − 1/ε₀) = e²Z*²/(Ωμε_∞²ω_L). Per mass ÷ρ_T → 1/M_cell. Correct.
(ii) **Rate ≠ 𝓘_pol.** The light-mediator kernel (2.1a) gives 𝓡_pol ∝ ∫_band dω L(0,ω)∫dq η/q = Σ_ν(πω_Lν/2)Δ_ν·η̄_ν ln(q₊/q₋(ω_Lν)), with q₋ ≈ ω/v_max.
For sapphire at m_χ = 1 MeV, ln(2m_χv_max²/ω) = 5.68 (48 meV) vs 4.83 (112 meV), a 15% relative re-weighting; near the edge the weights differ by orders of
magnitude. WP2-v3 (4.3) carries the same per-branch log. "𝓡_pol ∝ 𝓘_pol/ρ_T" is therefore [E] (multi-branch) and exact only for one branch at fixed m_χ.
(iii) **GaAs bound.** "ω_LO ≤ 34 meV" uses 1910.08092 p.30 ("34 meV, the highest phonon energy in GaAs", CONFIRMED verbatim). That is their DFT histogram
range (JARVIS JVASP-1174 `modes` top: 253.62 cm⁻¹ = 31.4 meV [DB], another DFT value), not a bound on the physical ω_LO. With the FT ε of 1807.10291 Table I, LST
forces ω_LO/ω_TO = √(12.9/10.89) = 1.088. A measured ω_TO ≈ 33.3 meV [UNVERIFIED, not in any fetched text] gives ω_LO ≈ 36.2 meV, so
𝓘_pol/ρ_T ≈ 0.153 (not "≤ 0.144"), an edge ≈ 10.3 keV (not 9.7), and a sapphire ratio ≈ 61 (not 65). Whatever the exact ω_TO, "≤" is unsupported. Use a measured
ω_TO plus LST with the same source's ε, tagged.
(iv) **Sensitivity.** "δln𝓘 = 2δlnZ* − 2δlnε_∞" ignores ω_LO(Z*, ε_∞) in (2.5b). At fixed ω_TO, ∂ln𝓘/∂lnZ* = 2 − (ω_L² − ω_T²)/ω_L² = 1.85 (GaAs), ≈ 1.5 (ω_L/ω_T ≈ 1.4).
"×2" is an upper bound, which is conservative for the 10% accuracy need: keep, but relabel as a bound.
(v) **(8.1).** Proof re-derived. For lossless interlaced poles, ∫L/ω = (π/2)(1/ε_∞ − 1/ε₀) by KK at ω = 0. Support is at the ω_Lν; ω_T1 < ω_L1, and
ω_LN = ω_TN√(ε₀/ε_∞)/Π_{ν<N}(ω_Lν/ω_Tν) ≤ ω_T,max√(ε₀/ε_∞). The checks C4c, C6o and C6e reproduce 15.77 ≤ 37.42 ≤ 45.36 and 17.79 ≤ 39.16 ≤ 50.69 meV. **DB
application:** the four JARVIS entries were re-pulled live and the field values in C6b are CONFIRMED (Al₂O₃ 3.204/8.803/369.01/613.17; AlN 4.573/4.976/600.05/653.02;
GaN 6.066/5.250/512.97/532.99; MgO 3.136/7.148/386.0/386.0). But `dfpt_piezo_max_dielectric_*` are, by their naming, maxima over the tensor, and `min/max_ir_mode` span all
polarisations, so D = 1/ε_∞ − 1/ε₀ is not the per-axis value required by the stated validity ("one principal axis at a time"). For uniaxial Al₂O₃, AlN and GaN
the DB intervals are not proven brackets; that Al₂O₃ [4.24, 13.63] contains 9.40 is a consistency observation, not a test. Only MgO (cubic, one mode) is
rigorous, and there the upper end is the exact one-mode value.
(vi) L-F2 source: the return cites "1807.10291 Eq. (32)" via WP2-v3. In the fetched v1 PDF, Eq. (32) is the general rate formula and the one-branch
|ℳ|² = e′²(ω_LO/2)(1/ε_∞ − 1/ε₀)/q² is **Eq. (22), p.17**. In the arXiv HTML rendering it is Eq. (32). The return uses PDF numbering elsewhere (Eq. (40), Table II
p.31), so state the numbering scheme. Physics CONFIRMED.

## 4. Migdal per-mass scaling (V13; L-F3)
(i) C8 is right for one species: (1/M)∫₀^{E_max}dE_N [MA²σ_n/(2μ_n²v²)]·(2E_N/M) = 2A²σ_nμ_N⁴v²/(μ_n²M³).
(ii) **Compounds.** The number of nuclei κ per unit mass is 1/M_cell, not 1/M_κ. Redoing C8 with two species (sympy, this report) gives
rate per mass ∝ 2m_χ⁴σ_nv²(Z₁² + Z₂²)/(m_n²m_u³(A₁ + A₂)) (m_χ ≪ M_κ). So the material scalar is **Σ_κZ_κ(k)²𝓜_Mig/A_cell**, not Z_κ²𝓜/A_κ per species;
(2.7), §0 and §5.1 must change. For elemental targets the two agree.
(iii) **Regime.** The material scaling needs only m_χ ≪ M_κ (μ_N ≈ m_χ). The label "m_n ≪ m_χ ≪ M_κ" in §0 and L-F3 selects 1–26 GeV, outside the claimed
dominant 10 MeV–1 GeV, where μ_n ≈ m_χ and the power is m_χ² (the return says this in a side sentence). Swap the label.
(iv) **Missing hypothesis.** Factorising with E_N ≤ 2μ_N²v²/M_κ ignores the electronic energy in the kinematics. With ω included, q_N ∈ [q₋, q₊],
q₊ = μ_Nv(1 + √(1 − 2ω/μ_Nv²)). The E_N² weight then carries [(1 + √(1 − 2ω/μ_Nv²))/2]⁴: 0.93 at ω/(μv²/2) = 0.07, 0.72 at 0.29 (for m_χ = 20 MeV,
μv²/2 ≈ 70 eV, i.e. ω ≈ 5 and 20 eV). So "m_χ-power × m_χ-independent material functional" holds only for ω ≪ μ_Nv²/2 and is broken by ~10–30% at the low-mass
end. Add this to L-F3's validity.
(v) **Z_κ.** 2011.09496 Eq. (6) (WP3-v3 L7b) uses Z_ion(k), the valence ion charge (NOTATION Z_κ(p) "effective ion charge"). §0 and §5.1 write bare
"Z_κ²/A_κ", which by NOTATION line 116 is the nuclear charge. With nuclear Z, Z²/A ∝ A and "light nuclei win" would be false. Write Z_κ(k) throughout;
"light nuclei win" holds at fixed valence charge.
(vi) **Mass range.** WP3-v3 L7b: impulse onset q ≳ 91.5/112 keV ⇒ m_χ ≳ 17.3 (Si)/21.1 (Ge) MeV at the kinematic endpoint. The class's "10 MeV" lower end lies
in L7c territory. Change it to ≈ 20 MeV, with L7c below.

## 5. Other classes (V3, V4, V5b, V8, V11, V15)
- **Z/A** (C7b, C7c): reproduced for the listed set. Counterexamples to "inorganic ∈ [0.40, 0.50]" (this report): Pb 0.396, Bi 0.397, U 0.387 (heavy scintillators and
  bolometers), LiH 0.503, H₂O 0.555. Restrict the claim to "the targets listed" and quote the range per family.
- **w_acc**: 𝓡_ER,heavy ∝ ∫dq q³∫dω ηL, while w_acc is defined on ∫ωL. The proportionality "∝ (Z/A)·w_acc" needs ∫_acc L dω = ⟨1/ω⟩_acc∫_acc ωL, so
  𝓡 ∝ (Z/A)w_acc⟨1/ω⟩_acc. Tag it [E] or add the factor.
- **Lindhard sketch**: L = (πω/2qv_F)(q²/k_TF²)/(1 + q²/k_TF²)² re-derived from ε₂ = (π/2)(k_TF²/q²)(ω/qv_F), ε₁ ≈ 1 + k_TF²/q². Correct.
- **ALP–photon**: see V5b. The return's "× B₀²" drops 1/m_φ², which changes the FOM's mass dependence by m_φ⁻² (irrelevant at fixed m_φ, wrong as a function of m_φ).
- **Impulse ∝ A**: valid at m_χ ≪ M_κ, far above the NR threshold. Near the edge, q ≥ √(2M_κE_th) reverses the ordering (lighter wins). The ∝ A is "at fixed
  ω-integrated detection", which the return does say; add "far above √(M_κE_th/2)/v_max".
- **FM magnons**: ω = 𝔇_swq² + Δ_mag. Kinematics 𝔇_swq² ≤ qv − q²/2m_χ ⇒ q ≤ v/(𝔇_sw + 1/2m_χ), ω_max = 𝔇_swv²/(𝔇_sw + 1/2m_χ)². This is not the (2.3b) algebra.
  "[D, by the same algebra]" FALLS for FM and STANDS for AFM (linear).
- **§3 floor**: with b_bg per mass per energy, s = σ𝓡MT and b = b_bgΔE·MT give σ_lim → Z f_sys b_bgΔE_ROI/𝓡 (numerically confirmed). The Asimov expression
  used is the discovery form. Exclusion uses 2[s − b ln(1 + s/b)]. Both → s²/b, so 𝓩_B stands. The 𝓩 scalars rank materials at fixed m_χ correctly. As
  reach formulas they need the factor ρ_χπ/(m_χμ_χe²) that (1.2) puts outside 𝓡.
- **Near-edge (V2)**: (7/2 + k + p̄)·½√(m_min/m)/(1 − √(m_min/m)) at 1.05 m_min: 132 (p̄ = 3), 101 (p̄ = 3/2, Si replica edge 0.3327 MeV, WP6-v3). The
  "1–2 meV" E_th need stands for the continuum; the replica needs ≈ 2.3 meV. Both are at the window edge, so quote it as "≥ 0.15% within Δm/m ≤ 5%".

## 6. Completeness of the WP8-U property list (V16; rubric f)
Missing or under-specified, each needed by a FOM the return itself defines or by STATEMENT H1:
1. **Nuclear spin content** (isotopic abundance of spin-carrying isotopes, ⟨S_p⟩, ⟨S_n⟩; WP2-v3 (7.1) spin density). There is no spin-dependent NR FOM class at all;
   the only isotopic item is "B−L".
2. **Dynamical quadrupoles 𝒬_κ** (WP2-v3 (4.5)): Si/Ge dark-photon one-phonon S ∝ q⁴. §2.5 says Z* = 0 but tabulates nothing for the q⁴ vertex.
3. **Ω, a, q_BZ, intra-cell positions r_κ**: they set the validity of (2.3a) and the optical NR term ∝ q⁴a² (§2(ii)).
4. **SOC strength / R̃_{s,c}**: it enters FOM_ALP and the spin rows (the nuisance table has it, the property table does not).
5. **Inelastic/exothermic DM (Δ_χ)**: STATEMENT H1 lists it, CONVENTIONS §3 defines it, and no FOM class covers it (edges shift by Δ_χ; exothermic gives
   ω < 0 reach).
6. **T_op and E_g(T_op)** are mentioned in a cell but not as a property row; ε_eh(T), ω_TA(Q*) at T_op likewise.
7. Radiopurity list (iii)(i) is [UNVERIFIED] and incomplete for the targets the return names: ¹⁸⁰W (CaWO₄, W), ¹¹⁶Cd/¹³⁰Te ββ (CdTe), ¹⁴⁷Sm, ¹⁵²Gd, ¹⁷⁴Hf,
   ¹⁹⁰Pt, ⁵⁰V, and the elements Th, U themselves.

## 7. Proposed LIMITS rows (rubric b)
| Row | Source quoted correctly? | Chain valid? | Validity / leading correction | Verdict |
|---|---|---|---|---|
| L-F1 | Only "§III A long-wavelength form" is cited, with "no number used". The actual source formula is **2205.02250 Eq. (30) with eigenvector Eq. (27)** [FT p.8], which (2.3a) reproduces per mass exactly | Yes (C1a, b) | Add the Θ(ω_LO − ω) cut; leading correction is the intra-cell phase O((q·r_κ)²) (source Eq. (31) for the optical term), ahead of the O(10⁻³) mass defect; heavy mediator m_χ ≲ 0.1–1 MeV, light mediator all m_χ (source p.8) | STANDS WITH CORRECTION |
| L-F2 | Physics CONFIRMED; equation number is HTML numbering (PDF v1: Eq. (22)) | Yes (C3–C6) | Add "per principal axis; DB tensor-maximum fields do not satisfy this"; multi-branch rate carries ln(q₊/q₋(ω_Lν)) weights | STANDS WITH CORRECTION |
| L-F3 | 2011.09496 Eq. (6) as quoted in WP3-v3 L7b (Z_ion(k), 4α) — consistent | Elemental only | Replace the per-species 1/M_κ by 1/M_cell (Σ_κZ_κ(k)²/A_cell); regime m_χ ≪ M_κ (drop m_n ≪ m_χ); add ω ≪ μ_Nv²/2; impulse onset 17–21 MeV | STANDS WITH CORRECTION |

## 8. Literature, database and provenance (rubric c, e)
**Full-text verifications (all fetched, PDFs deleted):**
| Claim in the return | Result |
|---|---|
| 1807.10291 Table I p.11: GaAs ρ_T 5.32, ε₀ 12.9, ε_∞ 10.89; sapphire ε_∞ 3.2, ε₀ 11.5 ∥ / 9.3 ⊥ | CONFIRMED (Table I also gives sapphire ρ_T 3.98, which the code uses untagged) |
| 1807.10291 Table II p.31: sapphire o/e ω_LO, γ_LO, ω_TO, γ_TO | CONFIRMED (e-ray widths are starred "adopted" from o-ray in the source; the return should say so) |
| 1807.10291 "Eq. (40) … [FT p.31]" polarisation average (1/3)e + (2/3)o | CONFIRMED in content; **page is p.30** |
| 1807.10291 p.6 c_s | CONFIRMED text, **misused** (V7b) |
| 1910.08092 p.30 "34 meV, the highest phonon energy in GaAs"; Umklapp dominance at 1 and 10 MeV (heavy mediator) | CONFIRMED verbatim; "above ~1 MeV" is a fair paraphrase. Use as a bound FALLS (§3(iii)) |
| 1706.05818 Table 1 p.12 natGe 75 ± 26, NaI 83 ± 27; Table 2 p.14 measured 82 ± 21 [16], 76 ± 6 [62] | CONFIRMED (the source notes these are neutron-only, so lower limits; add) |
| 2506.06568 p.1: "roughly 124 atoms/kg/day", "roughly 0.002 events/kg/keV/day for each day of sea-level exposure", 18.6 keV endpoint | CONFIRMED. The same page gives "half-life of 12.3 years": upgrade the [UNVERIFIED] tag on ³H T½ to [FT] |
| 2205.02250 §III A | CONFIRMED and sharpened (L-F1) |
**Database claims (live JARVIS OPTIMADE, 2026-11-01).** Rated per item:
- GaAs JVASP-1174: optb88 gap 0.085, mbj 1.321, density 5.102, `dfpt_…_electronic` 3097.93, `min/max_ir_mode` 1.77, K/G 61.93/42.32: **CONFIRMED**. "Metallic OptB88
  gap" is loose (0.085 eV); the vetting rule (gap > 0.3 eV) is right.
- Si JVASP-1002: 0.731/1.277/HSE 1.22, density 2.25, mepsx 10.7409, epsx 13.4865, K/G 87.27/63.28: **CONFIRMED**. Ge JVASP-890 optb88 gap 0.0, K/G/ρ CONFIRMED.
- NiO ehull 0.1267/0.1282 (both Fm-3m entries): **CONFIRMED**. MgO JVASP-116 ehull 0.0297 with I4/mmm JVASP-115229 at ehull 0.0: **CONFIRMED**.
  NaI P6₃/mmc JVASP-139584 ehull 0.0 vs rocksalt JVASP-1996 0.009: **CONFIRMED**. CsI and Y₃Fe₅O₁₂: 0 results: **CONFIRMED** (formula query).
- **Under-reported:** NaI JVASP-1996 min/max_ir_mode = 0.28 cm⁻¹ and SiC JVASP-8158 = 3.39 cm⁻¹ also fail rule (ii). IF-F7 lists only "zincblende GaAs";
  extend it to "rocksalt NaI, zincblende SiC".
- **Rule (i) "MBJ within ≈ 10%": REFUTED** by the same live data: Ge mbj 0.606 vs campaign E_g 0.744 eV (WP6-v3), −19%; GaAs 1.321 vs ≈ 1.52 eV [UNVERIFIED], −13%.
  WP8-U must not use MBJ gaps for edges either (the 1% need).
- Diamond JVASP-91 K/G/ρ: not re-pulled (pagination); **UNRESOLVED** by this referee (the value 18.0 km/s is physically plausible).
**Provenance tags (e).** CONVENTIONS §12 has no [DB], "[DB-derived]" or "[FT-R7 via …]" tags. Either add them through the coordinator (IF) or map them to [FT]/[E]
with a source line. Untagged material values: sapphire ρ_T 3.98 (FT Table I); ϵ_coll = 0.3 and E_st,1 ≈ 7–9 eV behind "2.7 eV" ([E]/[UNVERIFIED] in WP7-E-v3,
dropped here); class ROIs in §3 ([E]). ε_eh 3.749 ± 0.001, F_eh 0.119 ± 0.002 agree with WP5-v3 l.252 and are unchanged in WP5-v4 l.298. The §4 prior
𝒩(3.75, 0.05) matches WP6-v3 (5.2).

## 9. Consistency with WP0-v3, CONVENTIONS, NOTATION (rubric d)
- tr[𝔇ᵀS], the η/(2q) halo factor, v_max = 794.5, ρ_χ = 0.3, the S ↔ L map and the external-field rule (total ε for the dark photon, R_NN for nucleons, unscreened
  spins at SOC = 0) are all consistent with WP0-v3 (3.4), (5.3)–(5.5) and CONVENTIONS §6–§8.
- The "ER-ρ: total ε" in §0 is imprecise. For electron-only coupling the ELF form uses ε_e, equal to ε only at clamped nuclei or ω ≫ ω_max (CONVENTIONS §6,
  WP0-v3 (5.5)). It is harmless in the ER window (ω ≥ E_g), but write "ε (= ε_e at ω ≫ ω_max)".
- **Symbol collisions** (NOTATION): 𝒦_a (kinematic factor) collides with the cascade kernels 𝒦_c, 𝒦_{Λ₀→Λ₊} (NOTATION l.227, 266); 𝓜_Mig collides with the
  moment matrices 𝓜¹_ab, 𝓜³_ab (l.190); 𝓃_S is one case-change from 𝓃_s, the species number density (l.123); 𝓡 (FOM) is visually confusable with ℛ (rate).
  "ω̄_κ used unchanged" is not in NOTATION.md (0 hits). Propose renames via IF-F6 (e.g. 𝒦 → 𝒦^{kin}; 𝔐 is the τ Migdal slot, so use 𝓠_Mig for 𝓜_Mig).
- §4 halo row "v_esc 2–7%": WP6-v3 (3.5) l.295 states 2–7% in **v_max** (from the v_esc spread), so 4–14% in m_min is right; relabel "v_max 2–7% (v_esc)".
- WP5-v4: the return says "WP5-v4 not used". The values it uses are identical in WP5-v4, so there is no conflict.

## 10. Checks (rung 3)
Rerun: 39/39 PASS. Weak checks: C10d assumes the formula it tests (tautology); C12a tests a wrong comparison (V7b); C15 (GaAs < sapphire) and C6db ("well ordered")
are trivially true; C13 has a 35% tolerance. Missing checks this report ran: the compound Migdal per-mass sum (§4(ii)), Z/A counterexamples, GaAs LST ω_LO, the
POL log weights, the floor's ΔE, the replica sensitivity (101). None of the 39 tests the optical NR-1ph term or the v-dependent 𝔇 case.

**DONE rung-4 rubric items checked:** Bose factors (T = 0 forms; n + 1 in (2.3a)), screening applied once (total ε / R_NN / unscreened spins), F_DM and v_max
conventions (CONVENTIONS §8–§9; 794.5 km/s), η/(2q), yield values (WP5-v3/v4), Umklapp (V6(iii)), dipole limit outside validity (V4, V6): clean except where
listed above. Time ordering, Pauli blocking and the sign of q are not exercised by this return.

## Required corrections (summary, for the coordinator)
1. §2.3/§0/§5.1: replace the optical-branch statement and "(A₁ − A₂)²" with the intra-cell phase term (2205.02250 Eq. (31)); restrict π/(m_u²c_LA) to the light mediator,
   or heavy at m_χ ≲ 0.1–1 MeV.
2. C12a/§5.2: compare c_L only (+20% GaAs).
3. (2.7)/§0/§5.1/L-F3: Σ_κZ_κ(k)²/A_cell; regime m_χ ≪ M_κ; add ω ≪ μ_Nv²/2; lower end ≈ 20 MeV.
4. GaAs POL: ω_LO from LST (36.2 meV) ⇒ 0.153 meV cm³/g, edge 10.3 keV; drop "≤".
5. (8.1) DB brackets: rigorous only for cubic entries; label the uniaxial ones heuristic.
6. 𝓡_pol: carry the ln(q₊/q₋(ω)) weight, or tag "∝ 𝓘_pol" [E].
7. ALP–photon: × B₀²/m_φ², L_∥.
8. FM magnon edge: quadratic dispersion.
9. §3 floor: × ΔE_ROI; state the flux/σ̄ factor outside 𝓡.
10. (1.2): add "v-independent 𝔇"; define 𝒦 for v_T rows.
11. Z/A claim restricted; ⟨1/ω⟩ in the w_acc scaling.
12. Property list: items 1–6 of §6; IF-F7 extended (NaI, SiC); §5.3 rule (i) withdrawn (MBJ −13 to −19%).
13. Tags/pages: Eq. (40) p.30; L-F2 Eq. (22) (PDF v1); sapphire ρ_T [FT]; ³H T½ [FT]; [DB] tag via the coordinator; symbol renames (§9).
