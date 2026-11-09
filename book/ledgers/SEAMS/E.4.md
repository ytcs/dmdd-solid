# SEAM: E.4 Density-functional perturbation theory in practice

Length (detex): appE/E-4.tex 4,245 words (budget 5,000; equations dropped by detex; not padded). Build: clean in /tmp/build-E-b
(wrapper: preamble + appE header + E-1..E-8 inputs; 0 LaTeX errors, 0 undefined citations from E.4–E.6, no overfull boxes in E-4..E-6).
Undefined refs: only to unwritten sections/appendices (Chaps. 3–17, App. C.18, E.9). Lint: 1 hit (EQ-PUNCT false positive in a cases
environment) + long-sentence notes. Sources: sources/E-b/ (cond-mat_0012092 Baroni RMP, 1803.05462 Poncé 2018, 1202.3454 Noffsinger,
1112.5411 Marzari RMP; text only, PDFs deleted). Bib added: baroni2001phonons, ponce2018towards, noffsinger2012phonon (+ E.5/E.6 keys).

## The reader now knows
- What one DFPT run returns per Q: screened ∂_{κα,Q}V_KS (eq:E.4-sth projected Sternheimer, Baroni Eqs. (30)–(31), Giustino Eq. (48);
  eq:E.4-dV), D^dyn(Q) via 2n+1, and at Q = 0 ε∞, Z* (eq:E.4-rcomm commutator, Baroni Eq. (37), (44)).
- HL forms ε∞ = 1 + ∂P/∂ℰ, eZ* = Ω∂P/∂u = ∂F/∂ℰ (eq:E.4-epsZ; Baroni (94)–(96) Gaussian); nonanalytic term in HL (eq:E.4-na; Baroni (98)).
- Berry-phase P_el (eq:E.4-berry, Marzari Eqs. (89)–(90)), quantum eg_degR/Ω, finite differences ±δu.
- LO–TO check ω_L² − ω_T² = e²Z*²/(Ωε∞μ_red) (eq:E.4-LOTO, derived); error amplification 2δZ*/|Z − Z*| for near-cancellations (→ 11.8).
- Overscreening direction from KK (eq:E.4-kk); Si DFT ε∞ 12.89 (Poncé 2018) vs book measured 11.7; Poncé rescales to its adopted 11.94; reconciled with E.1's PBE 13.04 (we:E-si-bands).
- IFC interpolation (eq:E.4-ifc, Baroni (99)), 2–3 bond-length rule, Si ⟨110⟩ long-range IFCs; dipole subtraction; ASR as diagnostic;
  cost scaling frozen 3N R⁹ vs DFPT 3N⁴R³ (Baroni Sect. IV.B).
- B_κ from DFPT phonons (eq:E.4-B); Γ-cell error (eq:E.4-dBgamma, derived): N_Q⁻² at T = 0, N_Q⁻¹ at T > 0; Si 8³: 3.6e-4 Å² (300 K, c = 6 km/s), 1.9e-5 Å² (T = 0).
- Beyond-density state changes for transition amplitudes (eq:E.4-drho, eq:E.4-dpsi): occupied part of ∂ψ_v (sum over valence; cancels in density;
  singular at valence crossings → dynamical denominators of 13.2/13.6); empty-state equation (eq:E.4-dpsic), indefinite; window + projected
  positive-definite remainder (eq:E.4-dpsiperp, derived). Frequency-dependent Sternheimer (eq:E.4-sthw) for 12.5 and E.3.
- Elastic constants: three routes, relaxed ≤ clamped, Voigt shear-row ordering pitfall.
- WE E (we:E-dfpt-si): published Si settings (Noffsinger 35 Ry/14³/6³; Poncé 35 Ry PBE, 6³ q, 18³ k for Z* → 0); Z* = 0 by inversion + T_d + neutrality.
## Symbols introduced (with defining equation)
- a_sh (Sternheimer shift, eq:E.4-sth); P̂^occ_{k+Q}, P̂^deg_c, P̂^⊥_𝒲; 𝒲 (band window, eq:E.4-dpsiperp); N_Q (Q-grid size); Q_c (Γ-sphere radius,
  eq:E.4-dBgamma); c_ν (acoustic sound speed per branch); ΔB^{αα}; ∂ψ^±_v (eq:E.4-sthw); C_ij (Voigt elastic constants); 𝔗 written inline as \mathfrak{T}
  (propose a macro \Tlabel).
## Terms introduced
- projected Sternheimer equation; nonanalytic term (HL form); Berry-phase polarization (practical); Γ-cell correction; empty-state Sternheimer;
  Sternheimer remainder; frequency-dependent Sternheimer; clamped/relaxed elastic constants; shear-row ordering.
## Threads: opened / advanced / closed
- T4 (Born–Oppenheimer hierarchy): advanced (DFPT at n_B = 0, n_A = 0 placement).
## Promises made to later sections
- 13.2/13.6: the adiabatic ∂ρ fails at valence crossings; dynamical denominators there. 11.8: test Z*, ε∞ against eq:E.4-LOTO.
- E.5 uses eq:E.4-dpsiperp for the intermediate-state remainder.
## Open questions for the editor
- Measured Si ε∞: E.4 cites 11.94 (Poncé 2018, public); E.1/E.3 use 11.7 (no public source seen in their text). One book value is needed.
- E.8 uses γ_Qν for Grüneisen parameters, which clashes with the linewidth γ_Qν (NOTATION 5.7). E.4 now points to E.8 for the Grüneisen relation.
## Proposed ledger rows (the editor merges them)
NOTATION: a_sh | Sternheimer shift (> valence bandwidth) | eV | E.4 · N_Q | phonon-grid size per direction | 1 | E.4 · Q_c | radius of the Γ-cell
sphere | eV | E.4 · c_ν | sound speed of acoustic branch ν | 1 | E.4 · 𝒲, P̂^⊥_𝒲 | band window and projector on its complement | — | E.4 ·
GLOSSARY: projected Sternheimer equation; Sternheimer remainder; Γ-cell correction · CONCEPTS: DFPT practice (E.4) after 5.4, 5.5, 5.6, 6.2 ·
CLAIMS: Si DFT ε∞ 12.89 [cited Poncé 2018]; book value 11.7; Si DFPT k 18³ for Z* → 0 [cited]; Γ-cell error scaling [derived]; eq:E.4-LOTO [derived] ·
INDEX: density-functional perturbation theory; Sternheimer equation; Born effective charge; Berry phase; acoustic sum rule; force constants; elastic constants.
