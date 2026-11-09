# Chapter 3 mock-reader review: personas (b) and (c)

Read: tex/ch03/s3-1…s3-6, appC/C-1…C-8, appD/D-4, D-5. build/main.pdf (Nov 1 23:46) predates every source, so I read the
.tex. C.15 and C.17 are pointed to but outside my brief, so I took their claims on trust. Figs. 3.6–3.8 judged for pedagogy only.
I checked the numbers in sympy/numpy: every derived quantity I recomputed agrees to the quoted digits unless listed below.

## Persona (b): particle physicist, QFT, no solid state

**3.1 Lattices and reciprocal space**
- Lost: none.
- Not reproduced: the (200) "glide" extinction for every symmetric function (C.17, not in my set). I took it on trust.
- Before defined: none. "Miller indices" and "Bragg" are glossed in place.
- Pace: the cross-product algebra (b_i, BZ volume) is slow for me but harmless. The two Fourier conventions slow me down:
  f(r)=Σ f_G e^{−iG·r} here, c(G) multiplying e^{+iG·r} in 3.2. The one-clause reconciliation in 3.2 works, but it is friction.
- Outcomes: yes. I built b_i for fcc and confirmed q=(2.2,0.5,0)(2π/a) → G_q=(2,0,0), |q_r|=1.23 keV, q_r inside
  |kx|+|ky|+|kz|≤1.5. I reproduced S^bas(200)=0, (111)=1−i, GaAs 31−33=−2, and 13 101 G-vectors inside 2m_χv_max at 10 MeV.

**3.2 Bloch states and band structure**
- Lost: §TB end: "This bond charge … provides the potential of silicon with its (200) and (222) components" contradicts
  we:3-diamond ("(200) … forced to vanish for every function with the symmetry of the crystal"). As a non-specialist I cannot
  tell which statement is right. I checked with bond-centred charges at (a/8)(±1,±1,±1) (4 bonds/cell): Σe^{iG·b}=0 at (200)
  and −4i at (222). So 3.1 is right, and 3.2 (and 3.4, below) should say (222) only. The NFE paragraph's "for spherical atomic
  potentials U_{G200}=0" understates this: it is zero for any crystal potential.
- Not reproduced: none.
- Before defined: none.
- Pace: good. The two proofs of Bloch's theorem are welcome.
- Outcomes: yes. I diagonalised the 25-plane-wave 1D model: edges 0.7515/1.7491 eV, gap 0.9976; second gap 0.0964;
  |ρ21| = 0.0225/0.210/0.496 at q = 10/100/377 eV against optical 0.0225/0.225/0.848. Umklapp |ρ_m1|² = 0.298, 0.251, 0.226,
  0.225 with closure to 1e-15. The transition energy at q=377 eV is 1.62 eV, which needs q ≥ 0.611 keV, as stated.

**3.3 Silicon, germanium and GaAs**
- Lost: Fig. 3.6 caption against eq:3.3-Edir. E_dir is defined as the *minimum* vertical gap, yet the caption labels Γ (3.42 eV)
  as E_dir while giving the model's smallest vertical gap as 3.12 eV at L. Which value is E_min(q=0) in panel (b)? (Pedagogy
  only. I did not judge the numbers.)
- Not reproduced: m_dv = 0.50 m_e "from the spherically averaged heavy and light holes" comes with no recipe. My guess
  (⟨m_hh⟩^{3/2}+⟨m_lh⟩^{3/2})^{2/3} gives ≈0.55. The Luttinger 4×4 result eq:3.3-holes is quoted, not derived; the cited
  limits check. Kane: 1+18.3/1.42 gives m* = 0.0720, not "0.0718" (the input digits are probably rounded).
- Before defined: "semilocal functional" and "quasiparticle correction" (§3.3 ¶ after Fig. 3.7, before 3.4); "donor
  electrons", "cyclotron resonance"; ε∞ (forward ref to 4.4 given).
- Pace: the Luttinger paragraph is too fast for me. The rest is right.
- Outcomes: yes. n_i(300 K) = 6.1e9 cm⁻³, 1.0e-20 at 77 K, 10^−720.7 at 4 K. The Kane-SO formula gives 0.0660/0.0246/0.0755
  for gaps 1.52/0.5/1.77 eV. The k_c threshold gives 0.474 MeV. For Ge, 1898²/[2(5.03−0.744)] gives 0.420 MeV. The Luttinger
  masses in Table 3.1 follow from the listed γ's.

