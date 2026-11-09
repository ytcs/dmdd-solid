# Chapter 8, mock reader b: personas (b) particle physicist, (c) condensed-matter theorist
Sources: the PDF build (Nov 1 23:46) is older than the sources, so I read the .tex: ch08/ch08.tex, s8-1 … s8-8, and appD/D-24 … D-28. I did not open any brief, ledger, SPINE or notation file.
Method: I read linearly and redid the algebra by hand, with sympy and numpy where helpful. I re-ran every worked-example number I could, including a full numerical diagonalization of we:8-sectors. Notation for each line: `lost | not reproduced | UBD (used before defined) | pace | LO (inferred learning outcome: ✓ = I can do it now, ✗ = I cannot yet)`.

## Persona (b): particle physicist (QFT, no solid state)

**8.1 Couplings.**
lost: none. The reduction is clean. I checked the O3, O7, O8, O12, O13 and O15 rows of tab:8-operators term by term, the T_s identity (K² = q² + 4k·k'), and the longitudinal identity q·v⊥ → Δ_χ n_e via [H, e^{iq·r}] = q·j.
not reproduced: none. Checked: the D.24 bilinears (scalar 1 − K²/8m², γ⁰ 1 − q²/8m², iγ⁵ → −iq·S/m), ^29Si (0.312, 0.073, 10 %), we:8-darkphoton (3×10⁻⁶, 7×10⁻⁶ and 1.3×10⁻³, 1.9×10⁻⁵, 1.4×10⁻⁴), we:8-O2 (k_F = 3.57 keV, annulus 2.50–3.37 keV, ⟨B⟩ = 3.37×10⁻⁵, ⟨B²⟩ = 1.17×10⁻⁹, total 1.46×10⁻⁹, a factor 90 above v⁴).
field flag (spin): the claim that the list is complete ("products of more than one spin … reduce to at most one by the Pauli algebra", fifteen operators) holds for spin ½ only. Yet 𝔇_ab (eq 8.1-D) and the spin traces of D.24 are written for general |S_χ|. Spin-1 dark matter has further operators (Dent et al. 2015). Either restrict the list to spin ½ explicitly or add one sentence on the extension.
minor: we:8-O2 calls the 4A⟨B⟩ share (20 %) "interference through the current row". Half of it, the 2AB from (A+B)², is the n–𝒯 cross term, and only the other half is |j|². The 80/20 split is a split in A and B, not in rows.
UBD: none. pace: the Dirac-bilinear recap and the vector-mediator algebra are slow for me but right for persona (a).
LO: reduce any 𝒪_i to rows ✓ (I did O14: (i/m)(S_χ·q)(v̄·s − 𝒥^{αα})). Build 𝔇_ab for a spin-½ model ✓. Get nuclear coefficients from ⟨S_p⟩ and ⟨S_n⟩ ✓. Name the absorption rows of the ALP and the scalar ✓.

**8.2 Master formula.**
not reproduced: none. Checked: Tr[𝔇Sᵀ] − Tr[𝔇S] = 2Tr[𝔇_I S_I] (D.25 signs consistent), the 35 eV band maximum at 26.5 keV, |f|m_V = 2×10⁻⁸, the 7 eV occupation threshold, t_coh ≈ 1 ns, Γ_net = ζ²σ₁, and dark-matter detailed balance. we:8-cross: S↑ = 5.57×10⁷ eV², the 19.2 eV edge, the cross term c₁c₇v_T S↑ (longitudinal parts cancel ✓), the factor 4.0 S↑, the bound 5.7×10⁻⁵ (so "at least five", actually 6.6), the 8.4×10⁻⁴ wind term, and S_ns/S_nn = 0.068 at 10 eV for polarization 0.5.
UBD: "the truncation label 𝔗 of 8.5" and "the thermal order n_T" are forward references. They carry no weight here.
pace: good. The classical-field paragraph is the right length for me.
LO: write the rate of any model ✓. Reduce it to eq 1.5-rate ✓. Absorption rate and −Im Π/ω ✓. Fermionic absorption ✗, deferred: 𝔇_ab for a relativistic ν̃ is built only in 10.9.

**8.3 Exact relations.**
lost: briefly at "the mixed third moment … set by the contact density". It resolved once I did the commutator chain myself: [[n_e†,H],[H,[H,n_κ]]] = −(nm M)⁻¹ Σ e^{−iq·y}(q·∇)²w ✓.
not reproduced: none. Checked: the FT of (3cos²−1)/y³ = −8π/3 gives the 2n_e/3 term ✓; ∫j₂(x)/x dx = 1/3 (sympy) ✓; A(x) → 1 and → 1/3 ✓; (8.78 keV)², (8.76 keV)² and (2.34 keV)² from the stated n_e^(κ) ✓; the Ward cancellation m_e M³_ee + ΣM_κ M³_eκ = 0 at O(q²) ✓; jellium limit n q² ω_p²/m ✓; harmonic chain (one-phonon ratio q/Mω, two-phonon amplitudes, dispersion from the flux, 8.8×10⁻⁴) ✓; M³_ss kinetic bracket ✓; ω^{−9/2} tail ✓. The 1765 a₀⁻³ Hartree–Fock contact density I accept on trust (hydrogenic estimate ≈ 1650).
UBD: "Born–Oppenheimer approximation, n_B = 0" is used before 8.5 defines n_B. pace: fine.
condescension: "The name follows field theory, where a Ward identity is …" is borderline for me and harmless for (a).
LO: apply the interference bound ✓. Derive eq 8.3-M3lim ✓. Use the Hankel inequalities ✓. Show the q⁴ suppression of a mass coupling ✓.

**8.4 Screening.**
lost: Coulomb-line classes (8.4-lines). The tree-plus-one-cycle topology I follow (D.27). But the physical job of the *pair* lines (W^scr between "two halves of the amplitude") is deferred to 13.4, so I cannot judge the claim that leaving them out "is an omission". This passage is too fast.
not reproduced: none. Checked: the push-through to eq D.27-screened, vR_ZZ = ε⁻¹ − 1, the GaAs pole move T→L with unchanged weight, a_N = 9.4×10⁻⁴, 0.61 and 4.5, 650, 7×10⁻⁵ and 4×10⁻³, 0.02 eV, Z*/ε∞ = 0.19, |ε|² = 774 ≈ 770, Π_L → ζ/ε, and the Knapen-basis identity Im R = Im R̃/|ε|².
UBD: three forward references carry weight. The exactness proof uses "the impulse regime (8.5)". Its "practical content" uses eq 8.6-fsum-e and κ_BO suppression "of 8.6". The static-vertex error quotes we:8-label.
LO: screen any row ✓. Decide whether L is exact for a coupling ✓, for example a B−L coupling: no. Size the pair-line correction ✗, deferred to 13.4.

**8.5 Hierarchy.**
not reproduced: none. Every entry of tab:8-params re-derived. κ_BO = 0.0665 (²⁸Si), κ³ = 2.9×10⁻⁴, θ_ep = 0.010–0.016, x_R = 0.047 and 46 keV, 2W = 1 at 40 keV, the 139 keV / 0.37 eV impulse boundary, compound-Poisson c_k = E_R⟨ω^{k−1}⟩, Eτ = 7×10⁻⁶, ξ_D = 1.9 / 0.05 / 5×10⁻⁶, and the hydrogen 0.555 q²a₀² (= 2¹⁵/3¹⁰).
pace: good. This is the most useful section for an outsider.
LO: label a formula ✓ for electronic rates. For example the sudden atomic Migdal rate: n_B = 2, 𝔐 = sudden, n_D = 2. For phonon rates see (c).

**8.6 Decomposition.**
lost: 1. The gapless-targets paragraph (H_d, 𝔥_off, the bin bound): I follow its logic only via D.28. It is too dense for its place. 2. eq 8.6-ambiguity: the three terms appear without any main-text motivation. D.28 supplies it, and I verified 5/2π + 1/π = 1.1.
not reproduced: none. I **reproduced we:8-sectors completely** by diagonalizing H in 160 oscillator states. Sector weights of σ_x: 1.25×10⁻³ / 0.152 / 0.847. Electron-following first moment 8.32×10⁻⁵ eV of a total of 1.16915 eV. Smallest BO overlap 0.996. P_Mig = 3.94×10⁻⁶ (0.38 + 3.56). Energy-weighted interference (2.17 − 13.22 i)×10⁻⁴ eV, with the electronic sectors exactly opposite.
One mismatch is left uncommented: the electronic sectors take 4.72 μeV of recoil energy against 0.25 + 4.10 = 4.35 μeV from eq 8.6-fsum-k. That is 8 %, the same order as the 12 % displacement effect the text *does* explain for P_Mig. One sentence would close it.
Also checked: 21 % / 47 % at 50 keV, 2.73×10⁻⁴, δM = N_e m_e via TRK, eq 8.6-zsum via KK, and (PT)² = (−1)^N.
UBD: none. δ_w and δ_F are defined at first use.
LO: assign a final state to a sector ✓. Check the partial sum rules ✓. Apply the Dyson convention to a level-and-band model ✓. Compute Fano coefficients ✗, deferred to E.14.

**8.7 Resolved response.**
not reproduced: **the photon seeds of we:8-pairs.** The text says every pair at 10 eV shares ω − E_g = 9.2 eV. Dark-matter kick: 4.8 + 4.4 = 9.2 ✓. Transverse current: 5.4 + 3.9 = 9.3 ✓. Photon: 5.4 + 3.3 = **8.7 ✗**, which violates the text's own constraint by 0.5 eV. The "hole a volt less energetic" claim rests on these numbers, and it is repeated in the hand-off subsection and in the Summary.
Suspected cause: the 1/(ε_c − ε_v)² optical weight multiplies the Lorentzian tails (γ = 0.1 eV) of the very strong E₂ transitions near 4 eV. That would pull weight to lower transition energies. A rerun with smaller γ, or with weights binned on ε_c − ε_v, should settle it.
Checked: eq 8.7-factor ✓, the 4π/V with the 2π δ ✓, m²ω/πq₀ = 2.2×10⁸ ✓, |ε⁻¹₀₀|² = 0.33 and the ratio 0.29 ✓, q₀ = 1.633 (2π/a) and the 0.84 keV Umklapp partner ✓.
pace: the in-state/out-state paragraph is compact. I accept it from Lippmann–Schwinger.
LO: write eq 8.7-handoff and list its three conditions ✓. Compute screened pair weights from ε⁻¹ ✓.

**8.8 Uncertainty.**
not reproduced: none. Checked: eq 8.8-cost and its expansion, 1.0 / 8 / 19 %, the 0.47 linear-nuisance threshold, 6.1 % Debye–Waller, 0.15 meV, 3.5 eV per MeV, the convexity argument for eq 8.8-tilt, and the geodesic PSD argument.
pace: good. The statistics is standard to me and presented without fuss.
LO: build a template, assign its type and profile it ✓.

**Overall (b).** I would keep reading. The chapter does what a field theorist wants: one contraction, exact identities and an explicit error model. Every derivation I attempted closed. One headline number (the photon-seed hole energy in 8.7) is inconsistent with its own constraint. Coulomb-line classes and the gapless-sector bound are rushed.
**Verdict (b): MINOR GAPS.** Nothing blocks chapters 9–17. The 8.7 inconsistency affects a comparison, not a derivation chain.

## Persona (c): condensed-matter theorist (DFT and many-body, no dark matter)

**8.1** field flags. (i) "its momentum k is not a good label": crystal momentum is a good label; say "bare momentum". (ii) "a valence electron of silicon moves at v_F": silicon has no Fermi surface. The free-gas model is stated later, but the sentence reads as a property of Si. (iii) The nonlocal-pseudopotential correction to the current vertex is noted ✓. The paramagnetic-current terminology is right.
dark-matter side: the Galilean-invariant v⊥ and the reason for transversality are well motivated for me. The q-sign convention warning (Fitzpatrick vs this book) is valuable.
LO: map a dark-matter model onto my response functions (n, s, j, 𝒥, 𝒯) ✓. The table tells me which response blocks I must export.

**8.2** lost: none. The halo average (f_χ, η(v_min)) is enough for me via ch 1 and A.8. The spin-dependent cross term in a polarized gas is a nice test of positivity.
LO ✓.

**8.3** The moment matrices and the Hankel positivity are familiar. The mixed electron–nucleus third moment is new to me and correct (rederived, see b). The point that a frozen-core or pseudopotential calculation gets M³_eκ wrong by construction is well made, as is the PAW caveat.
pace: the recap of DB, FDT, KK and f-sum at the top is slow for me but fine.
LO: use moments as convergence checks of a computed S_ab ✓.

**8.4** The proper-versus-full split is the standard one, extended correctly to ionic charges. The Born charge at zero macroscopic field is the right vertex, and the LST algebra is right.
field check: the triplet channel keeps the direct (W) term and loses the exchange (v̄) term. The text has this right, including "the triplet xc kernel remains" in tab:8-screening ✓.
UBD: see (b). The Coulomb-line classes match my RPA diagrammatics. The D.27 static-vertex argument (TR plus reality ⇒ even in ω′, error (ω/E_g)²) is correct.
LO ✓, except the pair-line size (13.4).

**8.5** **Definitional hole on the 𝒳 axis.** The rungs IP / RPA / RPA+LF / TDDFT / BSE are defined for electronic responses only. Phonons, Born charges and ε∞ from DFPT are self-consistent static LDA linear response. Which rung do electron-following-sector quantities carry? The base point sets 𝒳 = IP by default, which is wrong for a DFPT phonon or Z*. As written I cannot label we:8-nucleon or a dark-photon one-phonon rate on the 𝒳 axis. One sentence would fix it, for example: "for DFPT inputs 𝒳 is the static TDDFT (Hxc) rung", or "𝒳 not applicable".
checked: ε∞ 11.45 / 10.22 / 10.81 / ≈11.9 are EPM-model values; my LDA intuition is ≈14 / 12.7 / 13.3, but the text labels the model. ZPR −56.2 meV against measured −62 to −64 ✓. Raman γ/ω ✓. Exciton binding 14.7 meV ✓.
LO: label ε₂^PA ✓ (agrees with we:8-label). Label a DFPT phonon rate ✗ (hole above).

**8.6** Superadiabatic projectors, the Herzberg–Teller term and Fan–Migdal are all used correctly. Migdal's ω_D/E_F ~ κ_BO² ✓. The derivation of the electron drag mass ✓. The PT-reality argument for Fano coefficients is correct, including the remark about Kramers doublets with spin–orbit coupling.
field flag: "at clamped nuclei the magnons are gapless". Anisotropy gaps exist (meV in NiO). The argument needs only magnon gap ≪ phonon energies, so reword.
superconductor: phase mode at ω_p, and no amplitude mode in the density response for particle–hole symmetry ✓. Semimetal α̃² width ✓.
LO: split a computed spectrum into sectors without double counting (four prescriptions) ✓.

**8.7** "Inverse dielectric matrix of a test electron" is used correctly (test electron, not test charge, with f_Hxc). The factorization proof with a Hermitian kernel ✓. The retarded-versus-advanced labeling and its PT equivalence ✓. GaAs differing by 15 % pair by pair is plausible. The photon-seed inconsistency (see b) is what I would ask the author to rerun first.
pace: the plasmon-as-not-a-class paragraph is good. Si plasmon decay into interband pairs ✓.
LO: export pair-resolved weights from my RPA+LF code ✓. I know which binning to keep.

**8.8** The geodesic matrix interpolation and the constrained-tilt nuisance are both sound. That the f-sum forces rung nuisances to be tilts is a good observation. My check of the first moments to 10⁻⁴ is consistent with that.
LO ✓.

**Notation clashes (both personas).** S⁰ is the zero-phonon sector (8.6, eq 8.7-IP) but also the IP structure factor in we:8-pairs ("S⁰(q₀,ω) = 1.7×10⁸"). 𝒜_fi (the amplitude of D.25) clashes with 𝒜_f (the off-shell amplitude of 8.6). In we:8-sectors, g is a level label next to the couplings g_d and g_n and next to the e-ph vertex g everywhere else. n_B against n_B(ω) is handled explicitly ✓.
**Too slow (both).** "The final state decides the sector, not the coupling" appears three times (8.6 theorem, tab:8-sectors caption, 8.6 hypotheses). "Holds at every point of 𝔗" is repeated in 8.2, 8.3 and 8.5.
**Condescension (c).** None beyond the recaps noted under pace.

**Overall (c).** I would keep reading. The chapter tells a materials theorist precisely which response blocks to compute, which exact relations to test them against, and how screening differs by coupling. Its field statements are almost all right. The three wording slips (k label, v_F of Si, gapless magnons) are minor. The 𝒳-axis gap for DFPT quantities is the one definitional hole, and a single sentence closes it.
**Verdict (c): MINOR GAPS.**

**Final verdict: MINOR GAPS.** Not LOST: no item blocks the following material. Fix list, in priority order:
1. Recheck the photon seeds of we:8-pairs (e + h = 8.7 ≠ 9.2 eV).
2. Define the 𝒳 rung for DFPT inputs.
3. Restrict the operator-list completeness claim to spin ½.
4. One sentence on the 4.72 vs 4.35 μeV mismatch.
5. The S⁰ / 𝒜 / g notation clashes.
6. The forward references in 8.3–8.4.
