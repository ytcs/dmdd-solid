"""R16 / CW1 checks (closure of LE-24 ... LE-47, LE-178, LE-179), revised by ERR-CW1 (returns/R16/CW1-errata.md §4).
Run: python3 checks.py   (all PASS, < 1 min, one core, no QE calls; loads the committed Wannier TB, ~10 s).
ERR-CW1: tolerances tightened; checks that only compared a json value with a window fitted to it are replaced by recomputations from raw data
(C1 masses from raw eigenvalues; C4 Wannier TB re-evaluated at the stored optimum; C6, C9-C15 against the regenerated QE runs out/errata_qe*.json);
pure consistency checks are labelled [consistency]; C33-C52 check the errata corrections.
Labels CW1-Cn are cited in returns/R16/CW1.md.  [CALC] inputs are the JSON files in out/, produced by scripts/*.py from QE 7.6 runs
(inputs/, SG15 Si_ONCV_PBE-1.2 and _FR-1.1, PBE, a_exp = 10.2631 bohr unless stated) and from the COMP-PH Wannier TB (read-only).
Units: eV, Angstrom, keV as marked; hbar = c = 1."""
import json, os, sys
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import sympy as sp
from scipy import integrate

H = os.path.dirname(os.path.abspath(__file__)); O = lambda f: json.load(open(f"{H}/out/{f}"))
sys.path.insert(0, f"{H}/scripts")
RES = []
def check(label, cond, note=""):
    RES.append((label, bool(cond))); print(f"{label:8s} {'PASS' if cond else 'FAIL'}  {note}")

me = 510998.95; A2eV = 1973.27; vmax = 794.5/299792.458; alpha = 1/137.035999

# ---------------- LE-24: masses, Q_w, thresholds ----------------
M = O("masses.json")
mhh = M["holes_100"][2]; Mx = M["m_l"] + mhh
kr, Er = np.array(M["raw"]["k"]), np.array(M["raw"]["E"]); conv = (2*np.pi/(10.2631*0.529177))**2*7.61996     # eV per unit curvature in (2pi/a)^2 at m = m_e
cb = Er[1:30, 4]; i0 = int(np.argmin(cb)); sl = slice(i0-3, i0+4)
p2 = np.polyfit(kr[1:30, 0][sl], cb[sl], 2); kc_raw = -p2[1]/(2*p2[0]); ml_raw = conv/(2*p2[0])                     # parabola, 7 points (as masses.py)
p4 = np.polyfit(kr[1:30, 0][sl], cb[sl], 4); r4 = np.real(np.roots(np.polyder(p4))); k4 = r4[np.argmin(abs(r4-kc_raw))]; ml4 = conv/np.polyval(np.polyder(p4, 2), k4)
mt_raw = conv/(2*np.polyfit(np.array([.01, .02, .03])**2, Er[30:33, 4]-Er[15, 4], 1)[0])
mhh_raw = conv/(-2*np.polyfit(np.array([.01, .02, .03])**2, Er[[33, 36, 39], 3]-Er[0, 3], 1)[0]); Mx = ml_raw + mhh_raw
mhh0 = conv/(-2*np.polyfit(np.array([0, .01, .02])**2, Er[[0, 33, 36], 3]-Er[0, 3], 1)[0])
check("CW1-C1", abs(kc_raw-M["kc"]) < 1e-4 and abs(ml_raw/M["m_l"]-1) < 1e-3 and abs(mt_raw/M["m_t"]-1) < 1e-3 and abs(mhh_raw/mhh-1) < 1e-3 and abs(Mx-1.19) < 0.01
      and abs(ml4/ml_raw-1) < 0.05 and abs(mhh0/mhh_raw-1) < 0.03,
      f"recomputed from the raw QE eigenvalues: k_c={kc_raw:.4f} X, m_l={ml_raw:.3f} (quartic fit {ml4:.3f}: nonparabolicity 3%), m_t={mt_raw:.3f}, m_hh[100]={mhh_raw:.3f} (d = 0-0.02: {mhh0:.3f}); "
      f"M_x = m_l + m_hh = {Mx:.3f} m_e (PBE, no SOC; WP1 1.19 confirmed; the source of WP3's 1.41 is not stated, ERR-CW1 E-3)")
Qw = lambda Mx_, d0, c=5.63/299792.458: (Mx_*me*c + np.sqrt((Mx_*me*c)**2 + 2*Mx_*me*d0))/A2eV
check("CW1-C2", 0.30 < Qw(Mx, 0.3) < 0.32 and 0.32 < Qw(1.41, 0.3) < 0.345, f"Q_w(delta0=0.3 eV) = {Qw(Mx,0.3):.3f} 1/A [M_x CALC] vs {Qw(1.41,0.3):.3f} (1.41 m_e)")
# Luttinger-type (no-SOC Dresselhaus) inverse-mass parameters from the hole masses (LE-29)
Lp, Mp = 1/M["holes_100"][0], 1/mhh
N110 = [2/M["holes_110"][0]-Lp-Mp, Lp+Mp-2/M["holes_110"][2]]; N111 = [(3/M["holes_111"][0]-Lp-2*Mp)/2, Lp+2*Mp-3/M["holes_111"][2]]
check("CW1-C3", abs(1/M["holes_110"][1]-Mp)/Mp < 0.02 and np.ptp(N110+N111)/np.mean(N110+N111) < 0.08,
      f"L={Lp:.2f}, M={Mp:.2f}, N={np.mean(N110+N111):.2f} (spread {np.ptp(N110+N111):.2f}) in units 1/m_e; [110] middle band = M (Delta_5 x2 structure)")

