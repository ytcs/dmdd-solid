# Citation audit (final pass, 2026-11-07)

Read-only audit. Nothing in tex/ or bib/ was edited. Line numbers were re-grepped after the language-audit revisions, against the tree as of the end of this run.

Rules applied: STYLE.md "Citations attribute, they do not carry content"; style-guide.md (Citations); prose-review patterns 20 (citations as content) and 22 (provenance narration); "as quoted by" for sources that were not read.

Source text extracts: `sources/citation-audit/` (148 arXiv text files). All PDFs were deleted.

## Scope and counts

| Check | Result |
|---|---|
| Bib entries | 581 (507 article, 37 book, 30 misc, 3 inproceedings, 3 incollection, plus the new zwerdling1959exciton) |
| Cite instances in the included tex | 3095 (580 distinct keys; `\cite` and `\cites`) |
| Unresolved keys | **0** |
| Duplicate keys | 0 |
| Same work under two keys | **1** borderline (IAEA, below) |
| arXiv IDs checked against the arXiv API | **301 of 301** (all of them, not a sample). All are well-formed, and the title and first author match for every one. |
| DOIs checked against Crossref (or doi.org for DataCite) | **512 of 512** (all, including Zwerdling 1959). All resolve to the right paper; no wrong DOI. |
| Pinpoint locators checked against source text | **107** in all: 72 in Limit Check boxes, 11 App F row-only, 18 random non-box cites from Ch18–22 and App C–E, plus box-against-row comparisons for all 105 boxes |
| Locator errors | **3** (one wrong, two incomplete) |
| Unused entries | **1** |

## 1. Bib defects

Required fields are author, title, year and journal/volume/pages or eprint. Every entry has author, title and year.

**Missing journal reference although one exists.** The style asks for the arXiv ID alongside the journal reference.
- `wei2016average` (misc, arXiv:1602.08005). Published as JINST **12**, P04022 (2017), doi:10.1088/1748-0221/12/04/P04022. The journal title differs slightly: "Average energy expended per e-h pair for germanium-based dark matter experiments".
- `mei2020impact` (misc, arXiv:1909.05806). Published as J. Phys. G **47**, 105106 (2020), doi:10.1088/1361-6471/ab9796.
- `debernardi1994anharmonic` (misc, cond-mat/9408051). The note names the 22nd ICPS proceedings, with no volume or pages. Add the proceedings volume and pages if a copy can be found; otherwise keep it as arXiv-only.
- `batatia2022mace` (inproceedings) has no booktitle. Add Adv. Neural Inf. Process. Syst. **35** (NeurIPS 2022).

**Entries that have a journal but no volume or pages** (accepted or in press; recheck before release): `kahlhoefer2026probing`, `berghaus2026migdal`, `pushkarov2004quantum` (pages missing; Cent. Eur. J. Phys. 2(3), 2004).

**Article with no pages and no eprint:** `lindhard1963integral` (Mat. Fys. Medd. 33, no. 10). This is the normal form for that series. Acceptable; "no. 10" stands in for the page range.

**arXiv-only entries** (verified against the API; arXiv records no journal_ref or DOI for any of them): essig2022snowmass, kadribasic2020crystal, komsa2009comparison (one of the two "arXiv-only" entries in the App E notes), dehghani2025influence, trickle2025piezoelectric, nielsen2026first, bergeron2020characterization, claes2025accurate, liu2025coherence, gan2026mean, barker2026first, hochberg2025determining, baryakhtar2020electromagnetic, aggarwal2026constraints, liang2026dielectric, aladulrazzaq2026anisotropic, ashour2024pressure, matas2025chiral, alves2026search, edwards2003evidence, zhang2026luttinger, das2023sub, buchenau2020sound, zhou2015generic, bloch2026dark, gsponer2023measurement, angloher2023light, melchiorre2025first, abdurrazaq2025accurate. Before release, run one Crossref title search on the older ones, which may since have appeared in journals: baryakhtar2020 (likely JHEP 2022), das2023, gsponer2023, angloher2023, ashour2024, kadribasic2020.

**Bib titles that are the arXiv title rather than the journal title** (same paper; IDs are correct):
- `baroni2010thermal`: the journal title is "Density-functional perturbation theory for quasi-harmonic calculations" (Rev. Mineral. Geochem. 71, 39). The arXiv title "Thermal properties of materials from ab initio quasi-harmonic phonons" is in the bib.
- `anand2014model`: the bib title is the journal title, but the key is formed from the arXiv title ("Model-independent WIMP scattering responses…"). Cosmetic.

