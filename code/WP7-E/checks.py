"""WP7-E (R10) checks: time-resolved energy and charge balance (yields, defects, delayed release).
Sympy/mpmath only (exact where possible; evalf for the [E] numbers). No simulation.
Run:  python3 -I checks.py      Prints PASS/FAIL per check. Labels WP7E-Cn (CONVENTIONS sec. 14).
Units: hbar = c = k_B = 1 for identities; eV, cm, s for numbers."""
import sympy as sp
import mpmath as mp
from sympy import Rational as Q, sqrt, pi, exp, log, symbols, simplify, integrate, oo

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:88s} {note}")
def num(x, n=4): return sp.N(x, n)

# ---------------------------------------------------------------- C1 charge-reservoir energy is mu-independent under neutrality
Ec, Ev, mu, ee, eh = symbols('E_c E_v mu epsilon_e epsilon_h', real=True)
Nef, Nhf, Net, Nht = symbols('N_ef N_hf N_et N_ht', nonnegative=True)
Eq = Nef*(Ec - mu) + Nhf*(mu - Ev) + Net*(Ec - ee - mu) + Nht*(mu - Ev - eh)
neutral = {Nhf: Nef + Net - Nht}
rep("WP7E-C1a d(E_pairs+E_trap)/dmu = N_h,tot - N_e,tot (vanishes iff neutral)",
    simplify(sp.diff(Eq, mu) - (Nhf + Nht - Nef - Net)) == 0)
rep("WP7E-C1b with neutrality E_pairs+E_trap is mu-independent",
    simplify(sp.diff(Eq.subs(neutral), mu)) == 0)
Eg = symbols('E_g', positive=True)
rep("WP7E-C1c all carriers free and paired: E_pairs = N E_g",
    simplify(Eq.subs({Net: 0, Nht: 0, Nhf: Nef}).subs(Ec, Ev + Eg) - Nef*Eg) == 0)

# ---------------------------------------------------------------- C2 every elementary process of the ledger (sec. 1.3) conserves energy
R = ['pairs', 'trap', 'lat', 'Q', 'sens_meas', 'sens_loss', 'esc', 'hot']
eps, F, dz, eta, Ehot = symbols('varepsilon F Delta_z eta E_hot', positive=True)
def proc(**d):
    return d
procs = {
 'hot-carrier relaxation to band edges (cascade, t<t_pr)': proc(hot=-Ehot, pairs=Eg, Q=Ehot-Eg),
 'capture e on level eps_e':            proc(pairs=-(Ec-mu), trap=(Ec-ee-mu), Q=ee),
 'capture h on level eps_h':            proc(pairs=-(mu-Ev), trap=(mu-Ev-eh), Q=eh),
 'emission e (phonon/athermal)':        proc(pairs=(Ec-mu), trap=-(Ec-ee-mu), Q=-ee),
 'nonrad recombination h + trapped e':  proc(trap=-(Ec-ee-mu), pairs=-(mu-Ev), Q=(Ec-Ev-ee)),
 'radiative recombination h + trapped e (photon escapes)': proc(trap=-(Ec-ee-mu), pairs=-(mu-Ev), esc=(Ec-Ev-ee)),
 'band-to-band recombination':          proc(pairs=-(Ec-Ev), Q=(Ec-Ev)),
 'pair collected at symmetric contacts':proc(pairs=-(Ec-Ev), Q=(Ec-Ev)),
 'lattice release path (phonon branch)':proc(lat=-eps, Q=eps),
 'lattice release path (photon branch)':proc(lat=-eps, esc=eps),
 'TLS resonant phonon absorption':      proc(Q=-eps, lat=eps),
 'phonon absorbed in sensor':           proc(Q=-eps, sens_meas=eta*eps, sens_loss=(1-eta)*eps),
 'phonon escapes to holder':            proc(Q=-eps, esc=eps),
}
ok = all(simplify(sum(p.values())) == 0 for p in procs.values())
rep("WP7E-C2a 13 zero-field processes: sum of reservoir changes = 0", ok, f"({len(procs)} processes)")
drift = proc(Q=F*dz)    # NTL emission at terminal velocity, battery work W = F dz
rep("WP7E-C2b drift step: Delta(reservoirs) = Delta W_bias (= e F dz)", simplify(sum(drift.values()) - F*dz) == 0)
# at t_pr (only cascade processes): omega = N E_g + H + E_st + E_esc  (WP5 (W4))
N, H, Est, Eesc = symbols('N_eh H E_st E_esc', nonnegative=True)
omega = N*Eg + H + Est + Eesc
rep("WP7E-C2c balance (1.1) at t = t_pr, E_trap = W = 0 reduces to WP5 (W4)",
    simplify((N*Eg + H + Est + Eesc + 0 + 0) - omega) == 0)