F = O("emin_fast.json"); X = O("emin_extra.json")
mq = lambda qkeV, E: (qkeV*1e3)**2/(2*(qkeV*1e3*vmax - E))/1e6
from wannier_si import bands, sc as sc_w, tpiba, nv
Kk = 1/(3.7289*tpiba); pairE_w = lambda k, q: bands((k+q)[None])[0, nv]-bands(k[None])[0, nv-1]+sc_w
def m_w(x): qa = np.linalg.norm(x[:3])/Kk; return (qa*1e3)**2/(2*(qa*1e3*vmax-pairE_w(x[3:], x[:3])))/1e6
x0 = np.r_[F["q_vec_2pi_a"], F["k_v"]]; Ew = pairE_w(np.array(F["k_v"]), np.array(F["q_vec_2pi_a"]))
gr = np.array([(m_w(x0+1e-4*np.eye(6)[i])-m_w(x0-1e-4*np.eye(6)[i]))/2e-4 for i in range(6)]); hd = [m_w(x0+3e-3*np.eye(6)[i])+m_w(x0-3e-3*np.eye(6)[i])-2*m_w(x0) for i in range(6)]
check("CW1-C4", abs(Ew-F["E_pair"]) < 1e-7 and abs(m_w(x0)-F["m_ZPL"]) < 1e-7 and np.max(abs(gr)) < 2e-3 and min(hd) > 0 and F["theta_rad"] > 0.1,
      f"Wannier TB re-evaluated at the stored optimum: E = {Ew:.6f} eV, m_ZPL = {m_w(x0):.5f} MeV, |grad m| <= {np.max(abs(gr)):.1e} MeV/(2pi/a), positive diagonal curvature; |q| = {F['q_keV']:.3f} keV, theta = {F['theta_rad']:.3f} rad")
ax_m = min(r[2] for kk, rows in F["scan"].items() for r in rows if r[0] == 0.0)
check("CW1-C5", abs(sorted(F["all"])[-1] - 0.4150) < 0.002 and all(rows[0][1] > min(r[1] for r in rows) + 0.01 for kk, rows in F["scan"].items()),
      f"on-axis local optimum 0.4150 MeV (COMP-PH 0.4154 reproduced); at |q| = 1.2-1.48 keV the [100] axis is a local MAXIMUM of E_min(theta) (min over angle lower by 14-107 meV)")
vo_p, vo_e = O("vertex_opt_a10.3507.json"), O("vertex_opt_a10.2631.json")
E_pbe = vo_p["Epair_PBE"] + vo_p["dE_local"] + (1.170 - 0.602); E_exp = vo_e["Epair_PBE"] + vo_e["dE_local"] + (1.170 - M["Eg_PBE"])
qn = np.linalg.norm(F["q_vec_2pi_a"]); q_exp = qn*2*np.pi/10.2631*3.7289
m_pbe, m_exp = mq(F["q_keV"], E_pbe), mq(q_exp, E_exp)
QE1, QS, QSc = O("errata_qe.json"), O("errata_qe_it2_SOC.json")["SOC"], O("errata_qe_it2_S12.json")["S12"]
check("CW1-C6", abs(QE1["S12"]["Epair_PBE"]-vo_e["Epair_PBE"]) < 2e-5 and abs(QE1["S12"]["gap_PBE"]-M["Eg_PBE"]) < 2e-5 and abs(m_pbe-0.4019) < 3e-4 and abs(m_exp-QE1["S12"]["m_center"]) < 3e-4,
      f"[regenerated] QE at the Wannier optimum reproduces CW1 pass 5 (E_pair {QE1['S12']['Epair_PBE']:.6f} vs {vo_e['Epair_PBE']:.6f} eV, gap {QE1['S12']['gap_PBE']:.5f}); a_PBE m = {m_pbe:.4f}, a_exp m = {QE1['S12']['m_center']:.4f} MeV (scalar, not re-minimised)")
Eb = 0.0147; qS = QS["q_keV_reminimised"]*1e3; mS = QS["m_center"]
dm1s = mS*Eb/(qS*vmax - QS["E_scissored"]); dm2p = dm1s/4
L2 = json.load(open(f"{H}/inputs/errata/labels2_SOC.json")); qS = np.linalg.norm(np.array(L2["k_e"])-L2["k_h"])*3.7289*2*np.pi/10.2631*1e3
dm1s = mS*Eb/(qS*vmax - QS["E_scissored"]); dm2p = dm1s/4
check("CW1-C7", abs(dm1s-0.0028) < 2e-4 and abs(mq(qS/1e3, QS["E_scissored"]) - mS) < 1e-7, f"bound-line shift of the SOC onset {mS:.4f}: 1s -{dm1s:.4f} MeV (1s onset {mS-dm1s:.4f}), 2p -{dm2p:.4f} MeV")
check("CW1-C8", abs(X["U200"]["m"]-0.4992) < 2e-4 and abs(X["U200"]["m"] - X["G0_beyondX"]["m"]) < 1e-4,
      f"(2bar00)-class edge (unfolded electron beyond the X face) m = {X['U200']['m']:.4f} MeV at |q| = {X['U200']['q_keV']:.3f} keV; inversion image {X['G0_beyondX']['m']:.4f}")

# ---------------- LE-25: vertices, symmetry controls ----------------
V4, V6 = O("vertex40.json"), O("vertex60.json")
check("CW1-C9", V4["axis_G0_sum_v_|rho_c1v|^2"] < 1e-12 and V6["axis_G0_sum_v_|rho_c1v|^2"] < 1e-12,
      "control C10a (WP1-v3 §3.2): G'=0 on-axis vertex at the extremum vanishes (< 1e-12) at 40 and 60 Ry")
u4, u6 = V4["umklapp"]["U200_1.1571"]["c1"], V6["umklapp"]["U200_1.1571"]["c1"]
check("CW1-C10", abs(u4-0.150) < 0.002 and abs(u4-u6)/u6 < 0.005 and V4["umklapp"]["U111"]["c1"] < u4,
      f"[consistency, 40 vs 60 Ry; not regenerated] (2bar00) vertex at the extremum sum_v|rho|^2 = {u4:.4f} (40 Ry), {u6:.4f} (60 Ry); (1bar11) {V4['umklapp']['U111']['c1']:.4f}: NOT small")
P = O("vertex_pair40.json")
check("CW1-C11", all(P[f"U200_{s}"]["rho2_hh"] < 1e-12 and P[f"U200_{s}"]["rho2_all"] > 0.1 for s in ("1.0", "1.05", "1.1")) and P["pair_axis_rho2_all"] < 1e-12,
      "on the axis the (2bar00) vertex lives entirely in the light hole (Delta_2'), heavy holes (Delta_5) give 0: multiplicity-1 rule B2 x (B2+E) of WP1-v3 §3.2(c)")
O2 = O("vertex_opt2_a10.3507.json")
VE = QE1["S12"]["vertex"]; O2e = O("vertex_opt2_a10.2631.json")
check("CW1-C12", O2["rho2_per_v"][2] < 1e-12 and VE["rho2_per_band"][3] < 1e-11 and abs(VE["rho2_per_band"][2]/O("vertex_opt2_a10.2631.json")["rho2_per_v"][1]-1) < 2e-3,
      f"[regenerated] mirror rule: at the {{001}}-plane optimum the top (heavy) hole vertex vanishes ({VE['rho2_per_band'][3]:.1e}; CW1 {O2['rho2_per_v'][2]:.1e}); 2nd band {VE['rho2_per_band'][2]:.4f} at -{O2['Epair_top_minus_second_eV']:.2f} eV")
