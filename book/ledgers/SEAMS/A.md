# SEAM: Appendix A (Conventions and units), A.1–A.9

## The reader now knows
- A.1: ħ = c = k_B = 1; CODATA 2022 conversion table (tab:A-conversions); metric (+,−,−,−); dimension counting (S ~ eV², Ṽ ~ eV⁻², σ̄_e ~ eV⁻²); 1 kg⁻¹ yr⁻¹ = 3.718e-59.
- A.2: Heaviside–Lorentz e² = 4πα, e > 0, electron −e, v_C(k) = e²/k²; map e² = 4πe_G² = e_SI²/ε₀^SI; ω_p, ε_GG′, σ_cond (σ₁ = ωε₂) in three systems; field and μ_B conversion.
- A.3: O(q) = ∫e^{+iq·r}O(r), f(ω) = ∫e^{+iωt}f(t); why the plus sign (eq:A.3-vertex); retarded analytic in Im ω > 0; box normalization; zone averages incl. ⟨⟨·⟩⟩; lattice Fourier series and the plane-wave-code sign (G → −G); unreduced-q indexing M_00(q) ≡ M_{G_qG_q}(q_r).
- A.4: q DM → target, never folded; ω to target; Δ_χ; ω < 0 via detailed balance; S(q) = S(−q) under P or T (derived), so the sign matters only for P- and T-broken targets.
- A.5: ψ over V, u over Ω; periodic gauge; ρ_mn(k,q) O(1), ρ_nn(k,0) = 1, Umklapp in the plane wave; optical limit q·v_mn/(ε_mk − ε_nk) (derived); gauge transformation of ρ and v; one gauge for ρ, g, Wannier tensors; SOC spinor convention; Wannier definition; v, c only as subscripts.
- A.6: displacement expansion, Σ_κ|e|² = 1, e(−Q) = e(Q)*; D^dyn sign; ℓ_Qν with N outside (derived for acoustic modes); EPW g normalization; hermiticity (derived); weights n + ½ ± ½; g^AH vs "Debye–Waller" = e^{−2W} only.
- A.7: R not χ; R_ab and S_ab definitions; Lehmann form; Im R_aa < 0 at ω > 0; FDT and detailed balance; ε_GG′ (unsymmetrized), ε_mac, L, ε_e⁻¹ = 1 + v_C R_ee; S–L relation; spin factor 2; f-sum π𝓃q²/m over ℝ, ∫₀^∞ωL = (π/2)ω_p², per-particle form.
- A.8: SHM set (points to 1.2); v_E(t) in integrals vs v_E^ref, v_max for reference scalars; η/(2q) kernel for direction-independent S; anisotropic S keeps full kernel; rate per unit target mass derived (eq:A.8-rate, -rateiso = eq:1.5-rate); |f_crystal|² = q³ΩS̄/(4παm_e²) dictionary.
- A.9: σ̄_e, F_DM, reference-point and in-medium conversions; |M_free|² = 16m_χ²m_e²|Ṽ|²; spin average; dσ/dq = qσ̄F²/(2μ²v²); σ_p, σ_N; heavy dark photon σ_p/σ̄_e = (μ_χp/μ_χe)²; kinetic-mixing sign; relativistic limit.