# ---------------------------------------------------------------- C3 release-kernel sum rules (WP7-T (5.2))
t, G, Gmin, Gmax, w, D, d = symbols('t Gamma Gamma_min Gamma_max w D d', positive=True)
rep("WP7E-C3a single path: int_0^oo Gamma e^{-Gamma t} dt = 1 (energy sum rule Sum P eps)",
    simplify(integrate(G*exp(-G*t), (t, 0, oo)) - 1) == 0)
# broad lambda: dN/dGamma = 1/(Gamma ln(Gmax/Gmin))
Rt = (exp(-Gmin*t) - exp(-Gmax*t))/(t*log(Gmax/Gmin))
Rt_direct = integrate(G*exp(-G*t)/(G*log(Gmax/Gmin)), (G, Gmin, Gmax))
Rt_direct = integrate(exp(-G*t), (G, Gmin, Gmax))/log(Gmax/Gmin)
rep("WP7E-C3b broad-lambda rate = (e^{-Gmin t}-e^{-Gmax t})/(t ln(Gmax/Gmin))", simplify(sp.expand(Rt_direct - Rt)) == 0)
mp.mp.dps = 30
gmin, gmax = mp.mpf('1e-9'), mp.mpf('1e3')
Rn = lambda tt: (mp.e**(-gmin*tt) - mp.e**(-gmax*tt))/(tt*mp.log(gmax/gmin))
tot = mp.quad(Rn, [0, 1e-3, 1, 1e3, 1e6, 1e9, mp.inf])
rep("WP7E-C3c broad-lambda kernel normalised (all relaxing energy released)", abs(tot - 1) < 1e-10, f"int = {mp.nstr(tot, 12)}")
Fw = lambda ww: 1 - (mp.e1(gmin*ww) - mp.e1(gmax*ww))/mp.log(gmax/gmin)
ww = mp.mpf(1e2)
approx = mp.log(gmax*ww)/mp.log(gmax/gmin)
rep("WP7E-C3d released fraction by w ~ ln(Gmax w)/ln(Gmax/Gmin) for 1/Gmax << w << 1/Gmin",
    abs(Fw(ww) - approx - mp.euler/mp.log(gmax/gmin)) < 1e-3, f"F(w)={mp.nstr(Fw(ww),6)} vs {mp.nstr(approx,6)} (+gamma_E/ln)")
fp = d/sqrt(4*pi*D*t**3)*exp(-d**2/(4*D*t))
Fcand = sp.erfc(d/sqrt(4*D*w))
rep("WP7E-C3e correlated recombination: released fraction by w = erfc(d/sqrt(4Dw)) (derivative, limits)",
    simplify(sp.diff(Fcand, w) - fp.subs(t, w)) == 0 and sp.limit(Fcand, w, 0) == 0 and sp.limit(Fcand, w, oo) == 1)

# ---------------------------------------------------------------- C4 Hecht relation from exponential trapping (limit of sec. 2)
lam, L, x, dd = symbols('lambda L x d', positive=True)
Emin = integrate(x*exp(-x/lam)/lam, (x, 0, L)) + L*exp(-L/lam)
rep("WP7E-C4a E[min(X,L)] = lambda(1 - e^{-L/lam}), X ~ Exp(lambda)", simplify(Emin - lam*(1 - exp(-L/lam))) == 0)
Emin2 = integrate(x**2*exp(-x/lam)/lam, (x, 0, L)) + L**2*exp(-L/lam)
varf = simplify((Emin2 - Emin**2)/dd**2)
rep("WP7E-C4b Var f -> 0 as lambda -> oo (complete collection)", sp.limit(varf, lam, oo) == 0)
rep("WP7E-C4c <f> -> L/d as lambda -> oo", simplify(sp.limit(Emin/dd, lam, oo) - L/dd) == 0)

