# Spine review, reader persona: Part I and Appendices

Scope: SPINE.md (design principles, front matter, Part I Chaps. 1–7, Appendices A–E) read in planned order against READER.md.
Reviewer: primary persona (a), a first-year PhD student; then secondary personas (b) and (c). Date: 2026-11-01.

## Systematic findings (stated once, not repeated per row)
1. **"→ READER.md assumed" covers items that READER.md does not list.** These are: Newtonian gravity (1.1), Galilean
   transformations (1.2, 1.3), the Born approximation and Lagrangians "at the level of special relativity" (1.4), Poisson statistics (1.5),
   identical particles and Slater determinants (2.3), the variational principle (3.4), atomic spin–orbit coupling and fine structure (3.3, 3.5),
   the interaction picture (4.1), classical small oscillations (5.2) and atomic exchange (7.1). Most are standard undergraduate material, so
   the fix is cheap. Either extend the READER.md assumed list (Newtonian mechanics, Poisson statistics, the interaction picture and Dyson
   series, elementary scattering theory) or give each item a one-paragraph refresher at its first use. Field Lagrangians must not be
   assumed: they are QFT, which READER.md excludes (see 1.4).
2. **No undergraduate solid-state physics is assumed**, so Chap. 3 rightly starts from lattices. The pace of 3.1–3.3 suits (a).
3. **Chapter 4 is the bottleneck.** Proper/improper response, local fields, TDDFT, BSE, Green's functions, Wick's theorem and diagrams
   arrive within 21,500 words, and some are used before they are defined (4.4, 4.5). Chapter 2 meanwhile spends 8,000 words (2.1 + 2.5) on
   material (a) mostly knows. Proposed rebalancing: take about 1,000 words from 2.1 and about 1,000 from 2.5, and give about 2,000 to 4.6.
4. **Known material is told at length; new material is rushed.** 2.1 (golden rule, 4,500) and 2.5 (Bose/Fermi from the grand ensemble)
   repeat (a)'s undergraduate courses. 4.6 (diagrams, 5,000) and 3.4 (HF + HK proof + KS + functionals + gap problem + GW, 5,500) are the
   least familiar material and have the smallest budgets relative to their content.
5. **Notation collisions a reader will trip on:** κ has three uses (species index in 5.2, κ_BO, κ_mix); v_F appears in 4.7 (electron gas)
   and 7.3 (Dirac); n is heavily overloaded (band index, n_e(q), n_B, n_Qν, plus 𝓃 for densities); there are two Migdals (see 6.1).
   The front-matter "List of symbols" duplicates App. B.1: keep one and point to it from the other.

## Section-by-section verdicts (persona a)

