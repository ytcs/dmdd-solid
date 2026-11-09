# Chapter 7 revision (2026-11-02)

Files: tex/ch07/ch07.tex, s7-1 … s7-4 (Summary at the end of s7-4), tex/appD/D-19 … D-23. No QE, no figure regenerated (no figure label
carries a renamed symbol; fig7_5 keeps ω₀, which stays). WE 7.4 valley-orbit numbers and the 7.7×10⁻⁴ were recomputed in a scratch script.
Build: /tmp/build-ch07rev, full main.tex, 0 LaTeX errors, 0 undefined citations; undefined references from Chap. 7 and D.19–D.23 only to
unwritten targets (chap:15, chap:19, sec:8.1, sec:8.3, sec:14.1, sec:14.2, sec:15.1, sec:15.2, sec:16.1, sec:16.5, sec:16.6, sec:19.4,
sec:20.4). Lint: 0 blocking in all ten files (EQ-PUNCT hits are the \end{gathered|aligned|split} false positives; the remaining LONG-SENT
hits are environment or display merges, or sentences with inline math the lint counts as words).
Format: item → fix → location. "Declined" gives the reason.

## Editor rulings (brief)
| # | Item | Fix | Location |
|---|---|---|---|
| 1 | D.19 Bogoliubov asymptotics | (A₀/2ω^M)^{1/2} → (\|S\|A₀/2ω^M)^{1/2} | D-19 §spin operators |
| 1 | 7.3 edge slope | "slope never falls below v_D" → DM curve lies below ω = v_max q, edge lies above ω = v_D q; Summary "never lies below the line ω = v_D q" | s7-3 §pairs ¶2; s7-4 Summary ¶3 |
| 1 | "steep" bands | opener: "linear, and slow enough, v_D < v_max, for a dark-matter particle to outrun them"; closing: "bands slower than the dark matter" | s7-3 opener, closing ¶ |
| 1 | 10 keV → 10.5 keV | opener and closing ("about 10.5 keV"); "thirty times" kept (333/10.5 = 32) | s7-3 opener, closing ¶ |
| 1 | pair at rest | "The edge is the dispersion of a relativistic particle of mass 2Δ_D and momentum q, with v_D in place of the speed of light" | s7-3 after eq:7.3-edge |
| 1 | 7.2 threshold numerator | numerator E(ω−E) ± Δ² → Δ² ± Δ² (2Δ² case I, 0 case II), denominator 2Δ × edge divergences, integral Δπ, /ω = 1/2Δ → π/2 written out | s7-2 after eq:7.2-pairspec |
| 1 | "falls as the mass grows" | bound 0.20 approached only for heavy particles; "the typical momentum transfer q ~ m_χv grows with the mass, and the typical ratio falls" | s7-2 ¶ after Ward identity |
| 1 | D.23 prolate | "oblate spheroid"; 7.4 now also says "oblate spheroid, flattened along the heavy direction" | D-23 §anisotropic; s7-4 ¶ variational |
| 1 | p levels 0.3 % | 0.4 % in the text and in the Fig. 7.4 caption | s7-4 measured-spectra ¶; fig:7-donor caption |
| 1 | T-center hole binding | 34.78(15) meV, from the excited hole series extrapolated to the ionization limit [bergeron2020characterization, Sect. IV, checked in sources/review-ch07/2006.08794.txt l.406–449]; "earlier estimates, quoted there, had put the hole binding at 22 to 32 meV" | s7-4 T-center ¶ |
| 1 | WE 7.3 expansion parameter | text definition kept (ln(v_DΛ_D/max(Δ_D, v_Dq)), "up to the numerical factor 1/3π"); WE now quotes 0.38 ln 11.5 = 0.93, "below one but not by much"; the induced term 0.093 is small through 1/3π; D.22 gapless form ln(Λ_D/q) is the same definition | s7-3 validity ¶; WE 7.3 static screening |
| 1 | WE 7.4 size | 7.7×10⁻⁴ (recomputed 7.71×10⁻⁴ with the rounded radii); formula written with \|F(0)\|² = 1/(πr_⊥²r_∥) and a = 5.43 Å | s7-4 WE 7.4 Size |
| 1 | WE 7.4 valley-orbit (derivation 6) | recomputed with −31.3: shifts −14.29, −2.59, −1.28; Δ_f −2.17, Δ₀+Δ_g −5.62, Δ₀ −4.10, Δ_g −1.51 meV | s7-4 WE 7.4 |
| 1 | dos Santos 14 % | "overestimates the measured maximum magnon energy by about 14 %" | s7-1 DFT+U ¶ |
| 1 | Summary 31.3 meV | "binds every donor by 31.3 meV at the liquid-helium dielectric constant 11.4 (29.7 meV at 11.7), and the central-cell correction … 14.3 meV" | s7-4 Summary ¶4 |
| 1 | t/U | 0.05 to 0.06 | s7-1 NiO ¶ |
| 2 | Dirac matrices | α_D^i, 𝛂_D, β_D (spelled as in C.15) in 7.3 (definition, keyresult, isotropic form, Weyl mass term) and D.22 (bubble, traces) | s7-3 §Dirac Hamiltonian; D-22 §bubble |
| 2 | Doublet Pauli matrices | σ^d_i defined at first use ("act within a doublet, not on the electron spin of eq:7.1-se … d for doublet"), used in 7.3 and D.22; 7.2's remark "which we do not call σ_i" now consistent | s7-3 ¶ after eq:7.3-block; D-22 §Dirac form |
| 2 | Dressed vertices | \varGamma (7.2) and upright Γ (D.21) → 𝖵_η, 𝐕-sans 𝖵_j (\mathsf{V}, \boldsymbol{\mathsf{V}}); phase-channel coefficient γ₂ → 𝖼₂ | s7-2 Ward ¶; D-21 §Ward |
| 2 | δk | bold κ → δ𝐤, components δk_i, magnitude δk, throughout 7.3 | s7-3 |
| 2 | E₀ (7.1) | one-electron energy of eq:7.1-dirac → E_orb ("sum of the two one-electron orbital energies"); AFM ground-state energy → E_gs (7.1 keyresult, D.19) | s7-1 eq:7.1-dirac, eq:7.1-afm; D-19 eq:D.19-omega |
| 2 | ω₀ | 7.1 and D.19 no longer write ω₀ = \|S\|A_k ("the diagonal energy \|S\|A_k"); 7.4 keeps ω₀ for the single effective mode of the displaced oscillator, as NOTATION's ω₀ row licenses for 5.6 and D.15 | s7-1 ¶ before eq:7.1-bogo; D-19 §Bogoliubov |
| 2 | E_d | Declined (rename): E_d as the displacement threshold is used in E.10, E.11 and E.23 with this meaning and has its NOTATION row; the clash is with the local level energy E_d of WE 4.7 (outside this revision), which is the one to rename | — |
| 2 | 𝒩_s | BCS quasiparticle DOS → 𝒩_qp(E) | s7-2 eq:7.2-dos and ¶¶; D-20 eq:D.20-dos |
| 2 | γ symbols | fcc structure factor γ_k → ζ_k (7.1, D.19); γ₂ → 𝖼₂ (7.2, D.21); Anderson–Bogoliubov speed c → c_AB (bare c is the speed of light); γ_k1, γ_k2 (Bogoliubov operators), γ_m (mass ratio) and γ_E kept, rows proposed | s7-1 eq:7.1-J2; D-19 §linear; s7-2; D-21 |
| 2 | a (lattice constant vs radius) | variational radii → r_⊥, r_∥ in 7.4 and D.23 (envelope, kinetic energy, ⟨1/r⟩, eq:D.23-variational, minimum); a stays the lattice constant; eccentricity e → e_ecc (e is the charge) | s7-4 variational ¶, density ¶, WE 7.4; D-23 §anisotropic |
| 2 | D.19 Fourier sign | S^±(k) = Σ e^{+ik·r}S^± as in 7.1; S^+_A(k) = (2\|S\|N_s)^{1/2}d_{A,−k}, lattice sum stated, u, v even in k, S^+(k) = (…)(u−v)(a_{−k1} + a†_{−k2}) | D-19 §spin operators |
| 2 | D.23 Coulomb term | "−e²/(4πr) in Heaviside–Lorentz units (e² = 4πα). The host screens it by its static dielectric constant ε: U = −e²/(4πεr) = −α/(εr). The dielectric constant is a pure number … for silicon ε = ε₀ = ε∞ = 11.7, and from here on we write it ε₀, the static constant, as in 7.4." Read "ε" as the book's dielectric-constant symbol in the Coulomb term; ε₀ kept afterwards because NOTATION row ε₀ (static dielectric constant) and eq:7.4-EMT = eq:D.23-EMT use it, and ruling 5 keeps 7.4's ε₀ sentences as written | D-23 §envelope equation |
| 2 | NOTATION rows | proposed in SEAMS 7.1–7.4 (revision blocks) | ledgers/SEAMS/7.1–7.4.md |
| 3 | Goldstone counting | "A particle physicist would count two Goldstone modes … The ferromagnet has one … ⟨[S^x_tot, S^y_tot]⟩ = i⟨S^z_tot⟩ ≠ 0 … coordinate and its conjugate momentum … In the antiferromagnet ⟨S^z_tot⟩ = 0, and the two modes appear, both linear" | s7-1 after eq:7.1-fm |
| 3 | Anderson–Higgs | one sentence naming the Anderson–Higgs mechanism; one sentence on the amplitude (Higgs) mode at 2Δ in the decoupled s₁ channel | s7-2 Goldstone ¶ |
| 3 | A₁/E/T₂ | "The donor site has the symmetry of a regular tetrahedron, the point group T_d … standard names of the irreducible representations of T_d … fixes the degeneracy, one, two or three" | s7-4 valley-orbit ¶ |
| 3 | NiO charge-transfer | "NiO is a charge-transfer insulator: the cheapest charge excitation moves an electron from oxygen to nickel, at Δ_CT < U_H, and superexchange depends on both energies"; "a Mott insulator, in this two-site picture" | s7-1 kinetic-exchange and NiO ¶¶ |
| 3 | k·p → Dirac pace | text: why H² is block diagonal, why MM† ∝ 1, the count 8 → 4 real numbers, the rotation statement, then α_D, β_D; the matrix algebra moved to a new D.22 subsection "The Dirac form" in five labeled steps, including the SO(4) step (U_c Q U_v† preserves det Q = x² + c², rotations of c plus one (x, c₃) plane rotation generate SO(4)) and the excluded nongeneric case | s7-3 ¶ after eq:7.3-block; D-22 new first subsection |
| 3 | Ward-identity pace | new opening: what a vertex is (amplitude for the density or current to scatter an electron), bare vertex η, how the identity is obtained (time derivative, continuity, equal-time commutators, multiply by 𝖦⁻¹ on both sides = amputation), "in words" sentence; spin paragraph split off | s7-2 Ward ¶; D-21 §Ward |
| 3 | D.20 "as one checks" | step written: γ_k1 on the factor (u + v c†c†)\|0⟩ = uv c†\|0⟩ − vu c†\|0⟩ = 0; γ_k2 likewise | D-20 §quasiparticles |
| 4 | Roadmap endings | removed in 7.1 ("We will derive … The section closes …"), 7.2 (count-teaser and roadmap → "We answer them in turn, starting from the electron–phonon vertex of 6.2"), 7.3 ("In this section we obtain … at the end …"), 7.4 ("We will compute …") | openers |
| 4 | Repeated facts | 0.36 meV / 0.1 keV: kept in the chapter intro (motivation), WE 7.2 (derivation) and the Summary; the 7.2 opener points to we:7-al, the 7.2 closing drops the numbers; Cooper 900× kept once (7.2 Cooper ¶, now with the WE inputs), WE paragraph cut; ε_bg double counting stated once (computational ¶), the 7.3 ¶ sentence cut and the WE sentence reduced; 7.1 silicon spin-flip and 7.3 "few meV" repeats cut; D.23 "brackets the answer" kept in 7.4 only | ch07 intro; s7-1/2/3; D-23 |
| 4 | Precision reassurances | cut: 4×10⁻¹⁶ (7.1), 4×10⁵ scan (7.1 → "Both conditions hold at once"), "to numerical precision" (7.2 → "reproduces their closed form"), 10⁻¹² (D.19), 1.76388 "to the accuracy" and machine-precision Fock check (D.20), 10⁻¹⁵ and 10⁻⁸ and "to rounding error" (D.21), 10⁻⁵ and 10⁻⁴ (D.22); kept the checks that carry physics (magnon attraction, 0.579 v_F, factors 28 and 4, classical vs quantum LSWT, 0.2 % q-range) | s7-1, s7-2, D-19 … D-22 |
| 4 | "gives" | 7.1 19 → 7, 7.2 20 → 10, 7.3 12 → 7, 7.4 24 → 8 per 10k (yields, leads to, binds, puts, predicts, supplies, fixes) | all |
| 4 | Comma after eq:7.1-dirac | deleted | s7-1 |
| 4 | "1s triplet" | "the three measured 1s levels"; "the larger of the two" | s7-4 WE 7.4 |

