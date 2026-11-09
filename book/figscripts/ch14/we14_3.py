"""Numbers of Sect. 14.3 (absorption into magnons) and of Worked example 14.3 (YIG Kittel-mode rate for a 10 ueV
axion-like particle). Every number printed in s14-3.tex that is not in limit14_3a.log or fig14_3.log is printed here.
Log: we14_3.log.  Run: python we14_3.py (instant).

Inputs and sources
  constants: mu_B = 5.7883818060e-5 eV/T, hbar c = 1.973269804e-7 eV m, u = 931.49410242 MeV, m_e = 0.51099895 MeV (CODATA 2018).
  halo: rho_chi = 0.3 GeV/cm^3, v0 = 238 km/s, v_E^ref = 250.5 km/s (book values, Sects. 1.2, NOTATION).
  t_coh = 1/(m v0^2) (book definition, Sect. 8.2 / Ch11 ruling).
  YIG: a = 12.375 A (COD 2101364, Nakatsuka et al. 1995, as in the book's data addenda), bcc primitive cell a^3/2 holding
       4 formula units Y3Fe5O12 (M = 737.94 g/mol) and 20 Fe3+ (S = 5/2): 12 on tetrahedral sites against 8 on octahedral
       sites (Mitridate et al. arXiv:2005.10256 Sect. III), so the net spin per primitive cell is (12 - 8) x 5/2 = 10.
       Cross-check: magnetization 38 emu/g at ~100 mK (Chigusa et al. arXiv:2001.10666 after Eq. (39)).
       Kittel width gamma/omega = 1e-5 (the YIG value taken in 2005.10256 Sect. V B).
       Exchange "mass" of the Kittel mode: omega_k = omega_L + k^2/2M with M ~ 3.5 MeV (2001.10666 Eqs. (19)-(20) text).
  MnF2: H_E = 47.05 T, H_A = 0.82 T with gamma = gamma_e (Vaidya et al. arXiv:2005.01203, text after Eq. (3));
        measured zone-center gap 1.1 meV at 4 K, S = 5/2 (Bayrakci et al. arXiv:1302.4867, p. 1);
        rutile cell with 2 formula units MnF2 (54.938 + 2 x 18.998 = 92.934 g/mol), one antiparallel pair.
  Rare-earth ground multiplets from Hund's rules (4f^n, trivalent).
"""
import os
import numpy as np
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "we14_3.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


muB = 5.7883818060e-5            # eV/T
hbarc = 1.973269804e-7           # eV m
hbar_eVs = 6.582119569e-16       # eV s
u = 931.49410242e6               # eV
me = 0.51099895e6                # eV
c_kms = 299792.458
kg_eV = 5.609588603e35           # eV per kg
s_inv_eV = 1.0 / hbar_eVs        # 1 eV = this many s^-1
yr = 3.15576e7
GeVcm3 = 1e9 * (hbarc * 100) ** 3   # 1 GeV/cm^3 in eV^4
rho = 0.3 * GeVcm3
v0 = 238 / c_kms
vE = 250.5 / c_kms
NAT_RATE = s_inv_eV * kg_eV      # natural rate per unit mass (dimensionless) -> s^-1 kg^-1

out("=== Lande factors of trivalent rare-earth ions (Hund's rules) ===")
out("ion  S  L  J  g_J  lambda_S=g_J-1  lambda_S/(g_J/2)")


def hund(n):
    # 4f^n, trivalent: S, L, J by Hund's rules
    ml = [3, 2, 1, 0, -1, -2, -3]
    up = min(n, 7)
    dn = n - up
    S = Fr(up - dn, 2)
    L = abs(sum(ml[:up]) + sum(ml[:dn]))
    J = abs(L - S) if n < 7 else L + S
    return S, Fr(L), J


def gJ(S, L, J):
    return 1 + (J * (J + 1) + S * (S + 1) - L * (L + 1)) / (2 * J * (J + 1))


for name, n in [("Ce3+", 1), ("Sm3+", 5), ("Gd3+", 7), ("Dy3+", 9), ("Ho3+", 10), ("Er3+", 11)]:
    S, L, J = hund(n)
    g = gJ(S, L, J)
    lam = g - 1
    out(f"{name}  {S}  {L}  {J}  {g} ({float(g):.4f})  {lam} ({float(lam):.4f})  {float(lam/(g/2)):.3f}")
