# SEAM: E.11 Molecular dynamics and machine-learned interatomic potentials

Length (wc): E-11.tex ≈ 3,900 words (budget 3,500). No App. D file. Lint: 0 blocking; remaining LONG-SENT hits are subsection
headers merged with first sentences, the r_min tabular and the table caption. Build: wrapper (E-11..13 only, own outdir) clean;
0 undefined citations; undefined refs only to unwritten sections. One overfull header box (31 pt, long running head): editor may add
a short title. Sources: sources/E-d/{1805.01568, 2206.06772, 2002.03525}.txt.
Coordinator change applied: \cref{sec:16.8} → \cref{sec:19.6} (three places). Note: SPINE row E.11 on disk still lists "→ 16.8".

## The reader now knows
- Classical MD on E^ad({R}) (eq:E.11-newton); place on 𝔗: n_B = 0, all anharmonic orders, beyond the impulse regime of 𝒦; classical nuclei; electronic losses absent (→ 19.2).
- DFT cost ∝ N_at³ (derived); locality decomposition (eq:E.11-local); SW/Tersoff vs MLIP families (Behler–Parrinello, GAP, ACE, NequIP, MACE).
- GAP-18 silicon: eq:E.11-gap (pair + kernel), 5 Å cutoff, 2475 cells / 171,815 environments, PW91 250 eV; point-defect energies within 7%; 100 ms/atom.
- Why thermal training sets miss close pairs (Boltzmann weight e^{-51/0.17}); ZBL potential (eq:E.11-zbl), a_U(Si–Si) = 0.128 Å; head-on r_min table
  (1.49 Å at 20 eV … 0.18 Å at 10 keV); splice (eq:E.11-splice) and its design rule.
- Time step from v_max (0.26 Å/fs at 100 eV; 0.19 fs and 0.06 fs at 0.05 Å/step); cell 4096 atoms, 6 Å thermostat border, 20 ps (Sassi).
- Cascade statistics: ≥ 1000 directions; Wigner–Seitz occupation; p_FP and binomial error; E_d as lowest crossing; SW minimum 18 eV (Si), 13 eV (Ge, mod. SW).
- Quench protocol (eq:E.11-Est); residual heat 0.53 eV per K in 4096 atoms; shared table of defect energies.
- CI-NEB, harmonic TST Γ = Γ_0 (italic \varGamma) e^{−E_b/T}; useless at 10 mK (e^{−1.2×10⁵} for 0.1 eV) → tunneling (19.6) or phonon activation (E.12).
- Cost: GAP 410 s/step for 4096 atoms; 2×10³ core-h per trajectory; 5×10⁷ core-h per 1000×20 scan (derived). Pitfalls; Table tab:E-md-si (title now "Recoil molecular dynamics").

## Symbols introduced (with defining equation)
- E^at_κ(𝒩_I) local atomic energy, 𝒩_I neighborhood, r_c cutoff (eq:E.11-local); V^(2), K, α_s, M_rep (eq:E.11-gap);
  V_ZBL, φ, a_U, Z_1, Z_2 (eq:E.11-zbl); r_min; f_sw, r_sw, b_sw, E^ad_ML (eq:E.11-splice); p_FP(E_R, r̂_R), N_dir, N_at, N_im; E_b, Γ_0; E^ad_min (eq:E.11-Est).
- Used: E^ad (5.1), M_κ, E_R, E_d, E_st, r̂_R (Sect. 19 tables use r̂_R).
## Terms introduced
- primary knock-on atom; machine-learned interatomic potential; descriptor; ZBL potential; splice; quench / inherent structure; nudged elastic band (climbing image).
## Threads: opened / advanced / closed
- None (method appendix).
## Promises made to later sections
- 19.2 treats electronic losses on the MD trajectory; 19.6 turns NEB barriers into tunneling rates; 19.4 uses p_FP and E_st distributions.
- The E′ specification (partition tables, quench protocol) is not pointed to: target is App. E.14–E.27 (merged).
## Proposed ledger rows (the editor merges them)
NOTATION: E^at_κ | local atomic energy of an interatomic potential | eV | E.11 · V_ZBL, a_U | ZBL screened pair potential and screening length | eV; Å | E.11 ·
r_min | head-on distance of closest approach | Å | E.11 · f_sw, r_sw, b_sw | ZBL switch function, center, steepness | 1; Å; Å⁻¹ | E.11 · p_FP | Frenkel-pair survival
probability of a recoil | 1 | E.11 (check vs P_FP of E.23 / p_surv of 19.4) · E_b, Γ_0 | barrier, attempt rate | eV; s⁻¹ | E.11 · N_at, N_dir, N_im | counts | 1 | E.11.
GLOSSARY: machine-learned interatomic potential; ZBL potential; quench protocol; nudged elastic band. CONCEPTS: E.11 needs 5.1, 5.2, 5.7, 7.4, 8.5.
CLAIMS: GAP-18 numbers [cited 1805.01568]; SW thresholds [cited 2206.06772 Table II]; r_min table, time steps, 0.53 eV/K, cost [derived].
INDEX: molecular dynamics; interatomic potential; Gaussian approximation potential; ZBL; stored energy (quench); threshold displacement energy (computation).