| Unit | Verdict | Missing item / problem | Proposed fix |
|---|---|---|---|
| Front matter | MINOR GAPS | "How to read" has three paths but no statement of what is assumed. Part I is about 184k words, and (a) needs to know what can be skimmed. | Add a half-page "What you need" list (the READER assumed list plus the items in finding 1) with refresher references. Add per-path skip lists at section granularity. |
| Ch. 1 start | CLEAR | Outline paragraph is fine. Physics is familiar except cosmology. | None. |
| 1.1 Evidence | MINOR GAPS | Ω_c h² needs h, ρ_crit and the Hubble rate. Freeze-out and Lee–Weinberg need the Boltzmann equation in an expanding universe (beyond-textbook astrophysics is not assumed). Natural units are used in WE 1.1 (GeV cm⁻³), but A.1 says "first 1.2". | Add a box (about 400 words) on H ∝ T²/M_Pl, Γ = n⟨σv⟩ ≈ H and the resulting ⟨σv⟩ ≈ 3×10⁻²⁶ cm³/s. Define ρ_crit and h. Change the A.1 row to "first 1.1". Outcome (iv) is then achievable. |
| 1.2 Local halo | CLEAR | The escape speed needs the idea of a gravitational potential (trivial). N_esc uses erf, which is in C.8 but not in this section's pointers. | Add C.8 to the 1.2 pointers. All outcomes are achievable. |
| 1.3 Kinematics | MINOR GAPS | WE 1.4 uses the Si gap and a 30 meV phonon before band gaps (1.5, 3.3) and phonons (5.3) exist. The plan marks them as qualitative, which is acceptable. η(v_min) in closed form is in D.1, so the outcome is fine. | Define "gap" and "phonon" in one sentence each where WE 1.4 first needs them, not only in 1.5. |
| 1.4 Models | LOST (as planned) | Outcome (i), "derive the NR potential from single-mediator exchange", needs QFT (tree-level propagator), which is not assumed. Kinetic mixing (iii) and the ALP couplings g_aee, g_aγγ need field Lagrangians. The Born approximation is treated as assumed here but derived in 2.2. | Derive the Yukawa potential from the static Klein–Gordon Green's function, which is classical field theory at undergraduate level. Present kinetic mixing as a field redefinition in a classical Lagrangian, with a half-page primer (or a new C.9). Give the NR limit of the ALP–electron coupling as a stated result. Forward-reference 2.2 for Born. With these changes the verdict becomes MINOR GAPS. |
| 1.5 Detectors | MINOR GAPS | Outcome (ii), "explain the slope" of an exclusion plot, needs rate scaling with F_DM. That comes from 1.4 but the rate formula only arrives in 2.2/4.2. Poisson statistics is not in READER. | State the scaling R ∝ σ̄_e·ρ_χ/m_χ·⟨F_DM²⟩ heuristically, with a forward reference to 4.2. Add a Poisson refresher (two lines). |
| Ch. 2 start | CLEAR | Familiar territory for (a). | Shorten (see finding 3). |
| 2.1 Golden rule | CLEAR (long) | Undergraduate content. The δ-limit and the box normalisation are the only new parts. | Cut to about 3,500 words. Keep WE 2.1 (breakdown time), which is genuinely new. |
| 2.2 Born, form factors | CLEAR | Helm form factor uses nuclear-physics input that is not assumed, but it is cited and that is enough. | None. All outcomes are achievable. |
| 2.3 Second quantization | MINOR GAPS | First truly new formalism for (a). 4,500 words cover fermion and boson Fock spaces, basis change, Coulomb with background, and normal ordering. Heaviside–Lorentz units are unfamiliar to (a). | Keep the budget. Put the A.2 unit conversion in the text at v_C(k) = e²/k². Make sure Table 2.1 includes the plane-wave density n_e(q). |
| 2.4 Second-order | MINOR GAPS | The Dyson series is assumed (via the interaction picture) without being listed. The Hadamard finite part is unmotivated here because it is first used in 6.5. Five outcomes in 5,500 words is dense but feasible. | List the Dyson series as assumed or recap it. Introduce the finite part with a one-line forward motivation (6.5 double poles) or defer it to C.4 and 6.5. |
| 2.5 Thermal states | CLEAR (long) | Outcome (v) re-derives Bose/Fermi functions that (a) knows. Only the second-quantized form is new. | Reduce (v) to a paragraph. Keep the detailed-balance derivation and WE 2.7. |
| Ch. 3 start | CLEAR | From-scratch start fits (a). | None. |
| 3.1 Lattices | CLEAR | None. The static-lattice assumption is stated explicitly, which helps. | None. |
| 3.2 Bloch, bands | MINOR GAPS | Ashcroft–Mermin Chs. 8–10 compressed into 5,500 words. Tight binding needs the LCAO overlap set-up. No momentum or velocity matrix element p_mn is defined, yet 3.4(v) and 6.5 need one. | Add p_mn = ⟨m|p|n⟩ next to v^g, with its relation to ρ_mn at small q. That also prepares the "O(q) suppression" of WE 3.4. |
| 3.3 Si, Ge, GaAs | CLEAR | The phonon-assisted window is qualitative before phonons exist, which is acceptable. k·p is derivable from assumed perturbation theory. | None. |
| 3.4 DFT | MINOR GAPS | Overloaded: HF, a proof of HK, KS, LDA/GGA/hybrid, the gap problem, scissor and GW in 5,500 words. GW "outline" comes before any self-energy or quasiparticle language (4.6). Outcome (v), "velocity matrix elements", refers to an object not yet defined (see 3.2). | Limit GW here to "KS gaps are not quasiparticle gaps; corrections and numbers", and give the formal statement after 4.6 (a short paragraph in 4.6 or 6.4). Fix p_mn in 3.2. Consider 6,500 words. |
| 3.5 Plane waves, PPs | CLEAR | PAW can only be reached at outline level, which matches outcome (iii). | None. |
| 3.6 Wannier | MINOR GAPS | Weak motivation: the first real use is 6.3, three chapters later. The spread functional needs the periodic position-operator subtlety. | Open with a concrete need (fine k/Q grids for 6.3 and Part II). Add a one-line pointer in 6.3 back to 3.6. Alternatively, move 3.6 to open Chap. 6. |
| Ch. 4 start | MINOR GAPS | The outline should warn that this is the densest chapter and give the internal dependency order. | Put a section dependency mini-chart in the outline paragraph. |
| 4.1 Kubo | CLEAR | The interaction picture is not in READER (finding 1). | Add a two-line recap. |
| 4.2 S(q, ω) | CLEAR | None. WE 4.4 (hydrogen) closing back to 2.2 works well. | None. |
| 4.3 Causality, sum rules | MINOR GAPS | The f-sum normalisation "π over the real line" differs from the textbooks (a) will read. WE 4.5 uses oscillator strengths, but they are not in Introduces. | Add oscillator strength to Introduces. Put a one-line conversion to the ∫₀^∞ form beside the boxed f-sum. |
| 4.4 Screening | MINOR GAPS | Fig. 4.4 (proper insertions joined by Coulomb lines) is a diagram two sections before diagrams (4.6). Thomas–Fermi needs k_F, E_F and the Fermi-level density of states, which are introduced in 4.7. Six outcomes. | Present R = R̃ + R̃v_C R as an algebraic geometric series. Label Fig. 4.4 as a schematic with a forward pointer to 4.6. Introduce k_F, E_F and the DOS at E_F here, or move them from 4.7 to 2.5. |
| 4.5 Beyond IP | MINOR GAPS (near LOST) | The BSE is "set up" before the ladder diagram exists (4.6). 4.6 lists R⁰ → 4.5, so the two sections cannot simply be swapped. Fifth rung in 6,000 words. | Write the BSE as an electron–hole eigenvalue problem (direct and exchange kernels) in the transition basis, with no diagrams. Defer the diagrammatic justification to 4.6 via the ladder in Fig. 4.7. Option: put 4.7 (electron gas: R⁰ and RPA on plane waves) before 4.5, so RPA is first met in the simplest model. |
| 4.6 Green's functions | LOST | Green's functions, Dyson, Wick at finite T (D.8), Feynman rules, ladder and cutting rule in 5,000 words for a reader with no many-body theory. "Matsubara at a mention" does not support real-time time-ordered diagrams at T > 0: finite-T perturbation theory needs the Matsubara or Keldysh contour. | Raise to about 7,000 words (funded by finding 3). Do diagrams at T = 0 first. Give finite T through Matsubara and analytic continuation, stated plainly. Add a fully worked second-order self-energy example, since 6.4 depends on it. |
| 4.7 Electron gas | CLEAR | Fine once 4.5 is in place. Better placed earlier (see 4.5). | Consider reordering to 4.4 → 4.7 → 4.5 → 4.6. Check the concept DAG (R⁰ would be defined in 4.7 for plane waves). |
| Ch. 5 start | CLEAR | Clamped nuclei were flagged in 3.1, so the late justification is not jarring. | None. |
| 5.1 Born–Oppenheimer | CLEAR | None. | None. |
| 5.2 Harmonic crystal | CLEAR | None. | None. |
| 5.3 Phonons | MINOR GAPS | WE 5.4 uses the Debye model, which is in no Introduces list. | Add the Debye model (and Debye temperature) to 5.2 or 5.3 Introduces. |
| 5.4 Phonons ab initio | CLEAR | The Sternheimer equation at outline depth suits (a). | None. |
| 5.5 Polar crystals | MINOR GAPS | Z*_κ is defined as ∂P/∂u, but in a periodic solid the polarisation is defined only through the Berry-phase theory. Not flagging this misleads (c). | Define Z* through the force induced by a uniform field (∂F_κ/∂E), or name the modern theory of polarisation with a pointer to E.4. |
| 5.6 Displacement corr. | CLEAR | None. The single meaning of "Debye–Waller" is stated. | None. |
| 5.7 Anharmonicity | CLEAR | SCHA/TDEP at outline level is fine. | None. |
| Ch. 6 start | CLEAR | None. | None. |
| 6.1 Non-adiabatic | MINOR GAPS | Migdal's theorem (1958, vertex corrections, ω_ph/E_F) and the Migdal sudden kick (1941) sit in one section, and Ch. 12 is "The Migdal effect". (a) will conflate them. Migdal's theorem needs vertex/self-energy language (4.6), which is not listed. The theorem is a metals statement, so its relevance to insulators needs a sentence. | Add 4.6 to the prerequisites. Name the two ideas differently in the text (e.g. "Migdal's adiabatic theorem" against "recoil-induced ionization"). State the insulator analogue (ω_ph/E_g). |
| 6.2 e–ph matrix elements | CLEAR | Five outcomes in 5,500 words is dense but well prepared. | None. |
| 6.3 Computing g | CLEAR | None. | None. |
| 6.4 Self-energy | MINOR GAPS | Depends wholly on 4.6 being solid. If 4.6 stays as planned, (a) cannot follow Fan–Migdal and Allen–Heine. | Resolved by the 4.6 fix. |
| 6.5 Phonon-assisted abs. | CLEAR | The velocity form of the optical vertex is introduced here; it should be met in 3.2. | See 3.2. |
| Ch. 7 start | CLEAR | None. | None. |
| 7.1 Magnetism | MINOR GAPS | "Heisenberg model from exchange" for NiO: NiO's coupling is superexchange (a charge-transfer insulator), not direct exchange. The spin-density response uses 4.1/4.2, which is fine. | Add superexchange (Anderson) qualitatively, with the J ∼ t²/U estimate, before the NiO numbers. |
| 7.2 Superconductivity | MINOR GAPS | No pairing mechanism, although Ch. 6 precedes this section. The prerequisites omit 6.2. The conserving-response outcome (iii) is heavy for (a) but feasible at outline level. | Add 6.2 to the prerequisites. Give one paragraph on phonon-mediated attraction (the retarded e–ph interaction) to motivate the BCS model interaction. |
| 7.3 Dirac | CLEAR | v_F notation collision with 4.7. | Write v_D, or subscript. |
| 7.4 Defects | CLEAR | None. Central-cell correction explains Si:P effective-mass theory (~31 meV) against the measured 45 meV. | None. |
| App. A | MINOR GAPS | A.1 "first 1.2" should be 1.1. | Correct the row. |
| App. B | CLEAR | B.2 correspondence is valuable (χ to R, W to L, q to Q). | Point to B.2 at R's first appearance (4.1). |
| App. C | MINOR GAPS | No primer on classical field Lagrangians and static Green's functions (needed by 1.4). C.4 finite part comes early (see 2.4). | Add C.9 "Classical fields and propagators" (about 1,500 words), or a box in 1.4. |
| App. D | CLEAR | Rows and entries match (D.1–D.19 against their sections). D.8 needs the Matsubara/real-time choice made explicit (see 4.6). | Align D.8 with the 4.6 fix. |
| App. E | CLEAR | Pointers are consistent with the chapters. | None. |