## Derivation report
| # | Item | Fix | Location |
|---|---|---|---|
| 1–5, 7–9 | see rulings | as above | — |
| 6 | valley-orbit reference rounding | recomputed with −31.3 (above) | s7-4 WE 7.4 |
| 10–16 | notation drifts | δk, E_orb/E_gs, 𝒩_qp, ζ_k/𝖼₂/c_AB, D.19 sign, D.23 Coulomb, r_⊥/r_∥ (above) | — |
| 16b | missing rows (V_BCS, ω^M_k, K_ex, E_cl, A_k, B_k, Ry*_⊥, a*_⊥, w_ZPL, Δ₀, Δ_g, Δ_f, Λ̃, 𝒩_D, F(ω), K, O_A, h_k, γ_E) | proposed in the SEAMS revision blocks | ledgers/SEAMS/7.1–7.4.md |
| Not re-run | numerical checks D.19–D.22 | their precision figures are gone from the text; the statements that remain are physics checks (see ruling 4) | — |

## Prose report
| # | Item | Fix | Location |
|---|---|---|---|
| §1 | eq:7.1-dirac comma | deleted | s7-1 |
| §1 | D-19 title | "Antiferromagnetic spin waves" | D-19 l.1 |
| §1 | LONG-SENT s7-1 l.93, l.192 | split (two-magnon numerics; transverse-spin amplitudes one sentence per region) | s7-1 WE 7.1; spin-density ¶ |
| §1 | s7-2 l.31 | rewritten as R7.2c | s7-2 §pairing strength |
| §1 | s7-2 l.139, l.179 | see S2-6, S2-9 | — |
| §1 | s7-4 l.37 cleft sentence | Declined: ruling 5 keeps the 11.4 note as written (prose §6 called R7.4a optional) | — |
| §1 | D-20 l.81 | split after "vanishes" | D-20 §T_c |
| C1 | opening roll-call | Dirac and donor sentences merged and recast, displacement clause added; bound written 2E_th/v_max² | ch07.tex |
| C2 | roadmap tails | removed (ruling 4) | openers |
| C3a–c | restatements | cut (ruling 4) | s7-1, s7-2, s7-3 |
| C3d | recap closings | 7.1 closing reduced to the consequence and the pointer; 7.2 to the edge, the f-sum check and the pointers; 7.3 split, kept as consequence + pointer; 7.4 unchanged | section ends |
| C4 | precision assurances | cut (ruling 4) | — |
| C5 | duplicated keyresults | appendix copies made plain numbered equations: D.19 omega, D.20 gap, ratio, cohE, D.21 Rc, ward, D.22 eps, D.23 EMT (labels kept) | D-19 … D-23 |
| C6 | Summary placement | Declined: moving it to ch07.tex changes the chapter's file structure, and the Chapter 6 revision left its Summary in s6-5; content fixed (31.3 meV; triad cut, ending on the pointer to Chap. 8) | s7-4 |
| C7 | σ seam | resolved by σ^d (ruling 2); bridge sentence to 7.2 in the 7.3 opener ("As in the superconductor of 7.2, the cheapest excitation is a pair whose energy starts at twice a half-gap") | s7-3 opener |
| C7 | 0.333 MeV attribution | sec:3.3 → sec:1.3 in 7.4 | s7-4 opener |
| C8 | register | "gives" reduced; mixed "percent" spellings made \SI{…}{\percent} where numeric (7.3, 7.4); "typical" now used in 7.2 | — |
| C9 | field terms | "coherence length" named (7.2 ¶ and WE 7.2); "Mott metal–insulator transition" named (7.4) | s7-2; s7-4 density ¶ |
| C10 | source comment | deleted | ch07.tex |
| S1-1 | roadmap | kept "three things", cut the rest | s7-1 opener |
| S1-2 | convention clause | ", which is the convention of that reference" deleted | s7-1 NiO ¶ |
| S1-3 | overloaded ¶ | new paragraph at "If every J^ex_ij < 0" | s7-1 §Heisenberg |
| S1-5 | "In a picture" | "Physically" | s7-1 |
| S1-6 | "here are its steps" | deleted | s7-1 §AFM |
| S1-7 | "the last term" | "the pair term d_Ai d_Bj + h.c." | s7-1 |
| S1-8 | Néel twice | merged with a colon | s7-1 after eq:7.1-afm |
| S1-9 | garden path | rewritten as proposed | s7-1 closing |
| S1-10 | Table I pointer | "with a spin-dependent coupling … [Eq. (4)]; 8.1 lists and derives these operators" | s7-1 spin-density ¶ |
| S1-11 | caption unit | "(meV)" | fig:7-nio |
| S1-12 | comma chain | rewritten as proposed | s7-1 F^mag ¶ |
| S2-1 | count-teaser | deleted; "We answer them in turn" | s7-2 opener |
| S2-2 | "two effects" | named | s7-2 |
| S2-3 | "If one also replaces" | R7.2c, with the Eliashberg gap equation named | s7-2 |
| S2-4 | 900× twice | WE paragraph cut; Cooper ¶ now carries the inputs (0.164, 40 meV, 0.40 µeV) | s7-2 |
| S2-5 | g_deg | accepted as written (meaning stated at each use) | — |
| S2-6 | kinematics ¶ | split at "at some angle" and at "This is the regime of dark-matter scattering in a metal." | s7-2 §coherence factors |
| S2-7 | σ seam | resolved (C7) | — |
| S2-8 | Ω | "and Ω the unit-cell volume" | s7-2 BCS model sentence |
| S2-9 | RPA twice | rewritten as proposed | s7-2 conserving response |
| S2-10 | overloaded ¶ | spin-density paragraph split off, semicolon chain made three sentences | s7-2 after Ward |
| S2-11 | pair size | "1/π times the ratio of the probed wavelength 1/q to the coherence length v_F/πΔ_BCS, the size of a pair" | s7-2; WE 7.2 |
| S2-12 | closing restatement | cut to the edge sentence, the f-sum sentence and the pointers | s7-2 closing |
| S2-13 | ω_log | "the logarithmic average phonon energy of 6.4, ω_log = 270 K [Savrasov Table III]" | WE 7.2 |
| S2-14 | ϝ vertices | 𝖵 (ruling 2) | — |
| S3-1, S3-2, S3-3, S3-8 | see ruling 1 / 4 | — | — |
| S3-4 | symbol-first sentence | "We write Δ_D for this half-gap." | s7-3 |
| S3-5 | uniqueness argument in text | moved to D.22 (ruling 3) | — |
| S3-6 | "calculations and measurements" | "first-principles values disagree on its size: they range from 24 to 35 meV" | s7-3 Weyl ¶ |
| S3-7 | DOS question | "at energy E" | s7-3 §DOS |
| S3-9 | ε_bg reason | "In ZrTe₅ the remote interband transitions and the polar lattice make it large" | s7-3 §screening |
| S3-10 | double counting ×3 | kept in the computational ¶; l.110 sentence cut; WE sentence reduced to "already contain a Dirac term of this size, which is harmless at the few-percent level" | s7-3 |
| S3-11 | limitbox attribution | "after [Eq. (2.7)], with a hard cutoff" | limitbox |
| S3-12 | comma splice | "whereas" | s7-3 |
| S3-13 | convention reconciliation | one sentence, "quoted there as g_deg α̃ = 0.80 with g_deg = 4" | WE 7.3 |
| S3-14 | device name | "the gapless regime of fig:7-gapless-limit" | WE 7.3 |
| S3-15 | fifty-fold | "about fifty-fold" | WE 7.3 |
| S3-16 | cite pair | "and~" | s7-3 |
| S3-17 | σ, α, β | ruling 2 | — |
| S4-1 | sec:3.3 | sec:1.3 | s7-4 opener |
| S4-2 | cite pair | "and~" | s7-4 |
| S4-3 | cleft sentence | Declined (ruling 5) | — |
| S4-4 | "It also lifts" | "The central cell also lifts" | s7-4 |
| S4-5 | pairing two lists | "the triplet T₂ at 33.89 meV and the doublet E at 32.58 meV" | s7-4 |
| S4-6 | "no other method" | "no supercell is large enough to hold the envelope" | s7-4 |
| S4-7 | triplet; largest | fixed | WE 7.4 |
| S4-8 | a | r_⊥, r_∥ (ruling 2) | — |
| S4-9 | T/NV ¶ | split at the NV center | s7-4 |
| S4-10 | nm units | \SI{1326}{nm}, \SI{637}{nm} | s7-4 |
| S4-11 | 0.30 clarity | "the photon count shifts S_HR by at most 0.30. The true Huang–Rhys factor lies between …" | WE zero-phonon fractions |
| S4-12 | M | "the silicon nuclear mass M = 26.16 GeV" | s7-4 displacement |
| S4-13 | Mott transition | named | s7-4 |
| S4-14 | ω₀, E_d | ruling 2 (ω₀ removed from 7.1/D.19; E_d declined) | — |
| D19-1 | E.9 cross-refs | Hamiltonian is eq:7.1-heis; result eq:D.19-omega "used in 7.1 and E.9"; "this is eq:7.1-afm, and also eq:E.9-afm" | D-19 |
| D20-1 | "as one checks" | ruling 3 | — |
| D20-2 | "the second form" | "the exponential form being valid for weak coupling" | D-20 |
| D20-3 | operator of 7.1 | "eq:7.1-se in second quantization" | D-20 |
| D20-4 | assurances | cut | D-20 |
| D21-1 | Γ, 𝟏 | 𝖵; \mathbf{1} → 𝟙; also the Nambu triplet shorthand 𝛔 = (s₁, s₂, η) → s_a with s₃ ≡ η (clashed with the spin 𝛔) | D-21 |
| D21-2 | "RPA" | "random-phase approximation", "random-phase kernel" | D-21; also D-22 "random-phase polarization" |
| D22-1 | title | "Dirac electrons and their polarization" (the section now also holds the Dirac form) | D-22 |
| D22-2 | l.55 | "A hard cutoff and a subtraction differ in this constant and in nothing else. Either way, Λ_D is a model parameter, fixed by matching to the computed band structure." | D-22 |
| D22-3 | l.59 | deleted | D-22 §limits |
| D22-4 | α, β | ruling 2 | — |
| D22 "only" | four cut (l.3, 14, 33, 69) | reworded | D-22 |
| D23-1 | prolate | ruling 1 | — |
| D23-2 | α_j | c_j (D.23 and 7.4) | D-23; s7-4 |
| D23-3 | "brackets" twice | D.23 sentence reworded, points to 7.4 | D-23 §isotropic |

