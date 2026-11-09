#!/usr/bin/env python3
"""WP5-AUD checks (R14 joint audit of WP5-v4 and WP7-E-v3; yield sites of WP8-R, WP8-F).

Closed-form sympy/numpy checks only (no DFT/MD/MC).  Cited in returns/R14/WP5-AUD.md as AUD-Cn.
Run:  python3 checks.py      (< 30 s)
Inputs and provenance are in the return (section 'Provenance').  WP8-R's figure-of-merit functions are
re-implemented here with the same formulas as code/WP8-R/checks.py (fom, fom_int, fom_prim) so that the
yield inputs can be varied; C7a checks that they reproduce WP8-R's published numbers first.
"""
import math, sys
import numpy as np
import sympy as sp

R = []
def rep(name, ok, note=""):
    R.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {note}")

S, Q = sp.simplify, sp.Rational
g, y, r, dl, dN, dE, e, xN, xE, h = sp.symbols('g y r delta dN dE e xN xE h', real=True)
eps_p = sp.Symbol('eps_p', positive=True)

# ---------------------------------------------------------------- C1: eta^phi_NR from the calibration procedure (1803.02903 Eq. (1), p. 6;
# phonon scale fixed on bulk ER, p. 8; MC recoil energies rescaled by eta, p. 15)  ->  general-r_coll first order (IF-R13-2)
S_ER = eps_p*((1 - dE) + r*g)                 # ER, y = 1: primary (1 - d'_ER) + NTL r g   (per unit omega)
S_NR = eps_p*((1 - dl)*(1 - dN) + r*g*y)      # NR: primary (1-delta)(1-d'_NR) + NTL r g y
eta = S((1 + g)/S_ER*S_NR - g*y)              # E_R^rec/omega = E_phi - E_Q eV_b/eps  with ER-calibrated scales
lin = sp.expand(sp.series(eta.subs({dl: h*dl, dN: h*dN, dE: h*dE}), h, 0, 2).removeO().subs(h, 1))
w = (1 + g)/(1 + r*g); kr = (1 + r*g*y)/(1 + r*g); rterm = g*(r - 1)*(1 - y)/(1 + r*g)
rep("AUD-C1a eta independent of eps_prim; 1 - eta = g(r-1)(1-y)/(1+rg) + w(r)[delta + d'_NR - kappa_cal(r) d'_ER] + O(2), "
    "w = (1+g)/(1+rg), kappa_cal(r) = (1+rgy)/(1+rg)",
    S(sp.diff(eta, eps_p)) == 0 and S(1 - lin - (rterm + w*(dl + dN - kr*dE))) == 0)
rep("AUD-C1b r = 1: w = 1, kappa_cal(1) = (1+gy)/(1+g) = WP7-E-v3 (E13) / LIMITS L38",
    S(w.subs(r, 1) - 1) == 0 and S(kr.subs(r, 1) - (1 + g*y)/(1 + g)) == 0)
rep("AUD-C1c d kappa_cal/dr = g(y-1)/(1+rg)^2 < 0 for y < 1 (kappa_cal(r) <= kappa_cal(1) for r >= 1)",
    S(sp.diff(kr, r) - g*(y - 1)/(1 + r*g)**2) == 0)
nv = {g: Q(400, 382), y: Q(3, 10), r: Q(1144, 1000)}
wn, kn, k1 = float(w.subs(nv)), float(kr.subs(nv)), float(kr.subs({**nv, r: 1}))
rep("AUD-C1d numbers: g_Luke = 1.047, kappa_cal(1) = 0.642; r = 1.144: w = 0.931, kappa_cal(r) = 0.618, w*kappa = 0.576",
    abs(float(nv[g]) - 1.047) < 1e-3 and abs(k1 - 0.642) < 1e-3 and abs(wn - 0.931) < 1e-3 and abs(kn - 0.618) < 1e-3
    and abs(wn*kn - 0.576) < 1e-3, f"w={wn:.4f} k(r)={kn:.4f} wk={wn*kn:.4f} k(1)={k1:.4f}")
