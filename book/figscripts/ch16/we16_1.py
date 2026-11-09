"""Worked example 16.1 (we:16-factor): the factor eps_bg^2 at eps_bg = 40, for the ideal isotropic benchmark of
Hochberg et al., arXiv:1708.08929 (Fig. 4 caption, Sect. 3.3): v_F = 4e-4, kappa = eps_bg = 40, g = 2, Lambda = 0.2 keV,
gapless (green curve) or Delta = 2.5 meV (purple curve); absorption with rho_T = 10 g/cm^3 (their Fig. 6 caption);
scattering with n_e V_uc = (5e24/kg)(60 A^3) = 1/rho_T, i.e. rho_T = 3.33 g/cm^3 (their Eq. (3.14) and text after it).
Modelling choice: Lambda = 0.2 keV is read as the hard cutoff of eq:7.3-eps (Lt = v_F Lambda = 80 meV); the
subtraction-scheme reading (their Eq. (2.6) taken literally) adds 5/3 to the bracket, which is quoted beside it.
Book halo and rho_chi = 0.3 GeV/cm^3 (rate10_2.py).  Every number printed here is quoted in Sect. 16.1.
Run: python we16_1.py > we16_1.log
"""
import os
import numpy as np
import dirac16 as d

HERE = os.path.dirname(os.path.abspath(__file__))
b = d.BENCH
vD, g, ebg, Lt = b["vD"], b["g"], b["ebg"], b["Lt"]
at = d.ALPHA / (ebg * vD)
print("benchmark: v_D = %.1e, eps_bg = %.0f, g = %d, Lambda_D = %.0f eV, v_D Lambda_D = %.3f eV" % (vD, ebg, g, Lt / vD, Lt))
print("alpha~ = alpha/(eps_bg v_D) = %.3f ; g alpha~ = %.3f" % (at, g * at))
print("Im eps_D deep in the continuum = g alpha/(6 v_D) = %.3f (independent of eps_bg)" % (g * d.ALPHA / (6 * vD)))

# one point: q -> 0, omega = 10 meV, gapless cone (s = omega^2)

w = 0.010
B = d.B_exact(w**2, 0.0, Lt)
eD = g * d.ALPHA / (6 * np.pi * vD) * B
print("\ngapless, sqrt(s) = 10 meV: bracket B = %.4f + %.4fi" % (B.real, B.imag))
print("eps_D = %.3f + %.3fi ; Re eps_D/eps_bg = %.4f" % (eD.real, eD.imag, eD.real / ebg))
eps = ebg + eD
L = eD.imag / abs(eps) ** 2
Llead = eD.imag / ebg**2
Lsrc = eD.imag / abs(1 + eD / ebg) ** 2
print("eps = %.2f + %.2fi, |eps|^2 = %.1f" % (eps.real, eps.imag, abs(eps) ** 2))
print("L (total eps) = %.4e ; leading form Im eps_D/eps_bg^2 = %.4e ; ratio L/L_lead = %.4f" % (L, Llead, L / Llead))
print("published scattering vertex: Im eps_D/|eps/eps_bg|^2 = %.4f ; ratio to L = %.1f (eps_bg^2 = %.0f)" % (Lsrc, Lsrc / L, ebg**2))
Bsub = B + 5.0 / 3.0
eDs = g * d.ALPHA / (6 * np.pi * vD) * Bsub
print("subtraction-scheme reading of Lambda: Re eps_D/eps_bg = %.4f ; L/L_lead = %.4f" % (eDs.real / ebg, ebg**2 / abs(ebg + eDs) ** 2))
Asrc = (eD.imag / ebg) / abs(1 + eD / ebg) ** 2
print("published absorption: Im(eps/eps_bg)/|eps/eps_bg|^2 = %.4f ; ratio to L = %.2f (eps_bg = %.0f)" % (Asrc, Asrc / L, ebg))

# absorption reach at m_phi = 10 meV, rho_T = 10 g/cm^3 (isotropic: L is the same for every polarization)
rho10 = 10 * d.GCM3
z_book = d.zeta_lim(L, rho10)
z_src = d.zeta_lim(Asrc, rho10)
rate = d.RHO_CHI / rho10 * L * d.KGYR
print("\nabsorption, m_phi = 10 meV, rho_T = 10 g/cm^3: R = %.3e zeta^2 per kg yr" % rate)
print("zeta reach (3 events, 1 kg yr): total eps %.3e ; published rule %.3e ; ratio %.3f (sqrt(40) = %.3f)" % (z_book, z_src, z_book / z_src, np.sqrt(ebg)))

