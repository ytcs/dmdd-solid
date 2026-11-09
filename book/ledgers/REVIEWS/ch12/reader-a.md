# Chapter 12 — mock reader (a), isolated review

Persona (a): a first-year PhD student. Source read: the .tex files `tex/ch12/*.tex`, `tex/appD/D-33.tex` and `D-34.tex`. The built PDF (Nov 1 23:46) is older than every ch12 source (Nov 2), so I did not use it. I read linearly and checked each derived step by hand. I also recomputed about 120 of the quoted numbers (kinematics, unit conversions, moments, bounds, the GaAs and Si Born charges and R_rel); unless a number is listed below, it reproduced to the digits shown.

## Section 12.1 The joint electron–lattice response

**Lost points**
1. §12.1-counting, "Fig. 12.1 shows that the second count is not a small correction to the first". P_Mig is 2e-6, so the double count *is* a 2e-6 correction to the rate. A few lines later the text says "the rate of a phonon detector does not see them". I think the intended meaning is "a Migdal event carries the full recoil energy, not a share of it", but as written it contradicts the next sentence. Fix: say what is not small, which is the lattice energy per Migdal event, not the count.
2. Worked example 12-oscillator, "Excited-surface final states". The mean lattice energy is given as 3ω0 = 0.192 eV. The next sentence then adds **0.188 eV** to 1.0463 eV to get 1.234 eV. I could not tell where 0.188 comes from. It is presumably the mean on the computed (unequal-frequency) surfaces, i.e. 1.234 − 1.0463. One sentence would fix it. The same paragraph quotes the Condon zero-phonon fraction as 0.056, while Poisson(3) gives e^-3 = 0.050. I assume the unequal frequencies (65.5 vs 64.1 meV) explain this, but the text has just told me to use the equal-frequency coherent state.
3. The P_Mig estimate in §12.1-boost uses δM/M = 2.7e-4, the atomic 14 m_e. §12.5 later says this is the trace value and "not what a kick measures" (on-site 28.7 m_e). Reading 12.1 I took the estimate at face value. A forward pointer ("the on-site value, §12.5, differs") would avoid the surprise. The 2e-6 still agrees with Fig 12.1, but only because the figure's point-ion valence drag mass, 11.8 m_e, happens to be close to 14.

**Steps I could not reproduce:** none blocking.
- eq:12.1-force: reproduced from D.33-amp, with the sign convention n_e(p) = Σ e^{+ip·r}.
- eq:12.1-amp: reproduced, i·(−i) = 1.
- eq:12.1-Skk: reproduced, including the prefactor (2π)^-1 = (2π/V)(V/2π)²V^-2·V from D.33-square.
- Estimates reproduced: E_R = 47.8 meV, ⟨p²⟩/2M = 0.6 meV (giving 48.4 meV), v_N p/ω_e = 1.8e-3 and (ω_l/ω_e)² = 6e-5.

**Used before defined:** none. θ_ep, the off-shell window, P_ad, n_B, the Dyson convention, the drag mass and 𝔇_ab are all in Ch. 5 and Ch. 8. The "coefficient 4α" in §12.1-truncations is defined only in §12.3, but a pointer is given, so this is acceptable.

**Too slow / too fast:**
- Too fast: the "Each row of the master formula occupies its own parts of the plane" paragraph packs six placements into one paragraph. I had to draw the plane to follow it. A small schematic, or labels on Fig 12.1, would help.
- §12.1-gapless is dense but clear.

**Outcomes:**
- I can place the sectors on the (ω_l, ω_e) plane: yes.
- I can state the Migdal entry and read its four factors: yes.
- Order-of-magnitude P_Mig ≈ (E_R/⟨ω_e⟩)(δM/M): yes. Si at 50 keV gives 0.0478/6 × 2.7e-4 = 2.2e-6.
- Weight 1 − P_Mig and mass M + δM in the lattice line: yes.

## Section 12.2 The atomic limit

**Lost points:** none.
- The centre-of-mass separation is clean. I verified the chain rule: the cross terms cancel and the ∇_R² terms sum to 1/2m_A.
- I verified X = R − (m_e/m_A)Σρ and the double commutator N_e/m_e + N_e²/M = N_e m_A/(m_e M), which gives (N_e m_e/M)E_R.

