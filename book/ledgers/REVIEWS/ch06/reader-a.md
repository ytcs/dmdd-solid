# Chapter 6 — mock reader (a), isolated review

Persona (a): first-year PhD student, undergraduate QM/EM/stat-mech, no graduate solid state or QFT.
Read: the .tex sources `tex/ch06/s6-1…s6-5.tex` and `tex/appD/D-16…D-18.tex`. I used the sources because
`build/main.pdf` (Nov 1 23:46) is older than every Chapter 6 source. **Figures were not viewed**, so I did not check
whether the figures match their captions. Labels from Ch. 1–5 and App. A–D were checked; all refs in Ch. 6 resolve
except the forward refs to Ch. 7, 8, 11, 12, 13 (expected).
Every number below marked ✓ was recomputed (by hand or in Python).

## 6.1 Non-adiabatic coupling (+ D.13 pointers)
**Lost points**
- Para. "For a nucleus in a crystal two times matter": the enhancement $[1-(\omega_{\rm ph}/\omega_e)^2]^{-2}$ "follows from
  the classical motion in the same way", but the trajectory is not stated. I had to supply $X(t)=(v_N/\omega_{\rm ph})\sin\omega_{\rm ph}t$
  plus the δ-kick, which gives $\int\ddot X e^{i\omega t}=v_N/(1-r^2)$ ✓. One clause would fix it.
- "Derivative coupling becomes physical once we read p/M as a velocity … acts as $-i\dot u\cdot d$": a heuristic step, made rigorous only
  by the classical-trajectory derivation that follows. Fine, but say "heuristically" or reverse the order.
**Could not reproduce**: none. Checked: antisymmetry, ⟨Ψj|∇²Ψi⟩ identity, eq. 6.1-Pd term by term ✓; 6.1-tdep ✓;
  integration by parts 6.1-accel ✓; sech² Fourier integral and 6.1-model ✓ (bracket 0.466 at 1, 0.074 at 2, asymptote ✓);
  Bloch property of ∂_{κ,Q}V and 6.1-Hep normalization ✓; $d_{j0}=m_e\Delta E\langle\sum r\rangle$ via $P=im[H,R]$ ✓;
  hydrogen argument $q/(\alpha m_p)$ ✓; WE 6-hydrogen (μ=484.2, q=2.566 MeV, 3.51 keV, v_N/α=0.375, F=0.933, P0=0.871,
  half-survival at v_N/α=0.87, 5.96 MeV, 18.9 keV, ΔEτ=1.6e-5) ✓; opening v_N=1.95e-4, 58 km/s, κ_BO³=2.94e-4, ratio 91 ✓.
**Used before defined**: "vertex corrections" (6.1, last para of derivative coupling) is only glossed here. Ch. 4.8 introduced the term,
  so this is acceptable.
**Too slow / too fast**: the closing "two results carry Migdal's name" paragraph is helpful but partly repeats the
  power-counting paragraph. Pace otherwise right.
**Learning outcomes (inferred)**
- Write the BO couplings as a derivative coupling / vector potential: yes (reproduced 6.1-Pd).
- Derive H_ep and g from V_eN: yes.
- Tell adiabatic from sudden and evaluate the exact model: yes (|α_d|²/sudden = 0.466 at ω_eτ=1).
- Compute sudden-kick survival: yes. For v_N/α = 0.2, F=16/4.04²=0.980, P0=0.961, 1−P0≈v²/α²=0.04 ✓.

## 6.2 Electron–phonon matrix elements
**Lost points**
- "The tail is removed by the local fields … Their effect is to replace the ionic charge by the Born effective charge"
  (Pick–Cohen–Martin): asserted, not shown. I take it on trust. It is central to "Si has no 1/Q vertex", so a two-line
  heuristic would help.
