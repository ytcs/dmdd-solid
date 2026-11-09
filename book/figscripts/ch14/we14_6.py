"""Numbers of Sect. 14.6 and Worked example 14.6 (we:14-crossover): the coherent regime of a 1 neV axion-like field.
Log we14_6.log.  Run: python we14_6.py (seconds).

Constants: CODATA hbar, h, hbar c, k_B, nuclear magneton mu_N/h = 7.6226 MHz/T (2101.01241 Supp. after Eq. (S11)).
Halo (Sect. 1.2): v0 = 238 km/s, v_esc = 544, v_E = 250.5 km/s, rho_chi = 0.3 GeV/cm^3; line model coh14.py.
t_coh = 1/(m_phi v0^2) (book definition, eq:14.6-tcoh).
207Pb in PMN-PT (Aybas et al. 2101.01241, Supplement): spin 1/2, mu = 0.5926 mu_N (Eq. (S11) and text), gamma/2pi =
  9.03 MHz/T (Eq. (S11)), n = 3.4e27 m^-3 (Eq. (S12)), T2 = 16.7 ms (Eq. (S25) text), B0 = 4.4 T, T = 4.2 K,
  mu0 M0 = 2.9 nT (Eq. (S13)), inhomogeneous width Gamma/2pi = 78 kHz and u = 3.8e-4 (Eqs. (S24)-(S25)).
Sensitivity model: coh14.n_eff, s_up_stoch, s_up_det (Limit Check 14.6c).
"""
import os
import numpy as np
import coh14 as C

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "we14_6.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


v0 = C.V0 * C.KMS
kB = 8.617333262e-5          # eV/K
rho = 0.3e9 * (1.973269804e-5) ** 3   # 0.3 GeV/cm^3 in eV^4 (1 cm = 1/1.9733e-5 eV^-1)
out(f"rho_chi = {rho:.4e} eV^4")

# coherence time and length
for m in (1e-12, 1e-9, 1e-6, 10e-6, 1.0):
    tc = C.HBAR / (m * v0 ** 2)
    lc = C.HBARC / (m * v0)
    out(f"m_phi = {m:.0e} eV: t_coh = 1/(m v0^2) = {tc:.4g} s; 2 pi t_coh = {2*np.pi*tc:.4g} s; 1/(m v0) = {lc:.4g} m")

m = 1e-9
f = m / C.H_PLANCK
tc = C.HBAR / (m * v0 ** 2)
out(f"\n1 neV: frequency m/h = {f/1e3:.2f} kHz; period {1/f*1e6:.3f} us; t_coh = {tc:.4f} s")
out(f"  m v0^2/h = {f*v0**2:.4f} Hz; line peak at {C.X_PEAK:.3f} m v0^2 above m ({C.X_PEAK*f*v0**2:.4f} Hz); "
    f"mean {C.X_MEAN:.3f} m v0^2 ({C.X_MEAN*f*v0**2:.4f} Hz)")
out(f"  equivalent width Delta omega_eq = {C.DW_EQ:.3f}/t_coh, i.e. {C.DW_EQ/(2*np.pi*tc):.4f} Hz; "
    f"fractional {C.DW_EQ*v0**2:.3e}; line ends at (v_max^2/2) m = {((C.VESC+C.VE)*C.KMS)**2/2:.3e} m above m")
# occupation of one coherence volume (1/(m v0))^3
occ = (rho / m) / (m * v0) ** 3
out(f"  quanta per volume (1/(m v0))^3: {occ:.2e}")
# field autocorrelation in the laboratory frame
tt = np.linspace(0, 20, 4001)
Cf = np.array([abs(np.trapezoid(C.Fg * np.exp(-1j * C.xg * t), C.xg)) for t in tt])
t_half = tt[np.argmax(Cf < 0.5)]
t_e = tt[np.argmax(Cf < np.exp(-1))]
out(f"  |<Phi(t)Phi*(0)>| falls to 1/2 at t = {t_half:.3f} t_coh and to 1/e at {t_e:.3f} t_coh (lab frame, truncated halo)")
# galactic-frame Maxwellian without cut: |C| = (1 + (t/2)^2)^(-3/4) (characteristic function of v^2/2v0^2 with
# <v_i^2> = v0^2/2): check
tg = 2.0 * np.sqrt(2 ** (4 / 3) - 1)
out(f"  halo rest frame, no cut: |C(t)| = [1 + (t/2t_coh)^2]^(-3/4): 1/2 at t = {tg:.3f} t_coh")