U = O("vertex_U200opt.json")
check("CW1-C13", abs(U["xc"]["rho2_c1_top"]-0.0095) < 2e-4 and abs(U["xc"]["rho2_c12_top"]-0.028) < 5e-4 and U["xc0.05"]["rho2_c1_top"] > U["xc"]["rho2_c1_top"],
      f"[consistency; not regenerated] (2bar00) class in the mirror plane allowed for the top hole (glide phase -1): |rho|^2 = {U['xc']['rho2_c1_top']:.4f} (c1), {U['xc']['rho2_c12_top']:.4f} (c1+c2) at the X face, {U['xc0.05']['rho2_c1_top']:.4f} 0.05 inside")
g = [V4["grad_k_rho_Angstrom"][k] for k in ("y0.005", "y0.01")]; g6 = V6["grad_k_rho_Angstrom"]["y0.005"]
check("CW1-C14", abs(g[0]-g[1])/g[0] < 0.01 and abs(g[0]-g6)/g6 < 0.03 and abs(V4["grad_k_rho_Angstrom"]["yz0.005"]-g[0])/g[0] < 0.02
      and abs(VE["dqz_A"]/O2e["dqz_top_A"]-1) < 0.01 and abs(VE["dkz_A"]/O2e["dkz_top_A"]-1) < 0.02,
      f"|d rho/d k_perp| at the extremum = {g[0]:.3f} A (60 Ry {g6:.3f}; C4v); [regenerated, step 0.02] mirror optimum (a_exp) |d_qz rho| = {VE['dqz_A']:.3f} (CW1 {O2e['dqz_top_A']:.3f}), |d_kz rho| = {VE['dkz_A']:.3f} (CW1 {O2e['dkz_top_A']:.3f}) A")
S = O("vertex_soc.json")
SX = QE1["SOC"]["soc_axis_extremum"]; SM = QE1["SOC"]["soc_mirror_optimum"]
check("CW1-C15", abs(SX["quartet_over2"]/(S["axis_extremum"]["all_valence"]/2)-1) < 1e-3 and abs(SX["quartet_over2"]-SX["all_valence_over2"]) < 1e-9
      and abs(SM["top_pair_over2"]/(S["mirror_optimum"]["top_pair"]/2)-1) < 0.01 and SX["top_pair_over2"] < SX["quartet_over2"] and max(abs(np.array(QE1["SOC"]["Gamma8_levels_meV"]))) < 1e-6,
      f"[regenerated] SOC-lifted vertex (scalar-equivalent): Gamma_8 quartet sum/2 at the on-axis extremum {SX['quartet_over2']:.2e} (CW1 run {S['axis_extremum']['all_valence']/2:.2e}; split-off adds 0); one Kramers pair "
      f"{SX['top_pair_over2']:.1e} here vs {S['axis_extremum']['top_pair']/2:.1e} in CW1 (gauge-dependent); mirror optimum {SM['top_pair_over2']:.3e} (CW1 {S['mirror_optimum']['top_pair']/2:.3e})")

# ---------------- LE-26: ratios (recomputed independently of ratio.py) ----------------
R = O("ratio.json")
mu = 1/(2*Eb*(4.9e-9/1.97327e-7)**2)
J = lambda e: (2*mu)**1.5*np.sqrt(e)/(4*np.pi**2)
SF = lambda e: 2*np.pi*np.sqrt(Eb/e)/(1-np.exp(-2*np.pi*np.sqrt(Eb/e)))
def e2opt(w):
    y = 0.65 + 78*(w-1.212) if w > 1.212 else max(0.65*(w-1.160)/0.052, 0)
    return (3.55+0.37*(w-1.17))*y**2/w*1.97327e-5/w
qa = 1390/A2eV; FF = np.exp(np.interp(qa, [0.6, 0.7, 0.8], np.log([0.077, 0.054, 0.040])))
g2 = 2*P["gradk_hh_A_0.005"]**2/A2eV**2
r_ax = (2*np.pi*alpha/1390**2)*4*np.pi*g2*(2*mu*0.1/3)*J(0.1)*SF(0.1)*(1+Eb/0.1)/(e2opt(1.455)*FF)
check("CW1-C16", abs(r_ax/R["G0_secondclass_q1.39keV"][2]["ratio"]-1) < 0.02 and r_ax < 0.1,
      f"on-axis second-class ZPL/PAER at eps_ex = 0.1 eV: {r_ax:.3f} (WP1-v3 [E14] central 2)")
# elliptic-cone angle average: closed form vs direct 2-D integration (u-substitution)
a_, b_ = R["offaxis_inputs"]["a_theta"], R["offaxis_inputs"]["b_z"]; e = 0.05
f2d = integrate.dblquad(lambda ph, th: (ph**2)*np.sqrt(max(e-a_*th**2-b_*ph**2, 0)), -np.sqrt(e/a_), np.sqrt(e/a_), lambda th: -np.sqrt(max(e-a_*th**2, 0)/b_), lambda th: np.sqrt(max(e-a_*th**2, 0)/b_))[0]
fcl = np.pi/(2*b_*np.sqrt(a_*b_))*integrate.quad(lambda u: u*np.sqrt(e-u), 0, e)[0]
check("CW1-C17", abs(f2d/fcl-1) < 1e-4, f"cone integral int ph^2 sqrt(e - a th^2 - b ph^2) = (pi/(2 b sqrt(ab))) int u sqrt(e-u) du: {f2d:.4e} vs {fcl:.4e}")
ra = [r["ratio_angleavg"] for r in R["G0_offaxis_optimum"]]; rs = [r["ratio_SOC_angleavg"] for r in R["G0_offaxis_SOC"]]
check("CW1-C18", abs(ra[1]-0.0157) < 5e-4 and abs(ra[3]-0.354) < 0.005 and max(rs) < 0.012 and abs(R["U200_Xface_xc"][1]["ratio"]-2.2) < 0.05,
      f"[CW1 values, superseded by C38-C40] angle-averaged forbidden-class ZPL/PAER at |q|_opt: {ra[1]:.3f} (E_x^b), {ra[2]:.3f} (50 meV), {ra[3]:.3f} (0.1 eV); SOC part <= {max(rs):.3f}; X-face allowed edge {R['U200_Xface_xc'][1]['ratio']:.2f}")
