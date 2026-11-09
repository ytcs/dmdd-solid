# Chapter 4 mock-reader review: reader b (personas b and c, isolated)

**Source read.** `build/main.pdf` (built Nov 1 23:46) is older than every Ch. 4 source, so I read the .tex: `ch04/s4-1…s4-9`, `appD/D-6…D-12`, `appC/C-5…C-7`, plus a grep of Ch. 1–3 to check definitions. Figs 4.7 and 4.11 judged for pedagogy only.
**How I checked.** I redid every derivation by hand. Numbers were rerun in Python (scipy). **Reproduced (number obtained → text):** $k_F$ 3570 eV, $E_F$ 12.47, $v_F$ 6.99e-3, $\omega_p$ 16.61 / 31.07 eV, $r_s$ 2.005 (all ✓). Then: TRK hydrogen, bound 0.5650, continuum 0.4350, 0.3163 within $E_B$, 0.0042 above $10E_B$, total 1.0000 ✓. Lindhard $\operatorname{Im} R^0$ against $-m^2\omega/2\pi q$ ✓. $q_c=0.7297k_F$, $\omega_{pl}(q_c)$ 24.84 eV ✓. $\omega_{pl}(0.3k_F)$ 17.65 eV ✓. $|\varepsilon_{\rm Lin}(q_0,q_0v_{\max})|^2$ 3.963 and $L$ 0.1833 ✓. $\varepsilon_{\rm Lin}(q_0,0)$ 2.102 ✓. Naive vs Mermin static, 12.83 vs 15.67 ✓. ALDA $\varepsilon(q_0,0)$ 2.62 ✓. $\int x^2/(1+x^4)^2=\pi/8\sqrt2$ ✓. Slow stopping 0.1808 vs full 0.1857 eV/Å (2.7 %) and 22.4 % at $v_{\max}$ ✓. Anderson level $\langle d^\dagger d\rangle$ 0.7875 ✓. Einstein shifts −9.14 / −11.09 meV, self-consistent −8.734 meV, $z$ 0.952, $\varGamma$ 2.08 meV ✓. Also ✓: $k_{TF}$ 4.117 keV, $\bar E$ 17.36 eV, $\varepsilon$ resonance 5.08 eV, peak 4.34, $L_{\rm model}(3\,\rm eV)$ 0.0353, Mermin $L(3\,\rm eV)$ 0.0425, $\bar K$ 561 eV, $(5/3)\bar K/m_e$ 1.83e-3, $14m_e/M$ 2.73e-4, Si-exciton bracket 13.4–18.9 meV, GaAs 5.24 / 3.74 meV and 12.6 / 14.9 nm.
**Not reproducible from the text alone (data, not counted against it):** the Henke integrals (0.35 / 8.46 / 1.61) and the Franta-table figures (87 %, 6.5 eV rms, slope 0.128, $\varepsilon_2=0.22$, 96 / 92 %, 99.8 / 97.8 %). **Tied to Figs 4.7 / 4.11 (pedagogy only):** 11.45 / 10.22 / 10.81, the peak heights, 81 meV, 3.4 % TDA, +36 % at 3 eV.

---

## Persona (b): particle physicist (QFT, no solid-state physics)

