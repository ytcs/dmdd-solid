# Ch11 revision log (2026-11-02)
Scope: tex/ch11/ch11.tex, s11-1 … s11-9, tex/appD/D-31.tex, D-32.tex; figscripts/ch11 logs; NOTATION.md rows + clash entry 80.
Sources: derivation-1 (d1), derivation-2 (d2), prose (pr), reader-a (ra), reader-b (rb), editor-notes R1–R12 and brief rulings (br).

## Opening (ch11.tex)
- pr/br paragraph 2 outline → done: one sentence (material numbers, checked against fuller result, electron-following sector, Chaps. 12–13).
- pr "Below about 10 MeV" → done: qualifier "where the free recoil energy reaches the phonon energies".

## 11.1
- br roadmap → done: three-sentence "We will…" cut to one sentence.
- d1-F O_A clash (NOTATION 637) → done: renamed O_N (nucleon-number operator); clash entry 80.
- ra/rb ω_q in eq 11.1-master → done: restated ω_q = q·v − q²/2m_χ as the DM energy loss, not a phonon frequency.
- pr l.11 "carrying the nuclei's forces" → done: "only through the forces they transmit between nuclei".
- pr l.33 CD2020 normalization bookkeeping → done: cut to the Eq. (7) attribution.
- pr l.35 "one for every purpose" → done: "one to 3×10⁻³".
- pr Γ zone-center typography → done: \mathrm{\Gamma} (l.44, l.164).
- pr l.59–63, ra m_p/m_u slow → done: one attribution sentence (composition drops out; applied to 2π/a, tested by the limit check).
- pr l.76 self-narration → done: deleted.
- pr l.97 long sentence → done: split.
- pr l.99 → done: replaced by the light/heavy statement.
- rb light-mediator "contributes … to the brackets" → done: reworded (q-integral; c_ν cancels the 1/c_ν weight).
- pr l.119 σ̄_n conversion → done: cut.
- d1 l.138 caption "2 %" → done: "3 %" (limit11_1b.log: 0.6329/0.6251/0.6128).
- pr l.155 count-teaser, 380-word paragraph, "largest transfers", "however" → done: split after Griffin Eq. (37); teaser replaced; "largest momentum transfers"; "However, it never exceeds".
- ra 654 /kg/yr reads as the 90 % value → done: parenthesized as the plateau.
- pr l.166 pitfall count-teaser + calibration rewrite → done.
- d1 l.175 "8.44" → done: 8.43.
- pr l.183 limitbox "computed here" → done: "from the Christoffel problem of the elastic tensor in Voigt order".
- pr l.202–210 Debye digression → done (partly): condensed; the keyresult stays because SPINE (LU4′) requires the elastic Debye temperature as a key result of 11.1.
- pr l.212 duplicate "A coupling to charge" → done: first sentence deleted.
- ra Ω for solid angle → done: dΩ_q̂ → d²q̂ in eq 11.1-cbarLA.
- d1-G limit11_1a/b/c have no .log → done: rerun (figures not rewritten), logs limit11_1a.log, limit11_1b.log, limit11_1c.log.