# scattering reach at 100 keV, light mediator, rho_T = 1/(n_e V_uc)
rhoT = 1.0 / (5e24 * 60e-24) * 1e3       # g/cm^3: (5e24 /kg * 60e-24 cm^3)^-1 kg/cm^3 -> g/cm^3
print("\nscattering: rho_T = 1/(n_e V_uc) = %.3f g/cm^3" % rhoT)
for D, name in [(0.0, "gapless"), (b["D"], "gapped 2.5 meV")]:
    Bt = d.Btab(D, Lt) if D > 0 else None

    def Bfun(s, D=D):
        if D > 0:
            return Bt(s)
        s = np.asarray(s, float)
        ok = (s > 0) & (s <= 4 * Lt**2)
        return np.where(ok, np.log(4 * Lt**2 / np.where(ok, s, 1.0)) + 1j * np.pi, 0.0)

    for m in (1e4, 1e5):
        res = {}
        for rule in ("book", "src", "lead"):
            Lf = lambda q, w, rule=rule: d.L_iso(q, w, vD, g, ebg, Bfun, rule)  # noqa: E731
            r = d.scatter_rate(m, Lf, max(2 * D, 1e-4), 2 * Lt, 2 * Lt / vD, rhoT * d.GCM3)
            res[rule] = d.sigma_lim(r)
        print("%s, m = %3.0f keV: sigma_lim total eps %.3e cm^2 ; published rule %.3e ; ratio %.1f ; leading form %.3e (total/leading %.3f)"
              % (name, m / 1e3, res["book"], res["src"], res["book"] / res["src"], res["lead"], res["lead"] / res["book"]))
        if D > 0 and m == 1e5:
            xg = np.loadtxt(os.path.join(HERE, "data", "pub_h_gapped.csv"), delimiter=",")
            xg = xg[np.argsort(xg[:, 0])]
            pv = np.exp(np.interp(np.log(100.0), np.log(xg[:, 0]), np.log(xg[:, 1])))
            print("  published gapped curve read at 100 keV: %.2e cm^2 ; over the recomputed published form %.2e: %.2f"
                  % (pv, res["src"], pv / res["src"]))

# the published curves, digitized from the vector figure of 1708.08929 (Fig. 4)
for f, fac, lab in [("pub_h_gapped.csv", ebg**2, "ideal gapped"), ("pub_h_gapless.csv", ebg**2, "ideal gapless"),
                    ("pub_h_Zr_th.csv", d.EBG_1708**2, "ZrTe5 th.")]:
    x = np.loadtxt(os.path.join(HERE, "data", f), delimiter=",")
    i = np.argmin(x[:, 1])
    print("published %-14s minimum %.2e cm^2 at %.0f keV -> corrected x%.1f = %.2e cm^2" % (lab, x[i, 1], x[i, 0], fac, x[i, 1] * fac))
print("\nZrTe5 of 1708.08929: harmonic mean of (187.5, 9.8, 90.9) = %.3f ; square %.1f ; sqrt %.3f" % (d.EBG_1708, d.EBG_1708**2, np.sqrt(d.EBG_1708)))
print("lower bound on the ratio if alpha~ < 1 and v_D < v_max: (alpha/v_max)^2 = %.3f (alpha/v_max = %.3f)" % ((d.ALPHA / d.VMAX) ** 2, d.ALPHA / d.VMAX))
print("eps_bg at which alpha~ = 1 for v_D = 4e-4: alpha/v_D = %.2f ; eps_bg^2 = 1.1 at eps_bg = %.4f" % (d.ALPHA / vD, np.sqrt(1.1)))
print("Yb3PbO (cubic, kappa = 42.8 in 1910.02091 Table 2): eps_bg^2 = %.1f, eps_bg^(1/2) = %.3f" % (42.8**2, np.sqrt(42.8)))
print("ZrTe5 isotropic (Sect. 7.3 WE): published |eps_r|^2 = (1 + 0.093)^2 = %.3f against |eps|^2 = 55.2^2 = %.0f; ratio %.0f = 50.5^2"
      % (1.093**2, 55.2**2, 55.2**2 / 1.093**2))
