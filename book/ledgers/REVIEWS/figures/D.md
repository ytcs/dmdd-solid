# Figure check, part D (chapters 18–22)

Directive: briefs/reviews/figure-check.md. Each figure was rendered at 150 dpi and checked against its caption, the paragraph that cites it and its script log. Fixes were made in the scripts only; each script was rerun and its PDF re-rendered. Every rerun log matches the previous log apart from run times. fig21_3.log had been cut off before its last lines and is now complete. Stray "done-a"/"done-f" marker lines from an earlier wrapper are gone from limit20_2a.log and fig20_2.log. No number in the text changed. One caption was edited (fig19_2). Font sizes were measured at the included width; ordinary text below about 5.5 pt was enlarged (sub- and superscripts excepted).

Totals: 50 figures, 15 OK, 35 FIXED, 0 LOGGED.

## Chapter 18
- map18 — FIXED: the Limit Check tags were the planned labels "18.2a-c, 18.3a, 18.4a-c", which differ from the printed numbers. They now read 18.1–18.3, 18.4 and 18.5–18.7, matching the auto counter (main.aux).
- fig18_1 — OK.
- limit18_2a — OK (gray onset 14.9 Eg, F peak 1.5 checked).
- fig18_2 — OK (log values match the text; script not rerun, 236 s).
- limit18_2b — FIXED: the label "F_ren/F_park = 0.870" sat on the dashed renewal curve. It now sits below the dotted line.
- limit18_2c — FIXED: the "λ_AB → 0" label sat in the gray ±10 % band, where it read as a label for the band. It now sits next to the markers, with an arrow.
- fig18_3 — OK.
- limit18_3a — OK.
- limit18_4b — FIXED: the legend said "cascade / Eq. (12)" and "Eq. (13)". Those are the paper's equation numbers and clash with the book's numbering. It now reads "cascade / plane" (caption: eq:18.4-RKplanes).
- limit18_4a — FIXED: the gray band was drawn between grid points (about 0.70 to 78), while the caption says 0.65 to 84. It is now drawn between the interpolated 10 % crossings from the log. The "1.8 Eg uniform population" label touched the cascade curve and was moved below the dotted line.
- limit18_4c — FIXED: the legend printed k2 = 1.87 eV against 1.88 in the caption and the log. It is now computed from k2(1.17, 0.063). The "diamond" and "CaWO4" labels overlapped each other and the NaI/CsI crosses. The diamond label now sits above-left. The CaWO4 label is dropped: it had no clear place, and neither the caption nor the text refers to it.
- fig18_4 — FIXED: the panel label "(b)" sat on the black r_gap curve and was moved.

## Chapter 19
- map19 — FIXED: the arrow label "add nonadiabatic close collisions" was crossed by its arrow and was moved right.
- fig19_1 — FIXED: annotation, region, legend and vertical-line fonts were 5.2–5.7 pt at print size and are now about 6–6.3 pt. The rotated labels x_R = 4, E_d⟨111⟩, E_d avg and "binary threshold" crossed curves; they were moved to clear places. The "vacancy" label touched the kick arrow.
- fig19_2 — FIXED: the legends were 5.5 pt and crossed the E_R,th line in both panels; they were enlarged and moved. Axis units changed from "[eV]" to "(eV)" to match the book. Caption: added "vertical line as in (a)" for the undescribed line in (b).
- limit19_3a — FIXED: the E_R,th label overlapped the dashed constant-binding curve.
- fig19_3 — FIXED: the legend label rendered as "0.1--3.9 keV" (literal double hyphen) and now uses an en dash. The legend was crossed by the E_R,th line and moved to lower right. The E_R,th label overlapped the dashed curve.
- limit19_3b — FIXED: "0.1--10 keV" literal double hyphen replaced by an en dash.
- limit19_4a — FIXED: "Kinchin--Pease" literal double hyphen in the legend replaced by an en dash.
- fig19_4 — FIXED: the "collisions, cascade" text ran over the y axis and the t_pr line; it is now rotated inside its band. Legend enlarged to 7 pt.
- limit19_5a — FIXED: the x-axis label was clipped at the right edge ("window" cut) and was shortened. The legend entry "Y_ph(0) = 1" was crossed by the f_ret = 0.941 line and was moved left.
- limit19_5b — FIXED: legend fonts were 5.5 pt and are now 6.1 pt.
- fig19_5 — FIXED: the legend in (a) was crossed by the Frenkel-pair spike and was moved to upper left.
- limit19_6a — FIXED: the \frac{5}{576} in the legend printed at 5 pt and now reads (5/576).
- limit19_6b — FIXED: the gray band started at the grid point 1.750, while the caption says 1.74. It now starts at the root-searched crossing 1.7437 from the log.

## Chapter 20
- map20 — FIXED: the labels "drift the pairs in the field", "follow the primary phonons" and "sensor energy" were crossed by their arrows and were moved clear.
- fig20_1 — OK.
- limit20_1a — OK.
- limit20_1b — FIXED: the legend said n_Q eV_bias, while the axis and caption say N_eh eV_bias.
- limit20_1c — FIXED: the legend said "printed form" and now says "published form", the caption's wording.
- limit20_2b — FIXED: the legend wrote E_D, while the caption writes ω_D, for the same 55.6 meV.
- limit20_2a — FIXED: the legend overlapped the dotted undecayed-line curve and was moved to lower right.
- fig20_2 — FIXED: the legends were 5.2–5.6 pt at the 0.80 scale; they are now 6.0–6.4 pt. The (b) legend was crossed by the Si dashed curve. The y range was extended down to 1e-7, with the legend below the curves and "(b)" at top right.
- fig20_3 — OK.
- limit20_3a — FIXED: the dash-dot and DMM legend handles were red, although those styles are drawn in both direction colours. They are now neutral gray proxies.
- fig20_4 — OK.
- limit20_4a — OK.
- fig20_rcoll — FIXED: the legend was 5.2 pt and was crossed by the purple curve and the 0.84 meV line. It is now a 7 pt legend below both panels (taller figure).
- fig20_5 — FIXED: the legend entry "zero bias, same readout" sat on the red S_HV = 2 line; the legend was moved up.

## Chapter 21
- map21 — FIXED: "add theory nuisances" touched the Kinematic-edge box. "unknown background; several experiments" and "add rankings, pair energies, readout, backgrounds" were crossed by their arrows. All three were moved clear.
- limit21_1a — OK.
- fig21_1 — OK.
- fig21_2 — FIXED: the "1 pair" label in (b) sat on the crossing of the 1- and 3-pair curves and was moved to the branch where the bound is the 1-pair curve.
- limit21_2a — OK.
- fig21_3 — FIXED: in (a) the legend was crossed by the diverging curves, and in (b) the "k_tail = 2.5" entry sat on the purple curve. Legends were 5.5 pt. The (a) legend now sits above the panel and the (b) legend sits between the 9.0 and 7.5 lines, both at 6.3 pt. The (b) label "year average, k_tail = 0" was crossed by the dashed mass line and was shortened to "year average"; the caption already states the year average.
- fig21_4 — FIXED: "electron--hole attraction" literal double hyphen replaced by an en dash.
- fig21_5 — FIXED: "(b)" overlapped the ε_yy² label, and the (b) legend was crossed by the ε_xx² line. The y range was raised to 3e6 and the legend enlarged to 6.1 pt.
- fig21_6 — OK.

## Chapter 22
- fig22_1 — OK (counts 2/12/9 agree with the text and log).
