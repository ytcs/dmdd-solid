"""CRDM flux from 2401.11971 Eqs. (1)-(3) with the Boschini et al. 1801.04059 Eq. (LIS) parametrisation. GeV units unless noted."""
import numpy as np
ME=0.51099895e-3; ALPHA=1/137.035999; Q0=ALPHA*ME
KPC=3.0857e21 # cm
def F_LIS(T):
    """(m^2 s sr GeV)^-1 , T in GeV, stated range 2 MeV - 90 GeV (second branch extended above 90 GeV)."""
    T=np.asarray(T,float)
    lo=1.181e11*T**-12.061/(1+4.307e8*T**-9.269+3.125e8*T**-10.697)
    hi=995.598*T**-3.505+4.423*T**-2.620
    return np.where(T<6.88,lo,hi)
def dPhiLIS(T): return 4*np.pi*F_LIS(T)*1e-4   # cm^-2 s^-1 GeV^-1
def Temin(Tx,m):
    Tx=np.asarray(Tx,float)
    r=np.sqrt(1+2*Tx/m*(m+ME)**2/np.maximum((2*ME-Tx)**2,1e-300))
    return np.where(Tx>2*ME,(Tx/2-ME)*(1+r),(Tx/2-ME)*(1-r))
def FDM2(q2,med):
    return (Q0**2/q2)**2 if med=='light' else 1+0*q2
def dsig(Tx,Te,m,med,sig=1.):
    mu=m*ME/(m+ME)
    return sig*FDM2(2*m*Tx,med)/(4*mu**2*(2*ME*Te+Te**2))*(m*Tx**2+2*m*(ME+Te)**2-Tx*(ME+m)**2-2*m*Tx*Te)
def flux(Tx,m,med,sig=1e-34,rho=0.4,Deff=8.02*KPC,nT=800,Temax=1e4):
    Tx=np.atleast_1d(Tx).astype(float); out=np.zeros_like(Tx)
    for i,t in enumerate(Tx):
        t0=max(float(Temin(t,m)),1e-9)
        lt=np.linspace(np.log(t0),np.log(Temax),nT); Te=np.exp(lt)
        f=np.maximum(dsig(t,Te,m,med,sig),0)*dPhiLIS(Te)*Te
        out[i]=np.trapezoid(f,lt) if hasattr(np,'trapezoid') else np.trapz(f,lt)
    return Deff*rho/m*out