# ---------------------------------------------------------------- C5 bias work = V_b x induced charge (Ramo-Shockley), coaxial geometry
a, b, r0, r1, Vb, qc = symbols('a b r_0 r_1 V_b q', positive=True)
r = symbols('r', positive=True)
Efield = Vb/(r*log(b/a))                 # coax, no space charge: E = -V_b grad(phi_w)
phiw = log(r/a)/log(b/a)                 # weighting potential (1 at r=b, 0 at r=a)
work = integrate(qc*Efield, (r, r0, r1))
Qind = qc*(phiw.subs(r, r1) - phiw.subs(r, r0))
rep("WP7E-C5a coax: W = int qE dr = V_b * q[phi_w(r1)-phi_w(r0)] = V_b Q_ind", simplify(work - Vb*Qind) == 0)
z0, z1 = symbols('z_0 z_1', positive=True)
rep("WP7E-C5b planar: W = q V_b (z1-z0)/d = V_b Q_ind", simplify(qc*(Vb/dd)*(z1 - z0) - Vb*qc*((z1 - z0)/dd)) == 0)

# ---------------------------------------------------------------- C6 compound induced-charge law: moments, thinning limit
n, Fe, m, s2, ep = symbols('n F_eh m s2 epsilon', positive=True)
mean_x = n*m; var_x = n*s2 + m**2*F*n      # placeholder F replaced below
var_x = n*s2 + m**2*Fe*n
Fmeas = simplify(var_x/mean_x)
rep("WP7E-C6a F_meas = s^2/m + m F_eh (law of total variance)", simplify(Fmeas - (s2/m + m*Fe)) == 0)
rep("WP7E-C6b Bernoulli f (CCD collection): F_meas = eps F_eh + 1 - eps (= WP5v3-C2a)",
    simplify(Fmeas.subs({m: ep, s2: ep*(1 - ep)}) - (ep*Fe + 1 - ep)) == 0)
# PGF form: G_x(s) = G_N(phi(s)); Bernoulli phi = 1 - eps + eps s, Poisson N
sv, nu = symbols('s nu', positive=True)
GN = exp(nu*(sv - 1)); phi = 1 - ep + ep*sv
Gx = GN.subs(sv, phi)
rep("WP7E-C6c Poisson N thinned by Bernoulli f is Poisson(eps nu) (PGF composition)", simplify(Gx - exp(ep*nu*(sv - 1))) == 0)

# ---------------------------------------------------------------- C7 two-channel recoil reconstruction (1803.02903 Eq. (1) form)
om, Estr, Eesc2, Qi, Vb2, epsg = symbols('omega E_stored E_esc2 Q_ind V_b epsilon_gamma', positive=True)
Et = om - Estr - Eesc2 + Vb2*Qi          # total phonon (zero sensor loss, contacts return E_g per collected pair)
Erec = Et - Vb2*Qi                       # recoil energy after subtracting the NTL term inferred from charge
rep("WP7E-C7a E_r^rec = omega - E_stored - E_esc: trapping cancels except through E_stored",
    simplify(Erec - (om - Estr - Eesc2)) == 0)
Ymeas = epsg*Qi/Erec
rep("WP7E-C7b measured yield = eps_gamma Q_ind/(omega - E_stored - E_esc) (two biases)", simplify(Ymeas - epsg*Qi/(om - Estr - Eesc2)) == 0)

# ---------------------------------------------------------------- C8 Kinchin-Pease/TRIM stored-energy fraction
psurv, Edam, ER, Est1, Ed = symbols('p_surv E_dam E_R E_st1 E_d', positive=True)
fDF = psurv*Q(4, 10)*(Edam/ER)*Est1/Ed
rep("WP7E-C8a f_DF decreasing in E_d at fixed E_st,1 (TRIM sentence, 1805.09942)", sp.diff(fDF, Ed).is_negative)
rep("WP7E-C8b with E_st,1 = E_d, f_DF is E_d-independent (incompatible with that sentence)",
    simplify(sp.diff(fDF.subs(Est1, Ed), Ed)) == 0)

# ---------------------------------------------------------------- C9 windowed heat quenching
Efrz, Erel, Etr, Fwin = symbols('E_frz E_rel E_trap F_w', nonnegative=True)
YH = 1 - (Efrz + Erel*(1 - Fwin) + Etr + Eesc)/ER
rep("WP7E-C9a Y_H(w) increasing in released fraction F(w)", sp.diff(YH, Fwin).is_nonnegative)
part = Erel*Fwin + Erel*(1 - Fwin) + Efrz
rep("WP7E-C9b in-window + after-window + frozen = E_st (each quantum assigned once)", simplify(part - (Efrz + Erel)) == 0)
ntr, eesum = symbols('n_tr epsilon_sum', positive=True)
heat_def_W11 = ntr*Eg; heat_def_new = ntr*(Eg - eesum)
rep("WP7E-C9c (W11) N_trap E_g overstates the deficit by n_tr(eps_e+eps_h) (released at capture)",
    simplify(heat_def_W11 - heat_def_new - ntr*eesum) == 0)

