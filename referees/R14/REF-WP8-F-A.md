# R14 referee REF-WP8-F-A (hostile, isolated): returns/R13/WP8-F.md

Brief: briefs/R14/REF-WP8-F-A.md. Read: the return, code/WP8-F/checks.py (rerun), CONVENTIONS, NOTATION (grep), LIMITS, DONE, and the cited campaign
packages returns/R8/WP0-v3, WP2-v3, WP3-v3, WP4-v3, WP5-v3, WP6-v3, WP1-v3 (grep), returns/R12/WP7-E-v3 (grep). Full texts fetched with lit.py into
literature/papers-r14-REF-WP8-F-A/ and deleted: 1807.10291 (v1), 1910.08092, 2011.09496, 2205.02250 (v2), 2506.06568, 1706.05818, 1708.08929.
JARVIS OPTIMADE re-queried (curl -L, `chemical_formula_reduced` filters) for JVASP-1174, -1002, -32, -30 and CsI. **Checks rerun: 39/39 PASS, 2.5 s.**

## Verdict table
| # | Main claim (return §) | Verdict | Reason (details below) |
|---|---|---|---|
| V1 | (1.1)–(1.2) factorisation, 𝒦_a = qF²η/(4π²), 𝓡_a | STANDS WITH CORRECTION | Prefactor is consistent with CONVENTIONS §8 (η/2q, |𝒱|² = πσ̄_e/μ²). Missing hypothesis: 𝔇 must not depend on v (𝔇^{(1)}, 𝔇^{(2)} rows need other halo moments). c_a is undefined (F1) |
| V2 | (1.2) edge vocabulary; near-edge log-sensitivity ≈ 132 | STANDS WITH CORRECTION | 132 reproduced from WP6-v3 (3.3) with p̄_on = 3. The exciton replica has p̄_on = 3/2 (WP6-v3 table), so the PAER sentence needs both (F2) |
| V3 | ER-ρ (2.1a), light-mediator reduction, L17 ceiling, Z/A ∈ [0.40, 0.50] | STANDS WITH CORRECTION | q-weights and the f-sum are correct. Z/A holds for the 12 listed solids only: it fails for "inorganic targets" in general (F3). §0 says "total ε" without its condition (F4) |
| V4 | ABS: A′ = L(0,m_φ)/ρ_T; ALP ∝ m_φ²ε₂/ρ_T; scalar; ALP in B₀ | STANDS WITH CORRECTION | A′ and ALP are correct. ALP-in-B₀ "× B₀²" leaves out 1/m_φ² (F5). 1807.10291 Eq. (40) is on p.30, not p.31 |
| V5 | (2.3a) per-mass coherent LA coefficient π q/(m_u²c_LA), A-free | STANDS WITH CORRECTION | Algebra checks and agrees with 2205.02250 Eq. (30) [FT]. Needs a pure-LA hypothesis for anisotropic crystals (F6) |
| V6 | Optical branch at q ≪ q_BZ "≈ 0" (§2.3a) and "(A₁ − A₂)²-suppressed" (§0) | FALLS (as stated) | §0 contradicts §2.3. Both omit the O(q·r_κ) basis-phase term: S_LO ∝ q⁴a², 2205.02250 Eq. (31) [FT] (F7) |
| V7 | (2.3b) acoustic edge; c_LA "opposite roles"; DB-vs-FT c_s cross-check | STANDS WITH CORRECTION | Edge formula and numbers reproduced. The "bracketing" check compares c_T–c_L with a source value that is explicitly longitudinal (F8) |
| V8 | §2.4 multiphonon/impulse: composition-free first moment, ∝ ⟨A⟩ zeroth moment, 2W ≈ q²/(2Mω̄) with ω̄ the first DOS moment | STANDS WITH CORRECTION | The moments are right. 2W uses ⟨ω⁻¹⟩ (WP2-v3 (3.1); 2205.02250 Eq. (24)), so the [D] tag is wrong (F9) |
| V9 | §2.5 (2.5a), (2.5b); GaAs ≤ 0.144, sapphire 9.40, ×65 | STANDS WITH CORRECTION | Identities are exact. 𝓡_pol ∝ 𝓘_pol needs a band-uniform kinematic weight. GaAs "≤" is not a bound (F10) |
| V10 | (8.1) DB-only bracket | STANDS (theorem); DB use WITH CORRECTION | Proof correct, checked. The DB "max" fields mix principal axes (F11) |
| V11 | §2.6 magnons | STANDS WITH CORRECTION | 1/(2|𝐒|) gives 1, not 0.5, at |𝐒| = ½ (inherited from WP4-v3). FM two-magnon ≡ 0 at T = 0 is not stated (F12) |
| V12 | §2.7 PAER edge, window, dominant range 0.33–0.54 MeV | STANDS WITH CORRECTION | Edges and window agree with WP6-v3. PAER *leads* only to ≈ 0.43 MeV, so §0 overstates the range (F13) |
| V13 | §2.7 Migdal (2.7), L-F3 | STANDS WITH CORRECTION | Z_κ(k)² is pulled outside a k-integral. The regime label conflicts with the dominant range. The source's 1BZ validity is missing (F14) |
| V14 | §2.8 TLS / LEE proxies, L32, L36 caps, L29 | STANDS | Every number matches LIMITS L29, L32, L36 (as corrected), L38 and WP7-E-v3 rows 13–14. The (prov.) flags are applied |
| V15 | §3 reach scalars 𝓩_0, 𝓩_B, systematics floor | STANDS WITH CORRECTION | 𝓩_0 and 𝓩_B are right. The floor is dimensionally wrong as written. Confidence levels are mixed (F15) |
| V16 | §4 nuisance table; §5.2 needed accuracies | STANDS WITH CORRECTION | On the ε₀/ε_∞ route the POL sensitivity to ε_∞ is ε₀/(ε₀ − ε_∞), which is 6.4 for GaAs, not 2. ρ_T row is inconsistent with its own rule (F16) |
| V17 | §5.2 WP8-U property list "complete" | STANDS WITH CORRECTION | Six inputs are missing (F17) |
| V18 | §5.3 DB vetting rules; JARVIS values | STANDS WITH CORRECTION | Re-pulled DB values match the return. MBJ "within ≈ 10%" fails for GaAs (−13%) (F18) |
| V19 | Literature quotes and [FT] tags (2506.06568, 1706.05818, 1910.08092, 1807.10291) | STANDS WITH CORRECTION | Every quote verified. One page, one equation-number version, and one calc/measured label are wrong (F19) |
| V20 | Proposed LIMITS rows L-F1, L-F2, L-F3 | STANDS WITH CORRECTION | Source pointers and validity columns need fixing (§B) |
| V21 | "Sources ×ε_bg too large" (Dirac absorption, carried from L16) | CONFIRMED for 1708.08929; UNRESOLVED for 1910.02091 | See §C |

