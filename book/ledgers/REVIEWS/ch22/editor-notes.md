# Chapter 22 editor notes

## Writer reports (pre-review)

### 22.2 (exact gaps): Table 22.2, 72 rows (proof 5, bounded 10, estimate 18, unsized 34, test 5)
- The coherent Migdal gap is placed in 17.1, outside Ch22 ownership. Reviewers should check the cross-reference.
- About ten gap rows were added beyond SPINE. Derivation reviewers should check each against its source chapter.
- Light-pass items it found: the s10-5 "interim statement" wording; the s10-6 Ge HSE claim (soften per DC-RESULTS); the 18.3 SEAM says 0.015 where the tex says 0.008 (the tex governs, so fix the SEAM).

### 22.3 (outside the framework) and Summary
- Q1: the isospin-limit Fermi strength A−2Z sits in the IAS (¹²⁵Te about 14 MeV). This implies the Dror et al. n_j ≃ A−Z overcounts (73 vs 21). **Derivation-1 must verify.**
- Q2: Dror Eq. 4.10 prints Γ(1+γ)² instead of Γ(1+2γ)². State it only as a fact about the printed formula. **Derivation-2 must verify.**
- Q3: Chapter 22 carries no rate truncation, so it needs no nuisance table. Ruling: the exemption is granted.
- Q4: the summary's 22.1 paragraph was drafted before 22.1 was final. The reviser must recheck it against final s22-1.tex.
- Q5: extend the Λ_F NOTATION row to the charged-current scale (at merge). Keep the "as quoted by" attributions to LRA and Lee–Fukuyama.

### 22.1 (calculation programme), opening
- Q1: 22.1 says the boosted-DM heavy-mediator case is settled, using the referee's quotable wording. 10.9 needs a light pass to match (already queued).
- Q2: the Ge hybrid-functional calculation without SOC inverts the direct and indirect gaps, and 22.1 adds a band-mass check. Queue E.14 to add band masses at its second pass. Consistent with the s10-6 softening.
- Q3: the Fig. 22.1 classes (recoil-charge and superconductor rows): reviewers to check.
- Q4: the WE tolerance of about 2 % is labelled as an estimate. Fine.
- Build: `junk1999confidence` is cited in s21-4 and missing from book.bib. The Ch21 reviser or post-check must add it.

## Rulings (Ch22 block), after five reviews
Verdicts: prose REVISE ×5 (no rewrite); reader-a and reader-b MINOR GAPS; derivation-1 5 WRONG / 7 GAP; derivation-2 has must-fix items. Q1 (isospin A−2Z in the IAS; Dror n_j overcount 73 vs 21) is verified twice. Q2 (Dror Eq. 4.10 prints Γ(1+γ)²) is verified.

- **R1 Fermi-function convention.** The book keeps prefactor 4. That is Hayen et al. Eq. (6), F₀ (checked in the source text: Hayen calls it the point-charge F₀ and notes that other definitions replace the 4). Derivation-2's "Hayen calls 2(1+γ) the point-charge form" is overruled. 22.3 must cite eq:21.7-fermi rather than redefine it (delete eq:22.3-fermi or make it a reference), and use y_S as 21.7 does. The claim about Dror's printed formula is stated for the gamma-function factor alone: Γ(1+2γ)²/Γ(1+γ)² = 3.22 at Z = 53 and 4.0 as Z → 0. Do not state it as a ratio of the whole functions, since the prefactors differ. 6.34 stands. Fix the summary: the daughter value is 4.5 % above the parent value (the parent value is 4.3 % lower). State the size of the finite-size L₀ correction (about 1 %) correctly and do not call it (pR)² ≈ 10⁻³.
- **R2 Gap table recount (tab:22-gaps).**
  - Reclassify 17.1 electron-following and 18.2 to unsized, matching their home chapters.
  - Make each row name ONE missing step. Where a row lists more, choose the decisive step and move the others to the "check" text, or split the row.
  - Classify the anharmonic row (11.5) as a method.
  - Rerun gaps22_2.py. Every count in 22.2, the summary and 22.1 comes from its log: classes, missing-step totals, and the chapter-range counts ("at least 29" where that is a lower bound).
- **R3 Calculation table (tab:22-calc) completeness.** Either add the roughly ten missing open calculations derivation-1 G2 lists (11.6, 14.2, 14.5, 15.3, 15.4, the Ch16 calculation-limited group), or drop the "every" claim. Preferred: add them, compactly. Also:
  - capture fraction 0.54 % (0.32–0.77 %);
  - drag-mass row restated per sec:12.5 (14 mₑ is exact; the open quantity is the on-site element, valence 18.6 mₑ, bounded 12–24);
  - BSE row: 39 % alone, 93 % with the converged IP table;
  - cascade row: add the computed ε_eh 4.15 eV against the measured 3.749 eV, with no fitted constant (Ch18, sec:18.1);
  - Fig. 22.1 classes: apply derivation-1 G3–G5, and give the cold-edge row a reference to sec:13.9.
- **R4 Quoting restriction.** The 10.9 boosted row must quote "density-row ratio 0.05 to 0.93", not "1.04 to 4.5 at 1 keV" (DC-49/54/36). Check every other DC-derived number in Ch22 against DC-RESULTS restrictions.
- **R5 22.3 physics.**
  - IAS threshold: "about 13–14 MeV" (Coulomb-energy systematics 13.2; uniform sphere 14.2).
  - Electron phase space ∝ p_e E_e.
  - Add g_A quenching and the Gamow–Teller side (Ikeda rule, which holds without isospin symmetry) to the per-neutron count argument.
  - Do not credit the B_F + λ²B_GT form to Dror Eqs. 4.9–4.13. Present it as standard and cite a textbook or Hayen.
  - 21.7 background row: say relativistic Fermi function.
  - 0.032 → 0.031; "lowest allowed threshold" wording at 374 keV.
  - CDW: the Goldstone check applies to the proper (unscreened) response. Split the Coulomb lifting into longitudinal and transverse phasons. One sentence on the large condensate effective mass behind the 1 meV scale.
  - Add one sentence to slow the isospin argument for persona (a).
  - "Four classes" must match the six table rows.
- **R6 22.1 physics.**
  - WE 22-fsum: Cauchy–Schwarz shows a small remainder is sufficient, not necessary.
  - Label the four silicon-window upper edges (0.405/0.42/0.43/0.51 MeV) by what each means, or reduce them to one with pointers.
  - Use one Born-parameter definition for the Si ion (15 vs 117), or name both distinctly.
  - PAW: do not call it free of nonlocal terms. "No ℓ=2 component" → scalar response.
- **R7 Prose.**
  - Rewrite the opening's second paragraph as motivation, not an outline.
  - Cut 22.1-checks to pointers (each Ch10–21 number appears once, with \cref). The silicon ×10 appears once.
  - Delete the paragraph that repeats the 22.2 keyresult.
  - Replace the word "home" throughout (column header: "Section"). Remove Ch21 shorthand ("survivors", "guide", "P(first)") or define it in the table caption.
  - Make "f-sum" uniform as $f$-sum. Define Λ_F, v_max and 𝒬 at first use in Ch22.
  - Delete the closing aphorism of 22.1.
  - Summary: rewrite the 22.1 paragraph around its result (the 11/10/2 split; the four calculations and five measurements that would change the most), and end the book on a substantive statement, not on one table row.
- **R8 Notation (record in NOTATION.md).** No new symbol for the Fermi function (R1). Γ (gamma function) stays upright as in 21.7. Add a STYLE note that the gamma function is upright, which is book-wide practice. Extend Λ_F to the charged-current scale.