# accuracy of the two forms at the degenerate point with sample deficits
pt = {**nv, dl: Q(5, 1000), dN: Q(2, 100), dE: Q(1, 100)}
ex = float(1 - eta.subs(pt)); gen = float((rterm + w*(dl + dN - kr*dE)).subs(pt))
a4 = float((rterm + dl + dN - (1 + g*y)/(1 + g)*dE).subs(pt))
rep("AUD-C1e at r = 1.144, delta = 0.005, d'_NR = 0.02, d'_ER = 0.01: general form error O(d^2) << A-4 (r=1 weights) error",
    abs(gen - ex) < 4e-4 and abs(a4 - ex) > 4*abs(gen - ex), f"exact {ex:.5f} general {gen:.5f} A-4 {a4:.5f}")

# ---------------------------------------------------------------- C2: data bound E_st/omega <= 1 - eta at general r (B-a..B-d), exact
etaB = S(eta.subs({dN: e + xN, dE: xE}))
rep("AUD-C2a exact with delta = X = 0: 1 - eta - e = g(r-1)(1-y-e)/(1+rg)  (no series)",
    S(1 - etaB.subs({dl: 0, xN: 0, xE: 0}) - e - g*(r - 1)*(1 - y - e)/(1 + r*g)) == 0)
rng = np.random.default_rng(1)
worst = 1.0
for _ in range(20000):
    gg, yy, rr = rng.uniform(0.3, 30), rng.uniform(0.05, 0.6), rng.uniform(1, 1.4)
    ee = rng.uniform(0, min(0.15, 1 - yy)); dd = rng.uniform(0, 0.1); xe = rng.uniform(0, 0.1)
    kk = (1 + rr*gg*yy)/(1 + rr*gg); xn = kk*xe + rng.uniform(0, 0.1)
    et = (1 + gg)*((1 - dd)*(1 - ee - xn) + rr*gg*yy)/((1 - xe) + rr*gg) - gg*yy
    worst = min(worst, (1 - et) - ee)
rep("AUD-C2b exact (not first-order) scan, 2e4 points: (B-a) delta>=0, (B-b) r>=1, (B-c) X_NR >= kappa_cal(r) X_ER, (B-d) e<=1-y "
    "=> E_st/omega <= 1 - eta", worst >= -1e-12, f"min(1-eta-e) = {worst:.2e}")
rep("AUD-C2c (B-c) with kappa_cal(1) implies (B-c) with kappa_cal(r) for r >= 1 (X_ER >= 0): the stated WP7-E condition suffices",
    all(float(kr.subs({g: gg, y: yy, r: rr})) <= float(kr.subs({g: gg, y: yy, r: 1})) + 1e-15
        for gg in (0.5, 1.047, 25.0) for yy in (0.1, 0.3, 0.9) for rr in (1.0, 1.144, 1.5)))

# ---------------------------------------------------------------- C3: energy ledger (E1-pr) -> (W4'), mu_F independence, D' completeness
Nef, Nhf, Net, Nht, NX, Ec, Ev, mu, Eg, ExB, Etre, Etrh = sp.symbols('Nef Nhf Net Nht NX Ec Ev mu Eg ExB Etre Etrh', real=True)
Etrap = Net*(Ec - Etre - mu) + Nht*(mu - Ev - Etrh)
rhs_pr = Nef*(Ec - mu) + Nhf*(mu - Ev) + (NX*(Ec - Ev) - NX*ExB) + Etrap          # pair + exciton + trap terms of (E1-pr)
neut = {Nhf: Nef + Net - Nht}                                                     # N_e^f + N_e^tr = N_h^f + N_h^tr
Neh = Nef + NX; Eunp = (Nhf - Nef)*(mu - Ev)
rep("AUD-C3a (E1-pr) pair/exciton/trap terms = N_eh E_g + E_pairs^unp + E_trap^pr + DeltaE_X^b  (N_eh = N_e^f + N_X, E_g = E_c - E_v)",
    S((rhs_pr - (Neh*(Ec - Ev) + Eunp + Etrap - NX*ExB))) == 0)
rep("AUD-C3b E_pairs^unp + E_trap^pr is mu_F-independent under neutrality (and not without it)",
    S(sp.diff((Eunp + Etrap).subs(neut), mu)) == 0 and S(sp.diff(Eunp + Etrap, mu)) != 0)
