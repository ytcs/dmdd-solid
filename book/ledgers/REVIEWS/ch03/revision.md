# Chapter 3 revision log (2026-11-02)

Scope: tex/ch03/ch03.tex, s3-1 to s3-6 (Summary at the end of s3-6); tex/appC/C-1 to C-8; tex/appD/D-4, D-5; D-6 (H_D → H_Dar only);
tex/appE/E-7 and tex/appC/C-15 ((Zα)² clause only). SEAMS 3.1–3.6 updated. No QE run, no figure regenerated.
Build: /tmp/build-ch03rev, 0 LaTeX errors, 0 undefined citations; the 96 undefined references of the whole book are all to unwritten targets.
Those referenced from the files of this revision: chap:10, sec:6.5, 7.2, 8.5, 8.6, 10.1, 10.4, 10.6, 10.7, 10.9, 11.4, 11.7, 12.5, 13.1, 13.3, 13.7, 13.9
(all unwritten). Lint: 0 blocking hits in every file; the remaining
EQ-PUNCT hits are periods inside `cases`/`aligned`/`gathered` or mid-sentence displays, and the LONG-SENT hits are inflated by inline math,
captions and EQN placeholders (the new long sentences were split).

Key: E = editor ruling (brief), N = editor-notes.md, D = derivation.md, P = prose.md, A = reader-a.md, B/C = reader-b.md personas (b)/(c),
F = figures.md.

