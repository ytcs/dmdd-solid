# Citation audit: fixes applied (2026-11-07)

Applies `citation-audit.md` under STYLE.md "Citations attribute, they do not carry content" and the "as quoted by" rule. Not committed. Readable primaries were looked for in `sources/` (all extract folders): none of Kaplan 1976, Zener 1932, Pines 1956, Tamura 1983/1985, Abragam–Bleaney, Bardeen 1937, Jacoboni–Reggiani 1983 or Kittel is held, so every primary below is credited through the secondary that was read.

## 1. Bib (tex/bib/book.bib)

| Key | Change | Checked against |
|---|---|---|
| wei2016average | misc -> article: J. Instrum. 12(04), P04022 (2017), doi:10.1088/1748-0221/12/04/P04022; title set to the journal title. Authors kept as on arXiv (Wei, Wang, Mei); Crossref lists only Wei and Mei. | Crossref; arXiv abs page (DOI listed there) |
| mei2020impact | misc -> article: J. Phys. G 47(10), 105106 (2020), doi:10.1088/1361-6471/ab9796 | Crossref |
| debernardi1994anharmonic | misc -> inproceedings: *The Physics of Semiconductors: 22nd International Conference, Vancouver, 1994* (World Scientific, Singapore, 1995). No volume or pages: Crossref has the proceedings (10.1142/9789814533638) but no record for the paper, and arXiv has no journal_ref. Pages remain open. | Crossref; arXiv abs page; extract header |
| batatia2022mace | booktitle split into Adv. Neural Inf. Process. Syst., volume 35; pages 11423–11436; doi:10.52202/068431-0830 | Crossref |
| akhiezer1965classical | Original Oliver and Boyd 1965 edition kept; the SIAM 2020 reprint DOI moved from `doi` into the note | Crossref (DOI is the 2020 reprint) |
| berghaus2023migdal, mccabe2014earth, dror2020absorption, hall2010freeze, essig2016direct, hochberg2016detecting | volume = year, number = issue, as in the other 13 JHEP/JCAP entries | DOIs encode year and issue |
| iaea2026livechart + iaea2026decaydata | Same resource (same author and URL): merged into `iaea2026livechart`, with both nuclide sets and both access dates in the note. The 4 `\cite{iaea2026decaydata}` in ch21/s21-7.tex now cite `iaea2026livechart`; ledgers/CLAIMS.md II-433 updated. | — |
| kolb1990early | Removed (cited nowhere) | grep |

## 2. Locators

- appF/F-rows.tex, row for lim:10.9d: baryakhtar2020electromagnetic `Eqs.~(2.1) and (2.2)`.
- appF/F-rows.tex, row for lim:21.2a: fox2011integrating `Eqs.~(A1)--(A2)`. The row's halo is now written as published, g = g₁Θ(v₁ − v).
- ch04/s4-5.tex:98 (lim:4.5b): kahn2022searches `Eq.~(171) and the text following it`.
- ch06/s6-4.tex:98 Kittel Al elastic constants: **no table number added**. No Kittel text is in `sources/citation-audit/` (or any other extract), so the audit's `[Chap.~3, Table~3]` could not be confirmed. Still open.

## 3. Attribution