**3.4 Many electrons and DFT**
- Lost: same (200) issue. "A sum of identical spherical atoms has no components at G200 and G222 … the charge piled up between
  neighbouring atoms gives V_KS exactly these components." Only G222.
- Not reproduced: none. I derived the scissor rescaling 1+Δ/(ε_c−ε_v), the HF-gas numbers ε_x = −6.22 eV, band 12.47 → 20.76 eV
  and v_x = −8.29 eV, and the threshold masses 0.148/0.171/0.313–0.367/0.333 MeV and 0.407 MeV.
- Before defined: G₀W₀ / W^scr / "Coulomb-hole term" (forward refs, acceptable).
- Pace: HK → KS → Janak → derivative discontinuity is fast in the main text. D.5 rescues it.
- Outcomes: yes. I can state the band-gap problem and repair a velocity under a scissor (3.12/2.55 → ×1.50 in |v|²).

**3.5 Plane waves, pseudopotentials, core states**
- Lost: none.
- Not reproduced: none. I checked eq:3.5-logder (sign included), the PAW cross-term argument, E_cut = 113 Ry → 5513 plane waves,
  1800 Ry → 3.5e5 plane waves, shell thresholds 28.6/43.0/524 MeV and q ≥ 38.0/57.0 keV, and Ge 3d at 8.5 MeV and 11.2 keV.
- Before defined: none.
- Pace: the Dirac → Pauli reduction is familiar to me but well done and convention-fixing. Not condescending.
- My field: correct. I checked ⟨H_mv⟩ = −(5/8)(Zα)⁴m and Darwin +(1/2)(Zα)⁴m, giving −(Zα)⁴m/8, the Dirac 1s term. The Thomas
  factor comes out right, and the 2p splitting α⁴m/32 = 0.366 cm⁻¹ agrees with experiment. Small point: 4.7/1781.2 = 0.264 %,
  not "0.27 %".
- Outcomes: yes. I can size a cutoff for a given q_max and say which shells open at which mass.

**3.6 Wannier functions**
- Lost: none.
- Not reproduced: the stationarity condition eq:3.6-stationary is quoted, not derived (it is cited, and nothing later needs it).
- Before defined: "Wigner–Seitz cell" (3.1 defines the BZ without naming the construction), "Chern invariants",
  "Foster–Boys". "Matrix of rank eight" / "matrix of rank N_W" should read "8×8" / "N_W×N_W", since H^W(R≠0) can be singular.
- Pace: the disentanglement paragraph is dense but followable.
- Outcomes: yes. I reproduced the two-band chain: |H^W(R)| = 2.192, 0.468, 0.0525, 0.0120 eV; one-WF interpolation errors 51 meV,
  4.75 meV (text "4.8"; 4.747 rounds to 4.7), 0.64 meV and 2.4 µeV for n_k = 4, 8, 12, 24; two-WF error 2e-15 eV for n_k ≥ 3 and 0.242 eV at n_k = 2;
  |∂H/∂k|_{+−} between 0.274 and 1.000 eV a.

**Appendices C.1–C.8, D.4, D.5**: I checked the derivations, including the central lobe 90.3 %, the Lorentzian test
1 − Γ/2 + Γ²/4, the Bogoliubov 0.8/−0.2/0.125, the cubic-harmonic norm 16/525, the r³e^{−βr}j₁ integral, the Matsubara example,
and the D.4 antiderivative and ⟨F_L⟩ = 3/4. All correct. D.4 cites sec:4.2 for k_F and E_F where Ch. 3 cites sec:2.5 for the
same numbers.

**Condescension (b):** none found. The QFT-adjacent material (Dirac reduction, the photon q = ω, HL units with α = e²/4π)
is correct and stated without talking down.

**Overall (b).** I would keep reading. Every step that matters for a rate I could redo, often to the last digit. What stopped
me was the internal contradiction about the (200) component (3.1 against 3.2 and 3.4), which a careful outsider cannot settle
from the text. The other items are small label and recipe gaps.
**Verdict (b): MINOR GAPS.**

## Persona (c): condensed-matter theorist, DFT and many-body, no dark matter

**3.1**
- DM side: the q_r/G_q split and "the momentum transfer is never folded" are clear. v_max, v_min and F_DM come from Ch. 1
  and are adequately recalled.
