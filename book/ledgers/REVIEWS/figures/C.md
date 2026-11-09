# Figure check, part C (chapters 14–17)

Directive: briefs/reviews/figure-check.md. Each figure was rendered at 150 dpi (renders in /tmp/claude-0/figcheck-C/) and checked against its caption, the paragraph that cites it and its script log. Fixes were made in the scripts only. Each fixed script was rerun and its PDF rendered again. Every rerun log is identical to the previous one, so no number in the text changed. No caption was edited. Font sizes were checked at the included width (text width 155 mm; limit boxes about 147 mm). Ordinary text below about 5.5 pt was enlarged; sub- and superscripts were not counted. The Limit Check numbers in map14–map17 were checked against the order of the limitbox environments, and all match.

Private build: latexmk into /tmp/claude-0/build-fig-C, 0 errors, 1842 pages.

Totals: 56 figures, 28 OK, 27 FIXED, 1 LOGGED.

## Chapter 14
- map14 — OK (Limit Check tags 14.1–14.8 match).
- limit14_1a — OK (gray band ends at 1/(2|S|) = 0.64, |S| = 0.78).
- fig14_1 — OK (log rates match the text; the gap and gapless ratio of 29 is checked).
- fig14_2 — LOGGED: the panel (a) legend, at lower right, sits on the red w_par curve and the (1,1,1) grid line. The fix is a one-line move to upper right. The script did not finish in 25 minutes (a 64^3 k sum at each of 363 path points, plus 3e6 random k for panel b), which is not light Python. The edit was reverted, and the PDF and log are unchanged. To fix it: in fig14_2.py, change `ax.legend(..., loc="lower right")` in panel (a) to `"upper right"` and rerun.
- fig14_3 — FIXED: the measured-gap square sat on the B0 = 0 axis and was half clipped; the x axis now starts at -0.3 T. Legend and labels raised from 6.5 to 7 pt, about 5.2 pt to 5.6 pt at 0.95 linewidth.
- limit14_3a — FIXED: the label "ferromagnetic pair" sat 40 % below its dotted line, inside the gray band, where it read as a label for the band. It now sits just above the line at 1. Legends raised from 6.3 to 7 pt, about 5.0 pt to 5.5 pt.
- fig14_4 — FIXED: the "q·s_e: no field" label of (a) ran into the shading legend of (b), and the legend moved under the matrix. Legend and side-column text raised from 6.0–6.6 to 7 pt, about 5.1 pt to 6 pt.
- limit14_4a — OK (gray band ends at 0.094, squares at 2.2 and 2.34).
- fig14_5 — FIXED: in (b) the "dark matter (1–3 eV)" label sat on the linear and turnover curves. The band labels now sit centered in their bands below the curve, and the legend moved to upper left. Legends raised from 6.0 to 7 pt, about 4.8 pt to 5.6 pt.
- limit14_5a — FIXED: in (a) the dashed all-branch curve, peaking at 0.25, ran through the legend text. The y range was raised to 0.42 so the legend sits above the curve. Legends raised from 6.3 to 7 pt.
- limit14_5b — FIXED: the "critical: open" label sat inside the hatched band, where the hatching crossed the text. It now sits just left of the band.
- limit14_6a — OK.
- fig14_6 — OK.
- limit14_6b — OK (gray band from 13 t_coh).
- limit14_6c — OK (circles at 23 and 5.4 t_coh).

## Chapter 15
- map15 — FIXED: the "resum the screening" label spanned the whole arrow and touched the box edge and the diagonal arrows. It now wraps onto two lines.
- fig15_1 — FIXED: the 2Δ_BCS dotted line in (b) ran through the legend handles. The legend now starts just right of the line. Values in the log match the 11–22 % and 27–34 % of the caption.
- limit15_1a — OK (gray band from y = 7.9).
- limit15_2a — OK (gray band from y = 9.1).
- fig15_2 — FIXED: the (a) legend entry "ω → ω + iγ_rel" sat on the red dotted curve, and the "kinematically forbidden" label was crossed by the black Lindhard curve. The legend moved to lower right and the label to the top of the gray band.
- limit15_4a — OK (gray band from 11.4 Δ, ω_D at 205 Δ).
- fig15_3 — FIXED: the ω_D line crossed both legends, and the red direct curve ran into the (b) legend text. The (a) legend now has an opaque frame. The (b) legend moved to upper right, with the y range raised to 1e8 and the (b) ω_D line stopped below it.

