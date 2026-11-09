# Ch16 part 3: derivation check (s16-7, s16-8, s16-9, s16-summary, D-42)

Reviewer: derivation verifier (isolated), 2026-11-06. Brief: briefs/reviews/ch16-derivation-3.md.
I wrote my own scripts, which import nothing from figscripts/ch16:
/tmp/claude-0/-home-user-breakthrough-maths/30a63adb-c597-5cb8-b46c-4c5645c8b7d4/scratchpad/rv/{v167.py, v168.py, v169.py}
(sympy, plus scipy quadrature). The only cached input read was figscripts/ch16/zrte5_16.npz. Nothing was sent to QE.
Sources fetched into sources/review-ch16 and read as text: 2103.06977, 2512.16451, cond-mat/9409105, 2009.03804,
1610.03974, 1610.03981, 2012.10139, 1705.01108, 0802.2404, cond-mat/0604205, 2409.02820, 1910.02091, 1510.05528 and 1708.08929.
The PDFs have been deleted.
Line numbers refer to the tex files as they stand.

Verdict counts: no derivation in these sections is WRONG. There is 1 WRONG statement (the Liu fluctuation-versus-homogeneous
factor) and 9 GAPs. Every priority number reproduces.

## A. Priority items

A1 eq:16.7-dp, lim:16.7b, WE 16.7 (s16-7 l.86–119) → CHECKED.
- L = Im(−1/ε) = tanδ/[ε_r(1+tan²δ)] follows from ε = ε_r(1+i tanδ). Combined with eq:10.7-dp, R = (ρχ/ρT)ζ² tanδ₀ tanh/ε_r.
  It carries a single tanh, which is correct: the net rate is the population difference times the stimulated term. Dimensions are consistent.
- Numbers reproduced:
  - m_φ = 24.81 µeV, m/2T = 14.40, ρχ/ρT/ħ = 2.072e23 /g/s, R = 5.029e29 ζ²/(kg yr), ζ = 2.442e-15;
  - 22 mg film → ζ = 5.21e-13; ×1.10 and ×16.7 (ζ ×0.245, which the text prints as 0.24); tanh at 100 mK = 0.8937;
  - p_TLS = 0.2268 eÅ = 1.090 D; Ω_R = 5.5e-7 s⁻¹ (text: < 6e-7); τ₁⁻¹(u=1) = 1.07e6 s⁻¹; p_φ = 2.93e-8 eV, λ = 42.3 m;
  - lim:16.7b 10 % masses: 1.148 neV at 10 mK and 114.6 neV at 100 mK. The T² scaling from (π³/6)K T⁴/m² checks.

A2 DM–TLS rate 3.1e-2 against the campaign's 3.7e-2 (s16-7 l.146–161; Table 16.1; tab:16-nuisances) → CHECKED, inputs identified.
- eq:16.7-S: with S = (2π/V)𝒮 (eq:2.5-golden), the matrix element ¼|f|²u² and eq:16.7-norm, S = (π/2)P̄⟨|f|²⟩p₀(ω),
  and detailed balance holds.
- eq:16.7-rate: in eq:10.1-rateiso, ∫q dq η(q/2m) = 2m²⟨v⟩ (checked numerically to 1e-12), which gives ρχσ(1+m/me)²⟨v⟩P̄|f|²/(4 mχρT p⁻¹₀).
- eq:16.7-host: |f_host| = 2n_eγ/(ρc_l²) and P̄|f|² = 4n_e²C_l/(ρc_l²). The core average is 128[1 − sin qd/qd].
- My recomputation with the book halo (v₀ 238, v_esc 544, v_E 250.5 km/s):
  - n_e = 6.615e23 cm⁻³, ρc² = 4.619e23 eV cm⁻³, P̄ = 1.201e20, |f_host| = 2.864, P̄|f_host|² = 9.852e20;
  - ⟨v⟩ = 354.06 km/s, host 8.98e-3, core 2.207e-2 (R_core 2.457), total 3.106e-2 /(kg day meV);
  - median q 1.727 keV, q_× 0.706 keV, 3.1e-3 /(kg day) over 0–0.1 meV.
