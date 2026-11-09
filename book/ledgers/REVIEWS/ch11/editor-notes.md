# Ch11 editor notes
- 11.1: Limit 11.1a holds within 10 % only to 0.48 q_BZ (the source applies it to 2π/a). Limit 11.1b's target independence holds only from 44× the edge, and the corrected form from 9×. WE 11.2 at 3× the edge shows the failure of the correction, which is deliberate and accepted.
- 11.8: the rigid-ion GaAs absorption of 2308.06314 overstates the rate 8.2× (the site coupling is Z − Z*/ε∞), a significant claim; verify at the derivation review. The resonator prescription is 1.8× too high at 𝔔_p = 𝔔_DM; verify. GaAs constants: book values Z* = 2.11 and ε∞ = 10.88 (5.5/11.2); E.17's 2.16/10.9 align at App E pass 2. The core kinetic-term shift of ~10 % is a parametric estimate, so label it and send it to the 11.9 nuisance table.
- 11.3: Limit 11.3b is relabelled n_T = 2 (the singular term ∝ T²); update the App. F planning table. The pointwise band is not a 10 % certificate for Si (its upper end is 2.7× at 10 keV), and the text says so. Warren is cited at book level only.
- 11.4: Si onset at x_R = 4 is 92.5 keV (⟨ω⟩ = 40.9 meV), with 8.5's x_R = 9 giving 139 keV, consistent. The Ge ⟨ω⟩ = 23.6 meV is a labelled estimate; replace it with the published Ge DOS mean if one is found at review. 12.5 keeps the split: the BO-surface curvature c₃ in 11.4 and the full Coulomb third moment in 12.5. Fermionic absorption on nuclei: m_χ²(1 − m_χ/M) after continuity; verify at the derivation review.
- 11.6: the headline is now Γ_iso/Γ_EM ≥ 5.0×10³ (PBE DOS 15.9 eV⁻¹, measured Im(−1/ε) = 5.42×10⁻⁶); SPINE and CLAIMS are updated. Isotope correlation +8.0 % (PBE) vs E.17's +9 % (Debye): use 8.0 %. The absorption value was read by eye from a figure (~10 %), and the text must say so. Lifshitz and Dawber–Elliott are cited without being read.
- 11.7: odd multipoles require breaking BOTH inversion and time reversal (fix the SPINE wording "or"). The electronic daily-modulation numbers come from the EPM model (labelled), and the first-principles components are an open problem. WE 11.7 at 2 MeV is accepted. Sapphire/SiC numbers are incoherent-approximation estimates.
- 11.5: Limit 11.5a is n_A = 2 (rate-order rule + time-reversal cancellation); update the F planning table. Boxes 11.5a/b are labelled models. The three-phonon coefficient is fitted, not derived: say so. No D derivation is needed for the Stieltjes band. Two overfull boxes (153/130 pt) late in the build, in or after the App F rows: check at the Ch11 review / F pass. The helium Lindemann ratio is "about a quarter" (E.19 says 0.3; align at E pass 2).

## For the Ch11 batch review (from the 11.9 writer)
- s11-8 ~l.97–99: possible near-duplicate paragraph (core kinetic energy / inputs); check and merge.
- WE 11.10 threshold 100 meV and σ_p = 1e-40 cm² chosen by the writer; frequency template is an upper estimate (uniform 2.6 % rescale).
- 11.6 should state the ~10 % digitization uncertainty on the absorption coefficient that 11.9 quotes.

## EDITOR RULINGS (2026-11-02) — bind the Ch11 reviser
R1. **WE 11.10 parameters accepted.** The 100 meV threshold and σ_p = 1e-40 cm² stay. State them once in the WE set-up as illustrative choices.
R2. **Phonon-frequency template.** The uniform 2.6 % rescale stays and is labelled "upper estimate" in Table 11.1.
R3. **Absorption coefficient.** 11.6 states the ≈10 % uncertainty on the absorption coefficient read off the published figure, at the point where it is used. 11.9 then cites that statement.
R4. **s11-8 l.95–99.** If the core-kinetic-energy paragraph repeats content, merge it into a single paragraph.
R5. **GaAs core kinetic-energy item (≈20 % of the scalar rate).** It stays as a parametric estimate and goes into DEFERRED-COMPUTE as a candidate for a proper calculation.
R6. **GaAs cell (from reader-b).** Ω = 44.80 Å³ implies a = 5.638 Å, which is not the book's room-temperature value of 5.653 Å (Ω = 45.17 Å³). Two cases:
  - Ω is the PBE-relaxed cell of the phonon calculation: say so where it first appears, and keep it in that calculation only.
  - Ω is a stray value: switch to 5.653 Å.
  Either way, name the source of the measured Si 64.1 meV optical phonon and of the room-temperature dielectric constants.
R7. **t_coh.** Keep the NOTATION/8.2 definition, 1/(m v₀²). 11.8 converts to it and does not introduce the 2π.
R8. **Υ_ℓ (11.x)** clashes with Υ_m (8.6). Rename the Ch11 symbol to a free letter per NOTATION, and add a clash entry.
R9. **Core kinetic-energy term (11.8, 11.9).** State the sign: Δd ≈ +1.2e-4 per u, so the rate falls by about 19 %. Label it a parametric estimate in 11.8 itself.
R10. **Limit Check 11.6a.** The ²⁹Si/host DOS ratio is "a factor 2" (peak 2.05 at 57.3 meV; minimum 0.59 near 60.7 meV), per limit11_6a.log.
R11. **Sapphire bracket (11.2).** State the bracket as its formula gives it, [15.9, 45.4] meV. The tighter 37.1 meV bound uses ω_L,max: state it explicitly as such or drop it. Harmonize 36.3 vs 35.9 meV, and give the averaging if the two values differ.
R12. **11.8 electron counts.** Bridge "28 and 36 electrons" (rigid ion) to the Z − Q/ε∞ effective values 30.724/33.276 explicitly, so that no literal reading gives a factor of 4000.
