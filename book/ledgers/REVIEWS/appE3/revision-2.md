# App. E second pass, part 2: revision of E.21–E.27

Brief: briefs/reviews/appE3-revise-2.md. Inputs: consistency-2.md (all items), ../appCE/prose.md (E.21–E.27 items), editor-notes.md (rulings E1–E6). Files edited: tex/appE/E-21.tex … E-27.tex, NOTATION.md (one row, clash entry 99). New: figscripts/appE/appE3_rev2_numbers.py and its .log (every number recomputed here). Not committed. E.1, E.15, E.16 and tex/ch08/s8-4.tex belong to the parallel reviser and were not touched.

## consistency-2, summary table

| # | item | status | how |
|---|---|---|---|
| 1 | E-24 F "two standard deviations"; ε "to 1 %" | done | opening: model reproduces ε_eh exactly because its constant is fitted; F = 0.114 lies 2.4σ below 0.119 ± 0.002 (s18-4, tab:18-pairs) |
| 2 | E-24 DFT 3.10 eV "15 %" | done | 14 % (log: 13.9 %); cite [Sect. III] and "time-dependent density-functional loss function" as s18-4 |
| 3 | E-24 A_AB = 5.2, R–K plane | done | A_AB = 5.703 eV³, ΔA = 1.43 eV³, slope 0.076 eV⁻² of s18-4 → 0.11 eV, 2.9 % (log) |
| 4 | E-24 plasmon 16.6 eV | done | loss peak 16.4 eV (sec:4.4) |
| 5 | E-25 ε₀ = 11.7, n_s 6.5–12.9e4 | done | ε₀ = 11.4 (sec:7.4, as s20-1), 𝓃_sh = 6.3 to 12.6e4 cm⁻² (log); Ch20 symbols 𝓃_sh, ξ_SC, p_tr |
| 6 | E-25 "about 4e4 V/cm" | done | E_x^b/(e a_x) = 3.5e4 V/cm (sec:18.5; log) |
| 7 | E-25 verdicts in sec:20.5 | done | "the readout verdicts collected in the Summary of \cref{chap:20}" (the Summary has no label); the closing paragraph that repeated the pointer is cut |
| 8 | E-26 defect "open" | done | states the Ch10 bound: ≥ 1/r, 1.7 for Xe 1s at 56.5 keV, transverse current only raises it, only the (Zα)² part has unknown sign; the calculation fixes the size |
| 9 | E-26 (Zα)² 0.16 vs Ch10/22 0.13 | done in E-26; **chapter fix queued** | E-26 prints (54/137.04)² = 0.155 (log). Ch10.9 l.176 and l.232 and Ch22 (s22-2 l.56) print 0.13 and should read 0.155 (editor notes: queued as a chapter fix; not edited here) |
| 10 | E-26 expansion | done | 1 − 2(m_χ² − 2m_χω)/m_med² + … (s10-9 l.178) |
| 11 | E-26 Cu shift "estimated" | done | −1.97e-2 (Cu), −2.2e-4 (Si) in d ln a/d ln α only; nuclear-mass term −1.12e-3 (Cu), −0.86e-3 (Si), entering through m_e; pasteka2019material Table II, as s11-8 l.186; acceptance = reproduce these |
| 12 | E-21 "falls as p⁻¹⁰"; "several hundred" | done | amplitude ∝ \|p − q\|⁻⁵, square ∝ \|p − q\|⁻¹⁰; "reaches up to 740 at 10 eV" |
| 13 | E-21 "Sommerfeld factor" | done | "Fermi factor of an unscreened point charge, eq:2.2-fermi" (both uses) |
| 14 | E-23 Qb@ll clause | done | "the real-space codes Octopus and SALMON or the plane-wave code Qb@ll"; grid clause adds "(or the equivalent plane-wave cutoff)" |
| 15 | E-23 "about 0.3 eV" | done | quantum–classical boundary 0.41 eV (sec:19.1), E_d 12.5–36 eV by direction |
| 16 | E.15 l.56 | not mine | outside E.21–E.27; parallel reviser (ruling E1) |
| 17 | E.1 l.147 | not mine | outside E.21–E.27; parallel reviser (ruling E1) |

## consistency-2, GAPs

