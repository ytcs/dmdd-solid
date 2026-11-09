# SEAM: E.5 Wannier functions in practice

Length (detex): appE/E-5.tex 3,431 words (budget 5,500; equations and the enumerate dropped by detex; not padded). Build/lint as E.4 (no hits
except long-sentence notes). Sources: sources/E-b/ 1202.3454 (Noffsinger), 1803.05462 (Poncé 2018), 2002.00628 (Brunin), 1604.03525 (EPW),
1112.5411 (Marzari RMP), cond-mat_0108084 (Souza), 1510.06373 (Verdi–Giustino); register/1603.06965 (Giustino RMP).
Bib added: verdi2015frohlich, brunin2020electron, souza2001maximally.

## The reader now knows
- Wannier interpolation of bands and of g (eq:E.5-ginterp = Giustino Eqs. (177)–(179) in A.6 normalization); interpolation is numerical, no 𝔗 component.
- Si projections: 4 bond WFs (isolated valence) vs 8 sp³ (disentangled); inner/outer windows (Marzari Fig. 5); Noffsinger 26 WFs from 34 bands
  (−10/+30 eV); four checks (spreads, centres, real-valuedness, off-grid bands); Si CBM at 0.85ΓX → 12³ coarse k (Poncé 2018).
- Decay of g^W: R_p⁻³ nonpolar, dipole R_p⁻² polar; diamond 4³/6³/8³ (Giustino Fig. 6); g^L (eq:E.5-gL, derived in HL from bound charge; Giustino
  Eq. (180)); quadrupoles nonzero in Si; omitting them: ~10% (Si), ~30% (GaAs) mobility error (Brunin).
- One gauge for g, v, ρ, energies; velocity rescaling with QP energies (eq:E.3-vrescale).
- ρ at DM momenta: small-q Wannier expansion fails (q × bond length ≈ 1.2 at 1 keV); direct ρ on coarse grid per target q, rotated with same U.
- WE (we:E-counts): 40³ Si counts: 4.1e9 pairs, 270 TB of vertices (never stored), 4 GB per Q, g^W ≈ 3 GB, ~3e16 flop, /48 symmetry,
  window fractions (δ = 0.3 eV, m* 0.5/0.32) → 3.5e5 pairs.
- α²F/γ^ep: double-delta smearing criteria; Pb: 14³/10³ DFPT, 0.025 Ry, 6³ coarse, 4e5 Sobol k + 2.7e4 q (EPW Fig. 12).
- ε₂^PA convergence: 40³ ↔ 14 meV, 24³ ↔ 30 meV, Γ_w = 100 meV insensitivity, rigid shift 0.15–0.23 eV (gap error + e–ph renormalization).
- Route of a phonon-assisted electron-recoil calculation (6 steps), controls (optical limit, g → 0, f-sum with δ_NL of eq:E.2-fsumNL), cost
  estimate ~1e16 flop (≈17 min at 1e13 op/s, 2–3 days at 5e10) (δ = 0.1 eV pockets on 120³, ~3e7 pairs per q (three valence bands within 0.1 eV), several hundred q), scaling δ³ and N_fine⁶.
## Symbols introduced
- g^W_{m'n'κα}(R_e, R_p) (eq:E.5-ginterp); R_e, R_p (electron and phonon lattice vectors of the Wannier transform); N_W (number of Wannier functions);
  N_fine (fine-grid points per direction; renamed from N_f); δ (energy window above a band edge, local to WE); τ_κ (atomic position in the cell; check NOTATION).
## Terms introduced
- disentanglement, inner (frozen) and outer windows (practical); dynamical quadrupole; Sobol sampling; energy windows / pockets.
## Threads
- T5 (silicon phonon-assisted window): advanced (method and cost only; edges are left to 13.9).
## Promises
- Edges stated in 13.9; window kinematics in 13.1; optical-limit control in 13.5.
## Proposed ledger rows
NOTATION: g^W | real-space (Wannier-gauge) electron–phonon matrix | eV Å⁻¹ | E.5 · R_e, R_p | lattice vectors of the electron hop and of the displaced atom | Å | E.5 ·
N_W | number of Wannier functions | 1 | E.5 · N_fine | fine-grid points per direction | 1 | E.5 · GLOSSARY: disentanglement; frozen window; dynamical
quadrupole · CLAIMS: Noffsinger grids/resolution [cited]; Brunin 10%/32% [cited]; 40³ counts [derived]; PAER-route cost ~1e16 flop (≈17 min at 1e13 op/s, 2–3 days at 5e10) [derived estimate] ·
INDEX: Wannier interpolation; electron–phonon vertex, interpolation; Fröhlich vertex; Eliashberg function, convergence.