| § | Lost / could not reproduce | Used before defined (for me) | Pace | Learning outcome as I infer it: can I do it? |
|---|---|---|---|---|
| 4.1 | — All steps reproduced: Kubo, Lehmann, the tail coefficient, the oscillator three ways, the two-level $\tanh$ and 1.523, the pole circle and $-0.38i\omega_0$. | "local fields" (forward to 4.4; harmless) | Right. The oscillator and two-level material is slow for me but right for persona (a). | Derive $R$ and its Lehmann form, and show UHP analyticity. **Yes**: I rederived the $1/z^2$ coefficient $\langle[O^\dagger,[H,O]]\rangle$ in eigenstates. |
| 4.2 | — Van Hove, the FDT with off-diagonal elements (signs checked term by term), the spectral form, $S^0$ of the gas (kinks, 0.239 at $0.75E_F$, $2.2\times10^8$ eV², 0.121) and hydrogen (0.41 + 0.59) all reproduced. | "Bragg term" (fine via 2.2) | Right | FDT and positivity. **Yes**: $(1-e^{-\beta\omega})S_{ab}=i(R_{ab}-R^*_{ba})$ rederived, and the oscillator check $(n_B+1)$, $-n_B$ works. |
| 4.3 | — KK both routes, moments, f-sum commutators, mass–velocity $4p^2q^2+8(p\cdot q)^2+2q^4$, TRK, gas f-sum, gap bound $q<0.24$ keV, 0.42 ✓. | "pseudopotential / $V_{\rm NL}$" (OK via 3.5) | Right | f-sum and TRK. **Yes**: $\int\omega S^0$ for $q>2k_F$ gives $q^2k_F^3/3\pi m$. |
| 4.4 | The Ward identity (eq. 4.4-ward) is only sketched. I **did** reproduce it with two integrations by parts; the boundary term is $\langle[q\cdot j^\dagger,n]\rangle/V=nq^2/m$ ✓. The rest ✓ ($\varepsilon=1+i\sigma/\omega$, transverse tensor, TF, Lindhard stopping $2Z^2\alpha/\pi v^2$). | "head" (implicit: inverse of the head of the inverse); "semilocal" (3.4 ✓) | Local fields and $\varepsilon_{\rm mac}$ come fast for a non-solid-state reader. Fine with D.7. | $S=(2q^2/e^2)L/(1-e^{-\beta\omega})$ and the loss sum rules. **Yes**: $\bar E=17.4$ eV, single-oscillator moments. |
| 4.5 | — Lindhard checked numerically. Plasmon $12/175=3/7-9/25$, weight $\pi\omega_p/2$, $S^{\rm st}\to q^2/2m\omega_p$, Drude limit and naive tail $2\gamma\omega/\omega_p^2$ all ✓. | "Kohn anomaly", "Friedel oscillation" (named only; OK) | Right | RPA plasmon and its cutoff. **Yes**: $q_c=0.730k_F$ found by root-finding. |
| 4.6 | — Crystal bubble, head $O(q^2)$, $\varepsilon_1^{\rm IP}(0)\propto\Delta^{-3}$, $f_x=-e^2/4k_F^2$, compressibility 1.55 ✓. | **"wings"** (l.41, l.108) are never defined. They are not in Ch. 1–3, and D.7 only uses them. **"Adler–Wiser", "scissor", "head/body"** come in a rush. | Too fast in the first half for me: EPM, 59 G-vectors, Lorentzian broadening. | Explain what each rung changes. **Mostly**: IP → RPA changes only $\lvert\varepsilon\rvert$; local fields change $\varepsilon_2$. I can say why, but I could not set up a calculation. |
| 4.7 | — Lehmann, $\mathsf A n_F$, Dyson, $\operatorname{Im}\Sigma\le0$, the quasiparticle expansion, the Anderson self-energy, the log form and $10^{-136}$ eV bound states ✓. | — | Right; familiar to me. | Quasiparticle from $\Sigma$. **Yes**: $z=1.0064$ and the 0.0064 weight outside the band check out. |
| 4.8 | — Rules and signs match D.11. Boson self-energy residues ✓. $W$ spectral weight $vL/\pi$ and lifetime eq. 4.8-lifetime with $(1-e)(n_B+1-n_F)$ ✓. Bubble cut ✓, $\omega_+=39.65$ eV. | "Ward identity" is named here for the identity 4.4 derived without a name. | A little slow for a QFT reader, but correct. | Use the Feynman rules and the cutting rule. **Yes**: I derived eq. 4.8-sigmaboson and the $\varGamma_{\rm in}=e^{-\beta\omega}\varGamma_{\rm out}$ split. |
| 4.9 | — WM reduction (convolution → $\alpha/\varepsilon r$), COM dispersion, Elliott sum, $S$ per exciton ✓. | **"LO–TO splitting"** (l.134; also D.12) comes before Ch. 5 and is not in Ch. 1–3. Luttinger $\gamma_1$ (Ch. 3 ✓) | Right | BSE and hydrogenic excitons. **Yes**: $E_x^b$ and $a_x$ for GaAs and the Si bracket reproduced. |
| D.6–D.12 | — I followed D.6 (second difference of $F(p)$), D.7 (push-through, the $\bar R$ head), D.8, D.9 (Mermin algebra), D.10, D.11 (Gaudin; overall sign $(-1)^n(-1)^F$; $T=0$ factor $i^n(-1)^F$) and D.12 ($\mathsf L^0=\mathsf G_m\mathsf G_n$, spin, blocks). | — | D.11 is careful and complete. | — |
| C.5–C.7 | — Matsubara sum example $(2n_B+1)/2\omega_0$ ✓. Block inverse and Woodbury ✓. | — | Right | — |

