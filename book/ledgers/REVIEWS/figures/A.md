# Figure check, part A (chapters 1-8, appendices)

Directive: briefs/reviews/figure-check.md. Each figure rendered at 150 dpi (zoomed to 200-400 dpi where needed), read against its caption and citing paragraph. Fonts were checked as the nominal size in the script times the print scale (included width / PDF width). All fixes are in the figure scripts. Each script was rerun and the new PDF rendered and checked again. No physics, no numbers and no captions changed. Where a script writes a `.log` (fig6_6, fig7_3), the rerun output matches the log exactly.

Appendices: none of the appendix tex files includes a figure (no `\includegraphics` in tex/app*), so there is nothing to check there.

Totals: 73 figures checked (incl. 7 Limit Check plots and 6 chapter maps). 36 OK, 37 FIXED, 0 LOGGED.

## Chapter 1
- fig1_1: FIXED. The "primordial black holes" label ran across the Planck-mass dotted line; it now sits above its bar.
- fig1_3: FIXED. The legend sat on the June/December curves near the peak; ylim raised to 3.7 so the legend clears them.
- fig1_4: OK
- fig1_5: FIXED. The mass labels (0.1-100 MeV) sat on the line omega = q v_max; they now sit just right of each edge at q = 2 m v_max. The 100 MeV label goes inside the edge, because outside it ran past the frame. The "free Si nucleus" label was crossed by the 100 MeV edge and moved.
- limit1_nuclear (Limit Check 1.1): OK
- fig1_6: FIXED. The v_max label collided with the curves at the bottom and moved up to 1e-3.
- fig1_7 (Limit Check 1.2): FIXED. The legend read "light limit, (q0/q)^2" on an F_DM^2 axis. It now reads "F_DM = (q0/q)^2", parallel to the heavy-limit entry.
- fig1_8: OK
- fig1_9: FIXED. The heavy-mediator curve ran through the m_min label, which moved to the bottom of the dotted line.

## Chapter 2
- map02: OK (its tag "Limit Check 2.1" matches lim:2.2a)
- fig2_1: OK (smallest text about 5.7 pt)
- fig2_2: FIXED. The F^2 curve crossed the "q = q0" label, which moved left of the line.
- limit2_ionization (Limit Check 2.1): OK
- fig2_3: OK
- fig2_4: OK
- fig2_5: FIXED. In panel (a) the legend sat on the imaginary-part Lorentzian; it moved to the upper left.
- fig2_6: OK

## Chapter 3
- map03: OK
- fig3_1: FIXED. The a2 label touched a bond line and was offset.
- fig3_2: FIXED. The Gamma and W labels lay on zone edges and k_x lay on its axis; all three were re-offset.
- fig3_3: FIXED. The q_r labels sat on their arrows and on the dashed circle. The q label sat on a zone corner. The "2 m v_max (1 MeV)" label lay on a grey zone. All were moved into free space.
- fig3_4: FIXED. Panel (a) labelled n = 4, but band 4 (>= 11.4 eV) was off the 9 eV axis and the n = 3 label pointed at no band. The axis now runs to 14.2 eV, so the caption's "four lowest bands" are all shown, and each n label sits by its band. In panel (b) the optical-limit line crossed the 2|U|/v_max label, which moved left of the line.
- fig3_5: OK
- fig3_6: FIXED. E_dir touched the conduction band and E_g in (b) lay on the dashed and dotted lines; both moved.
- fig3_7: FIXED. The Gamma_2'c label was crossed by the band rising from Gamma and moved below it.
- fig3_8: OK
- fig3_9: OK
- fig3_10: FIXED. The legends lay over the small-p tails; they now have an opaque white box.
- fig3_11: OK
- fig3_12: FIXED. In (a) the legend covered bands and "frozen window" lay on the bands; the legend moved below the X-W-K bands and the frozen-window line got a legend entry. The closing Gamma tick was missing and is restored. In (b) the legend lay across the dips; it moved to the empty K-Gamma corner.