**Steps I could not reproduce:** none.
- Ge worked example: m_A, q, v_A, q_e, the factor 0.0296, 1/580, 1/231 and 8.18 eV all reproduce. (7.28 + 0.63)/8.18 gives 96.7 %, quoted as 96.8 %; trivial.
- "124 eV per ionizing event" uses only the ionization part of the moment (7.28 × 0.0296 / 1.73e-3). The sentence "since only one event in 580 ionizes" made me first divide the total 0.242 eV, which gives 140 eV. One clause would avoid this.
- He excitation: 13.606 eV × Σf/ΔE gives 0.177, 0.220 and 2.7e-5. Hydrogen 1 − (5/8)ξ²: reproduced.

**Used before defined:** none.

**Too slow / too fast:** the right pace. Limit box 12.2a's sentence on "an electron that is ionized can no longer leave the rest of the outer shell unexcited" is the one place I needed the Cox reference to believe it.

**Outcomes:**
- Free-atom Migdal probability shell by shell from a table at another q_e: yes (done above for Ge).
- The first-moment sum rule as a check: yes.
- Why core shells keep atomic values in a crystal: yes. Deceleration 2(ω_ph/ΔE)² = 3e-6 for Ge 3d, reproduced.
- Excitation lower bound P_exc/P_ion ≥ F_exc/F_ion: yes.

## Section 12.3 Crystals at large momentum

**Lost points**
1. **(Blocking for the low-mass claim.)** §12.3-validity, eq:12.3-bracket, and **§12.4-amp contradict each other.**
   - 12.3 writes the free-recoil boost as 1/(ω_e − y) − 1/ω_e with y = (q − p)·p/M. Angle-averaging gives the "soft limit proper" correction 3p²/q², which is said to "decide the low masses". Limit box 12.3b and the section opening say the formula fails below about 16 MeV and is low by a factor of 2 at 5 MeV.
   - 12.4 derives the exact free-nucleus amplitude from the two time orderings: b/[(ω − b + a)(ω + a)], with b = q·p/M and a = p²/2M. I re-derived its denominators from energy conservation, and I verified the commutator series ([A,H_N] = (p·P/M + p²/2M)A, [[A,H_N],B] = (q·p/M)e^{i(q−p)X}).
   - 12.4 then states: "None of the three is a ratio p/q … keeping that difference without the matching p²/2M in both denominators would introduce an error of relative order p/q". Its key result says dP/dω_e "is eq:12.3-soft at every q".
   - Setting a → 0 in 12.4's expression gives y = b, not b − 2a. So 12.3's y double-counts the p²/2M recoil in one denominator and drops it in the other.
   - Consequence: I cannot tell whether the soft-limit probability is valid below 16 MeV. 12.4 and the nuisance table (no soft-limit row) say yes; 12.3, lim:12.3b (solid curve) and the 12.3 opening paragraph say no. D.33-soft also refers to "the exact energy denominator for a free recoil that §12.3 derives".
   - Fix: reconcile. 12.4's derivation looks right to me, which would make the 12.3 solid curve and the 16.5 MeV boundary wrong.
2. The limit box 12.3b formula uses N_T, Ω and p_N with no definition nearby. I guessed N_T = targets per mass, Ω = cell volume, and p_N = q.
3. "**F** = Σ_i∇_iV_eN minus the total force on the electrons" (§12.3-wannier) reads as a subtraction. It means "F, which is minus the total force". Reword it.

**Steps I could not reproduce:** none algebraic.
- The combination of factors to 4α: reproduced, with e² = 4πα.
- f-sum worked example: c = e²/π reproduced.
- Expansion of eq:12.3-bracket: I reproduced 1 + 3p²/q² + (9/5)v²p²/ω² for 12.3's own y. The problem is the y, not the algebra.
- Per-mass rate: 2α/(3m_χμ²M³) → 4μ⁴⟨v³⟩ → 8α/(3m_u³). Reproduced.
- Wannier: A^W_cv and the bound 2W/ω + W²/ω² (1.56, 0.54, 0.25) reproduced.
- Numbers reproduced: E_R = 100 eV gives q = 2.29 MeV and v_N = 8.74e-5; the ratios 29 and 47; the Ni factors 25 and 81.

**Used before defined:** "Born-charge"-style rung labels (𝒳 = RPA+LF) are fine (§8.5). N_T and p_N: see above.

**Too slow / too fast:**
- §12.3-wannier is fast. It is a single paragraph from the double commutator to eq:12.3-AW, and "inserting a complete set" needed two passes.
- The acoustic-sum-rule argument for the operator ordering is good and well paced.