- Where the two numbers differ:
  - C: the book uses 2.6e-4 (Buchenau Table I); WP7-T-v2 §2.4 used C_TLS = 3e-4. This is a factor 0.867 on both the host and the core terms.
  - Halo: the book has an escape cut; WP7-T-v2 used a boosted Maxwellian without one. ⟨v⟩ is 354.06 against 358.24 km/s, and R_core is 2.457
    against 2.541. WP7-T prints R_core = 2.6, but 2.54 is what reproduces its total of 3.71e-2.
  - Cross-checks: book halo with C = 3e-4 gives 3.58e-2; campaign halo with C = 2.6e-4 gives 3.22e-2.
  - SOTA l.522 (3.7e-2) should note "3.1e-2 with C = 2.6e-4 and the escape-cut halo". The difference sits inside the factor 3.
- GAP (inputs). The text says the host term is fixed by the longitudinal C_l (eq:16.7-host). The number then uses
  C = 2.6e-4, which is Buchenau's soft-potential "average C", and the core term's P̄ = Cρc_l²/γ_l² does the same.
  With Golding's measured C_l = 1.9e-4, which l.58 quotes, host and core both scale by 0.731: total 2.27e-2, host 6.6e-3.
  Correction: either write "C_l ≈ C = 2.6e-4 (polarization average)", or quote the band 2.3–3.1e-2.
  The 16.9 row and the nuisance row inherit this.
- GAP (minor, l.146). q_× = |f_host|/(8d) uses the core displaced along q̂. The orientation-averaged core,
  ⟨|f_core|²⟩^{1/2} ≈ 4.62 qd, crosses at 1.22 keV. Add "for a displacement along q̂".

A3 Born validity, eq:16.7-Vopt/scrit, lim:16.7c (s16-7 l.222–246) → CHECKED.
- σ_crit = m⁴v⁴/(4πn₀²) follows from |V_opt| = E_kin with b = (σ/4π)^{1/2}.
  At 20 eV it is 1.1605e-38 (v = 1e-3), 2.406e-38 (1.2e-3) and 5.72e-37 cm² (v_max = 2.650e-3).
- V_opt/E_kin is 1.857 and 1.289 at 4e-38 cm². This matches the campaign (R12 1.86, REF 1.85).
- R/R_Born = 1 + x + 7x²/8 (sympy). The 10 % bounds are 0.0920 (repulsive) and 0.1096 (attractive); the text quotes the stricter one.
- Liu Eq. (14): n₀ = 2.69e24 and δn̄² = (7.29e22 cm⁻³)², so δn = 7.29e22 is read correctly. Sect. IV reach is ~4e-38 cm² at 0.02 keV.
  Eq. (12) is eq:16.7-Ffluc, and the transform 8πξ³/(1+q²ξ²)² checks by sympy.
- WRONG (l.220). "at qR ≫ 1 this beats the homogeneous term by a factor of order R/ξ_c". The sphere-averaged |F_homo|² is 9/[2(qR)⁴].
  At qξ ≫ 1 this gives |F_fluc|²/|F_homo|² = (4/3)(R/ξ_c)(δn/n₀)². For Ti–6Al–4V, (δn/n₀)² = 7.3e-4, so the
  homogeneous term can dominate.
  Correction: insert (δn/n₀)². The quotable wording of returns/R18/REF-DC-49-54-36.md §4 item 8 says exactly this:
  "for its own δn²/n₀² = 7×10⁻⁴ the homogeneous term it drops is the larger one below a few hundred eV on an equal-mass
  sphere". DC-36 is PARTLY VALIDATED, so quote only that wording.
- The claim "a bound is a conjecture" (l.246) is consistent with DC-RESULTS ("any bound from the reflection channel stays [C]").
  DC-36 has since delivered a force for a parametric model (REF §4 item 7). The phrase "until it is done" may stay, because the DWBA term is an exact gap.

A4 D.42 superconducting factor sinh(u)K₁(u) (D-42 l.50–69, eq:16.8-sc) → CHECKED.
- Coherence sum: summed over the four sign combinations, (uu′−vv′)² gives 2(1−Δ²/EE′).
  The normal-state integral is ∫dξ[f(1−f′)+f′(1−f)] = Δ_tl coth(Δ_tl/2T).
- Small-y limit: the coherence fraction (y+a)/[y(y+2a)]^{1/2} and the cosh substitution give a e^{a/T}K₁(a/T), so the ratio is 2e^{−Δ/T} sinh u K₁(u).
  I checked this step by step.
