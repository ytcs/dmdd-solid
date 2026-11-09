# DC-2-gw pre-registration: Ge QP bands by G₀W₀ (written before any GW run, 2026-11-06)

New item. DC-2 (HSE06+SOC) and DC-2-alpha stay CLOSED as failed. Approved by the user's stand-in; Yambo first (user), BerkeleyGW is the fallback.

Code: Yambo 5.3 double precision, on QE 7.6 output via p2y.
Starting points, both run, spread reported as starting-point uncertainty:
- S1: PBE+SOC at a_exp. Known hazard: Γ s-state inside the valence band, occupations wrong at Γ.
- S2: PBE0+SOC at a_exp. Changed from HSE06: Yambo developers state GW on an HSE start is not supported, PBE0 and HF are (forum, 2019–2021; not confirmed for 5.3). QE and Yambo must treat the exchange divergence identically (vcut_spherical with Yambo's sphere cutoff). SG15 FR Ge, no NLCC, 3d valence.
DFT+α is excluded: Yambo recomputes V_xc and would miss the α term.

Method: G₀W₀, Godby–Needs plasmon pole, spinor SOC, k 8³ IBZ.
Convergence: bands in χ⁰ and Σ 200/300/400; screening cutoff 4/6/8 Ry. Accepted when L and Γ gaps move < 20 meV between the last two values of each.

Controls, on converged values:
- C1: L below Γ.
- C2: E_g(L) = 0.744 ± 0.1 eV.
- C3: E_dir = 0.89 ± 0.1 eV.
- C4 (T3): m_t 0.082 ± 0.010, m_Γ 0.038 ± 0.005, m_l 1.59 ± 0.15 m_e, from QP bands. If 8³ cannot resolve masses, compute from QP energies at extra k or state the test as not reached; do not score it as passed.
- Stated, not corrected: T = 0, no zero-point renormalisation (Ge ≈ −50 meV).
- Interpolation: Wannier QP bands vs direct QP at off-grid k within 10 meV near the valley minima, or test 10³.
The two starting points may disagree beyond tolerance. That is a result, reported as such.

E_min(q) only if a starting point passes C1–C4. Not allowed: tuning a scissor or mixing fraction to hit a control; choosing the better start after the fact without reporting the other.
