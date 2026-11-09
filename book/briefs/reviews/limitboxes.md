# Redesign the three existing limit boxes (user directive)

The user's verdict on the current boxes: "more informative way to present a limit is just to show a plot. Writing a chain of citations and procedure doesn't convey useful information." The new design is in book/STYLE.md, book/SPINE.md ("Literature formulas as limits") and briefs/sections/COMMON.md.

Rewrite the three existing boxes:
- **s1-3 "Elastic nuclear recoil".** Plot the free-recoil δ(ω − q²/2M) response against the lattice-bound impulse peak, with width ≈ (E_R ω̄_ph)^{1/2}, as a function of E_R/ω̄_ph for silicon. Shade E_R ≫ ω̄_ph, where the free formula holds, and mark the single- and few-phonon regime. Use a simple, explicitly stated model: an Einstein or Debye phonon spectrum with the Si phonon energy from the text. Label the model in the caption.
- **s1-4 "Heavy and light mediators".** Plot F_DM(q)² against q/q₀ for a range of mediator masses m_V against the two limits (1 and (αm_e/q)²), with the region where each limit holds within 10% shaded.
- **s2-2 "Atomic ionization rate".** Plot the quantity whose limit the box states against its controlling parameter, comparing the limit form with the fuller result in the text (read s2-2 to choose).

For each box:
- **Content:** the literature formula with a one-line source citation (keep the existing citation); the figure inside or directly attached to the box; and one sentence on what breaks down outside the shaded region. The chain stays in, or moves to, the surrounding text.
- **Appendix F row:** move the old Source / Chain / Validity / Leading-correction content into a row of tex/appF/F-rows.tex. Create the file: a longtable with columns Formula | Source (eq.) | Approximation chain | Validity | Leading correction | Section. Create tex/appF/appF.tex as \chapter{Literature formulas as limits}\label{app:F} that \inputs it, and add \input{appF/appF} to main.tex after appE.
- **Figures:** scripts go in book/figscripts/chNN/, PDFs in tex/figures/chNN/, with every number sourced and every model choice named in the caption.

**Follow:** REGISTER.md and the prose rules in COMMON.md, including no process artifacts.

**Coordination.** Another agent is doing a register pass on Chapter 1 at the same time. Edit only the three limitbox blocks and their immediately adjacent sentences, with exact Edit replacements, re-reading each region first.

**Build** into /tmp/build-limits. Report the 3 figures and the build status. Do not commit. Final message ≤ 6 lines.