- Numerical eq:D.42-Rs, my own code:
  - 0.86256 against the closed form 0.86316 (T = 0.005Δ, Δ_tl = T), a relative difference of 7e-4 as stated;
  - 0.43802 against 0.44705 (T = 0.02Δ, 5T), the 2 % stated;
  - Δ_tl → 0 gives 2f(Δ) to 2e-10, which is Meißner Eq. (9).
- Meißner Eq. (9) is printed as W²π/(2ħ)(Δ/E)²E coth/(1+e^{Δ/T}), with "strictly only for E ≪ Δ_BCS".
  The ratio to Eq. (8) is 2/(1+e^{Δ/T}), so the book's statement of the source is exact. The new factor adds the condition E ≪ T.
- Values: 0.8632 (u = ½), 0.7074 (u = 1). sinh u K₁ = 0.9 at Δ_tl/T = 0.784 in the T ≪ Δ limit.
  The text's "≤ 0.7T" comes from the full integral at T/T_c = 0.2–0.8 (0.69–0.73) and is conservative: CHECKED.
- Expansion 1 + (u²/2)[ln(u/2) + γ_E − 1/6] and the large-u limit (π/8u)^{1/2} were checked with sympy. "14–29 % slower" is correct.

A5 Qureshi Γ(1+α)/Γ(1−α) (s16-8 l.66–100, eq:16.8-scaling, eq:16.8-qureshi, eq:16.8-Tcoh) → CHECKED.
- From eq:C.20-ohmrate at Δ_as = 0 and eq:C.20-Dr, 2Γ_LR = Γ(1+α)/Γ(1−α)·Δ_r^{2(1−α)}(2πT)^{2α−1}/α.
  The sympy ratio is 1.000000 at α = 0.1, 0.28 and 0.4.
- Qureshi Eq. (10) prints Δ̃₀ = Δ₀(Θ/ω_c)^K[Γ(1−2K)cos πK]^{1/2}, γ₀ = KΘ, Θ = 2πT, and he states K ≪ 1. The text matches the source.
- His Eqs. (8)–(9) at ε = 0 give a slow pole 2cos(πK)G(0). Divided by Δ̃₀²/γ₀ this is exactly Γ(1+K)/Γ(1−K) (0.7106 at 0.28).
  So the factor is what his own Eq. (9) loses in the step to Eq. (10). That step is a stated K ≪ 1 approximation, not a misprint, and the text frames it correctly.
- Numbers: 0.7106 (α = 0.28), 0.5576 (0.44), 10 % at α = 0.0907; T^{−0.44}; T_coh = 2.442 Δ_r; T_coh → Δ_r/πα.
  "Half of eq:16.8-black" for a symmetric defect at T ≫ Δ (πα·2T against παT) checks.
- K = α_ohm (exponents Γ(1−2K) and (Θ/ω_c)^{2K}) agrees with NOTATION l.1131 and with the partII note.

A6 Exact single-channel α_ohm (s16-8 l.30–35, eq:D.42-alpha, lim:16.8a(b)) → CHECKED.
- t = VΩ/(1+iπN VΩ) gives S = (1−iπNVΩ)/(1+iπNVΩ), so tanδ = −πNVΩ and δ̃ = 2arctan(πK_b^{1/2}) per spin.
  Then α = (1/2π²)·2·δ̃² = (4/π²)arctan²(πK_b^{1/2}) = 4K_b(1 − 2π²K_b/3 + …) (sympy).
