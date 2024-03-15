#!/usr/bin/env python

"""
Code which generates a series of fingerprints
defining the structure of the MOF
"""


import os
from sys import argv


script, jobfile = argv
SPATH = '/'.join(os.path.realpath(__file__).split('/')[:-1])


if '.cif' in jobfile:
   TYPE = 'cif'
elif '.xyz' in jobfile:
   TYPE = 'xyz'
else:
   print("Error: No Valid Filetype Found. Defaulting to .xyz")
   TYPE = 'xyz'


class CifAtoms(object):
    """Holes all of the atom data from the cif file"""

    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type
        self.coords = []
        self.charge = 0.0

    def set_coords(self, coords):
        """Sets the coordinates"""
        self.coords = coords

    def set_charge(self, eq=0.0):
        """Sets the atomic partial charge"""
        self.charge = eq


def import_table():
    """Imports the periodic table with the atoms in
    their respective period

    Period 19 isn't really a period but the Lanthanides
    Period 20 isn't really a period but the Actinides
    """
    periods = {1: 'H,Li,Na,K,Rb,Cs,Fr'.split(','),
               2: 'Be,Mg,Ca,Sr,Ba,Ra'.split(','),
               3: 'Sc,Y'.split(','),
               4: 'Ti,Zr,Hf,Rf'.split(','),
               5: 'V,Nb,Ta,Db'.split(','),
               6: 'Cr,Mo,W,Sg'.split(','),
               7: 'Mn,Tc,Re,Bh'.split(','),
               8: 'Fe,Ru,Os,Hs'.split(','),
               9: 'Co,Rh,Ir,Mt'.split(','),
               10: 'Ni,Pd,Pt,Ds'.split(','),
               11: 'Cu,Ag,Au,Rg'.split(','),
               12: 'Zn,Cd,Hg,Cn'.split(','),
               13: 'B,Al,Ga,In,Tl,Nh'.split(','),
               14: 'C,Si,Ge,Sn,Pb,Fl'.split(','),
               15: 'N,P,As,Sb,Bi,Mc'.split(','),
               16: 'O,S,Se,Te,Po,Lv'.split(','),
               17: 'F,Cl,Br,I,At,Ts'.split(','),
               18: 'He,Ne,Ar,Kr,Xe,Rn,Og'.split(','),
               19: 'La,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu'.split(','),
               20: 'Ac,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr'.split(',')}
    reference = {}
    for period in periods:
        for atom in periods[period]:
            reference[atom] = period
    return reference


def import_atoms(type='All'):
    """Imports the atom lists for the fingerprinting"""
    if type == 'All':
        filename = '{}/data/all_atoms.data'.format(SPATH)
    elif type == 'Metal':
        filename = '{}/data/metal_atoms.data'.format(SPATH)
    else:
        print("ERROR: DATA TYPE NOT SPECIFIED")
        exit()
    data = [atom.strip() for atom in open(filename, 'r').readlines()]
    atom_idx = {}
    blank = []
    for idx, atom in enumerate(data):
        atom_idx[atom] = idx
        blank.append(0)
    return {'Reference': atom_idx, 'Print': blank}


def read_atoms_cif():
    """Reads in the atoms from the cif"""
    atoms = {}
    data = open(jobfile, 'r').readlines()
    start = False
    start_flag = '_atom_type_partial_charge'
    stop_flag = 'loop_'
    for line in data:
        if not start and start_flag in line:
            start = True
        elif start and stop_flag in line:
            start = False
        elif start:
            line = line.split()
            if len(line) == 0:
                continue
            atom = CifAtoms(name=line[0], type=line[1])
            coords = [float(val) for val in line[3:-1]]
            atom.set_coords(coords)
            atom.set_charge(eq = float(line[-1].strip()))
            atoms[atom.name] = atom
    return atoms


def make_print(set, atoms):
    """Makes the fingerprint"""
    fprint = set['Print'][:]
    for atom in atoms:
        if atoms[atom].type in set['Reference']:
            idx = set['Reference'][atoms[atom].type]
            fprint[idx] = 1
    return fprint


def period_print(periods, atoms):
    """Generates a print based off the periods of the atoms
    found in the mof
    """
    fprint = [0 for val in range(0, max([periods[period] for period in periods]))]
    for atom in atoms:
        ident = atoms[atom].type
        fprint[periods[ident] - 1] = 1
    return fprint


def main():
    """Main Execution"""
    atom_set = import_atoms()
    metal_set = import_atoms(type='Metal')
    periods = import_table()
    if TYPE == 'cif':
        atoms = read_atoms_cif()
    all_fprint = make_print(atom_set, atoms)
    metal_fprint = make_print(metal_set, atoms)
    period_fprint = period_print(periods, atoms)


if __name__ in '__main__':
    main()
