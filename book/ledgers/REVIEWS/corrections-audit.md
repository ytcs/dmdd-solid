# Corrections audit: book tex against state/CORRECTIONS.md and state/SOTA.md

Scope: tex/ch01–ch08, ch10, ch11, appC, appD, appE. Read-only (no tex edited). Date 2026-11-02.
Method: each S item of CORRECTIONS (§1–§20) turned into a grep signature (old value, factor, formula fragment
or symbol); context read only on hits. §0 renames grepped and checked against book/NOTATION.md. SOTA.md
REFUTED/FALLS/WITHDRAWN entries grepped. Ch12/ch13 (PAER window, Migdal E^Mig_3, Si TA onset) are out of scope.
Severity: S = a formula, factor or claim the campaign has superseded; N = notation; W = wording.

## Findings

### F1 (S) Gapless decomposition bound asserted for U_qp = 1: withdrawn claim
- ch08/s8-6.tex:200, last sentence of the paragraph after eq:8.6-bin:
  "Without any dressing, $U_{\mathrm{qp}} = 1$, the bound still holds, with $\mathfrak{h}_{\mathrm{off}}^2$ bounded by
  the zeroth moment of the Fan--Migdal spectral function, the sum $N^{-1}\sum|g_{mn\nu}|^2(2n_{\vect{Q}\nu} + 1)$ ..."
- appD/D-28.tex:97 (derivation): "Without any dressing, $U_{\mathrm{qp}} = 1$, the diagonal part $H_{\mathrm{d}}$
  conserves the bare numbers, a one-quasiparticle state stays one ..., and
  $\mathfrak{h}_{\mathrm{off}}^2 \le \max_{n\vect{k}}\langle n\vect{k}|H_{\mathrm{off}}^2|n\vect{k}\rangle$ ..."
- Superseded by: CORRECTIONS §19.4 (WP4-v3 OW4-1, CW3-errata §2.2 item 22); SOTA l.567 "(G5′) with U_qp = 1
  WITHDRAWN (FALLS)". With U_qp = 1 the disconnected term c†H_off|FS⟩ (H_off acting on the Fermi sea, not on the
  probe's quasiparticle) makes 𝔥_off extensive; the D-28 step treats only the one-quasiparticle state.
- Replacement: delete the U_qp = 1 sentence (s8-6:200) and the U_qp = 1 derivation (D-28:97). State: "(G5′) with
  U_qp = 1 fails: H_off acting on the Fermi sea makes 𝔥_off extensive. The open item is the connected bound
  (G5′-c), which needs a dressed vacuum (U_qp) and a commutator bound uniform in N; its connected size is [E]
  ≈ 0.2 eV (Al), at most λ_max of the Fan–Migdal zeroth-moment band matrix." s8-6:222 already lists the
  existence of U_qp as open ("Third, ..."); add the connected (G5′-c) bound to that list.

### F2 (S, soft) Fano term "vanishes" in Si/Ge without the degenerate-manifold qualifier
- ch08/s8-6.tex:188: "In many crystals the Fano term vanishes. ... every matrix element and every off-shell
  amplitude is real, and $\Imag(\rho_m^*\mathcal{A}^{\mathrm{off}}_\nu) = 0$ ... Silicon and germanium satisfy the
  hypothesis, with or without spin--orbit coupling."
- appE/E-14.tex:72: "The term vanishes in crystals invariant under inversion combined with time reversal with an
  even electron number, such as silicon and germanium, but not in GaAs."
- appD/D-28.tex:79 half-acknowledges it ("degenerate pairs need the matrix form of the same algebra"); D-28 §"Real
  amplitudes under PT" (l.93) proves reality in a PT-invariant basis but not that this basis also diagonalizes
  the level-shift matrix of a degenerate X0 manifold.
- Superseded by: CORRECTIONS §19.1 (WP0-v3 §6.2 (iv″b), CW3-errata §2.2 item 5) and §19.3 (WP3-v3 §M4, item 6).
- Replacement (add after "with or without spin--orbit coupling"): "... at the level of one-body self-energies,
  whose level-shift matrix is scalar on each degenerate (Kramers or irrep) zero-phonon manifold [D]. Level shifts
  from the electron–hole vertex can split such a manifold in a basis that is not PT-real; then only the branch
  sum Σ_b 𝔉_b = 0 survives, not each 𝔉_b." Same qualifier in E-14:72.

