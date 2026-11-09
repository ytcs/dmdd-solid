"""Full-band silicon cascade: every number of it quoted in Chap. 18 (Sects. 18.1, 18.3, 18.4, Summary, nuisance table).
Run: python fbc18.py > fbc18.log  (a second).  Data: fbc18_data.json (copied from the full-band Monte Carlo; provenance in
its "_provenance" field).

Model (stage 1 of a full-band calculation; no constant fitted to the pair energy):
  bands: local empirical pseudopotential of Cohen and Bergstresser (form factors refit to measured transition energies);
  impact ionization: golden rule with the diagonal statically screened Coulomb kernel (model dielectric function of
     Cappellini et al.) on the full zone, direct and exchange terms combined as in Kane's form quoted by Kotani and van
     Schilfgaarde (arXiv:0812.2923, Eq. (5)); exchange factor R_x = Gamma_full/Gamma_direct computed above 3 eV, 0.75 below
     (range 0.5-1.0 carried in the envelope);
  phonons: deformation-potential couplings of Lundstrom's textbook (Li et al. footnote a; hole D_ADP also credited to
     Jacoboni and Reggiani) as tabulated by Li, Graziosi and Neophytou (arXiv:2104.08998, Table III), with the first-principles ratios of the same table (electrons x 0.52, holes x 3.0)
     as variants;
  E_g = 1.160 eV (123 K); cascade stops when every carrier has E < E_g, residual booked as heat.
Envelope: joint corners of screening (static Cappellini, static Resta, dynamic band RPA) x phonon set (JR, first principles)
x threshold R_x (0.5, 1.0), plus the two single-carrier phonon corners; k-grid term +-8 % (5 eV) applied to P(N >= 2).
Model-class systematic (not in the envelope): at least +-0.4 eV in eps, the shift between Nielsen and Fischetti's two
loss functions (TDDFT 3.10 eV, GW/BSE 3.50 eV; arXiv:2610.16949).
"""
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "fbc18_data.json")))
P, E = D["primary"], D["envelope_joint"]

print("full-band cascade, silicon, E_g = 1.160 eV (primary: static Cappellini screening, JR phonons, threshold R_x 0.75)")
print("eps_eh = %.3f eV, envelope [%.3f, %.3f] eV; measured 3.749 eV: primary %+.1f %%" %
      (P["eps"], E["eps"][0], E["eps"][1], 100 * (P["eps"] / 3.749 - 1)))
print("   model-class systematic >= +-0.4 eV (Nielsen-Fischetti 3.10 -> 3.50 eV)")
print("F_eh = %.3f, envelope [%.3f, %.3f]; measured 0.119 +- 0.002" % (P["F"], E["F"][0], E["F"][1]))
print("equivalent A_AB of the energy-only cascade at the full-band eps: %.1f eV^3 [%.1f, %.1f]" %
      (D["matched"]["v2primary"]["A"], D["matched"]["c_lo"]["A"], D["matched"]["c_hi"]["A"]))
print("P(N >= 2, 5 eV), dark-matter seed at q0: %.3f, envelope with k-grid term [%.3f, %.3f]" %
      (P["Pge2_5.0"], E["Pge2_5.0_withgrid"][0], E["Pge2_5.0_withgrid"][1]))
print("step-model overcount of the two-pair bin at 5 eV: %.1f, envelope with grid [%.1f, %.1f]; upper end from the corner"
      " (static Resta, holes x 3.0, threshold R_x 0.5)" % (P["overcount_5"], E["overcount_5_withgrid"][0],
                                                       E["overcount_5_withgrid"][1]))
print("total heat at 100 eV: %.1f %% [%.1f, %.1f]; pairs %.1f %%" % (100 * P["heat_100"], 100 * E["heat_100"][0],
                                                                    100 * E["heat_100"][1], 100 * P["pairs_100"]))
print("mean pair number at 10 eV: %.2f [%.2f, %.2f]" % (P["mean_10"], E["mean_10"][0], E["mean_10"][1]))