# reachable excess energy above E_min at the optimum |q| vs m_chi
q0 = F["q_keV"]*1e3; emx = lambda m: q0*vmax - q0**2/(2*m*1e6) - F["E_pair"]
emxS = lambda m: qS*vmax - qS**2/(2*m*1e6) - QS["E_scissored"]
check("CW1-C19", abs(emx(0.42)-0.100) < 0.005 and abs(emxS(0.42)-0.066) < 0.002 and abs(emxS(0.44)-0.161) < 0.003,
      f"eps_ex,max at |q|_opt: CW1 (Wannier, scalar) {emx(0.41):.3f}/{emx(0.42):.3f}/{emx(0.44):.3f} eV; errata (a_exp, SOC, re-minimised) {emxS(0.41):.3f}/{emxS(0.42):.3f}/{emxS(0.44):.3f} eV at 0.41/0.42/0.44 MeV")
# second-class line/continuum consistency (WP1 C8c) with the p-wave Sommerfeld factor
n, z = sp.symbols("n zeta", positive=True)
lines = sp.limit((n**2-1)/(3*sp.pi*n**5)*n**3, n, sp.oo)          # weight x level density n^3/(2 E_b) per unit E_b a_x^5 units
cont = sp.limit(sp.Rational(1, 3)*2*sp.pi*z/(1-sp.exp(-2*sp.pi*z))*(1+z**2)/z**3 * 1/(2*sp.pi**2) * sp.Rational(1, 1), z, sp.oo)
check("CW1-C20", sp.simplify(lines/2 - 1/(6*sp.pi)) == 0 and sp.simplify(cont - 1/(3*sp.pi)) == 0,
      "second-class: line density (n^2-1)/(3 pi n^5) x n^3/(2E_b) -> 1/(6 pi) per (a_x^5 E_b), p-wave continuum S_F(1+zeta^2) k^3/3 matches (WP1 C8c)")

# ---------------- LE-27: LO (2bar00) class, TA crossover ----------------
LO = O("lo_gamma.json")
Kpk = (2-0.842)*2*np.pi/(10.3507*0.529177); qX = 2*np.pi/(10.3507*0.529177)
neg = []
for Qv in (0.06, 0.10, 0.15):
    w0 = LO[f"{Qv}_001"]["w0"]; wd = (LO["0.2_001"]["w0"]-LO["0.1_001"]["w0"])/0.1; qq = Kpk - Qv
    coef = wd*qq*Kpk/(2*Qv) + w0*min(LO[f"{Qv}_001"]["gamma"], LO[f"{Qv}_011"]["gamma"])*qq**2/Qv**2
    neg.append(coef < 0)
check("CW1-C21", all(neg) and all(LO[k]["gamma"] < 0 for k in LO), "Si (2bar00)-class LO: v_g < 0 and gamma_w < 0 -> axis is a maximum of the threshold, minimum off axis: p_bar = 3, not 4")

# ---------------- LE-45: spin sum ----------------
px, py, pz = sp.symbols("p_x p_y p_z", real=True)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
Sdotp = sig[0]*px + sig[1]*py + sig[2]*pz
check("CW1-C22", sp.simplify(sum(sp.Abs(Sdotp[i, j])**2 for i in range(2) for j in range(2)).rewrite(sp.conjugate) - 2*(px**2+py**2+pz**2)) == 0,
      "sum_{ss'} |<s'|sigma.p|s>|^2 = 2|p|^2 (WP1-v3 §2.5: ALP spin sum = velocity form)")

# ---------------- LE-46: temperature transfer ----------------
kB = 8.617333e-5; wTA = 0.0186; nB = lambda w, T: 1/np.expm1(np.minimum(w/(kB*T), 700))
check("CW1-C23", abs(nB(wTA, 77)-0.0645) < 1e-3, f"n_TA(77 K) = {nB(wTA,77):.3f} (WP3-v3 §4(b) 0.07)")
w = np.linspace(1.10, 1.40, 1501); Eg0 = 1.170; dEg = 0.0040
A_true = lambda x: np.clip(x-Eg0, 0, None)**2                    # synthetic T-independent branch spectrum (p_on = 2 per branch)
def sig_T(T, shift):                                              # forward model sigma^{X+}(w;T) = sum (n+1) A(w - w_nu + shift) + n A(w + w_nu + shift)
    return (nB(wTA, T)+1)*A_true(w-wTA+shift) + nB(wTA, T)*A_true(w+wTA+shift)
s77 = sig_T(77, dEg); s0 = sig_T(1e-3, 0.0)
rel = lambda x: np.interp(Eg0+wTA+x, w, s77)/np.interp(Eg0+wTA+x, w, s0)
# exact inverse transfer: solve sigma(w;77K) = (n+1)A(w-wTA+d) + n A(w+wTA+d) for A on the grid (least squares), then forward to mK
dw = w[1]-w[0]; nb = nB(wTA, 77); sh1 = int(round((-wTA+dEg)/dw)); sh2 = int(round((wTA+dEg)/dw))
Mtx = np.zeros((len(w), len(w)))
for i in range(len(w)):
    for sh, c in ((sh1, nb+1), (sh2, nb)):
        if 0 <= i+sh < len(w): Mtx[i, i+sh] += c
Ainv = np.linalg.lstsq(Mtx, s77, rcond=None)[0]; s0rec = np.array([Ainv[i-int(round(wTA/dw))] if i-int(round(wTA/dw)) >= 0 else 0 for i in range(len(w))])
inner = (w > Eg0+wTA+0.005) & (w < 1.30)
check("CW1-C24", rel(0.015) > 2 and rel(0.025) < 2 and 1.3 < rel(0.05) < 1.6 and np.max(np.abs(s0rec[inner]/s0[inner]-1)) < 1e-3,
      f"uncorrected 77 K data / mK truth: {rel(0.015):.2f} (15 meV above E_g+w_TA), {rel(0.025):.2f} (25), {rel(0.05):.2f} (50), {rel(0.1):.2f} (100 meV); exact inverse transfer recovers the mK spectrum")

