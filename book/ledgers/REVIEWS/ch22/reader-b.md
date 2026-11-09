# Chapter 22 mock-reader review: reader b (personas b and c)

Source read: tex/ch22/ch22.tex, s22-1.tex, s22-2.tex, s22-3.tex, s22-summary.tex, and fig22_1.pdf (rendered).
Back-references checked against Chapters 1, 3, 8 and 19 where a number depended on them (v_max, PAW, the 20Aμ bound, the Born parameters).
Numbers checked with mpmath: the Fermi function and its threshold ratios, the kinematics of the charged-current example, the isospin counts, the f-sum tolerances, the constant-term example and the phason scales. I also recounted Table 22.2 by class and by chapter and counted the circles in Fig. 22.1.

## Persona (b): particle physicist (QFT, no solid-state physics)

### 22 opening + §22.1 Calculations specified but not done
**Lost points.**
- §22.1 opening and the chapter opening give 0.333–0.405 MeV as "the only electron-recoil rate". Table 22.1 row 1 gives 0.333–0.43 MeV, an "end of lead" at 0.42–0.43 and a two-channel band at 0.43–0.51. Within one page that is four upper edges, and none is labeled. I eventually took 0.405 MeV to be the kinematic zero-phonon onset and 0.42–0.43 to be where the phonon-assisted channel stops leading, but that is a guess. Fix: one clause saying what 0.405 marks.
- Two different "Born parameters" for the same silicon ion: Zα/v_F = 15 (§22.1, recoil charge) and Z₁α/v = 117 to >1000 (§22.3, tracks). Ch. 19 distinguishes them, but Ch. 22 places them two sections apart with no qualifier. Fix: name the velocity each time.
- §22.1-limits: Fig. 22.1 marks "Nuclear recoil, Si lattice" and "Polar phonons, GaAs" as data-limited (filled circles). The prose never says which datum limits them, and it says the Si lattice rate is already known to 0.25%. I could not infer the datum.

**Steps I could not reproduce.**
- WE 22-fsum, Cauchy–Schwarz paragraph: "A small remainder is *necessary* for a small truncation error, and sufficient once the vertex sum ... is bounded." The inequality is an upper bound, so it gives sufficiency only. A large remainder is compatible with a small truncation error, through small b_m or cancellation. Logic error; delete "necessary", or say "a large remainder leaves the truncation error unbounded".
- The inequality itself (√Δ ρ against b/√Δ): reproduced.
- WE 22-fsum, transfer rule: "agree to about 2 %, 1.8 at θ=0.010, 2.1 at 0.016". I reproduced it as θ + (Z_v m_e/M_cell)/θ = 1.00 + 0.78 = 1.78 % and 1.60 + 0.49 = 2.09 %. The text never says that the two relative errors are added, or why the g⁴ term relative to the sideband is θ. Too fast: one equation would fix it.
- Reproduced: q²/2m_e = 0.9785 eV at 1 keV; 4×0.9785 = 3.914 eV; Z_v m_e/M_cell = 7.81e-5; 2 %/θ = 1.25–2.0; dm/dω ≈ 2/v_max² gives 8.5e-5 MeV per 0.3 meV; the Born parameters 14.6 and 34.7 with r_s ≈ 2.0 and 2.08.
- Not reproduced, because they need a band-structure run: the 531-plane-wave fractions 0.1514 to 0.9996 and the 3.1135 eV target at general k. They are plausible: the target falls by Σ q·v_g = −0.80 eV.
- §22.1, the last recast paragraph: "a change R of the detection rate moves such a limit by R^{-1/2}". Combined with 0.05–0.93 this gives a σ_e shift of 1.04–4.5, which matches the Table 22.2 row for §10.9. Consistent, but the reader has to make that link alone.

**Used before defined (in this chapter; all are defined in earlier chapters).** These are θ_ii, Q*, P(first), "survivors", "the guide", q_0 and q_BZ. For an index chapter this is acceptable. P(first) 0.315/0.498 is not readable without §21.7.

**Too slow / too fast.**
- Too fast: Table 22.1 "Result it changes" is shorthand ("×1.28 on the rate from 3.6 to 10 MeV (heavy mediator)", "×3.2 at 1 MeV and ×1.34 at 3 MeV"). This is fine as an index, but a QFT reader cannot tell which numbers are factors on the rate and which are factors on a limit.
- Too slow: the chapter opening, the §22.1 opening and the closing paragraph of §22.1 each restate the factor of ten on the phonon-assisted rate.

