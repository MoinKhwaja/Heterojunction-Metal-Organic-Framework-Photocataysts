#!/usr/bin/env python

"""
Tests the connectivity graphs of the different functional groups
"""


import numpy as np
from sys import argv
from glob import glob
from itertools import combinations


script, infile = argv


def get_atom(tag):
    """Gets atom's identity based on the tag, ex C1, Cr13, etc.
    will return C and Cr, etc
    """
    try:
        float(tag[1])
        return tag[0]
    except ValueError:
        return tag[:2]


def distance(cor1, cor2):
    """Returns Euclidean Distance"""
    return (sum((cor1 - cor2) ** 2)) ** 0.5


def get_structure():
    """Imports the structure being analysed, returns the connectivity table"""
    blen = 1.8 # maximum distance for bond lengths
    data = open(infile, 'r').readlines()[2:]
    table = {}
    atoms, locs = [], {}
    for dx, line in enumerate(data):
        idx = dx + 1
        tag = line.split()[0] + str(idx)
        atoms.append(tag)
        coords = np.array([float(val) for val in line.split()[1:]])
        locs[tag] = coords
    combos = list(combinations(atoms, 2))
    for combo in combos:
        one = combo[0]
        two = combo[1]
        dist = distance(locs[one], locs[two])
        if dist > blen:
            continue
        if one not in table:
            table[one] = [two]
        if two not in table:
            table[two] = [one]
        if two not in table[one]:
            table[one].append(two)
        if one not in table[two]:
            table[two].append(one)
    return table


def import_groups():
    """Imports the groups based on their provided connectivity tables"""
    group_files = glob('../COOCH3*.conn')
    groups = {}
    for gfile in group_files:
        group = gfile.split('.conn')[0].split('/')[-1]
        data = open(gfile, 'r').readlines()
        groups[group] = {'Main': data[0].strip(), 'Connect': {}}
        if len(data) == 1:
            groups[group]['Connect'][data[0].strip()] = []
            continue
        for line in data[1:]:
            one = line.split()[0]
            two = line.split()[1]
            if one not in groups[group]['Connect']:
                groups[group]['Connect'][one] = [two]
            if two not in groups[group]['Connect']:
                groups[group]['Connect'][two] = [one]
            if two not in groups[group]['Connect'][one]:
                groups[group]['Connect'][one].append(two)
            if one not in groups[group]['Connect'][two]:
                groups[group]['Connect'][two].append(one)
    return count_layers(groups)


def count_layers(groups):
    """Counts the number of layers in the functional group"""
    for group in groups:
        g_main = groups[group]['Main']
        conns  = groups[group]['Connect']
        n_main = len(conns[g_main]) + 1
        natoms = len(conns)
        groups[group]['Nodes'] = [g_main]
        if n_main == natoms:
            groups[group]['Layers'] = 1
            continue
        c_layers = 1
        done, checked = False, [g_main]
        next = conns[g_main][:]
        while not done:
            check = next[:]
            next = []
            for atom in check:
                if atom in checked:
                    continue
                if len(conns[atom]) > 1:
                    for satom in conns[atom]:
                        if satom in checked:
                            continue
                        next.append(satom)
                        if atom not in groups[group]['Nodes']:
                            groups[group]['Nodes'].append(atom)
                checked.append(atom)
            if len(next) == 0:
                groups[group]['Layers'] = c_layers
                done = True
            else:
                c_layers += 1
            
    return groups


def single_layer_scan(groups, group, structure):
    """Performs the can on groups with a single layer"""
    found = False
    g_main = groups[group]['Main']
    g_type = get_atom(g_main)
    n_num  = len(groups[group]['Connect'][g_main]) + 1
    for atom in structure:
        s_type = get_atom(atom)
        tol = 0
        if g_type != s_type:
            continue
        if len(structure[atom]) != n_num:
            continue
        g_list = groups[group]['Connect'][g_main][:]
        s_list = structure[atom][:]
        if len(g_list) == 0 and len(s_list) == 1:
            found = True
        for s_tag in s_list:
            if found:
                break
            s_id = get_atom(s_tag)
            s_found = False
            for g_tag in g_list:
                g_id = get_atom(g_tag)
                if s_id == g_id:
                    g_list.remove(g_tag)
                    s_found = True
            if not s_found and tol > 0:
                break
            elif not s_found:
                tol += 1
        if len(g_list) == 0 and tol <= 1 and not found:
            found = True
        if found:
            print "Found", group
            break
    if not found:
        print group, "not found"

    return found


def multi_layer_scan_alt(group, structure):
    """Performs a multi layer scan for the structure"""
    # initialize the data for the connecting atom
    start      = group['Main']
    start_conn = group['Connect'][start]
    start_n    = len(start_conn)
    start_elem = get_atom(start)

    nodes = group['Nodes']
    print nodes, start_n
    found, first = False, True
    running = True
    omit = []
    while running:
        for atom in structure:
            elem = get_atom(atom)
            if elem == 'O':
                print structure[atom]
            if elem != start_elem:
                continue
            print len(structure[atom])
            if len(structure[atom]) != start_n + 1:
                continue
            print atom
        exit()


        running = False


def multi_layer_scan(groups, group, structure):
    """Perform the multilayer scan"""
    m_found = True
    nodes  = groups[group]['Nodes']
    print groups[group]['Main'], nodes

    consider = [atom for atom in structure]
    print consider
    founds = []
    for node in nodes:
        found = False
        next   = []
        g_main = node
        g_type = get_atom(g_main)
        n_num  = len(groups[group]['Connect'][g_main]) + 1
        for atom in consider:
            s_type = get_atom(atom)
            tol = 0
            if g_type != s_type:
                continue
            if len(structure[atom]) != n_num:
                continue
            g_list = groups[group]['Connect'][g_main][:]
            s_list = structure[atom][:]
            if len(g_list) == 0 and len(s_list) == 1:
                found = True
            for s_tag in s_list:
                if found:
                    break
                s_id = get_atom(s_tag)
                s_found = False
                for g_tag in g_list:
                    g_id = get_atom(g_tag)
                    if s_id == g_id:
                        g_list.remove(g_tag)
                        s_found = True
                if not s_found and tol > 0:
                    break
                elif not s_found:
                    tol += 1
            if len(g_list) == 0 and tol <= 1 and not found:
                found = True
            if found:
                print "Found", group
                break
        founds.append(found)

    for found in founds:
        if not found:
            m_found = False
    print m_found, founds

    return m_found


def scan_for_groups(groups, structure):
    """Performs the scan for each group"""
    for group in groups:
        if groups[group]['Layers'] == 1:
            single_layer_scan(groups, group, structure)
        else:
            multi_layer_scan_alt(groups[group], structure)
    return None 


def main():
    """Main Execution"""
    groups = import_groups()
    structure = get_structure()
    scan_for_groups(groups, structure)


if __name__ in '__main__':
    main()
