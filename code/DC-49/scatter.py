"""Scattering reach of 1910.02091: event integral N(m_chi) for 3 events/1 kg yr, with screening rules swapped.
Rules: src  1/|1 + P sum_i qhat_i^2 v_i^2/kappa_ii|^2                        (their (3.14), physical sign)
       URF  1/|qhat.kappa.qhat + P sum_i qhat_i^2 v_i^2|^2                    (WP4 [5.2], diagonal kappa)
       URFo as URF with the symmetric off-diagonal part of Table 2 kept
       lead 1/(qhat.kappa.qhat)^2  (WP4 [5.1] leading form: Re and Im delta eps dropped from the denominator)
       bare 1 (no screening; diagnostic)
Rate:  R = (g/rho_T)(rho_chi/m)(sigma/(8 pi mu^2)) Int d^3q Int d omega F^2 |F_med|^2/q W(Qt,omega) gtilde(omega/q+q/2m, psi)
       W = (Qt^2 dm - dm^3/3)/(16 pi^2 Qt vvv),  dm = min(Qt beta, 2 E_L - omega), beta = sqrt(1-4D^2/(omega^2-Qt^2))."""
import numpy as np, dirac as d, sys, json, time
from numpy.polynomial.legendre import leggauss
from scipy.special import erf
HALO = dict(rho=0.3e9/d.CM**3, v0=220*d.KMS, vesc=544*d.KMS, ve=232*d.KMS)   # defaults; see fit_halo.py
ALPHAE = np.deg2rad(42.)
def vE_dir(t):
    """(2.20): unit vector of v_e(t), t in days."""
    b = 2*np.pi*t; s, c = np.sin(ALPHAE), np.cos(ALPHAE)
    return np.array([s*np.sin(b), s*c*(np.cos(b)-1), c*c+s*s*np.cos(b)])
def gtil(w, h):
    """Radon transform of the truncated Maxwellian, w = v_min - v_e cos(psi): exact form of (2.19)."""
    z = h['vesc']/h['v0']; Nesc = erf(z)-2*z*np.exp(-z*z)/np.sqrt(np.pi)
    Nn = 1/(np.pi**1.5*h['v0']**3*Nesc)
    return np.where(np.abs(w) < h['vesc'], 2*Nn*np.pi*h['v0']**2*(np.exp(-w*w/h['v0']**2)-np.exp(-(h['vesc']/h['v0'])**2)), 0.)
def dirs(nth, nph):
    x, w = leggauss(nth); ph = (np.arange(nph)+.5)*2*np.pi/nph
    X, PH = np.meshgrid(x, ph, indexing='ij')
    s = np.sqrt(1-X*X)
    n = np.c_[(s*np.cos(PH)).ravel(), (s*np.sin(PH)).ravel(), X.ravel()]
    wt = (w[:, None]*np.ones(nph)[None, :]*(2*np.pi/nph)).ravel()
    return n, wt