## Chapter 16
- map16 — OK (Limit Check tags 16.1–16.17 match).
- limit16_1a — OK.
- fig16_1 — FIXED: legends raised from 6.2–6.3 to 6.8 pt, about 5.3 pt to 5.8 pt. The (a) y range was raised to 1e-31 so the larger legend clears the "× 642" curve.
- fig16_2 — FIXED: the axis units "[eV]" were changed to "(eV)", the book style. The x label now reads "momentum q (eV); q_∥ for the sheet and the tube".
- limit16_2a — OK (gray band ends at 1.36 k_F).
- limit16_2b — FIXED: the red 3D curve crossed the long legend entries. These were shortened to "3D/2D, full Lindhard, light species".
- limit16_2c — OK (1.12 and 1.78 at k a_s = 12 match 0.473/0.4215 and 0.487/0.274).
- fig16_3 — OK.
- limit16_3a — OK (blue curve ends at 31 eV, gray bands 0.60 and 94 eV).
- limit16_3b — OK.
- limit16_4a — OK.
- fig16_4 — OK.
- fig16_5 — FIXED: the line labels 2p0, 2p±, 3p0 and 3p± sat on the peaks and were crossed by them. Each now sits just above the taller of the two peaks; 3p0 is set slightly right of 2p±.
- limit16_5a — FIXED: the "impurity band" label sat in the hatching over the orange curve. It now sits centered in the hatched band at 0.6, clear of the curves, on a white patch.
- fig16_6 — FIXED: the "1.0 GeV" arrow was drawn diagonally from a label crowded against "0.5 GeV" and the dashed curve. It is now a vertical arrow from a label at 4.5, below the curves.
- limit16_6a — OK (gray bands from 1.36 and 2.65).
- fig16_7 — FIXED: the panel label "(a)" sat on the red curve and was moved to lower right.
- limit16_7a — FIXED: the blue 0.5 GHz curve crossed the "relaxation plateau 1/2" label. The label now sits at the right end, above the dotted line.
- limit16_7b — OK (gray band from 1.15 neV).
- limit16_7d — OK (gray band ends at 4.3 meV).
- limit16_7c — FIXED: the Ti-6Al-4V label touched the blue curve and was moved down.
- fig16_8 — OK.
- limit16_8a — FIXED: the panel labels "(a)" and "(b)" sat on the black line at 1 and were moved down.
- limit16_8b — OK.
- limit16_8c — OK.
- limit16_8d — OK.

## Chapter 17
- map17 — FIXED: the Absorption → Figures of merit arrow cut through the Interference box. The Interference box was narrowed, and the arrow now runs down its right side and enters from the right. The "keep the cross terms" label sat on its own arrow and now sits beside it.
- fig17_sectors — FIXED: the (c) title said σ_n = 1e-38 cm², while the caption and text use σ_p; it now reads σ_p, and the script docstring was changed to match. The 10^-2 contour labels sat on the bunched acoustic edge and the dash-dotted line, where they could not be read. They were dropped; the 10^0 to 10^4 labels remain. A larger legend font (6.5 pt) was tried and covered the "phonon-assisted window" note, so the 6 pt legend (about 5.4 pt at print size) was kept.
- fig17_2 — FIXED: the ZrTe5 label sat on the green curve and its end tick, and was moved above them. The axis unit "[eV]" was changed to "(eV)".
- fig17_3 — FIXED: the endothermic curves, the plasmon-pole curve and the 1.11 eV line ran through both legends. Both legends moved to upper left. The axis unit "[eV]" was changed to "(eV)".
- fig17_4 — FIXED: in (b), "phonon-assisted only" was crossed by the q_BZ line and now sits on a band-colored patch; the "0.45" mass label was crossed by the q* line and was shifted right. In (a) and (b), "window" touched the frame and "no scattering" touched the dashed edge, and both were moved.
- limit17_5a — FIXED: the legend covered the ω_p^val line and the 3.5 reference line. It moved to the free area right of the K edge, with an opaque frame.
- fig17_window — OK (dotted lines at 0.32, 0.41, 0.42 and 0.65 MeV, gray band ±10 %).
- fig17_5 (rank17_6.py) — FIXED: the P(first) column was printed inside the rank range, and the LiF bar ran into its "0". The x range was widened to 28.5 and the column moved right.
