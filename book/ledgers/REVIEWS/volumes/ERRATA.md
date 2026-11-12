# Errata harvest (stage 1 of briefs/volumes/ERRATA.md)

Harvested 2026-11-12 from every file in book/ledgers/REVIEWS/volumes/ (unit logs ch*.md and appA-appC.md; E2E-vol1/2/3.md; E2E-vol1/2/3-notes.md; E2E-vol1/2/3-structure.md; the dups and undefined-label lists were read but hold only layout and label items; there is no notation.md) and from the lead's list scratchpad/followups.md (cited below as "followups l.N").

Locations are the current tree (HEAD dab4d82 plus the uncommitted edits of the structure editors at harvest time), found by grep on the quoted text or label, not taken from the logs. Line numbers will drift while the structure editors work: the quoted text is the anchor, the line number is a hint. Quotes are copied from the tex (LaTeX source, shortened with "..." only at the ends or where marked).

"Self" in the Reported-by line marks an item I noticed while checking locations; it was not in any log.

Categories: VALUE, DERIVATION, CITATION, DEFINITION, TEXT (definitions in the brief). Pure layout, wording, terminology, label retargets and structure items are excluded; the list at the end names the reported items that were excluded or that the current text already resolves, so that the proposal stage does not reopen them.

Counts: VALUE 13, DERIVATION 3, DEFINITION 5, CITATION 2, TEXT 5; 28 entries.

---

## VALUE

### ER-1 (VALUE) Alig–Bloom constant, model Fano factor and its distance from the measurement: two calibrations
- ch29/E-13.tex:69 (sec. "The single-parameter model", next to eq:E.13-ab at :67): "The original model takes $A_{\mathrm{AB}} = 5.2$, in the units of the source (quoted there as eV$^2$, with which the ratio in \cref{eq:E.13-ab} carries a leftover eV$^{-1}$), chosen to reproduce the measured pair energy at high energy. ... The cascade of \cref{sec:18.4} fixes it instead by the measured pair energy at \SI{123}{K} in its own solution of the model, $A_{\mathrm{AB}} = \SI{5.703}{eV^3}$ (\cref{eq:18.4-AAB})."
- ch29/E-13.tex:71: "With $A_{\mathrm{AB}} = \SI{5.703}{eV^3}$ tuned to the first, the model predicts $F_{\mathrm{eh}} = 0.114$, $2.4\sigma$ low (\cref{sec:18.4})."
- ch29/E-13.tex:92 (caption of tab:E-cascade-si): "The ionization probabilities follow from \cref{eq:E.13-ab} with $A_{\mathrm{AB}} = 5.2$~\cite{ramanathan2020ionization}, the model Fano factor from the calibration $A_{\mathrm{AB}} = \SI{5.703}{eV^3}$ of \cref{sec:18.4}"
- ch18/s18-4.tex:11–14 (eq:18.4-AAB): "$A_{\mathrm{AB}} = \SI{5.703}{eV^3}$ ... The value lies \SI{10}{\percent} above the 5.2 that Alig and coworkers fitted to the pair energy of silicon~\cite[Sect.~II]{nielsen2026first}."
- ch18/s18-4.tex:31, :41; ch18/s18-summary.tex:9, :30; ch18/s18-2.tex:37; ch18/s18-1.tex:122; appB/B-1-vol2.tex:488 and appB/B-1.tex:1239: 5.703 eV^3, F_eh = 0.114, 2.4σ.
- Before the Vol III E2E pass E-13 had "A_AB = 5.2, eps = 3.71 eV, F = 0.115, two standard deviations low"; the E2E reader removed the 3.71/0.115 Ramanathan–Kurinsky planes and made E-13 name the calibration, "No number changed" (E2E-vol3.md, block ch27–ch30).
- Reported by: ch18 unit editor (ch18.md, "PRE-EXISTING inconsistency"); ch29-32 unit editor (ch29-32.md items 1, 1); followups l.23 (PRE-EXISTING), l.82; E2E Vol III block reader ch27–ch30 (E2E-vol3.md).
- Open for the proposer: whether the two-calibration wording now in E-13 is correct (5.2 "in the units of the source" against 5.703 eV^3, the "10 %" of s18-4:14 with 5.703/5.2 = 1.097, the attribution of 5.2 to Alig et al. via nielsen2026first in s18-4 against ramanathan2020ionization in E-13), and whether any 0.115 / "two standard deviations" survives anywhere (grep found none at harvest).

### ER-2 (VALUE) Plasmon energy of silicon: 16.6 eV against 16.4 eV
- ch29/E-13.tex:36: "In silicon the plasmon is at \SI{16.6}{eV}~\cite[Table~I]{ramanathan2020ionization}"
- ch29/E-13.tex:100 (tab:E-cascade-si): "Plasmon energy; hole band width & \SI{16.6}{eV}; \SI{12}{eV}~\cite{ramanathan2020ionization}"
- ch32/E-24.tex:9: "$\Imag\varepsilon^{-1}$ at the plasmon, whose loss peak lies at \SI{16.4}{eV} in silicon (\cref{sec:4.4})"
- Vol I separates the two: ch04/s4-3.tex:89 "For the valence density of silicon, ... $\omega_p = \SI{16.6}{eV}$" (free-electron plasma frequency); ch04/s4-4.tex:94 "The loss function peaks there, at \SI{16.4}{eV}"; ch04/s4-5.tex:3 "the plasma frequency, $\omega_p = \SI{16.6}{eV}$, and the measured loss peak of silicon ... sits at \SI{16.4}{eV}". ch27/E-6.tex:3 and :81 use 16.6 eV as ω_p.
- Reported by: ch29-32 unit editor (ch29-32.md, items 2 and 1); followups l.23; E2E Vol III block reader ch27–ch30 (E2E-vol3-notes.md).
- Probably two quantities (rule: say which is which). E-13 calls 16.6 eV "the plasmon"; the proposer should check what Ramanathan–Kurinsky Table I tabulates.