**QFT-side flags and errors.**
- **4.3, relativistic f-sum (l.100–105).** For the full Dirac Hamiltonian, which is linear in $\mathbf p$, $[n^\dagger,[H_D,n]]=0$: the f-sum is carried by the negative-energy, pair continuum near $2m_e$. The mass–velocity reduction is the positive-energy (Foldy–Wouthuysen / no-pair) statement. Say so in one sentence. Otherwise "an all-electron relativistic calculation should not reproduce 4.3-fsum" depends on whether that calculation keeps pair states.
- **4.7 l.163 and D.11 l.39** overstate their case. "The real-time time-ordered function … has no such expansion at $T>0$" and "no such construction exists for real times": real-time thermal field theory (the Schwinger–Keldysh contour) does exist. What is missing is the single-contour Gell-Mann–Low form. Suggest "has no expansion of this simple form".
- **4.1 l.106.** $\phi_0^2=2\rho_\chi/m_\phi^2$ is the square of the *field*, but $\phi_{\rm ext}$ was defined as an energy. A coupling constant $g$, with $\phi_{\rm ext}=g\phi$, has been absorbed silently. Name it.
- I found no condescension toward a QFT reader. The Cutkosky/Weldon attribution, Gell-Mann–Low with "no level crossing", and the sign rule for $R$ vs $\chi$ are all accurate.

**Overall (b).** I would keep reading. Sections 4.1–4.3, 4.7 and 4.8 are fully reproducible and well paced. My gaps are solid-state vocabulary: "wings", "LO–TO", and the opening of 4.6. None of them blocks the physics. **Verdict (b): MINOR GAPS.**

---

## Persona (c): condensed-matter theorist (DFT, many-body; no dark matter)

| § | Lost / could not reproduce | Used before defined (for me) | Pace | Learning outcome: can I do it? |
|---|---|---|---|---|
| 4.1 | — | $\rho_\chi$, $m_\phi$, "bosonic DM field" (Ch. 1–2 ✓) | Slow (oscillator plus two-level for an expert) but not condescending | Rate ∝ $-\operatorname{Im} R$ for absorption. **Yes.** |
| 4.2 | — | $\omega_{\mathbf q}$ in eq. 4.2-rate is not restated; it is the energy fixed by DM kinematics (Ch. 2 ✓). $v_{\max}$ (Ch. 1 ✓) | Right | Why the rate needs $S_{ab}$ and why interference is bounded. **Yes.** |
| 4.3 | — | "Migdal effect" (named; Ch. 1–2 ✓) | Right | Use sum rules as code checks. **Yes**: valence-only f-sum and core overlap well argued. |
| 4.4 | — | "dark photon $\zeta$" (1.4 ✓) | Right. The electron-only vs total-charge $L$ discussion is valuable. | Know when measured $L$ gives the DM rate. **Yes**: always for the dark photon; for electron-only couplings, above phonon energies. |
| 4.5 | **Mermin causality** (l.144; D.9): analyticity of $R^0(z+i\gamma)$ does not exclude zeros of the denominator $1+(i\gamma/z)R^0_\gamma/R^0_{\rm st}$ in the UHP. The conclusion is standard; the argument is incomplete. | — | Right | Why the plasmon is inaccessible: $\omega_p/v_{\max}=6.27$ keV $>q_c$ ✓. **Yes.** |
| 4.6 | Fig 4.7 numbers judged for pedagogy only. | — | Right | Quote a rung spread as the many-body uncertainty. **Yes.** It is clear that this is not a bound. |
| 4.7 | — | — | Slow for me; fine for (a) | — |
| 4.8 | — | — | Right. "An injected electron is a DM particle with a Coulomb coupling" is a very good bridge. | Read $\varGamma_{\rm qp}$ as eq. 4.2-rate with $\tilde V=v_C$. **Yes.** |
| 4.9 | "Diagonal elements of $K^{\rm d}$ average 81 meV" (l.116) is grid-dependent: the $\mathbf p\to0$ head scales with the mini-zone volume. It is quoted as "a measure of the attraction" without saying so. | — | Right | Excitonic $S$ at finite $q$. **Yes**, including the $\lvert\varepsilon_{\rm mac}\rvert^2$ caveat and long-range-exchange shift. |
| D/C | Mermin: as in 4.5. | — | — | — |