| Location | Change |
|---|---|
| ch15/s15-1.tex:91 | Hochberg–Lin–Zurek Eq. (17) gives only the elliptic (case-I) form, citing Allen (ref. [29]). The text now says that Allen's theory contains the elliptic form, "as quoted by" Hochberg et al., and credits Mattis–Bardeen for the case-II form with a bare citation. |
| ch20/s20-4.tex:23 | "the form Kaplan et al. use" is removed. The α²F ∝ E² form is now tied only to the quadratic factor in Leman's emitted-phonon spectrum (Sect. IV). |
| ch20/s20-4.tex:28 | The book's own eq:20.4-tpb is no longer called "the rate of Kaplan et al.". The linear rise is credited as Kaplan's approximate t_pb ∝ 1/E scaling "as quoted by Guruswamy et al. [p. 5]" (checked: Guruswamy p. 5, "τpb(Ω) scales approximately as 1/Ω", ref. 10 = Kaplan). |
| ch20/s20-4.tex:35 | Now reads "a rate first given by Kaplan et al." (priority only); with α²F ∝ E² it is the distribution quoted by Leman Sect. IV (checked: item 3, P_φ(Ω) = Ω²ρ(E−Ω)[1−Δ²/E(E−Ω)], refs. [39–41]). |
| appE/E-23.tex:7 | Zener citation now also cites vutha2010simple, as in s19-2. |
| ch16/s16-2.tex:133 (lim:16.2b) | **Deviation from the audit's suggestion.** hochberg2025unconventional (2507.07164, read) does not contain v_a = ω_{p,h}/k_{TF,l} or the width, so "as quoted by Hochberg" would be false. Pines is now cited for the demon itself (priority only), v_a points to the book's own eq:16.2-demon, and Hochberg is kept only for the loss-function rate. The bare Pines citation at line 104 is unchanged. |
| appE/E-12.tex:20, 28 | Tamura rate laws now also cite leman2012invited Eq. (6) (Γ_I = Bν⁴) and Eq. (8) (Γ_A = Aν⁵), checked in the extract. "Tamura's isotropic calculation gives A = 7.41e-56 s⁴" now reads "as tabulated by Leman [Table I]" (Leman's ref. [34] = Tamura 1985). |
| ch14/s14-4.tex:35 (Abragam, g_ion ≃ 2.2) | **Unchanged; recorded as unverified.** No source that was read (in any `sources/` folder) states g ≈ 2.2 for Ni²⁺, so there is no secondary to quote through. To close it, open Abragam–Bleaney or find an open review that tabulates g for octahedral Ni²⁺. |
| ch06/s6-2.tex:17 | "goes back to Bardeen, as quoted by Giustino [Eqs. (3)–(5)]" (checked: Giustino Sect. II.A, Eqs. (3)–(5), Bardeen 1937). |
| ch18/s18-1.tex:106 | "deformation-potential phonons of Jacoboni and Reggiani [jacoboni1983monte], as tabulated by Li et al. [Table III]", matching s18-3 and fbc18.py. Caveat: Li's Table III marks most of its "previous works" electron values with footnote a (Lundstrom's textbook, ref. [26]); Jacoboni–Reggiani (ref. [85]) is flagged only on the hole D_ADP. The Jacoboni–Reggiani name follows the audit and the existing s18-3 wording. If strict sourcing is wanted, write "the literature values tabulated by Li et al." in both places. |
| Sapphire captions: ch10/s10-7.tex:96, ch11/s11-8.tex:108 | All input values are now in the caption: ordinary LO 112.4/78.0/59.7/48.1 meV (widths 1.98/0.55/0.17/0.17), TO 78.6/70.5/54.4/47.7 (0.47/0.40/0.19/0.17); extraordinary LO 109.2/63.3 (1.98/0.17), TO 72.2/49.3 (0.40/0.19). These are griffin2018 Table II converted from cm⁻¹, the same numbers used by figscripts limit10_7a.py and abs11_8.py. |
| ch11/s11-2.tex:127, 147 | 127: ordinary LO 78.1 corrected to 78.0 meV (629.5 cm⁻¹ = 78.05 meV). 147: extraordinary frequencies and ε∞ = 3.2 [Table I] are stated, and the ordinary frequencies point to fig:11-limit-2b. |

## Audit items not in this pass (still open)

s20-2.tex:46 ⟨c⁻³⟩ against the published ⟨c³⟩ (also in E-12); Skauli, Franta, Holmström table numbers and Fischer NiO, to be recorded as closed-access and unverified; arXiv-only entries to recheck before release; key-year mismatches (no action).

## Build and lint

- Private build: `latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-cite main.tex`, 5 runs, exit 0. 0 errors, 0 undefined citations or references, 0 biber warnings.
- Lint (skills/long-form-writing/scripts/lint.py with BANNED-TERMS.txt) on the 13 changed tex files: 219 warn-tier hits, 0 blocking.