### ER-3 (VALUE) SG15 silicon p-channel core radius: 1.89 Å against 3.56 bohr = 1.88 Å
- ch24/s3-5.tex:37: "with $r_c = \SI{1.27}{\angstrom}$ for $s$ and \SI{1.89}{\angstrom} for $p$"
- ch24/s3-5.tex:44 (caption of fig:3-psae, label :45): "generated for this figure at the core radii of the SG15 potential of the plane-wave calculations, 1.27 and \SI{1.89}{\angstrom} for $s$ and $p$, to within \SI{0.02}{\angstrom}"
- ch24/E-2.tex:31: "s and p channels with $r_c = 2.40$ and $3.56$ bohr (\SI{1.27}{\angstrom} and \SI{1.88}{\angstrom})"
- 3.56 bohr = 1.8839 Å; 2.40 bohr = 1.270 Å. Same source (schlipf2015optimization).
- Reported by: ch23-25 unit editor (ch23-25.md items 4, 4); E2E Vol III block reader ch23–ch26 (E2E-vol3-notes.md); followups l.69.
- Script: the figure potential of fig:3-psae (book/figscripts/ch03/, ld1 inputs) states its radii; check which radius it used.

### ER-4 (VALUE) LDA lattice constant of silicon: 5.401 Å against 5.403 Å
- ch03/s3-4.tex:56: "In the local-density approximation, introduced next, the computed lattice constant of silicon is \SI{5.401}{\angstrom}, \SI{0.5}{\percent} below the measured one (\cref{sec:3.1})." (no citation)
- ch03/s3-1.tex:49: "For silicon in the local-density approximation the minimum lies at \SI{5.401}{\angstrom}, \SI{0.5}{\percent} below the measured value~\cite[Sect.~10.2]{ponce2016epw}."
- ch05/s5-1.tex:54: "yields \SI{5.401}{\angstrom} in the local-density approximation and \SI{5.477}{\angstrom} with the PBE functional"
- ch23/E-1.tex:30 (tab:E-functionals, LDA and PBE from csonka2009assessing): "Si   & 5.403 & 5.466 & ..."
- Related, same table: the book's own PBE relaxation 5.477 Å (s3-4:66, s5-1:54, E-1:136, "in line with the PBE row of that table") against the tabulated PBE 5.466 Å.
- Reported by: ch23-25 unit editor (ch23-25.md items 5, 4); E2E Vol III block reader ch23–ch26 (E2E-vol3-notes.md); followups l.69. The s3-1 and s5-1 locations were found at harvest (Self).
- Likely two sources (EPW tutorial vs Csonka et al.); rule: say which is which.

### ER-5 (VALUE) PBE Kohn–Sham gap of silicon quoted as 0.602 eV without its setting
- ch04/s4-7.tex:121: "A PBE calculation of silicon puts the indirect gap at \SI{0.602}{eV}, against the measured \SI{1.17}{eV} at low temperature"
- ch04/s4-9.tex:166 (Chap. 4 Summary): "The quasiparticle correction to Kohn--Sham energies repairs the gap, \SI{0.602}{eV} with PBE against the measured \SI{1.17}{eV} in silicon."
- ch03/s3-3.tex:29 (caption of fig:3-si-bands, $a = \SI{5.431}{\angstrom}$): "the indirect gap $\Eg$ at \SI{0.557}{eV} (measured \SI{1.17}{eV})"
- ch03/s3-4.tex:66: "a gap of \SI{0.557}{eV}, half the measured value (\cref{fig:3-si-bands}). Minimized in its total energy, the lattice constant comes out at \SI{5.477}{\angstrom}, \SI{0.85}{\percent} above the measured one, where the gap is \SI{0.602}{eV}."
- ch03/s3-4.tex:84: "LDA puts the silicon gap at \SI{0.52}{eV}, PBE at 0.56 to \SI{0.60}{eV}"; ch23/E-1.tex:136 (we:E-si-bands): 0.602 eV at the relaxed 5.477 Å, 0.557 eV at the measured lattice constant; ch25/s3-6.tex:147: "its gap, \SI{0.557}{eV}"; ch27/E-7.tex:110: "about \SI{0.6}{eV} in the representative PBE calculation (\cref{we:E-si-bands})".
- Reported by: E2E Vol I block reader ch03–ch04 (E2E-vol1.md "Left for the lead"); followups l.125 (PRE-EXISTING).
- Two settings, both right; s3-4:66 and E-1:136 now state both. Open: s4-7:121 and s4-9:166 give 0.602 eV with no lattice constant.

### ER-6 (VALUE) LDA gap of silicon: 0.52 eV against 0.51 eV
- ch23/E-3.tex:48 (tab:E-gw, from aryasetiawan1998gw): "Si & 0.52 & 1.24--1.29 & 1.17 & ..."; used in ch03/s3-4.tex:84, :89, :140, :150 (we:3-mmin-gap, $m_{\min}$ with 0.52 eV).
- ch23/E-1.tex:30 (tab:E-functionals, lucero2012improved, gap at the LDA relaxed lattice constant): "Si   & 5.403 & ... & 0.51 & 1.22 & 1.17"
- Reported by: E2E Vol III block reader ch23–ch26 (E2E-vol3-notes.md: "Two sources, both cited; no change").
- Listed because the reader recorded it; expected outcome "no change" or one clause saying the two values are at different lattice constants/sources.