- Lost / not reproduced: none.
- Pace: slow for me but appropriate for persona (a). No condescension.
- Outcomes: yes.

**3.2**
- My field, error: the (200) bond-charge claim (see (b) 3.2). For Fd-3m the d-glide forbids h00 with h = 4n+2 for any scalar
  lattice function. (222) is only site-symmetry "forbidden" and appears through the bond charge.
- Lost: none.
- DM side: the statement that DM momenta sit at or beyond the edge of the optical limit (|v_mn| vs v_max) is a nice bridge,
  clear to me.
- Pace: NFE and tight binding are slow for me but right for (a).
- Outcomes: yes (see above).

**3.3**
- Lost: none. The E_min(q) and threshold-mass logic is new to me and fully followable from eq:1.3-region.
- Not reproduced: m_dv = 0.50 (as for b).
- My field: values and attributions are sound (Hensel masses, Luttinger γ's, Δ_SO, Kane-SO). The Fig. 3.6 E_dir label is a
  pedagogy item (as for b). Table 3.1 mixes room-temperature a for Si with 0 K a for Ge/GaAs; the caption discloses it, but it is
  worth one clause.
- Outcomes: yes. With the measured valley data I can bound the zero-phonon threshold (0.333–0.474 MeV) and explain the
  phonon-assisted window.

**3.4**
- My field, error: the (200) claim again ("gives V_KS exactly these components").
- My field, otherwise accurate: Koopmans in a crystal (1/N relaxation), Janak, the straight-line theorem, Δ_xc per Godby et al.,
  the screened-exchange picture, the scissor velocity theorem and its f-sum corollary.
- DM side: we:3-mmin-gap ("halo supply grows by orders of magnitude over a factor of two in mass") leans on §1.3. I accepted it
  but could not re-derive it here.
- Outcomes: yes.

**3.5**
- My field, imprecise: "The generalization to two or more reference energies per channel, due to Vanderbilt and used in
  Hamann's optimized potentials, requires the overlaps … to agree for every pair." Vanderbilt (1990) introduced the
  multi-reference scheme precisely to *relax* that condition (ultrasoft, with augmentation charges). Generalized norm
  conservation is the constraint Hamann imposes in ONCV. Suggest: "…due to Vanderbilt; Hamann's norm-conserving version keeps
  the overlaps … equal".
- My field, otherwise correct: Phillips–Kleinman, HSC, KB, the PAW vertex (eq:3.5-rhoAE), core binding energies, Ge 3d semicore.
- DM side: "heavy mediator, unlike a light one, does not suppress them" relies on F_DM from §1.4. That is fine.
- Outcomes: yes.

**3.6**
- My field, overstatement: "Both sets are real, as the functions at a minimum must be in a crystal with time-reversal
  symmetry." Realness of MLWFs is a Marzari–Vanderbilt conjecture, observed and not proven in general. "Are found to be" is
  safer.
- My field, surprising: Fig. 3.11 and the text assert that the lower-spread disentangled minimum has its main lobe pointing
  *away* from the bonds (toward the empty tetrahedral site), with bond-directed hybrids a less localized stationary point
  (19.8 vs 16.2 Å²). That is the opposite of the familiar picture. It may well be right for this window, but it needs one sentence
  of reason or a cross-check pointer (Fig. 3.11 is not among the regenerated figures).
- Consistency: Fig. 3.12 caption puts the PBE CBM at 0.85(2π/a) and §3.4 says 0.840. "Rank eight" (as for b).
- My field, otherwise correct: the gauge rule and the aliasing argument; the claim that the interband velocity needs
  r-matrix elements; the polar long-range split.
- Outcomes: yes (two-band chain reproduced, above).

**Appendices**: correct. D.5's v-representability caveat and Levy constrained search are properly stated.

**Condescension (c):** none. Material I know (3.1–3.2, D.4–D.5) is pitched for (a) without talking down. The phrase "The material
is standard" sets the tone well.

**Overall (c).** I would keep reading. The DM kinematics woven into each section (E_min against qv_max − q²/2m_χ, shell opening
masses, cutoff from q_max + p_f) are exactly what a CM reader lacks, and they are derived rather than asserted. There are four
items in my own field to fix: the (200) bond-charge claim (3.2, 3.4), the Vanderbilt attribution (3.5), "must be real" (3.6), and
an unexplained Wannier-function orientation (Fig. 3.11). None blocks the later material.
**Verdict (c): MINOR GAPS.**