## 11.2
- br roadmap → done: one sentence (band integral; rate order reversed in reach).
- pr l.36 bookkeeping opener → done: calibration rewrite (Trickle et al., ions in the vertex).
- pr l.40 count-teaser/ordinal → done: the three conditions named in the opening sentence; "The small-q vertex is the condition that matters".
- br/pr "(modelling choice)" l.47 → done: tag dropped.
- ra "dynamical quadrupoles" undefined → done: one-clause definition.
- ra halo named two ways → done: "standard halo of Sect. 1.2" in the 11.2 captions.
- d1 l.71 "370 keV" GAP → done: replaced by the logged heavy full/one-branch ratio (1.0011 at 99 keV, fig11_2.log).
- d1 l.76 ω_L = 36.34 → done: "(DFPT)".
- d1 l.80 "850 at 32 keV" GAP → done: "about 840 near 29 keV" (fig11_2.log 835.8 at 28.9 keV).
- d1 l.80 acoustic "< 1 % below 100 keV" WRONG → done: "at most 3 %, near the edge, and about 1 % at 100 keV".
- rb Γ(v) "rate per particle" → done: scattering rate of one DM particle of speed v (dimension energy).
- d1-A ω̄ → ω̄_pol → done (text ×2, fig:11-limit-2b caption); NOTATION row added.
- R11 / d1 / ra sapphire bracket → done: [15.9, 45.4] meV as the formula gives it (36.3 is ~70 % up); 37.1 meV stated as the tighter bound with ω_L,max itself.
- br/pr 26 %/37 % repeat l.166 → done: cut (kept at l.38 and in Table 11.1).
- pr "easy to read off" → done: "The factors are:".
- pr l.199 false contrast → done: "The reversal is general."
- R6 / rb GaAs cell → done: a = 5.638 Å is the zero-temperature measured lattice constant of Table E.1, the cell of WE 5.6 and of the DFPT phonons, stated in WE 11.ipol; RT 5.653 Å (+0.8 % volume, −0.8 % ρ_T) stated. Neither case of R6 fits literally (not PBE-relaxed: PBE is 5.746 Å; not stray: it is the Chap. 5 value behind Z* = 2.11), so the value is kept and labelled. RT dielectric constants cited (Lockwood et al. 2005) at first use (l.38).
- ra sapphire ε₀ − ε∞ 6.58 vs 6.63 → no change: limit11_2cd.log prints 6.581 for the factorized ordinary-ray model, as the caption says.
- ra l.55 nucleon-vertex digression → kept: it is the Part II commitment (check of WE 8.6 against the full phonons); unchanged.
- rb p (Born-charge vector) vs momentum → no change: local to 11.2, defined in eq 11.2-eps.

## 11.3 and D.31
- br roadmap → done: "We will derive / bound / A last term" cut; one result sentence kept.
- rb/br 140 vs 90 keV impulse onset → done: "about 90 to 140 keV … by the two onset criteria compared there" (11.4: x_R = 4 → 92.5 keV, x_R = 9 → 139 keV).
- pr/Summary "about 7 keV" → done: 6.6 keV (limit11_3a); "ten percent" → \SI{10}{\percent} (l.3, l.122).
- pr l.28 bookkeeping → done: Ω/2π and s²₁,₂ clause cut.
- pr l.43 symbol dictionary → done: folded into one cited clause.
- ra/rb q₀ reuse (Kahn et al.) → done: q_osc² = 2M_κω₀; NOTATION row; clash entry 80.
- pr l.66 self-narration → done: deleted.
- ra two "0.44"s → done: the bond correlation coefficient is said to be distinct from j_BZ.
- d1 "above q_BZ within one percent" WRONG → done: "above about 2 q_BZ" (δ₂ −0.109 vs nn −0.085 at q_BZ).
- pr title "The coherent remainder" → done: "Exact phonon-order weights".
- d1 l.108 "5.1e-4 Å²" GAP → done: dropped (limit11_3a prints only the bond coefficient 0.443).
- br/rb certified band too fast → done: one worked line (n_at = 2: |a₁+a₂|² = 2(|a₁|²+|a₂|²) − |a₁−a₂|²; shifting q only in the Kronecker delta and zone-averaging turns it into 1/N, freeing the last phonon → P_n).
- pr l.122 calibration rewrite → done.
- d1 l.146 T/c_T → done: "with the Hill transverse speed c_T of Sect. 11.1".
- ra charge-vertex −i suppressed → done: "i G_α times the density component", with the translation phase stated.
- pr seam l.152 double pointer → done: "Sect. 11.5 asks …" cut.
- pr Warren without equation → no change (editor: book-level citation accepted).
- d1-F c_κ (species weight) → resolved: c_κ stays the per-species weight of 11.3 (12.6 already uses it "of Sect. 11.3"); NOTATION row added, clash entry 80.
- pr D.31 "of order" ×11 → done: three estimate uses → "∼"; the rest are "term of order n" (index, not estimate).
- pr D.31 l.87 `\end{equation*} Collecting` run-on → done: line break.