**Year or edition mismatches:**
- `akhiezer1965classical`: year 1965, but the DOI 10.1137/1.9781611976397 is the 2020 SIAM reprint. Either cite the reprint (year 2020, with original 1965 in a note) or drop the DOI.
- Key year differs from the bib year: `du2022doped` (2024), `hochberg2025unconventional` (2026). The keys are internal; the printed year is right. No action needed unless the key rule is enforced.
- Eprint posted after publication; these are correct as they stand: graham2015, baroni2010, antonius2022, malica2020, sahling2010, sahling2014.

**Inconsistent JHEP/JCAP volume convention.** Six entries put the month in `volume`: berghaus2023migdal, mccabe2014earth, dror2020absorption, hall2010freeze, essig2016direct, hochberg2016detecting. The other 13 use volume = year with number = month. Pick one convention; biblatex prints these six as "vol. 02" and so on.

**Duplicate work (borderline).** `iaea2026livechart` and `iaea2026decaydata` cite the same database (same author and URL) for different nuclide sets and access dates. Merge them into one entry with a combined note, or keep both deliberately; they must not be read as two works.

**New entry.** `zwerdling1959exciton` (18.5) has a correct DOI, authors, volume and pages. It also closes the Ch18 open item "Ge exciton binding uncited" (s18-5.tex:60).

**RESUME item "verify lee1974conductivity journal ref":** verified. Solid State Commun. 14, 703–709 (1974), doi:10.1016/0038-1098(74)90868-0. The Crossref title and authors match.

## 2. Wrong IDs or DOIs

**None.**
- All 301 arXiv IDs match the cited work. For the four with low title similarity, I checked by hand that arXiv and journal titles differ for the same paper: anand2014model, rideau2006strained, buongiornonardelli1995high, baroni2001phonons.
- All 512 DOIs resolve to the cited work. The three DataCite DOIs resolve on doi.org: NIST ASD, NIST XCOM, and Lachish's ResearchGate DOI. Crossref differences are formatting only: MathML in titles, JHEP volume = year, or online year before print year (lejaeghere2014, duffy2007, huangfu2018, schwerdtfeger2019, all of which are correct).
- For every DOI listed by arXiv, the bib DOI agrees with it.

## 3. Locator errors (location → cited → actual → fix)

| Location | Cited | Actual | Fix |
|---|---|---|---|
| appF/F-rows.tex:174 (row for lim:10.9d) | baryakhtar2020electromagnetic Eqs. (1) and (2) | The paper numbers equations by section. The dipole Lagrangian is Eq. (2.1) and τ⁻¹ ∼ πδ³/Λ_d² is Eq. (2.2). There is no Eq. (1) or (2). | Change to `Eqs.~(2.1) and (2.2)`, as in the box (s10-9.tex:218) and the text (s10-9.tex:204). |
| appF/F-rows.tex:916 (row for lim:21.2a) | fox2011integrating Eq. (A1) | (A1) is only the step halo g = g₁Θ(v₁ − v). The spectrum with the step is (A2), and the limit on ρσg₁/m_χ is stated in the text after (A2). | Change to `Eqs.~(A1), (A2)`, as in the box (s21-2.tex:87). |
| ch04/s4-5.tex:98 (box lim:4.5b) | kahn2022searches Eq. (171) | (171) is only the q → 0 plasmon pole. The dispersion ω² ≈ ω_p² + 3q²v_F²/5 and q_c ≃ ω_p/v_F are in the text directly after it. | Change to `Eq.~(171) and the text after it`, which the App F row already has. |

**Notes (the locators hold the cited content; the text needs attention):**
- ch20/s20-2.tex:46, 62 (lim:20.2b), hernandez2025modeling Eq. (4). The source writes B = 4π³Γ_md Ω/⟨c³⟩. The book prints ⟨c⁻³⟩, which is a different average for an anisotropic medium. Write it as published, or state that the book uses the inverse-cube average.
- ch20/s20-2.tex (lim:20.2a), leman2012invited Eqs. (6), (8). (6) is the isotope rate Bν⁴ and (8) the anharmonic rate Aν⁵. The book lists the two formulas in the opposite order to the equation numbers. This is harmless.
- App F rows 202–223: the qualifier "v1 numbering" on griffin2018directional is unnecessary. The latest arXiv version has the same numbering for (19), (21), (23), (37), (B11) and (B14). It can stay or go.
- The 64 other box/row locator differences found by the comparison are all cases where the row cites a superset of the box's equations (it records the full chain). They are not errors.
- Checked items whose text extraction was too garbled to confirm the content beyond the tag: dror2021absorption Eqs. (7)–(9) and (30); bauer2026dark Eqs. (5)–(8). The tags exist, and Eq. (10) and Eq. (3) respectively confirm the content.

