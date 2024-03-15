import os
import json
from pymatgen.core import Structure

# ------Settings------#
struct_json_path = "qmof_structure_data.json"  # path to structure json
cif_folder_path = "relaxed_structures"  # path to folder where CIFs will be stored
write_site_props = True  # if site properties should be written to CIF
only_ddec_charge = False  # set to True if you only want _atom_site_charge flags
# ------Settings------#

# Make new folder to store CIFs
if not os.path.exists(cif_folder_path):
    os.mkdir(cif_folder_path)

# Read in structure data
with open("qmof_structure_data.json") as f:
    qmof_struct_data = json.load(f)

# Loop over structures and write each one out to a CIF
qmof_structs = {}
for entry in qmof_struct_data:

    qmof_id = entry["qmof_id"]  # name for CIF
    print(f"Writing {qmof_id}")

    struct = Structure.from_dict(entry["structure"])  # Pymatgen structure
    cif_path = os.path.join(cif_folder_path, f"{qmof_id}.cif")  # path to write CIF
    struct.to(filename=cif_path)  # write CIF
    properties = dict(sorted(struct.site_properties.items()))  # fetch site properties

    # Overwrite CIF with site properties
    if write_site_props:
        new_cif = ""
        i = 0
        prop_lines = False

        with open(cif_path, "r") as f:
            for line in f:
                if "_atom_site_occupancy" in line:
                    new_cif += line
                    if only_ddec_charge:
                        new_cif += f" _atom_site_charge\n"
                    else:
                        for key in properties.keys():
                            new_cif += f" _atom_site_{key}\n"
                    prop_lines = True
                    continue

                if i == len(struct):
                    prop_lines = False

                if prop_lines:
                    new_cif += line.strip()
                    if only_ddec_charge:
                        new_cif += f"  {properties['pbe_ddec_charge'][i]}"
                    else:
                        for value_sets in properties.values():
                            new_cif += f"  {value_sets[i]}"
                    new_cif += "\n"
                    i += 1
                else:
                    new_cif += line

        # Write out new CIF
        with open(cif_path, "w") as f:
            f.write(new_cif)
