# SEAM: E.14–E.17 (computational specifications: phonon-assisted recoil, excitons and core states, electronic response libraries, lattice libraries)

Files: tex/appE/E-14.tex (≈4,100 wc), E-15.tex (≈2,400), E-16.tex (≈3,300), E-17.tex (≈3,650); wc counts include LaTeX. Budgets 3,000 / 2,000 / 2,500 / 3,000.
No App. D files. Inputs inserted in appE.tex after E-13. Bib appended (Crossref/arXiv-checked DOIs): macfarlane1958fine, liang2025plasmon (2401.11971),
togo2015distributions, deinzer2004two, kapil2019ipi.

## The reader now knows
- E.14: L^PA(q,ω) on (|q|, q̂, ω) bins (0.25–1.25 Å⁻¹, 30 directions); 𝔗 = n_B 0, n_g 2, n_T 0, 𝒦 one phonon, 𝒳 RPA+LF; parameter table tab:E14-params;
  controls (optical limit vs EPW ε₂^PA and Macfarlane 20 K; g → 0; frozen phonon at X vs adiabatic form; soft acoustic; symmetry zeros; GaAs direct-gap control);
  zero-phonon side on common bins (mirror-plane cones, second heavy-hole cone, X-face (2̄00) edge; Wannier–Mott with anisotropic μ(Q)); onset verification
  route (two lattice constants, second pseudopotential family, direct DFPT at Q*, neutron-scaled TA; 0.3 meV ↔ 8.5×10⁻⁵ MeV); Ge (HSE06+SOC, 6³ DFPT, TA
  deficit test), GaAs, other indirect-gap crystals; f-sum check with the truncation remainder computed exactly (eq:E.14-remainder) and δ_NL separately; costs.
- E.15: BSE with coupling vs TDA (one-oscillator estimate eq:E.15-tda: ×2 overstatement at 0.7 Å⁻¹); bound lines from effective mass because 24³ cannot
  resolve a_x ≈ 4.9 nm; exciton dispersion eq:E.15-disp; replicas and the 1D exact-diagonalization completeness test; exciton lines for Migdal; STE Poisson line
  (eq:E.15-ste); core-level ZORA+SOC; Ge SOC mixing.
- E.16: 12-function response library + exported R⁰_GG′; current screening by mixed blocks; triplet ladder; cubic-harmonic components (Lebedev 110→230→434);
  local fields in the window (1D model, supercells n = 2, 3, 4 with their resolved |q|, proxy eq:E.16-dLF); candidate loss functions; orbit–orbit f-sum shift;
  relaxed static step eq:E.16-step (Ω_P,e = 0.51 eV for Si, checked); kinetic row eq:E.16-TT; boosted-dark-matter recast (density row ×(1 − ω²/q²)², transverse row).
- E.17: harmonic base; strain deformation tensors; multiphonon tables; coherent two-phonon via eq:E.17-Bkk and eq:E.17-Wn; lattice anisotropy; valence deformation
  and core polarization; contact-density factor; PIMD momentum distributions; isotope Hessians and T = 0 two-phonon ε₂; Z*(ω); GaAs near-cancellation with LST
  (eq:E.17-lst; Z/M values 0.4446/0.4405 and d = −1.33×10⁻³ rechecked); candidate batch (tab:E17-batch), elastic tensors, lifetimes (n_A = 2 per ruling), thermal contraction.

## Symbols introduced (with defining equation)
- 𝔚^(n)(q): ω-integrated n-phonon weight (eq:E.17-Wn). δ^coh_n(q) = 𝔚^(n)/𝔚^(n)_inc − 1 (E.17). Chosen to avoid ℛ_n (rate with n pairs, 1.5).
- B_κκ′(ΔR): static displacement correlation tensor, B_κκ(0) = B_κ (eq:E.17-Bkk).
- 𝒢_GS(q), Z^(e)_κ(q), ε_cl(q), Ω_{P,e} (\varOmega_{P,e}) electron "plasma" scale of the relaxed static step (eq:E.16-step).
- Λ(q) = |M̃|²/|M|² screening ratio; δ_LF, δ_pair; δ_LF^(0) (eq:E.16-dLF); ε_mac used as 1/(ε̃⁻¹)₀₀ (existing row).
- P^⊥_N, φ (E.14 f-sum remainder; local).
- S_HR, ω̄ Huang–Rhys factor and mean phonon energy (eq:E.15-ste); E_x(Q), μ(Q) (eq:E.15-disp).
- d, v_κ (GaAs near-cancellation, local to E.17); μ_red (pair reduced mass, existing family).
- Used: L^PA, m_min^PA, m_min^ZP, δ_w, E_min, E_x^b, a_x, μ_x, W^scr, R⁰_GG′, R̃, 𝒯_e, S_ℓ, x_R, B_κ, W_κ, 𝒞_κκ′, Γ_iso, Z*_κ, ε_∞, ρ_T, q_BZ, c_ν, B.