out("check projection identity: lambda_S = <S.J>/J(J+1) = [J(J+1)+S(S+1)-L(L+1)]/[2J(J+1)] = g_J - 1 (same expression)")

out("\n=== illustrative quenched ion with g = 2.2: lambda_S = g - 1 would give 1.2, rate factor (1.2)^2 =", f"{1.2**2:.2f}")

out("\n=== length and time scales for m_phi = 10 ueV ===")
m = 10e-6
p = m * vE
out(f"Compton wavelength 2 pi/m = {2*np.pi*hbarc/m:.3f} m; de Broglie 1/(m v_E) = {hbarc/(m*vE):.1f} m;"
    f" 2 pi/(m v_E) = {2*np.pi*hbarc/(m*vE):.0f} m")
aYIG = 12.375e-10
out(f"p_phi a (YIG, a = 12.375 A) = {p*aYIG/hbarc:.2e}")
tcoh = hbar_eVs / (m * v0**2)
out(f"t_coh = 1/(m v0^2) = {tcoh:.3e} s; relative ALP line width ~ v0^2 = {v0**2:.2e}")
Mex = 3.5e6
out(f"exchange shift k^2/2M with k = m v_E, M = 3.5 MeV: {p**2/(2*Mex):.2e} eV; relative to omega: {p**2/(2*Mex)/m:.1e}")
out(f"Larmor frequency per tesla (g = 2): 2 mu_B = {2*muB*1e6:.2f} ueV/T = {2*muB/(2*np.pi*hbar_eVs)/1e9:.2f} GHz/T")

out("\n=== YIG ===")
Omega = aYIG**3 / 2              # m^3, bcc primitive cell
s_net = (12 - 8) * 2.5
mcell_u = 4 * 737.94
out(f"primitive cell volume a^3/2 = {Omega*1e30:.1f} A^3; net spin per cell s_net = {s_net}; cell mass = {mcell_u:.1f} u")
mom = 2 * s_net * 9.2740100783e-24      # A m^2 (g = 2)
Ms = mom / Omega
mu0Ms = 4e-7 * np.pi * Ms
out(f"M_s = {Ms:.4e} A/m; mu0 M_s = {mu0Ms:.4f} T; 4 pi M_s = {mu0Ms*1e4:.0f} G")
emu_per_g = (2 * s_net / 4) * 9.2740100783e-21 * 6.02214076e23 / 737.94
out(f"magnetization per mass = {emu_per_g:.1f} emu/g (5 mu_B per formula unit) [2001.10666 quotes 38 emu/g]")
omegaM = 2 * muB * mu0Ms
out(f"omega_M = 2 mu_B mu0 M_s = {omegaM*1e6:.2f} ueV = {omegaM/(2*np.pi*hbar_eVs)/1e9:.2f} GHz")
Bsat = mu0Ms / 3
out(f"sphere saturates for B0 > mu0 M_s/3 = {Bsat*1e3:.1f} mT, i.e. Kittel frequency > {2*muB*Bsat*1e6:.2f} ueV"
    f" = {2*muB*Bsat/(2*np.pi*hbar_eVs)/1e9:.2f} GHz")

