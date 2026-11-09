# Chapter 2 revision log (2026-11-02)

Scope: tex/ch02/ch02.tex, s2-1 to s2-5; tex/appA/A-1 to A-9, appA.tex; tex/appD/D-2, D-3, appD.tex; plus the cross-chapter fixes the rulings require
(tex/ch01/s1-3, s1-4, s1-5; tex/appF/F-rows.tex row 27; tex/bib/book.bib; figscripts/ch01/fig1_5.py, figscripts/ch02/fig2_6.py; ledgers/SEAMS/1.5.md).
appC was not touched. Build: /tmp/build-ch02rev, 0 LaTeX errors, 0 undefined citations in the files of this revision (the final rebuild also picked up a
concurrently written tex/ch04/s4-1.tex that cites kubo1957statistical, not yet in book.bib; not touched); undefined references only to unwritten
chapters and appendices (Chaps. 3-8, 10, 18, 20, 21; App. B.2, D.6, D.7, D.10, D.15, E.x). Lint: no banned terms, no blocking hits; the
remaining LONG-SENT and EQ-PUNCT hits are the detex merges and the full stop inside `aligned` already identified as false positives.

Key: E = editor ruling (brief), N = editor-notes, D = derivation report, P = prose report, A = reader (a), B/C = reader (b)/(c).

