"""Worked example 21.1 (we:21-debris): the silicon electron-recoil rate at m_chi = 10 MeV, heavy mediator,
sigma_e = 1e-37 cm^2, for a halo of the standard halo model plus a debris flow, from the rate kernel k(v) alone.
Also the floor numbers of Sect. 21.1 that use the debris flow. Prints every number; output we21_1.log.

Halo model: f = (1 - eps) f_SHM + eps f_DF (Kuhlen, Lisanti, Spergel [KLS] Eq. (10)) at the same total density
rho_chi = 0.3 GeV/cm^3; eps = 0.22 and v_flow = 340 km/s ([KLS], Via Lactea II, text below Fig. 6); f_DF an isotropic
shell of galactic speed v_flow, laboratory speed distribution [KLS] Eq. (7), eta of [KLS] Eq. (8). Earth speed
v_E^ref = 250.5 km/s for both components (as WE 10.1).
Kernel: kernel21.py; k(v) = P C(v)/v. For the shell, R_DF = int dv v/(2 v_flow v_E) * P C(v)/v
        = (P / v_flow) * Cbar, with Cbar the mean of C(v) over v_flow - v_E < v < v_flow + v_E.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kernel21 import kernel, cumulative, prefactor, rate_eta, spectrum_eta, CKM  # noqa: E402
from halo21 import (eta_shm, eta_df, fspeed_shm, fspeed_df, V_FLOW, EPS_DF, VE_REF, VMAX, VESC,  # noqa: E402
                    vE_of_t)

LOG = open(os.path.join(HERE, "we21_1.log"), "w")


def say(s):
    print(s)
    LOG.write(s + "\n")


M = 10e6
P = prefactor(M)
lo, hi = V_FLOW - VE_REF, V_FLOW + VE_REF
say(f"prefactor P(10 MeV) = {P:.4e} /kg/yr; debris-flow window {lo:.1f}-{hi:.1f} km/s")
say(f"1/v_flow = c/{V_FLOW:.0f} km/s = {CKM/V_FLOW:.1f} (natural); 2 v_flow v_E = {2*V_FLOW*VE_REF:.0f} (km/s)^2")

v = np.linspace(lo, hi, 200001)
C = cumulative(M, v)
Cbar = np.trapezoid(C, v) / (hi - lo)
R_df_kernel = P * CKM / V_FLOW * Cbar
R_df_eta = rate_eta(M, lambda u: eta_df(u))
R_df_quad = np.trapezoid(fspeed_df(v) * kernel(M, v), v)
for vv in [150.0, 200.0, 300.0, 400.0, 500.0, 590.0]:
    say(f"  C({vv:.0f} km/s) = {float(cumulative(M, vv)):.4e}; k = {float(kernel(M, vv)):.4e} /kg/yr")
say(f"C at v_max = {float(cumulative(M, VMAX)):.4e} (the WE 10.1 integral uses eta instead: 0.652)")
say(f"Cbar over the window = {Cbar:.4e}")
vk = np.trapezoid(v * kernel(M, v), v) / (hi - lo)
say(f"mean of v k(v) over the window = {vk:.4e} km/s /kg/yr; divided by v_flow: {vk/V_FLOW:.4e} /kg/yr")
say(f"R_DF from (P/v_flow) Cbar = {R_df_kernel:.4e}; from int F_DF k dv = {R_df_quad:.4e}; "
    f"from P sum w eta_DF = {R_df_eta:.4e} /kg/yr")

vs = np.linspace(0.5, VMAX, 400001)
R_shm_kernel = np.trapezoid(fspeed_shm(vs) * kernel(M, vs), vs)
R_shm = rate_eta(M, lambda u: eta_shm(u))
say(f"R_SHM from int F_SHM k dv = {R_shm_kernel:.4e}; from P sum w eta = {R_shm:.4e} /kg/yr (WE 10.1: 1.60e5)")
say(f"per particle: R_DF / R_SHM = {R_df_eta/R_shm:.4f}")
R_mix = (1 - EPS_DF) * R_shm + EPS_DF * R_df_eta
say(f"mixed halo, eps = {EPS_DF}: R = {1-EPS_DF:.2f} x {R_shm:.4e} + {EPS_DF:.2f} x {R_df_eta:.4e} = {R_mix:.4e} /kg/yr; "
    f"ratio to SHM {R_mix/R_shm:.4f}; per kg-day {R_mix/365.25:.1f}")

# mean speed and <1/v> of the two components for the explanation
inv_df = float(eta_df(0.0)) * CKM
inv_shm = float(eta_shm(0.0)) * CKM
say(f"<1/v>: SHM {inv_shm:.1f}, debris flow {inv_df:.1f} (natural) = c/{CKM/inv_df:.1f} km/s")
frac_df = np.trapezoid(fspeed_df(v)[v > 400], v[v > 400])
frac_shm = np.trapezoid(fspeed_shm(vs)[vs > 400], vs[vs > 400])
say(f"fraction of particles above 400 km/s: SHM {frac_shm:.3f}, debris flow {frac_df:.3f}")

# spectra
for name, ef in [("SHM", lambda u: eta_shm(u)), ("DF", lambda u: eta_df(u))]:
    E, s = spectrum_eta(M, ef)
    say(f"  spectrum {name}: peak {E[np.argmax(s)]:.1f} eV, mean {np.sum(E*s)/np.sum(s):.2f} eV, "
        f"share below 4.9 eV {np.sum(s[E < 4.95])/np.sum(s):.3f}, ends at {E[np.nonzero(s)[0][-1]]:.1f} eV")
E, s1 = spectrum_eta(M, lambda u: eta_shm(u))
_, s2 = spectrum_eta(M, lambda u: eta_df(u))
sm = (1 - EPS_DF) * s1 + EPS_DF * s2
say(f"  spectrum mixed: mean {np.sum(E*sm)/np.sum(sm):.2f} eV; largest debris-flow deposit "
    f"0.5 m (v_flow+v_E)^2 = {0.5*M*(hi/CKM)**2:.2f} eV")

# light mediator, and 1 MeV, for the closing remark
for mm, med in [(10e6, "light"), (1e6, "heavy"), (3e6, "heavy"), (100e6, "heavy")]:
    a = rate_eta(mm, lambda u: eta_shm(u), med)
    b = rate_eta(mm, lambda u: eta_df(u), med)
    mix = (1 - EPS_DF) * a + EPS_DF * b
    say(f"m = {mm/1e6:g} MeV, {med}: R_SHM = {a:.4e}, R_DF = {b:.4e}, R_DF/R_SHM = {b/a:.4f}, mixed/SHM = {mix/a:.4f}")

# floors
say(f"largest laboratory speed of the debris flow {hi:.1f} km/s < v_max = {VMAX:.1f} km/s")
vE = vE_of_t(np.arange(7305) * 365.25 / 7305)
vm_jun = VESC + vE.max()
say(f"June: v_esc + |v_E| = {vm_jun:.1f} km/s; floor ratio (v_max/v_Jun)^2 = {(VMAX/vm_jun)**2:.4f} "
    f"({100*((VMAX/vm_jun)**2-1):.1f} %)")
CK = 299792.458
for Eth, lab in [(1.170, "Si E_g(0) = 1.170 eV"), (1.1553, "Si exciton 1.1553 eV")]:
    mm = 2 * Eth / (VMAX / CK) ** 2 / 1e6
    say(f"floor 2E/v_max^2 for {lab}: {mm:.4f} MeV; with the June speed {2*Eth/(vm_jun/CK)**2/1e6:.4f} MeV")
say(f"debris-flow-only halo, 1.170 eV: smallest mass {2*1.170/(hi/CK)**2/1e6:.4f} MeV")

# year-averaged standard-halo rate at 10 MeV against the rate at v_E^ref (Limit Check 21.1a context)
tt = np.arange(730) * 365.25 / 730
vEt = vE_of_t(tt)
for mm in [10e6, 1e6]:
    vm_, w_ = __import__("kernel21").bins(mm)
    sel = w_ > 0
    eavg = np.mean([eta_shm(vm_[sel], ve) for ve in vEt], axis=0)
    Ravg = prefactor(mm) * np.sum(w_[sel] * eavg * CKM)
    Rref = rate_eta(mm, lambda u: eta_shm(u))
    say(f"m = {mm/1e6:g} MeV heavy: year-averaged SHM rate {Ravg:.4e} vs v_E^ref {Rref:.4e}; ratio {Ravg/Rref:.4f}")