### ER-7 (VALUE) Optical-phonon energy of silicon: 60 meV against 64 meV
- ch01/s1-5.tex:57 (tab:1-quanta, label :50): "Heat & athermal phonon & \SI{60}{meV} optical at creation, a few meV after decay, in Si"
- ch01/s1-5.tex:40: "The phonons first created in silicon are optical phonons of about \SI{64}{meV}"
- ch01/s1-3.tex:125: "the optical phonon of silicon at the zone center has \SI{64}{meV}, or \SI{15.5}{THz}~\cite{nilsson1972study}"; ch01/s1-3.tex:91 (caption of fig:1-kinematics): "the optical-phonon energy at the zone center, \SI{64}{meV} (green)"
- ch01/s1-3.tex:140 (lim:1.3a, :135): "$\omega_0 = \SI{60}{meV}$, a typical silicon phonon energy" (a model choice, per the reporter).
- Reported by: E2E Vol I block reader ch01–ch02 (E2E-vol1.md "Possible inconsistency left"); followups l.120 (PRE-EXISTING).
- Script: book/figscripts/ch01/ (fig1_3.py or the kinematics figure; limit box script) for the 60 meV of lim:1.3a.

### ER-8 (VALUE) NiO magnon maximum: 118 meV (model) against ~117 meV (measured)
- ch14/ch14.tex:2: "a magnon, costs anywhere from a few meV to \SI{118}{meV} (\cref{sec:7.1})"
- ch14/s14-1.tex:110: "the magnon energies, at most \SI{118}{meV}, are negligible against $qv$"
- ch07/s7-1.tex:182: "$\omega^{\mathrm{M}}_{\mathrm{max}} = |\vect{S}|(6J_2 - 3J_1) = \SI{118.2}{meV}$, against $6J_2|\vect{S}| = \SI{114.1}{meV}$ for $J_2$ alone and a measured maximum of ${\sim}\SI{117}{meV}$"; also s7-1.tex:167 (caption, 118.2 meV off the plotted lines)
- ch07/ch07.tex:4: "a magnon, can take up anything from a few meV to \SI{117}{meV}"; ch07/s7-1.tex:3 "energies up to ${\sim}\SI{117}{meV}$"; ch07/s7-4.tex:153 (Summary) "a maximum of ${\sim}\SI{117}{meV}$"
- Reported by: E2E Vol II block reader ch14–ch15 (E2E-vol2-notes.md); followups l.127 (PRE-EXISTING / errata, "two settings").
- Two settings; rule: say which is which in ch14.tex:2 and s14-1:110.
- Script: book/figscripts/ch07/fig7_1.py (dispersion), book/figscripts/ch14/magnon14.py.

### ER-9 (VALUE) Silicon displacement threshold in the Stillinger–Weber potential: 17.5 eV against 18 eV
- ch28/E-10.tex:3: "In the Stillinger--Weber potential, displacing a silicon atom from its site takes between 17.5 and \SI{63.5}{eV}, depending on the direction in which it is struck~\cite{kadribasic2018directional}."
- ch29/E-11.tex:76: "With the Stillinger--Weber potential the minimum threshold over all directions is \SI{18}{eV} in silicon and \SI{13}{eV} in germanium" (sassi2022energy; also tab:E-md-si, label E-11.tex:111)
- The density-functional value 12.5 eV along ⟨111⟩: ch07/s7-4.tex:159, ch19/s19-1.tex:33.
- Reported by: E2E Vol III block reader ch27–ch30 (E2E-vol3-notes.md: "Two sources, consistent within rounding").
- Expected outcome: say the two are different sources or roundings; no number change unless the sources disagree.

### ER-10 (VALUE) Numbers of fig:12-plane recomputed during the edit
- ch12/s12-1.tex:71 (text of fig:12-plane, figure at :75, label :77): "The Migdal weight, $P_{\mathrm{Mig}} = 2.93\times10^{-6}$, or $6.1\times10^{-5}$ per eV of recoil energy (\cref{sec:12.3}), sits at $\omega_e$ above the gap: half of it below \SI{4.4}{eV}, \SI{89}{\percent} below \SI{10}{eV}, with a mean of \SI{5.9}{eV}. ... holds \SI{21}{\percent} of it ... The mean lattice energy of a Migdal event is \SI{48.5}{meV} ... $\langle p^2\rangle^{1/2} = \SI{6.1}{keV}$."
- Before: the figure was computed with a point ion of charge 4 while the text gave both $3.9\times10^{-5}$ and $6.07\times10^{-5}$ per eV (ch12.md, Cross-unit item 4). The ch12 editor then regenerated fig12_1.pdf with Z_ion(p) and updated the text numbers from the script output (followups l.98: "numbers changed by recomputation of a dominated input"; l.29).
- Consistency at harvest (Self): E_R = (50 keV)^2/(2×26.16 GeV) = 0.0478 eV and 2.93e-6/0.0478 = 6.13e-5, consistent with "6.1e-5 per eV" and with "6.07e-5 per eV" of sec:12.3 (ch12/s12-4.tex:136).
- Reported by: ch12 unit editor (ch12.md); followups l.29 (pre-existing; report), l.98.
- Script: book/figscripts/ch12/fig12_1.py. Its docstring names a log fig12_1.log, which is not on disk (Self): rerun and compare every number of the paragraph.