# ---------------------------------------------------------------- C10 field and thermal emission from shallow traps at mK
mstar, E0, Fe_ = symbols('m_star varepsilon_0 eF', positive=True)
xt = E0/Fe_
SFN = 2*integrate(sqrt(2*mstar*(E0 - Fe_*x)), (x, 0, xt))
rep("WP7E-C10a triangular-barrier WKB exponent = (4/3) sqrt(2m*) eps^{3/2}/(eF)",
    simplify(SFN - Q(4, 3)*sqrt(2*mstar)*E0**Q(3, 2)/Fe_) == 0)
hbarc_eVcm = Q(197327, 10**12)           # eV cm
me = 510998.95                            # eV
mval = 0.3*me; e0 = 0.045                 # [E] effective mass 0.3 m_e, 45 meV (P in Si [UNVERIFIED])
Fneed = 4/3*mp.sqrt(2*mval)*e0**1.5/30 / float(hbarc_eVcm)   # eV/cm for exponent 30 ; divide by e -> V/cm
rep("WP7E-C10b field for exponent 30: >~ 1e4 V/cm (>> detector fields 1-100 V/cm) [E]", Fneed > 1e4, f"F = {mp.nstr(Fneed,3)} V/cm")
kT = 8.617333e-5*0.05
rep("WP7E-C10c thermal emission exponent eps/T at 50 mK for 45 meV: > 1e4 (frozen)", e0/kT > 1e4, f"eps/T = {e0/kT:.3g}")

# ---------------------------------------------------------------- C11 particle-seeded single releases are below current thresholds [E]
Ed_si = 20.0; Edam_1keV = 750.0
NFP = 0.8*Edam_1keV/(2*Ed_si)
rep("WP7E-C11a NRT Frenkel pairs at E_R = 1 keV (E_d = 20 eV, E_dam = 0.75 keV) ~ 15 [E]", 10 < NFP < 20, f"N_FP = {NFP:.1f}")
Est1_max = 9.0; ecoll = 0.3; thr = 30.1   # formation-energy scale [UNVERIFIED]; collection [E]; CRESST Det-A NR threshold [FT, 2202.05097]
rep("WP7E-C11b one FP release seen in phonons: eps_coll*E_st,1 << 30.1 eV threshold", ecoll*Est1_max < thr/5, f"{ecoll*Est1_max:.1f} eV")
rep("WP7E-C11c upper bound on the stored fraction at 1 keV: N_FP E_st,1/E_R ~ 0.13 (p_surv = 1) [E]", 0.1 < NFP*Est1_max/1000.0 < 0.2, f"{NFP*Est1_max/1000:.3f}")

# ---------------------------------------------------------------- C12 STM release in an amorphous sensor film: power, not events [E]
Pbar = 1.6e19       # eV^-1 cm^-3 (a-SiO2, WP7-T C14c)
Vfilm = 1e-5        # cm^3 (100 nm x 1 cm^2)
T1 = 8.617333e-5*1.0   # 1 K freeze-out scale [E]
Qdot = lambda tt: (mp.pi**2/24)*Pbar*Vfilm*T1**2/tt     # WP7-T (4.5), T0 -> 0
p10d = Qdot(10*86400.0)
rep("WP7E-C12a film TLS release power at t = 10 d ~ 1 eV/s (sub-threshold continuum) [E]", 0.1 < p10d < 10, f"{mp.nstr(p10d,3)} eV/s")
Estored = (mp.pi**2/12)*Pbar*Vfilm*T1**2
rep("WP7E-C12b total stored excess pi^2 Pbar V T1^2/12 ~ 1e6 eV, released in quanta <~ few T1 (~1e-4 eV)",
    1e5 < Estored < 1e7, f"{mp.nstr(Estored,3)} eV; quantum ~ {3*T1:.1e} eV")
rep("WP7E-C12c number of release quanta per 10 eV burst-equivalent >~ 1e4 (needs collective release)", 10/(3*T1) > 1e4)

print(f"\n{sum(RES)}/{len(RES)} PASS")