## Editor rulings
| item | fix | location |
|---|---|---|
| E1 Si optical phonon 64 meV | fig2_6.py set to 64 meV and rerun; 0.09 quanta, 10⁻⁸¹, βω₀ = 2.48, n_B = 0.092, e^{2.48} = 11.9, 4 K: 186 and 2.3×10⁻⁸¹, 2n_B + 1 = 1.18 (from the script printout); cited to Nilsson and Nelin (neutron data; paywalled, not read) | s2-5 opening, WE 2-oscillator; A-1 example (+cite); s1-3 fig 1.5 caption (fig1_5.py W_PH = 0.064, rerun) and "Phonons" paragraph; s1-5 "about 64 meV"; bib nilsson1972study |
| E1 toy ω₀ | left at 60 meV as instructed (labelled model) | s1-3 limit box; F-rows row 20 |
| E2 Si gap | §2.2: 1.11 eV (projection value) with 0.42 keV at v_max; §2.4: "1.12 eV at 300 K" twice; bare "1.1 eV" removed | s2-2 kinematic-match paragraph; s2-4 opening, "When second order dominates"; F-rows row 27 |
| E3 α ≈ 10 v | "about ten times" | s1-3 (two places), s2-2 after WE 2-free |
| E4 §2.4 sign | inner-integral numerator −i → +i (that display only) | s2-4 "Second-order golden rule" |
| E5 targets a/b → i_T, f_T | text, Eq. 2.4-orderings, Fig. 2.4 caption, Fig. 2.5 caption, Rayleigh paragraph, cascade paragraph, WE 2-twophoton (Γ_{i_T→f_T}, Γ_{m→f_T}, 𝒟_{f_T}) | s2-4 |
| E5 s species vs spin s; z_κ vs Z_κ | z_e, z_κ and the upright index s removed; subtraction written N_e + Σ_κ Z_κ²N_κ; A.2 charge-number sentence replaced by a plain statement of the charge density | s2-3 WE 2-jellium; A-2 first paragraph and fields paragraph |
| E5 Z residue (D.3) | renamed r_p | D-3 |
| E5 V | first-use sentence: bare V is the volume, potentials carry an argument or tilde (NOTATION clash 28) | s2-1 box normalization |
| E5 β | hydrogen decay constants b, β → λ_1s, λ_2p (also removes the bare b) | s2-2 WE 2-hydrogen |
| E5 ξ | A.8 speed moment ξ → η_2; ξ_C keeps its mandatory subscript; bare ξ is the mismatch only | A-8 |
| E5 Ω | A.9 writes dΩ_q (bold q) as in Eq. 2.2-born; no other solid-angle Ω in scope | A-9 |
| E5 δ_w | → Δ_w | s2-4 finite-part paragraphs |
| E5 rows | proposed in SEAMS 2.1, 2.2, 2.3, 2.4, 2.5, A | ledgers/SEAMS |
| E5 A.9 σ_T, μ_χe | σ_T, σ_N, μ_χe, μ_χN throughout; nuclear form written out | A-9 |
| E5 v_C upright | v_{\mathrm{C}} everywhere | s2-3 (incl. Table 2.1), A-2, A-7 |
| E6 nuclear levels | sentence replaced by ENSDF values (²⁸Si 1.78, ²⁹Si 1.27, ³⁰Si 2.24 MeV; even Ge 0.56-1.04 MeV; ⁷³Ge 13.3 and 66.7 keV, 7.8 %); cited to IAEA Live Chart (ENSDF); CSVs saved in sources/review-ch02/ensdf/ | s2-2 "Nuclei and the Helm form factor"; bib iaea2026livechart |
| E7 textbooks | all section numbers removed: Sakurai → Chap. 5 / Chap. 6; Peskin → Chap. 2 / Chap. 4; Landau-Lifshitz → whole work; Jackson → Appendix; Cohen-Tannoudji, Bruus, Fetter, Giuliani, Ashcroft already chapter level. Sakurai citation dropped from the "Born = exact for Coulomb" sentence, and the sentence with it | s2-1, s2-2, s2-4, s2-5, A-2 |
| E7 Bernreuther DOI | doi 10.1088/1475-7516/2024/03/047, volume 2024, number 03 | book.bib |
| E8 limit box | Essig comparison reworded (xenon and argon, O(30 %) in the total rate, continuum in the atomic potential) plus one plain clause that hydrogen's ≈ half does not contradict it (shell-dependent); "quarter at 10 E_B" → "between a quarter and a third for E_ej of several E_B" (script prints 0.264 at 10 E_B, checker 0.29-0.34); closing reduced to one sentence; caption: one electron = half the two-spin formula; "within a factor of two" → "reaches about half" | s2-2 Fermi-factor paragraph, limit box |
| E8 Duda | Sect. IV → Sect. V | s2-2 Helm paragraph |
| E9 pattern 19 | deleted/rewritten: "These numbers are printed by the script" ×2 (§2.2); "Eq. 2.2-dsdq is the normalization collected in A.9" → parenthesis; spin-count sentence → fact about the source; §2.4 "which is how §2.1 could claim" → "justifies"; §2.5 density-form sentence folded into the keyresult; A-1 "Sect. 1.2 rounds"; A-2 "keeps the source's units and says so"; A-4 "binding for this reason … converted before use"; A-6 "never uses one name"; A-7 "the text says so when it does", "labeled as such when quoted"; A-8 "values are conventions …", "book keeps them apart" | s2-2, s2-4, s2-5, A-1, A-2, A-4, A-6, A-7, A-8 |
| E9 process comments | removed from ch02.tex, appA.tex, appD.tex; none in ch01.tex; appC.tex not touched (other owner) | ch02.tex, appA.tex, appD.tex |
| E10 opening | no longer walks through 2.3-2.5; names why a solid differs and adds absorption by bosonic dark matter | ch02.tex |
| E10 summary | own paragraph for §2.4 (T-matrix, interfering orderings, Wigner-Weisskopf, cascade + finite part, double counting); "vanishes" → "suppressed by e^{−β\|ω\|}"; Born-validity and η clauses added; 10²⁶ repeat removed | s2-5 Summary |
| E10 2.3×10⁻⁸ | 3×10⁻⁸ → 2.3×10⁻⁸ | s2-2 WE 2-free |
| E10 950/953 | §1.4 now 1.215 and 953 | s1-4 |
| E10 v_max vs v | "q ≳ 0.42 keV at v_max" | s2-2 |
| E10 j₁ named | j_1(x) = (sin x − x cos x)/x² at first use | s2-2 WE 2-hydrogen |
| E10 rotating frame | one sentence: c̃_f = c_f e^{iξ_f t} makes the coefficients constant | s2-1 WE 2-continuum |
| E10 f_ion Jacobian, dω = E_ej d ln E_ej | two sentences before Eq. 2.2-ion | s2-2 |
| E10 factor ½ | the four contraction terms and the ½ that cancels the 2 written out | s2-3 before Eq. 2.3-direct-exchange |
| E10 A.8 → sec:2.5 | first pointer → eq:2.5-golden; second (S_ab) → sec:4.2 (NOTATION: 𝒮_O identified with S_ab in 4.2) | A-8 |
| E10 WE 2.6 vs equation | states that both photons are absorbed, so the second ordering has +ω₂ in place of −ω₂ | s2-4 WE 2-twophoton |
| E11 SEAM 1.5 | 74 events, r = 7.39×10⁴¹, limit 3.1×10⁻⁴² (10 kg yr 3.1×10⁻⁴³), two rows | ledgers/SEAMS/1.5.md |
| E11 §1.4 radius | "1/R ≈ 57 MeV for silicon, R ≈ 3.47 fm (Sect. 2.2)" | s1-4 |
| E (deliverable) R9, R10 | pasted; R10 split into two sentences to stay under 45 words | s2-1 opening, "Conditions for a rate" |
| E (deliverable) word frequencies 2.1, 2.3 | measured after revision (prose only): 2.1 so 3.0, gives 2.6, however/but 1.0, we can/see 1.0 per 1000 words; 2.3 so 2.3, gives 1.6, however/but 0.9, we can/see 0.7 per 1000 (before: 5.0/4.6 and 6.2/5.3 per 1000) | s2-1, s2-3 |

