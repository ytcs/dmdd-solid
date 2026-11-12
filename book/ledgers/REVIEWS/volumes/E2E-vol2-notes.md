# Volume II end-to-end review: notes for the lead

## Block ch18-19 (+ appE D-43..45)
- ch22/s22-2.tex l.119, row "Sufficiency of the marks; \cref{sec:19.6-open}": the open problem now stands in sec:18.5-open; retarget and move the row up into the ch18 group (rows 107-110).
- ch32/E-25.tex l.29 repeats ch19/s19-6.tex l.181 (the two missing inputs of the collective-release model, U_rel with its rate spread, and b_br; dups list 0.27). ch19 is first in reading order; suggest E-25 point to sec:19.6-lee and keep only its specification.
- appB / NOTATION: no symbol removed in this pass. Bibliography: dinmohammadi2024daily is no longer cited in ch19 (check other chapters before pruning).
- Thread not fixed (outside block): ch20 opening quotes "up to about 55 eV stored in defects (sec:19.5)" - still valid (tab:19-bounds).
- Volume-level: Chap. 19 is long (sect. 19.5 alone ~6600 words) and carries the CDMS II/SuperCDMS calibration algebra in detail; if more pages are needed, sec:19.5-inversion and the germanium-threshold subsection are the candidates (both are reanalyses of specific measurements), but cutting them removes derived results (two-bias inversion, eq:19.5-linear, D.45 Cramer solution) that ch20/appF may cite; not done here.

## Block ch11 + D-31, D-32
- ch17/s17-5.tex:79–80: repeats s11-1 (acoustic edges 6.1/10.2/3.1 keV, light-mediator "44 times the higher edge", κ_η correction). Later side; suggest cutting to pointers to eq:11.1-edge, lim:11.1b.
- ch17/s17-5.tex:146: restates the Rayleigh floor eq:11.1-rayleigh; fine as an application, but the formula display can go (point to eq:11.1-rayleigh).
- ch08/s8-4.tex we:8-nucleon and ch11: the finite-q nucleon vertex now lives only in we:8-nucleon (s11-2 points to it).
- ch10/sec:10.10 and tab:10-nuisances: s11-9 now uses "theory uncertainties"/"uncertainty budget"; ch10 titles should match (labels unchanged).
- ch21/s21-4.tex:32 "The theory nuisances come from the tables …": wording ("nuisance parameters" are fine in 21.4, "theory nuisances" is not).
- Volume shape: sec:11.8-bar and sec:11.8-mass (finite-body acoustic modes, resonant-mass detectors) are absorption on macroscopic modes of the body, closer to the coherent-field material of sec:14.6 than to lattice excitations; consider moving them to Chap. 14 (not done: outside the block).
- s11-3 thermal diffuse subsection with lim:11.3b: negligible at detector temperatures (T² suppression 10⁻⁹); kept for completeness (it is the only treatment and closes the T>0 divergence), candidate for a further cut if pages are needed.

## Block ch12-13 + appE/D-33..D-37 (block reader)
- tex/ch30/E-18.tex:31: cites `tab:12-truncations`, removed (table of published Migdal formulas, dominated by fig:12-map and the Limit Checks). Fix: "reports the rate at each truncation of \cref{fig:12-map}".
- Dup pair ch12/s12-5.tex:46 / ch30/E-18.tex:16 (Sternheimer inverse moments, bound P_Mig <= E_R dM/(M Eg)): Chap. 12 is first and keeps it; E-18 should keep only the solver recipe and point to sec:12.5 / eq:12.5-bound.
- Dup pair ch13/s13-9.tex:13 / ch30/E-16.tex:17: later side in Vol III; E-16 should point to sec:13.9-edges for the off-axis optimum rather than restate it.
- Pre-existing (from ch13 log, not fixed): s13-4 defines 1+delta_LF against the head-only loss function; ch30/E-16.tex l.29 defines 1+delta_LF^(0) against |rho/eps_mac|^2. One definition should change.
- tex/ch13/s13-9.tex tab:13-window: the "Status" column ("two independent calculations", "one calculation") reads as audit record; lead may want it reduced to established/estimate/open (left as is).
- ch13 no longer cites kahn2022searches, hochberg2017absorption, miglio2020predominance; ch12 no longer cites the Liang/Berghaus detail equations it dropped (keys still cited elsewhere in the chapter). Nothing breaks; per-chapter bibliographies shrink.
- tex/xref/all.tex still lists tab:12-truncations until the next full build.

