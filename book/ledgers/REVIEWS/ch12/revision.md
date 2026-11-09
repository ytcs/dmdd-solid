# Ch12 revision log (2026-11-02/03)

Files changed: tex/ch12/ch12.tex, s12-1 … s12-6; tex/appD/D-33.tex, D-34.tex; tex/appF/F-rows.tex (Ch12 rows); tex/ch08/s8-6.tex (R15 only);
tex/ch05/s5-5.tex, tex/ch11/s11-2.tex, tex/appE/E-1.tex (R24 label only); tex/bib/book.bib (+macfarlane1957fine); NOTATION.md (rows + entry 81).
Scripts rerun (no QE): limit12_3b.py (rebuilt), fig12_2.py (ω_e axis), mom12_5.py (core 10.12 m_e), contact12_5.py (+radius, e^{-2λr}),
we12_3.py (+v_N p/ω_e). Logs: figscripts/ch12/*.log.

## Editor rulings
| Item | Status | How |
|---|---|---|
| R1′ (35 % = diagonal local fields; G≠G′ unsized) | done | 12.1 l.129 rewritten ("local fields enter twice"); 12.3 l.12 and off-diagonal paragraph (KKL "order one" vs Berghaus "small", unsized, pending full LF calc); 12.4 l.77 "unsized"; 12.5 l.67 (no 35 % on G≠G′); tab:12-nuisances row split in two (diagonal ×1.35 computed / G≠G′ named); 12.6 l.192; Summary. Coordinator's off-diagonal estimate block was not in editor-notes.md at finish, so "unsized" kept. |
| R2 (ω_e axis) | done | fig12_2.py replotted on ω_e = E_B + E_ej (measured core binding, atomic IE for valence; stated in script and caption); caption names "ω_e (electronic energy transfer)"; 12.2 text follows. |
| R3, R6, R7, R8, R11, R12, R14 | done | R7: 12.1 now gives 3.9e-5/eV (model) and 6.07e-5/eV (full, \cref{sec:12.3}); R11: 5.6 keV labelled point ion, 6.1 keV Z_ion; R14: 12.4 l.157 and 12.5 l.69 → \cref{tab:12-nuisances}; R6 bound curve kept (8.1e-6). |
| R5 (Ge exciton) | done, deviated | Macfarlane et al. 1957 (Phys. Rev. 108, 1377, DOI checked on Crossref) give 0.005 eV in their abstract, not 4.15 meV; no open source for 4.15 meV could be verified. Text: "about 5 meV \cite{macfarlane1957fine}". Editor may substitute 4.15 meV with a verified source. |
| R9/R17/R22 (12.3 bracket) | done | eq:12.3-bracket = b/[(ω_e−b+a)(ω_e+a)] with expansion; exact angle average 1 − 2p²/Mω + (9/5)v²p²/ω²; "no term in p/q". Removed 3p²/q², 16/16.5 MeV, 0.495, "soft limit fails first", "above 16 MeV". 12.3 opener, validity paragraph, l.115 rewritten. Lim 12.3b rebuilt (limit12_3b.py): x = m_χ 3 MeV–1 GeV, soft/exact rate (≤1.1e-3 to 150 MeV, 0.91 at 1 GeV), probability at E_R^max (10 % to ≈160 eV, 0.62 at 500 eV), leading-correction curve, bound curve, pole share (0.9 % at 500 eV, 3.7 % at 1 keV; pole = electronic stopping of the moving ion; pole cells left out of both rates). New finding: higher orders of the bracket double the (9/5) term near the gap (0.93/0.79/0.62 vs 0.96/0.90/0.85 at 100/300/500 eV). 12.1 l.87, D-33 l.64 (KKL Eq. (3) consistent only in soft limit), limit12_3b.py docstring and code, F rows l.328 and l.334–335 fixed. 12.4 l.41 states the result positively. 12.5 l.85 → factor 1.6 at 500 eV. |
| l.149 exponents | done | "This factor has the local exponents …" (derivation-1). |
| Berghaus Eq. (3.8) | done | 12.1 text and tab:12-truncations: full loss-function matrix in the formula, diagonal in the evaluation. |
| R10 | checked | No misattribution in Ch12/D-33/D-34; F row l.354 already cites 2603.13052. |
| R13 | no change | Confirmed by derivation-2; NOVELTY logged there. |
| R15 | done | s8-6 l.120 (re-read first; one exact Edit) and 12.1 l.138: below 1e-3 for E_R ≲ 16 eV; 3 % at 500 eV. |
| R18/R24 (GaAs a) | done | Source check: Table E.1 "measured" column is Csonka et al. Table II, measured values extrapolated to 0 K with zero-point anharmonic expansion removed, i.e. a static-lattice value, not measured at any temperature. Relabelled "static-lattice" in E-1 (column "static (expt.)" and caption), s5-5 caption, s11-2 l.184, s12-6 WE; 44.80 Å³ kept. Not in scope and not changed: ch06/s6-2 l.114 ("measured constants of we:5-lst … Ω = 44.80"); Ge 5.658 (12.6) vs 5.640/5.652 (flag for Ch5 owner). |
| R19 | done | Ge "about 30 % low"; ε̃ "symmetric" with Im = anti-Hermitian part; operator count removed; GPAW defined; tagged-recoil defined; displaced-oscillator numbers (1.0463, 1.0418, 63.4/65.5 meV, 0.188, 0.192, 0.056) all in we12_1.log and explained in the WE. |
| R20 | done | 12.2 l.110 and closing paragraph: crystal changes valence channel by >10× (47×, \cref{sec:12.3-atom}). |
| R21 | done | Both labelled: 1.63e-3 Cox (DHF), 1.73e-3 Ibe (local potential), both ionization-only (fig12_2.log); opener, Fig. 12.2, l.83, WE, Summary. |
| R23 | done | mom12_5.py uses its own core sum 10.12 m_e → δM/M 5.60e-4, E1 0.280 eV, off-site −14.7 m_e; radius sensitivity 0.10 %/0.53 %; Ge rigid core w/o 1s = 26; D.34: 2ZR/a0 = 1.8e-3/5.8e-3, dropping e^{−2λr} overstates by 0.14 %/0.43 % (contact12_5.log); non-log Dirac remainder (c_rel) and p₁/₂ contact density named in 12.5, D.34 and the nuisance row. |

## Derivation-1
| Item | Status |
|---|---|
| ZPE label (12.1 l.9) | done: "phonons and a recoil" |
| WE oscillator 0.188 / 0.056 | done |
| 12.2 "2 to 3 %" → about 2 % (log 1.5/2.2 %) | done |
| WE Ge 124 eV logic | done (ionization part 0.215 eV) |
| Si 2p 99.6 → 99.5 (centroid) | done (12.2, 12.5 WE) |
| NOTATION drift (6 clashes) | done: H_int→H_rel; s_κ(Q,ω)→s^inc_κ; 𝓕_L→𝓕_Mig; bold F→𝐅_e; D_q̂ kept + row; missing rows added (entry 81) |

## Derivation-2
| Item | Status |
|---|---|
| Doppler 5.1e-4 (12.4, table, F row) | done (limit12_4a.log) |
| 22.5 keV statement | done: stated as estimate from the logged 2.8 % above 10 keV |
| Ge cores 26.8 vs 26 | done |
| R_rel second form | done: c_rel(Zα)² non-logarithmic |
| Z*(1 eV) notation; 3.3² wording; force sign l.110; c_κ drift | done |
| Si valence share 0.43 % | kept; logged in figscripts/ch08/we8_4.log (4.32e-3) |

## Prose
E1–E4 done. Lint: 0 blocking in all files; genuine long sentences split (12.1 l.150, 12.3 l.149, 12.6 l.192/196, new 12.3 text). "Computational connection" heading removed. Count-teasers and narration (12.1 l.53/87/102/129, 12.2 l.3/104/112/145, 12.3 l.7/66/117/130, 12.4 l.5/81/92/102/154, 12.5 l.94/163, 12.6 l.7/55/98) fixed. Label tails cut; "the box" → \cref. Titles: 12.3 "The loss-function Migdal probability", 12.4 subsection "Zero-phonon, few-phonon and impulse regimes", 12.5 "Moments of the Migdal spectrum". Chapter opener folded to one orienting sentence. 12.6 opener varied. Kouvaris–Pradler Eq. numbers via \cite. s12-2 subsection labels added. Numbers in \SI. D-33 l.50 and D-34 opener shortened; D-33 binding correction unified with 12.4 (2.9e-3 with 44.7 meV). Not done (optional register calibration rewrites, Sect. 7 of prose.md).

## Readers
Reader-a: all lost points fixed (12.1 count, oscillator, drag-mass forward pointer; 12.3 contradiction, N_T/Ω/p_N, F wording; 12.4 fragment, frame open; 12.5 rounding, 30 %, O((Zα)²), "valence", chain pointer; 12.6 Ω label, atomic-unit conversion; D.33 HT sentence). Not changed: F_cr compression (12.5), 0.9(ω/eV)² bound reasoning (12.6, lives in App. E.17).
Reader-b/c: L1–L3 fixed; GPAW, tagged recoil, eq:12.2-rate unit, v_max explicit, Hermitian→symmetric, operator count, D.33 vs 12.4 binding estimate reconciled. Not changed: one-clause solid-state reminders in 12.3 (terms defined in Chaps. 3–10), μ⁴ scaling derivation.

## Build and checks
latexmk -pdf -outdir=/tmp/build-ch12rev main.tex (after the last edit): 0 LaTeX errors, 0 undefined citations, 0 undefined references to Ch12/D.33/D.34/tab:E labels (remaining undefined references are unwritten chapters/appendices). The ch11/s11-7 "\n\n" break reported by the 12.5 writer is no longer present.
Lint (BANNED-TERMS): 0 blocking in all nine files. check_notation.py (ch12, D.33, D.34): 2 gaps, both S^ad_{κ;GG′}, whose row exists but whose key the checker splits at ";".
fig12_1.py: top-panel label s → s^inc_κ, rerun, log identical.
