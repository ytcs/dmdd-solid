# Chapter 9 — mock reader (a), isolated review

Persona: first-year PhD student entering direct detection; has read Chapters 1–8. Source read: tex/ch09/*.tex
(the PDF is stale for this chapter). I did not read Chapters 10–22, and judged forward pointers by their glosses.
Numbers were checked in Python with v_max = 794.5 km/s = 2.6502e-3 and 2/v_max^2 = 2.8476e5.

**Verdict: MINOR GAPS.** Nothing blocks the material that follows. All derivations I attempted reproduce.
There are five internal inconsistencies (plasmon cutoff, cell count, box count, NiO label, 45 vs 46.7 MeV)
and a few numbers stated without the step that gives them.

## Chapter opening
Not lost. The 3.5 eV for 1 MeV reproduces (½ m v_max^2 = 3.51 eV); the three questions are a clear contract.

## 9.1 The excitation–interaction matrix

**Checks done.** Counted from the tabular: 24 rows, 54 filled cells (column totals 14/6/8/11/10/5), 90 empty.
All of these match the text. The vector column holds 11 cells, as the worked example says. Absorption
kinematics: c·v ≈ 2.5e-8 of m_phi ("some 1e-8") holds. A free nucleus needs m_phi = 2M/v^2 (impossible), and
MHz modes in a mm crystal (c/L ≈ 9 MHz) hold. The dark photon's B' smaller than E' by v holds.

**Lost points**
1. *Last paragraph of WE 9-darkphoton:* it says "two of the last [column]". But the example itself
   names three cells: 10.9 (pairs), plus 17.3 for plasmons and 17.3 for optical phonons. Either the count or the
   list is wrong. Fix: say "three", or say which 17.3 cell is excluded.
2. *WE 9-darkphoton, nuclear column:* the example opens the Migdal cell of the nuclear column. It never says
   whether the dark photon reaches the free-nuclear-recoil cell (11.4), which lies in the same column, at large q.
   "Above the zone ... the charge vertex of the multiphonon response in 11.3" covers multiphonons only.
   One sentence on the impulse regime would close this.
3. *Table 9-atlas legend:* "--- no channel at leading order". Sec. 9.1-empty then says that some "---"
   cells are allowed but not computed (a core-electron spin flip, pair breaking by spin, spin plus Migdal).
   The legend hides that difference. A reader who scans the table for gaps will think they are forbidden.
   Fix: give these cells a different mark, or name them in the caption.
4. *Columns paragraph:* "a coupling to n_e appears in the first column when elastic and in the last when
   inelastic". Two paragraphs later "No new response" says the last column is mostly empty because its rate
   follows from the elastic cell. These read together are confusing at first. A clause in the first passage
   ("only where the kinematics change the physics, see below") would settle it.

**Steps not reproduced:** none. **Used before defined (relative to Ch. 1–8):** none that blocked me. The operators O_1…O_15, the n_s, s_s, j_s
and T_s rows, the P_0/P_ad/P_+ sectors, S_{eκ} and the Dyson/Fano terms are all in Ch. 8. "ad^s" and "qp" are
new, but the caption and 9.1-sectors define them.

**Pace:** the column paragraph of 9.1-axes is too dense (six columns, operator lists, four kinematics); a list
would read better. The dark-photon example is long and partly a directory of section numbers.

**Learning outcomes (inferred)**
- *Read the atlas by row (detector) and by column (model).* Yes.
- *Give each row its sector and say what adds and what is one response.* Yes. Example: pairs, plasmon, exciton
  and core are one S^0_ee constrained by the f-sum rule; Migdal splits across P_0 and P_+.
- *Explain an empty cell by one of the four rules.* Yes. Tried: the density operator cannot make a magnon
  ([n_e, S_tot] = 0, ΔS = 1); multiphonon absorption is empty (a linear-in-u vertex at q→0 makes one phonon).
- *Select a model's cells.* Mostly. Tried O_4 = S_χ·S_e in Si: pairs (10.4) and excitons (10.5), with no
  lattice cell. I needed the prose ("nuclear spins reach the lattice only via 11.6") to know that the spin
  cells of the phonon rows are nuclear-spin cells. The column header does not say this.

## 9.2 The kinematic map

**Checks done (all reproduce):** Eq. 9.2-mch and its bound 2ω_th/v^2. Floors: Al 0.10 keV, GaAs LO 10.35 keV,
Si optical 18.3 keV, Ge 3d 8.5/8.7 MeV. Acoustic edges: Si 6.12, Al 8.60, Ge 10.19 keV; Si transverse 9.76 keV;
factor 21.5; NiO 7.31 keV. ZrTe5 by numeric minimisation: 7.12/9.66/8.04 keV, exponents -2.12/-2.76/-2.36
(text: 7.1/9.6/8.0, -2.12/-2.74/-2.37). Si offset bound 0.474 MeV. Free recoil 17.5 MeV; it meets the floor
exactly at m = M. Eq. 9.2-halo: -2 and -1.012; 3.15%, 6.3%/3.2%, exact -6.0/+6.6%. Every number in WE 9-acoustic.

**Lost points**
1. *Core shell, Si 2p:* "whose opening momentum is 38 keV, at 2×38 keV/v_max = 28.7 MeV". This is not the
   flat-onset formula of the same paragraph (2E0/v^2 at q̄ = 2E0/v). I recovered it only by noticing that
   38 keV × v_max = 100.6 eV ≈ 99.4 eV + E_g, so "2×38 keV/v_max" is just 2E0/v^2 rewritten. Calling 38 keV an
   "opening momentum" also suggests a threshold in q, and with E0 ≈ 100 eV, q̄ = 76 keV ≠ 38 keV.
   Fix: write 2(99.4 + 1.17) eV / v_max^2 = 28.7 MeV, as was done for Ge 3d.
2. *Offset minimum:* "A phonon can take up the mismatch of momentum for 15 meV or less." Why 15 meV? The
   absorption paragraph puts the lowest phonon-assisted state of cold Si at 1.1728 eV, whose floor is 0.3340
   MeV. That is above the quoted scattering onset of 0.3332 MeV. I worked out that in scattering the dark matter
   supplies part of k_c, so the phonon needed sits at smaller momentum and costs less energy (E_g - 14.7 + 15 meV
   → 0.3332 MeV). The text never says this, and without it the 0.3332 looks like it is below the floor of its
   own final state. One sentence is needed.
3. *Plasmon closure:* the text says "phase velocity stays above 9.54e-3". The Fig. 9.2 caption gives the
   dispersion ω_p^2 + (3/5) q^2 v_F^2 with ω_p = 16.6 eV. With v_F = 6.98e-3, the cutoff is at 2.24 keV (as in
   the caption), and the phase velocity there is 9.18e-3, not 9.54e-3. The conclusion (≈3.5 v_max, closed)
   stands, but I cannot reproduce the number. See also 9.3, point 1.
4. *NiO zone-centre magnon:* here it is placed at 4.54 meV "by far-infrared absorption". Table 9-supports gives
   "gap 4.54 meV (model)". Which is it?
5. *Mass for free recoil to take up the gap:* "about 45 MeV" here, 46.7 MeV in 9.3. With E_g = 1.17 eV I get
   46.7. "About 47" would remove the visible mismatch.
6. *Annual shifts:* with 781/810 km/s I get -3.8/+3.5% (floor) and -1.9/+1.7% (acoustic). The text has
   -3.9/+3.4 and -2.0/+1.7. This is probably rounding of the endpoints taken from Ch. 1, but I cannot reproduce
   it exactly.

**Used before defined:** none (E_th, v_E^ref, eqs. 1.3-mmin and 3.3-allowed are in Ch. 1/3).

**Pace:** the derivation of the lightest mass and the five shapes is excellent and at the right speed. The
offset-minimum paragraph is too fast. It holds about twelve numbers from four materials, the 15 meV argument is
missing, and the Ge zero-phonon estimate "bounds the edge in neither direction" is stated but not explained. The
Fig. 9.1 caption is very long.

**Learning outcomes**
- *Compute the lightest mass for a given dispersion shape.* Yes. Tried a gapped branch for ZrTe5, and the
  acoustic edge of Ge (10.2 keV).
- *Explain why an acoustic edge sits v/4c above the floor, and when a branch is closed (c ≥ v_max).* Yes.
- *Give the halo exponent of an edge.* Yes. -2 flat, -1 linear, below 2 in magnitude for a falling E_ch.
- *Read the map as reach and not rate.* Yes. The last paragraph before the WE makes this point well.

## 9.3 Excitations on the momentum–energy plane

**Checks done (all reproduce):** 2W at 1.59–53 keV (0.0016 … 1.8). E_R(5 keV) = 0.48 meV. sqrt(2ME_g) = 247 keV
and 46.7 MeV. x_R = 1 at 46 keV. Impulse at 92.5 keV ↔ 17.5 MeV. Lengths of k_c + G (1.94 … 5.32 keV); the
0.72 keV gap gives 0.107 eV. Reach of 0.3/1/10 MeV. All numbers in WE 9-open (1.11 MeV, 195 km/s, window
2.29/2.01 eV, Migdal 2.1e-8). Table 9-overlaps: 5.47e-4, 5.1e4, 196.

**Lost points**
1. *Plasmon cutoff:* the caption gives "up to its cutoff at 2.24 keV". The text says q_c = 2.60 keV twice, and
   the reach paragraph and WE 9-open use 2.60 again. Only one can be right for the drawn line. From the
   caption's own dispersion I get 2.24 keV. If 2.60 comes from a different model (Lindhard, or the measured
   16.4 eV), say so. Linked to the 9.54e-3 phase velocity of 9.2.
2. *Plasmon start:* the text says it starts at the measured 16.4 eV, while the dashed line uses ω_p = 16.6 eV
   (free-gas value). This is harmless, but name the 0.2 eV difference.
3. *WE 9-open, Migdal estimate:* "δM_κ/M_κ = 2.7e-4" appears without a gloss. In 8.6, δM_κ is a tensor. The
   number equals Z m_e/M_κ (14 × 0.511 MeV / 26.16 GeV). Saying "the electron mass carried with the nucleus,
   Z m_e/M_κ" would save a look-up.
4. *Three meanings of "free" recoil:* this section uses the impulse onset at 92.5 keV (four mean phonon
   energies, 0.164 eV, also in Table 9-edges). 9.4 opens with "nine phonon energies" (Lim 1.3a), and WE 9-place
   gives x_R ≥ 2.3 (Lim 11.4a). WE 9-place reconciles 9 with 2.3, but the 4 used for the map and the plane is
   never placed against them. One sentence in 9.3 or 9.4 would fix this.

**Steps not reproduced:** the E_min values along [100]/[110]/[111] (3.17, 1.77, 2.59/2.02/2.31 eV) and the
loss-function values. These come from band and table data I do not have, which is acceptable for a figure.

**Used before defined:** none (δ_w, the window, θ_ep and the Fano term are all in Ch. 8).

**Pace:** the prose is right. The Fig. 9.2 caption is about 20 lines. It is a legend and a methods section
together, and the methods part (quantiles, PBE, gap set to 1.11 eV) could go to the text or a footnote. The
overlap section is the clearest statement I have read of "overlap is not interference". The 196 + 196 example
is memorable.

**Learning outcomes**
- *Place a (q, ω) point and say which sectors are open.* Yes. Tried q = 1 keV, ω = 1.3 eV: P_ad is closed
  (2W ≈ 0.0007, about 20 phonons needed). P_0 is closed (E_min = 1.77 eV). P_+ is open, inside the window
  (1.3 < 1.47). This matches the opening paragraph.
- *Say where interference is possible and how large it is.* Yes. There are two mechanisms and four regions,
  and only region 1 matters at leading order. *Read a mass's reach on the plane:* yes.

## 9.4 Limit Checks and the truncation label

**Checks done.** Counted Table 9-limitchecks: 75 boxes, 27 on the label (X 12, K 6, n_A 3, M 3, n_D 2,
n_T 1), and 48 on qualifiers (5/9/5/29). By chapter: 12 has 7/9, 10 has 8/15, 11 has 7/20, 14 has 0/8, 16 has
2/17. All match the text. 9 × 60 meV = 0.54 eV and (E_R ω0)^{1/2} < E_R/3 ⇔ x_R > 9: reproduced.

**Lost points**
1. *Opening paragraph:* "recover 90 published formulas ... and give 75 of them a box". 9.4-appF says that 80
   of the 90 rows belong to the 75 boxes (one box can hold two formulas), and 10 have none. So 80 formulas have
   a box, not 75. Fix: "and check 80 of them in 75 boxes".
2. *WE 9-place, loss-function rate:* "in a model of the acoustic peak at 1 MeV, the electron-only coupling has
   more than 1e4 times the electronic rate". Is 1 MeV the dark-matter mass? And is "the electronic rate" the
   rate above the phonon band? Make the referents explicit.
3. *WE 9-place, crystal form factor:* "0.22 at q_0". q_0 = α m_e is from Ch. 1, but a reminder in parentheses
   would help, because the box itself is in Ch. 10.
4. *Table 9-limitchecks order:* 11.5c is listed before 11.5b, and 16.7d before 16.7c. This looks like a
   generator sort, and it is confusing when checking off boxes.

**Used before defined:** none (𝔗, δ_k, n_B, n_g, n_D, ξ_D, x_R, 𝔐, 𝒦 are in 8.5/8.8). A three-word gloss on n_B
(order in the nonadiabatic coupling) at "n_B = 0 ... n_B = 2" would spare a look-back.

**Pace:** 9.4-plot is clear. The counting paragraphs and 9.4-appF are bookkeeping a student skims. WE 9-place is
the best part; the contrast of the two impulse boxes (x_R ≥ 9 vs 2.3) teaches that the band edge depends on the
quantity compared.

**Learning outcomes**
- *Say what a Limit Check box contains and how to read its band.* Yes.
- *Place a formula on 𝔗 and choose its controlling parameter.* Yes. Tried: Migdal at dipole order → n_D = 2, ξ_D.
- *Read a formula's status from what the plot compares with.* Yes (calculation, model, or nothing shaded).

## Summary section and forward pointers
The summary agrees with the body and inherits only the errors above. Almost every forward pointer carries a
usable gloss ("which treats ..."); bare entries in Tables 9-atlas and 9-edges are acceptable as tables.

## Overall
I would keep reading. The chapter does what it promises. It gives a map of which channel lives where, why each
empty cell is empty, the lightest mass by shape, and where amplitudes can and cannot interfere. Sec. 9.2 and the
overlap discussion in 9.3 taught me things I will use. The problems are local consistency errors: plasmon
q_c 2.24 vs 2.60 keV, "two of the last" vs three cells, 75 vs 80 formulas with boxes, NiO "measured" vs "model",
and 45 vs 46.7 MeV. There are also two missing steps: the Si 2p edge formula, and why the phonon-assisted Si
onset can use a ≤15 meV phonon. None of these blocks Part II.