Spot checks of key numbers (consistent): m_min(Si gap) ≈ 0.32 MeV; 2π/a(Si) ≈ 2.28 keV; Al 2Δ, giving m_min ≈ 0.1 keV;
ω_p(Si) ≈ 16.6 eV; S = q²L/(2πα(1 − e^{−βω})) with the stated FDT and S normalisation; f-sum π𝓃q²/m_e.

## Persona (a): first-year PhD student
Chapters 1–3 and 5 are well paced. Two items stop me. First, 1.4 as planned assumes QFT: a classical-field derivation fixes it. Second,
4.6 tries to teach all of Green's-function and diagram technique in 5,000 words, after 4.4 and 4.5 have already used its pictures
(the Fig. 4.4 chain, the BSE ladder). Smaller gaps are concepts used one step early: k_F before 4.7, p_mn before 6.5, GW before
self-energies, the Debye model, oscillator strengths. Each needs a sentence or a moved definition. I would be bored by 2.1 and parts of
2.5. Learning outcomes are achievable everywhere except 1.4(i) and (iii) and 4.6(iii) and (iv) as budgeted. The two Migdals in 6.1 would
mislead me later in Ch. 12. The "nothing left to the reader" principle helps a lot: with every step written out, density is the main risk,
not missing steps.

## Persona (b): particle physicist, no solid state
Bored by 1.4 (Yukawa, kinetic mixing), 2.1–2.4 (golden rule, Born, Fock space, T-matrix), and the T = 0 parts of 4.6. The theorist
reading path should say these can be skipped. Chapters 3–7 are what (b) came for, and the pace fits. Misleading: 1.4(iv) absorption of a
dark photon without any warning that in-medium mixing changes the effective coupling (κ_eff via the photon self-energy). T2 only lands in
Chap. 8, so add a forward caveat in 1.4. (b) will expect relativistic state normalisation, so the nonrelativistic box normalisation of 2.1
needs a one-line comparison. The "R, not χ" convention is welcome because χ is the DM particle. Heaviside–Lorentz units are (b)'s native
units, so A.2 should convert toward Gaussian/SI for (a) and (c), not the other way. The κ triple use (κ_mix against species κ) will
cause errors in Part II formulas.

