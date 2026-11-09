# Final residuals (2026-11-07)

Closes the items left open by `citation-audit.md` and `citation-audit-applied.md`, and regenerates App. B. Rules: citations only attribute; "as quoted by" for sources that were not read; no claim requires opening a source. Not committed.

## A. Citation items

| Item | Resolution |
|---|---|
| s14-4.tex:35, Abragam g ≈ 2.2 | No source the book reads gives it. A readable source was fetched with lit.py: Kritzell et al., arXiv:2308.10159 = Adv. Opt. Mater. 12(10), 2302270 (2024), doi:10.1002/adom.202302270 (Crossref-checked). It quotes the NiO Landé factor 𝔤 = 2.18 from the literature (its ref. [9], Rezende et al. 2019). The text now reads "the literature value of the Landé factor, as quoted by Kritzell et al., is 2.18; we round it to g_ion ≃ 2.2". `abragam1970electron` is removed from the bib (it is no longer cited) and `kritzell2024terahertz` is added. Text extract: sources/14.4/2308.10159.txt. SEAMS/14.4.md noted. |
| s18-1.tex:106, s18-3.tex:69, Li Table III | Li et al. Table III (sources/6.2/2104.08998.txt) marks every "previous works" value the cascade uses with footnote a (ref. [26], Lundstrom, *Fundamentals of Carrier Transport*, 2nd ed., 2000). Jacoboni–Reggiani (ref. [85], footnote p) appears only on the hole D_ADP, which also carries footnote a. Both places now credit "Lundstrom's textbook [lundstrom2000fundamentals], as quoted by Li et al. [Table III]", and Li's extra credit of the hole acoustic value to Jacoboni and Reggiani is mentioned in a clause. New bib entry `lundstrom2000fundamentals`. The fbc18.py docstring matches. |
| s20-2.tex:62 (lim:20.2b), ⟨c⁻³⟩ | Now written as published: B_iso = 4π³g_md Ω_at/⟨c³⟩, where ⟨c³⟩ is the polarization-averaged cubed speed [hernandez2025modeling, Eq. (4)], checked in sources/20.2/2408.04732.txt. The text then says that the book uses ⟨c⁻³⟩, the average the Debye density of states contains, and that the two agree when the speeds are equal. E-12.tex:26 has the same note in a parenthesis. The F-rows entry already says "1/⟨c³⟩ in the source". |
| Skauli (s17-2.tex:66; s12-6.tex:78, 87) | The audit's fix was applied: cite the open tabulation as well. All three now cite `polyanskiy2024refractiveindex` (refractiveindex.info, GaAs/Skauli: 22 °C, formula 1, 0.97–17 µm). The book's numbers were checked against that formula: n = 3.4185 at 1 eV, ε without the phonon term = 11.688, n = 3.475 at 1.17 eV (3.48), and the range ends at 1.278 eV. Copy: sources/12.6/gaas_skauli.yml. |
| Franta, ε∞ = 11.7 (s4-4.tex:47; E-4.tex:70) | The audit's fix was applied: a second open source for 11.7. s4-4 now adds "the square of the long-wavelength refractive index 3.414 of Li's tabulation at 293 K [li1980refractive], as reproduced in Ref. [polyanskiy2024refractiveindex]" (refractiveindex.info Si/Li-293K, n(14 µm) = 3.4142; 3.4142² = 11.66). E-4 points to sec:4.4. |
| Holmström Tables III, IV, Sect. IV (s7-4.tex:130, 139; s19-1.tex:87; s19-4.tex:14) | **Verified, no change.** The audit called these paywalled, but an open copy is held: sources/7.4/holmstrom2008.txt (SEAMS/7.4.md). Table III: V 3.4/3.9, interstitials 4.7–5.8, Frenkel pair 6.8/7.5, bond defect 2.6/3.0 eV. Table IV: ⟨111⟩ 12.5, ⟨100⟩ 19.5–20.5, E_d,ave^FP 36, E_d,ave^BD/FP 24 eV. Sect. IV: SW 20.5/16.5 against DFT 14.5/12.5 along ⟨111⟩, so 4–6 eV over. All the locators hold. |
| Fischer NiO, a = 4.17 Å and T_N = 523 K (s7-1.tex:3, 148) | The audit's fix was applied. Both now read "the measured value … as tabulated by Fischer et al." (Table I, exp. column 4.17 Å; Table IV, "Experiment" row 523 K; checked in sources/E.9/0905.0391.txt). |
| Kittel Al table number (s6-4.tex:98) | No readable Kittel text is held, so the table-number request is dropped and the citation stays general (it already was). Closed in SEAMS/C-c.md item 5. |