# D' completeness at t_win: zero-field toy, pairs (incl. excitons) return E_g to phonons with probability P_g(t_win)
om, NNR, NER, Pg, DNR, DER, dc = sp.symbols('omega N_NR N_ER P_g Dp_NR Dp_ER delta_c', positive=True)
YH_full = (1 - dc)*(om - DNR - NNR*Eg*(1 - Pg))/(om - DER - NER*Eg*(1 - Pg))
YH_A4 = (1 - dc)*(om - DNR)/(om - DER)
rep("AUD-C3c (E1) at t_win: Y_H with the full pre-sensor deficit equals A-4/(E7) only if P_g(t_win) = 1 (E_pairs = E_X = 0 at t_win)",
    S(YH_full.subs(Pg, 1) - YH_A4) == 0 and S(YH_full - YH_A4) != 0)
gapNR = (1 - 0.102)*1.17/3.75          # NR-minus-ER gap fraction Delta f_g (WP8-R (b)), 2303.02196 yield at 100 eV
rep("AUD-C3d size: unreleased gap energy shifts zero-field Y_H by +(1-y)E_g/eps_eh (1-P_g) = +0.28 (Si, 100 eV) at P_g = 0",
    abs(gapNR - 0.280) < 2e-3, f"{gapNR:.3f}")
# pre-t_pr bias work: booked in H (A-12) but it is NTL heat (weight eps_NTL), NOT part of the eps_prim argument omega - D'
Wpr, NTL, er_, ep_ = sp.symbols('W_pr NTL eps_r eps_q', positive=True)
Esig_once = ep_*(om - DNR) + er_*NTL            # NTL = W_bias - Delta E_es over the whole drift, includes W_pr
Esig_twice = ep_*(om - DNR + Wpr) + er_*NTL     # if the W_pr booked in H_pr were also counted as primary heat
rep("AUD-C3e pre-t_pr bias work counted once: weighting H_pr (which contains W_pr) by eps_prim double-counts W_pr by eps_prim*W_pr",
    S(Esig_twice - Esig_once - ep_*Wpr) == 0)

# ---------------------------------------------------------------- C4: quench reading of E_st (IF-R13-3; WP5v4-C39 re-derived)
xx, m_, w_ = sp.symbols('x m w', positive=True)
psi0 = (m_*w_/sp.pi)**Q(1, 4)*sp.exp(-m_*w_*xx**2/2)
Vexp = sp.integrate(psi0**2*m_*w_**2*xx**2/2, (xx, -sp.oo, sp.oo))
cell = 3*0.045/4*4096
rep("AUD-C4 harmonic ground state <V> = w/4 per mode; 3<w>/4 = 33.8 meV/atom (<w> = 45 meV); 138 eV per 4096-atom cell",
    S(Vexp - w_/4) == 0 and abs(cell - 138.2) < 0.1, f"{cell:.1f} eV")

# ---------------------------------------------------------------- C5: visibility numbers (A-6; WP7-E-v3 (b), (b'))
Na = [16.3/(0.3*0.2), 16.3/(0.3*0.1)]; fp = [0.3*7, 0.3*9]
rep("AUD-C5 pocket N_a >= 272 (0.2 eV/atom) .. 543 (0.1 eV/atom) at 16.3 eV, eps_coll = 0.3; single FP visible iff E_thr <= 2.1..2.7 eV",
    abs(Na[0] - 271.7) < 0.1 and abs(Na[1] - 543.3) < 0.1 and abs(fp[0] - 2.1) < 1e-9 and abs(fp[1] - 2.7) < 1e-9, f"{Na}")

# ---------------------------------------------------------------- C6: Lindhard (WP5 L20 form, 2001.06503 Eq. (7)) vs 2303.02196 Table II
def lind(Z, A, EkeV):
    k = 0.133*Z**(2/3)*A**-0.5; ee = 11.5*Z**(-7/3)*EkeV; gg = 3*ee**0.15 + 0.7*ee**0.6 + ee
    return k*gg/(1 + k*gg)