- Piezoelectric paragraph: "it comes from the dynamical quadrupoles of the displaced atoms" is undefined (see below).
  The formula itself I reproduced: $V=e\hat Q\cdot\mathcal E/(iQ)$ with $\hat Q\cdot(\varepsilon_\infty\mathcal E+P)=0$ gives the stated sign ✓.
**Could not reproduce**: none. Checked: $(1-fR^0)^{-1}=1+fR$ ✓; 6.2-asr via $T_d V T_d^\dagger$ ✓; strain → 6.2-D ✓;
  Herring–Vogt effective constants ✓; ℓ(0.55 meV)=0.260 Å, |g|=26 meV / 2.6 meV ✓; ℓ_opt=0.0241 Å, |g|=0.25 eV ✓;
  Fröhlich C_F² from g^L + LO–TO + LST (using D.14, read with Ch. 5) ✓; ΔE integral and α_F algebra ✓;
  WE 6-frohlich: Ω=5.831e-9 eV⁻³, C_F²=4.11e3 eV⁴, |g|=3.25 eV, √=686, α_F=0.072, 2.6 meV, 39.6 Å, 0.025 Å⁻¹, 1.29 eV;
  LST route 0.01328, α_F=0.067 ✓; Wannier phase bookkeeping of 6.2-gW ✓ (but compressed: "translate every term by the
  cell of the bra" took me a page).
**Used before defined**: "dynamical quadrupoles" (6.2, piezoelectric para.). It is not defined anywhere in Ch. 1–5.
**Too slow / too fast**: the screening paragraph, which covers test electron, f_xc, metal/insulator, local fields and Born charges in about
  15 lines, is the densest stretch of the chapter. The Wannier-interpolation derivation is fast but reproducible.
**Learning outcomes**
- Write the DFPT vertex in the ℓ × (eV/Å) form: yes.
- Acoustic g∝Q^{1/2} from translation invariance and a deformation potential: yes (26 meV reproduced).
- Optical deformation potential: yes (0.25 eV).
- Fröhlich vertex and α_F: yes. α_F(GaAs)=0.072 reproduced.
- Explain the Wannier interpolation and the long-range subtraction: yes, qualitatively.

## 6.3 Electron self-energy from phonons (+ D.16)
**Lost points**
- **Degenerate valence top.** The key result (6.3-FM/AH) and D.16 are stated "for a nondegenerate band n", and the
  RIA prime excludes degenerate partners. 6.2 says the Si VBM is threefold degenerate, and line 54 says the adiabatic
  form fails "wherever another band is degenerate". Yet 6.3 then quotes the VBM shift (+35 meV) and a gap ZPR
  (−56.2 meV) without saying how the degenerate top is handled (degenerate-subspace average? matrix self-energy?). This
  is the chapter's central number, and I cannot see how it was computed from the formulas given. One sentence is needed.
- **Which ZPR is "measured"?** The text gives three experimental scales: −52 / −59 meV (WE 6-zpr, inverted Einstein
  model), −62 / −64 meV (Cardona, "from the same two routes"), and −71 / −73 meV (e–ph part after the 9 meV zero-point
  expansion). It says calculations fall ~20 % short of the last, while the WE says experiment brackets −56.2. Why the
  same two routes give −52…−59 here and −62…−64 in the literature is not explained (a different ω_Ein? thermal expansion?).
  The practical answer ("use the measured Eg(0)") is there, but the numbers are not reconciled, and I left the section
  unsure what the computed AHC value is actually missing.
- Silicon lifetime paragraph: the Ξ² angular average is said to be "relative to k". The angle that enters 6.2-D is between
  Q and the valley axis, so for a random valley orientation the average is over that angle. The result is unchanged, but
  the wording confused me for a moment.
**Could not reproduce**
- WE 6-zpr inverse slope: −(353/2)×0.33 = −58.2, printed −59 (rounding of the slope; −58 would be honest).
- "For small Q the interband remainder is smaller by ~Q²": taken on trust.
- Checked ✓: D.16 Matsubara residues (all three, including n_B(iω_F−ξ)=−(1−n_F)); adiabatic numerator sum 2n+1;
  Fröhlich adiabatic divergence integral; translational cancellation 6.3-cancel (Fan → ℓ²Σ(ε_n−ε_m)|p|², AH → −same via
  ⟨[p,[p,H]]⟩); sum rules D.16-sr1/sr2, D.16-ria (factor 2/N) and the symmetrisation to 6.3-ria; smearing 6.3-smear;
  Einstein: coth(0.588)=1.892, −50.1 meV; measured fall 46.2 meV; slopes 0.26 / 0.33 meV/K; 0.318 meV/K; 1.2254 eV;
  ²⁸→³⁰Si +1.79 meV; 600 K model −140.4 vs measured −140.6 meV; Cherenkov angle, Q_max, 6.3-cherenkov prefactor;
  Ξ_L=4.75, Ξ_T=3.23 eV; thresholds 0.065/0.031 meV; Γ(10 meV)=7.15+5.15=12.3 µeV, 53 ps; 0.91 ns at 1 meV; 16 ps at 30 meV.
**Used before defined**: λ_ep and the mass enhancement in the Migdal-theorem subsection. It is forward-glossed to 6.4, which
  is acceptable. ω_D, E_F, v_F, z_qp all come from Ch. 4–5.
**Too slow / too fast**: the ZPR subsection plus WE 6-zpr (about 40 lines of numbers) feels long compared with the
  translational-invariance argument, which is the conceptual core and is dense. The Migdal-theorem phase-space argument is brisk
  but clear.
**Learning outcomes**
- Write Σ^FM and Σ^AH and read the thermal factors: yes (D.16 reproduced).
- Adiabatic limit = average over the smeared lattice: yes.
- Show the acoustic cancellation and derive the RIA form: yes.
- Use the Einstein model for E_g(T) and a ZPR: yes (−50.1 meV at 300 K; +1.8 meV isotope shift).
- Phonon-limited lifetime of a hot carrier: yes (12.3 µeV at 10 meV).
- State Migdal's theorem and where it fails: yes. Partly for degenerate band edges (see above).

## 6.4 Phonon self-energy and the Eliashberg function (+ D.17)
**Lost points**
- **Unit clash in the Al model.** Line 98 writes the ion potential as "−3e²/r" and w(q)=−4π·3e²cos(qr_c)/(Ωq²ε). Those are
  Gaussian forms. The book uses Heaviside–Lorentz (A.2-vC: v_C=e²/k²; 6.1: −Ze²/(4πr); 6.2 uses e²=0.0917). A reader
  who plugs in e²=4πα gets w 4π too large and λ off by (4π)²≈158. It should read −3e²/(4πr) and w=−3e²cos(qr_c)/(Ωq²ε),
  or say e→e_G explicitly.
- Static subtraction 6.4-nonad: the text says that the exact Π has the bare vertex at one end, but subtracts the screened–screened
  Π(Q,0). It is not shown that this Π(Q,0) is what DFPT contains, so the argument feels too fast.
- Fig. 6-a2F caption: "The transverse peak is suppressed, although three quarters of the modes lie below 32 meV, in
  α²F because…" is garbled. I had to reread it to parse it.
**Could not reproduce**
- λ_ep=0.436 and ω_log=250 K of the Al model: the force constants (first/second neighbors fitted to X, L, elastic
  constants) are described but no values are given, so the number cannot be checked. The same goes for the 0.44–0.46 range in r_c.
  This is fine as a quoted model result, but it is not reproducible from the text.
- Checked ✓: bubble sign count and Π=2ωΠ^b; pole expansion and γ=−ImΠ/ω (full width); 6.4-gamma; Allen limit;
  electron-gas double δ = m²/(4π²q); D.17 mass-enhancement logs → λ; 6.4-a2Fgas from 6.4-a2F; Al k_F=1.75 Å⁻¹,
  E_F=11.7 eV, v_F=2.0e6 m/s, Q≲2.3e-3 Å⁻¹; Migdal 0.0034 / 0.0015; e^{−Eg/2T}=4e-10; specific heat 0.951 mJ K⁻² mol⁻¹,
  1.43; 36 periods; WE 6-al: λ=0.396, ratios 1.4 / 2.9, TA share 70 %, ω_log=26.7 meV=310 K.
**Used before defined**: none (Kohn anomaly, α²F, λ_ep and ω_log are defined where used).
**Too slow / too fast**: the Al-model paragraph packs phonons, pseudopotential, screening, umklapp and integrals into one
  block, which is too fast for persona (a). The vertex-correction paragraph repeats 6.3 and could be cut to one sentence.
**Learning outcomes**
- Phonon self-energy as the electron bubble, and the shift and width: yes.
- Why insulators have no e–ph phonon width: yes.
- Allen's formula → α²F → λ: yes. Two-peak λ=0.396 reproduced; by λ=Σγ/(2πN_FΩω²) I can turn a measured width into λ_Qν.
- Mass enhancement 1+λ from the specific heat: yes (0.43).

## 6.5 Phonon-assisted optical absorption (+ D.18)
**Lost points**: none blocking.
- Main text 6.5-joint carries Ω² with ⟨⟨…⟩⟩, while D.18 carries Ω with (VN)⁻¹Σ. Both are consistent (I checked that A_ν agrees),
  but the switch of normalization between text and appendix cost me time. A one-line cross-note would help.
**Could not reproduce**: none. Checked ✓: A(t) ↔ 𝓔(t) and the amplitude 𝓔/2ω; D.18-eps2 from power balance; α=ωε₂/n_r;
  fermion sign of hole paths 3 and 4 and their on-shell denominators (they map onto paths 2 and 1); phonon-first ∓ sign for
  absorption; DOS (2m)^{3/2}ε^{1/2}/4π²; ∫√(ε(x−ε))=πx²/8; joint result; A_ν from 6.5-eps2PA; thresholds
  1.1123 / 1.1517 / 1.1883 / 1.2277 eV and excitonic ones; 212 K→18.27 meV, 670 K→57.73 meV; THz conversions;
  n_TA=0.973, n_TO=0.120, slopes 0.987/1.405/0.346/1.058, ratios 0.702/0.327; 77 K and 20 K occupations; ω/T=2.12e4.
**Used before defined**: none (E_dir is from 3.3, E_x^b from 4.9).
**Too slow / too fast**: the "rough size" paragraph is a welcome orientation. The double-counting paragraph at E_dir relies on
  2.4-split from memory, but it is fine. "From light to dark matter" overlaps with the Summary.
**Learning outcomes**
- Build the four-path amplitude M^± and explain the hole orderings: yes.
- Write ε₂^PA and the HBB edge: yes (re-derived A_ν).
- Read phonon energies and temperature off an edge: yes (−2T ln 0.702 = 18.3 meV).
- Explain why only emission survives at 10 mK and how the DM vertex replaces the optical one: yes.

## Overall
I would keep reading. Every derivation in the five sections and D.16–D.18 that the text claims to carry out
I could reproduce, and every worked-example number I checked agrees to the quoted precision. Three things slowed
me down without stopping me:
(1) the Gaussian-unit Coulomb in the Al model (6.4), a real notation clash with the book's Heaviside–Lorentz
    convention that would derail anyone reproducing λ;
(2) the silicon ZPR: the formulas are for nondegenerate bands, but the headline number involves the degenerate VBM, and
    three different "experimental" scales are given without reconciliation;
(3) a few assertions taken on trust: local fields → Born charges, the ~Q² interband remainder, and the bare/screened static subtraction.
None of these blocks 6.5 or the appendices. The rest is small: one undefined term (dynamical quadrupoles), one
garbled caption sentence, one rounding (−59 vs −58 meV), and a missing trajectory in 6.1.

**Verdict: MINOR GAPS**