## 11.5 and D.32
- br/pr roadmap "We will find the corrections in this order" → done: cut; the opener ends on the exact-moment bound in one clause. "five percent" → \SI.
- br/d2-3/ra/rb "first three hold at any temperature" → done: D.32 new subsection "The moments at any temperature" proves all five for any thermal state of a time-reversal-invariant H (real eigenbasis, A_i = H − E_i, ‖[H,δD]|i⟩‖², mixed term imaginary; harmonic check E_Rω₀³coth(ω₀/2T)); keyresult now says all five hold at any T with thermal averages.
- pr "The second consequence" → done: "Time reversal adds a selection rule."
- d1-F 𝔫_κ clash (NOTATION 923) → done: momentum distribution renamed 𝔣_κ(p) (11.4, 11.5, D.32); NOTATION row; clash entry 80.
- br/d2-2/ra/rc E_kin range → done: ±0.2 % with the two extreme pairs named (closed form 1 − 44λ₃² + 12λ₄); σ_ω ≤ 0.09 meV; cumulative ≤ 2.5e-4 ("nearly three thousand times less" than the band); "for every practical purpose" → "to a part in a thousand". Same in WE 11.mkpeak.
- d2-4 18λ₃²k⁴ → done: two-kick amplitude 24λ₃²k⁴ minus 6λ₃²k⁴ from interference with k³/√6 and the O(λ₃²k) one-kick amplitude.
- ra ν as exponent → done: λ₃^j k^{2i} (text and limitbox).
- d2-12 Campbell-Deem Fig. 2 claim → done: "dominate near the on-shell LA resonance, where accessible".
- br/ra/rb Markov–Krein band too fast → done: the three-point canonical representation stated as five equations in five unknowns, bounds read off, one worked line for the Gaussian at its mean (0, ±√3; 2/3, 1/6, 1/6; moment check; F(0) ∈ [1/6, 5/6]); "node passes through infinity" explained in words; WE points back.
- pr Γ upright for Ashour's rate (and source symbols σ̄_n, μ_χn, F_med) → done: the source formula is replaced by a statement in book terms; no Γ.
- pr l.139 60-word sentence → done: split at the colon.
- pr "so" rate (44/10k) → done: five instances converted.
- pr "of order" l.48 → done: "∼".
- rb fermionic spin trace pointer (11.4/D.32) → done: one sentence in D.32 with the two contractions m³ρ²/q and mqρ² (ratio q²/m²).
- pr D.32 l.10 run-on (and l.46) → done: line breaks.
- d1-F cumulants c_k vs c_κ → kept c_k (12.5, written in parallel, prints c₃ as "the lattice curvature of 11.4"); NOTATION row and clash entry 80 record c_k (integer order) vs c_κ (species weight) vs c_ν (sound speed) vs 𝔠_b. Editor may rename book-wide.

## 11.4
- br roadmap → done: one sentence; ra/rb onset confusion (90 vs 70 vs 140 keV) → the opener says "above 90 to 140 keV depending on the criterion".
- pr count-teasers l.11, l.93, l.95 → done: "Its mean and variance follow exactly"; "The onset depends on the criterion"; the three effects named (anharmonicity, electronic excitation, displacement).
- pr l.37 symbol dictionary (Δ_d, ω̄_d, m_d) → done: cut, citation kept.
- d1 l.59 "88.1 meV; 68.4 %" GAP → done: dropped (FWHM 207 meV kept, logged).
- pr l.61 forward reference in WE → done: estimate source (Debye temperature 373 K) stated in one clause.
- pr "minimum speed" → done: "minimum velocity".
- pr "however" → done: l.80.
- d1 Kahn–Krnjaic–Mandava pointer → done: [text after Eq. (4)].
- pr calibration l.93 → done: "For germanium a rough ⟨ω⟩ is enough …".
- d1 l.107 "per unit volume" WRONG → done: "per dark-matter particle, in a target of free nuclei".
- pr l.109 ρ_χ 0.4 → 0.3 bookkeeping and σ_NC source symbol → done: cut; Dror et al. stated with σ_F.
- pr/br limit box N_T undefined → done: "per nucleus".
- pr duplicate 61 keV/16× in caption → done: caption's two edge sentences cut; text and the breakdown sentence keep them.
- "about 7 keV" → 6.6 keV (l.111). "the box" → "the limit check" (11.1, 11.3, 11.4).
- editor 11.4 (92.5 keV, ⟨ω⟩ 40.9, 139 keV; Ge 23.6 meV labelled estimate; c₃ vs 12.5 split; m²(1 − m/M)) → verified by d1; unchanged.