## Editor notes (editor-notes.md)
| item | fix | location |
|---|---|---|
| §1.4 radius | as E11 | s1-4 |
| WE 1.7 / SEAM 22.4 | as E11; §2.1 quote 74 matches | SEAMS/1.5.md |
| A.9 bare σ, μ | as E5 | A-9 |
| v_C upright | as E5 | s2-3, A-2, A-7 |
| Essig spin factor 2 | verified by the derivation check; text now says the source formula counts 2(2l+1) electrons and hydrogen's single electron gives half | s2-2 after Eq. 2.2-fion-pw; limit-box caption |
| textbook pointers | as E7 | — |
| "hundreds of keV" needs a source | as E6 | s2-2 |
| Adler, Wiser eq. numbers | moot: A.2 cites no equation numbers | — |
| Bernreuther DOI | as E7 | book.bib |
| Si optical phonon 64 meV | as E1 | — |
| §2.5 summary vs §2.4 | as E10 | s2-5 |
| Landau-Lifshitz §§ | removed (whole-work citation) | s2-5 |
| §2.4 a/b | as E5 | s2-4 |
| §2.4 qualitative Si band facts | wording checked; qualitative and forward-referenced to §3.3; gap value per E2 | s2-4 |
| Sakurai, Cohen-Tannoudji §§ | as E7 | — |

## Derivation report
| item | fix | location |
|---|---|---|
| D1 sign | as E4 | s2-4 |
| D2 2.3×10⁻⁸ | as E10 | s2-2 |
| D3 nuclear levels | as E6 | s2-2 |
| D4 Duda Sect. V | as E8 | s2-2 |
| D5 A.9 σ, μ | as E5 | A-9 |
| D6 a/b | as E5 | s2-4 |
| D7 64 meV | as E1 | — |
| D8 gap 1.12 eV | as E2 | s2-4 |
| D9 Lin Eq. (104) in A.9 | cited for the coupling rescaling only, "relative to the neutron coupling"; Z² for the dark photon stated without the citation | A-9 |
| D10 limit box | as E8 | s2-2 |
| D11 bib | as E7 | book.bib |
| D12 crystal form factor eqs | Eqs. (3.13) and (3.17); named in one clause | s2-2 last paragraph of ionization |
| D13 Marzari, typo | "Sect. II A, footnote 1, and Eq. (10)"; "A vertex" capitalized | A-5 |
| D14 textbooks | as E7 | — |
| D15 Rayleigh sign | "minus the dynamic polarizability … times the field squared", formula written out (no α symbol: α is the fine-structure constant) | s2-4 |
| D16 summary | as E10 | s2-5 |
| D17 SEAM 1.5 | as E11 | — |
| D18 §1.4 | as E11 | s1-4 |
| D §2.2 "heavy atoms" | → xenon and argon | s2-2 |
| D §2.2 spin factor caption | as editor-note row | s2-2 |
| D §2.5 Knapen n_{−k} | noted where Knapen Eq. (4) is cited | s2-5 thermal golden rule |
| D limit box "within a factor of two only just" | "reaches about half" | limit-box caption |