**CMT-side flags and errors.**
- **4.2 l.58.** $S^{\rm st}$ is called "the probability, per electron, that the target absorbs $\mathbf q$". $S(q)$ is not bounded by 1: Bragg terms are $O(N)$, and liquid peaks reach 2–3. Call it the normalized total weight. Also, $S^{\rm st}=1+n\!\int e^{iq\cdot r}g$ hides a forward $(2\pi)^3n\,\delta(\mathbf q)$. The small-$q$ sentence ("cancels most of the one") needs the $g-1$ form.
- **Notation clashes.**
  - $K^{\rm x}$ is the $\mathbf G\neq0$ part in 4.6 and 4.9 but the full sum in eq. D.12-crystal. Yet 4.9 l.27 says 4.9-bse "is D.12-eig with the kernels of D.12-crystal", while D.12 itself says the matching form needs $\bar K^{\rm x}$.
  - $\ell(\cdot)$ is the Lindhard log in 4.5 and is redefined as the band-integral log in we:4-einstein.
  - $\varepsilon$ is both the dielectric matrix and the band energy $\varepsilon_{n\mathbf k}$ in the same equations of 4.6 and 4.9.
  - 4.7 l.140 calls the level-shift function "$R(z)$", which collides with the response $R$.
- **Summary l.166.** "$E_x^b=\mu_x\alpha^2/2\varepsilon_\infty^2$: 14.7 meV … in silicon" reads as a prediction. In fact 14.7 meV is measured and $\mu_x$ was inferred from it (4.9 l.68). Rephrase.
- **Fig 4.11 pedagogy.** It demonstrates the attraction on bands that already contain the excitonic shift, so the reader learns about the double counting only from the caption and l.125. Say it before the figure, or present the comparison as a shape test.
- **"Light DM samples the first eV above the gap"** (4.6 l.140, 4.9 l.146): add the one-line reminder $\omega\le\tfrac12m_\chi v^2$ (≈3.5 eV at 1 MeV with $v_{\max}$). It exists in Ch. 1, but here the claim carries the uncertainty argument.
- **Physics I checked and found right:** Adler–Wiser $\varepsilon_{\rm mac}$, local fields lowering $\varepsilon_\infty$, ALDA head/wings dropping out, compressibility sum rule, Luttinger $(\omega-\mu)^2$, the HF velocity log, the PPM-without-lifetimes remark, $K^{\rm x}$ singlet/triplet, the TDA error estimate. None is condescending.
- **Minor typos.** "and and" (we:4-siepsinf). Fig 4.5 caption "Dashed: … (dashed)". Check the rounding chain "17 percent" → "about 11.9".

**Overall (c).** For a condensed-matter reader this is the most useful chapter so far. It places textbook linear response exactly where the dark-matter rate lives: $\omega\le qv_{\max}$, the low-energy side of $L$, and the rung spread. The flags above are precision and notation, not blockers. **Verdict (c): MINOR GAPS.**