# ---------------- LE-179: rotations ----------------
k1, k2, k3, w12, w13, w23 = sp.symbols("k1 k2 k3 w12 w13 w23", real=True)
mx, my, mz = sp.symbols("m_x m_y m_z", positive=True)
eps = k1**2/(2*mx) + k2**2/(2*my) + k3**2/(2*mz); kv = sp.Matrix([k1, k2, k3]); Wr = sp.Matrix([[0, w12, w13], [-w12, 0, w23], [-w13, -w23, 0]])
d_eps = (sp.Matrix([[sp.diff(eps, v) for v in (k1, k2, k3)]])*(Wr*kv))[0]
check("CW1-C25", sp.simplify(d_eps.subs({k1: 0, k2: 0, k3: 0})) == 0 and sp.simplify(d_eps.subs({mx: 1, my: 1, mz: 1})) == 0,
      "rigid rotation shifts eps_n(k) by v.(omega k): zero at extrema (v = 0) and for isotropic bands -> antisymmetric D^n has no effect at band edges")
Xi_u, cLA = 8.6, 8.18/299792.458
check("CW1-C26", 300 < Xi_u/cLA/1e3 < 330, f"D/c_LA = {Xi_u/cLA/1e3:.0f} keV >> q <= 2 keV (Xi_u = 8.6 eV [UNVERIFIED], c_LA[100] = 8.18 km/s [CALC, COMP-PH], as in the CW1 text)")

# ---------------- LE-44: ALDA kernel ----------------
nn, Cx = sp.symbols("n C_x", positive=True)
ex = -Cx*nn**sp.Rational(4, 3)
check("CW1-C27", sp.simplify(sp.diff(ex, nn, 3) - sp.Rational(8, 27)*Cx*nn**sp.Rational(-5, 3)) == 0,
      "k_xc = d^3 E_x/dn^3 = (8/27) C_x n^(-5/3) (LDA exchange), positive")
# relative size of the ALDA cross term to the Hartree pair term at P: |k_xc dn_q dn_Q| / |f_H dn2| ~ (P/2k_F)^2 x (dn/n): bound 0.1 x 0.1
check("CW1-C28", abs((1.0/(2*3.57/1.97327))**2-0.0764) < 1e-3, f"[arithmetic] (|P|/2k_F)^2 = {(1.0/(2*3.57/1.97327))**2:.4f} with |P| = 1 1/A, k_F = 3.57 keV")

# ---------------- LE-47: GaAs C8 parabolic scan ----------------
def mzp(E, Q0, Mx_, qmin=0.0):
    qs = np.linspace(max(qmin, 1), 8000, 80001)
    den = qs*vmax - (E + (qs-Q0)**2/(2*Mx_*me)); ok = den > 0
    return (qs[ok]**2/(2*den[ok])).min()/1e6 if ok.any() else np.inf
aG = 5.653; K_L = np.sqrt(3)*np.pi/aG*A2eV; K_X = 2*np.pi/aG*A2eV; G111 = 2*np.sqrt(3)*np.pi/aG*A2eV
m_PA = 2*(1.519+0.008)/vmax**2/1e6
m_G = mzp(1.519, 0.0, 0.067+0.51); m_L = mzp(1.71, K_L, 1.9+0.51); m_X = mzp(1.981, K_X, 1.3+0.51); m_U = mzp(1.519, G111, 0.067+0.51)
check("CW1-C29", m_G == np.inf and 0.42 < m_PA < 0.45 and m_L < m_X and 0.75 < m_U < 0.9,
      f"GaAs parabolic [E]: PAER edge {m_PA:.3f}; ZPL Gamma(q~0) unreachable; L {m_L:.3f}; X {m_X:.3f}; Umklapp G111 {m_U:.3f} MeV -> PAER-only band {m_PA:.2f}-{min(m_L,m_X,m_U):.2f}")

# ---------------- LE-178: non-adiabatic intraband optical term ~ sqrt(w0) ----------------
mband, w0, Qc = 0.3*me, 0.062, 5000.0
def dz(w):
    f = lambda Q: Q**2*(1/(Q**2/(2*mband)) - 1/(Q**2/(2*mband)+w))
    return integrate.quad(f, 0, Qc, limit=400)[0]
an = lambda w: (2*mband)**1.5*np.sqrt(w)*np.pi/2
check("CW1-C30", abs(dz(w0)/an(w0)-1) < 0.05 and abs(dz(w0/4)/dz(w0)-0.5) < 0.03,
      f"int d^3Q [1/e_Q - 1/(e_Q + w0)] = (pi/2)(2m)^(3/2) sqrt(w0) [1 + O(sqrt(w0/E_c))]: ratio {dz(w0)/an(w0):.3f}")

# ---------------- LE-40/42: coherent-potential limit of (2.2) (exact scalar identity) ----------------
chi0, v, Um = sp.symbols("chi0 v U")
eps_ = 1 - v*chi0
Mt = Um*1 + 1*(v/eps_)*(Um*chi0)          # M + rho W T with T = U chi0, W = v/eps, rho = 1
check("CW1-C31", sp.simplify(Mt - Um/eps_) == 0, "X2 (2.2) with M_f' = U rho_f' for all f': M~ = M/eps(P) exactly (input to the X2-N1 benchmark)")

# ---------------- LE-43: Kubo vertex rung (CW1.20) ----------------
a_s, b_s, w_s, fm, fmp = sp.symbols("a b omega f_m f_mp")
Fk = ((1-fm)/(a_s-w_s) + fm/(a_s+w_s) - (1-fmp)/(b_s-w_s) - fmp/(b_s+w_s))/(b_s-a_s)
dF = (fm*(1/(a_s+w_s)-1/(a_s-w_s)) - fmp*(1/(b_s+w_s)-1/(b_s-w_s)))/(b_s-a_s)
check("CW1-C32", sp.simplify(Fk.subs({fm: 0, fmp: 0}) - 1/((a_s-w_s)*(b_s-w_s))) == 0 and sp.simplify(Fk - Fk.subs({fm: 0, fmp: 0}) - dF) == 0
      and sp.limit(dF, w_s, 0) == 0 and sp.simplify(dF.subs({fm: 0, fmp: 1, b_s: w_s/2})) != 0,
      "(CW1.20): f = 0 gives the one-electron RS product; Delta F -> 0 as w_Q -> 0 at fixed a, b, but is finite for |b| ~ w_Q with an occupied m'")