## Prose report
| item | fix | location |
|---|---|---|
| Lint gap (process-comment regex, EQ-PUNCT in aligned) | not changed: lint.py belongs to the skill, outside this brief; reported here | — |
| 2.1:3 R9 | as above | s2-1 |
| 2.1:68 R10 | as above | s2-1 |
| 2.1:35 relative error | "relative error ∼ 1/(t δE_g)" | s2-1 |
| 2.1:40 therefore / calibration (c) | rewritten as proposed | s2-1 |
| 2.1:48 split | split before the switch-on | s2-1 |
| 2.1:73 split | split twice | s2-1 |
| 2.1:92 split; √n redundancy | split before "For a classical field"; §2.3 now points back to §2.1 in one clause | s2-1, s2-3 |
| 2.1:113 breakdown | "First order therefore breaks down at Γt ≈ 0.2" | s2-1 |
| 2.1:131-145 "so" ×6 | reduced; "We see that the rate is proportional to 1/V" added | s2-1 |
| 2.1:147 relativistic paragraph | labelled as an aside for readers comparing with particle-physics papers; T-matrix kept to one clause | s2-1 |
| 2.1:118 Lin (A1), (A2) | kept (optional per report) | — |
| 2.1 seam (move coda) | declined: the labelled aside is short and A.9 relies on it | — |
| 2.2:94, :222 script sentences | deleted | s2-2 |
| 2.2:61 gap value, v_max, kinematic match | as E2/E10; calibration (c) rewrite applied | s2-2 |
| 2.2 bare "transfer" | "momentum transfer" at every occurrence in §2.2 (and A-3, A-4) | s2-2, A-3, A-4 |
| 2.2:77 paragraph | split twice; the run-on spin sentence untangled | s2-2 |
| 2.2:38 bookkeeping | parenthesis "(also Eq. A.9-dsdq)" | s2-2 |
| 2.2:131 spin sentence | one clause about the source | s2-2 |
| 2.2:156 crystal form factor | named in one clause; Eqs. (3.13), (3.17) | s2-2 |
| 2.2:160-175 redundancy, title | "once more" and the duplicate σ_T = σ̄_e sentence cut; title "Scattering off a free electron" | s2-2 |
| 2.2:174 "For concreteness" | kept (only one in the chapter) | — |
| 2.2:197 grammar, M | rewritten; "with M the nuclear mass" | s2-2 |
| 2.2:225 unanchored | "For dark-matter masses below about 10 MeV" | s2-2 |
| 2.2:208 typography | (1.23A^{1/3} − 0.60) fm, text and Fig. 2.3 caption | s2-2 |
| 2.2:183 citation | as E6 | s2-2 |
| 2.2:96 rhetorical question | kept (acceptable once) | — |
| 2.2 limit box closing | one sentence | s2-2 |
| 2.3:240-245 s species | as E5 | s2-3 |
| 2.3:240, A-2 z_κ | as E5 | s2-3, A-2 |
| 2.3 v_C | as E5 | s2-3 |
| 2.3:57, :51 count teasers | removed / named | s2-3 |
| 2.3:88 "The picture is simple" | deleted | s2-3 |
| 2.3:156 teaser | rewritten as proposed | s2-3 |
| 2.3:221 jellium | rewritten as proposed | s2-3 |
| 2.3:7 | rewritten | s2-3 |
| 2.3:47 over-claim | "rarely need a determinant" | s2-3 |
| 2.3 so/gives tic, "we see", "however" | reduced and added (counts above) | s2-3 |
| 2.3:117 "other 10²⁶" | "The spectators" | s2-3 |
| 2.3:181 imperative | "The order of the last two indices matters:" | s2-3 |
| 2.3:154 layout | line break after the display | s2-3 |
| 2.3 advisory trims (extensivity, HF energy) | declined: both readers used them as checks, and they are short | — |
| 2.3 calibration (d) | rewrite applied | s2-3 |
| 2.4 a/b | as E5 | s2-4 |
| 2.4 gap | as E2 | s2-4 |
| 2.4:7 recap opener | opens on the question | s2-4 |
| 2.4:61 duplicate argument | cut to one sentence; full argument kept in "When second order dominates" | s2-4 |
| 2.4:88 | rewritten; "in an important way" deleted | s2-4 |
| 2.4:102 pattern 19 and 0.4 % repeat | "justifies the statement of §2.1"; 0.4 % kept only in WE 2-continuum and D.3 | s2-4 |
| 2.4:24, :59 signposting | deleted | s2-4 |
| 2.4:90 10²⁶ | "the other electrons" | s2-4 |
| 2.4:150 δ_w | as E5 | s2-4 |
| 2.4:65 calibration (c) | rewrite applied; Γ_w defined there | s2-4 |
| 2.4:3 opener | kept (acceptable per report) | — |
| 2.5 64 meV | as E1 | s2-5 |
| 2.5:39, :102 "anticipated" | dropped | s2-5 |
| 2.5:85 teaser | starts with the system | s2-5 |
| 2.5:83 bookkeeping | folded into the keyresult | s2-5 |
| 2.5:64 citation | rewritten with the Knapen sign note | s2-5 |
| 2.5:19 calibration (c) | rewrite applied | s2-5 |
| appA.tex, appD.tex comments | as E9 | — |
| A-4, A-7 ×2, A-6, A-2, A-8:3 pattern 19 | as E9 | — |
| A-5:31 typo | fixed | A-5 |
| A-8 cross-references | as E10 | A-8 |
| A-9 notation | as E5 | A-9 |
| A-4:180 "least speed" | "minimum velocity needed for a momentum transfer q and an energy deposit ω" | A-4 |
| A-4:184 | "Nor is ω restricted to positive values" | A-4 |
| A-3 vs A-4 "never folded" | kept in A.3; A.4 points to it | A-4 |
| A-8:7-13 | kept as the definition home; "keeps them apart" cut | A-8 |
| A-8:13 typography | \SIrange{232}{244}{km.s^{-1}} | A-8 |
| A-2:94 polarizability "up to the sign and 1/V" | declined: stating the exact relation needs Adler 1962 and Wiser 1963, which are not public and were not read; the sentence makes no false claim | — |
| A-1:15, A-3:163 optional pointers | kept | — |
| A-2:88, A-7:204, A-9:56 count teasers | named the members | A-2, A-7, A-9 |
| A-5:40 title | "Gauge consistency" | A-5 |
| A-1:27 | deleted | A-1 |
| D-2:110 | kept (acceptable per report) | — |
| D-3 Z | as E5 | D-3 |
| Ch. opening | as E10 | ch02.tex |
| Ch. summary (a)-(d) | as E10 | s2-5 |
| Redundancy (1) √n | as above | s2-1, s2-3 |
| Redundancy (2) first order vanishes | as 2.4:61 | s2-4 |
| Redundancy (3) σ̄_e in A.9 | A.9 kept as the conventions home, now says "as in Eq. 2.2-dsdq" | A-9 |
| Redundancy (4) 0.4 % | as 2.4:102 | s2-4 |
| Redundancy (5) η/2q | 2.5 now cites Eq. 2.2-spectrum | s2-5 |
| Redundancy (6) 𝓃_e | acceptable per report; unchanged | — |
| Seams 2.1-2.5 | 2.3/2.4 seam fixed through the 2.4 opener; others clean or optional | s2-4 |