# 207Pb in PMN-PT at the Larmor field for 1 neV
muN_h = 7.6226e6       # Hz/T
gam = 0.5926 * muN_h / 0.5   # Hz/T
B = f / gam
out(f"\n207Pb: gamma/2pi = {gam/1e6:.3f} MHz/T; Larmor field for 1 neV: {B*1e3:.2f} mT")
T2 = 16.7e-3
out(f"  T2 = {T2*1e3:.1f} ms: T2/t_coh = {T2/tc:.4f}; 1/T2 = {1/T2:.1f} s^-1 vs m v0^2 = {1/tc:.3f} s^-1 "
    f"(spin line {tc/T2:.0f} times wider than the field line)")
# thermal polarization at 4.4 T, 4.2 K and M0
wl = C.H_PLANCK * gam * 4.4      # eV
p = np.tanh(wl / (2 * kB * 4.2))
n = 3.4e27
mu = 0.5926 * 5.0507837461e-27   # J/T
M0 = n * mu * p
out(f"  4.4 T, 4.2 K: omega_Lar = {wl:.4e} eV ({gam*4.4/1e6:.2f} MHz); p_pol = tanh(omega/2T) = {p:.3e}; "
    f"M0 = n mu p = {M0:.3e} A/m; mu0 M0 = {4e-7*np.pi*M0*1e9:.2f} nT (source: 2.9 nT)")
G = 2 * np.pi * 78e3
out(f"  u estimate pi/(Gamma T2) = {np.pi/(G*T2):.3e} (source Eq. (S25): 3.8e-4)")

# scaling crossover and sensitivity gains
out("\nSensitivity model (Limit Check 14.6c): y = (A_95^2 t_coh/S_n)^(1/2)")
def y_stoch(T):
    return np.sqrt(C.s_up_stoch(C.n_eff(T)) / T)
def y_det(T):
    return np.sqrt(C.s_up_det(C.n_eff(T)) / T)
for t_s in (0.1, 1.0, 10.0, 60.0, 600.0, 3600.0, 86400.0):
    T = t_s / tc
    out(f"  t_int = {t_s:8.1f} s = {T:10.2f} t_coh: N_eff = {C.n_eff(T):9.2f}; y_Rayleigh = {y_stoch(T):.4e}; "
        f"y_fixed = {y_det(T):.4e}")
T1h, T1d = 3600 / tc, 86400 / tc
g_s = y_stoch(T1h) / y_stoch(T1d)
out(f"  1 h -> 1 day: coupling limit improves by {g_s:.3f} (Rayleigh); (24)^(1/4) = {24**0.25:.3f}; (24)^(1/2) = {24**0.5:.3f}")
T01, T1 = 0.1 / tc, 1.0 / tc
out(f"  0.1 s -> 1 s: improves by {y_stoch(T01)/y_stoch(T1):.3f} (Rayleigh), {y_det(T01)/y_det(T1):.3f} (fixed); sqrt(10) = {10**0.5:.3f}")
out(f"  crossover (local slope -3/8, limit14_6c.log): 23.3 t_coh = {23.25*tc:.1f} s (Rayleigh), 5.37 t_coh = {5.37*tc:.1f} s (fixed)")
out(f"  t_int = 0.1 s: Rayleigh/fixed coupling ratio = {y_stoch(T01)/y_det(T01):.3f}")
# number of coherence cells in a day
out(f"  coherence times in one day: {86400/tc:.0f}")

# coherence times in one hour for YIG at 10 ueV (we:14-yig: 35 events per hour in a 1 cm sphere)
tc10 = C.HBAR / (10e-6 * v0 ** 2)
out(f"\nYIG at 10 ueV: t_coh = {tc10*1e3:.4f} ms; coherence times per hour = {3600/tc10:.3e}")
# 207Pb Larmor frequency at 1 neV in rad/s vs T2
out(f"1 neV in rad/s: {m/C.HBAR:.4e}; 2 pi x 241.8 kHz = {2*np.pi*f:.4e}")