## A. Findings (corrections owed)
**F1 (V1, rubric a, f).** (1.1)→(1.2) is correct for 𝔇^{(0)}. For velocity-dependent couplings the kinematic factor holds other halo moments (v_T, v_T⊗v_T; CONVENTIONS §7,
WP6 (1.2)): for example 𝒪₈ in §2.1 and the "non-density NR-EFT rows". Add "𝔇 independent of v, or 𝔇^{(0)} only" to the hypotheses of (1.2), or give
𝒦_a^{(1,2)}. "c_a" in 𝔇_aa = |𝒱_a|²F²c_a is undefined, and it collides with c_κ, c_s (CONVENTIONS §7, §13 row 9). Name it or drop it.

**F2 (V2).** δ_v,0 and the exponent 7/2 + k_tail + p̄_on reproduce 131.7 at 1.05 m_min (C14b; recomputed). WP6-v3 gives p̄_on = 3 for the continuum PAER edge and
3/2 for the exciton replica, so the 0.333 MeV replica edge has exponent 5 and a log-sensitivity of ≈ 101. §2.7(e) states only "p̄_on = 3". Also,
"0.15%-level E_th sensitivity" is the *needed accuracy* 0.2/132, not a sensitivity.

**F3 (V3).** C7b proves Z/A ∈ [0.403, 0.500] only for the 12 listed solids. Counterexamples to "inorganic targets": Pb 0.396, LiH 0.503, H₂O
0.555. Scintillators stay inside (CsI 0.416, PbWO₄ 0.413, BGO 0.421). Replace with "for the listed targets; ≈ 0.39–0.56 over solids incl. hydrides".
The light-mediator reduction "η̄·ln(q₊/q₋)" is a definition of η̄ (the dq/q-weighted mean of η(v_min(q,ω))), not a derived constant. Say so.
The Lindhard sketch "𝓡 ∝ ∫q⁴dq/(k_TF²v_F)" omits the ω-integral ∫dω ω η(v_min), whose range ω ≤ min(qv_F, qv_max − q²/2m_χ) (v_F ≳ v_max, only 2–3× for metals) adds q powers. Only the
1/(k_TF²v_F) scaling is correct. Write it as such.