out("\n--- WE 14.3: YIG sphere, m_phi = 10 ueV ---")
B0 = m / (2 * muB)
out(f"B0 = m/(2 mu_B) = {B0*1e3:.1f} mT; internal field B0 - mu0Ms/3 = {(B0-Bsat)*1e3:.1f} mT")
T = 0.010
kB = 8.617333262e-5
out(f"beta omega at 10 mK = {m/(kB*T):.1f}; exp(-beta omega) = {np.exp(-m/(kB*T)):.1e}")
gam = 1e-5 * m
out(f"gamma = 1e-5 omega = {gam:.1e} eV = {gam/(2*np.pi*hbar_eVs)/1e3:.0f} kHz (FWHM in frequency); 1/gamma = {hbar_eVs/gam*1e6:.1f} us")
vperp2_perp = v0**2 + vE**2          # z perpendicular to v_E
vperp2_par = v0**2                   # z parallel to v_E
vperp2_avg = v0**2 + 2 * vE**2 / 3
out(f"<v_perp^2>: z perp v_E {vperp2_perp:.4e}; z par v_E {vperp2_par:.4e}; ratio {vperp2_par/vperp2_perp:.3f}; avg {vperp2_avg:.4e}")
gaee = 1e-13
mcell = mcell_u * u
R_nat = rho * gaee**2 * vperp2_perp * s_net / (me**2 * mcell * gam)
R = R_nat * NAT_RATE
out(f"peak rate R = rho g^2 <v_perp^2> lambda^2 s_net/(m_e^2 m_cell gamma) = {R:.2f} /s/kg = {R*yr:.2e} /kg/yr  (g_aee = 1e-13)")
msph = 4 / 3 * np.pi * 0.5**3 * 5.173 * 1e-3   # kg, 1 cm diameter
out(f"1 cm diameter sphere: mass {msph*1e3:.2f} g, peak rate {R*msph:.2e} /s = {R*msph*3600:.0f} per hour")
# golden rule vs 2001.10666: their coherent rate per kg  s rho v_perp^2 tau g^2/(4 m_e^2 m_cell) (Eq. (38) without the 1/2 of the cavity)
tau_eq = 4 / gam
out(f"equality with 2001.10666 Eq. (38) (cavity factor 1/2 removed) at tau = 4/gamma = {hbar_eVs*tau_eq*1e6:.1f} us")
# film alternative
w0 = (-omegaM + np.sqrt(omegaM**2 + 4 * m**2)) / 2
out(f"thin film, in-plane field: omega_0 = {w0*1e6:.2f} ueV, B0 = {w0/(2*muB)*1e3:.1f} mT;"
    f" weight factors sqrt(w_y/w_x) = {np.sqrt((w0+omegaM)/w0):.2f}, sqrt(w_x/w_y) = {np.sqrt(w0/(w0+omegaM)):.3f},"
    f" transverse average {(w0 + w0 + omegaM)/(2*m):.2f}")

out("\n=== MnF2 ===")
HE, HA = 47.05, 0.82
wE = 2 * muB * HE
wA = 2 * muB * HA
wAF = np.sqrt(wA * (2 * wE + wA))
r = wAF / (2 * wE + wA)
out(f"omega_E = {wE*1e3:.3f} meV, omega_A = {wA*1e3:.4f} meV, omega_A/omega_E = {wA/wE:.4f}")
out(f"omega_AFMR = sqrt(omega_A(2omega_E+omega_A)) = {wAF*1e3:.3f} meV = {wAF/(2*np.pi*hbar_eVs)/1e9:.0f} GHz"
    f" [measured gap 1.1 meV at 4 K, 1302.4867]")
out(f"weight factor omega_AFMR/(2 omega_E + omega_A) = {r:.4f}; small-ratio form sqrt(omega_A/2omega_E) = {np.sqrt(wA/(2*wE)):.4f}")
S = 2.5
out(f"weight per pair |S| r = {S*r:.3f} (ferromagnetic pair: {S})")
Bsf_line = wAF / (2 * muB)
Bsf = np.sqrt(HA * (2 * HE - HA))
out(f"lower line reaches zero at B0 = omega_AFMR/(2 mu_B) = {Bsf_line:.2f} T; spin-flop field sqrt(H_A(2H_E-H_A)) = {Bsf:.2f} T")
m_pair = 2 * 92.934
W_Mn = 2 * S * r / m_pair   # both degenerate lines at B0 = 0: weight 2|S|r per pair cell (S_xx = 2 pi W_pair/Omega_p)
W_Y = s_net / mcell_u
out(f"weight per mass: MnF2 {W_Mn:.3e} /u, YIG {W_Y:.3e} /u, ratio {W_Mn/W_Y:.3f}")
ratio_Q = W_Mn / W_Y * (m / wAF)
out(f"peak-rate ratio MnF2 (at omega_AFMR) / YIG (at 10 ueV), equal gamma/omega: {ratio_Q:.1e}")
R_Mn = rho * gaee**2 * vperp2_perp * 2 * S * r / (me**2 * m_pair * u * 1e-5 * wAF) * NAT_RATE
out(f"MnF2 peak rate at gamma/omega = 1e-5, g_aee = 1e-13, z perp v_E: {R_Mn:.2e} /s/kg = {R_Mn*yr:.2e} /kg/yr")
LOG.close()