Every other locator checked holds the cited content. The list is in the scratch log; representative ones by chapter: lin2019tasi (77), (78), (104), (71); essig2012 (1), (5), (6), (15); essig2016 (3.13), (3.17), (A.18)–(A.21), (B.4), (B.5); knapen2021dark (6), (12), (13), (17)–(19), (24); kozaczuk (5), (7); kurinsky (4), (13), (14); hochberg2025 (6); an2015 (20); berlin2024 (7); mitridate2021 (18), (56), (38)–(40); hochberg2022impact (2), (3); gu2022; campbelldeem2022 (15), (27), (30), (36), (39), (42); trickle2020multichannel (92), (105), (106); griffin2018 (19), (21)–(24), (37), (B11), (B14), (B15), Tables I and II; ibe2018 (73), (86)–(92); knapen2021migdal (6); berghaus2023 (3.6), (3.8); dzuba2024 (14), (17); zacharias2016 (5), (10), (20); oshikawa (2.4), (2.5); qureshi1995 (8)–(10); subashiev (23); wei2016 (3); agnese2018nuclear (3); pushkarov (61); lachish (1)–(4); ponce2015 (16); giustino2017 (146); kelsey2023 (8), (9); cowan2011 (14); kotani2010 (1), (2); baroni2001 (94)–(96); blase2020 (18), (20); bernreuther2024 (2.17), (2.18); catena2025 (4.16)–(4.20).

## 4. Attribution-rule violations

### 4a. Primary sources cited as if read, where the editor notes say they were not

| Location | Source (status in the notes) | Problem | Fix |
|---|---|---|---|
| ch20/s20-4.tex:28 | kaplan1976quasiparticle (paywalled, unread; ch20 derivation-2) | "the zero-temperature pair-breaking rate of Kaplan et al." is cited to Kaplan alone and carries content (eq:20.4-tpb). | Cite Guruswamy p. 5 ("τ_pb scales approximately as 1/Ω"), or write "as quoted by Guruswamy et al.". |
| ch20/s20-4.tex:23, 35 | kaplan1976 with leman2012invited Sect. IV | "the form Kaplan et al. use for aluminum" (α²F = bE²). Leman's text never names Kaplan; Kaplan appears only as ref. [39]. Leman Sect. IV gives only the Ω² factor in P_φ(Ω). | Write "the Ω² phonon spectrum of Leman Sect. IV" and credit Kaplan with a bare citation for priority, without "use", or drop the claim about what Kaplan used. |
| ch20/s20-4.tex:57, appE/E-12.tex:61 | kaplan1976 | "Kaplan cascade" naming credit. | Acceptable (priority only). |
| appE/E-23.tex:7 | zener1932non (unread; ch19 notes) | The formula is stated with Zener alone. 19.2 was fixed to cite Zener together with Vutha. | Add `vutha2010simple`, as in s19-2.tex:59. |
| ch14/s14-4.tex:35 | abragam1970electron (not opened; ch14 notes) | g_ion ≃ 2.2 is cited to Abragam alone. The wording "usually quoted" softens it, but the source is still unread. | Verify, or attribute through an opened source (for example a review that quotes Abragam). |
| appC/C-19.tex:26 | lovesey1984theory Vol. 2 (no chapter, not read) | A bare citation next to Squires Chap. 7. | Acceptable as credit if Squires carries the content; otherwise add a chapter or drop it. |
| ch16/s16-2.tex:133 | pines1956electron (unread; ch16 notes) | The formula v_a = ω_{p,h}/k_{TF,l} is attributed "(Pines …)". Hochberg 2025 (the source that was read) cites a different Pines paper (RMP 1956, "Collective energy losses"). | Attribute the formula as quoted by hochberg2025unconventional. Keep the bare Pines citation at s16-2.tex:104 (priority, "prediction in 1956"). |
| appE/E-12.tex:20, 28 | tamura1983isotope, tamura1985spontaneous (unread; ch20 notes) | The rate laws are cited to Tamura alone. | Add leman2012invited Eqs. (6), (8), which state the same laws and were read. |
| ch17/s17-2.tex:66; ch12/s12-6.tex:78, 87 | skauli2003improved (closed access, not checked) | Values n_r = 3.48 and ε = 11.688 are cited to the primary. | They cannot be verified here. Mark them unverified in the ledger, or cite an open tabulation such as refractiveindex.info, as 16.3 does. |
| ch04/s4-4.tex:47, 101 and elsewhere | franta2017temperature (closed access) | ε∞ = 11.7 and the n_r data are used book-wide. | ε∞ = 11.7 is the standard value. I could not open the source; add a second open source for 11.7. |
| ch07/s7-4.tex:130, 139 | holmstrom2008threshold Tables III and IV (paywalled; ch19 derivation-2 NOT VERIFIED) | Values with table locators. | Locators unverified. Keep them, but record them as unverified, or drop the table numbers. |
| ch07/s7-1.tex:3, 148 | fischer2009exchange Tables I and IV for NiO, a = 4.17 Å and T_N = 523 K | The editor asked for the original measurements "if feasible". The book still cites a DFT paper's tables for measured values. | Write "as tabulated by Fischer et al." or cite the original measurements. |
| ch05/s5-1.tex:147 and elsewhere | flensburg1999lattice (abstract only) | The ch05 note asked whether ⟨u²⟩ is one Cartesian component. The abstract gives ⟨u²_LD⟩ = 0.005941(21) Å² without naming the component. With B = 8π²⟨u_x²⟩ this gives B = 0.469 Å², the standard room-temperature Si value, so the book's reading as ⟨u_x²⟩ is consistent. | No change. Record that the abstract plus B confirm the reading. |

