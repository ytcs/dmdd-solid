# Chapter 22: post-revision check (isolated verifier, 2026-11-07)

Scope: tex/ch22/*.tex and figscripts/ch22 after revision.md, against rulings R1–R8 (editor-notes.md), the R9 Ge addendum, the five reports and the current tex of Ch10–21 and App. E.14. All five figscripts were rerun; gaps22_2, fig22_1, scope22_3 and we22_1 reproduce their logs exactly (index22_1 writes its log and prints only its derived lines, which agree).

**Verdict: FIXES NEEDED.** One WRONG (a bib DOI) and four CONCERNs, all small text edits. Everything else is CONFIRMED.

## 1. Rulings

**R1 Fermi function: CONFIRMED.**
- eq:22.3-fermi is gone. 22.3 evaluates F_Fermi of eq:21.7-fermi, calls it the point-charge function with prefactor 4 [Hayen Eq. (6)], and uses y_S = αZ_dE_e/p_ej of eq:21.7-beta.
- Independent mpmath evaluation of eq:21.7-fermi (r_A = 1.2·125^{1/3} = 6.0 fm): F(53, 626 keV) = 6.338, F(52) = 6.062. Daughter over parent is 1.0455 (+4.5 %, as in the summary); parent is 4.35 % lower (as in 22.3 and the CC "needs" paragraph).
- Γ(1+2γ)²/Γ(1+γ)² = 3.224 at Z = 53 and 4.0 as Z → 0. It is stated for the gamma-function factor alone; the whole-function ratio (3.10) is not claimed.
- p_ejr_A = 0.0309, so (p r_A)² = 9.5e-4 is stated as the nuclear-operator correction. αZ_dE_er_A = 0.0134, "about 1 %", is stated as L₀.
- F(53, 10 keV) = 32.55, F(53, 1 keV) = 102.1. The pEF ratios are 0.235 and 0.228 ("0.23"); the pE ratios are 0.046 and 0.014. The K-shell radius is 998 fm; 1/p is 194 fm at 626 keV and 1942 fm at 10 keV.

**R2 Gap table: CONFIRMED, with one CONCERN (C4).**
- I parsed tab:22-gaps straight from s22-2.tex: 73 rows; proof 3, bounded 10, estimate 17, unsized 38, test 5. Per chapter: Ch10–13 29 rows (6 unsized), Ch18–20 17 rows (14 unsized). These match gaps22_2.log, which gives calc 55 / meas 11 / proof-method 7.
- The same figures appear in the 22.2 prose (l.15, 17, 153, 157: "Eleven", 3 + 8), in the summary and at "all 73".
- 17.1 electron-following and both 18.2 rows are unsized. 11.5 is a method, and 14.5 is split. The 10.4 row says "at least 29", and s10-4 states "at least 29" with the density row screened.
- C4 (minor): two rows still name more than one step.
  - 16.3: "ε_in(ω) of real dots … measured or computed". gaps22_2 counts this row as a measurement. Fix: "measured" (the 22.2 prose already lists it among the measurements).
  - 19.6-lee: "U_rel … ; b_br as for two-level systems". Fix: keep U_rel and move b_br to the statement column, since the shared-step paragraph l.155 already carries it.

**R3 Calculation table: CONFIRMED for the listed items; CONCERN C1 on the "each once" claim.**
- Capture fraction 0.54 % (0.32–0.77 %) matches s18-5 l.39 and the 18 summary.
- Drag mass: on-site valence 18.6 mₑ (12–24); the trace 14 mₑ is exact but not on-site; eq:12.5-trace is checked. This matches s12-5 l.56/69 and tab:12 l.174.
- BSE 39 %/93 %: recomputed from β = 0.247, 0.289, 0.078, 0.064 (s10-10) as 0.394/0.934, and exp(σ) = 1.482.
- Cascade: ε_eh 4.15 eV [3.95, 4.73], ≥ ±0.4 eV, against 3.749 eV. This matches s18-4 l.16 and the 18 summary. The row cites sec:18.3/18.4, and 4.15 is stated in 18.4.
- Added rows 11.6, 14.2, 14.5, 15.3, 15.4 ×2 and the Ch16 group are present.
- Fig. 22.1 (fig22_1.log): 22 rows; filled calc 12 / data 9 / theory 2, with the Si window counted twice. G3 (TLS calc:O), G4 (Si lattice calc:F, data:O) and G5 (cold edge → sec:13.9-open) are applied. The prose (l.130–132) and the summary agree.
- **C1 CONCERN.** 22.1-list says the table "lists the open calculations of the book, each once", and 22.2 l.155 says "tab:22-calc lists each calculation once". The table has 33 rows against 55 calculation steps in tab:22-gaps. About 20 calculation gaps have no row and are not folded into one:
  - 10.5-open NaI STE
  - 10.8 quadratic response; 10.8 Compton profiles of bound shells
  - 12.5 Dirac contact density; 12.6 site-resolved Born charges; 12.6 S^ee at vanishing reduced momentum
  - 13.8 replicas (BSE in the vertex gauge); 13.9 GaAs control
  - 14.5 chirality decay, large moments, multiferroic
  - 15.4 spin current; 15.4 scalar amplitude channel
  - 16.5 impurity band and donor local-field ratio
  - 18.5 memory with first-principles couplings
  - 19.6 reactions, marks, U_rel
  - 20.4 thick-film transport
  - 22.3 shell-model strengths; CDW conserving response
- Fix (the qualifying option of derivation-1 G2): 22.1-list → "lists the open calculations that change a result of the running example or of a contrast target, each once; the calculation steps of the remaining rows of tab:22-gaps are stated there". l.155 → "tab:22-calc lists each of the calculations it orders once". Alternatively, add one compact catch-all row per chapter group.

**R4 Quoting restriction: CONFIRMED.**
- The 10.9 rows (tab:22-calc l.84, tab:22-gaps 10.9) say "density-row ratio 0.05 to 0.93 at 1 keV". "1.04 to 4.5" appears nowhere in Ch22.
- The heavy-mediator 10⁻⁴/10⁻⁴, the R^{-1/2} scaling, "<1 % for m_χ ≥ 10 keV" and the "pole at 𝒬 = ω, low-energy treatment not stated" all follow REF-DC-49-54-36 §4 items 1–3.
- Checked against state/DC-RESULTS.md:
  - DC-2: no hybrid+SOC promise; HSE06 inversion stated.
  - DC-2-alpha: the route is mentioned with masses failing, as that row allows. The book's 24 % is 0.101/0.0815 (E.14); the DC row says +23 %. Fine.
  - DC-91: the GaAs row uses the measured Z*/ε∞.
  - DC-67: no P_casc library numbers.
  - DC-93: CsI is "cold density" only, as in s21-7 l.136.
  - DC-41: no Al conserving-table numbers.