### ER-11 (VALUE) Chap. 21 worked examples rest on the independent-particle crystal form-factor rate that Chap. 10 no longer uses as a rate model
- ch21/s21-1.tex:3: "The independent-particle silicon rate of \cref{sec:10.10-manybody}, \num{1.60e5} events per kilogram and year at \SI{10}{MeV} for $\sigmae = \SI{e-37}{cm^2}$, rests on one velocity distribution"
- ch21/s21-1.tex:54, :76, :80 ("built from the tabulated form factor of \cref{fig:10-fcrys}"; "by Essig et al. (gap set to \SI{1.11}{eV}, first energy \SI{1.2}{eV}; \cref{fig:10-fcrys})"); ch21/s21-2.tex:33, :53 ("Step columns from the angle-averaged crystal form factor of Essig et al.").
- Against ch10/s10-2.tex:38: "the form-factor table of \cref{sec:10.1}, which gives $1.60\times10^5$ ..., $8.6\times10^4$ in the random-phase approximation without local fields and $5.9\times10^4$ with them"; ch10/s10-10.tex:87.
- Affected per the reporter: fig:21-kernel, fig:21-hib, we:21-debris, we:21-stream, lim:21.2a, we:21-combine.
- Reported by: E2E Vol II block reader ch20–ch22 (E2E-vol2-notes.md); followups l.132 ("ERRATA/CONSISTENCY item ... recompute with the screened (RPA+LF loss-function) rate via scripts if feasible, else state the input").
- Scripts: book/figscripts/ch21/ (fig21_1–4.py, halo21.py, hib21.py, kernel21.py, limit21_*.py), screened tables from book/figscripts/ch10/si_elf_binned.npz.

### ER-12 (VALUE) Local-field factor at 3 MeV: "1.35 times" against the worked factor 1.345 (Self)
- ch21/s21-4.tex:3: "excludes ... every cross-section above $\SI{1.24e-41}{cm^2}$ ... the same zero excludes everything above $\SI{9.23e-42}{cm^2}$, a limit 1.35 times stronger."
- ch21/ch21.tex:4: "The same zero in silicon excludes cross-sections 1.35 times smaller at \SI{3}{MeV} if local fields are left out of the response"
- ch21/s21-4.tex:68–70: "$\mathcal{R} = \num{2.494e4}$ and $\sigmae^{\mathrm{lim}} = \SI{9.23e-42}{cm^2}$." / "They lower the rate to \num{1.855e4}, a factor 1.345, and the nominal limit is $\SI{1.24e-41}{cm^2}$."
- 2.494e4/1.855e4 = 1.3445 and 1.24e-41/9.23e-42 = 1.343; "1.35" is a rounding of 1.345 that the inputs do not give.
- Reported by: Self.
- Script: book/figscripts/ch21/we21_4.log / its script.