## 11.6
- br/pr/ra/rb 11.6 must not point forward to 11.8 for the cancellation → done: l.3 drops 11.8 (and the anthropomorphic "never noticed"); l.13 states the cancellation as derived here, credited to Mitridate et al. Eq. (44); l.27 contrasts with the zone-center line of 11.2; 11.8 now points back to 11.6.
- br roadmap → done: one sentence.
- pr l.61 calibration, "Before we compare" → done: rewritten into one sentence with "however"; process sentence deleted.
- pr l.89 deletion test → done: deleted.
- R10 / d2-1 ²⁹Si ratio → done: box "up to a factor of 2"; text "about 2, peak 2.05 at 57.3 meV … minimum 0.59 near 60.7 meV" (limit11_6a.log max |D29/D − 1| = 1.0402; positions per R10/d2 raw grid).
- pr l.111 caption process aside → done.
- pr l.121 70-word sentence → done: split.
- R3 / editor 11.6 absorption-coefficient uncertainty → done: "≈10 %" now stated where α is read off the figure (WE 11.iso); the later sentence keeps only the PBE-shift point.
- R6 / rc Si 64.1 meV source → done: named as room-temperature neutron scattering (Sect. 5.2) in WE 11.tail (s11-3) and in WE 11.iso; RT dielectric constants cited in 11.2.
- "one percent", "seventeen" → \SI / numerals.
- ra pair-term paragraph dense → no change (the T-matrix step is written out; reader followed it).