**R5 22.3 physics: CONFIRMED.**
- IAS threshold "about 13 to 14 MeV". Recomputed: uniform-sphere ΔE_C = (6/5)Zαħc/r_A = 14.98 MeV, minus 1.293 MeV, plus mₑ, gives 14.19 MeV. The exchange term dE_x/dZ = −0.547 MeV gives 13.64 MeV, quoted as 13.6. (The ruling's 13.2 systematics value is unsourced; the range covers it.)
- Phase space ∝ p_ejE_e.
- Quenching ≈0.75: the Gysbers source text l.52/106 says "factor of about 0.75". 1/q² = 1.78, "about two".
- Ikeda is stated as an operator identity without isospin symmetry. Counts: 21, 73, 219 against 63.
- B_F + λ²B_GT is credited to Hayen Sect. I. Dror is cited only for Eqs. 4.1, 4.2, 4.6, 4.9, 4.10 and Table 1, with no misattribution.
- 21.7 background row says "relativistic Fermi function". "Lowest allowed threshold" is at 374 keV.
- CDW: Goldstone check on the proper response; longitudinal against transverse phason; condensate mass via LRA. 0.951 meV, 271 eV, 188.7 keV per keV and 263–315 all recomputed.
- The scope count (3 + 2 + 1) matches the six table rows.

**R6 22.1 physics: CONFIRMED.**
- Cauchy–Schwarz is stated as sufficient, not necessary.
- The edges are labeled: 0.405 = first zero-phonon edge; 0.42/0.43 = phonon-assisted lead; 0.51 = comparable band.
- Born parameters: Z_κα/v_F = 15/35 (s19-2 l.66) and Z₁α/v = 117 to >1000 (19.3), related in one sentence.
- PAW and "ℓ = 2 of any scalar response" wording as ruled.
- WE numbers: 0.9785 eV, 0.507 Å⁻¹, Z_val mₑ/M_cell = 7.81e-5, 1.78 %/2.09 %, and 1.25 to 2 × θ_ep.

**R7 Prose: CONFIRMED, with one CONCERN (C3).**
- The opening's second paragraph is motivation; its last sentence states the sort, not an outline.
- 22.1-checks is pointers. The silicon ×10 is in the opening only. The keyresult-repeat paragraph is gone.
- "home" appears in no tex and is gone from the fig22_1.pdf header ("section"); the variable name in fig22_1.py is harmless.
- Guide, survivors and P(first) are defined in the tab:22-calc caption, and survivors in tab:22-gaps. "$f$-sum" is uniform. Λ_F, v_max and 𝒬 are defined at first use. The 22.1 aphorism is gone.
- The summary is built on 12/9/2 with the four calculations and five measurements, and ends on "20 of 22 channels…" (22 − 2 theory = 20).
- **C3.** The summary says "The unsized gaps cluster in the measurement chain". gaps22_2.log gives Ch14–17 16 unsized of 19 against Ch18–20 14 of 17, so the claim misreads the count. Fix: "The unsized gaps lie mostly after Chapter 13, in the special targets of Chapters 14–17 and in the measurement chain, where…". Optionally add the Ch14–17 count to 22.2 l.153 as well.

**R8 Notation: CONFIRMED.** NOTATION.md l.700 (Λ_F extended) and l.1335 ("no new symbol for the Fermi function"); STYLE.md l.43 (upright Γ(z)).

**R9 Ge addendum: CONFIRMED in substance; CONCERN C2.**
- The 0.775/0.823 eV inversion is cited to Abdurrazaq Fig. 1(a), and E.14 also says it is without SOC. "No exchange fraction reproduces both" agrees with E.14 (34 %/17 % off at 0.3).
- "adding SOC does not restore the order" agrees with E.14's HSE06+SOC result.
- 4s shift: both gaps right; masses 24 %/39 % heavy (E.14: 0.101 and 0.053 mₑ).
- The row check matches E.14 word for word: order; 0.1 eV of 0.744/0.89; 0.010 mₑ of 0.0815; 0.005 mₑ of 0.038.
- **C2.**
  - Ch22 does not name GW as the next route. E.14 does ("The next route is a quasiparticle GW correction (app:E.3) … subject to the same check"). Fix: after "…heavy." in s22-1 (Ge paragraph) add "The next route is a quasiparticle $GW$ correction on top of those bands, under the same checks (\cref{app:E.14})", with no verdict.
  - Also cite \cref{app:E.14} on the SOC clause, which rests on the book's own calculation, not on Ref. abdurrazaq.
  - Optional: E.14 gives the bracket 0.212–0.420 MeV around the 0.32 MeV estimate. The Ch22 row ("orients but does not bound") is consistent, but could name the 0.420 upper end.

## 2. Cross-chapter numbers (44 checked; all CONFIRMED against current tex)
- Ch1: v_max 2.650e-3. Ch10: ×1.28; 1.48 and the β's; ×3.2 at 1 MeV, ×1.34 at 3 MeV (s21-4 l.104); 1.1–1.2 against 0.93; at least 16 and 29 (10.4); 3d/valence 0.07–0.69; −0.76 % (10.6); 1.7 at 56.5 keV (10.9).
- Ch11: 5.0e3 at 50 meV, 65 meV (11.6); 1.3–1.5 (11.7); −19 % (11.8); quarter percent above 100 meV at 30 MeV (11.9 l.94). Ch12: 14.9; 33 %/7 %; 1.35, 1.38 (12.3); 18.6 (12–24), 1.6/0.54/0.25; 14 mₑ (12.5).
- Ch13: 0.405 (0.402–0.405 line); factor of ten (s13-9 l.87); 0.3332/0.3374; 0.81/0.89; 0.3–2.6; 1.815 eV; 1.1728 eV (13.8); 0.2119; 0.32 MeV (13.1). E.14: 350–450 core-hours; 0.3336/0.3378; 8.5e-5; the Ge mass checks.
- Ch14: 7.8 %; 0.04; 0.034, 0.124, 0.030 μN. Ch15: 1.25e4, 0.39, 0.52. Ch16: 1.33; 2.8 (we:16-band); α_ohm 0.28/0.44 (lim:16.8b; the row cites sec:16.9, which discusses α_ohm, OK). Ch17: 12.3 MeV, 0.75 keV; 5.7e5.
- Ch18: 4.15 [3.95, 4.73]; 0.097 [0.030, 0.173]; F = 0.114; 0.54 %. Ch19/20: 352/399 eV; 0.10 at 100 eV; 25 ± 3 % at 254 eV; 0.81–1.02 against 1.128; 117 (19.3).
- Ch21 (current): P(first) 0.315/0.498; GaSb 0.83; width 0.21; 4.8 % and 0.987 → 0.956 (s21-7 l.143); ×9 at 0.36 MeV and factor 3 (tab:21-dominant l.108). Ch22 quotes none of 724, 1.38 mBq/kg, 3.72e-42 or 1.77e-41, so nothing is stale (the "1.38" in tab:22-gaps is the Ch12 factor).

## 3. Regressions: CONFIRMED
- No process or campaign words in tex/ch22: grep for campaign, ledger, ruling, revision, DC-, persona, writer and [CALC] returns nothing.
- lint.py --banned BANNED-TERMS.txt tex/ch22/*.tex: 39 hits, **0 blocking**. All are LONG-SENT on table rows, captions and lists.

## 4. Bibliography
- **gysbers2019discrepancy: CONFIRMED.** Crossref for doi:10.1038/s41567-019-0450-7 gives Nature Physics 15, 428–431 (2019), with the same title. The eprint 1903.00047 matches sources/22.3/1903.00047.txt.
- **lee1974conductivity: WRONG (DOI only).** Crossref gives "Conductivity from charge or spin density waves", Solid State Communications 14, 703–709 (April 1974), **doi 10.1016/0038-1098(74)90868-0**. The bib has …90869-0, which Crossref does not resolve. Journal, volume, pages, year, authors and title are correct. Fix: `doi = {10.1016/0038-1098(74)90868-0}`.

## 5. Build: CONFIRMED
- `latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-ch22post main.tex` returns rc 0, 0 LaTeX errors and no undefined citations.
- The 11 undefined references are only app:B.2 (5) and sec:9.1/9.2/9.4 (6), all known.
- No rerun warning. No overfull boxes traced to ch22 files.

## Informational (not Ch22 fixes)
- s21-7 still calls eq:21.7-fermi the "relativistic Fermi function of a point nucleus of radius r_A". 22.3 now calls it the point-charge F₀ with prefactor 4. The optional Ch21 wording fix is listed in revision.md and is still open.

## Fix list
1. book.bib lee1974conductivity: DOI → 10.1016/0038-1098(74)90868-0 (WRONG).
2. 22.1-list and 22.2 l.155: qualify "each once" or add catch-all rows (C1).
3. s22-1 Ge paragraph: name GW as the next route, with no verdict (E.14), and cite app:E.14 on the SOC clause (C2).
4. Summary: replace "cluster in the measurement chain" with a statement matching the Ch14–17 and Ch18–20 counts (C3).
5. tab:22-gaps 16.3 and 19.6-lee: one missing step each (C4, minor).
