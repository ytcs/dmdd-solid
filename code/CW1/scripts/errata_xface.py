"""ERR-CW1 E-5: SOC shift of the (2bar00)-class X-face edge pair (k_v = (-0.204, 0.167, 0.002), k_e = (-1, 0.028, 0.023) 2pi/a, the CW1 'xv'/'xc' point),
FR-1.1 j-averaged vs FR-1.1 + SOC, a_exp, 40 Ry, each scissored to 1.170 eV against its own gap (inputs/errata/nscf_xface_*.in).  usage: errata_xface.py workdir out.json"""
import sys, json, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from eig import read
W, out = sys.argv[1:3]; R = {}
for v, (iv, ic) in (('FRav', (3, 4)), ('SOC', (7, 8))):
    k, E = read(f'{W}/xf/{v}/si.save'); gap = E[1, ic]-E[0, iv]
    R[v] = dict(gap=float(gap), E=float(E[3, ic]-E[2, iv]+1.170-gap), Ev_vbm=float(E[2, iv]-E[0, iv]), c2_c1=float(E[3, ic+(2 if v == 'SOC' else 1)]-E[3, ic]))
q = np.linalg.norm(k[3]-k[2])*3.7289*2*np.pi/10.2631*1e3; vmax = 794.5/299792.458; m = lambda E: q*q/(2*(q*vmax-E))/1e6
R.update(shift_meV=1e3*(R['SOC']['E']-R['FRav']['E']), q_keV=float(q/1e3), m_FRav=float(m(R['FRav']['E'])), m_SOC=float(m(R['SOC']['E'])))
R['dm'] = R['m_SOC']-R['m_FRav']; json.dump(R, open(out, 'w'), indent=1); print(R)