## Terms introduced
- phonon-assisted output grid / common bins; resonant (Tamm–Dancoff) form vs full coupling; response library; mixed (density–current) block; relaxed static step;
  kinetic-energy row; coherence correction; contact-density factor; harmonic base (shared lattice input).

## Promises / pointers
- E.14 → 13.2, 13.3, 13.4, 13.6, 13.7, 13.9 (all numbers taken from SOTA "R17 final state" as 13.9 will state them); E.5 for the route; E.16 for supercell LF; E.17 for GaAs Z*.
- E.15 → 10.5, 10.6, 12.3, 13.8 (+ E.18 Migdal path, 18.5 for STE relaxation).
- E.16 → 10.2, 10.4, 10.6, 10.7, 10.9, 11.7, 13.9 (via 13.4), 21.6, 21.7; also 4.3 (mass–velocity 1.8×10⁻³; consistent with δ_rel ≈ −0.23 % TF).
- E.17 → 11.1–11.4, 11.6, 11.7, 11.8, 12.5, 12.6, 17.5, 21.6, 21.7; E.18 for (1 − P_Mig).
- Undefined references in a full build are only to unwritten sections (Chaps. 8–21, E.18–E.21).

## Writer-only placement of the planning items (not book text)
E.14: DC-1, 2, 3, 4, 8, 97 placed; DC-5 (vertex 0.150) and DC-6 vertex part reported as computed, DC-6 remainder placed as the zero-phonon side on common bins;
DC-7: LE-27 part done (reported), finer q̂ search folded into the joint-minimum consistency requirement; SOC LA-kink folded in E.15 (SOC section).
E.15: DC-9, 10, 11, 12, 13, 16 placed. E.16: DC-14, 15, 17, 28, 39, 40, 54, 88 placed. E.17: DC-18, 19, 20, 21, 22, 23, 29, 33, 34, 35, 91–96, 98 placed
(DC-91/92/95 cutoffs table; DC-93 CsI; DC-94 magnetic; DC-96 lifetimes; DC-98 contraction).

## Open questions for the editor
1. E.14 is over budget (~4,100 incl. LaTeX); the onset-verification, Ge/GaAs and f-sum passages are what the 13.9 open rows require. Trim candidates: the GaAs paragraph.
2. Cost conversions follow the planning ledger rule (CPU-h read as core-h; "h on 4 cores" ×4). Two figures are my order-of-magnitude estimates and say so:
   core-level BSE (~10³ core-h) and candidate loss functions (10–10² per two-atom cell).
3. E.16 states the orbit–orbit term only in words (the formula belongs to 10.6).
4. "Kapil et al." bib entry abbreviates the author list with "others".