| gap | status | how |
|---|---|---|
| G1 E-24 Ge route | done | Ge bands enter only after the app:E.14 check (L below Γ, both gaps to 0.1 eV, m*_⊥ at L, m_Γ); PBE, HSE06+SOC and the 4s-shift correction named as failing (as E.14 states); G₀W₀ with SOC on a PBE or hybrid ground state named as the next route under the same check, no verdict (ruling E1). Table row says "Ge after the E.14 check" |
| G2 E-24 GaAs ε∞ | done | ionic part from measured ε∞ and the measured LO–TO splitting, Z*/ε∞ = 0.194 (sec:5.5, sec:11.9); "a semilocal ε∞ of GaAs is not a safe input". Note: consistency-2 wrote Z*²/ε∞ = 0.194; s11-9 l.100 says Z*/ε∞ = 0.194, which the text follows |
| G3 E-24 tail law, reader | done | lattice Gaussian sampled at the integers (unit bins add 1/12), Edgeworth terms beyond the table; absolute pointwise error C/x, relative skewness x^(−1/2), C ≈ 0.24 for Si → 1.2e-2 at 20E_g (REF-DC-67 §8 items 1–3; log); reader returns δ_{N1} below θ_iiE_g, interpolates from the threshold up, row at the jump (DC-67 failure mode, stated as a requirement, no DC number quoted) |
| G4 E-24 Richardson order | done | h^{3/2}: f(h/2) + [f(h/2) − f(h)]/(2^{3/2} − 1) (app:D.43) |
| G5 E-24 marks | done | new paragraph: the tables carry the marks 𝔪 of eq:18.3-obs (phonon spectrum, electron and hole counts, carrier positions, stored energy) and how each is obtained; table row "library, marks" |
| G6 E-24 pair separations | done | the Si cascade records end-of-cascade carrier energies and pair separations (compared with r_ℰ in sec:18.5); capture probability f(x) averaged over that distribution; table row updated |
| G7 E-21 3.60 keV, thresholds, 𝒰 | done | 0.685, 3.60, 3.88 keV (opposite) and 2.33, 2.74 keV; lightest masses 130 and 441 keV (sec:16.5); 𝒰_{j'j}(G) named as an output from the same Bloch functions and grid; table row |
| G8 E-21 R̃²ᴰ, r₀, tube excitons | done | R̃²ᴰ and r₀ reported as inputs with their definition (sec:16.2); new paragraph: ladder (BSE) step for semiconducting tubes on the projected bands, acceptance (10 meV under doubling; measured optical transition of the same tube), cost 10²–10³ core-h; new table row |
| G9 E-23 HSE arm in Ge | done | hybrid arm serves Si only; in Ge HSE06 at 0.25 fails the E.14 check, so the Ge spread rests on surface hopping and Landau–Zener until a functional passes (ruling E1); table "HSE (Si only)" |
| G10 E-22 Born-limit acceptance | done | 0.28/0.44 labelled the Born reading; beyond Born 0.19 at K_b = 0.07 and a 32 % stronger contact potential (sec:16.8); computed α_ohm compared through the rate with the measured damping, not with 0.28; table updated |
| G11 E-25 interface | done | measured 0 K Al constants primary (Voigt 6.63/3.30 km/s, 2.70 g/cm³, sec:20.3); finite-strain DFT only without a measurement (W films); isotropic limit must return 0.368 / 0.282; anisotropic result compared with the 0.327–0.405 sensitivity of sec:20.3 |
| G12 E-26 axioelectric caveats | done | singlet/triplet, spin–orbit and the factor ¾ (sec:10.8), sec:15.4-spin conditions; tests accept the pair tensor and moments, not the row |
| minor E-21 l.18 thresholds | done | with G7 |
| minor E-23 l.21 "ten to thirty" | done | 17 to 19 times the 6.8–7.5 eV of a close Frenkel pair (sec:19.1; log) |
| minor E-24 opening, full-band reference | done | 4.15 eV, envelope [3.95, 4.73] eV, ≥ ±0.4 eV class systematic, 0.6 eV unexplained against 3.50 eV (s18-4) |
| minor E-25 Y_qp target | done | 0.590 with maximum 0.600 at 5.46Δ (sec:20.4) inside 0.57–0.6; guruswamy cited [p. 2] as Ch20; table updated |

## Prose review (appCE/prose.md), E.21–E.27

| location | status | how |
|---|---|---|
| Recipe template (rate ≤ 1.5 per 1000 words) | done | slot openers (quantity/method/acceptance/convergence/cost/result-enters/On 𝔗) now: E.21 2 in 3.0k words (0.7), E.22 1 (0.3), E.23 2 (0.7), E.24 3 (0.8), E.25 2 (0.5), E.26 1 (0.6), E.27 0. E.21 specification paragraphs rewritten as prose (ruling E5) |
| Count-teasers | done | E.22 l.13, E.23 l.37 (now "Three errors must be avoided: …", correct count), E.24 l.15, 19, 57, E.25 l.9 (four additions listed, exciton module separate), l.43, l.67 ("four … fourth" removed), E.26 l.9, E.27 l.52 (the even–even zero is a correct zero, now separate), E.23 opening "Six … Three … Three", E.24 "two cascades, two tests …" |
| Post-table recaps | done | cut in E.22, E.23 (table pointer moved into the opening), E.24 (run order moved into the wide-gap paragraph), E.25, E.26, E.27 |
| Table conventions | done | lower-case headers; labels tab:E22-summary, tab:E23-summary, tab:E24-summary, tab:E25-runs (no external references existed) |
| Units outside \SI | done | E.24 l.21 (\SI each value), E.25 l.51 (\SIlist) |
| Truncation-label phrasing | done | first mention "On the truncation label 𝔗 (\cref{sec:8.5})", later folded into the method sentences |
| E.21 l.14 "it" | done | "if it changes more, a 1728-atom PBE cell is added as a third size" |
| E.21 l.28 subject switch | done | "The Frenkel code takes … , Fourier transforms them, builds …, and diagonalizes …" |
| E.21 l.32 dangling r_t, a_s | done | attached at first use |
| E.21 l.51 STE | done | "self-trapped-exciton and F–H pair energies" |
| E.21 l.22 to-do note | done | "gives the corrected curves; it takes minutes" |
| E.22 l.40 climbing-image elastic band | done | "climbing-image nudged elastic band" |
| E.22 l.85 cliché | done | cut |
| E.23 l.76 looped close | done | cut |
| E.24 l.13 Ge sentence | done | prose-review wording |
| E.24 l.21 section named twice | done | "replace the estimates of \cref{sec:18.4}" |
| E.25 l.3 | done | "these numbers"/"wait on them" replaced; "chains the steps" |
| E.25 l.11, l.31 tense | done | "must both be reproduced"; "one has to be trained" |
| E.25 l.17 ε₀ clash | done | one ε₀ (NOTATION row ε₀, value 11.4); vacuum permittivity named in words. ε_s was not introduced: NOTATION has ε₀ for this meaning and a second symbol would break one symbol, one meaning (entry 99(c)) |
| E.25 l.49 negation framing | done | "Soft surface spectra are measured: …" |
| E.26 l.19 title | done | "Pair, Compton and Barkas responses" (the suggested longer title fails the lint title check) |
| E.26 l.9 vague hedge | done | the Ch11 values with citation (item 11) |
| E.26 l.21 "the source", "It" | done | "Bauer et al. take …~\cite{bauer2026dark}"; "The Barkas table is new code …" |
| E.26 l.17 circular | done | "Computing … fixes the size of the defect" |
| E.27 l.30 third symbol set | done | C.12 symbols 𝗄_i, Ξ, 𝖿, λ_i throughout; translation sentence deleted (ruling E6; NOTATION entry 99) |
| E.27 l.46 Gordon et al. | done | name dropped; spectrum attributed through \cite{saldanha2020cosmogenic}, whose inputs it is (no bib entry for Gordon et al. exists) |
| E.27 l.26 low content | done | "each needs one computation, specified below" |
| E.27 l.40 | done | "is imposed in the galactic frame"; "the leakage-corrected bound of \cref{sec:21.2-leak}" |
| E.27 survivors | done | first use "every target retained in \cref{sec:21.7} (the survivors)" |

## Rulings
- E1: E.23 (HSE arm) and E.24 (G₀W₀) use "germanium bands that pass the check of app:E.14"; GW named as the next route, no GW result quoted.
- E3: all E.21–E.26 numbers listed there applied; recomputed numbers in figscripts/appE/appE3_rev2_numbers.log.
- E4: E.21 (3.60 keV, 𝒰, R̃²ᴰ/r₀, tube excitons), E.22 (Born-limit acceptance), E.24 (marks, pair separations), E.26 (axioelectric caveats) kept.
- E5: E.21 rewritten as prose; template, count sentences, recaps and mixed headers removed in E.21–E.27; E.25 ε₀, E.21 STE and l.28 fixed; E.27 citation handled.
- E6: E.27 dual weights are C.12's λ_i; NOTATION entry 99 records the retirement of 𝔎_i, F, 𝔥, ξ_i, μ_i and the new λ_dec row (rows for 𝔎_i, 𝔥, ξ_i are no longer needed since the symbols are gone).

## Chapter fixes found (not edited)
1. Xenon (Zα)²: Ch10.9 (s10-9 l.176, l.232) and Ch22 (s22-2 l.56) print 0.13; (54/137.04)² = 0.155. E-26 prints 0.155.
2. consistency-2 "outside scope": s16-8 l.51 figure caption uses c_TA = 3.40 km/s and 2.73 g/cm³ for aluminum "(sec:15.4)", not the 0 K Voigt set (3.30 km/s, 2.70 g/cm³) of Ch20.

## Checks
- lint.py --banned BANNED-TERMS.txt on E-21 … E-27: 0 blocking (LONG-SENT warnings only, about a third from headings and captions joined to the next sentence).
- check_notation.py --files 'appE/E-2[1-7].tex': no new gap from this revision (λ_dec now has a row); 20 pre-existing gaps listed in entry 99(e) for the App. E ledger merge.
- Build: latexmk -pdf -outdir=/tmp/claude-0/build-appE3-2 main.tex (result in the final report).
- Table widths (coordinator follow-up): the four tables in E.22–E.25 each had their fixed column widths cut from 0.92 to 0.88 of the line width, and the E.23 kernel row was reworded so it can break. Rebuilt: 0 errors and no overfull boxes in E.21–E.27.