- Values: K_b = 0.07 gives 0.1949 (0.696 of Born); 0.11 gives 0.2632; 10 % at K_b = 0.01715; the strength ratio is 1.319 (the text's "32 % stronger" checks).
- Born limit (D-42 l.28–35): 2J = 16π(N_F V_dΩ)²ω, so α = 4K_b. The factor 4 is the spin sum times the 2V_d difference. This agrees with CORRECTIONS §19.10 G-T1.
- Maillet Eq. (4) prints 4πKΔ₀²coth(ε/2T)/(ħε) with K = (n₀VΩ)² and a single-spin n₀ (their S035). The text reproduces it.

A7 Heat-release law and WE 16.8 (s16-8 l.136–175) → CHECKED, with one GAP.
- Excess energy ∫x/2[tanh(x/2T_lo) − tanh(x/2T_hi)] = π²(T_hi² − T_lo²)/12. The density is ½ per unit ln Γ, which gives 1/2t, so the prefactor is π²/24.
  This equals Sahling 2010 Eq. (6). Eq. (8) is eq:16.8-Tfrz with τ₀ = 1/Γ₀. Eqs. (4)–(5): A = 8π³k³/(ρh⁴)(…), and with h = 2π this is K_ph.
- Sahling 2014 Table I (a-SiO₂): P_C 8.0, P_Q 2.0 (×1e44 J⁻¹m⁻³), T*_n 4.8 K, T*_a0 14.5 K. Text p. 4: P_a/P_n = 3, P_a0/P_a = 0.05, τ_amax ≈ 100 s.
- WE numbers reproduced:
  - 𝒱 = 0.4545 cm³; P̄ = 3.204e19 eV⁻¹cm⁻³; tQ̇ = 1.642e-7 J;
  - 45.6 pW (1 h), 1.900 pW (day), 0.2715 pW (week); 0.841 µJ = 5.25e12 eV; ×4 with P_C;
  - P_C = 1.282e20; 100 g → 4.6 nW and 0.19 nW.
- GAP (l.174). "adds another 1.4 times the normal release": 0.15×(14.5/4.8)² = 1.37 from Table I.
  Sahling 2014 itself says the anomalous part is "roughly 2 times larger than the contribution of normal TLSs". Its text values T*_n = 5.5 K
  and 14.1 K would give 0.99. Mark 1.4 as "from the Table I freezing temperatures (the source states ≈2)".
- lim:16.8d: e^{28} spans 12.16 decades, and the 1.83–7.1e10 τ_min window is 10.6 decades: CHECKED (log).

A8 eq:16.9-power (s16-9 l.50–55) → CHECKED.
- ∂ln L/∂ln ε_bg = −2ε_bg(ε_bg + Re ε_D)/|ε_bg + ε_D|² = −2[1 − r + O(r², s)] with r = Re ε_D/ε_bg and s = |ε_D|²/ε_bg² (sympy).
  The reach therefore scales as ε_bg^{2(1−r)}.
- The Dirac fractions recomputed per axis are 3.2, 7.6 and 5.3 %, the text's "3 to 8 %". p = 1.87–1.94 implies r = 3–6.5 %, which is consistent.

A9 WE 16.9, the ZrTe₅ band (s16-9 l.57–71) → CHECKED where I could recompute; RELIED on the log otherwise.
- Tensors: Geilhufe Table 2 (308.4, 20.75, 126.1; g = 2) and Hochberg Table 1 / Geilhufe "Ref. [21]" (187.5, 9.8, 90.9). Both are quoted correctly.
- My recomputation:
  - leading-form ratio 0.3264 (direction-averaged 1/(q̂·ε·q̂)², Monte Carlo); share within 30° of y 0.645; (9.8/20.75)² = 0.2231;
  - α̃_y 0.155 → 0.327;
  - static Dirac term (gα/6π)v_i²/Πv·[ln(4Λ̃²/Δ²) − 5/3] = 9.80, 1.57, 6.71, leaving the remainder 298.6, 19.18, 119.39;
  - threshold masses along y 7.22, 9.39, 10.53 keV (Δ_D 12.0, 15.6, 17.5); axes 12.66, 9.39, 11.29; isotropic 10.49 keV;
  - from zrte5_16.npz: best reach 2.242e-40 cm² at 49.5 keV; published/book 4815–6562 (the text's 4800–6600); isotropic/book 0.36–0.44,
    so the text's "2.3 to 2.7" overstatement checks.
- Not recomputed (no cached arrays; the full anisotropic reach is a heavy run): B/A 0.345–0.362, 0.31, 8.10e-41, p = 1.84–1.94, C/A 0.893–0.896, ζ ratios 0.49–0.55.
  The we16_9.log values match the text exactly. "Band 2.8": 2.242/0.810 = 2.77.
- FLAG (superseded value?). Δ_D = 15.6 meV is the ISIF7 row of 1910.02091 Table 1 (gap 31.2 meV).
  CORRECTIONS v4 row 1543 says "use 11.8 (DFT, NR)", and SOTA l.621 lists 11.75 against 11.8 as an open conflict.
  The book's choice belongs to 16.1 (outside my files). WE 16.9's gap band 24–35 meV (Δ 12.0–17.5) covers 11.8 only to 0.2 meV.
  The coordinator should rule; if 11.8 is adopted, the threshold 9.4 keV becomes ≈7.1 keV.
- DC-RESULTS: REF-DC-49-54-36 §4 item 5 gives ZrTe₅ ×(4–6)×10³ (th.) and ε×6.2–6.3, with ±10–15 % accuracy.
  The book's 4800–6600 and 6.2 are its own calculation and are consistent with it. Do not cite DC-49.

A10 Summary and nuisance table against the sections → CHECKED, with these exceptions:
- Inherited GAP: the "3.1e-2" in Table 16.1, in the nuisance row and in the summary (3e-3/kg/day) all carry A2's C_l issue.
- Minor: summary l.9 and nuisance row (summary file l.49) "+29 to +35 % (light)". s16-4 l.85 says "at all masses above 2 MeV", and l.82 gives 10–35 % from 1.2 MeV. Add "above 2 MeV".
- Minor: summary l.15 (16.7) "optical potential exceeds about a tenth of the kinetic energy". The criterion 0.092 is on V_opt/E_n (normal energy). Say "of the normal kinetic energy".
- Table 16.1 nanotube row: q⊥r_t = 2v_D/3v_max is 0.760 or 0.858, and J₀² is 0.740 or 0.677 (v_D 3.02 or 3.41e-3). The 0.86/0.68 pair appears only in the table, but it is correct.
- Every other table and summary number matches the section text or the logs:
  - 16.1 numbers: 9.4–12.7, 98, 2e-40, 7.6, 6.2;
  - 16.2–16.6 numbers: 0.18–0.36, 1.94, 14.5 keV, 1.22 MeV, 1/1.44 = 0.69, 1/1.84 = 0.54, 7.3/3.4/2.6, 0.566 ≈ 0.57, 6.00, 4.6–6.7,
    1.33/0.39 (= 0.57^{−½}, 6.7^{−½}), 0.94/0.74, 1.47/0.56, 4.84/4.85/3.85, 1.2e-4, 2.6–8.8e17, 4.8e15, 0.186/0.113/0.255/0.41 GeV, 1.22–1.36 E_d
    (limit16_6a.log: 1.221/1.3625), 2 % above 2E_d, 42.9 MeV, 0.84/0.75, 1.28 k_F, 0.38, 0.95/0.85, 226 keV, 9π/8kR, 31 meV, 0.98, 0.08–0.13;
  - ζ bands 1.8 (= √3.2) and 4.1 (= √16.7); "seventeenfold" = 16.7.

## B. Other steps in s16-7

- eq:16.7-P and eq:16.7-norm → CHECKED (Jacobian E/Δ_as, dλ = −dΔ₀/Δ₀; ∫u(1−u²)^{−½} = 1; 86.6 % from u > ½).
  The source is Meißner Eq. (12), identical. The Δ_as ≥ 0 convention is consistent with Buchenau Eq. (6) (Q⁻¹ = πC tanh) and Sahling Eq. (6).
- eq:16.7-chires and eq:16.7-tand → CHECKED. χ″ = πP̄⟨b²⟩tanh. In Heaviside–Lorentz ε₂ = χ″, so tanδ₀ = πP̄p²/3ε_r.
  Buchenau Eqs. (4)–(6) (γ = ½∂Δ/∂ε, C_j = P₀γ_j²/ρv_j²) and Müller Eq. (16) (ε = 2γ·S + 2p·E) are quoted correctly.
- Relaxation: static χ_rel = 2b²(Δ_as/E)²∂_E tanh. The ratio eq:16.7-relax re-derived. The slow limit: u-integral 1/3, ∫z³/sinh z = π⁴/8,
  coefficient (π³/12)KT³/ω (numerical 2.58386).
- K_ph = 4.627e4 eV⁻². The 10 % temperature is 1.342 K by the estimate and 1.360 K from my full double integral (0.4244/0.4255 K at 0.5 GHz).
  The relaxation/resonant ratio at 10 mK, 5 GHz is 3.7e-9 ("4e-9"). All CHECKED.
- GAP (wording, l.71). "When every system relaxes fast, ωτ₁ ≪ 1, the u integral is π/4". If every system had ωτ₁ ≪ 1 the integrand would vanish.
  The plateau comes from ωτ₁(u=1) ≪ 1, with the integral dominated by small-u systems where ωτ₁ ∼ 1 (½∫dx/(1+x²) = π/4).
  Correction: "When the fastest systems (u = 1) relax fast, ωτ₁(u=1) ≪ 1, …".
- Buchenau citations (Eq. (8) saturation with I_c ~ 1e-7 W/cm², Table I with ρ, v_l, v_t and C = 2.6e-4, Sect. III Golding values) → CHECKED.
  Meißner Eq. (7) equals eq:16.7-tau1 → CHECKED.
- O'Connell Table I → CHECKED: thermal 300–330, PECVD 2700–2900 and SiN_x 100–200, all ×1e-6.
  GAP (minor, l.98): for a-Si:H the text quotes only the LC row, 22–25e-6. Table I also lists CPW 10–130e-6. Write "2.2–2.5e-5 (LC resonators)".
- eq:16.7-epsglass, eq:16.7-eps2, eq:16.7-CIR, eq:16.7-AB → CHECKED. Im[1/(ω_ν² − ω² − iωΓ)] → πδ(ω−ω_ν)/2ω. The normalization (M_I/NM̄)^{½} gives |p|² = S^Z/M̄.
  The weights ŵ ∝ c⁻³ and B^IR = ΣŵS″/(2c²M̄) check.
- Taraskin: A = 4000 cm⁻², ω̃_IR ≈ 35 cm⁻¹, Θ_D = 330 K → CHECKED.
  The printed "B = 0.3 cm⁻¹" is dimensionally a source misprint, since C is in cm⁻² and ω̃ in cm⁻¹, so B is dimensionless. The book's reading is right.
  α = C(ω)g(ω) is in the text before Eq. (1), and Eq. (2) is the rigid-ion C(ω). The citation "[Eq. (2)]" at l.178 should read "[Eq. (2) and text before Eq. (1)]" (minor).
- Recomputed values: Debye 229.36 cm⁻¹; at 10 cm⁻¹, α = 0.1002 cm⁻¹, ε₂ = 3.149e-3, rate 1.354e30; crossing at 0.4636 meV;
  (A/B)^{½} = 115.5 cm⁻¹; Bω²/A = 0.0919 at 35 cm⁻¹ → CHECKED.
- GAP (l.206). The crossing at 6.4 meV for tanδ₀ = 5e-3 lies above ω_IR = 4.3 meV, where the A + Bω² law and the Debye g no longer hold
  (the text says so itself, l.203). Add "(an extrapolation above ω_IR)".
- Zhou: γ_l/γ_t = 1.60 for a-SiO₂ and 1.44–1.84 over 18 glasses → CHECKED.

## C. Other steps in s16-8 and D-42

- eq:16.8-golden → CHECKED. The matrix element ½λ sinθ(n+1)^{½} gives Γ↓ = ½sin²θ J(n+1) with J = πΣλ²δ (eq:C.20-J).
- eq:16.8-Jph and the D-42 phonon block → CHECKED. λ² = 2γ²ω/(ρ𝒱c²) gives J = Σγ_ν²ω³/(πρc_ν⁵) = 2K_ph ω³, which is Meißner Eq. (7) and Sahling Eqs. (4)–(5) with h = 2π.
- Other values:
  - 2(c_l/c_t)⁵ = 16.57 (SiO₂) and 49.9 (Al);
  - Al rates: 1.778e5 s⁻¹ (phonon, 10 mK) and 2.487e9 s⁻¹ (electrons, α = 0.28);
  - Γ₁^el = Δ_tl at 1.51 K; π·0.28 = 0.880;
  - SC electron rate at 50 mK ≈ 1.9e-9 s⁻¹ (closed form);
  - the D-42 phonon wavelength is 165 nm.
  All CHECKED.
- D-42 l.11: the statement that Meißner's text "δε = γS" needs δε = 2γS for Eq. (7) agrees with CORRECTIONS (REF-WP7-T both referees) → CHECKED.
- Meißner Eq. (8) with W² = 4α_ohm is eq:16.8-black → CHECKED.
- eq:16.8-kappa → CHECKED: x/sin x gives 1 + u²/24 + 7u⁴/5760 (sympy). T_× = ω‡/2π, and 10 meV gives 18.47 K.
  λ_tun ≤ ln(1e13·yr)/2 = 23.60 uses the Phillips convention (Δ₀ = ω e^{−λ}) and agrees with the campaign's λ_P.
- Eckart barrier, my exact integral of the transmission: exact/classical = 6.156 at T_× and 2.218 at 1.5T_×; Wigner/exact = 0.902 at 2.1T_×;
  parabolic/exact = 1.090 at 1.5T_×. Lawrence p. 11 says ">6 at T_c, >2 at 1.5T_c, ≈20 % low" → CHECKED.
  The instanton value of 18 % is taken from the log and was not recomputed.
- eq:16.8-Tfrz → CHECKED (Γ₀e^{−V/T} = V|Ṫ|/T²).

## D. Conventions and NOTATION (drift report)

- No factor-2, π or sign drift was found in the rates. These conventions are consistent across 16.7, 16.8, C.20, D.42 and the sources:
  δΔ_as = 2γS, P̄ counting Δ_as ≥ 0, J_s = πΣλ²δ, α_ohm = 4K_b with a per-spin 𝒩_F, K(Qureshi) = α_ohm,
  Γ₁ = τ₁⁻¹ = population-difference rate, and e² = 4πα (HL) in eq:16.7-epsglass and tanδ₀.
- GAP (NOTATION l.1128). The P̄ row reads "per energy and volume". It should read "per unit asymmetry Δ_as ≥ 0, per unit λ_tun and per unit volume".
  Both qualifiers matter, because counting both signs doubles every rate (s16-7 l.20).
- GAP (NOTATION l.1130). 𝓃₀ is defined as "mean nuclear number density", but the text (l.215, l.220) and Liu Eq. (14) use the nucleon density.
  b_χN is per nucleon, so the coherent A is absorbed into the density. Change to "nucleon".
- GAP (NOTATION completeness). These 16.7/16.8 symbols have no row:
  - glass and TLS: γ_TLS, γ_l, γ_t, p_TLS, C, C_j, C_l, C_t, K_ph, τ₁ (with Γ₁, already flagged), λ_tun, ω_w, d_tun, M_tun, f_TLS, S^Z_ν, ŵ_ν;
  - random medium: V_opt, b_χN, ξ_c, E_kin, E_n;
  - kinetics and heat: Γ₀, ω‡, κ_PB, κ_W, T_×, S_inst, T_frz, Q̇_TLS, 𝒱, b_br, T_coh, J_s^ph, J_s^el, Γ₁^s, Γ₁^el.
  Note that C (tunneling strength) is close to C(t) and Ĉ(z) of C.20 and eq:16.8-qureshi.
  V_b against E_b is already in the editor notes; NOTATION l.1494 shows V_b was freed by the V_bias rename.

## E. Known editor-note items for these files: verdicts

| item | verdict |
|---|---|
| 3.1e-2 vs 3.7e-2 | CHECKED; the inputs are C (2.6 vs 3.0e-4) and the halo escape cut (A2). Update SOTA. New GAP: C vs C_l |
| Host term fixed by C_l alone | CHECKED (product independent of γ); in Table 16.1 |
| lim:16.7c, V_opt/E = 1.86 | CHECKED (1.857); the published reach lies in the non-Born regime. New WRONG: the R/ξ_c sentence (A3) |
| ε_r = 3.9, γ_l = 1 eV labels | kept as assumed (Table 16.1, l.101); no open source checked |
| Taraskin B units | CHECKED: the source misprint is cm⁻¹; the book's reading as dimensionless is correct |
| D.42 sinh(u)K₁(u) | CHECKED (A4); Meißner Eq. (9) is quoted exactly |
| Qureshi Γ(1+α)/Γ(1−α) | CHECKED (A5), including from his own Eq. (9) |
| α_ohm single channel 0.19 (0.70) | CHECKED (A6) |
| Meißner δε = 2γS | CHECKED for Eq. (7); only Eq. (7) is used |
| WE 16.8 46/1.9/0.27 pW | CHECKED; GAP on the "1.4" anomalous factor (A7) |
| "for Δ_tl ≪ T" in 16.9/summary | present in the summary (l.17) and the nuisance row (s16-summary l.61) |
| α_ohm 0.19 vs 0.28 printed ratio | consistent (0.696 → "0.70"; 0.19/0.28 = 0.68) |
| graphene v_D in Table 16.1 | both numbers correct (0.76/0.74 and 0.86/0.68); unify per ruling |