**F4 (V3, rubric f).** §0 row ER-ρ says "L = Im[−1/ε] (total ε)". For an electron-only coupling the external-field type is |e⟩ with ε_e (CONVENTIONS §7).
That equals the total/clamped ε only at clamped nuclei or ω ≫ ω_max (WP0-v3 (5.5)). The statement is right above the gap, where ER lives. Copy the
condition of §2.1(a) into §0. The other screening statements are correct: ER L not pointwise 1/|ε|²; A′ total ε; ALP none at LO; Dirac ε_bg in total ε (×ε_bg on sources);
POL built in; NR via R_NN; MAG none at SOC = 0; TLS ε_r.

**F5 (V4).** WP0-v3 (2.9) maps κ_mix m_φ² → g_aγγB₀m_φ, i.e. κ_eff = g_aγγB₀/m_φ. The A′ FOM then carries **g_aγγ²B₀²/m_φ²**, not "× B₀²". Note also
that WP0-v3 (2.9) has its source-prefactor check open (O6). ALP: Γ ∝ m_a²σ₁ = m_a³ε₂ gives ℛ ∝ m_a²ε₂/ρ_T. Verified.

**F6 (V5).** The rigid eigenvector e_κ = √(M_κ/M_cell) q̂ assumes a purely longitudinal acoustic mode along q̂ (isotropic, or high-symmetry q̂). In
general it is √(M_κ/M_cell) ê_ν, and the coefficient is π q Σ_ν (q̂·ê_ν)²/(m_u²c_ν(q̂)). Add this to (2.3a) and L-F1, since anisotropy is the L19 input.
"Exactly" A-free holds only to the accuracy of M_κ = A_κm_u (≤ 0.8%, H worst). 2205.02250 Eq. (30) has m_p, which differs by 1.5% in 1/m².