## Reader (a)
| item | fix | location |
|---|---|---|
| "??" to App. C | App. C is being written by another agent; the C labels now resolve in this build | — |
| V, β, ξ, Ω, w clashes | as E5; E_w and Γ_w are NOTATION rows with distinct subscripted meanings, unchanged | — |
| 2.1 rotating frame | as E10 | s2-1 |
| 2.1 relativistic paragraph fast | labelled as an aside | s2-1 |
| 2.2 0.4 keV at v_max | as E10 | s2-2 |
| 2.2 dΩ_q subscript | kept (NOTATION entry 29 mandates it); the existing parenthesis explains it | — |
| 2.2 3×10⁻⁸, 953/950 | as E10 | s2-2, s1-4 |
| 2.2 j₁ before named | as E10 | s2-2 |
| 2.2 f_ion Jacobian | as E10 | s2-2 |
| 2.3 factor ½ | as E10 | s2-3 |
| 2.4 sign | as E4 | s2-4 |
| 2.5 Gibbs subsection too slow | declined: short, and persona (a) is the pace setter | — |

## Readers (b) and (c)
| item | fix | location |
|---|---|---|
| B α ≈ 100 v (pp. 18, 22, 59) | as E3 | s1-3 ×2, s2-2 |
| B 3×10⁻⁸ | as E10 | s2-2 |
| B dω = E_ej d ln E_ej | as E10 | s2-2 |
| B massless-mediator diagonal element | one clause pointing to the neutrality argument of §2.3 | s2-1 |
| B Fig. 2.3 partial-wave sum not given | declined: the caption names the method and the limit box quotes the result; the full partial-wave expansion belongs to the computational appendix | — |
| B "dynamic structure factor ??" | points to Eq. 2.5-golden and Eq. A.7-S | s2-2 |
| B, C sign in 2.4.2 | as E4 | s2-4 |
| B Γ_w before definition | defined in place with a pointer to Eq. 2.4-width | s2-4 |
| B WE 2.6 two absorptions | as E10 | s2-4 |
| B f-sum "??" | points to Eq. A.7-fsum | s2-5 WE 2-oscillator |
| B A.8.3 Sect. 2.2 → 2.5 | as E10 | A-8 |
| C Born-validity parameters not derivable | declined: quoted to O(1) from the textbook at chapter level; deriving them is outside the chapter's scope | — |
| C η reminder | one clause defining η at its use | s2-2 |
| C Coulomb/kinetic "ratio about 6" | replaced by α/d ≈ 8.4 eV against (3/5)E_F = 7.5 eV and r_s = 2.0 | s2-3 |
| C Table 2.1 legibility | layout unchanged; the problem is a pdftotext artifact of the p-columns, and the table compiles cleanly | — |
| C "of course" | declined: REGISTER recommends "of course" for a caveat the reader expects, and the prose calibration accepted this sentence | — |
| C A.5 typo | as D13 | A-5 |