### F3 (S) Germanium zero-phonon reach set by the L valley; the direct Γ route at ≈ 0.25 MeV is dismissed
- ch03/s3-3.tex:217 (we:3-mmin): "Depositing \SI{0.744}{eV} at $q = \SI{1.90}{keV}$ requires
  $\mchi \ge ... = \SI{0.420}{MeV}$, twice the naive bound. Germanium's smaller gap buys less reach than its value
  suggests, because its valleys lie as far out in the zone as those of silicon."
- Same paragraph: "The direct gap matters for photons and for absorbed dark matter, not for the threshold of
  scattering", said of Si and implicitly extended to Ge.
- Superseded by: SOTA l.328 and l.342 (REF-WP1-B/A, FALLS: pinning q at the valley momentum is wrong; "Ge:
  zero-phonon via the direct Γ valley at 0.256 MeV"); CORRECTIONS §20.1 (COMP-PH Ge §6.2, DC-2): Ge thresholds
  need the joint (q,k) minimisation, and parabolic brackets are unreliable. In Ge the Γ minimum (0.89 eV, the
  book's own number at s3-3:40) is 0.15 eV above L and reachable at q ≈ 0.67 keV, so it, not L, sets the
  zero-phonon floor (the book's own table gives 0.253 MeV).
- Replacement: "In germanium the conduction minimum at Γ lies only 0.15 eV above the L valleys and needs no large
  momentum transfer, so zero-phonon pairs open near 0.25 MeV through the Γ valley, not at the 0.420 MeV that the
  L valleys alone would need; the joint (q, k) minimisation of §13.1 settles it." Drop "Germanium's smaller gap
  buys less reach than its value suggests".

### F4 (N) "Debye–Waller" used for the Allen–Heine term in a subsection title
- ch06/s6-3.tex:5: "\subsection{Fan--Migdal and Debye--Waller terms}"
- CORRECTIONS §0 row 5 ("Debye–Waller" for the AH tadpole → AH); NOTATION l.495 reserves Debye–Waller for
  e^{−2W}; s6-3:99 says the same ("to which we reserve the name"). The keyresult below (l.22) already says
  "Fan--Migdal and Allen--Heine self-energies".
- Replacement: "\subsection{Fan--Migdal and Allen--Heine terms}".

### F5 (N) Sound speed per polarization written c_s
- appE/E-12.tex:26: "$\langle c^{-3}\rangle = \tfrac13\sum_s c_s^{-3}$ the average of the inverse cubed sound
  speed over the three acoustic polarizations $s$"
- CORRECTIONS §0 (c, c_s → c_ν); NOTATION l.483 (c_ν, sound speed of branch ν); s is the species index.
- Replacement: "$\langle c^{-3}\rangle = \tfrac13\sum_\nu c_\nu^{-3}$ ... over the three acoustic branches $\nu$".

### F6 (N, known) Carrier kinetic energies ε_e, ε_h in D.18
- appD/D-18.tex:61: "where $\varepsilon_{\mathrm{e}}$ and $\varepsilon_{\mathrm{h}}$ are the kinetic energies of
  the electron and the hole"
- CORRECTIONS §0 (ε_e, ε_h carriers → E_e, E_h); NOTATION l.599, l.758 and l.1682 already log this as "unify to
  E_e, E_h at the next touch" (ε_e collides with the electron-channel dielectric ε_e of A.7, 8.4, 10.2).
- Replacement: E_e, E_h (also 6.5 per NOTATION l.758, outside this grep's hit list).

### F7 (W) Source-notation c_s in a quoted scaling
- ch11/s11-1.tex:151: "$R \propto \sigma_n/c_s$ ... \cite[Eq.~(37)]{griffin2020multichannel}". This is a quote
  of the source's symbol, but the book's symbol is c_ν (or c̄). Optional: "$R \propto \sigma_n/\bar c$ (their
  $c_s$)".

## Checked, not a finding
- ZrTe₅ Δ_D = 15.6 meV (ch07/s7-3.tex:50, 64, 135). CORRECTIONS §19.13 (11.75 vs 11.8 meV) targets the WP8-U
  table's "Exp. [52]" attribution. The book uses the relaxed-cell column of 1910.02091 Table 1 (gap 31.2 meV),
  recorded as CLAIMS I-83, and quotes the 24–35 meV DFT spread. This is a different column, not the superseded
  number. The reviser may add "(experimental-volume DFT: 23.6 meV)" for completeness.
- ch01/s1-5.tex:42, film value 2Δ_BCS = 0.6 meV "adopted by projections", and ch07/s7-2 bulk Al 0.18 meV: matches
  CORRECTIONS §19.13 OC-11(b) (0.3 meV film-like, ≈ 1.7× bulk).

## S items verified correct in the book
- D1 §2 isotropic factor η(v_min)/(2q), not η/q: ch01/s1-3.tex:161, 170.
- D1 §2 crystal form factor 2π²/(αm_e²Ω), Ω S̄⁰ = 4παm_e²|f_crys|²/q³: appD/D-29.tex:52–66; ch10/s10-1.tex:41.
- D1 §5.2 Hadamard finite part, not PV, for the double pole: ch02/s2-4.tex:116–150 (fp 1/x²); D-28:87.
- WP0 (1.2) relativistic f-sum: Darwin and SOC drop out, only mass–velocity, −(5/3)K̄/m_e: ch04/s4-3.tex:100–105.
- WP0 (4.6) [H, n] = q·j exactly, with no (q²/2m)n term: ch04/s4-3.tex:66 (eq:4.3-continuity).
- WP0 (8.2) f-sum ∫_ℝ ωS = π n_e q²/m_e over the whole real line, not 2π: ch04/s4-3.tex:72–80.
- WP0 (8.1) additive nuisance violates positivity; power/matrix forms used: ch08/s8-8.tex:18, 79.
- WP0 (9.3) L12 ZG deterministic single configuration (not stochastic): ch06/s6-3.tex:103.
- WP0 §6.2 Theorem D needs a gap; gapless targets treated separately: ch08/s8-6.tex:5, 38, 190–202.
- WP0 Table 6.1: 2W = q·B·q in general, q²⟨u_x²⟩ only at cubic sites: ch05/s5-6.tex:23; ch11/s11-7.tex:69.
- F11 static-DFPT screening error O(ω_Q²/E_g²), not O(ω_Q/E_g): ch06/s6-2:17, s6-3:181, s6-4:47; ch08/s8-4:145,
  s8-5:45, 119, s8-8:65; ch11/s11-2:40, s11-8:97; appD/D-17:34, D-27:83.
- WP1-D6 / X2 (2.2) / F1 external weight: retarded (ε̃⁻¹)_{G0} out-state, with the advanced in-state form giving
  the same total: ch08/s8-7.tex:49–74; s8-4:137.
- CW3-errata item 3 Fano bound |ΔP| ≤ max|c^F| ≲ 0.3Γ/δ (no 2π), K_ν ≥ 0 for Γ/δ ≤ 0.5: appE/E-14.tex:72.
- 17th basis row 𝔳²_s in 𝒪₂ = v̄²n − 2v̄·j + (2/m)𝒯: ch08/s8-1.tex:64, 138–144 (written as (2/m)𝒯, equivalent).
- §19.1 §9.2(iii) static step not usable for the relaxed electron channel: ch10/s10-2.tex:95–97.
- COMP-PAER / CW1 Si window numbers: onset 0.3332/0.3374 MeV, ZPL edge 0.405–0.408 (best 0.407), second heavy hole
  0.415–0.420, allowed (2̄00) ZPL ≈ 0.50, lead to 0.42–0.43, band to 0.51 MeV: appE/E-14.tex:3, 7, 50, 56. No 0.42/0.54,
  0.547 or 0.4154 MeV found. The Si bracket 0.333–0.474 MeV in ch03/s3-3:205 defers to §13.1 and contains 0.407.
- GAP-EF / CMPMC: Si ε_eh 3.749 eV, F 0.119 used as measured validation: appE/E-13:71, E-24:13, 68. No 11.46, no
  "derived 1.61E_g", no σ_ln 0.2, no 54/175.
- AH tadpole kept distinct from the Debye–Waller factor e^{−2W}: ch06/s6-3:92–99; ch07/s7-4:88; ch05/s5-6:25 (except F4).
- 2109.08168 Eq. (3) (refuted ALP formula), 2205.02250 "peak shift", the QROCODILE "conservative" claim, the
  Elliott-weight ×3, and the "GaAs ×0.47" scalar claim: not used in scope. GaAs rigid-ion scalar rate is flagged as
  high (×8.2, ch11/s11-9:54), consistent with SOTA l.611 (high by ≈ 7–9).
- §0 renames: no hits in tex math for χ/χ⁰/χ_KS (response), Π (D2), P(Q|…), S^G, Δ_X, v_k/v_q (Coulomb),
  a_{Qν}/A_{Qν}, W_e(q)/W(ε), ε_M/ε_L, M¹_ab, Λ_f, Sommerfeld κ, 𝔄-type generator. The book uses R, R⁰, v_C, b/B,
  W^scr, ε_mac/ε_Mer/ε_Lin, Λ_D, ε_bg, c_ν and 𝒪_i per NOTATION. appD/D-17:34 "W_e(ω) − W_e(0)" is a quoted
  Giustino symbol, attributed.

## Count of real findings (S/N; W excluded)
ch01 0 · ch02 0 · ch03 1 (F3 S) · ch04 0 · ch05 0 · ch06 1 (F4 N) · ch07 0 · ch08 2 (F1 S, F2 S) ·
ch10 0 · ch11 0 (F7 W only) · appC 0 · appD 3 (F1 S at D-28:97, F2 at D-28:79/93, F6 N) · appE 2 (F2 S at E-14:72, F5 N).
Distinct findings: 3 S (F1–F3), 3 N (F4–F6), 1 W (F7).

## Revision log (2026-11-02)
- F1 → done. s8-6 (para after eq:8.6-bin): U_qp = 1 sentence replaced: the undressed bound fails (H_off on the Fermi sea makes 𝔥_off
  extensive); connected part² ≤ λ_max of the Fan–Migdal zeroth-moment band matrix, ≈ 0.2 eV (Al). "Third, …" open item extended with the
  connected bound (dressed vacuum, commutator estimate uniform in N). D-28 §Gapless: one-quasiparticle derivation recast as the connected
  part, disconnected term stated, open item pointed to 8.6. CLAIMS II-10, SEAMS 8.6 updated.
- F2 → done. Qualifier "at the level of one-body self-energies" (scalar level-shift matrix on Kramers/irrep manifolds; e–h vertex shifts leave
  only the branch sum) added at s8-6 (Fano paragraph), E-14:72, D-28 (end of PT proof). CLAIMS II-11, SEAMS 8.6 updated.
- F3 → done, with a deviation from the replacement text above. SOTA l.356 and l.374 (VER-WP1-B §R1-a, rebuttal ACCEPTED; WP1-v3 §R1, C9f)
  supersede SOTA l.328/342: 0.256 MeV is the flat-band floor 2E_dir/v_max², and the Γ route opens only near 3.1 MeV; the Ge zero-phonon
  onset is the L valley, parabolic 0.32–0.36 MeV [E], not a reliable bracket (CORRECTIONS §20.1). s3-3 we:3-mmin now states: 0.420 MeV is
  the q-pinned value (counterpart of Si 0.474), threshold between 0.212 and 0.420 MeV, located by the joint minimization of sec:13.1 (the
  parabolic 0.32–0.36 MeV is not printed, per §20.1); Γ route: 0.253 MeV floor, pair recoil ≈ 0.8 eV at 0.67 keV, opens only at a few MeV
  for parabolic bands (derived estimate; SOTA gives no public citation). "Twice the naive bound" and "buys less reach" dropped; table row
  0.253 MeV kept (correct floor). CLAIMS I-197,
  SEAMS 3.3 updated.
- F4 → done. s6-3:5 subsection title "Fan--Migdal and Allen--Heine terms". Other Debye–Waller uses untouched.
- F5 → done. E-12: Σ_ν c_ν^{-3} over the three acoustic branches ν.
- F6 → done in D-18 (all seven occurrences, eq. at l.57–58 and l.61 → E_e, E_h). 6.5 still writes ε_e, ε_h (outside this file list; open).
- F7 (W) not applied (out of scope). Build -outdir=/tmp/build-corr: 0 LaTeX errors; no new undefined references (sec:13.1 pre-existing).