## Editor rulings (brief)
| item | fix | location |
|---|---|---|
| E1 (200) vs (222) | 3.2: bond charge gives (222) only, (200) zero by the glides; NFE paragraph: U_{G200} = 0 exactly by the glides; 3.4: (222) from the bond charge, (200) vanishes for any crystal-symmetric potential; all point to we:3-diamond and C.17 | s3-2 NFE and sp³ paragraphs; s3-4 after KS keyresult |
| E1 glide defined | one sentence at first use: reflection in a plane parallel to a cube face plus a translation by a quarter face diagonal within it (from C.17) | s3-1 we:3-diamond |
| E2 gap values | 1.17 eV low T / 1.12 eV at 300 K unchanged in 3.3; 1.11 eV only as "the projection threshold" (3.3 l.24 and WE 3-kc); WE 3-scales recomputed at 1.17 eV (0.44 keV = 0.19(2π/a); 0.49–4.81 keV = 2.11(2π/a) at 1 MeV; 10/100 MeV unchanged); chapter opener "about 1.1 eV" → 1.17 eV | s3-1 we:3-scales; s3-3 we:3-kc; ch03.tex |
| E3 lattice constants | room temperature throughout, "zero-temperature" labels removed: Ge 5.658 Å (Rideau Sect. II A; Vurgaftman covers III–V only), GaAs 5.653 Å (Vurgaftman); Table 3.1 value and caption | s3-3 Ge and GaAs paragraphs, tab:3-materials |
| E4 figures text | k_c 0.843 for every PBE value (3.3 text, 3.4 computational paragraph re-anchored to a = 5.431, Fig. 3.12 caption); measured 0.85 kept where it is the measurement; LDA minimum written 0.848 as in Fig. 3.8; Ge semimetal in PBE with SOC (3.4 gap paragraph); LDA caveat present in Fig. 3.8 caption and text | s3-3, s3-4, s3-6 |
| E4 l.44 paragraph | figures are QE (true now); duplicate "first-principles … from DFT" sentence removed; empirical pseudopotential introduced as a model used only for the sum-rule checks | s3-3 paragraph after Fig. 3.7 |
| E4 k·p check | Cohen–Bergstresser inputs in one sentence (−0.21, +0.04, +0.08 Ry on |G|² = 3, 8, 11; τ = ±(a/8)(1,1,1); |G|² ≤ 20 → 113 PW); degenerate pair contributes 4.53 of 5.43, Σ|v|² = (4.1×10⁻³)² | s3-3 "Silicon provides a check" |
| E5 Wannier | wannier90 examples described as reported (symmetric start → away; same-orientation start → mixed stationary point, 2.02 Å²/0.79 Å away, 2.37 Å² along); "the more localized set is the one that points away from the bonds"; reality "found", not proven (MV 1997), and "reality, a common check that a minimization has converged"; Chern invariant defined in one clause | s3-6 disentanglement paragraphs, l.23 |
| E6 δk | bold κ → δk (δk_α, δk_∥, δk_⊥, |δk|) in the k·p subsection, eq:3.3-valley and eq:3.3-holes; κ now only the basis index | s3-3 |
| E6 φ^at_j | all atomic orbitals of the tight-binding subsection | s3-2 |
| E6 φ^tr_n | kept; gauge phases renamed θ_n(k) so φ^tr is the only φ in 3.6 | s3-6 l.23, 31, gauge-rule paragraph |
| E6 velocity hat | \op{\vect{v}} → bare v (A.5 l.38 convention) | s3-2 eq:3.2-pv, text, eq:3.2-dHk, practice paragraph |
| E6 E_qp | already E_qp in 3.4; E.3's E^QP is outside this brief, left for the E.3 owner | — |
| E6 H_D → H_Dar | both occurrences | appD/D-6 |
| E6 NOTATION rows | δk, γ̄^Lu, φ^at_j, bare v, θ_n; Ch. 3 rows confirmed in SEAMS 3.2, 3.3, 3.4, 3.6 | ledgers/SEAMS |
| E7 C.2 duplicate | derivation and counting cut; subsection now states eq:C.2-latticesum as eq:3.1-latticesum (label kept for C.2's own references) and keeps the infinite-crystal form, eq:C.2-unfold and the grid material; opener reworded | appC/C-2 |
| E8 attribution | norm conservation = Hamann–Schlüter–Chiang; Vanderbilt's ultrasoft scheme relaxes it (augmentation); Hamann's ONCV keeps it in generalized form (Eq. 23) | s3-5 after eq:3.5-logder |
| E9 (Zα)² clause | E.7 and C.15: (Zα)² is the size of each term; net 1s shift about a quarter of it, 0.26 % Si, 1.46 % Ge | appE/E-7 core paragraph; appC/C-15 Darwin paragraph |
| E10 "keyresult" in prose | → "The exactness condition of eq:3.6-exact" | s3-6 WE 3-w1d |
| E10 "We will" runs | openers of 3.2, 3.3, 3.4, 3.5, 3.6 reduced to one orienting sentence without "We will"; 3.1 "We will" → "We construct" | section openers |
| E10 "representative calculation" | removed from Figs. 3.6, 3.7, 3.8, 3.9 captions and s3-5 | s3-3, s3-4, s3-5 |
| E10 WRONG/GAP items | C.4 sign; 0.27 → 0.26 %; 4.8 → 4.7 meV; eq:3.5-rhoAE one-cell normalization (see D rows) | appC/C-4; s3-5; s3-6 |
| E10 reader-a items | Δ_xc from the piecewise-linear E(N) (3.4 and D.5); q = 377 eV stated as a reference scale, not an allowed event; ω/v_max for any mass vs 2ω/v_max at threshold (38/76, 57/114, 11/22 keV) and Fig. 3.10 caption | s3-4, appD/D-5, s3-2 WE 3-vertex, s3-5 core paragraphs |
| E10 undefined terms | semilocal, quasiparticle correction (3.3); Wigner–Seitz cell (3.1); Chern invariant (3.6); glide (3.1); Ry and Bohr radius (3.5); scalar-relativistic (Fig. 3.9 caption); HOMO/LUMO (D.5) | as listed |
| E10 "rank eight" | "8×8 matrix"; "matrix of rank N_W" → "N_W×N_W matrix" | s3-6 opener, after eq:3.6-HWR |
| E11 Summary | re-checked: 1.17 eV, 0.85 measured valley, 0.916/0.191, 3.4 eV, 0.333 MeV, 0.52 → 0.148 MeV, (Zα)², 0.3 GeV all agree with the revised sections; "several keV and above" → "Above about a keV" | s3-6 Summary |

## Editor notes (editor-notes.md)
| item | fix | location |
|---|---|---|
| N Γ sweep | ch03 has no rate written as upright Γ; stale typography sentence fixed ("the rates Γ" → "the italic rates \varGamma") | s3-1 zone-point paragraph |
| N C.2 pointer | as E7 | appC/C-2 |
| N Ge/GaAs a with public source | as E3 | s3-3 |
| N 3.2 φ^at, hat | as E6 | s3-2 |
| N Si gap 1.17/1.12 | as E2 | s3-1, s3-3 |
| N we:3-diamond verify | confirmed by D (symmetrized numerically); text consistent | s3-1, s3-2, s3-4 |
| N lattice constants, ε∞ 11.7 | as E3; ε∞ unchanged | s3-3 |
| N Figs. 3.6/3.7 QE vs model | QE (figure pass); text re-synced (E4) | s3-3 |
| N symbols γ^Lu, ξ_SO, 𝛋, L/S | δk adopted; γ^Lu, ξ_SO, L, S rows proposed in SEAMS 3.3 | SEAMS/3.3 |
| N 3.4 QE, E_qp, E.1 pointer | figures QE; E_qp in 3.4; E.1 pointer and E.3 rename outside this brief | — |
| N 3.5 two derivations | both stay; 3.5 already points to C.15 | — |
| N 3.5 Si 2p doublet | "a few tenths" kept, consistent with 99.4/99.8 eV given in the same section | s3-5 |
| N Fig. 3.9 potential | caption already states the writer-generated TM potential | s3-5 |
| N 3.6 orientation | confirmed (F); text keeps away-from-bond result, plain statement added (E5) | s3-6 |
| N 3.6 interpolation errors | confirmed (F: 350.4/123.0/50.5 meV); unchanged | s3-6 |
| N new 3.6 symbols | rows in SEAMS 3.6 (and θ_n added) | SEAMS/3.6 |

## derivation.md
| item | fix | location |
|---|---|---|
| D WE 3-scales "13106" (GAP) | "which a direct count confirms" (no fragile integer) | s3-1 |
| D WE 3-scales 1.11 eV (GAP) | as E2 | s3-1 |
| D WE 3-gap1d 0.024 (WRONG) | "lower edge 0.023 eV, upper 0.026 eV"; second-order −0.025 eV "for each edge, the average of the two computed shifts" | s3-2 |
| D 3.3 l.44 DFT/EPM (GAP) | as E4 | s3-3 |
| D EPM inputs (GAP) | stated (E4) | s3-3 |
| D sum-rule decomposition (WRONG) | degenerate pair 4.53 of 5.43 (E4). Note: figscripts/ch03/fig3_6.py text-check block still asserts the old 2.27; script not rerun (no figure changes in this revision) | s3-3 |
| D Kane 0.0718 (precision) | recomputed from the model (epm.py, as in fig3_7.py): E_P = 18.32 eV, gap 1.417 eV → 0.0718; printed to that precision | s3-3 |
| D lattice-constant labels | as E3 | s3-3 |
| D PBE numbers mix lattice constants | 3.4 paragraph re-anchored: a = 5.431 → 0.843, m∥ 0.95, 0.557 eV; relaxed 5.477 → 0.602 eV; Fig. 3.12 0.843 | s3-4, s3-6 |
| D r_c(p) 1.88 → 1.89 Å | text and Fig. 3.9 caption | s3-5 |
| D eq:3.5-rhoAE normalization (GAP) | projections taken with states normalized over one cell (A.5), with the 1/N bookkeeping stated | s3-5 after keyresult |
| D WE 3-Zalpha 0.27 % (WRONG) | 0.26 % | s3-5 |
| D wannier90 example (WRONG) | as E5 | s3-6 |
| D WE 3-w1d 4.8 meV (WRONG) | 4.7 meV | s3-6 |
| D WE 3-w1d 0.36 eV a (GAP) | "up to 0.3 to 0.8 eV a in different draws" | s3-6 |
| D C.3 T_d vs O_h (GAP) | Si/Ge O_h; GaAs T_d, half the operations, no inversion; T_d with q → −q gives O_h | appC/C-3 |
| D C.4 sign (WRONG) | right side of the display sign-corrected; "minus the bracket of eq:2.4-fp"; eq:C.4-dPV unchanged | appC/C-4 |
| D C.8 1.5 % wording | Gaussian term 1.4 %, with erfc 1.5 %; x written 544/238 = 2.2857 | appC/C-8 |
| D D.4 l.78 pointer | sec:4.2 → sec:2.5 | appD/D-4 |
| D NOTATION drifts: V(r) in eq:3.3-HSO, V_l(r) in eq:3.5-radial | not applied (no ruling); proposed in SEAMS 3.3 as open | SEAMS/3.3 |
| D NOTATION drifts: unhatted ϱ (D.4 density matrix, C.5 spectral density) | declined here: no ruling; both are local to their appendix and defined at first use; left for the notation batch | — |
| D NOTATION drifts: φ(p), φ_nl in Figs. 3.9/3.10; PAW φ^AE (\phi) vs \varphi | declined: momentum-space orbitals and PAW partial waves carry arguments/superscripts that keep them apart from the field φ; glyph unification left to the notation batch | — |
| D known items (𝛋, hat, L/S, ξ, Γ, H_D) | handled under E6/N | — |

## prose.md
| item | fix | location |
|---|---|---|
| P A1 (200) (three places) | as E1 | s3-2, s3-4 |
| P A2 gap 1.11 | as E2 | s3-1 |
| P A3 lattice constants | as E3 | s3-3 |
| P A4 κ, φ_j, phase, hat | as E6 | s3-2, s3-3, s3-6 |
| P A5 stale Γ sentence | as N | s3-1 |
| P A6 "always dΩ_q" | "a solid angle always carries a subscript, as in dΩ_q" | s3-1 |
| P A7 CBM 0.85 in Fig. 3.12 | 0.843 | s3-6 |
| P 3.1 l.26 κ sentence | rewritten as suggested | s3-1 |
| P 3.1 l.139 "of order N" | "Physically, the N phases add up only when they agree … and cancel otherwise" | s3-1 |
| P 3.1 l.141 essig citation | dropped | s3-1 |
| P 3.1 l.220 rhetorical question | statement | s3-1 |
| P 3.2 opener outline | one sentence | s3-2 |
| P 3.2 l.122 flat sentence | calibration rewrite ("Of course, the result is only as good as the basis …") | s3-2 |
| P 3.2 l.277 second reading | rewritten (with A item) | s3-2 |
| P 3.2 l.279 unanchored "other half" | band 2 quarter stated | s3-2 |
| P 3.2 l.268 "15 to 20 percent" | \SIrange | s3-2 |
| P 3.3 opener | one sentence | s3-3 |
| P 3.3 l.111 "we call" | "denoted" | s3-3 |
| P 3.3 l.203 "half way", three conclusions | "halfway"; paragraph split before "A particle of 0.333 MeV" | s3-3 we:3-kc |
| P 3.3/3.4 Kane 0.025 duplicate | kept in 3.3; 3.4 points to it | s3-4 |
| P 3.3 l.182 so/because chain | rewritten as suggested | s3-3 |
| P 3.4 l.30 anthropomorphic (and D.5:26) | "does not depend on the nuclei" | s3-4; appD/D-5 |
| P 3.4 l.64 "ladder" | "Each step from LDA to GGA to hybrids" | s3-4 |
| P 3.4 l.82 / D.5:89 duplicate | D.5 cut to a pointer to the band-gap problem of 3.4 | appD/D-5 |
| P 3.4 l.89 "(every listed value)" | "(all values listed there)" | s3-4 Fig. 3.8 |
| P 3.4 l.107 "densities" | "Energies and the density vertex are easy." | s3-4 |
| P 3.4 l.154 label sec:1.3-edge | note only (label resolves; owned by Ch. 1) | — |
| P 3.5 l.3 "transfers" | "momentum transfers" | s3-5 |
| P 3.5 l.17 "have" | "had" | s3-5 |
| P 3.5 l.43 f-sum | "$f$-sum" (also C.5 ×3) | s3-5; appC/C-5 |
| P 3.5 l.47 numbers | \SI{10}{\percent}, \SI{2}{keV} | s3-5 |
| P 3.5 l.83 size of reconstruction | Griffin Sects. 3.1 and 4: well above the pseudo result at ~10 eV thresholds; > an order of magnitude with core states at higher thresholds, especially Ge (the source gives no single factor at a stated threshold) | s3-5 |
| P 3.5 l.158 garden path | rewritten as suggested | s3-5 we:3-Zalpha |
| P 3.5 l.29 HSC register | "Two of them do the work …" | s3-5 |
| P 3.6 l.161 "keyresult" | as E10 | s3-6 |
| P 3.6 l.93 three jobs | split before the figure result | s3-6 |
| P 3.6 l.138 three jobs | split at "Derivatives come for free." | s3-6 |
| P 3.6 l.149 signposting | "That is the rule of app:A.5, and the reason is short." | s3-6 |
| P Summary as its own file | declined: Chs. 1, 2 and 4 all keep `\section*{Summary}` at the end of their last section file; kept for consistency | — |
| P Summary l.180 | "Above about a keV" | s3-6 |
| P C opener "about 1.1 eV" | 1.17 eV | ch03.tex |
| P C redundancy (200)/(222) | 3.2 and 3.4 reduced to one clause each pointing to we:3-diamond/C.17 | s3-2, s3-4 |
| P C redundancy photon/absorbed DM | 3.2 shortened to a clause pointing to 3.3 | s3-2 |
| P C redundancy LDA 5.401 | kept in 3.4 as a pointer to 3.1 (acceptable per report) | — |
| P C HF gap picture | "as anticipated above" added | s3-4 |
| P C seam 3.3→3.4 | last clause of 3.3 trimmed | s3-3 |
| P C register tics (so/only/of order) | partly addressed in the rewritten sentences; no global substitution (would touch correct uses) | — |
| P C number style | "85 percent", "two percent", "about one percent", "15 to 20 percent", "ten percent", "one or two percent", "one percent … five", "a tenth of a percent" → \SI / \SIrange | s3-2 to s3-6, appE/E-7 |
| P D C.2 | as E7 | appC/C-2 |
| P D C.3 l.79 | "$\sim q_0/2$ (\cref{sec:1.3})" | appC/C-3 |
| P D C.5 | $f$-sum | appC/C-5 |
| P D C.6 l.83 | "This is Bloch's identity, proved in app:D.15; Mermin …" | appC/C-6 |
| P D C.8 l.44 | "The DLMF writes" | appC/C-8 |
| P D D.4 l.33 punctuation | display now ends the sentence ("canonical form,") | appD/D-4 |
| P D D.4 l.86 | sec:2.5 | appD/D-4 |
| P D D.5 l.82 HOMO/LUMO | defined in words at first use | appD/D-5 |
| P D D.5 l.89 | as P 3.4 l.82 | appD/D-5 |
| P E figure-tied sentences | all re-synced to the QE numbers (F) and to E4 | s3-3, s3-4, s3-6 |

## reader-a.md (persona a)
| item | fix | location |
|---|---|---|
| A 3.1 glide | as E1 | s3-1 |
| A 3.2 q = 377 eV | as E10 | s3-2 |
| A 3.2 e^{−E_g/2T} pointer | points to eq:3.3-ni | s3-2 |
| A 3.3 cross-site SO terms | one sentence (dV/dr concentrated near each nucleus) | s3-3 |
| A 3.3 m_dv recipe | (m_hh^{3/2} + m_lh^{3/2})^{2/3} with spherical averages m_e/(γ1 ∓ 2γ̄), γ̄ = (2γ2 + 3γ3)/5 (gives 0.50) | s3-3 |
| A 3.3 Kane 0.0718 | as D | s3-3 |
| A 3.3 semilocal, quasiparticle correction | defined at first use | s3-3 |
| A 3.3 1.11 vs 1.17 | as E2 | s3-1 |
| A 3.3 Fig. 3.6 mark |G200| − k_c | declined: no figure regeneration in this revision; the value 2.63 keV is in the text next to the figure | — |
| A 3.4 Δ_xc motivation | as E10 | s3-4, appD/D-5 |
| A 3.4 Gaussian-basis caption | obsolete: Fig. 3.8 is now a plane-wave QE calculation (F) | — |
| A 3.4 G0W0 a different calculation | stated in the text | s3-4 |
| A 3.4 norm-conserving/SG15 before 3.5 | pointer to sec:3.5 added | s3-4 |
| A 3.4 "LDA works because of the hole sum rule" pace | declined: D.4 shows the exchange-hole sum rule; one sentence suffices at this level | — |
| A 3.5 38 vs 76 keV | as E10 (2p, 2s, Ge 3d, Fig. 3.10) | s3-5 |
| A 3.5 pointer to 3.3 for fully relativistic potentials | → app:E.1 (where the Ge SOC calculation is described) | s3-5 |
| A 3.5 0.27 % | as D | s3-5 |
| A 3.5 Ry, bohr, scalar-relativistic | defined | s3-5 |
| A 3.6 "this test" | as E5 | s3-6 |
| A 3.6 0.840 vs 0.85 | as E4 | s3-4, s3-6 |
| A 3.6 Chern invariant | as E5 | s3-6 |
| A 3.6 eq:3.6-stationary to E.5 | declined: the equation is cited (MV Eq. 52) with one sentence on how codes use it; moving it would leave the false-minima remark without its object | — |
| A appendices C.2 duplicate; D.4 sec:4.2 | as E7; as D | appC/C-2; appD/D-4 |
| A caption names Troullier–Martins, single-projector, Dirac–Kohn–Sham | left: method names in captions, each attached to a cited or described calculation | — |
| A Berry connection, Löwdin, Foster–Boys | no change: the Berry connection is given by its formula at first use; Löwdin and Foster–Boys are names attached to a displayed construction | — |

## reader-b.md (personas b and c)
| item | fix | location |
|---|---|---|
| B 3.2/3.4 (200) contradiction; NFE "spherical" understatement | as E1 | s3-2, s3-4 |
| B 3.1 Fourier-convention friction | no change: book convention (A.3); 3.2 reconciles it in one clause | — |
| B 3.3 Fig. 3.6 E_dir label | resolved by the figure pass (Γ is now the smallest vertical gap, 2.56 eV) | s3-3 caption |
| B 3.3 m_dv, Kane, semilocal, quasiparticle | as A | s3-3 |
| B 3.3 Luttinger pace | kept (quoted with citation; limits stated) | — |
| B 3.5 0.27 % | as D | s3-5 |
| B 3.6 Wigner–Seitz, Chern, rank eight | as E10/E5 | s3-1, s3-6 |
| B WE 3-w1d 4.75 → 4.7 | as D | s3-6 |
| B D.4 sec:4.2 | as D | appD/D-4 |
| C 3.2/3.4 (200) | as E1 | — |
| C 3.3 Table mixes temperatures | as E3 | s3-3 |
| C 3.5 Vanderbilt attribution | as E8 | s3-5 |
| C 3.6 "must be real" | as E5 | s3-6 |
| C 3.6 orientation needs reason or cross-check | robustness sentence (F) plus the wannier90 examples and the plain statement (E5) | s3-6 |
| C 3.6 0.85 vs 0.840; rank eight | as E4, E10 | s3-6 |

## figures.md
| item | fix | location |
|---|---|---|
| F every number of Figs. 3.6–3.8 | checked against the captions and text after this revision (0.843, 0.557, 2.56, 2.70, 0.61, 3.17, 1.26/3.1 keV, 2.13, 1.9 eV, 0.95/0.193; Ge −0.05/+0.10/0.29; GaAs 0.51/1.00/1.46, 0.030; LDA 0.40 at 0.848, 0.77, 0.66–0.70) | s3-3, s3-4 |
| F flagged: s3-3 l.33/35 lattice constants | as E3 | s3-3 |
| F E_min at 2.57 keV (WE 3-mmin "every direction") | checked on qe_si_pbe.npz: 1.18 ([100]), 1.42 ([110]), 2.26 ([111]) eV, all below 3.4 eV; wording "well below 3.4 eV" | s3-3 we:3-mmin |
| F Wannier robustness / interpolation errors | text unchanged apart from E5 | s3-6 |

## Out of scope or left open
- App. E.3 E^QP → E_qp and the E.1 pointer (editor notes): E.3/E.1 are not in this brief's file list.
- fig3_6.py text-check block asserts the superseded 2.27 split; the tex now quotes the pair total 4.53 (derivation-confirmed). Update the
  assertion when the script is next run.
- V(r) → U_at(r) (eq:3.3-HSO) and V_l → U_l (eq:3.5-radial), unhatted ϱ in D.4/C.5: proposals only, for the notation batch.