## Symbols introduced (with defining equation)
- e_G (Gaussian charge, e_G² = α), e_SI, ε₀^SI (eq:A.2-map) — e_G and e_SI are new.
- f_G lattice Fourier component (eq:A.3-periodic); ⟨⟨·⟩⟩ zone average over k and Q (eq:A.3-BZ); M_00(q) unreduced indexing (eq:A.3-unreduced).
- L_e (electron-channel loss), S^prop (eq:A.7-SL); S̄ angle-averaged S (eq:A.8-rateiso); ξ(v_min), η̃(v_min) (A.8 text).
- 𝓜_free (relativistic free amplitude), c₁ (A.9 text); θ_W (weak angle, A.9 text only); V_NL (nonlocal pseudopotential, A.5 text); μ_B, g_e (A.2 text; g_e is NOTATION clash 20's magnetic-context use).
## Terms introduced
- periodic gauge; unsymmetrized/symmetrized dielectric matrix; zero-point length; Allen–Heine vertex (vs Debye–Waller); reference scalar.
## Threads: opened / advanced / closed
- Closes the forward pointers app:A.1, A.2, A.3, A.4, A.8, A.9 from Chap. 1 and C.9.
## Promises made to later sections
- 4.1/4.2: Kubo definition (eq:A.7-R) and FDT stated here, derived there. 4.3/D.6: f-sum. 4.4: ε_GG′, ε_e vs total ε. 5.2: D^dyn sign convention (eq:A.6-Ddyn). 5.6: 2W = q·B_κ·q. 6.2: g normalization (EPW). 6.5: ⟨⟨·⟩⟩ and one-gauge rule. E.7: nonlocal correction of velocities.

## Open questions / for the editor
0. Word count 7214 by wc on the .tex files (prose-only lower).
1. **Kinetic-mixing sign.** NOTATION's editor note says "ℒ ⊃ −(ζ/2)F_μνF′^μν" per Lin Eq. (70). The fetched Lin text (sources/A/1904.07915.txt, Eq. (70)) has **+(κ/2)F_μνV^μν** with +eA_μJ^μ_EM; C.9 (eq:C.9-mix) and 1.4 also use +(ζ/2). A.9 follows the written text (+). The NOTATION note should be corrected.
2. Chapter 1 uses v_min with absolute value (followed); conventions' signed form not used.
3. f-sum: A.7 states ∫₀^∞ωL_e = (π/2)ω_p² at any T (follows from detailed balance and S(q) = S(−q)); the source conventions said T = 0 — the T-independent statement is the stronger correct one.
4. Jackson (3rd ed.) "Appendix, Table 3" cited from memory [UNVERIFIED equation/table number]; Adler 1962 and Wiser 1963 cited without equation numbers (closed access). Bernreuther 2024 entry has no DOI (not given by arXiv API).
5. The silicon valence plasma energy 16.6 eV (A.2) is computed here from a = 5.431 Å, 4 e/atom; 4.3 should use the same value.
6. A.6 relies on Giustino Eq. (14) for D^dyn with e^{+iQ·R}; writer of 5.2 should match.
7. Lint: one remaining LONG-SENT hit in A-1 is the conversion table (tabular cells read as one sentence); no prose hit.
8. Undefined references (all to unwritten targets): app:B.2, app:D.6, app:E.4, app:E.7, sec:2.2, sec:3.1, 3.2, 3.5, 3.6, 4.1, 4.2, 4.3, 4.4, 5.2, 5.5, 5.6, 6.2, 6.3, 6.5, 7.1.

## Proposed ledger rows (the editor merges them)
NOTATION: e_G | Gaussian elementary charge, e_G² = α | 1 | A.2 · e_SI, ε₀^SI | SI charge and vacuum permittivity (quoted SI formulas only) | — | A.2 · f_G | Fourier component of a lattice-periodic function, Ω⁻¹∫_Ω e^{+iG·r}f | as f | A.3 · ⟨⟨·⟩⟩ | zone average N⁻²Σ_{kQ} | — | A.3 · L_e | electron-channel loss Im[−(ε_e⁻¹)_00] | 1 | A.7 · S^prop | structure factor of R̃_ee | eV² | A.7 · S̄(q,ω) | S averaged over directions of q | eV² | A.8 · ξ(v_min) | 2∫_{v_min}^∞ v′η(v′)dv′ | 1 | A.8 · η̃(v_min) | ρ_χσ̄_eη/m_χ | — | A.8 · 𝓜_free | relativistic free DM–electron amplitude | 1 | A.9 · μ_B | Bohr magneton e/2m_e | eV⁻¹ | A.2 · V_NL | nonlocal part of a pseudopotential | eV | A.5 · z_e, z_κ | charge numbers −1 and Z_κ in species sums | 1 | A.2 · D^{dyn,αβ}_{κκ′}, Φ^{(2),αβ}_{κκ′} | Cartesian components written as superscripts (clash 17) | — | A.6
GLOSSARY: periodic gauge | ψ_{n,k+G} = ψ_nk | A.5 · reference scalar | threshold/edge quantity evaluated at v_E^ref | A.8 · Allen–Heine vertex | second-order e–ph vertex g^AH (not "Debye–Waller") | A.6 · Debye–Waller factor | e^{−2W_κ(q)} only | A.6
CONCEPTS: Heaviside–Lorentz charge (A.2); box normalization and N-independence (A.3); sign of q under P/T (A.4); gauge covariance of second-order amplitudes (A.5); FDT/detailed balance (A.7); per-mass rate (A.8)
CLAIMS: |f_crystal|² = q³ΩS̄/(4παm_e²) (A.8, derived; matches KKL Eq. (16)) · ε₂ optical prefactor 8π²α/(Ωω²) ↔ 8π²e_G²/(Ωω²) (A.2) · ∫₀^∞ωL_e = (π/2)ω_p² at all T (A.7, derived)
INDEX: natural units; conversion factors; Heaviside–Lorentz units; Gaussian units; Fourier convention; box normalization; Umklapp; periodic gauge; density vertex; optical limit; Wannier function; polarization vector; zero-point length; electron–phonon vertex; EPW; Debye–Waller factor; Allen–Heine vertex; Kubo formula; Lehmann representation; fluctuation–dissipation theorem; detailed balance; dielectric matrix; loss function; spin factor; f-sum rule; standard halo model; rate per unit mass; crystal form factor; reference cross-section; kinetic mixing

Revision rows (Chapter 2 review):
NOTATION: | η_2(v_min) | second speed moment 2∫_{v_min}^∞ dv′ v′η(v′) (replaces ξ, which is the energy mismatch of 2.1) | 1 | A.8 |
NOTATION: | r_p | residue of the decaying pole, 1/(1 − R′(z_p)) (D.3; replaces Z, the atomic number; not the quasiparticle residue z_qp) | 1 | D.3 |
NOTATION: A.9 now writes σ_T, σ_N, μ_χe, μ_χN and dΩ_q (decorations mandatory, clashes 31, 32).

## Revision after the Chapter 6 review (2026-11-02)
- A.6 §Second order: the sentence "The two objects enter sum rules with opposite effects (5.6, 6.3)" is replaced by what 5.6 and 6.3 show:
  e^{−2W_κ} and Σ^AH share B_κ and sit next to the first-moment double commutator (eq:4.3-firstmoment) in different roles, the elastic share of
  the weight whose mean energy the sum rule fixes (5.6), and the Fan–Allen–Heine cancellation for a rigid translation (6.3). See SEAMS 6.3.
