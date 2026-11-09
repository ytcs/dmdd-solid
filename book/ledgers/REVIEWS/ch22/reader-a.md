# Chapter 22 mock-reader review: persona (a)

Persona (a). Read tex/ch22/*.tex linearly plus the rendered fig22_1.pdf; back references checked in
Chs. 8, 13, 19; Appendix E not read. Every number in Worked Examples 22-fsum, 22-cc and 22-constant
reproduces (mpmath/numpy), including the local-model band-sum fractions.

## Chapter opener
- Clear; its hooks (Si window 0.333-0.405 MeV, Ge edge, 100 eV recoil) agree with secs. 13.9, 19.2.

## 22.1 Calculations specified but not done

**Lost points**
1. Line 3 says the phonon-assisted (PA) rate is "the only electron-recoil rate between 0.333 and 0.405 MeV".
   The first row of tab:22-calc says "rate and reach from 0.333 to 0.43 MeV, now known to a factor of ten".
   Rereading sec. 13.9 settles it: PA alone up to 0.405, PA leading up to about 0.43, two channels from
   0.43 to 0.51. On a first pass the two ranges look like a contradiction. Fix: half a clause in the table,
   e.g. "(alone to 0.405)".
2. sec:22.1-checks (line 9 to 15) packs about 20 equation references into four paragraphs, among them
   eq:8.6-fsum-e/-k/-ek, eq:13.7-fsum, eq:8.3-M3lim, eq:13.9-glide, eq:D.43-moments and eq:20.1-Fpos. As an
   index this is fine. Still, two items depend on recalling a precise statement and are not restated even
   in a phrase: "the Fano term ... vanishes at the level of one-body self-energies" (sec. 8.6) and the
   "mixed third moment" (eq:8.3-M3lim). I had to go back. Not blocking.
3. Worked Example 22-fsum, "The transfer rule": the tolerance "about 2 percent of either, 1.8 percent at
   theta_ep = 0.010 and 2.1 percent at 0.016" is not derived. I reconstructed it as
   theta_ep^2/theta_ep + 7.8e-5/theta_ep, which gives 1.0 + 0.78 = 1.78 percent and 1.6 + 0.49 = 2.09
   percent. That matches, but the text should say that the two error sources are added and that both are
   divided by the sideband's own share theta_ep. One sentence would do it.
4. Table row "Migdal row of the guide ... largest P(first) 0.315" uses P(first) and "survivors" from Ch. 21
   with no gloss. I remembered them, but a reader who skipped Ch. 21 would not.

**Steps I could not reproduce**
- None in the text proper. "The sum over the bands above N is one expectation value, eq:E.14-remainder"
  points to Appendix E, which I have not read. I took the identity on trust; it is plausible as a closure
  relation.
- Reproduced: q^2/2m_e = 0.9785 eV, 4 q^2/2m_e = 3.9139 eV; Z_v m_e/M_cell = 7.81e-5; 2 percent /
  theta_ep = 1.25 to 2; the Cauchy-Schwarz bound (split sqrt(Delta_m) between the factors).
  - Local-model band sums: Cohen-Bergstresser Si (sec. 3.3), 531 plane waves, q = 1 keV [100] gives
    0.1514, 0.9265, 0.9939, 0.9992, 0.9996 for 8-100 bands as printed; target 3.1135 eV at
    k = (0.1,0.2,0.3) 2pi/a; closure to about 1e-13. Very satisfying.
  - 8.5e-5 MeV per 0.3 meV (0.283 MeV/eV of sec. 13.7); two-pair envelope 0.173/0.030 = 5.8.
- Figure 22.1: 11 calculation, 10 data, 2 theory filled circles over 22 rows; matches line 120.

**Used before defined (within this chapter; all defined earlier in the book)**
- theta_ep, delta_NL, q_BZ, Q*, theta_ii, F_eh, E_reorg/eps^hop, curly Q, P(first), "survivors",
  "the guide". All are recalled by pointer only. Acceptable for an index chapter, but the table is
  hard going for anyone who is not fresh from Chs. 12 to 21.

**Too slow / too fast**
- Slow: the Si PA factor of ten appears four times (opener, line 3, line 79, summary).
- Fast: the table; several "Result" cells are four bare numbers (e.g. "Velocity couplings").

**Learning outcomes (inferred)**
- *Name, for an open calculation, the result it changes and its checks.* Yes. Ge zero-phonon edge: L
  below Gamma, L gap within 0.1 eV of 0.744 eV, band masses, TA branch against neutron data.
- *Carry out the band-sum f-sum check and say what a shortfall means.* Yes. I reproduced it (above). I can
  also say why the total f-sum cannot see the sideband: the sideband is 1 to 1.6 percent of the sum, below
  the 2 percent tolerance.
- *Classify a channel as limited by theory, calculation or data.* Yes. Example: ZrTe5 is data-limited,
  because its background tensor moves the reach by 2.8.

## 22.2 Exact gaps in the theory

**Lost points**
1. **The counts disagree with the summary.** Line 19 says the missing step is "a calculation in 55 rows, a
   measurement in 11 and a proof or method in 6". The summary says 53, 11 and 8. Both add to 72, so one of
   them is wrong. Counting from the table, I get 5 proof rows plus Dirac at alpha-tilde >= 1 (method) plus
   sec. 11.5 ("a real-time method ... or neutron Compton scattering"), and arguably sec. 14.4 ("None from
   neutron data alone: the isotropy hypothesis ..."). That is 6 to 8 depending on how the mixed rows are
   read. Fix: make the two consistent and say how mixed rows are counted.
2. Line 13 says the missing step is "single in the sense that nothing else stands between the statement
   and the result". Several rows list more than one step:
   sec. 16.6 ("four factors open", three measurements); sec. 21.7 backgrounds (forbidden shapes, 210Pb,
   production rates); sec. 14.2 (two materials plus existence of a bound pair).
   A careful reader notices the tension with the definition. Fix: allow "a single step, which may have
   several parts", or split those rows.
3. Line 15 uses delta_X ~ +0.28 as the example of a *nuisance*. Yet tab:22-gaps lists "Attraction ~ +0.28
   over the 3 MeV window" as a *gap* (estimate). The next sentences explain the sized/open split, but they
   use the PA sideband as the example, not this one. Fix: use the same item for both, or say explicitly
   that the attraction is itself such a split item.
4. The block heading "Chapter 22. Outside the framework" contains the CDW row, which sec. 22.3 says lies
   *inside* the framework. Minor.

**Steps I could not reproduce**
- None. Reproduced from the table: Limits classes 5/10/18/34/5 = 72; Chs. 10-13 29 rows (6 unsized);
  Chs. 18-20 17 rows (12 unsized); the 11 measurements of line 158. Worked Example 22-constant:
  3.232 x 1.160 = 3.749 eV; 10/3.749 = 2.667; +0.35 -> 3.017 (13.1 percent); 0.3 and 7.1 percent;
  1 percent reached at 131 eV.
- "the step model's +0.19" is not introduced in the example. I assume it is from Ch. 18, but a pointer is
  needed.

**Used before defined**: U_qp, h_off, kappa_BO, the "Dyson convention", the Markov-Krein band,
S_HR, b_br, the marks m and r_med appear in table cells by pointer only. This is acceptable in an
index. "superadiabatic generator" (line 3) is used before the table gives any context; it is from sec. 8.6.

**Too slow / too fast**: The definition and the gap/nuisance distinction are well paced. The closing
"shape of the table" paragraph is useful.

**Learning outcomes (inferred)**
- *Define an exact remaining gap versus a nuisance.* Yes: strongest statement plus one missing step,
  against a truncation with a sized next order that enters the likelihood with a width.
- *Read a gap from its home and decide what it limits.* Yes. I followed Worked Example 22-constant and
  the contrasting ZP/PA ratio (estimate, which moves the takeover mass).
- *Know which gaps share a missing step.* Yes: BSE Si/Ge, Ge bands with SOC, b_br, mK exciton rates.

## 22.3 Channels outside the framework

**Lost points**
1. **Nuclear physics goes too fast for persona (a).** Isospin, tau^+, Gamow-Teller, "shell model",
   "allowed approximation", "first-forbidden" and the "isobaric analog state" are not in the assumed
   background. They arrive in two paragraphs.
   "a ground state of total isospin T_iso = (A - 2Z)/2" is asserted (minimal T = |T_z|), and the Fermi
   sum follows from T-T+ = T^2 - T_z^2 - T_z = 2T. One displayed line would carry a reader who knows
   only angular-momentum ladder algebra.
   I could do it from QM ladder operators, so this is not blocking.
2. Worked Example 22-cc says "at fixed matrix element the rate would grow with the electron phase space, as
   p_ej". The two-body phase space is p_ej E_ej (total energy), not p_ej. The later ratios (pF -> 0.51) are
   stated for p_ej F only, so they are correct as written. Still, "rate ~ p_ej" is not quite right. At
   626 keV versus 10 keV, the factor E_ej changes by 1.137/0.521.
3. The paragraph on the Dror et al. convention says the printed function "is therefore larger by
   Gamma(1+2gamma)^2/Gamma(1+gamma)^2, ... 3.2 at Z_d = 53". It also prints 2(1+gamma_d) instead of 4.
   With both differences the ratio at Z_d = 53 is 3.10, not 3.22 (at Z_d = 1 both give 4.0). Either say
   "the gamma functions alone make it larger by" or quote 3.1.
4. CDW paragraph: the massive phason is "lifted ... to the plasma frequency of the condensed electrons", and
   this is identified with a 0.951 meV mode. A plasma frequency of 1 meV puzzled me. Presumably it is
   because the condensate carries a large (Frohlich) effective mass, but the book never says so. One clause
   is needed.
5. "The density row ... can excite modes 263 to 315 times below the charge gap": the phrasing is odd. I
   read it as "modes lying 263 to 315 times below the charge gap". Minor.

**Steps I could not reproduce**
- None. Reproduced with mpmath: p_ej = 1.0157 MeV, y_S = 0.4329, r_A = 6.0 fm, p r_A = 0.0309;
  F(53, 626 keV) = 6.338, F(52) = 6.062 (4.35 percent lower); F(53, 10 keV) = 32.55, F(53, 1 keV) = 102.1;
  pF ratios 0.514, 0.507; p ratios 0.100, 0.0315; 1/p = 194, 1942 fm; a0/53 = 998 fm; the
  nonrelativistic limit 2 pi y/(1 - e^{-2 pi y}) via Gamma(1+iy)Gamma(1-iy) = pi y/sinh pi y.
  Sum rules: 2T = A - 2Z = 21; Ikeda 3(N - Z); analog threshold (6/5)Z e^2/r_A - (m_n - m_p) + m_e =
  14.2 MeV; 73/21 = 3.48. CDW: 0.23 THz = 0.951 meV; 2 omega/v_max^2 = 271 eV (v_max = 2.650e-3);
  189 keV per keV; 263 and 315. Consistent with sec. 8.2 (m_V <~ 20 A mu) and sec. 19.3 (Born 117).

**Used before defined / notation**
- gamma_d (Fermi function) appears beside gamma_mu and gamma^5 (Dirac matrices) in the same subsection.
  It is readable, but it is a clash. Gamma is explicitly disambiguated from the Gamma point, which is good.
- "Fano" means the interference term in sec. 22.1 (line 15) and the Fano factor F_eh elsewhere in the
  chapter. That is a mild clash.
- Lee-Fukuyama, the Ward identity, Goldstone: the first is new and attributed. The others were used earlier.

**Too slow / too fast**: The scope subsection (three properties plus a fourth class) is excellent and well
paced. The charged-current part is fast on nuclear physics (item 1). The CDW part is fast on condensed-
matter mechanism (item 4). Radiative decay and ion tracks are well paced.

**Learning outcomes (inferred)**
- *State the properties of the amplitude that the master formula needs, and classify a process.* Yes:
  species-conserving one-body rows, a free plane wave out on the dark side, a Gibbs initial state read as
  an excitation, plus the Born and coherence conditions of sec. 8.2. Example: radiative decay of chi_2
  breaks the first, because there is no target operator.
- *Explain why charged-current absorption has no D_ab x S_ab form, and when it factorizes.* Yes. The
  outgoing electron's distortion belongs to |f> (Z+1), and the squared amplitude is non-local in r, r'.
  It factorizes when p_ej r_A << 1 and E_ej is large enough that screening does not matter.
- *Evaluate the Fermi function; apply the Fermi/Ikeda sum rules.* Yes, reproduced above.
- *List the checks a CDW response must pass.* Yes: the Goldstone pole for an incommensurate wave (gapped
  if commensurate), the f-sum, the measured phason/amplitudon frequencies, and the kernel from the same
  functional as the distortion.

## Summary section
- **Error:** "the Fermi function is 6.34, 4.3 percent more than with the charge of the parent". 6.34/6.06
  is 4.5 percent more. The parent value is 4.3 percent *lower*, as sec. 22.3 correctly says.
- The missing-step counts 53/11/8 conflict with sec. 22.2 (55/11/6); see 22.2 item 1.
- Otherwise it is an accurate digest.

## Overall
I would keep reading; this is a closing index, and it works as one. Every derived number I tried
reproduces, including the band-sum fractions of the local model, which made the f-sum check concrete. The
blocking-level problems are none. The real defects are bookkeeping: the 55/6 versus 53/8 count, the
summary's "4.3 percent more", the 0.405/0.43 range on a first read, and the 3.2 versus 3.1 convention
factor. Two pacing gaps remain: nuclear isospin in sec. 22.3-cc and the CDW plasma-frequency step. Both
can be fixed with a sentence each.

Verdict: **MINOR GAPS**