**Outcomes.**
(1) For an open calculation, name the result it moves and its check: yes. I did this for the TA-frequency row: the onset moves by 8.5e-5 MeV per 0.3 meV, and the check is a bracket within 0.3 meV.
(2) Separate an exact relation from a control: yes.
(3) Run the three-part f-sum check: the logic yes, except the "necessary" error; the numbers only in part.
(4) Classify a channel as limited by theory, calculation or data: yes, from the definitions. Fig. 22.1 counts check out: 11 calculation + 10 data + 2 theory = 23 over 22 rows, with the Si phonon-assisted window counted twice.

### §22.2 Exact gaps in the theory
**Lost points.**
- **Count inconsistency.** §22.2-definition gives the missing steps as 55 calculations, 11 measurements and 6 proofs/methods. The Summary gives 53 / 11 / 8. Both cannot be right. My own count: 5 proof rows (3 in Ch. 8, 2 in Ch. 18) plus "a controlled method" for Dirac targets (§16.1) is 6. The anharmonic row (§11.5) asks for "a real-time method ... or neutron Compton scattering", and §22.1-limits itself says that for the anharmonic crystals "the next step is a method, not a run". That makes at least 7, so the body's 6 looks low. The longitudinal-spin row (§14.4) reads "None from neutron data alone ...", yet the measurement paragraph counts it among the 11 measurements. Fix: classify §11.5 and §14.4 explicitly and reconcile the two counts.
- The "limits" counts check exactly. I recounted the table: 5 proof, 10 bounded, 18 estimate, 34 unsized, 5 test, total 72. Chapters 10–13 have 29 rows, 6 of them unsized. Chapters 18–20 have 17 rows, 12 of them unsized. All as stated.

**Steps.** WE 22-constant:
- 3.232 × 1.160 = 3.749 eV;
- 10/3.749 = 2.667 pairs;
- 0.35/2.667 = 13.1 %, 0.008/2.667 = 0.3 % and 0.19/2.667 = 7.1 %;
- 1 % is reached at ω = 131.2 eV.

All reproduced.

**Used before defined.** "Not concentrated on a lattice in ln x" is renewal-theory jargon for non-arithmetic. It is presumably defined in App. D.44, but the worked example uses it with no gloss. "Step model" (+0.19) is also not re-anchored.

**Too slow / too fast.** The definition box and the gap/nuisance distinction are well paced. The final paragraph after WE 22-constant (the "opposite verdict") is useful and short.

**Outcomes.**
(1) Define an exact remaining gap and tell it apart from a nuisance: yes. Test on δ_X ≈ +0.28: a nuisance with a width. Test on the screening of the phonon-assisted sideband: split into a nuisance row and a gap.
(2) Read a gap from its home and say what it limits: yes. I re-ran WE 22-constant and reached the same "proof" verdict.

### §22.3 Channels outside the framework
**Lost points.**
- The opening says these processes lie "outside the framework", but the fourth class and the CDW row are explicitly inside it. That is stated, but the section title and the Table 22.3 caption still say "outside". A word such as "outside, or uncomputable within" would avoid the double take.
- The "Damage tracks of fast heavy ions" paragraph (§22.3-tracks) then evaluates a silicon ion "at the speeds of dark-matter recoils", which is β < 10⁻³ and slow compared with v_F. "Fast" and "slow" for the same object.

**Steps (all reproduced with mpmath).**
- Kinematics: p_ej = 1.0157 MeV; y_S = 0.4329; p_ej r_A = 0.0309 with r_A = 6.0 fm.
- Fermi function at 626 keV: F(53) = 6.338; F(52) = 6.062, which is 4.35 % lower.
- Near threshold: F(53, 10 keV) = 32.55 and F(53, 1 keV) = 102.1. The ratio of p·F to its value at 626 keV is 0.514 and 0.507; the ratio of p alone is 0.100 and 0.0315.
- Limits of F: at Z_d = 1, F = 1.0262 against the nonrelativistic 1.0259, so the limit holds.
- Length scales: a₀/53 = 998 fm; 1/p = 194 fm at 626 keV and 1942 fm at 10 keV.
- Isospin: A − 2Z = 21 and A − Z = 73, ratio 3.48. Uniform-sphere ΔE_C ≈ 1.2 × 1.44 × 52/6.0 − 1.293 + 0.511 ≈ 14.2 MeV, so "about 14 MeV" holds.
- Phason: 0.23 THz = 0.951 meV; 263–315; 2ω/v_max² = 271 eV with v_max = 2.650e-3; 189 keV per keV of |Q_CDW|.
- **Imprecise:** the printed Fermi function of the cited reference is larger by Γ(1+2γ)²/Γ(1+γ)² *times* (1+γ)/2. At Z_d = 53 that is 3.22 × 0.961 = **3.10**, not 3.2. At Z_d = 1 the prefactors agree and 4.0 is right. The sentence "therefore larger by Γ(1+2γ)²/Γ(1+γ)²" drops the prefactor difference that it has just named.