## Reader (a)
| Item | Fix | Location |
|---|---|---|
| D.19 \|S\| | ruling 1 | — |
| D.19 cites E.9 | D19-1 | — |
| two-magnon "all spins rotated together" | "we leave out those that are rotated copies of states with fewer deviations, S⁻_tot\|F⟩ and S⁻_tot acting on one-magnon states" | s7-1 WE 7.1 |
| Wigner–Eckart | one-clause statement of the theorem | s7-1 spin-density ¶ |
| Néel temperature | "the ordering temperature of an antiferromagnet" | s7-1 opener |
| E.9 references (DFT+U, frozen magnon) | Declined: asides, as the reader says; E.9 is written | — |
| ±Δ² sentence; "falls as mass grows" | ruling 1 | — |
| shell restriction of the bubbles | "All bubbles here carry the restriction of the pair states to the shell, as in eq:7.2-HBCS." | s7-2 after eq:7.2-violation |
| NVren rests on E.9 | Declined: the step is in App. E.9 (written); 7.2 states the approximation (cutoff in the Matsubara coupling) and the result | — |
| Ward-identity vocabulary | ruling 3 | — |
| Conserving response "carries a lot in two sentences" | Declined beyond the Ward rewrite: D.21 gives the argument in full and 7.2 points there; the q = 0 closed form follows in the text | — |
| 7.3 slope, expansion parameter, SO(4) | rulings 1, 3 | — |
| QED analogies | Declined: asides, nothing depends on them | — |
| oblate, a clash, triplet, Summary 29.7, D.23 ε₀ | rulings 1, 2, 4 | — |
| A₁/E/T₂ | ruling 3 | — |
| slow shallow-donor opening | donor/acceptor paragraph shortened from six sentences to three | s7-4 §shallow donors ¶1 |