## Block ch14-15
- ch14/ch14.tex:2 and s14-1 (heavy-end paragraph): NiO magnon maximum "118 meV" (model, 118.2 in s7-1:182) vs "~117 meV" (measured) in ch07.tex:4, s7-1, s7-4 summary. Not a typo; suggest the opening say "about 117 meV (measured)" or state model value explicitly. Left.
- appB/B-1-vol2.tex: symbols of the deleted tables tab:14-inputs, tab:15-inputs need no change; check that nothing else points to those two labels (grep found only xref/all.tex).
- Structural proposal (item 6): s14-6 (coherent fields, exponential-bin likelihood, Neyman construction, lim:14.6b/c) is statistics of a detector record, not a magnetic excitation; it would sit better beside the statistical treatment of Sect. 21.4 (or sec:8.2-absorption for the regime), leaving in Ch. 14 only the Bloch-equation signal of the nuclear spins. Not moved (outside block).
- Structural proposal: s14-5 (chiral phonons, molecular magnets, multiferroics) is a set of detector concepts with mostly open responses (~4400 words); the lead could decide whether the multiferroic subsection (response "not known") earns its place.
- ch21/s21-4.tex cites tab:14-nuisances, tab:15-nuisances and sec:15.2-nuisance: labels kept; captions now read "Uncertainty budget of the ... rates", subsection "Corrections and uncertainties" — check the wording of the citing sentence.
- ch07/s7-1.tex:100: alias \label{app:D.19} still unused by this block (from earlier pass).

## Block ch16–ch17 + appE/D-42 (block reader)
- ch33/s22-1.tex:107 near-duplicates ch16/s16-9.tex:37 (theory-limited targets list; dups pair 18/0.42). Chap. 16 is first in reading order and keeps it; shorten the ch33 copy to a pointer to sec:16.9-limits.
- ch13/s13-9.tex:143 subsection title "Nuisance table of the phonon-assisted sector" (terminology rule): "Uncertainty budget of the phonon-assisted rate" (ch13 owner).
- ch16/s16-1.tex Sect. 16.1.2 (published Dirac construction, lim:16.1a, published numbers of we:16-factor, red/gray curves of fig16_1): kept as the record of the remote-band screening that moves ZrTe5 reaches by 5200–6400; lead may still decide to cut it to the key result eq:16.1-ratio (would need ch09/tab9-3 row lim:16.1a and fig16_1.py rerun).
- ch17/s17-2.tex Sect. 17.2.3 (counting against linear readout, eq:17.2-ratio, ~900 words) is readout physics; consider moving to the readout chapters of Part "Detection" (Chap. 20/21) and leaving a pointer in 17.2.
- ch17/s17-4.tex: Sect. 17.4 derives the Migdal–phonon-assisted cross term at length (eq:17.4-Mmig, eq:17.4-Sek) for an effect it finds 3 orders below the window uncertainties; structural reader/lead may want it condensed to the key results eq:17.4-lock, eq:17.4-rate and the electron-following cell.

## From block reader Chaps. 20-22 + appE/D-46, D-47
- ch33/s22-1.tex:17 caption of tab:22-calc: "the remaining calculation steps are in \cref{tab:22-gaps}". tab:22-gaps is now an index (gap, home section, class); the steps stand in the home sections. Suggest "...are stated in the sections indexed by \cref{tab:22-gaps}".
- appF/F-rows.tex: row of lim:20.1c (published Fano correction of Ramanathan and Ernst, Eqs. (A6)-(A7)) to remove; the box is gone.
- figscripts/ch20/map20.py / figures/ch20/map20.pdf: if the map draws a lim:20.1c tag, regenerate without it (caption already updated).
- ch21 (fig:21-kernel, fig:21-hib, we:21-debris, we:21-stream, lim:21.2a, we:21-combine) is built on the angle-averaged independent-particle crystal form factor table of Essig et al., which the ch10 pass removed as a dominated rate model (we:10-rate, lim:10.1a). I retargeted the references to sec:10.10-manybody, eq:10.1-fcrys and fig:10-fcrys. The worked numbers (1.60e5 /kg/yr at 10 MeV etc.) stay valid as the IP tabulation; lead to decide whether ch21 examples should be recomputed from the screened (RPA+LF) tables. That would be new numbers, so I did not do it.
- tab:21-dominant kept although it re-tabulates the channel budgets: ch33/s22-1.tex:75,107 cite it.
- ch20 chapcheck: 2 overfull hboxes > 5pt (not in text I touched).
- Dup pair ch20/s20-1.tex:142 vs ch32/E-25.tex:17 (vol3): ch20 is first in reading order and keeps it; the Vol III side should point back.

## From block ch09–ch10
- tex/ch10/s10-6.tex Sect. 10.6.5 (sec:10.6-fsum, ~600 words): relativistic shifts of the f-sum rule (orbit–orbit commutator derivation, eq:10.6-oo) for a −0.24/−0.76 % shift; a single-derivation section I left whole under the no-cut-of-unique-derivation rule. Lead may condense to the δ_mv and δ_oo results and the 0.8 % precision statement.
- tex/ch09/s9-2.tex l.14: overfull hbox 46 pt (pre-existing, Flat-onset paragraph).
- Any later removal of a Limit Check in Chaps. 10–17 (e.g. lim:16.1a, considered by the ch16–17 reader) needs a rerun of figscripts/ch09/fig9_3.py (1 s; regenerates tab9-3 and fig9_3) and the counts in s9-4 (two paragraphs) and s9-summary; the script prints all of them.
- tex/ch09: the atlas now lists 57 channels by section; a section removed elsewhere would leave a dangling \ref in tab:9-atlas (all resolve today).
- tex/figures/ch10/limit10_8b.pdf is no longer used (lim:10.8b removed); can be deleted with its script.