LOG = open(os.path.join(HERE, "we14_3.log"), "a")
out("\n=== MnF2 shape: sublattice saturation magnetization ===")
# Vaidya et al. 2005.01203 (text after Eq. (3)) quote M_s = 47.7 kA/m, which is the sublattice magnetization divided by
# 4 pi (Gaussian 4 pi M convention): 5 mu_B per Mn on one sublattice of the rutile cell (a = 4.873 A, c = 3.310 A,
# a^2 c = 78.6 A^3, one Mn per sublattice) gives 590 kA/m = 4 pi x 47.0 kA/m.  The SI value enters omega_M = 2 mu_B mu0 M_s
# (the convention of omega_M for YIG above, 28.5 ueV).
V_rut = 4.873e-10**2 * 3.310e-10
Msub = 5 * 9.2740100783e-24 / V_rut
out(f"5 mu_B / a^2 c: M_sub = {Msub/1e3:.0f} kA/m = 4 pi x {Msub/4/np.pi/1e3:.1f} kA/m; 4 pi x 47.7 kA/m = {4*np.pi*47.7:.0f} kA/m")
for lab, M in (("5 mu_B per Mn", Msub), ("4 pi x 47.7 kA/m", 4 * np.pi * 47.7e3), ("47.7 kA/m read as SI", 47.7e3)):
    mu0M = 4e-7 * np.pi * M
    wM_Mn = 2 * muB * mu0M
    out(f"  {lab:22s}: mu0 M_sub = {mu0M:.3f} T; omega_M = {wM_Mn*1e6:.1f} ueV; omega_M/omega_E = {wM_Mn/wE:.1e}")

out("\n=== MnF2: measured gap and spin flop as the reference ===")
# measured: zone-center gap 1.1 meV at 4 K (Bayrakci et al. 1302.4867 p. 1); spin flop mu0 H_SF ~ 9.4 T (Vaidya et al.
# 2005.01203 Fig. 1 caption).  For omega_A << omega_E, omega_AFMR ~ g mu_B B_sf.
wgap = 1.1e-3
out(f"omega_AFMR/(2 mu_B) for the measured 1.1 meV: {wgap/(2*muB):.2f} T (measured spin flop ~9.4 T)")
out(f"fitted fields: omega_AFMR = {wAF*1e3:.3f} meV and B_sf = {Bsf:.2f} T, {100*(1-wAF/wgap):.1f} % and {100*(1-Bsf/9.4):.1f} % below the measured pair")
wA2 = np.sqrt(wE**2 + wgap**2) - wE
r2 = wgap / (2 * wE + wA2)
out(f"keeping omega_E = {wE*1e3:.3f} meV, omega_A refit to the 1.1 meV gap: omega_A = {wA2*1e3:.4f} meV;"
    f" weight factor {r2:.4f} (sqrt form {np.sqrt(wA2/(2*wE)):.4f}); per pair |S| r = {S*r2:.3f} ({100*(r2/r-1):.0f} % above the fitted-field value);"
    f" B_sf = sqrt(B_A(2B_E - B_A)) = {np.sqrt((wA2/(2*muB))*(2*HE - wA2/(2*muB))):.2f} T")
W_Mn2 = 2 * S * r2 / m_pair
R_Mn2 = rho * gaee**2 * vperp2_perp * 2 * S * r2 / (me**2 * m_pair * u * 1e-5 * wgap) * NAT_RATE
out(f"weight per mass relative to YIG {W_Mn2/W_Y:.3f}; peak rate at 1.1 meV, gamma/omega = 1e-5: {R_Mn2:.2e} /s/kg"
    f" (fitted fields: {R_Mn:.2e}); peak-rate ratio to YIG {W_Mn2/W_Y*(m/wgap):.1e}")
out(f"peak rate prop. to |S| omega_A/omega_AFMR^2: fitted {S*wA/wAF**2:.4f} /meV, refit {S*wA2/wgap**2:.4f} /meV")

out("\n=== Exchange mass of the YIG uniform mode from the book's stiffness (WE 14.2) ===")
Dsw = 5.985e-3 * 1e-18          # eV m^2
Mbook = hbarc**2 / (2 * Dsw)
out(f"M = 1/(2 D_sw) = {Mbook/1e6:.2f} MeV (Chigusa et al. quote ~3.5 MeV); shift k^2/2M at k = m v_E: {p**2/(2*Mbook)/m:.1e} of omega")
LOG.close()