**F7 (V6) FALLS as stated.** (i) §0 "(A₁ − A₂)²-suppressed" is the equal-mass approximation (cf. 1807.10291's GaAs form factor). §2.3's own diatomic
algebra gives the q-linear coupling √(M₁M₂/M_c)(A₁/M₁ − A₂/M₂), which vanishes for A ∝ M even when A₁ ≠ A₂. (ii) Both versions drop the basis phase
e^{iq·r_κ} of WP2-v3 (2.2). At next order it gives a non-zero optical term: S_LO ≈ (2π/Ω_c) q⁴a²A₁A₂/(32ω_LO m_p(A₁+A₂)), 2205.02250 Eq. (31) [FT]. So the
optical branch is not "≈ 0" at q ≪ q_BZ. It is O((qa)²) relative, set by r_κ, and it is the leading in-1BZ optical channel above the acoustic band.
Correction: replace both statements by "q-linear term ∝ (A₁/M₁ − A₂/M₂), ≈ 0; leading term O(q⁴a²) from intra-cell phases (2205.02250 Eq. (31)); Umklapp."

**F8 (V7).** 1807.10291 p.6 [FT]: "the **longitudinal** sound speed is cs ∼ 4000 m/s in GaAs and cs ∼ 10⁴ m/s in sapphire". Compare like with like:
DB c_L(GaAs) = 4.82 km/s is +20% on the FT 4.0. The "c_T–c_L brackets c_s" check (C12a) tests nothing. Reword C12a and the §5.2 row ("2.9–4.8 bracket
FT 4.0") as "c_L DB/FT = 1.20", which is at the edge of the stated 20% need. The edge algebra (2.3b), m_min^{ac}(1 meV) values and opposite-role
statement are verified.

**F9 (V8).** WP2-v3 (3.1), ∫dω′w_κ = 2W_κ, gives 2W_κ = (q²/2M_κ)⟨ω⁻¹⟩_{D_κ} (T = 0). So does 2205.02250 Eq. (24) [FT]. The first moment ω̄_d is only the
order-of-magnitude scale in 2205.02250 Eqs. (25)–(26). "2W_κ ≈ q²/(2M_κω̄_κ) (ω̄_κ the first DOS moment)" is therefore an [E] under a [D] heading. By
Jensen's inequality it underestimates 2W (×1.125 for a Debye DOS, more for acoustic-weighted DOS). Use ω̄ ≡ ⟨ω⁻¹⟩⁻¹ in the Poisson-tail FOM and in
§5.2 ("10% in ω̄"), or retag as [E]. Impulse: per mass ∝ A × μ_χN² (from ∫q dq η(q/2μ)) holds in both limits m_χ ≶ M_κ, not only "at m_χ ≳ M_κ".

**F10 (V9).** The identities are verified: (2.5a) by partial fractions of 1/ε, (2.5b) by C3. Three corrections.
(i) Hypothesis: 𝓡_pol = Σ_ν(πω_Lν/2)Δ_ν·K(ω_Lν; m_χ), with K = ∫dq η(v_min(q,ω_Lν))/q. This is ∝ 𝓘_pol only when K is uniform across the band (m_χ ≫ 2ω_L,max/v_max²).
Near the edges the per-branch logs of 1807.10291 Eq. (24) (PDF v1) weight the branches differently. Add this to (2.5a), §0 and L-F2.
(ii) "GaAs ≤ 0.144" uses ω_LO ≤ 34 meV. That is 1910.08092's DFT "highest phonon energy" (quote verified, p.30–31). The measured ω_LO(Γ) is ≈ 36.2 meV, and LST with
the FT ε's (10.89, 12.9) and measured ω_TO 33.3 meV gives the same [UNVERIFIED, standard]. So write ≈ 0.144–0.153 (not a bound), edge ≈ 9.7–10.3 keV, ratio ×61–65.
(iii) The (2.5b) log-derivatives hold at fixed ω_LO. With ω_T fixed (the DFPT input) ω_L depends on Z*.

**F11 (V10).** (8.1) is correct: ω_Lν ≥ ω_Tν ≥ ω_T,min; ω_Lν ≤ ω_T,max·Π_μ(ω_Lμ/ω_Tμ) = ω_T,max√(ε₀/ε_∞) under interlacing; Δ_ν ≥ 0. C6o/e are confirmed.
Its stated validity is "one principal axis at a time", but the DB inputs `dfpt_piezo_max_dielectric_electronic/_ionic` are maxima over directions, possibly
from different axes. C6x then compares a mixed-axis DB bracket (density 3.882) with the FT ordinary ray (density 3.98). "Contains the FT 9.40" is therefore
not a like-for-like test. Use per-axis tensors, or label the DB bracket "orientation-maximal".

**F12 (V11).** 1/(2|𝐒|) = 0.2 (|𝐒| = 5/2) is right, but at |𝐒| = ½ it is **1**, not 0.5. This is inherited from WP4-v3 l.99/117 and owed there too. WP4-v3 [2.4](a): a Heisenberg FM
has S^{(2m)} ≡ 0 at T = 0. The return's "two-magnon adds a continuum" holds for AFM/ferri only. "Si/Ge have no magnon FOM" is correct.

**F13 (V12).** The edges 0.337 (continuum) / 0.333 (replica) and the windows Si 0.333–0.42, Ge 0.213–0.32 MeV are WP6-v3 (3.1)(iii) verbatim. But WP6-v3 also says
"PAER-leading to ≈ 0.43; two-channel 0.43–0.54; allowed ZPL above ≈ 0.54". §0's "dominant 0.33–0.54 MeV (Si)" should read "PAER-only 0.333–0.42,
leading to ≈ 0.43, shared to 0.54". The Δm_PAER/m definition is fine.

**F14 (V13).** 2011.09496 Eq. (6) [FT, verified]: dP/dω = 4α∫d³k/(2π)³ Z_ion²(k)|v_N·k|²/(ω⁴k²) Im[−1/ε(k,ω)]. Three corrections.
(i) Z_ion(k) is inside the k-integral and varies with k (valence charge at small k, larger at large k). (2.7) and §5.1 pull "Z_κ²" outside 𝓜_Mig. Define
𝓜_Mig,κ ≡ ∫d³k Z_κ(k)²L/(3(2π)³ω⁴) and drop the separate Z_κ². The /3 also needs an isotropic L.
(ii) The source states Eq. (6) is "only valid for k in the first Brillouin zone" (App. A otherwise). Add this to L-F3's validity.
(iii) The algebra (C8) is right: ∝ (A²/M³)μ_N⁴/μ_n² at fixed σ_n. But the material scaling Z²𝓜/A per mass holds for any m_χ ≪ M_κ. The §0/L-F3 label "m_n ≪ m_χ ≪ M_κ"
covers only ≈ 1–10 GeV, outside the stated dominant range 10 MeV–1 GeV, where μ_n ≈ m_χ and the power is m_χ². Relabel: "m_χ ≪ M_κ (material scaling);
m_χ⁴ only for m_χ ≫ m_n". Kinematic floor: ω ≤ μ_Nv²/2 ⇒ Migdal edge ≈ 2E_g/v_max², not "E_g at q_N"; say which.

**F15 (V15).** With s = σ𝓡MT and b = MT b_bgΔE: σ_lim → Z f_sys **b_bgΔE_ROI**/𝓡 (or Z f_sys∫b_bg dE/𝓡). As written, "Z f_sys b_bg/𝓡" mixes a density with an
integrated rate. The checks use one-bin b, so C10d does not see it. The background-free limit uses 90% C.L. (2.303), but C10c/d use Z = 1.64 (95% one-sided).
State one C.L. for both, e.g. Z = 1.28 at 90%. 𝓩_0 = ϵ_cut𝓡 should be ∫ϵ(E)𝓻̂_s dE when the efficiency is E-dependent. The Asimov limit and 𝓩_B = 𝓡/√(b_bgΔE) are verified.
So is the line case ∝ 1/√(b_bgσ_E): ∫𝓻̂²/b = 𝓡²/(2√π σ_E b).

**F16 (V16, rubric f).** On the route (2.5a)/(8.1), which uses ε_∞ and ε₀ (the DB fields): ∂ln𝓘/∂lnε_∞ = −ε₀/(ε₀ − ε_∞) and ∂ln𝓘/∂lnε₀ = ε_∞/(ε₀ − ε_∞).
Values: GaAs 6.4 / 5.4; AlN 1.9 / 0.9; sapphire(o) 1.5 / 0.5; MgO 1.4 / 0.4. The §4/§5.2 entries "2 (POL) → 10%" hold only on the Z*-route (2.5b) at fixed ω_LO.
For weakly polar crystals the needed ε accuracy is ≈ 3%, so the "±15%" JARVIS ε fields cannot rank them. Add this row. §5.2 ρ_T "5% for ER near edge" contradicts the
table's own rule (|∂lnFOM/∂lnρ_T| = 1 everywhere ⇒ 20%). The near-edge need belongs to E_g, which is already listed.

**F17 (V17, rubric f) — missing from the WP8-U property list.** (i) Z_κ(k) / ion-core charge profile (Migdal, F14). (ii) Nuclear spins and odd-A isotopic
abundances, ⟨S_p⟩, ⟨S_n⟩ (spin-dependent nucleon rows I_κ of WP0-v3 (2.2)); WP8-F has no SD-NR class at all. Either add a class or state the exclusion. (iii) Charge
transport μτ / trapping and collection (L33–L35 inputs: Hecht, Ramo, r_coll), which set the threshold in quanta and the LEE degeneracy (L38). (iv) SOC
strength, or R̃_{s,c}, for the ALP row (cited in §2.2/§4, absent from §5.2). (v) Nuclear radius / Helm parameters for the impulse FOM (× F_Helm²).
(vi) Operating-temperature E_g(T_op) and exciton binding at T_op, which §4 requires but §5.2 lists only as "E_g, E_x^b".

**F18 (V18).** Rule (i): MBJ 1.321 vs GaAs 1.52 eV is −13% and Si 1.277 vs 1.17 is +9%, so "within ≈ 10%" is wrong for GaAs. Re-pulled [DB],
**CONFIRMED** as quoted:
- JVASP-1174 (GaAs, F-43m): ε_el = 3097.93, ε_ion 7.08, max = min IR mode = 1.77 cm⁻¹, OptB88 gap 0.085 eV, MBJ 1.321, K 61.93, G 42.32, ρ 5.102.
- JVASP-1002 (Si): ρ 2.25, OptB88 0.731, MBJ 1.277, HSE 1.22, K 87.27, G 63.28.
- JVASP-32 (Al₂O₃): 3.204 / 8.803, IR 369.01–613.17, ρ 3.882.
- JVASP-30 (GaN): 6.066 / 5.250, IR 512.97–532.99.
- CsI: no entry.
So the "DB field invalid" claims stand. Add to F11: JVASP-32's `dfpt_piezo_max_dielectric` = 11.97 ≈ 3.204 + 8.803, i.e. the ∥c (e-ray) value (FT ε₀∥ 11.5). The
DB bracket is an e-ray-like bracket, compared in C6x with the FT o-ray integral.

**F19 (V19, rubric e).** Verified [FT]:
- 2506.06568 p.1: "roughly 124 atoms/kg/day", "roughly 0.002 events/kg/keV/day for each day of sea-level exposure", 18.6 keV. The ³H half-life is also in
  the FT (12.3 y p.1; 12.312 y later), so its [UNVERIFIED] tag can become [FT].
- 1706.05818 Table 1 p.12 (natGe 75 ± 26 calc.), Table 2 p.14 (82 ± 21, 76 ± 6 measured). NaI 83 ± 27 is the *calculated* sum (Table 1 caption); add "calc.".
- 1910.08092: "34 meV, the highest phonon energy in GaAs" (p.30–31); Umklapp dominance "For mχ = 1 MeV and 10 MeV … in the heavy mediator case". Verified.
- 1807.10291 v1 PDF: Table I p.11 (5.32, 12.9, 10.89; 3.98, 11.5, 9.3, 3.2) and Table II p.31 are verified. Eq. (40) is on **p.30**. The one-branch |ℳ|² is PDF **Eqs. (21)–(22)** (rate (24)).
  "Eq. (32)" is the arXiv-HTML numbering of the same object, while PDF Eq. (32) is the nucleon S(q,ω) rate. The return mixes PDF pages with HTML equation
  numbers (WP2-v3 (4.3) has the same inheritance). Cite one version.

## B. Proposed LIMITS rows (rubric b)
- **L-F1.** Chain valid (C1a,b re-derived by hand). Source: name **2205.02250 Eq. (30)** [FT] (S_LA = 2π(Σ_dA_d)q²δ(ω − ω_LA)/(Ω_c2m_pω_LA), with the cutoff
  Θ(ω_LO − ω)). It reproduces π q/(m_p²c_LA) per mass exactly. §6 says 2205.02250 was used for "wording only, no number used", which contradicts its use as the
  source formula; fix §6. Validity: add a pure-LA mode along q̂ (F6), e^{−2W} ≈ 1, and ω ≤ ω_LO (the source's cutoff). Leading correction: add O((qa)²) dispersion/phase
  terms (F7). m_p vs m_u is 1.5% in 1/m².
- **L-F2.** Chain (4.2)–(4.3) + LST → (2.5b) and KK → (8.1) is valid (C3, C4, C6). Source pointer: "1807.10291 Eq. (32)" → **PDF v1 Eqs. (21)–(22), rate (24)** (= HTML (31)–(32))
  (F19). Validity: add q ≪ q_BZ, ω ≪ E_g (WP2-v3 hypotheses), a band-uniform kinematic weight for 𝓡_pol ∝ 𝓘_pol (F10i), and per-axis ε inputs for the DB bracket (F11).
  The leading correction "damping < 1%" is verified (C4a).
- **L-F3.** Chain valid as algebra (C8). Fix the source quote (Z_ion(k) inside, F14i). Validity: add "k ∈ 1BZ (2011.09496 below Eq. (6); App. A otherwise)",
  isotropic L, soft limit |k| ≪ |q_N|, and relabel the mass regime (F14iii). The leading correction list is otherwise right (L7c below the onset; δM_κ).

## C. Claims that a published paper or database is wrong (rubric c)
| Claim | Source checked | Rating |
|---|---|---|
| Dirac absorption rates ×ε_bg too large (L16, §2.2c) | 1708.08929 Eqs. (2.4)–(2.6), (4.4)–(4.5) [FT]: (ε_r)_Dirac = 1 + (e²g/4π²κv_F)∫…, i.e. the background κ enters only through α̃ and not as the leading "κ +". The rate ε_eff²Im ε_r is then ×κ relative to Im[−1/ε] with ε = κ + δε (|δε| ≪ κ) | **CONFIRMED** (1708.08929); 1910.02091 not re-read: UNRESOLVED here (REFEREED R×2 in LIMITS L16) |
| JARVIS GaAs DFPT / IR fields invalid; CsI absent | OPTIMADE re-query (F18) | **CONFIRMED** (YIG not re-queried) |
| 1/|ε|² pointwise ≠ rate ratio (2101.08275) | not a "paper wrong" claim; carried from LIMITS L1 | — |
No other claim in the return says that a source is wrong.

## D. Consistency (rubric d)
- WP0-v3: (3.4) with tr[𝔇ᵀS], (3.5)–(3.6), (2.9), (5.5), (5.6), G6 ×2.30: consistent. CONVENTIONS §6 S ↔ L, §8 η/(2q), v_max 794.5 and halo: consistent; edge numbers
  reproduced (C16).
- NOTATION collisions: **𝓃_S** (new) vs existing 𝓃_s (number density of species s), a one-letter-case clash; rename it, e.g. 𝓃_spin. **𝒦_a** vs 𝒦_c, 𝒦_{Λ₀→Λ₊}, 𝒦^{rel}
  (cascade kernels). **𝓜_Mig** vs 𝓜¹_ab (moment matrices). **Δ_ν** vs Δ_χ, Δ^τ_k. **ω̄** is defined in NOTATION as a DOS moment alongside ⟨ω⁻¹⟩, which supports F9. ϵ_coll
  (§2.8) is not in NOTATION (the rows are ϵ_prim, ϵ_NTL); it is a WP7-E [E] value (0.3), so tag "≈ 2.7 eV [E]".
- WP6-v3 (3.1′), (3.3), (5.2), and WP2-v3 (2.2), (3.1)–(3.4′), (4.2)–(4.5), (8.2): consistent, except F7 (phase term) and F9 (2W).

## E. Checks (rerun; rubric DONE rung 3)
39/39 PASS. Weak or tautological: C12a (a bracket, F8), C6x (mixed axes, F11), C14 (arithmetic only), C8 (integrates the assumed form; it does not test the
Z_κ(k) factorisation), C10d (one-bin, so it misses the F15 dimension). No check covers (2.5a)'s kinematic-weight hypothesis, the optical O(q⁴) term, or the
Lindhard sketch. Suggested additions: (a) an angle-averaged diatomic S_LO with e^{iq·r_κ} against 2205.02250 Eq. (31); (b) ⟨ω⁻¹⟩ vs 1/⟨ω⟩ on a
Debye DOS; (c) per-branch K(ω_Lν; m_χ) for sapphire at 2–3× the edge.

## F. Rung-4 rubric items (DONE)
Screening once: satisfied (F4 wording only). DM kinematics: v_max, η/(2q) and σ̄_e are correct; the v-dependent 𝔇 gap is F1. Phonon normalisation: correct
(CONVENTIONS §5; C1). Umklapp: acknowledged; the F7 phase term is missing. Threshold/yield assumptions: flagged (prov.) throughout. Double counting: the WP3 N4 rule is
cited. No time-ordering or Pauli items apply to an FOM reduction.

**Overall:** no derivation falls except the optical-branch statement (V6). Owed corrections: F1, F5, F7, F9, F10, F14, F15, F16, F17, plus the pointer fixes
of F19 and §B, before WP8-U uses §5.