**Errors and omissions in my field (particle/nuclear physics).**
- WE 22-cc: "the rate would grow with the electron phase space, as p_ej". The two-body phase space of an absorption with a heavy recoil goes as p_ej E_ej, not p_ej. Near threshold E_ej → m_e, so the conclusion survives (finite with distortion, vanishing without), but the 0.10/0.032 ratios are ratios of p only. Say "p_ej E_ej", or state that E_ej is held fixed.
- No mention of the quenching of g_A in nuclei. Shell-model GT strengths with λ_A = 1.27 typically need a quenching factor of about 0.75² for GT, and the measured Ikeda sum is only partly exhausted below the GT resonance. Since §22.3-cc tells a prediction to "exhaust" Eq. 22.3-sumrules "in the space in which they are computed", one sentence on quenching belongs here.
- The comparison of 73 with 21 covers the Fermi strength only. The reader would want the parallel GT statement: per-neutron counting gives 3 × 73 = 219 against Σ B_GT(n→p) = 63 + Σ B_GT(p→n). The Summary says the per-neutron count "overstates the Fermi strength", which is correct, but the reader is left wondering about the GT part, which carries the rate below 14 MeV.
- Sign convention: (1 + λ_A γ⁵) with λ_A = +1.27 is a convention. One phrase ("in the convention of the reference") would stop a reader from checking it against the PDG's g_A/g_V < 0.
- "First-forbidden", "allowed approximation" and "shell model" are used without a gloss. That is fine for me, but personas (a) and (c) will lack them.

**Condescension.** None. "Here Γ is Euler's gamma function" is justified by the clash with the Γ point and the widths.

**Outcomes.**
(1) State the three properties the master formula needs and which process breaks which: yes.
(2) Show why CC absorption is not D·S, and compute F_Fermi: yes, every number reproduced.
(3) Apply the isospin sum rules: yes.
(4) List what a CDW calculation needs and its three checks: yes, at the level of the text.

**Verdict (b): MINOR GAPS.** I would keep reading. Nothing blocks, but there are two outright errors and one imprecise factor:
- the "necessary" in the Cauchy–Schwarz paragraph;
- the 55/11/6 against 53/11/8 count clash;
- the 3.2 that should be 3.10.

## Persona (c): condensed-matter theorist (DFT, many-body; no dark-matter physics)

### §22.1
**Lost points.**
- The dark-matter quantities in the "Result it changes" column are opaque without the dark-matter chapters: "MeV" as a dark-matter mass, "heavy/light mediator", "reach", "threshold mass", "the Migdal row of the guide", "recast", "cosmic-ray-boosted". The table is usable only as a pointer list. That is acceptable for an index, but the chapter never reminds the reader that energies quoted in MeV are dark-matter masses, with v_max = 2.65e-3 converting them to deposits. Fix: one sentence at the head of §22.1.
- "Fano term" (§22.1-checks) and "Fano factor" sit in the same paragraph. Ch. 8 disambiguates them, Ch. 22 does not. For me this is mild; for persona (a) it is a real trap.

**Errors and imprecisions in my field.**
- WE 22-fsum: "an all-electron (PAW) calculation, which has no nonlocal term, checks the split". The PAW pseudo-Hamiltonian is nonlocal: the projectors enter through the D_ij terms. The f-sum closes only with PAW-reconstructed vertices, meaning the one-centre augmentation of e^{iq·r}, which is what makes it all-electron. Say "a PAW calculation with the reconstructed vertices".
- "A cubic crystal has no ℓ = 2 component of any response." This holds for a scalar function of the q direction. A tensor response such as S_ab with vector rows can carry ℓ = 2 combinations. Say "of any scalar response".
- The acoustic sum rule imposed on the dynamical matrix, and "never by setting the e–ph vertex to zero", is correct and well put. The note that the bare BCS bubble breaks the exact relations is correct.
- The hybrid-functional statement for Ge (direct below indirect without spin–orbit coupling, no single exchange fraction reproducing both gaps) is consistent with what I know. The check list (L below Γ, band masses) is the right one.
- "A norm-conserving PBE pseudopotential reaches 0.81 / 0.89." The nonlocal commutator plausibly accounts for most of the 0.11. Correct that the local-model 4e-4 sets the scale.