## Chapter 4
- map04: FIXED. The "Exact constraints" body ran past its box and is now wrapped into three lines. The arc ran through the "causality, commutators" label, which moved clear of it.
- fig4_1: OK
- fig4_2: OK
- fig4_3: FIXED. The legend showed a literal "Kramers--Kronig" and now uses an en dash.
- fig4_3b: OK
- fig4_4: FIXED. The "+ ..." ran into the last leg; spacing widened.
- fig4_5: FIXED. The E_g label lay on the loss curve and the gap line, and moved to the top.
- limit4_tf (Limit Check 4.1): FIXED. The legend showed a literal "Thomas--Fermi" and now uses an en dash.
- limit4_plasmon (Limit Check 4.2): OK
- fig4_6: FIXED. In (a) the right eV axis that the caption describes was hidden under the colorbar; the colorbar was moved and the axis labelled. The omega_+, omega_pl(q) and q_c labels lay on lines or dark fill and were moved. In (b) the legend crossed the plasmon arrow; it moved, and the Mermin entry was shortened, since gamma_rel is given in the caption.
- fig4_7: FIXED. In (b) the legend lay on the curves and the dotted 16.4 eV line, and the rotated window label lay on the unscreened curve. The legend now names only the two styles that panel (a) lacks, and sits lower right. The window label moved inside the band. The legend in (a) no longer touches the frame.
- fig4_8: FIXED. The "Im z" label overlapped the top circle in (a) and the arc in (b), and was moved.
- fig4_8b: OK
- fig4_9: FIXED. In (d) the middle rung covered the electron and hole arrows; it is now 4 rungs, none at the arrows.
- fig4_9b: FIXED. The emission-onset leader ran through the legend, which moved. "absorption only" crossed the x = 0 line.
- fig4_10: OK
- fig4_11: FIXED. In (a) the legend sat on the measured 46 peak; ylim raised and the legend kept inside the frame.

## Chapter 5
- map05: OK
- fig5_1: FIXED. In (a) the "omega_opt 0.064" label ran into the axis label of (b), so the panels were spaced wider. In (c) the inset fonts were 5-5.5 pt (5.2 pt printed) and the inset legend and y label collided with data and ticks. Inset fonts are now 6.2 pt and the legend is dropped (the caption names the circles and line). The unit is now the inset title.
- fig5_2: OK
- fig5_3: FIXED. The (c) y label overlapped panel (a); the right-hand panels moved right. The (b) legend went from 5.8 to 6.5 pt.
- fig5_4: OK
- fig5_5: OK
- fig5_6: FIXED. In (b) the TA, LA and g_ph labels lay on the shaded DOS peaks and moved to the empty bottom corner. The script reruns in about 95 s, using its cached force constants.

## Chapter 6
- map06: OK
- fig6_1: FIXED. In (a) the legend sat on the steps at t = 0. It is now narrow (title omega_e tau_acc, entries 0, 1, 4) and sits below the plateau.
- fig6_2: OK
- fig6_3: OK
- fig6_4: OK
- fig6_5: OK
- fig6_6: FIXED. The legend text lay over the shaded g_ph area. The label was shortened ("scaled"; the caption says how) and the legend moved up. The rerun output equals fig6_6.log.
- fig6_7: FIXED. In (b) "photon omega" was clipped by the frame and moved left of the arrow.
- fig6_8: OK (smallest text about 5.7 pt)

## Chapter 7
- fig7_1: OK (smallest text about 5.7 pt)
- fig7_2: OK
- fig7_3: FIXED. In (a) the legend lay on the band lines and moved lower center. In (b) the dotted 7 keV curve crossed its label, which moved past the curve's end. The rerun output equals fig7_3.log; limit7_gapless comes from the same script and is unchanged.
- limit7_gapless (Limit Check 7.1): OK
- fig7_4: OK
- fig7_5: FIXED. The text was 6-6.5 pt at a 0.87 print scale (5.2 pt). The figure width went from 7.0 to 6.5 in and all small text is now 7 pt. The E_ZPL notes overlapped the ground surface and the emission arrows, and moved left of the absorption arrows. The absorption and emission labels were re-placed clear of the curves.

## Chapter 8
- map08: OK
- limit8_2a (Limit Check 8.1): FIXED. In the left panel the 10^-24 label straddled the grey boundary and the second 10^-20 label sat on the red dashed line; both were re-placed. In the right panel contours crossed the "m_V = p_rel" label. It was removed, since the line is labelled in the left panel and in the caption.
- fig8_1: OK
- fig8_3: FIXED. The rate formula's fractions printed at about 4 pt; they are now display fractions, with the second line set separately. The Readout and Counts bodies touched their chapter tags, so the boxes were made taller. The width went from 6.4 to 6.0 in, so the smallest text prints at about 6 pt.

## Notes (no action)
- fig3_12 caption: it quotes the PBE gap at 0.843 (2pi/a), the fine-grid value of fig3_6. The fig3_12 script prints 0.848 from its coarser path sampling. The figure itself shows no number, so nothing was changed.
- Chapter-map tags write chapter ranges with a hyphen ("Chaps. 3-7"), not an en dash. This is a style point outside this check.