### 4b. "As quoted by" chains (checked: the secondary actually quotes the primary)

All 13 chains checked hold. In each case the secondary states the value or formula and cites the primary:
- Lockwood ε₀ = 12.9, ε∞ = 10.88 in knapen2018detection, ref. [34] (s5-5.tex:95).
- Fernandez L/S = 0.34 in kwon2000unquenched, ref. [17] (s14-4.tex:39).
- Kamm–Alers C₁₁ = 114.3 GPa (1143 kbar) in malica2020quasi Table 2 (s15-1.tex:7).
- Allen 1971 in hochberg2016absorption, ref. [29], Eq. (16) (s15-4.tex:71, 76; F-rows 525).
- Mott n_c ≈ 3×10¹⁸ in du2022doped Sect. II (s16-5.tex:104).
- Kinchin–Pease in cogswell2021passive Sect. II (s16-6.tex:55).
- Golding C_l = 1.9×10⁻⁴, C_t = 2.0×10⁻⁴ at 500 MHz in buchenau2020sound (s16-7.tex:58).
- Black et al. in meissner2021acoustic Eq. (8) (s16-8.tex:28).
- Bertuccio–Maiocchi for GaAs in nielsen2026first Fig. 1, ref. [20] (s18-4.tex:46, 68).
- Schmid 200–300 ns in lo2015hybrid, ref. [17] (s18-5.tex).
- Lindhard's basic integral equation in sarkis2020study Eq. (3) (s19-3.tex:43).
- Lewin–Smith g(ε) in sorensen2015atomic Eqs. (5)–(7) (s19-3.tex:63).
- Lee–Rice–Anderson and Lee–Fukuyama in kim2023observation (s22-3.tex:95).
- The PbS exciton radius of 20 nm in blanco2023dark, ref. [129].

One chain is weaker than its wording: s15-1.tex:91 says Hochberg, Lin and Zurek quote "the elliptic form and the corresponding case-II form of Mattis and Bardeen". hochberg2016absorption gives the elliptic (case-I) form, but its text does not name Mattis–Bardeen or case II. Credit Mattis–Bardeen with a bare citation and keep "as quoted by" for the elliptic form only.

### 4c. Implicit "as quoted by" (a named primary credited only through a secondary's citation)

- ch06/s6-2.tex:17: "goes back to Bardeen~\cite[Eqs. (3)–(5)]{giustino2017electron}". Write "as quoted by Giustino" or cite Bardeen 1937.
- ch18/s18-1.tex:106: "the deformation-potential phonons of Jacoboni and Reggiani~\cite[Table III]{li2021deformation}". Write "as tabulated by Li et al.".

### 4d. Citations as sentence subjects

There are 49 sentences of the form "Ref.~\cite{…} writes / uses / defines …", mostly in App A and B (notation dictionaries) and E.7. All of them state a fact about the literature next to content the book states itself, which pattern 19 allows ("phrase it as a fact about the literature, in one clause"). None stands in for content. None starts with a bare `\cite`. **No violation.** If the editor prefers fewer of them, the densest cluster is E-7.tex:91–97 (five in a row).

