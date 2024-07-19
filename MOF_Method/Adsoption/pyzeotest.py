from pyzeo import AtomNetwork

cif_file_path = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Adsoption/structures/test/Al6H50C99O31.cif'

# Initialize AtomNetwork and read the CIF file
structure = AtomNetwork()
structure.read_from_CIF(cif_file_path)

# Since there is no direct method for finding open metal sites in AtomNetwork,
# let's print the structure to inspect it and figure out how to proceed.
print(structure)