**Outcomes:**
- Derive dP/dω_e = (4α v_N²/3ω_e⁴)L_Mig from the Migdal entry: yes.
- Fix 4α from the f-sum: yes.
- Evaluate the per-mass rate and its m_χ scaling: yes (exponents 1 and 3).
- Explain the factor ~30 crystal/atom (threshold, plasmon/interband weight, vertex): yes.
- Say below which mass the soft limit fails: **no**, because of item 1.

## Section 12.4 Phonon final states at small momentum

**Lost points**
1. The 12.3/12.4 contradiction above. The reader meets it here.
2. Last paragraph: "The lattice factor below |q − p| ≈ 6.6 keV, where the incoherent approximation … is not certified (lim:11.3a), while the zero-phonon line … agrees with its Bragg sum within 8 %." This is a sentence fragment with no main verb. I could not tell whether 6.6 keV is a limit of the chapter's results or only a caveat on the phonon-emitting share.
3. "The frame itself is the open question of §12.1-boost". §12.1-boost never calls it open; it says valence electrons "lie between the two cases". Either flag it there or point to §12.6-open.

**Steps I could not reproduce:** none.
- The series eq:12.4-series: reproduced, with the signs of both orderings checked.
- The phonon-mediated proof eq:12.4-pm: reproduced once I wrote B a† = (a† − β*)B myself. The text says "the terms in ⟨f|a†B|0⟩ cancel", and that cancellation is the one non-obvious line. A single displayed intermediate step would make "a few lines" true.
- Worked example 12-five-keV: E_R = 0.478 meV, v_N = 57 m/s, 0.94 MeV, 0.75 and 7.0 eV, 2.90e-8, 2.9e-3, 1.10e-9 and "64 × E_R" all reproduce. So do ⟨|q−p|²⟩/2M = 1.20 meV and the Poisson fractions at 50 keV (0.21/0.32/0.25/0.22).
- Minor numerical inconsistency in D.33-phonon. It sizes the bound-nucleus correction with 64.1 meV: (64.1/1170)² = 3e-3 in the amplitude, 6e-3 in probability. §12.4 uses ⟨ω²⟩^{1/2} = 44.7 meV and gets 2.9e-3 in probability. D.33 also calls keeping the propagator "not a consistent improvement", while 12.4 presents it as exact at first order in p. The two passages should agree.

**Used before defined:** none (P^κ_n, Poisson weights and ⟨ω^-1⟩ are from Ch. 5 and Ch. 11).

**Too slow / too fast:** about right. The three-regimes subsection is the clearest part of the chapter.

**Outcomes:**
- Derive the leading factor for a bound nucleus without the impulse approximation: yes.
- Write the harmonic phonon-resolved Migdal probability and state its sum rule: yes.
- Explain why the zero-phonon line dominates at q ≲ 33 keV and why the phonon-emitting share follows 2W(q − p): yes.
- Relate the phonon-mediated form to the leading form: yes.

## Section 12.5 Migdal sum rules and bookkeeping

**Lost points**
1. On-site drag mass: the text gives 10.1 + 18.6 = 28.7 m_e. The worked example says δM_II/M = 5.58e-4, but 28.7 × 0.511/26160 = 5.61e-4. §12.5-trace gives Σ_{J≠I} = −14.6, but 14 − 28.7 = −14.7. Both match 28.6 m_e, so one of the inputs is rounded inconsistently. This is trivial, but it made me recheck everything.
2. "Third moments from nonrelativistic all-electron densities are therefore about 40 % low for germanium". 1/1.425 = 0.70, so they are 30 % low. The relativistic value is 42 % *higher*.
3. eq:12.5-Rrel's "+ O((Zα)²)" remainder is of the same order as the term kept. I understood it to mean "non-logarithmic (Zα)²", but saying so would help.
4. Opening line: "gives them on average 0.18 eV per kick" is the valence part only; the total including cores is 0.279 eV (worked example). Say "valence".

**Steps I could not reproduce:** none.
- Moments k = 0…3, δM = 2I_3, E_2 = 4E_R E_BH: reproduced.
- Expansion of Φ(ω): reproduced.
- Trace rule via TRK (D.34): reproduced.
- Cauchy–Schwarz and threshold bounds: reproduced.
- Worked example: 0.163, 0.0174, 0.0303 and 0.24/0.12 reproduced. The 1s/2s/2p bound 8.0e-4 is plausible, but the split of the 2.9 m_e between 1s and 2s is not given, so I could not reproduce it exactly.
- Third moment: Ze²n/3M gives 1497 eV² for Si and 16 850 eV² for Ge. R_rel reproduces as 1.082 and 1.425, and the log terms as 0.066 and 0.281.
- Cross moment: the geometric-mean argument and Z − Z* (14, 28.9, 35.1) reproduce.