### 4e. Claims that require opening the source (pattern 20)

These are figure inputs given only by reference:
- ch10/s10-7.tex:96 (lim:10.7a caption) and ch11/s11-8.tex:108: sapphire "frequencies and 77 K widths of Ref. [griffin2018 Table II]". The widths are not stated. s11-2.tex:127 states the frequencies.
- ch11/s11-2.tex:147: "Lossless factorized ε from the data of Ref. [Tables I and II]".
- Fix: state the eight sapphire widths once (for example in the 11.2 caption or a table in App E) and point there.

No body-text formula or value was found that is given only by reference. The earlier Limit Check problem is gone: every box states its formula.

### 4f. Textbook locators asked for in the notes (not opened; checked against standard editions)

- ch06/s6-4.tex:98: the Al elastic constants (106.8, 60.7, 28.2 GPa) are cited to kittel2005introduction with **no table number**, which the App D note asks for. Add `[Chap.~3, Table~3]` (8th ed., elastic stiffness constants of cubic crystals; confirm against the edition held).
- Already consistent with the 8th edition: Kittel Chap. 5 Table 1 (Θ_D = 645 K) and Chap. 10 Table 5 (ξ₀ = 1.6 μm).
- Consistent with the editions cited: Fetter–Walecka Chaps. 3 and 7; Mahan (3rd ed.) Chaps. 2 and 3; Born–Huang App. VIII (adiabatic approximation).
- dolling1963inelastic: the title matches the standard citation ("Lattice vibrations in crystals with the diamond structure", IAEA 1963, Vol. II, p. 37).
- Kubo 1957 is cited without equation numbers, as ruled.

## 5. Unused entries

- `kolb1990early` (Kolb and Turner, The Early Universe). It is not cited in any included file. Delete it, or cite it in 1.1.

Neither of the two unincluded files (gate.tex, appE/appE-gate.tex) carries a citation that is otherwise missing.

## 6. Resolution of the two App F items

**10.9d (box "Eqs. 2.1–2.2" against row "1–2"): the box is right.** In arXiv:2006.13918 (JHEP numbering by section), the dipole operator (1/Λ_d) χ̄* σ^{μν} χ F_{μν} is Eq. (2.1) and τ⁻¹ ∼ πδ³/Λ_d² is Eq. (2.2). There are no Eqs. (1) or (2). Fix F-rows.tex:174 to `Eqs.~(2.1) and (2.2)`. Text and box (s10-9.tex:204, 218) are correct, and the formula matches the source.

**21.2a (box "A1–A2" against row "A1"): the box is right.** In arXiv:1011.1915 App. A, Eq. (A1) is the step halo g(v; v₁) = g₁Θ(v₁ − v), Eq. (A2) is the recoil spectrum with it, ∝ g₁Θ(v₁ − v_min), and the bound on ρσg₁/m_χ is stated in the text immediately after (A2). The book's bound η̃(u₀) ≤ minᵢ N_i^up/𝒜_i(u₀) needs both. Fix F-rows.tex:916 to `Eqs.~(A1), (A2)`. The row's phrase "step halo g = g₁Θ(v₁ − v_min)" merges (A1) with (A2); "g = g₁Θ(v₁ − v)" is the published halo.

## Fix list (in priority order)

1. F-rows.tex:174 and F-rows.tex:916, the two App F locators above.
2. s4-5.tex:98, locator for Eq. (171).
3. s20-4.tex:23, 28, 35, Kaplan attribution (4a).
4. E-23.tex:7, add Vutha. E-12.tex:20, 28, add Leman. s16-2.tex:133, Pines formula via Hochberg 2025.
5. s15-1.tex:91, the Mattis–Bardeen chain. s6-2.tex:17 and s18-1.tex:106, implicit chains.
6. s20-2.tex:46, the ⟨c⁻³⟩ form. s6-4.tex:98, the Kittel table number.
7. Sapphire widths in the captions at s10-7.tex:96, s11-8.tex:108 and s11-2.tex:147.
8. Bib: add the journal references for wei2016average and mei2020impact; add a booktitle for batatia2022mace; resolve the akhiezer DOI and year; unify the JHEP/JCAP volume convention; settle the IAEA pair; delete or cite kolb1990early.
9. Record as unverified (closed access): Skauli, Franta, Holmström table numbers, Abragam g ≈ 2.2, Fischer for measured NiO values.
