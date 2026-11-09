# R16 VER-CW1: hostile referee report on returns/R16/CW1.md

Referee: VER-CW1 (isolated). Read: returns/R16/CW1.md, code/CW1/ (all scripts, inputs, out/*.json), returns/R15/COMP-PH.md, COMP-PAER.md,
returns/R8/WP1-v3.md, WP3-v3.md (cited sections), LIMITS.md, state/LOOSE-ENDS.md. Not read: other referees/R16, other returns/R16, briefs, log/LAUNCHES.
Reruns: `checks.py` 32/32 PASS (3 s, one core). Independent: (a) 30 random-start joint (q,k) Nelder–Mead minimisations on the committed Wannier TB
(own script, one core, 52 s); (b) the second valence band restricted minimum; (c) sympy checks of (CW1.5), (CW1.9) moments, (CW1.20), (CW1.25) and the
k_xc derivative; (d) re-derivation of the σ_z glide selection rule; (e) recomputation of SOC-consistent pair energies from the return's own
out/vertex_soc.json. No QE run (none needed). Literature [FT]: 2011.12765, 1608.01994 (PDFs deleted, HTML kept in literature/papers-r16-VER-CW1/).
**Chain-of-evidence limitation:** /root/work/CW1/ (the QE save dirs) no longer exists, so every vertex number (0.150, 0.0095, 3×10⁻¹⁴, 1.3×10⁻⁴,
the gradients) can be checked only for internal consistency against out/*.json, not regenerated. The Wannier numbers were regenerated (see §0).

## Verdict table (scope 1–3)
| # | item | verdict | reason (short) |
|---|---|---|---|
| V1 | LE-24 Si: first ZPL off axis in a {001} mirror plane (CW1.1, §1.2) | STANDS | joint minimum reproduced from 30 random starts (0.39972 MeV, same point up to O_h images); axis is a saddle of E_min(θ) |
| V2 | LE-24 Si number "0.400–0.405 MeV" (continuum), "0.397–0.402" (1s) | STANDS WITH CORRECTION | lower end is Wannier (DFT shows +11 meV); return's own SOC run raises the off-axis pair by +15.6 meV → **≈ 0.405–0.408** (1s ≈ 0.402–0.405) |
| V3 | Reconciliation with COMP-PH 0.4154 and COMP-PAER 0.405–0.408 (§1.2) | STANDS WITH CORRECTION | COMP-PH part correct (on-axis local optimum reproduced, 0.41501). COMP-PAER agreement at no-SOC level (0.405) is genuine; with SOC CW1 lands on 0.405–0.408 too |
| V4 | M_x = m_l + m_hh[100] = 1.19 m_e; 1.41 withdrawn (OC-5) | STANDS WITH CORRECTION | numbers reproduce (C1); "WP3 used a DOS mass" is CW1's inference: WP3-v3 l.115 says only "m_l + m_hh ≈ 1.41 [UNVERIFIED]"; masses are PBE without SOC |
| V5 | LE-24 Ge: "Γ₈ heavy hole more anisotropic than Si", ≈4% lowering transfers | FALLS (the sentence) | Luttinger warping (γ₃−γ₂)/γ₁ = 0.26 (Si) vs 0.11 (Ge); m_hh[111]/m_hh[100] = 2.6 vs 2.45. In Ge the L axis [111] is already the heavy-hole direction. Ge spec itself stands |
| V6 | LE-25: (2̄00) vertex Σ_v\|ρ\|² = 0.150, light hole only on axis | STANDS | json 0.1500 / 0.1503 (40/60 Ry); hh < 10⁻²¹; multiplicity rule consistent |
| V7 | σ_z mirror (glide) selection rule (§2.2) | STANDS | re-derived: ρ = s_c s_v e^{−iG′·t_d} e^{i(k_c−k_v)·(T/2−t_d)} ρ, with T/2 − t_d = (0,0,−a/4); in-plane → phase e^{−iG′·t_d} = ±1 (G′=0 / (2̄00)). Numerical zero 3×10⁻¹⁴ consistent |
| V8 | §2.3 allowed-size ZPL opens at ≈ 0.50 MeV on the X face; IF-6 hedge removed; 0.62 fallback withdrawn | STANDS WITH CORRECTION | minimum sits *on* the class constraint (k_x+q_x = −1), continuous with the G′=0 (−x valley) region; the in-plane X face is the X–W line where c₁/c₂ are degenerate and swap σ_z parity. At the DFT point c₁/c₂ split by 50 meV, c₁ = 0.0095 vs c₁+c₂ = 0.028: the "0.0095" is sensitive (×3). Withdrawal of 0.62 stands |
| V9 | §2.3 ZPL/PAER ≈ 2 at the opening, ≥ 10 from ≈ 0.51 | STANDS (as [E]) | json 2.4/2.2/1.6 and 10.5/9.6/6.5 reproduced; PAER side ×/÷10, so "leads robustly" is ×/÷10 robust only |
| V10 | (CW1.3)–(CW1.4) cone average, ϖ̄_II table (§3.2) | STANDS WITH CORRECTION | cone integral correct (C17, closed form); the bold 0.35 at 0.1 eV lies outside the return's own validity ε ≲ 0.08 eV and must carry the "overcount" tag; omissions below (V11) |
| V11 | §3.3 "PAER leads at least to ≈ 0.42, centrally ≈ 0.44 MeV"; two-channel 0.44–0.51 | STANDS WITH CORRECTION | add SOC shift (+0.003 MeV) to all edges; the mirror-even second heavy hole (open from 0.4150 MeV, on axis, vertex linear off axis) is omitted from ϖ̄_II; ∂_{q_z}ρ taken at fixed k_v, not at the relaxed pair optimum (≤ ×1.4 in \|ρ\|²) — all inside ×/÷10 |
| V12 | LE-27 (2̄00) LO minimum off axis → p̄_on = 3 (OC-6) | STANDS | C21 logic correct given lo_gamma.json (negative v_g and γ_ω) |
| V13 | OC-6 LA kink "SOC admixture ≲ 10⁻⁴" replaces "~2×10⁻³" | STANDS WITH CORRECTION | 10⁻⁴ is the on-axis ZPL-vertex transfer; at the mirror optimum the computed lift is (4.5%)² ≈ 2×10⁻³, WP3's old number. Must read "[E, transfer]" and state geometry |
| V14 | (CW1.5) "TDA overstates L by ×2" (§5, CW1-L5) | STANDS WITH CORRECTION | algebra correct ((E₀+ω)/2E₀, sympy), but it is the error of a *resonant-only* ε₁; a standard TDA BSE builds χ with ±E_λ poles (retarded), so this is not the TDA (coupling-block) error, which stays unquantified. The rule (TDA for ε₂, external screening from RPA+LFE) stands |
| V15 | (CW1.6) exciton dispersion with μ(Q) | STANDS | effective-mass statement; Dresselhaus L, M, N internally consistent ([110]/[111] N spread 0.19) |
| V16 | (CW1.9) Franck–Condon dressing | STANDS | moments E+S ω̄, variance S ω̄² (sympy) |
| V17 | §10 FW O(m⁻⁴) ~ 10⁻⁶, no-pair ≤ (Zα)² = 0.055 Ge 1s | STANDS | arithmetic correct; [D] as before |
| V18 | §11 triplet = singlet ladder up to O((a/a_x)³) [D, sketch] | STANDS (as sketch) | 0.11³ ≈ 10⁻³; sketch tag kept correctly |
| V19 | §12 L3 factor "interval 8–39 [E]"; "no longer unresolved in kind" (OC-11) | FALLS | "≥ 12×" in WP1-v3 l.458 is the Cauchy–Schwarz bound (√r−1)² at r ≳ 20, not an IP value; the return multiplies it by 0.7 and the IP r = 30 by 1.3, and drops WP1's in-medium enhancement "×2–9". Consistent IP range is [(√r−1)², (√r+1)²] = 12–42, larger in medium. Keep L3 text unchanged |
| V20 | §12 mixed block vanishes at G = 0 on 3-/4-fold axes | STANDS | n(q) is A₁ of C₄ᵥ/C₃ᵥ, transverse j is E |
| V21 | LE-36 Si SOC lift: 1.6×10⁻⁶ on axis, 1.3×10⁻⁴ mirror (OC-7, CW1-L6) | STANDS WITH CORRECTION | at the extremum the hole is at Γ where bands 5–8 form the Γ₈ quartet (vertex_soc.json Γ levels all 0): `top_pair` sums one arbitrary Kramers pair — gauge-dependent. Γ₈ sum bounded by all_valence/2 = 3.6×10⁻⁶ → write "(1.6–3.6)×10⁻⁶ (0.3–0.5% amplitude)". 1.3×10⁻⁴ and 2.6×10⁻⁶ (non-degenerate) stand |
| V22 | (CW1.14) plasmon branching 10⁻³–10⁻² [E]; q ≥ 6.3 keV | STANDS | 16.6 eV / v_max = 6.26 keV |
| V23 | (CW1.19) δ_LF and its vertex-level proxy | STANDS | definition; no claim beyond it |
| V24 | LE-43 (CW1.20): f-free one-electron sum withdrawn | STANDS | Matsubara sum re-done by residues: result matches up to an overall convention sign; f=0 limit and ΔF (C32) verified |
| V25 | LE-44 k_xc = (8/27)C_x n^{−5/3}; ≲ 5% of pair term | STANDS | sympy; size [E] |
| V26 | LE-45 spin sum Σ\|⟨s′\|σ·p\|s⟩\|² = 2\|p\|²; 1608.01994 Eq. (10) for X+ | STANDS | holds also for complex p (tr σ = 0); Eq. (10) [FT] is the ALP formula as cited |
| V27 | LE-46 (CW1.23) inversion; ×2.6/1.9/1.46/1.28 (OC-10) | STANDS | reproduced (C24); TA-only synthetic bound correctly labelled; TO-dominated ×1.17/1.08 correct |
| V28 | LE-47 GaAs: Γ ZPL unreachable (M_x v²/2 = 1.04 < 1.519 eV); band 0.43–0.51 (OC-12) | STANDS | arithmetic reproduced (C29); masses [UNVERIFIED] as stated |
| V29 | LE-178 (CW1.25) √ω₀ term; ΔZPR ≈ 0.2 meV; Si ZPR −56 meV [FT] | STANDS WITH CORRECTION | coefficient (2m)^{3/2}√ω₀/4π verified; my order estimate 0.2–1.5 meV (ℓ₀, m* uncertain), so "≲ 1 meV" → "≲ 2 meV [E]". "So in Si NA ≲ 1 meV" is not from 2011.12765 (its ASC −65 vs AHC −56 differ by 9 meV) |
| V30 | LE-179 (i) symmetric D^n at extrema [C]→[D]; (iii) piezo irrelevant [C]→[D] | STANDS | v_n·(ωk) = 0 at v_n = 0; Si/Ge centrosymmetric |
| V31 | LE-179 (ii) D/c ≈ 300 keV | STANDS | text cites c_LA = 8.18 km/s [CALC], C26 uses 8.43: 315 vs 306 keV, immaterial; align |
| V32 | IF-CW1-3: E_min^{ZPL}(0.90 keV) = 1.697 eV at ϑ = 0.34 | STANDS WITH CORRECTION | json confirms; scalar, a_PBE: SOC adds ≈ +10–16 meV off axis (V2) |
| V33 | Scope 2: claims about published papers | — | CW1 states no paper is wrong. 2011.12765: Table S5 Si −56, Ge −33 meV and the "more covalent materials (C, Si, Ge, AlSb, AlAs)" quote **CONFIRMED** [FT]. 1608.01994: uses 77 K data "where available" and asserts 77 K vs 4.2 K "even smaller" **CONFIRMED** [FT]; CW1's overestimate near the edge is an [E] TA-only bound |

## 0. [CALC] verification (scope 0)
- **Joint (q,k) minimum.** My 30 random starts (|q| 1.1–1.6 keV, random q̂ and k_v) converge to 0.399721 MeV (same q = (0.562, ±0.103, 0), k_v =
  (0.126, ∓0.107, 0)·2π/a and O_h images); other local minima 0.577, 0.602. The return's 18/21 starts agree. On-axis local optimum 0.415008
  (COMP-PH 0.4154). Second valence band restricted: minimum 0.415008 on axis (degenerate Δ₅ pair), i.e. the mirror-even partner opens at 0.415.
- **Convergence.** 40 vs 60 Ry vertices ≤ 2% (json). Wannier vs DFT at the optimum +11.5 meV (a_PBE). The pair energy at a_exp is not re-minimised.
- **SOC shift of the threshold (not in the return).** From out/vertex_soc.json (same fractional (k_v, k_v+q), a_exp, 40 Ry FR-1.1): SOC PBE gap 0.5374 eV
  (axis_extremum), mirror-optimum pair 0.7386 eV → E = 1.3711 eV vs scalar 1.3555 eV (vertex_opt_a10.2631: 0.7422 + (1.170 − 0.5567)): **+15.6 meV**.
  On axis (axis_pair) the shift is +0.9 meV. E_g(0) = 1.170 eV is measured from the Γ₈ (SOC) VBM, so the SOC-referenced value is the consistent one:
  m_χ^{ZP}(a_exp) = 0.4046 (scalar) → **0.4077 MeV (SOC)**, with local re-minimisation (dE = −0.9 meV) 0.4075. Physical reason: the off-axis hole sits
  61 meV below the VBM, beyond Δ_SO = 49 meV, so it does not share the Δ/3 rise of Γ₈; the on-axis hole (k = 0.05·2π/a) does. Off axis still wins
  (0.408 < 0.415), so V1 stands. The m_hh[110] = 2.5 m_e "flat direction" is a no-SOC object (4×4 k·p with SOC gives ≈ 0.57 m_e); the SOC energy at the
  point already includes this, but the optimum location with SOC is unknown (re-minimisation owed, cheap: a 3×3×3 stencil around the point, < 1 min nscf).
- **Vertices.** All json values match the text (0.150/0.1503; 0.157/0.156/0.154 lh only; 0.037 (1̄11); 0.40/0.25/2.21 Å; 3.0×10⁻¹⁴, 0.064 at −0.39 eV;
  1.38/0.31 Å; 0.0095, 0.024–0.036; SOC 3.2e-6/2, 5.3e-6/2, 2.57e-4/2). Not regenerable (save dirs gone).
- **Ratios.** ratio.json reproduces §2.3 and §3.2 tables (C16, C18 recompute independently). μ_x = 0.108 m_e, 𝔉_ρ extension 0.0172/0.0121/0.0104.
- **COMP-PAER/COMP-PH reconciliation.** COMP-PH 0.4154 = on-axis local optimum (five directions): confirmed. COMP-PAER (a_exp, 400 directions, 40³,
  bias −0.003) 0.405 vs CW1 scalar a_exp 0.4046: agree. COMP-PAER's (2̄00) 0.547 used nearest-pocket assignment by q; the X-face point (q_x ≈ −0.80)
  is nearer the G′ = 0 pocket and was labelled forbidden there. CW1's re-labelling rests on the computed vertex at the face (V8), not on the class.

## 1. Owed corrections (scope 1): target-by-target
| OC | verdict | required change to CW1's replacement text |
|---|---|---|
| OC-1 (L8) | STANDS WITH CORRECTION | "– 0.402–0.405 (1s) / 0.405–0.408 (continuum ZPL) MeV [CALC, a_exp; upper end SOC at the scalar optimum, not re-minimised]"; "PAER leads to ≈ 0.42–0.44" unchanged within its [E]; "0.547 MeV is the nearest-pocket (2̄00) value" OK |
| OC-2 (WP1 §3.4, IF-6) | STANDS WITH CORRECTION | same numbers as OC-1; "\|ρ\|² ≈ 0.01–0.04" → "0.01–0.04 (lowest band; 0.03 for the c₁+c₂ sum at the face)"; deletion of the 0.62 fallback stands |
| OC-3 (WP1 §3.7, IF-6b) | STANDS WITH CORRECTION | "0.35 at 100 meV" → "≤ 0.35 at 100 meV (outside the cone validity ε ≲ 0.08 eV; overcount)"; add "second hole band and SOC shift not included" |
| OC-4 (WP3 §M9) | STANDS WITH CORRECTION | (1) "m_χ^{PA} ≲ m_χ < 0.405–0.408 MeV [CALC]"; (2) "0.405–0.51 MeV" |
| OC-5 (WP3 §M3(c)) | STANDS WITH CORRECTION | replace "1.41 m_e used a DOS heavy-hole mass and is withdrawn" by "1.41 m_e (source not stated in WP3) is withdrawn; PBE, no SOC" |
| OC-6 (WP3 §M3(e), p̄_on) | STANDS WITH CORRECTION | p̄_on = 3 and crossover 1.35 keV stand; LA kink: "SOC admixture ≲ 10⁻⁴ on axis, ≈ 2×10⁻³ at the off-axis optimum [E, transfer of the CALC ZPL-vertex lift]" |
| OC-7 (WP1 §3.2(c), §10.6) | STANDS WITH CORRECTION | "\|ρ\|² ≈ (1.6–3.6)×10⁻⁶ at the extremum (Γ₈ sum bounded), 2.6×10⁻⁶ at the on-axis pair (0.3–0.5% amplitude)" |
| OC-8 (COMP-PH §0, §4) | STANDS WITH CORRECTION | "joint (q,k) minimum 0.405–0.408 MeV off axis (CW1 §1.2, SOC-corrected by VER-CW1)" |
| OC-9 (COMP-PAER) | STANDS WITH CORRECTION | "first zero-phonon final state 0.405–0.408 MeV (continuum)": i.e. COMP-PAER's number is *kept*, not replaced; the (2̄00) sentence stands |
| OC-10 (L9b) | STANDS | as written ("TA-branch bound" carried) |
| OC-11 (L3) | FALLS | do not apply; L3 keeps "≥ 12× (Cauchy–Schwarz, IP r ≳ 20), larger in medium (×2–9 on r), factor UNRESOLVED" |
| OC-12 (C8) | STANDS | as written |

Status upgrades: LE-24 Si → CLOSED stands with the V2 number; LE-25 → CLOSED stands (V8 caveat recorded); LE-27 → CLOSED stands; LE-35 "unresolved
in kind → value only" FALLS (V19; the row stays CLOSED-AS-EXACT-GAP with L3 text unchanged); LE-43 claim withdrawal stands; LE-45 stands; LE-178 stands
with V29 wording; LE-179 (i), (iii) [C] → [D] stand.

## 2. New derived results (scope 3): hypotheses, steps, limits
- (CW1.1): hypotheses (monotone m in E at fixed q, continuum edge) stated; correct. Limit: rigid scissor; SOC omitted in the energies (V2).
- Mirror rule: requires q, k_v in the plane *and* the parity labels referred to reduced-zone k with λ = ±e^{−ik·T/2}, T = σt_d + t_d = (a/2,a/2,0).
  The return states only "operator phase e^{−iG′·t_d}"; add the convention, otherwise "σ_z-odd relative to Δ₁" is undefined across the X face.
- (CW1.4): the relaxed-pair vertex along φ is ∂_{q_z}ρ + ∂_{k_z}ρ·dk_z*/dq_z (hole takes m_h/(m_e+m_h) of δq_z); the return uses ∂_{q_z} at fixed k_v.
  With 1.38 vs 0.31 Å the bias is |1.38 ± 0.25|² / 1.38² = 0.67–1.40. Validity ε ≲ β_θϑ² = 0.081 eV correct; the four O_h-related cones in a {001}
  pair overlap from the same energy (separation 0.26 rad vs semi-axes 0.20/0.16 rad at 0.1 eV).
- (CW1.5), (CW1.9), (CW1.20), (CW1.25), k_xc: algebra verified (sympy / residues). (CW1.5) scope restricted as V14.
- (CW1.12): formula stands as a definition; the composed L3 interval does not (V19).
- (CW1.23): exact for branch-resolved data only; for unresolved data the inversion is ill-posed (two branches, one spectrum): already implied, state it.

## 3. CLOSED-AS-EXACT-GAP rows (scope 4)
| row | single missing step? | spec sufficient (what / τ / method+convergence / pitfalls)? |
|---|---|---|
| LE-24 Ge | yes (QP E^{ZP}(q) on joint space) | yes; add SOC to the Si lesson; delete the anisotropy sentence (V5) |
| LE-26 | **no**: besides S^{PA} from the amplitude, the ZPL side is [E] (isotropic Wannier–Mott μ_x, second hole band omitted, unrelaxed ∂_{q_z}) | partial: no convergence criterion of its own (defers to tier H); add the ZPL side as a second item (anisotropic μ(Q) from §6 on the same bins) |
| LE-28 | yes (beyond-TDA run) | yes (G5: k grid, Haydock, f-sum < 1%); item (i) should test coupling vs retarded TDA, not vs resonant-only (V14) |
| LE-30 | yes (two-pair sector with W) | **no**: the control "(W.14) with W off vs (M.1)" tests only the W = 0 limit already proven by the M2 theorem; it cannot detect the open piece. Needs a computation that includes two-pair (biexciton-continuum) intermediates with W, e.g. a 1D two-band ED with contact W comparing (W.14) to the exact O(g) amplitude |
| LE-32 | yes (S_HR, ω̄, ρ_{λ0} for NaI as one chain) | mostly; no convergence criterion for S_HR vs supercell size (state: 64 → 216 atoms change < 10%) |
| LE-33 | yes (4-component code) | adequate by reference (G7) and the f-sum control; no k convergence criterion |
| LE-34 | yes | yes (control at W = 0, f_xc = 0) |
| LE-35 | yes (G10 mixed blocks) | yes; but the interval statement falls (V19) |
| LE-36 Ge | yes | yes; add an ecut/HSE-nscf convergence line |
| LE-39 | yes | **correction**: "Lebedev 110 points suffice to ℓ = 8 exactly" is false in general: the rule is exact to degree 17, so ∫K₈S is exact only if S has no ℓ ≥ 10 content; near the edge (minima at ϑ ≈ 0.18 rad) it has. Require a convergence test (110 → 230 → 434 points) |
| LE-41 | yes | **correction**: n = 3 cubic supercell (2π/3a) reaches \|q\| = 0, 0.76, 1.08, 1.32, 1.52 keV, not "1.16"; the "n = 3 → 4 at 1.15 keV" convergence test is impossible as stated (n = 4 has 1.14, n = 3 does not). The n = 3 and n = 4 meshes share no non-zero q below 2.28 keV (= 2π/a), so the test must use n = 3 vs n = 6 at a common q, or compare Λ(q) after interpolation in \|q\| |
| LE-47 | yes (band-structure check) | yes |

## 4. Proposed LIMITS rows (scope 5)
- CW1-L1: STANDS WITH CORRECTION: note "Si m_χ^{ZP} 0.405–0.408 (1s 0.402–0.405) MeV; leading correction: SOC (+0.003 MeV, included), re-minimisation
  with SOC (≤ −0.002 MeV, owed)". Validity: rigid scissor; Wannier interpolation ±11 meV.
- CW1-L2: STANDS; add the parity convention (§2).  CW1-L3: STANDS WITH CORRECTION (V8: c₁ vs c₁+c₂ at the X–W line).  CW1-L4: STANDS WITH
  CORRECTION (V10/V11 tags).  CW1-L5: STANDS WITH CORRECTION: "resonant-only ε₁ overstates L ≈ ×2; TDA coupling error unquantified".
- CW1-L6: STANDS WITH CORRECTION ((1.6–3.6)×10⁻⁶).  CW1-L7, CW1-L8: STAND.
- CW1-L9: source quoted correctly from full text (2011.12765 Table S5: Si ZPR_g −56 meV, Ge −33 meV; main text covalent-materials sentence refers to ASC,
  not to non-adiabaticity). Correction: "Si ΔZPR ≲ 2 meV [E, own estimate]; not stated in 2011.12765".

## 5. Smaller points
- C26 constant mismatch (8.43 vs cited 8.18 km/s). §1.2 "0.17·2π/a short of k_c" is with the Wannier k_c = 0.855 (DFT a_exp 0.843 → 0.155).
- §2.1 "for scale, Σ|ρ|² = 0.45 at 1.155 Å⁻¹" is a 4-conduction-band, direction-averaged sum, compared with a single-band 0.150: label it.
- §3.3 ε_ex^{max} is evaluated at the optimum |q| only; at fixed m_χ a different |q| can reach more. Direction of the bias: underestimates the open region.
- Interface flags IF-CW1-1/3/4/5 should carry the SOC-corrected numbers.

## Bottom line
The physics content (off-axis optimum, mirror-forbidden first ZPL, non-small (2̄00) vertex, withdrawal of the 0.62 MeV fallback, Kubo form of δρ^V)
survives. The headline number does not: with the return's own SOC calculation the Si zero-phonon edge is ≈ 0.405–0.408 MeV, i.e. COMP-PAER's value is
kept, not replaced. OC-11 / the L3 interval falls. The TDA, Lebedev, LE-41 mesh, LE-30 control and Ge-anisotropy statements need the corrections above.