**Used before defined:** "Born–Huang" first appears here (Ch. 8 cites Panati et al. for the same term). κ_BO is from §5.1, fine. 𝓜^1_{eκ} and eq:8.6-fsum-ek are from Ch. 8.

**Too slow / too fast:**
- §12.5-trace is fast on the 1-D chain model. I accepted the numbers without being able to picture the model; a sentence on the parameters, or a pointer to D.34, which does have it, would help.
- §12.5-cross is very compressed: "F_cr" in a crystal is defined only by reference to eq:8.6-fsum-ek.

**Outcomes:**
- Compute the Migdal moments from inverse force moments: yes.
- Bound P_Mig from both sides at 500 eV: yes (done).
- Distinguish the trace and on-site drag masses and say which a kick probes: yes.
- Compute the contact-density third moment and its relativistic factor: yes.
- Use the cross first moment to size the mixed-coupling interference: only qualitatively.

## Section 12.6 Bremsstrahlung and Migdal-type absorption

**Lost points**
1. Worked example 12-gaas: Ω = a³/4 = **44.80 Å³**. With a = 5.653 Å I get 45.17 Å³ (45.0 at a = 5.648). The subsequent 3.249e-2 eV^-2 is consistent with 44.80, so the input itself looks off by 0.8 %. It is harmless, but a careful reader stops here.
2. "Atomic units" for α_pol: the text gives 37.3 a.u. and I had to work out that the formula needs 4π × 37.3 a0³ in Heaviside–Lorentz units. The worked example says this for Ga and As, but §12.6-photon does not say it for Si. Move the sentence up.

**Steps I could not reproduce:** none.
- Brems amplitude −[[H,D],K]/ω²: sign reproduced.
- Sum rule eq:12.6-sum: reproduced.
- Si: C = 0.155 eV^-2, Z*(1 eV) = −0.165 and Z*_at = −0.050 reproduce, as do the enhancement 33–38× and 4.0e-13 photons per recoil (order of magnitude).
- GaAs: −0.347, 8.965, 6.20e-3 and 4.94e3 reproduce, as does the formula for the sum of squares at a general split.
- Acceleration form and eq:12.6-mass: reproduced.
- n_r/|ε|² = 1 + (3/2)ω_p²/ω² reproduces, and 1.2e-3 at 1 keV.
- σ_φ relation: reproduced.

**Used before defined:** g^φ_{n_κ} and the "density row" of §8.1-absorption are fine. The photon field comes from App. C.16, which I had to accept.

**Too slow / too fast:**
- The "Polar crystals" paragraph is fast: "the same appendix bounds each dispersion by 0.9(ω/1 eV)²" arrives with no reasoning.
- "Couplings not proportional to mass" is dense. I followed the logic but could not have done the calculation.

**Outcomes:**
- Bremsstrahlung rate with Z*(ω) from ε(ω) for Si/Ge: yes.
- Why GaAs is not suppressed: yes.
- Scalar absorption through the loss function and the medium factor vs the atomic formula: yes.
- Read the nuisance table: yes. Note that it contains no soft-limit row, which agrees with 12.4 but not with 12.3.

## Appendices D.33–D.34
- I followed every step except one. The final Herzberg–Teller sentence of D.33-amp ("differ at first order, by a term of relative order p/q against the kick") was not obvious. Expanding e^{−ip·u} gives a first-order term in p·u, but why that is "p/q" was not spelled out.
- D.33-soft refers to "the exact energy denominator for a free recoil that §12.3 derives": see the contradiction above.
- D.34 is clear throughout; the Dirac-density subsection is very nicely done.

## Overall
I would keep reading. The chapter builds one object and derives every published Migdal formula from it, and the algebra holds up: I reproduced every key result and nearly every number. Most problems are small: a handful of inconsistent roundings, one sentence fragment, one misleading "not a small correction", and "40 % low" that should be 30 %. One is not small. §12.3 and §12.4 disagree on whether the soft-limit probability fails below about 16 MeV (12.3: factor 2 at 5 MeV; 12.4: exact at every q, and 12.3's form makes an O(p/q) error). That decides the low-mass Migdal rate, the main reason a student would read this chapter. It does not block §12.5–12.6, which do not depend on it.

**Verdict: MINOR GAPS.** One must-fix contradiction (12.3-validity / lim:12.3b vs 12.4-amp and its key result) plus small numerical and wording fixes.
