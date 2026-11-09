"""Dark-photon absorption reach, 1910.02091 (2.25)-(2.29) and the URF replacement [5.5]."""
import numpy as np, dirac as d, sys
EXPO = d.KG*d.YR
def Gam(p, m, rule, sign=+1):
    """Gamma/eps^2, unpolarised. src: per-component vertex of (2.27); URF: kappa_mix^2 m Im(-1/eps_ii) (WP0-v2 L9b).
    sign=+1: physical eps = kappa + v^2 P (P = -pi, Re P > 0); sign=-1: literal m^2+Pi^{ii} with Pi^{ii}=m^2 v^2 pi/kappa."""
    B = d.Bfun(m*m, p['D'], p['Lt']); P = p['C']*B
    out = 0.
    for i in range(3):
        a = p['v'][i]**2/p['kap'][i]
        if rule == 'src':   out = out + m*a*P.imag/np.abs(1+sign*a*P)**2
        elif rule == 'URF': out = out + m*(p['v'][i]**2*P.imag)/np.abs(p['kap'][i]+sign*p['v'][i]**2*P)**2
        elif rule == 'lead':out = out + m*a*P.imag/p['kap'][i]
    return out/3
def eps_lim(p, m, rule, rho_chi=0.3e9*(1/d.CM)**3, nev=3., sign=+1):
    R = rho_chi/(p['rhoT']*m)*Gam(p, m, rule, sign)        # per (eV^-1 . eV) -> rate per mass
    return np.sqrt(nev/(R*EXPO))
if __name__ == '__main__':
    for n in ['ZrTe5_th','ZrTe5_exp','Yb','BNQ']:
        p = d.setup(n)
        pub = np.loadtxt(f'data/pub_abs_{n}.csv', delimiter=',')
        pub = pub[(pub[:,1] < 1e-14) & (pub[:,0] < 2*p['EL']*.98) & (pub[:,0] > 2*p['D']*1.3)]
        sel = pub[::max(1, len(pub)//300)]
        for sign in (+1, -1):
            y = eps_lim(p, sel[:,0], 'src', sign=sign)
            r = y/sel[:,1]
            print(n, 'sign', sign, 'mean ratio(calc rho=.3/pub)=%.4f  spread min %.4f max %.4f' % (np.exp(np.log(r).mean()), r.min(), r.max()))