# =============================== ERR-CW1 additions (returns/R16/CW1-errata.md) ===============================
QF, Q2S = O("errata_qe.json"), O("errata_qe_it2_S12.json")["S12"]; ER = O("errata_ratio.json")
# E-1 (V2, V3, OC-1...OC-9): SOC shift of the Si ZPL edge, pseudo-consistent, and the DFT re-minimisation
d12, dav = QF["SOC_minus_S12_meV"], QF["SOC_minus_FRav_meV"]
check("CW1-C33", abs(d12["center"]-dav["center"]) < 0.5 and 14.5 < dav["center"] < 16.5 and abs(dav["axis"]) < 1.5 and abs(d12["axis"]) < 1.5,
      f"[regenerated] SOC shift of the scissored pair energy at the mirror-plane optimum: +{dav['center']:.2f} meV vs FR-1.1 j-averaged (same pseudo family), +{d12['center']:.2f} vs PBE-1.2; "
      f"on-axis 1.39 keV pair +{dav['axis']:.2f} / +{d12['axis']:.2f} meV (VER-CW1: +15.6 / +0.9)")
check("CW1-C34", QS["step_max"] < 1e-3 and Q2S["step_max"] < 1e-3 and abs(QS["m_reminimised"]-QS["m_center"]) < 1e-4 and abs(Q2S["m_reminimised"]-Q2S["m_center"]) < 1e-4
      and abs(QS["m_center"]-0.4072) < 2e-4 and abs(Q2S["m_center"]-0.4042) < 2e-4 and abs(QS["m_center"]-Q2S["m_center"]-0.0030) < 2e-4 and QS["m_center"] + 0.002 < 0.4150,
      f"[regenerated] (CW1.1) re-minimised on DFT bands (a_exp, two Newton steps on 3^3 stencils, h = 0.02): scalar {QF['S12']['m_center']:.4f} -> {Q2S['m_center']:.4f}, "
      f"SOC {QF['SOC']['m_center']:.4f} -> {QS['m_center']:.4f} MeV (last step {QS['step_max']:.1e}); SOC shift +{QS['m_center']-Q2S['m_center']:.4f} MeV; off axis still below the on-axis 0.4150(+0.0002)")
check("CW1-C35", 1/QS["hole_inv_mass_eig"][0] > 1.6 and 1/Q2S["hole_inv_mass_eig"][0] > 1.6 and abs(QS["hole_inv_mass_eig"][0]/Q2S["hole_inv_mass_eig"][0]-1) < 0.1,
      f"[regenerated] Rebuttal R-2: hole mass tensor at the optimum, flat direction m = {1/QS['hole_inv_mass_eig'][0]:.2f} m_e with SOC, {1/Q2S['hole_inv_mass_eig'][0]:.2f} m_e scalar (not 0.57 m_e)")
# E-6 (V10, V11, §2 (CW1.4)): cone geometry, relaxed-pair vertex, second heavy hole
xs, th_, bth, bzz = sp.symbols("x vartheta beta_theta beta_z", positive=True)
fdiag = bth*(xs-th_)**2 + bzz*xs**2; xmin = sp.solve(sp.diff(fdiag, xs), xs)[0]
et_sym = sp.simplify(fdiag.subs(xs, xmin)); et = float(et_sym.subs({th_: F["theta_rad"], bth: a_, bzz: b_}))
fc_ = ER["first_channel"]
check("CW1-C36", sp.simplify(et_sym - th_**2*bth*bzz/(bth+bzz)) == 0 and abs(et-ER["eps_touch"]) < 1e-9 and abs(et-0.0486) < 5e-4 and et < a_*F["theta_rad"]**2
      and all(abs(r["grid_indep_gfix"]/r["closed_gfix"]-1) < 3e-3 for r in fc_[1:]) and all(abs(r["mincones_gfix"]/r["grid_indep_gfix"]-1) < 3e-3 for r in fc_[:3])
      and fc_[4]["mincones_gfix"] < 0.8*fc_[4]["grid_indep_gfix"],
      f"Rebuttal R-3: adjacent {{001}} cones touch at eps = theta^2 b_th b_z/(b_th+b_z) = {et:.4f} eV (< b_th theta^2 = {a_*F['theta_rad']**2:.3f}); grid = closed form; min-of-cones = independent sum below it, "
      f"{fc_[4]['mincones_gfix']:.3f} vs {fc_[4]['grid_indep_gfix']:.3f} at 0.1 eV, {fc_[5]['mincones_gfix']:.3f} vs {fc_[5]['grid_indep_gfix']:.3f} at 0.2 eV")
check("CW1-C37", abs(ER["midpoint"]["E_true_minus_E0"]/ER["midpoint"]["model"]-1) < 0.05,
      f"min-of-cones model at the midpoint between adjacent cones: {ER['midpoint']['model']*1e3:.1f} meV vs Wannier E_min {ER['midpoint']['E_true_minus_E0']*1e3:.1f} meV above E_0")
me_, mh_, qz, ke_ = sp.symbols("m_e m_h q k_e", positive=True)
kstar = sp.solve(sp.diff(ke_**2/(2*me_) + (ke_-qz)**2/(2*mh_), ke_), ke_)[0]
check("CW1-C38", sp.simplify(kstar - qz*me_/(me_+mh_)) == 0 and 0.67 < VE["bias_rel"] < 1.40 and abs(VE["bias_rel"]-1.30) < 0.03 and abs(Q2S["vertex"]["bias_rel"]-1.30) < 0.03 and VE["cos_ab"] < -0.98,
      f"relaxed pair: k_e* = q m_e/(m_e+m_h) (sympy); d_qz rho|rel = {VE['g_rel_A']:.3f} A vs d_qz at fixed k_v {VE['dqz_A']:.3f}: |rho|^2 x{VE['bias_rel']:.2f} (re-minimised point x{Q2S['vertex']['bias_rel']:.2f}; VER band 0.67-1.40); "
      f"m_zz = {VE['f_e']:.3f} fraction to the electron (m_zz^h = {QF['S12']['hole_mzz']:.3f}, m_zz^e = {QF['S12']['elec_mzz']:.3f})")
SB = ER["second_band"]; IM = {r["m"]: r for r in ER["in_m"]}
check("CW1-C39", abs(SB["m_axis_wannier"]-0.4150) < 2e-4 and all(abs(b1/b2-1) < 0.02 for b1, b2 in zip(SB["beta2_002"], SB["beta2_004"])) and max(SB["beta2_002"])/min(SB["beta2_002"]) > 3
      and IM[0.42]["total_central"] < 1 < IM[0.43]["total_central"] and IM[0.42]["total_low"] < 1 < IM[0.43]["total_low"] and IM[0.415]["ratio2_low"] == 0 and IM[0.43]["ratio2_central"] > IM[0.43]["ratio1"],
      f"second (mirror-even) heavy hole: on-axis edge {SB['m_axis_wannier']:.4f} MeV (Wannier), beta^ZP_2 = {SB['beta2_002'][0]:.2f}/{SB['beta2_002'][1]:.2f}/{SB['beta2_002'][2]:.2f} eV/rad^2 at azimuth 0/pi8/pi4 (quadratic); "
      f"ZPL/PAER at eps_max(m): 0.42 MeV {IM[0.42]['total_central']:.2f} ({IM[0.42]['total_low']:.2f}), 0.43 {IM[0.43]['total_central']:.2f} ({IM[0.43]['total_low']:.2f}), 0.44 {IM[0.44]['total_central']:.2f} -> crossover 0.42-0.43 MeV")
