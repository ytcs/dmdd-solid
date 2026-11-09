"""SHM eta(v_min) per CONVENTIONS §8 (2105.00599): v0=238, vesc=544, vE=250.5 km/s (reference frame), c=1 units."""
import numpy as np
C=299792.458
def make_eta(v0=238.,vesc=544.,vE=250.5,n=4000):
    v=np.linspace(0,(vesc+vE),n)[1:]
    c=np.linspace(-1,1,801)
    V,CC=np.meshgrid(v,c,indexing='ij')
    w=np.exp(-(V**2+vE**2+2*V*vE*CC)/v0**2)*((V**2+vE**2+2*V*vE*CC)<vesc**2)
    F=2*np.pi*V[:,0]**2*np.trapezoid(w,c,axis=1)
    F/=np.trapezoid(F,v)
    # eta(u) = int_u F(v)/v dv  (km/s)^-1 -> convert to c=1
    integ=F/v
    cum=np.concatenate([[0],np.cumsum(0.5*(integ[1:]+integ[:-1])*np.diff(v))])
    eta_tab=(cum[-1]-cum)*C
    vv=v/C
    return lambda u: np.interp(u,vv,eta_tab,right=0.0), (vesc+vE)/C
if __name__=='__main__':
    eta,vmax=make_eta(); print(vmax*C, eta(np.array([0,300/C,600/C])))