## B. App. B regeneration

**gen_B3.py (acronyms).** The matcher had two gaps, and both are now fixed. First, digit-bearing acronyms: a letter with its digits inside one word matches (G4 ↔ Geant4), and trailing digits match the end of a number (09 ↔ 2009). Second, a new appositive form, "ACR functional|code|toolkit|…, the ⟨expansion⟩". G4CMP ("Geant4 Condensed Matter Physics", 20.1) and TB09 ("meta-generalized-gradient functional of Tran and Blaha (2009)", 21.6) are now taken from the text. Seven acronyms that the text expands in words whose letters do not follow the acronym were added to DEFINED_IN_TEXT: CODATA, EXCEED-DM, HSE06, NR, PBE0, SALMON and XCOM.

**Acronyms expanded at their first book-wide use (exact edits):**
- ACE and MLIP (E-23)
- ANO and RCC (E-16; ANO-RCC now splits into the two)
- CASSCF (E-19)
- CODATA (A-1)
- CPU (E-12)
- DAMIC (s10-9)
- DLMF (C-8)
- DOS and NR (F-rows)
- FFT (E-1)
- FIRE (E-23)
- ST and FT (E-12 table)
- GIPAW (E-26)
- GPU (E-22 caption)
- GRASP (E-20)
- HOMO and LUMO (D-5)
- NV, PBE0 and WEST (E-21)
- SALMON (E-23)
- SCAN (E-17)
- ZBL (E-11; the subsection title now spells out Ziegler–Biersack–Littmark, and "(ZBL)" follows the names in the first sentence)

PT was used only in a subsection title (D-28), which now reads "inversion and time reversal", as the body does.

**Result:** B-3 has 85 acronyms, **0 unexpanded**, and 0 expanded only after their first use.

**gen_B1.py (symbols).** NOTATION rows were edited where entries 102(a) and 103(b) asked. The 14.2 row X_αβ, f_me now reads u_αβ, f_me, and E.23's track density λ_tr joins the row 𝓃_pair, C_Aug, r_tr. NOTATION entry 104 records both. The following are all present in the regenerated B-1.tex:
- the F̄_μν, F̄² row (C.9)
- d_kink (C.20)
- f^L₁, f^L₂ (10.3)
- 𝔞_kj (C.16)
- the C.12 rows Ξ, 𝓑; 𝗄_i; λ_i; ℬ_h…; ξ_a (21.2, also C.12)
- the entry-100(b) rows (spot-checked: w_ξ, F_model, z_CL, H_FK, 𝒢_Λ, T_N, N_meas, f_coll, C_Aug, r_tr)

Two meanings had printed a precomposed accented letter as a text letter. These were ô in o_γ (2.3) and ê in M^±_cvν(k, Q; ê) (6.5). Both are now fixed through RAW_FIX, and the converter now logs any lone accented letter.

**B-1.tex check:**
- 1527 rows
- 0 unrendered symbols. The log shows 0. The only non-ASCII characters left are accents in personal names: Grüneisen, Fröhlich, Néel, Landé, Røising, Fejér, Meißner, Rényi.
- 0 section numbers in symbol cells
- 0 editorial words. Two hits for "entry" are matrix entries.
- 0 missing labels
- 12 dropped rows (dash or removed first use, as before)

## Build and lint

- Private build, `latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-final-B main.tex`: 5 runs, exit 0. The result was 0 errors, 0 undefined citations or references, and 0 biber warnings.
- Lint (skills/long-form-writing/scripts/lint.py, BANNED-TERMS.txt) on the 28 changed tex files: 352 warn-tier hits, mostly LONG-SENT in the B tables; **0 blocking**.

## Still open (outside this pass)

These are the arXiv-only entries to recheck before release and the key-year mismatches (no action needed), as in citation-audit-applied.md. The debernardi1994anharmonic pages are also still open.