L = {E: lind(14, 28.09, E/1000) for E in (100, 220, 300, 460)}
data = {100: (0.102, 0.072, 0.136), 220: (0.108, 0.098, 0.117), 460: (0.136, 0.128, 0.145)}   # Y, Y-, Y+ (2303.02196 Table II, PDF p. 5)
rep("AUD-C6 Lindhard 0.153 (Si) / 0.126 (Ge) at 100 eV (WP8-R C6); 2303.02196 Y lies below Lindhard at 100, 220, 460 eV",
    abs(L[100] - 0.153) < 1e-3 and abs(lind(32, 72.63, 0.1) - 0.126) < 1e-3 and all(data[E][2] < L[E] for E in data),
    f"Lindhard {[round(L[E],3) for E in L]}")

# ---------------------------------------------------------------- C7: WP8-R figure of merit with the measured yield and Fano inputs
eps_si = 3.75
def fom(ER, Vb, C, da, yy, sigE=2.65, F_ER=0.15, F_NR=1.0, q=1.0):
    gg = q*Vb/eps_si                       # q = <frak-q> collection (NTL gain g_Luke <q>)
    Etot = ER*(1 + yy*gg); E_er = Etot/(1 + gg)
    n_nr, n_er = yy*ER/eps_si, E_er/eps_si
    dO = C*(gg/(1 + gg) - yy*gg/(1 + yy*gg)); sn = sigE/Etot
    s_nr = math.sqrt(sn**2 + da**2 + (C*q*Vb*math.sqrt(F_NR*n_nr)/Etot)**2)
    s_er = math.sqrt(sn**2 + da**2 + (C*q*Vb*math.sqrt(F_ER*n_er)/Etot)**2)
    return dO/math.sqrt(0.5*(s_nr**2 + s_er**2))
def fom_int(ER, Vb, yy, F_ER=0.15, F_NR=1.0, q=1.0): return fom(ER, Vb, 1.0, 0.0, yy, 1e-9, F_ER, F_NR, q)
def fom_prim(ER, yy, C=1.0, sigE=2.65, da=0.0, fs=0.017): return C*(1 - yy)*fs/math.sqrt((math.sqrt(2)*sigE/ER)**2 + da**2)
def Cmin(E, da, yy, F_NR=1.0):
    best = None
    for Vb in np.arange(1, 40.5, 0.5):
        for C in np.arange(0.02, 1.0001, 0.01):
            if fom(E, Vb, C, da, yy, F_NR=F_NR) >= 2:
                if best is None or C < best[0]: best = (round(C, 2), Vb)
                break
    return best
yL = L[100]
rep("AUD-C7a re-implementation reproduces WP8-R: S_prim(100/300 eV) = 0.38/1.15; S_int(100 V; 100/300 eV) = 0.53/0.91; C_min = 0.15/0.28/0.53",
    abs(fom_prim(100, yL) - 0.38) < 0.01 and abs(fom_prim(300, yL) - 1.15) < 0.01
    and abs(fom_int(100, 100, yL) - 0.53) < 0.01 and abs(fom_int(300, 100, L[300]*0 + yL) - 0.91) < 0.01
    and [Cmin(100, d, yL)[0] for d in (0.02, 0.05, 0.10)] == [0.15, 0.28, 0.53])
ok_a = all(fom_prim(E, yy) < 2 for E in (50, 100, 300) for yy in np.linspace(0, 0.25, 26))
E2 = min(E for E in np.arange(10, 5000, 1.0) if fom_prim(E, 0.072) >= 2)
rep("AUD-C7b (a) primary route: S < 2 at E_R <= 300 eV for every yield in [0, 0.25]; with Y(100 eV) lower edge 0.072, 2 sigma first at >= 0.47 keV",
    ok_a and E2 >= 470, f"E_2sigma = {E2:.0f} eV")
# energy-matched measured inputs (2303.02196 Table II): 100 eV Y 0.072-0.136, F 0.5-1.6; 220 eV Y 0.098-0.117, F 0.4-0.7;
# 300 eV bracketed by the 220/460 eV bands: Y 0.098-0.145, F 0.4-2.4.  F_ER -> F_meas^obs in [0.119, 0.3]; <q> in {0.873, 1}
bands = {100: ((0.072, 0.102, 0.136), (0.5, 0.9, 1.6)), 220: ((0.098, 0.108, 0.117), (0.4, 0.5, 0.7)), 300: ((0.098, 0.12, 0.145), (0.4, 0.9, 2.4))}
smax = max(fom_int(E, 100, yy, F_ER=fe, F_NR=fn, q=qq) for E, (Ys, Fs) in bands.items() for yy in Ys for fn in Fs
           for fe in (0.119, 0.15, 0.3) for qq in (0.873, 1.0))
