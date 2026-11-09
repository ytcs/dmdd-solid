# App E.14–E.27 second pass: editor notes
Reviews: consistency-1.md (E.14–E.20), consistency-2.md (E.21–E.27), ../appCE/prose.md (App E part). All chapters are accepted, so the chapter text governs every number. Where a spec disagrees with an accepted chapter, change the spec; consistency-2 notes the one exception, the xenon (Zα)², which is queued as a chapter fix.
## Rulings
- E1. Germanium, uniformly: no spec prescribes a route known to fail. E.1 l.147, E.15 (the l.56 HSE06 reuse and the BSE on G₀W₀@PBE), E.16 (the library on PBE+scissor), E.18 (drag masses on PBE), E.23 (the HSE arm) and E.24 (G₀W₀) all use "germanium bands that pass the check of app:E.14 (valley order, both gaps, masses at L and Γ)". GW quasiparticle bands are named as the next route under that check, with no verdict. Do not quote any GW result.
- E2. E.18 gains the coherent zero-phonon Migdal response from 0.75 keV to 2q_BZ, which carries nearly all of the Si Migdal rate at 0.42–1 MeV (Ch12 erratum; tab:22-calc). Specify the quantity, method, acceptance test and cost in prose.
- E3. Numbers follow the chapters:
  - E.20: the ZrTe₅ row of Ch16 (half-gap 11.8 meV; velocities 1.1e-3, 4.5e-4, 1.0e-3; cutoff 0.191 eV; α̃ ≈ 0.18, Ry_D ≈ 0.10 meV, a_D ≈ 1.4e3 Å, recomputed in a small logged script);
  - E.17: CsI uses the measured 4.2 K elastic constants, and the missing quantity is the cold-cell density;
  - E.16: off-axis minima 0.13–0.22 rad;
  - E.24: F 2.4σ low; the DFT cascade 14 % low; A_AB 5.703 eV³; plasmon 16.4 eV; GaAs measured ε∞ and LO–TO (not computed); the Gaussian tail law C/x; extrapolation in h^{3/2};
  - E.25: ε_s per the book value (with 6.3–12.6e4 cm⁻² and 3.5e4 V/cm recomputed), the readout verdicts pointer to the Ch20 Summary, and the 0 K Al constants;
  - E.26: the vector defect is bounded (Ch10); the light-mediator expansion keeps the ω term; Cu shift −1.97e-2;
  - E.21: |p−q|⁻⁵ amplitude; "Fermi" factor per 16.3;
  - E.23: Qb@ll is plane-wave (fix the clause); classical boundary 0.41 eV.
  Every recomputed number goes in a figscripts/appE log.
- E4. Promises the chapters make that a spec must keep (consistency-1 and -2 lists):
  - E.14: the phonon-assisted kinetic row, as cited by four chapters;
  - E.16: the library f-sum tolerance of 2 % (Ch21/22), the 𝒪₂ kinetic rows, and the REF §4 low-energy-flux caveat;
  - E.17: PIMD error ≤ 0.2 %;
  - E.20: the Al impurity ladder and ℓ_mfp scope (DC-41 wording); the Holstein tests λ_tr = 0.39 and low-ω α²F_tr; the magnetoelastic B₁, B₂ and the DM constants;
  - E.21: the 3.60 keV line, the 𝒰 coefficients, R̃²ᴰ/r₀, and the tube excitons;
  - E.22: the Born-limit resonator acceptance;
  - E.24: the outputs that Ch21.6 and Ch18.5/22 rely on (marks, pair separations);
  - E.26: the axioelectric caveats.
  
  Fix 8.4's pointer (the supercell is in E.16) as a one-line edit in tex/ch08/s8-4.tex.
- E5. Prose:
  - Rewrite the specification paragraphs of E.15, E.20 and E.21 as prose, and remove the recipe template ("The quantity is / The method is / The acceptance test is / The cost is / The result enters") throughout, down to the E.1–E.13 rate (≤ 1.5 per 1,000 words).
  - Remove the count-announcing sentences (fix the three wrong counts), the recap paragraphs after tables, and the mixed table headers.
  - E.25: two uses of ε₀. E.21: define STE; fix the l.28 subject switch. E.18: fix the broken parallel. E.27: cite Gordon et al. properly or drop the citation.
- E6. E.27 notation: the linear program uses the symbols of C.12 and Ch21 (stream masses ξ_a). Rename the E.27 dual weights so they do not clash, and record that in NOTATION. Add NOTATION rows for 𝔎_i, 𝔥, ξ_i (renamed) and λ_dec, owed since the Ch21 merge.
- Sequencing: two revisers, E.14–E.20 (clash entry 98) and E.21–E.27 (clash entry 99). Each re-reads NOTATION.md before each edit and only appends. The App B reviser may also be editing NOTATION.