# where eps is decided: rate multipliers below 4.5 eV and above 5 eV; phonon and screening variants
V = D["variants"]
print("W_ii x 3 below 4.5 eV: eps = %.2f eV; W_ii x 2 above 5 eV: eps = %.2f eV" % (V["v2wlo3"]["eps"], V["v2whi2"]["eps"]))
print("phonons electrons x 0.52: eps %.2f; holes x 3.0: %.2f; both: %.2f; dynamic band RPA screening: %.2f eV" %
      (V["v2e052"]["eps"], V["v2h30"]["eps"], V["v2fp"]["eps"], V["v2rpaw"]["eps"]))
# Nielsen-Fischetti-like choices (first-principles phonons for both carriers, no exchange): 4.11 eV, a run quoted by
# the verification of the full-band return (not in the data file); NF obtain 3.10 (TDDFT) and 3.50 eV (GW/BSE)
print("NF-like choices (first-principles phonons, no exchange): 4.11 eV against NF's 3.50 eV (GW/BSE): gap %.1f eV" %
      (4.11 - 3.50))

# exchange factor above 3 eV, pooled in 1-eV blocks [E, E + 1) (below 3 eV the sampled ratio is noise; 0.75 is used there)
rx = D["rx"]
Eb = np.array(rx["Ebins"])
for a, lab in (("Rx_e", "electrons"), ("Rx_h", "holes")):
    r = np.array(rx[a])
    vals = [r[(Eb >= e) & (Eb < e + 1)].mean() for e in range(3, 21)]
    print("R_x %s, 1-eV blocks from 3 to 21 eV: " % lab + " ".join("%.2f" % v for v in vals) +
          "; range %.2f-%.2f" % (min(vals), max(vals)))

# phonon competition near threshold (paired v1 runs: no phonon emission vs primary)
n1, p1 = np.array(D["v1_nophonon"]["omegas"]), np.array(D["v1_nophonon"]["Pge2"])
o1, q1 = np.array(D["v1_primary"]["omegas"]), np.array(D["v1_primary"]["Pge2"])
for w in (3.0, 4.0, 4.5):
    print("P(N >= 2, %.1f eV): without phonon emission %.3f, with %.3f" % (w, p1[np.argmin(abs(n1 - w))], q1[np.argmin(abs(o1 - w))]))
om2 = np.array(D["omegas_v2"]); P2 = np.array(D["primary_P_heavy"])
i4 = np.argmin(abs(om2 - 4.0))
print("v2 primary, P(N >= 2, 4.0 eV) with phonon emission: %.3f" % (1 - P2[i4, :2].sum()))
G = D["photon_seed_grid"]
print("photon seed between k grids (energy-only cascade, max TV): 20^3 vs 12^3 %.2f, 20^3 vs 28^3 %.2f; DM seed 20^3 vs 12^3 %.3f"
      % (G["photon20_vs_photon12"], G["photon20_vs_photon28"], G["dm20_vs_dm12"]))
mo = np.array(D["v1_memory_tv"]["omegas"]); sel = (mo >= 2) & (mo <= 20)
print("first-generation momentum memory (full band vs shell-randomized, 2-20 eV): max TV %.3f; 123 K vs mK: %.3f" %
      (np.array(D["v1_memory_tv"]["eo"])[sel].max(), np.array(D["v1_memory_tv"]["T123"])[sel].max()))

# energy-only cascade recalibrated to the full-band eps, and the limits, against the full-band distribution (max TV)
print("matched distances to the full-band cascade (energy-only cascade recalibrated to the full-band eps), max TV, 4.4-21 eV:")
for k in ("c_lo", "v2primary", "c_hi"):
    d = D["matched"][k]["d"]
    print("  %-9s eps %.2f: energy-only, DM seed %.3f (at %.2f eV); computed split %.3f (%.2f eV); R-K alpha=1 %.3f; alpha=inf %.3f;"
          " step %.3f" % (k, D["matched"][k]["eps"], d["bookDM"]["max"], d["bookDM"]["at"], d["split"]["max"],
                          d["split"]["at"], d["rk1"]["max"], d["rkinf"]["max"], d["step"]["max"]))