rep("AUD-C7c (c) HV (100 V) ceiling with energy-matched measured Y and F_NR (2303.02196): S_int < 2 at E_R <= 300 eV",
    smax < 2, f"max S_int = {smax:.3f} (300 eV, Y = 0.098, F_NR = 0.4, F_ER = 0.119: band edge)")
s015 = fom_int(300, 100, 0.102, F_ER=0.15, F_NR=0.15)
rep("AUD-C7c' WP8-R C7l ('robust at F_NR = 0.15') fails with the measured yield: S_int(300 eV, Y = 0.102, F_NR = 0.15) > 2; "
    "the HV NO-GO rests on F_NR >= 0.4 (measured)", s015 > 2, f"{s015:.2f}")
cm = {d: Cmin(100, d, 0.102, F_NR=0.9) for d in (0.02, 0.05, 0.10)}
rep("AUD-C7d (d) low bias, Y = 0.102, F_NR = 0.9 (2303.02196): zeta_O,min(100 eV) = 0.13/0.24/0.44 at sigma_pos = 0.02/0.05/0.10 (WP8-R: 0.15/0.28/0.53)",
    [cm[d][0] for d in (0.02, 0.05, 0.10)] == [0.13, 0.24, 0.44], f"{cm}")
dfg = [(1 - yy)*1.17/3.75 for yy in (0.102, 0.072, 0.136)]
rep("AUD-C7e (b) Delta f_g = (1-Y)E_g/eps_eh = 0.28 (0.27-0.29) with the measured Si yield (WP8-R: 0.26 Lindhard)",
    abs(dfg[0] - 0.28) < 0.005, f"{[round(v,3) for v in dfg]}")

# ---------------------------------------------------------------- C8: theta_coll prior on r_coll (WP7-E-v3 sec. 6) vs the degenerate point
from math import erf, log, sqrt
Phi = lambda z: 0.5*(1 + erf(z/sqrt(2)))
z05, z20 = log(1.144)/0.05, log(1.144)/0.2
rep("AUD-C8a sigma_ln = 0.05 puts r_coll = 1.144 at 2.69 sigma (tail 0.36%) and |r-1| = 0.2 (WP8-R) at 3.6 sigma; sigma_ln = 0.2: 0.67 sigma",
    abs(z05 - 2.69) < 0.01 and abs(1 - Phi(z05) - 0.0036) < 2e-4 and abs(log(1.2)/0.05 - 3.65) < 0.01 and abs(z20 - 0.67) < 0.01)
# profile illustration: datum 1-eta = 0.048, sigma = 0.0041 (95% band +0.9/-0.7 % -> 0.8/1.96); 1-eta = rterm(r) + w(r) e ; e >= 0 flat
gn, yn = 400/382, 0.3
es = np.linspace(0, 0.1, 801); lr = np.linspace(-0.6, 0.6, 1201)
def post(sig):                                                # (B-b) r >= 1 imposed; returns P(e < 0.01), median
    rr = np.exp(lr)[:, None]; ww = (1 + gn)/(1 + rr*gn); rt = gn*(rr - 1)*(1 - yn)/(1 + rr*gn)
    like = np.exp(-0.5*((rt + ww*es[None, :] - 0.048)/0.0041)**2)*np.exp(-0.5*(lr[:, None]/sig)**2)*(lr[:, None] >= 0)
    pe = like.sum(0); pe /= pe.sum(); c = np.cumsum(pe)
    return float(pe[es < 0.01].sum()), float(es[np.searchsorted(c, 0.5)])
(p05, m05), (p20, m20) = post(0.05), post(0.2)
rep("AUD-C8b prior width decides the E_st reading (r >= 1): median E_st/omega 0.036 vs 0.026, P(E_st/omega < 0.01) 3% vs 18% "
    "for sigma_ln(r) = 0.05 vs 0.2, same datum", abs(m05 - 0.036) < 0.002 and abs(m20 - 0.026) < 0.002 and p05 < 0.04 and p20 > 0.15,
    f"median {m05:.4f}/{m20:.4f}, P {p05:.3f}/{p20:.3f}")