## 11.7
- br roadmap → done: "We derive … Symmetry then decides …" cut; "one/six percent" → \SI.
- R8 / d2-11 Υ_ℓ vs Υ_m (8.6) → done: halo multipoles renamed ℋ_ℓ (script H) throughout 11.7; NOTATION row; clash entry 80. App. F row (F-rows.tex l.282–286, outside this revision's files) still prints Υ_ℓ: editor item.
- pr "which we call the halo multipoles" → done: "the multipoles of the halo".
- ra cosine u vs velocity u (and 11.1's u = q/2m) → done: the cosine is x = q̂·v̂_E.
- ra Ω for solid angle → done: dΩ_q̂ → d²q̂ (3×).
- pr Y^c_ℓ used before definition → done: (eq C.3-cubic) cited in the keyresult.
- pr l.26 long sentence → done: split.
- ra halo "of App. A.8" → done: "standard halo of Sect. 1.2" (text and limit-check caption).
- pr/prose Al-Adulrazzaq normalization bookkeeping → done: cut.
- pr limit box in source notation (W_ℓm, 𝓡^(ℓ), f̂_ℓm′, "the book's notation") → done: the box states eq 11.7-rate in book symbols, sources cited for credit.
- d2-7 / ra / rb 1.79 vs 1.76 q_BZ → done: "just beyond the shell |G₁₁₁| = 3.95 keV = 1.76 q_BZ, at q = 1.79 q_BZ"; "at most 0.1" → "about 0.1 at most"; "0.2 to 0.4" → |S₄/S₀| 0.2, |S₆/S₀| 0.4.
- pr l.79 400-word paragraph → done: split before "A cubic crystal therefore modulates".
- d2-5 P₂ −0.495 → done: −0.497.
- d2-6 sapphire 0.6 % vs A_day 0.48 % → done: one-phonon 0.6 %, all phonon numbers 1.0 %.
- pr caption l.106 site tensors → done: weighted anisotropy B^cc/B^aa − 1 = +0.059 stated.
- pr l.112 → done: "In silicon both the electron and the nucleon rates modulate, and with the same phase."
- ra 2.84 vs 2.8 q₀ → done: WE says the model ends at 2.8 q₀ and the sliver up to 2.84 q₀ at the kinematic edge is dropped (as we11_8.py does).
- d2-8 0.05 % → done: 0.06 % (we11_8.log Si_lat 0.0006).
- pr "only" 52/10k → done: four instances rephrased. "one percent" → \SI.
- editor 11.7 (both symmetries; EPM labelled; sapphire/SiC estimates; WE at 2 MeV) → present; unchanged.

## 11.8
- br roadmap → done: "We will derive … We then turn to …" cut to one result sentence.
- ra eq 11.8-shift reproducible only after assuming the rank-one form → done: R_ab = R̃_ab + v_C R̃_aZ R̃_Zb/ε, ε = 1 − v_C R̃_ZZ restated.
- br/pr cancellation derived twice → done: 11.8 points back to Sect. 11.6 (coupling-to-mass cancellation) with the Mitridate citation.
- R12 / ra / rb 28 and 36 electrons → done: named as zero-field rigid-ion counts Z − Q; the field adds Q(1 − 1/ε∞); the counts in d are Z − Q/ε∞ = 30.724/33.276; the literal reading (d = −0.079/u, rate thousands of times larger) is stated as wrong.
- R9 / R5 / d2 / pr core kinetic-energy term → done: labelled a parametric estimate in 11.8 itself, sign stated (Δd ≈ +1.2e-4/u, |d| −10 %, rate −19 %), "Neither this section nor the literature" replaced; carried to 11.9. DEFERRED-COMPUTE entry (R5) is outside the files of this revision: editor item.
- R4 l.95–99 near-duplicate → checked: distinct paragraphs (Mitridate; core/mass/frequency terms; DFPT inputs), no merge; l.99's repeat of the "Z*/ε∞ to 1 %" sensitivity cut (pr).
- br/pr "(modelling choice)" ×3 → done: "widths set to 1 %", "an assumed width of 1 %", "𝔔 = 100 for visibility".
- pr limit box l.67 describing the source's method → done: the box states eq 11.8-Gamma in book symbols.
- R11 / ra / rb sapphire 35.9 vs 36.3 meV → done: 35.9 meV is ⅔ ordinary + ⅓ extraordinary (fig11_8.log 35.868), ordinary alone 36.3 meV of 11.2; "same comparison as for scattering" made explicit (per-mass band integral of 11.2-band).
- R7 / d2-10 t_coh → done: t_coh = 1/(m_φ v₀²) = 1.05 ms at 1 μeV (no 2π).
- ra halo of App. A.8 → done: standard halo of Sect. 1.2 (text and captions).
- Trickle's "Q_DM ∼ 10⁶" quote in source notation → done: 𝔔_DM.
- Arvanitaki d_{m_e}, d_e, G_N (unregistered source symbols, d clash) → done: described in words, cited.
- rb N (depolarization) vs N (cells) → done: N_dp.
- editor 11.8 (rigid-ion 8.2×, resonator 1.8×, Z* 2.11/ε∞ 10.88) → verified by d2; unchanged.

## 11.9 and Summary
- pr/br l.3 plan sentences → done: cut; the band result kept.
- br/pr de-duplicate nuisances → done: the restating paragraph after the table (old l.62) cut; its one new clause (errors of a simpler calculation, factors 16 and 8.2) moved into the free-recoil paragraph; table-description sentence (l.31) cut.
- br 26 %/37 % repeats → done: kept in 11.2 (first statement), Table 11.1 and the Summary; cut at s11-2 l.166 and s11-9 l.23.
- br/d2-2 E_kin range → done: ±0.2 % in text and table. WE 11.band30 keeps the logged template −0.14 % (named pair; we11_10.log) and states that the −0.2 % extreme gives −1.2e-4 (0.12 × −0.1 %), σ_lnR unchanged at 2.4e-3.
- d1 acoustic charge < 1 % → done: "at most 3 % near the edge, 1 % at 100 keV" (text and table).
- R9/R5 core term → done: sign and size (rate −19 %, parametric) in text and table; points to 11.8.
- R3 → done: 11.9 cites WE 11.iso for the ≈10 % reading.
- R2 → done: frequency row labelled "uniform rescale (upper estimate)".
- R1 → done: 100 meV and σ_p stated once in the WE set-up as illustrative choices.
- pr ℛ^𝔗 undefined → done: defined at first use in the WE (central values of the truncation labels, Sect. 10.10).
- pr "named but not sized here", "computed neither … nor in the literature", "a modelling choice" → done.
- d2-9 MK band 0.95 → resolved as 80.4 keV: we11_10.log prints [0.194, 0.949] at q = 80.4 keV (0.944 is the value at exactly 80 keV); text now says 80.4 keV, band 0.19–0.95.
- ra "6.8 % lower" vs 6.65 % → no change: we11_10.log prints (free − central)/central = −0.068 from unrounded rates.
- pr Summary "ten percent", "six percent", "about 7 keV" → done: \SI; 6.6 keV. Onset sentence → 90–140 keV (Si) and 113–170 keV (Ge) by criterion.

## Notation (NOTATION.md)
- br/d1-F/d2-11 register new symbols → done: 33 Ch11 rows after the Γ_iso row (O_N, A_cell, m_u, q_up,ν, c_LA,max, ℛ_light, I₀, Δ_C, A_Z, s_Q, p_Q, v_L/v_T/v_m/G_V/G_R, K_η, ℐ_pol, w^pol_ν, ω̄_pol, ω_L,max, ω_T,max, γ_L, c_κ, 𝔚^(n), 𝔓^(n), δ^coh_n, j_BZ, q_osc, c_min, D/δD, p_q̂, E^kin_κ, σ_ω, c_k, 𝔣_κ, q_abs, Γ_V, λ₃/λ₄/ℓ₀/q_×, r_L, g_i, δ^M_i, h_iso, 𝖦_h/𝖦_i, x_κi, g_B−L, 𝔟, Ω_at, S_OO, ℋ_ℓ, f̂_gal, Y_ℓm, S_ℓm, L_ℓ, A_day, ℛ_ℓ, b̄_κ, Δb_κ, 𝒢^φ_κ, O_φ, d, χ_ab, p_a, x_a, f_sh, N_dp, h_mod, 𝔔 family, resonator and bar symbols).
- d1-A κ_η row → done: "3.14 for c → 0 and 3.09 at the sound speed of Si".
- br O_A, 𝔫_κ, c_κ clashes; R8 Υ_ℓ → done: clash entry 80 (renames, kept symbols, F-rows follow-up).
- Check: check_notation.py on ch11/*.tex, D-31, D-32 → 0 gaps (was 93); default file set → 0 gaps. Bare 𝒞 in D.31 given its subscripts.
- rb η/η_anh, κ/κ_η → no change (decorated, registered rows); ra Ω for solid angle → done (d²q̂ in 11.1, 11.7).
- br "every symbol inside each Limit Check box in book notation" → swept all 20 boxes: rewritten 11.4b (N_T), 11.7a (W_ℓm, 𝓡^(ℓ), f̂_ℓm′), 11.8a (method sentence → formula); 11.5 Ashour formula (Γ, σ̄_n, μ_χn) removed from the text; remaining boxes use book symbols only (checker clean).
- br upright Γ never a rate → done: the only upright Γ rate (11.5, Ashour) removed; zone centre is \mathrm{\Gamma} throughout (11.1 fixed).

## Prose register (pr Sect. C)
- "so"/"only"/"gives" rates → partly: converted where touched (11.1, 11.5, 11.7); "however" added at 11.1 l.155, 11.4 l.80, 11.6 l.61. "typical"/"note that" not introduced (no natural place without padding).
- American spelling "modeling" → done: no "modelling" left in Ch11 (all were "(modelling choice)" tags, now removed).

## Build and lint
- latexmk -pdf -outdir=/tmp/build-ch11rev: 0 LaTeX errors ("! " lines), 0 undefined citations; no undefined references to any Ch11, D.31/D.32 or touched label (the 68 undefined labels are unwritten chapters/appendices, e.g. chap:13, app:B.2, sec:15.2, sec:18.2). latexmk stops with "needed too many passes" because of those unresolved forward references, as in the editor builds.
- lint: 0 blocking hits; the long sentences introduced by this revision were split.

## Outside the files of this revision (editor items)
- App. F planning table: n_T = 2 (Limit Check 11.3b), n_A = 2 (11.5a); F-rows.tex l.282–286 still print Υ_ℓ (now ℋ_ℓ).
- SPINE: 11.7 "inversion or time reversal" → "both"; 11.6 headline already updated by the editor.
- DEFERRED-COMPUTE: GaAs core-kinetic-energy term (R5).
- E.17: Z* 2.16/ε∞ 10.9 vs book 2.11/10.88 (App E pass 2); E.19 helium Lindemann 0.3 vs "about a quarter".
- c_k cumulants: book-wide rename optional (12.5 prints c₃).
- R10 positions 57.3 meV/0.59 at 60.7 meV are from the reviewer's raw-grid evaluation; limit11_6a.log prints only the maximum (2.04) and the 10 % boundary — rerun of an extended script would put them in the log.
- Advisor pass: 11.5 three-phonon interference attribution corrected; Lindemann distance d → d_nn (row + entry 80); "three percent" → \SI; s11-7 literal \n fixed (coordinator note); rebuild 0 errors.