**Steps.** As for persona (b). The remainder identity is exact by construction in a finite plane-wave basis, so passing it to 1e-13 tests the Hamiltonian–vertex consistency, as the text says. That is correct, but I would add that it says nothing about basis convergence.

**Outcomes.**
(1) Specify the sum-rule and control suite for a phonon-assisted calculation: yes, and the list matches what I would demand.
(2) Classify channels: yes for the ones I can judge (anharmonic crystals limited by theory, the cascade limited by calculation).

### §22.2
**Lost points.**
- As for persona (b): the 55/11/6 against 53/11/8 count clash.
- A small point: Table 22.2 has 0.1–0.5 Å⁻¹ for the f-sum test, while WE 22-fsum uses 1 keV = 0.507 Å⁻¹, just outside that range. Harmless, but worth a word.
- "Strongest statement" entries such as "Markov–Krein band", "Huang–Rhys factor" and "limiting-absorption principle" are familiar to me.
- The dark-matter entries are opaque: "anapole moment" in the opening paragraph, and "retarded density row of boosted dark matter, Cherenkov pole". For me "anapole ... exceeds the static-electron formula 16 times" is readable only as "some coupling", which is enough for the argument being made.

**Errors in my field.** None found in the condensed-matter rows. The Self-trapped-exciton, Holstein-factor ((1+λ_tr)^{-2} = 0.52 needs λ_tr = 0.387, consistent with the 0.39 of Table 22.1), impurity-band and two-level-system rows are stated correctly.

**Outcomes.** Define a gap and classify it: yes. Use the table to find what blocks a given material: yes.

### §22.3
**Lost points.**
- The charged-current subsection is nuclear physics I do not have: Gamow–Teller, isobaric analog state, shell-model strengths, first-forbidden. The isobaric analog state is glossed inline and τ⁺ and σ^β τ⁺ are defined, which is enough to follow the argument. "First-forbidden" and "allowed approximation" (beyond "evaluate the wave at the nucleus") are not explained.
- The decisive physical point is clear and well made: the final-state Coulomb distortion depends on the final state, so no D tensor exists. It is the same structure as a core-hole final-state effect (an x-ray edge or Mahan–Nozières), and saying so would anchor the argument for a condensed-matter reader.

**Errors and imprecisions in my field (CDW subsection).**
- "Lifts the phason at small wave vector ... to the plasma frequency of the condensed electrons." In a quasi-1D crystal only the phason with q having a component along Q_CDW (longitudinal) is pushed up. A transverse phason stays acoustic, or pinned. Because dark matter probes all directions of q, the direction dependence should be stated, so the reader does not conclude that the whole phason branch sits at 0.951 meV.
- The attribution "Lee and Fukuyama showed this" is imprecise: the Coulomb lifting of the longitudinal phason goes back at least to Lee, Rice and Anderson (1974). "As quoted by Kim et al." softens this, but it is still worth checking.
- The conserving-kernel prescription is correct and well stated: a time-dependent mean field with the functional derivative of the same self-energy, no double counting of the Q_CDW phonon between the kernel and the dressed propagator, the Goldstone check at artificial incommensurability, and gapped when commensurate.
- (TaSe₄)₂I with T_c ≈ 260 K and 2Δ ≈ 250–300 meV is consistent with the literature I know.

**Condescension.** None. The analogy to §7.2 and §15.1 is pitched right for me.

**Outcomes.**
(1) Explain when a target response suffices and when it does not: yes; the final-state argument is clear.
(2) Specify a conserving CDW response and its checks: yes, apart from the longitudinal/transverse caveat.

**Verdict (c): MINOR GAPS.** I would keep reading. The condensed-matter content is correct apart from three imprecisions:
- PAW described as having "no nonlocal term";
- "no ℓ = 2 component of any response", which should say scalar response;
- the phason lifting stated without its direction dependence.

The dark-matter shorthand in Table 22.1 is the main obstacle for me, and one orienting sentence would remove most of it.

## Overall verdict: MINOR GAPS
Priority fixes:
1. Reconcile the missing-step counts, §22.2 (55/11/6) against the Summary (53/11/8), and classify §11.5 and §14.4 explicitly.
2. In WE 22-fsum, Cauchy–Schwarz paragraph: drop "necessary".
3. §22.3-cc: 3.2 → 3.1 (keep the prefactor ratio), and phase space p_ej E_ej.
4. WE 22-fsum: PAW needs reconstructed vertices; it is not free of nonlocal terms.
5. Add a sentence on g_A quenching and the GT side of the per-neutron count.
6. CDW: longitudinal against transverse phason.
7. Label what 0.405 MeV marks, and name the velocity in each "Born parameter".