check("CW1-C40", abs(fc_[1]["mincones_grel"]-0.020) < 0.001 and abs(fc_[3]["mincones_grel"]-0.164) < 0.003 and abs(fc_[4]["mincones_grel"]-0.343) < 0.005 and abs(fc_[5]["mincones_grel"]-0.584) < 0.01,
      f"[record of errata_ratio.json for the E-6 table] varpi_II (min-of-cones, d_qz rho|rel, a_exp SOC edge) = {fc_[1]['mincones_grel']:.3f}/{fc_[3]['mincones_grel']:.3f}/{fc_[4]['mincones_grel']:.3f}/{fc_[5]['mincones_grel']:.3f} at 14.7/50/100/200 meV")
# E-5 (V8): X-face c1 vs c1+c2
XF = {(r["eps"], r["point"], r["vertex"]): r["ratio"] for r in ER["Xface"]}; XS = O("errata_xface_soc.json")
check("CW1-C41", abs(U["xc"]["rho2_c12_top"]/U["xc"]["rho2_c1_top"]-2.93) < 0.03 and abs(XF[(0.001, "xc", "rho2_c1_top")]-2.38) < 0.03 and abs(XF[(0.001, "xc", "rho2_c12_top")]-6.96) < 0.05
      and abs(U["xc"]["Ec"][1]-U["xc"]["Ec"][0]-0.050) < 0.001 and abs(XS["FRav"]["c2_c1"]-0.0517) < 1e-3 and 15 < XS["shift_meV"] < 17 and abs(XS["m_SOC"]-0.5027) < 3e-4,
      f"X-face opening: c2 - c1 = {1e3*(U['xc']['Ec'][1]-U['xc']['Ec'][0]):.0f} meV at the computed point; (c1+c2)/c1 = {U['xc']['rho2_c12_top']/U['xc']['rho2_c1_top']:.2f}; ZPL/PAER at 1 meV {XF[(0.001,'xc','rho2_c1_top')]:.2f} (c1) to {XF[(0.001,'xc','rho2_c12_top')]:.2f} (c1+c2), at 0.1 eV {XF[(0.1,'xc','rho2_c1_top')]:.2f}-{XF[(0.1,'xc','rho2_c12_top')]:.2f}; [regenerated] SOC shift of this pair +{XS['shift_meV']:.1f} meV, m {XS['m_FRav']:.4f} -> {XS['m_SOC']:.4f} MeV (a_exp, not re-minimised)")
# E-8 (V19, OC-11): L3 Cauchy-Schwarz interval
r_, vT, Snn = sp.symbols("r v_T S_nn", positive=True)
lo = sp.simplify((vT*sp.sqrt(Snn) - sp.sqrt(r_*vT**2*Snn))**2/(vT**2*Snn)); hi = sp.simplify((vT*sp.sqrt(Snn) + sp.sqrt(r_*vT**2*Snn))**2/(vT**2*Snn))
cs = lambda rv: ((np.sqrt(rv)-1)**2, (np.sqrt(rv)+1)**2)
check("CW1-C42", sp.simplify(lo - (1-sp.sqrt(r_))**2) == 0 and sp.simplify(hi - (1+sp.sqrt(r_))**2) == 0 and abs(cs(20)[0]-12.06) < 0.01 and abs(cs(30)[1]-41.95) < 0.01,
      f"Cauchy-Schwarz: true/their 𝒪8 rate in [(sqrt r - 1)^2, (sqrt r + 1)^2]: r = 20-30 (IP) -> {cs(20)[0]:.1f}-{cs(30)[1]:.1f}; r x 2-9 in medium -> {cs(40)[0]:.0f}-{cs(270)[1]:.0f}; "
      f"the 0.7/1.3 'δ_LF' composition (8-39) is withdrawn")
# E-9 (V14): resonant-only vs retarded TDA vs full coupling, one oscillator
w, E0s, D, Kk_ = sp.symbols("omega E_0 Delta K", positive=True)
res_only = 1/(E0s - w); retarded = 1/(E0s - w) + 1/(E0s + w)
chi_full = 2*D/(w**2 - D*(D + 2*Kk_)); chi_tda = 2*(D + Kk_)/(w**2 - (D + Kk_)**2)
check("CW1-C43", sp.simplify(res_only/retarded - (E0s + w)/(2*E0s)) == 0 and sp.simplify(chi_tda.subs(w, 0)/chi_full.subs(w, 0) - (D + 2*Kk_)/(D + Kk_)) == 0
      and sp.simplify(sp.sqrt(D*(D + 2*Kk_)).series(Kk_, 0, 2).removeO() - (D + Kk_)) == 0,
      "(CW1.5) is the resonant-only error (E0+w)/2E0; retarded TDA vs full coupling (2-level, exchange K): static chi ratio (Delta+2K)/(Delta+K) = 1 + O(K/Delta), pole shift O(K^2/Delta)")
# E-11 (LE-39): Lebedev degree
from scipy.integrate import lebedev_rule
def leb(order, f): x, wts = lebedev_rule(order); return np.sum(wts*f(*x))/np.sum(wts)
c110, c230 = len(lebedev_rule(17)[1]), len(lebedev_rule(25)[1])
check("CW1-C44", c110 == 110 and c230 == 230 and abs(leb(17, lambda x, y, z: x**16) - 1/17) < 1e-12 and abs(leb(17, lambda x, y, z: x**18) - 1/19) > 1e-8
      and abs(leb(25, lambda x, y, z: x**18) - 1/19) < 1e-12,
      f"Lebedev {c110} points: exact to degree 17 (x^16 exact, x^18 error {abs(leb(17, lambda x,y,z: x**18)-1/19):.1e}); {c230} points exact on x^18: K8 x S needs S free of l >= 10")