RULES = ['src', 'URF', 'URFo', 'lead', 'bare']
def event_integral(p, m, h=HALO, nth=32, nph=48, nq=48, nw=32, nt=24, fdm='light', Bt=None, nv=400, sign=+1, iso_halo=False, kt=None):
    """returns dict rule -> N(t) array (events per kg yr per unit sigma[cm^2]) on nt phases of the day"""
    Bt = Bt or d.Btab(p)
    mu = m*d.ME/(m+d.ME); vmax = h['vesc']+h['ve']; D = p['D']; EL = p['EL']; C = p['C']
    n, wt = dirs(nth, nph)
    xq, wq = leggauss(nq); xw, ww = leggauss(nw)
    # outer t grid and v_min grid for histogramming
    ts = np.arange(nt)/nt; vE = np.array([vE_dir(t) for t in ts])   # (nt,3)
    vg = np.linspace(0, vmax, nv); dv = vg[1]-vg[0]
    out = {r: np.zeros(nt) for r in RULES}
    qs = np.geomspace(1e-3*D/vmax, 2*m*vmax, 3000)
    for nd, wd in zip(n, wt):
        vt = np.sqrt(np.sum(nd**2*p['v']**2))
        ok = (np.sqrt(vt**2*qs**2+4*D*D)+qs**2/(2*m) < qs*vmax) & (np.sqrt(vt**2*qs**2+4*D*D) < 2*EL)
        if not ok.any(): continue
        ql, qh = qs[ok][0], qs[ok][-1]
        i0 = max(np.argmax(ok)-1, 0); ql = qs[i0]; i1 = min(len(qs)-1, len(qs)-np.argmax(ok[::-1])); qh = qs[i1]
        lq = .5*(np.log(qh/ql))*xq+.5*np.log(qh*ql); q = np.exp(lq); wtq = .5*np.log(qh/ql)*wq*q
        Qt = vt*q
        wmin = np.sqrt(Qt**2+4*D*D); wmax = np.minimum(q*vmax-q*q/(2*m), 2*EL)
        good = wmax > wmin
        q, wtq, Qt, wmin, wmax = q[good], wtq[good], Qt[good], wmin[good], wmax[good]
        if len(q) == 0: continue
        # stretch omega nodes towards wmin (beta ~ sqrt edge)
        u = .5*(xw+1); om = wmin[:, None]+(wmax-wmin)[:, None]*(u**2)[None, :]
        wom = (wmax-wmin)[:, None]*(2*u*.5*ww)[None, :]
        s = om**2-Qt[:, None]**2
        beta = np.sqrt(np.maximum(1-4*D*D/s, 0))
        dm = np.minimum(Qt[:, None]*beta, np.maximum(2*EL-om, 0))
        W = (Qt[:, None]**2*dm-dm**3/3)/(16*np.pi**2*Qt[:, None]*p['vvv'])
        F2 = (d.Q0/q)**4 if fdm == 'light' else np.ones_like(q)
        base = (wtq*q*q*F2/q)[:, None]*wom*W*wd                # d^3q = q^2 dq dOmega
        vmin = om/q[:, None]+q[:, None]/(2*m)
        P = C*Bt(s)*sign
        a = np.sum(nd**2*p['v']**2/p['kap']) if kt is None else vt**2/kt; vt2 = vt**2   # kt: 1708.08929 isotropised kappa-tilde
        if p.get('typo'): a = a+nd[0]**2*(p['v'][2]**2-p['v'][0]**2)/p['kap'][0]         # printed q_x^2 v_F,z^2 of (3.13)-(3.14)
        kd = np.sum(nd**2*p['kap']); ko = nd@p['ksym']@nd
        den = {'src': np.abs(1+a*P)**2, 'URF': np.abs(kd+vt2*P)**2, 'URFo': np.abs(ko+vt2*P)**2,
               'lead': kd**2+0*a*P.real, 'bare': 1+0*a*P.real}
        idx = np.clip(((vmin/dv).astype(int)), 0, nv-2); fr = vmin/dv-idx
        c = ((np.arange(nt)+.5)/nt*2-1) if iso_halo else vE@nd  # (nt,)  iso_halo: mean over cos(psi) (spherically averaged SHM)
        G = gtil(vg[None, :]-h['ve']*c[:, None], h)  # (nt,nv)
        for r in RULES:
            wgt = (base/den[r]).ravel()
            H = np.bincount(idx.ravel(), wgt*(1-fr).ravel(), nv)+np.bincount(idx.ravel()+1, wgt*fr.ravel(), nv)
            out[r] += G@H
    pref = (p['g']/p['rhoT'])*(h['rho']/m)/(8*np.pi*mu**2)*d.KG*d.YR*d.CM**2
    return {r: pref*out[r] for r in RULES}
def mod_amp(Nt):
    """A = (N_max-N_min)/(N_max+N_min) in the two 12 h windows around max and min (section 5.1 of the source)."""
    nt = len(Nt); best = 0
    cs = np.r_[Nt, Nt]
    win = np.array([cs[i:i+nt//2].sum() for i in range(nt)])
    i = np.argmax(win); return (win[i]-(Nt.sum()-win[i]))/Nt.sum()
if __name__ == '__main__':
    t0 = time.time()
    p = d.setup('ZrTe5_th')
    Nt = event_integral(p, 50e3)
    print(time.time()-t0, {r: 3/np.mean(Nt[r]) for r in RULES})