# ---------------------------------------------------------------- C9: theta_K tilt (WP6-v3 (5.1'')) for a one-path class
tg = np.linspace(0.1, 5, 40); Sc = np.exp(-tg)              # 1 energy point, many times
Ev = np.full_like(tg, 2.0)
Hm = np.array([[np.sum(Sc), np.sum(Sc*Ev)], [np.sum(Sc*Ev), np.sum(Sc*Ev**2)]])
psi = 0.3*np.log(tg)                                         # a time-shape template
def tilt(l0):                                                # constraint fixes only l0 + 2 l1
    l1 = (np.log(np.sum(Sc)/np.sum(Sc*np.exp(psi))) - l0)/2.0
    return Sc*np.exp(psi + l0 + l1*Ev)
s1, s2 = tilt(0.0), tilt(0.7)
Ev2 = np.where(np.arange(40) % 2 == 0, 1.0, 3.0)
H2 = np.array([[np.sum(Sc), np.sum(Sc*Ev2)], [np.sum(Sc*Ev2), np.sum(Sc*Ev2**2)]])
rep("AUD-C9 one-path class: moment matrix of (1, E) singular, lambda non-unique but S(theta) unique (time-shape tilt only); "
    "two-path class: PD", abs(np.linalg.det(Hm)) < 1e-9*np.sum(Sc)**2 and np.allclose(s1, s2)
    and abs(np.sum(s1) - np.sum(Sc)) < 1e-9 and np.linalg.det(H2) > 0.1)

# ---------------------------------------------------------------- C10: threshold conversion for NTL phonon readout (WP8-F sec. 2.4(b))
YH0 = sp.Symbol('Y_H', positive=True)
Eee_NR = om*(YH0 + r*g*y)/(1 + r*g)          # ER-calibrated (keV_ee) NTL phonon energy of an NR, D'_ER = 0, Y_H = (1-delta)(1-d'_NR)
Ethee = sp.Symbol('E_th_ee', positive=True)
Ethnr = sp.solve(sp.Eq(Eee_NR.subs(om, sp.Symbol('Enr')), Ethee), sp.Symbol('Enr'))[0]
rep("AUD-C10 E_th^nr = E_th^ee (1 + r_coll g_Luke)/(Y_H + r_coll g_Luke y_ion); r = Y_H = 1: (1+g)/(1+gy); g -> 0: E_th/Y_H",
    S(Ethnr - Ethee*(1 + r*g)/(YH0 + r*g*y)) == 0 and S(Ethnr.subs({r: 1, YH0: 1}) - Ethee*(1 + g)/(1 + g*y)) == 0
    and S(Ethnr.subs(g, 0) - Ethee/YH0) == 0)

# ---------------------------------------------------------------- C11: bound arithmetic (WP7-E-v3 sec. 3.2; WP5-v4 sec. 6.3; LIMITS L36)
b = [0.048 + 0.007, 0.0608 + 2*0.0018]; ps = [b[0]/(0.4*0.65), b[1]/(0.4*0.8)]; pv = [ps[0]/(9/20), ps[1]/(6/19.7)]
rep("AUD-C11 0.055/0.064; p_surv E_st,1/E_d <= 0.21/0.20; p_surv <~ 0.47/0.66 (x1.01: 0.475/0.67; 0.48 is a rounding artefact) = WP8-F sec. 2.8(d)",
    round(b[0], 3) == 0.055 and round(b[1], 3) == 0.064 and round(ps[0], 2) == 0.21 and round(ps[1], 2) == 0.20
    and round(pv[0], 2) == 0.47 and round(pv[1], 2) == 0.66 and round(1.01*pv[0], 3) == 0.475 and round(1.01*pv[1], 2) == 0.67
    and round(0.056/0.26/0.45, 2) == 0.48, f"x1.01 Si: {1.01*pv[0]:.4f} (0.48 only after rounding 0.0556 -> 0.056)")

print(f"\n{sum(R)}/{len(R)} PASS")
sys.exit(0 if all(R) else 1)