# E-12 (LE-41): Route S cubic supercell q meshes
a_A = 5.431; qn_ = lambda n: sorted({round(float(np.sqrt(i*i+j*j+k*k)*2*np.pi/(n*a_A)*1.97327), 2) for i in range(5) for j in range(5) for k in range(5)})[:6]
check("CW1-C45", qn_(3)[:5] == [0.0, 0.76, 1.08, 1.32, 1.52] and 1.14 in qn_(4) and 1.14 in qn_(2) and 1.16 not in qn_(3) and not (set(qn_(3)[1:]) & set(qn_(4)[1:])),
      f"cubic n x n x n meshes |q| (keV): n=2 {qn_(2)[:3]}, n=3 {qn_(3)[:5]}, n=4 {qn_(4)[:5]}: n = 2 and 4 share 1.14 keV; n = 3 and 4 share no non-zero q below 2.28 keV")
# E-4 (V5): Luttinger warping Si vs Ge [E, memory values: Si 4.285/0.339/1.446, Ge 13.38/4.24/5.69]
Lu = dict(Si=(4.285, 0.339, 1.446), Ge=(13.38, 4.24, 5.69)); wrp = {k: (g3-g2)/g1 for k, (g1, g2, g3) in Lu.items()}; an = {k: (g1-2*g2)/(g1-2*g3) for k, (g1, g2, g3) in Lu.items()}
check("CW1-C46", wrp["Si"] > 2*wrp["Ge"] and abs(an["Si"]-2.60) < 0.05 and abs(an["Ge"]-2.45) < 0.05,
      f"warping (g3-g2)/g1: Si {wrp['Si']:.2f}, Ge {wrp['Ge']:.2f}; m_hh[111]/m_hh[100]: Si {an['Si']:.2f}, Ge {an['Ge']:.2f} (Ge less warped; its [111] valley axis is already the heavy direction)")
# E-10 (V29): Delta ZPR order estimate
Om = 0.25*5.431**3/1973.27**3; Mc = 2*28.0855*931.494e6; wo = 0.0642
dzpr = lambda mstar, lfac, D0=5.0: Om*(D0*lfac*np.sqrt(1/(2*Mc*wo))*1973.27)**2*(2*mstar*me)**1.5*np.sqrt(wo)/(4*np.pi)
zr = [dzpr(ms, lf) for ms in (0.3, 0.5) for lf in (1, np.sqrt(2))]
check("CW1-C47", 1e-4 < min(zr) and max(zr) < 2e-3, f"Delta ZPR = Omega |g0|^2 (2m*)^(3/2) sqrt(w0)/4pi, D0 = 5 eV/A: {min(zr)*1e3:.2f}-{max(zr)*1e3:.2f} meV for m* = 0.3-0.5, l0 x 1-sqrt2 -> '<= 2 meV [E]'")
# E-7 (§2 convention): glide {sigma_z | t_d}
a_s_ = sp.symbols("a", positive=True); td = sp.Matrix([1, 1, 1])*a_s_/4; sz = sp.diag(1, 1, -1); T = sz*td + td
Gp = sp.Matrix([-2, 0, 0])*2*sp.pi/a_s_
check("CW1-C48", T == sp.Matrix([a_s_/2, a_s_/2, 0]) and sp.simplify(sp.exp(-sp.I*(Gp.T*T)[0]/2)) == -1 and sp.simplify(sp.exp(-sp.I*(Gp.T*td)[0])) == -1,
      "{sigma_z|t_d}^2 = {E|T}, T = (a/2, a/2, 0): eigenvalues varsigma e^{-ik.T/2}; k -> k + (2bar00) flips the label (e^{-iG.T/2} = -1) and the operator phase e^{-iG'.t_d} = -1")
# E-13 (V13, OC-6) and E-12 (V21, OC-7)
lift = SM["top_pair_over2"]/SM["second_pair_over2"]
check("CW1-C49", abs(lift-2.0e-3) < 1e-4 and abs(np.sqrt(SX["quartet_over2"]/0.150)-0.0049) < 2e-4,
      f"mirror-optimum SOC lift relative to the allowed partner: {lift:.2e} (amplitude {np.sqrt(lift)*100:.1f}%); on-axis Gamma_8 quartet amplitude vs 0.150: {np.sqrt(SX['quartet_over2']/0.150)*100:.2f}%")
# E-2 (V32, IF-CW1-3): the q* = 0.90 keV pair
qq = QF["qstar"]
check("CW1-C50", abs(dav["qstar"]-d12["qstar"]) < 0.5 and 15 < dav["qstar"] < 17 and abs(qq["E_SOC"]-1.727) < 0.002 and abs(qq["E_wannier_aPBE"]-O("emin_qstar.json")["0.9"]["Emin"]) < 1e-6,
      f"[regenerated] q* = 0.90 keV pair: Wannier a_PBE {qq['E_wannier_aPBE']:.4f}, DFT a_exp {qq['E_S12']:.4f}, +SOC {qq['E_SOC']:.4f} eV (shift +{dav['qstar']:.1f} meV); not re-minimised")
# §5 (smaller points): eps_ex,max at q_opt underestimates the reachable excess energy at fixed m
emax_q = {kk: max((float(kk.split('_')[0])*1e3*vmax - (float(kk.split('_')[0])*1e3)**2/(2*0.42e6) - min(r[1] for r in rows)) for _ in [0]) for kk, rows in F["scan"].items() if kk.endswith("001")}
check("CW1-C51", max(emax_q.values()) >= emx(0.42) - 1e-3, f"eps_ex,max at 0.42 MeV over the scanned |q| (1.20-1.48 keV, {{001}} minima): max {max(emax_q.values()):.3f} vs {emx(0.42):.3f} eV at |q|_opt (Wannier): q_opt value is a lower estimate")
check("CW1-C52", abs(np.linalg.norm(F["k_v"]) - 0.1654) < 1e-3 and abs(QF["S12"]["Ev_minus_vbm"]+0.0616) < 5e-4 and abs(QF["SOC"]["Ev_minus_vbm"]+0.0771) < 5e-4,
      f"hole at |k_v| = {np.linalg.norm(F['k_v']):.4f} 2pi/a, {-QF['S12']['Ev_minus_vbm']*1e3:.1f} meV below the VBM (scalar), {-QF['SOC']['Ev_minus_vbm']*1e3:.1f} meV below Gamma_8 (SOC) > Delta_SO/3")

npass = sum(r[1] for r in RES); print(f"\n{npass}/{len(RES)} PASS")
sys.exit(0 if npass == len(RES) else 1)