## Proposed ledger rows (the editor merges them)
NOTATION: 𝔚^(n)(q) | ω-integrated n-phonon weight per cell | 1 | E.17 · δ^coh_n(q) | coherence correction of the n-phonon weight | 1 | E.17 · B_κκ′(ΔR) | static displacement
correlation, B_κκ(0) = B_κ | Å² | E.17 · Z^(e)_κ(q) | electron-following charge | e | E.16 · 𝒢_GS(q) | lattice part of the relaxed static step | 1 | E.16 · Ω_{P,e} |
e²𝓃_e²/ρ_T scale (all electrons) | eV | E.16 · Λ(q), δ_LF, δ_pair | screening ratio and local-field/pair corrections of L^PA | 1 | 13.4/E.16 · S_HR, ω̄ | Huang–Rhys factor,
mean phonon energy | 1; eV | E.15 · μ(Q) | pair reduced-mass tensor at total momentum Q | m_e | E.15.
GLOSSARY: resonant (Tamm–Dancoff) approximation; response library; coherence correction; contact density; kinetic-energy row.
CONCEPTS: f-sum truncation remainder as one Hamiltonian application (E.14); TDA overstatement of the screened loss function (E.15); triplet = singlet ladder to (a/a_x)³ (E.16);
GaAs near-cancellation needs LST, not DFPT (E.17).
CLAIMS: eq:E.14-remainder [derived]; eq:E.15-tda [derived, one oscillator]; Si Ω_P,e = 0.51 eV, 3×10² at 1 keV [derived/estimate]; d = −1.33×10⁻³, +41% [derived];
onset shift 8.5×10⁻⁵ MeV per 0.3 meV [derived]; all costs [estimates from measured pilots or scaling].
INDEX: phonon-assisted electron recoil (computation); Tamm–Dancoff approximation; exciton–phonon replica (computation); self-trapped exciton; orbit–orbit interaction;
relaxed static response; kinetic-energy density (scalar absorption); multiphonon tables; coherent two-phonon; isotope disorder (Hessians); Born charge, dynamical;
Lyddane–Sachs–Teller relation (GaAs); quasi-harmonic thermal contraction; path-integral molecular dynamics (momentum distribution).

## Revision (2026-11-02, App. E.14–E.27 review)
- Shared lattice setting book-wide: PBE, SG15, 60 Ry, measured a (Si 5.431, Ge 5.658, GaAs 5.653 Å); Si 12³ k / 8³ q, Ge and GaAs 8³ / 6³; 80 Ry check for 3d. Costed once in E.17 (Si ≈ 100, Ge ≈ 15, GaAs ≈ 20 core-h); E.14, E.18 and later sections point to it. Neutron tolerance per branch: optical/LA 3 %, Si TA 10 % (8 % soft, 5.2), Ge TA 15 % pending the 12³-k test.
- E.14 rewritten (argued prose; content headings; no Cost/Pitfalls sections; costs in tab:E14-params). Absorbs the GaAs Fano map formerly in E.26 (subsection "Fano widths and detunings in GaAs"; 90 Ry FR spinors as the one stated departure from the base). Window quantities distinguished: PAER onset 0.3332/0.3374 MeV; first ZPL edge 0.405–0.408 (0.407), glide class, small vertex; second heavy-hole cone 0.415–0.420; allowed-size (2̄00) X-face edge ≈ 0.50 MeV. Neutron-scaled onsets 0.3333/0.3375. Density vertices ≈ 10⁶ diagonalizations, 200–300 core-h; plane-wave total 350–450 core-h; amplitude per E.5 (10¹⁶ ops). Sternheimer remainder a correction below ≈ 1.9 keV, full on 1.9–2.5 keV. GaAs scissor targets T → 0: Γ 1.519, L 1.815, X 1.981 eV (vurgaftman2001band). Ge window 80–240 core-h.
- E.15: ×2 overstatement belongs to the resonant-only form (symbol ε₁^res, not ε₁^TDA, in eq:E.15-tda); retarded TDA error ≈ 10 % on ε₂; pass test |S^TDA/S^full − 1| ≤ 0.15 at 0.5–1.4 keV. Mass–velocity f-sum shift (−0.58 %, Ge) tested crystal vs atomic (E.16). STE ≈ 10⁴ core-h. Exciton Migdal 2–3×10³ core-h.
- E.16: library cost ≈ 10³ core-h (Si), R⁰_GG′ stored on a coarse subset (≈ 10 GB; full grid would be ≈ 600 TB), Dyson by iterative solve. 4 Ry ≈ 37 G. 𝒯_e = p²/2m_e² stated.
- E.17: title "Lattice libraries". S per cell in eV⁻¹ = Ω × per-volume S (eV²); 𝔚^(n) now dimensionless per cell (1/Ω dropped). Charge vertex ≈ 725 G (Si), 821 (Ge, GaAs) per Q. Batch table without GaAs, with the remaining batches (DC-92, 94, 95, 98).
- NOTATION change proposed: 𝔚^(n)(q) units 1 (per cell), not 1/Ω. ε₁^res (resonant-only) local to E.15.
