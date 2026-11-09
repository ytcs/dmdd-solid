"""Read eigenvalues (eV) and k (2pi/a) from a QE save dir XML."""
import numpy as np, xml.etree.ElementTree as ET, sys, json
def read(d):
    r=ET.parse(f'{d}/data-file-schema.xml').getroot()
    ks=[];E=[]
    for k in r.iter('ks_energies'):
        ks.append([float(x) for x in k.find('k_point').text.split()]); E.append(np.array(k.find('eigenvalues').text.split(),float)*27.211386)
    return np.array(ks),np.array(E)