## Reader (b) and (c)
| Item | Fix | Location |
|---|---|---|
| (b) Goldstone counting; Anderson–Higgs; amplitude mode | ruling 3 | s7-1; s7-2 |
| (b) ±Δ², slope, a/b, ε₀ | rulings 1, 2 | — |
| (b) Kramers derivation too terse | ruling 3 (D.22 five steps) | — |
| (b) A₁, E, T₂, point group | ruling 3 | — |
| (c) t/U 0.07; charge-transfer | rulings 1, 3 | — |
| (c) case I/II "every probe falls into" | "every one-body probe is a sum of a part even and a part odd under time reversal, one from each class" | s7-2 after eq:7.2-cohE |
| (c) Na₃Bi, Cd₃As₂ off the TRIM | "although their nodes sit on a rotation axis away from the time-reversal-invariant momenta, where a crystal rotation protects them" | s7-3 Weyl ¶ |
| (c) daily-modulation mechanism | "The dark-matter wind arrives from a fixed direction in the Galaxy, which turns once a day in the laboratory with the rotation of the Earth" | s7-3 kinematics ¶ |
| (c) TZZ coupling deferred to 8.1 | accepted (forward reference; S1-10 rewording) | — |
| (c) 1s triplet; 29.7 vs 31.3 | rulings 1, 4 | — |

## Editor notes
| Item | Status |
|---|---|
| α_D, β_D (7.3, D.22) | done |
| σ^d (7.3) | done |
| Si ε 11.7; 11.4 note | kept as written; no sweep |
| S_HR = −ln 0.23 inferred | stated (caption and WE), unchanged |
| Bergeron arXiv-only | audit item; Sect. IV now cited for the 34.78 meV |
| ω₀, E_d | ruling 2 (ω₀ resolved; E_d declined with reason) |
| Al T_c 1.18 K; 40 meV cutoff | unchanged |
| \varGamma → 𝖵 | done (7.2, D.21) |
| Δ/(v_Fq) ≤ 0.20 bound | kept, with the typical-ratio fix; 15.1/15.2 pointer unchanged |
| ZrTe₅ α̃ 0.19–0.20, g_deg = 2 (ruling 6) | 7.3 coupling ¶ ("0.19 to 0.20 with g_deg = 2"), WE 7.3 (0.19; earlier set 0.20, quoted 0.80 with g_deg = 4) and Summary; consistent with E.20 |

## Not touched
"translation invariance" in s7-2 (the Ward paragraph) is left as the book's majority spelling; the sweep of other agents is outside these files.