## Persona (c): condensed-matter theorist, no dark matter
Bored by most of Chaps. 2–5: second quantization, Bloch, DFT, Kubo, Lindhard, phonons. The front matter must give (c) an explicit
path: Ch. 1 → 4.2 (the rate as S(q, ω)) → 4.4 (S–L relation, electron-only versus total-charge probes) → 5.6 → 6.5 → Ch. 8. Chapter 1 is
the essential new content for (c) and is well chosen. Errors or framings (c) would flag in their own field:
- real-time diagrams at T > 0 with "Matsubara at a mention" (4.6, D.8);
- the Heisenberg model "from exchange" for NiO without superexchange (7.1);
- Born charges as ∂P/∂u without the Berry-phase caveat (5.5);
- Migdal's theorem stated for semiconductors without the ω_ph/E_g reinterpretation (6.1);
- BCS with no pairing mechanism even though e–ph coupling is already built (7.2).

The R notation and the π-over-the-real-line f-sum normalisation are unconventional for (c). B.2 handles the first, and the second needs a
conversion line. "Proper/improper" matches Giuliani–Vignale and is fine. (c) would value the Limit boxes and the computational-connection
paragraphs and would not find them condescending, provided 3.4–3.6 and 5.4 stay at the physics level as the App. E boundary promises.