### ER-13 (VALUE) Gap used for the single-parameter ionization probabilities: 1.17 eV against the 123 K gap 1.160 eV (Self)
- ch29/E-13.tex:69: "The original value 5.2 makes the ionization probability per event 0.05 at \SI{3}{eV}, 0.36 at \SI{5}{eV}, 0.77 at \SI{8}{eV} and 0.88 at \SI{10}{eV}, from \cref{eq:E.13-ab} with $\Eg = \SI{1.17}{eV}$."
- ch29/E-13.tex:85: "The gap must match the detector temperature, \SI{1.17}{eV} at millikelvin against \SI{1.12}{eV} at room temperature"
- ch18/s18-1.tex:8 and s18-2.tex:37, s18-4.tex:31: the same model at "$\Eg = \SI{1.160}{eV}$ (silicon at \SI{123}{K})", the temperature of the calibration that E-13:71 compares with.
- Reported by: Self. Possibly intended (the original model's own setting); then E-13 should say so. Low priority.

---

## DERIVATION

### ER-14 (DERIVATION) In-medium factor of silicon at 3 eV: 761 against ε₂/L = 774 from the printed inputs
- ch08/s8-4.tex:149 (sec:8.4-mixing, :147): "At \SI{3}{eV} silicon has $\varepsilon_2 = 2.4$ and a loss function $L = 3.1\times10^{-3}$ (\cref{sec:4.4}), so $|\varepsilon|^2 = \varepsilon_2/L = 761$. A dark photon absorbed there couples as if its squared mixing were $\zeta^2/761$"
- ch08/s8-8.tex:135 (Summary): "an absorbed dark photon in silicon at \SI{3}{eV} is suppressed by the factor $|\varepsilon|^2 = 761$" (was "770" until the E2E Vol I pass, which aligned it with s8-4).
- 2.4/3.1e-3 = 774.2; 761 presumably from unrounded inputs.
- Reported by: ch08 unit editor (ch08.md, "Problems seen and not fixed", "Left listed"); E2E Vol I block reader ch07–ch08 (E2E-vol1.md, E2E-vol1-notes.md "Lead may want to confirm"); followups l.78.
- Scripts: the silicon optical data of sec:4.4 (book/figscripts/ch04/fig4_5.py, fig4_6.py); fix the inputs to the precision that gives 761, or the result to the inputs.

### ER-15 (DERIVATION) Complex couplings in the n-phonon weight: c_κ c_κ′ against c_κ^* c_κ′
- ch11/s11-3.tex:101 (eq:11.3-weight, label :102): "$\mathfrak{W}^{(n)}(\vect{q}) = ... = \frac{1}{n!}\sum_{\Delta\vect{R},\kappa,\kappa'}c_\kappa c_{\kappa'}\,\ee^{-\ii\vect{q}\cdot\Delta\vect{R}_{\kappa\kappa'}}\,\ee^{-W_\kappa - W_{\kappa'}}\,\bigl[\vect{q}\cdot B_{\kappa\kappa'}(\Delta\vect{R})\cdot\vect{q}\bigr]^n$"
- The removed redisplay in ch31/E-17 (label eq:E.17-Wn) had $c_\kappa^*c_{\kappa'}$; E-17.tex:21 now cites eq:11.3-weight. Other users: appE/D-31.tex:39, :43; ch11/s11-9.tex:7, :68.
- Reported by: E2E Vol III block reader ch31–ch33 (E2E-vol3-notes.md: "if complex couplings are meant anywhere, 11.3 needs the conjugate"); followups l.131.
- Open: are c_κ ever complex in the book (e.g. couplings with phases, effective-operator couplings of sec:11.8)? If yes, which factor carries the conjugate given the sign of the phase $\ee^{-\ii\vect{q}\cdot\Delta\vect{R}}$.

### ER-16 (DERIVATION) Size of the connected off-sector term in aluminum: is "about 0.2 eV" h_off or its square?
- ch08/s8-6.tex:203: "What a bound has to control is the connected part, in which $H_{\mathrm{off}}$ acts on the probe's excitations. Its square is at most the largest eigenvalue of the band matrix of zeroth moments of the Fan--Migdal spectral function, whose diagonal entries are the sums $N^{-1}\sum|g_{mn\nu}|^2(2n_{\vect{Q}\nu} + 1)$ of \cref{sec:6.3} without their energy delta function, and in aluminum it is estimated at about \SI{0.2}{eV}."
- appD/D-28.tex:97: "these moments form a matrix whose largest eigenvalue bounds the square of the connected part, estimated at about \SI{0.2}{eV} in aluminum."
- The eigenvalue has units eV² (sum of |g|²); "it" can be read as the eigenvalue or as h_off. The bin-width condition ("bins wide compared with ...", s8-6:203) depends on which.
- Reported by: ch08 unit editor (ch08.md, twice); followups l.78.
- Open: the source of the 0.2 eV estimate (no citation in either place).

---

## DEFINITION

### ER-17 (DEFINITION) Local-field ratio 1 + δ_LF: head-only reference (Sect. 13.4) against ε_mac reference (eq:E.16-dLF)
- ch13/s13-4.tex:122 (sec:13.4): "The local-field ratio $1 + \delta_{\mathrm{LF}}$ is $L^{\mathrm{PA}}$ with local fields but without the pair channel, divided by $L^{\mathrm{PA}}$ with the head alone. ... The macroscopic factor changes from $1/\varepsilon_{1,\vect{0}\vect{0}}^2$ to $1/\varepsilon_{\mathrm{mac}}^2$, an increase of 25 to \SI{31}{\percent} at \SI{1}{keV}"
- ch30/E-16.tex:27 (eq:E.16-dLF, label :28): "$1 + \delta_{\mathrm{LF}}^{(0)}(\vect{q},\omega) = \frac{\sum_{cv}\big|\sum_{\vect{G}}(\tilde\varepsilon^{-1})_{\vect{G}0}(\vect{q},\omega)\,\rho_{cv}(\vect{q}+\vect{G})\big|^2}{\sum_{cv}|\rho_{cv}(\vect{q})/\varepsilon_{\mathrm{mac}}|^2}$"
- ch30/E-16.tex:23 (Self, a third reference): "the same supercell with independent particles and a scalar screening $1/\varepsilon(\vect{q},\omega)$ gives the reference, and the difference is $\delta_{\mathrm{LF}} + \delta_{\mathrm{pair}}$; a third run with local fields restricted to the primitive reciprocal lattice gives $\delta_{\mathrm{LF}}$ alone."
- ch30/E-14.tex:13: "The two corrections are reported as the ratios $\delta_{\mathrm{LF}}$ and $\delta_{\mathrm{pair}}$ of \cref{sec:13.4}."
- Reported by: ch13 unit editor (ch13.md, "Pre-existing inconsistency, reported"); ch30-33 unit editor (ch30-33.md); E2E Vol II block reader ch12–ch13 (E2E-vol2-notes.md); E2E Vol III block reader ch27–ch30 (E2E-vol3-notes.md); followups l.92 (PRE-EXISTING).
- The two references differ by the 25–31 % macroscopic change. If E-16's δ^(0) is meant as a different quantity, it needs its own name; otherwise one definition changes.

### ER-18 (DEFINITION) Site positions of the magnet: r_i (antiferromagnet) against R_j (ferromagnet) in the same section
- ch07/s7-1.tex:121, :218, :224 (antiferromagnet, text moved from old D.19): "$\sum_i\ee^{\ii(\vect{k}-\vect{k}')\cdot\vect{r}_i} = N_{\mathrm{s}}\delta_{\vect{k}\vect{k}'}$"; "$S^+_{\mathrm{A}}(\vect{k}) \equiv \sum_{i\in\mathrm{A}}\ee^{\ii\vect{k}\cdot\vect{r}_i}S^+_i$"
- ch07/s7-1.tex:196, :204 (ferromagnet, form factor): "the spin density near ion $j$ is $\vect{S}_j\,\varrho_{\mathrm{s}}(\vect{r} - \vect{R}_j)$"; "$S^\pm(\vect{q}) = \sum_j\ee^{\ii\vect{q}\cdot\vect{R}_j}S^\pm_j$"
- appE/D-38.tex:7: "$\ee^{\ii\vect{G}\cdot\vect{r}_i} = 1$ on A, while on B, $\ee^{\ii\vect{G}\cdot\vect{r}_j} = ...$"
- Reported by: ch07 unit editor (ch07.md item 4, "Notation, report only"); followups l.76.
- Check NOTATION.md / appB for which symbol is registered for lattice sites (r is also the electron coordinate in s7-1:196).

### ER-19 (DEFINITION) Italic V for the normalization volume in Appendix A
- appA/A-5.tex:6: "$\int_V\dd^3r\,|\psi_{n\vect{k}}|^2 = 1$"
- appA/A-7.tex:21: "$\int_{-\infty}^{\infty}\dd t\,\ee^{\ii\omega t}\langle O_a^\dagger(t)O_b\rangle = VS_{ab}(\vect{q},\omega)$"
- macros.tex reserves italic V for a potential; the normalization volume is \Vol (script V). The same typo was fixed in s7-2:175 and s8-3:39 in the E2E Vol I pass.
- Reported by: E2E Vol I block reader appA/appC/appB (E2E-vol1-notes.md; "Plain typos, not changed because Appendix A symbols are frozen"); followups l.123.

### ER-20 (DEFINITION) One letter 𝒜 for activity and for the step column
- ch21/s21-7.tex:64, :69: "normalized to the activity $\mathcal{A}_{\mathrm{act}}$ per unit mass"; "The rate density below \SI{1}{keV} is therefore $\mathcal{A}_{\mathrm{act}}f_\beta$ per keV"
- ch21/s21-2.tex:33, :37: "$\mathcal{A}_i$ comes out in years for $\tilde\eta$ in inverse years"; "$\max_i\mathcal{A}_i(u_0) > 0$"
- Reported by: ch21 unit editor (ch21.md, "Notation remark, not changed").
- Low priority; check NOTATION.md for the registered meaning of 𝒜.

### ER-21 (DEFINITION) Notation entry of r_K, ω_K still describes the removed Klein relation
- appB/B-1-vol2.tex:502 and appB/B-1.tex:1253 (generated): "$k_{2}$; $r_{K}$, $\omega_{K}$ & Constant of the observed linear law ...; phonon-loss coefficient and phonon energy of the Klein relation $(14/5)E_{\mathrm{g}} + r_{K}\o..."
- ch18/s18-4.tex:49 (the only definition left): "$r_K$ the mean number of phonons of energy $\omega_K = \omega_{\mathrm{AB}}$ emitted above threshold per" carrier; the Klein relation (sec:18.4-klein, lim:18.4a, eq:18.4-klein) was removed in the ch18 third pass.
- Reported by: ch18 unit editor (ch18.md, "description is wrong: phonons per pair above threshold, phonon energy omega_AB"); followups l.115.
- The fix is in the generator input (NOTATION.md / gen_B1), then regenerate; not a hand edit of B-1.

---

## CITATION

### ER-22 (CITATION) Pitfall sentence of E-13 retargeted from sec:18.4 to the full-band cascade; author to confirm
- ch29/E-13.tex:85: "Two models that reproduce the same $\varepsilon_{\mathrm{eh}}$ do not validate each other's $F_{\mathrm{eh}}$, and the agreement of the full-band cascade of \cref{sec:18.3-fullband} with the single-parameter model is agreement of two models, not independent support."
- Before: "the agreement of the cascade of sec:18.4 with the single-parameter model" (a self-comparison, since sec:18.4 is that model).
- ch18/s18-4.tex:41: "Nor does the full-band cascade of \cref{sec:18.3-fullband}, which has no fitted constant: it gives $F_{\mathrm{eh}} = 0.114$, the envelope of its variants $[0.101, 0.115]$"
- Reported by: E2E Vol III block reader ch27–ch30 (E2E-vol3.md: "Author to confirm").
- Open: the full-band cascade reproduces ε_eh only to 4.15 eV (s18-4:16), not the measured 3.749 eV, so "two models that reproduce the same ε_eh" may not fit the new target.

### ER-23 (CITATION) "Dense tracks" in E-23 cited sec:19.1; retargeted to sec:18.5, sec:19.5
- ch32/E-23.tex:35 (subsection "Dense tracks", :33): "The calculation gives the ratio of $P(N_{\mathrm{eh}}|E_R)$ with and without interactions and the change of $F_{\mathrm{NR}}$, per recoil energy and species, which \cref{sec:18.5,sec:19.5} need for the dense tracks of nuclear recoils."
- Before: the subsection said sec:19.1 uses the dense-track ratio to bound subtree independence; the material is in sec:18.5 and sec:19.5 (ch29-32.md, "Outside references and inconsistencies" item 3).
- Reported by: ch29-32 unit editor; followups l.84; retargeted by E2E Vol III block reader ch31–ch33 (E2E-vol3.md).
- Open: verify that sec:18.5 and sec:19.5 do use the dense-track ratio as stated (grep "dense" in ch18/s18-5.tex, ch19/s19-5.tex); also E-23:35 "The cascade of \cref{sec:18.1} treats the pairs of one event as independent".

---

## TEXT

### ER-24 (TEXT) "Local fields change the silicon rate little" (E-6) against Volume II
- ch27/E-6.tex:44: "In the dark-matter rate of silicon and germanium, by contrast, the difference between the loss function with and without local fields is small~\cite{knapen2021dark}, because the rate integrates over $\vect{q}$ and $\omega$ and is dominated by energies and momenta ..."
- ch10/s10-2.tex:38: "$8.6\times10^4$ in the random-phase approximation without local fields and $5.9\times10^4$ with them"; ch10/s10-10.tex:87 (same numbers).
- ch21/ch21.tex:4: "excludes cross-sections 1.35 times smaller at \SI{3}{MeV} if local fields are left out of the response"; ch21/s21-4.tex:70 "a factor 1.345".
- ch08/s8-8.tex:66 (tab:8-nuisances): "local-field correction, RPA $\to$ RPA + LF ($\mathcal{X}$): $-0.44$ to $+0.25$ across $q$ and $\omega$, \cref{we:8-lf-nuisance}"; s8-8.tex:120.
- Reported by: E2E Vol III block reader ch27–ch30 (E2E-vol3-notes.md: "Technical statement, not changed; suggest the author qualify E-6:44").
- Open: what knapen2021dark actually says (book/sources/), and at which masses.

### ER-25 (TEXT) Chap. 23 opening quotes "about 0.5 eV" for "a density-functional calculation of silicon" without the functional
- ch23/ch23.tex:5: "a density-functional calculation of silicon puts the gap at about \SI{0.5}{eV}, less than half the measured \SI{1.17}{eV}, which would put the reach of a silicon detector at \SI{0.15}{MeV} instead of \SI{0.33}{MeV}."
- ch27/E-7.tex:110: "The Kohn--Sham gap is about \SI{0.6}{eV} in the representative PBE calculation (\cref{we:E-si-bands})"; ch04/s4-9.tex:166 "\SI{0.602}{eV} with PBE"; ch03/s3-4.tex:84 "LDA puts the silicon gap at \SI{0.52}{eV}, PBE at 0.56 to \SI{0.60}{eV}".
- Reported by: E2E Vol III block reader ch27–ch30 (E2E-vol3-notes.md: "The ch23 number is the LDA one (0.51–0.52 eV); suggest ch23:3 name the functional").
- Check also the reach: 2×0.52/(2.650e-3)² = 0.148 MeV (LDA, s3-4:140), 0.171 MeV with PBE 0.602 eV (s3-4:141).

### ER-26 (TEXT) Observation time for a classical field: "the shorter of" t_coh and the inverse width (Sect. 8.2) against D-25
- ch08/s8-2.tex:81: "The ensemble average needs an observation time long compared with the shorter of the coherence time $t_{\mathrm{coh}}$ of the field, ... and the inverse width of the target's response; a single record reproduces it only when it is also long compared with $t_{\mathrm{coh}}$. When both times exceed the record, ..."
- appD/D-25.tex:86: "The Gaussian field average sets those with $\vect{k} \ne \vect{k}'$ to zero; a single realization does the same in time, once the observation time exceeds the inverse spread of the frequencies $\omega_{\vect{k}}$, which is the coherence time $t_{\mathrm{coh}}$."
- Reported by: ch08 unit editor (ch08.md: "the two can be read consistently (ensemble average vs single record) but the wording differs"); followups l.78.
- The current s8-2 sentence already separates ensemble average and single record; the proposer checks that D-25 and s8-2 now agree and may propose "no change".

### ER-27 (TEXT) Sect. 9.1 says Sect. 22.2 "collects the open items of the book"
- ch09/s9-1.tex:91: "\Cref{sec:22.2}, which collects the open items of the book, lists the eight as one gap."
- ch22/s22-2.tex (tab:22-gaps, label :20) is now an index, one line per gap with its home section; whether it covers Volumes I and III as well as II decides "of the book" against "of this volume". (The same claim in s9-4 is gone.)
- Reported by: ch09-17 unit editor (ch09-17.md); followups l.6.

### ER-28 (TEXT) Caption of tab:22-calc says the remaining calculation steps are in tab:22-gaps
- ch33/s22-1.tex:17 (tab:22-calc, label :18): "Open calculations that would change a printed result, limit or ranking of the book, ordered by the result each would change; the remaining calculation steps are in \cref{tab:22-gaps}."
- tab:22-gaps (ch22/s22-2.tex:20) is now an index (gap, home section, class); the steps stand in the home sections, and some rows (13.9 onset, f-sum, rate and reach; 20.1 validation) are now only in tab:22-calc (ch20-22.md).
- Reported by: E2E Vol II block reader ch20–ch22 (E2E-vol2-notes.md, suggests "...are stated in the sections indexed by \cref{tab:22-gaps}"); ch20-22 unit editor (ch20-22.md); followups l.133.

---

## Reported items not entered

Resolved in the current text (checked by grep at harvest; nothing left to correct):
- ch08/s8-8 Summary "factor 770": now 761 (the remaining 761/774 question is ER-14).
- ch08/s8-1 fermionic absorption kinematics (bosonic values given for the fermion): now "the kinematics, which \cref{sec:8.1-kinematics} fixes" (s8-1:184).
- ch08/s8-5 "App F gives each literature formula in this form": replaced (no app:F in s8-5).
- ch09/s9-4 and s9-summary App F counts (90 rows, 80 tested, six unsized): recounted by the ch09–ch10 block reader.
- ch17/s17-5 "5.6 % below the measured average (we:11-cbar)" and lim:11.1c clause: deleted; tab:17-boundaries row contradicting tab:9-edges: removed.
- ch22/s22-2 "Landau form within 10 % ... T ≥ 0.94 T_CM": gone; ch22 boosted row: removed.
- ch10/s10-9 "app:E.26 ... which also sizes the term": gone.
- ch31/E-21 NV-center target specification: no NV left in E-21.
- ch23 opening and ch33 opening/Summary "every method is placed on the truncation label": removed.
- E-14 "PAW has no nonlocal term" against we:22-fsum: the worked example now sits in E-14 and E-14:100 carries the accurate wording.
- appC/C-18 isotropic [100] model sentence pointing to a comparison in sec:5.2: gone.
- ch01/s1-4 app:C.9, ch06/s6-4 app:D.8, appE/D-31 app:D.15, ch08/s8-8 app:D.47 pointers: gone or retargeted.
- ch26/E-4 ∂n against ∂𝓃: E-4 now writes ∂\nd.
- tab:20-nuisances cell "room-temperature aluminum constants lengthen t_l by 20 %": removed with the trim.
- ch03/s3-3 pointer to "the value 1.11 eV of we:1-mmin": removed.

Excluded as layout, wording, terminology, label retarget or structure (handled elsewhere): every retarget of a removed label (followups l.16–20, 26, 35, 43–45, 49, 56, 61, 63, 68, 75, 80, 91, 124; unit-log "Outside references to fix" tables); Gamma typography in E-4 (l.51); duplicate passages and pointer-backs (l.10, 25, 30, 36, 40, 42, 47, 54, 59, 73, 77, 87, 122); missing Summaries (l.3, 24, 33); figures still drawing removed models and unused figures (l.7, 46, 53, 62, 93, 97, 109); notation-table rows of removed symbols (l.8, 27, 86, 111, 115 apart from ER-21, 119); terminology pass "nuisance" (l.112, 129); placement and decisions (l.9, 21, 28, 58, 72, 74, 88, 104, 121, 126, 128, 130, 134); remap/map tools (l.13, 89, 94, 106, 110); stash incidents (l.15, 65); oversized tables (l.64); s16-5:108 multivalley envelope against the removed effective-mass envelope (l.118; a model-removal consistency question for the ch16 owner, not a value); ch33 chapter ranges \crefrange{chap:31}{chap:32} (chapter order of Vol III is being changed by the structure editors); E-11/E-13/E-17/E-23/E-24 placing calculations on 𝔗 (reader: can stay); G4CMP lumped absorption kept (l.11); A.2/A.7 duplicate formula (appA-appC.md item 4).

---

## Proposed grouping for stage 2

Five groups, 4–7 entries each, all 28 entries assigned once.

### Group G1 `si-electronic-constants` (6 entries): ER-2, ER-3, ER-4, ER-5, ER-6, ER-25
Silicon constants of the electronic-structure chapters: plasmon 16.4/16.6 eV, SG15 core radius, LDA lattice constant, PBE and LDA gaps, the Chap. 23 opening gap.
- Chapters: ch03 (s3-1, s3-3, s3-4), ch04 (s4-3, s4-4, s4-5, s4-7, s4-9), ch05 (s5-1), ch23 (ch23.tex, E-1, E-3), ch24 (s3-5, E-2), ch25 (s3-6 caption), ch27 (E-6, E-7), ch29 (E-13), ch32 (E-24).
- Scripts and data: book/figscripts/ch03/qe_ch03.py, qe_si_pbe.npz, qe_si_lda.npz, qe_si_tm.npz, fig3_8.py, ld1/ (fig:3-psae potential), fig3_* for fig:3-si-bands; book/figscripts/ch04/fig4_5.py, fig4_6.py (loss peak).
- Sources: schlipf2015optimization, csonka2009assessing, ponce2016epw, lucero2012improved, aryasetiawan1998gw, ramanathan2020ionization (Table I).

### Group G2 `vol1-numbers-and-notation` (7 entries): ER-7, ER-8, ER-14, ER-16, ER-18, ER-19, ER-26
Volume I numbers and symbols cited across volumes: Si optical phonon 60/64 meV, NiO magnon maximum, in-medium factor 761/774, size of h_off, t_coh wording, site-position symbol, italic V in Appendix A.
- Chapters: ch01 (s1-3, s1-5), ch07 (ch07.tex, s7-1, s7-4), ch08 (s8-2, s8-4, s8-6, s8-8), ch14 (ch14.tex, s14-1), appA (A-5, A-7), appD (D-25, D-28), appE (D-38).
- Scripts: book/figscripts/ch01/ (fig1_* kinematics figure, limit1_nuclear.py), book/figscripts/ch07/fig7_1.py, book/figscripts/ch14/magnon14.py, book/figscripts/ch04/fig4_5.py and fig4_6.py (ε₂ and L at 3 eV), book/figscripts/ch08/we8_4.py.
- Also NOTATION.md, tex/macros.tex (\Vol).

### Group G3 `cascade-and-recoil` (6 entries): ER-1, ER-9, ER-13, ER-21, ER-22, ER-23
Ionization cascade, Alig–Bloom calibration and nuclear-recoil specifications: the two A_AB calibrations, the E-13 gap, the full-band retarget, the r_K/ω_K notation entry, the dense-track pointer, the SW displacement threshold.
- Chapters: ch18 (s18-1, s18-2, s18-3, s18-4, s18-5, s18-summary), ch19 (s19-1, s19-5), ch28 (E-10), ch29 (E-11, E-13), ch32 (E-23, E-24), appB (B-1, B-1-vol2; via NOTATION.md and the generator).
- Scripts: book/figscripts/ch18/casc18_4.py, table18_4.py (+ .json/.log), si_cascade18.py, fbc18.py (full-band, fbc18_data.json), fig18_2.py; appB generator (tools/, gen_B1).
- Sources: ramanathan2020ionization, nielsen2026first, rodrigues2021absolute, kadribasic2018directional, sassi2022energy.

### Group G4 `screening-and-local-fields` (4 entries): ER-11, ER-12, ER-17, ER-24
How much screening and local fields move the silicon rates: the Chap. 21 examples on the independent-particle table, the 1.35/1.345 factor, the δ_LF reference, the E-6 claim.
- Chapters: ch08 (s8-8), ch10 (s10-1, s10-2, s10-10), ch13 (s13-4), ch21 (ch21.tex, s21-1, s21-2, s21-4, and the worked examples named in ER-11), ch27 (E-6), ch30 (E-14, E-16).
- Scripts and data: book/figscripts/ch21/ (fig21_1–4.py, halo21.py, hib21.py, kernel21.py, limit21_*.py, we21_4), book/figscripts/ch10/ (rate10_2.py, si_elf_binned.npz, si_fcrys.py, nuis10_10.py), book/figscripts/ch13/ (eps13_4.npz).
- Sources: knapen2021dark, essig2016direct.

### Group G5 `vol2-rates-and-index-text` (5 entries): ER-10, ER-15, ER-20, ER-27, ER-28
Remaining Volume II items: recomputed fig:12-plane numbers, the conjugate in eq:11.3-weight, the 𝒜 symbol, and two statements about what Chap. 22's index holds.
- Chapters: ch09 (s9-1), ch11 (s11-3, s11-9), ch12 (s12-1, s12-4), ch21 (s21-2, s21-7), ch22 (s22-2), ch31 (E-17), ch33 (s22-1), appE (D-31).
- Scripts: book/figscripts/ch12/fig12_1.py (no log on disk; rerun), mig12.py; book/figscripts/ch11/ (we11_3.py, mph11.py for the n-phonon weight); book/figscripts/ch22/gaps22_2.py (row list of tab:22-gaps).
