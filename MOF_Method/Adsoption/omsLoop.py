import os
import subprocess
import glob
import shutil

zeopp_exec = "/Users/moinkhwaja/zeo++-0.3/network"
probe_radius = 1.65
num_samples = 50000

structure_folder = "/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Adsoption/structures/test"  # Path to the folder containing structure files
output_oms_folder = "/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Adsoption/OMS"

structure_files = glob.glob(f"{structure_folder}/*.cif")

for structure_file in structure_files:
    structure_name = os.path.splitext(os.path.basename(structure_file))[0]
    output_oms_file = os.path.join(output_oms_folder, f"{structure_name}.oms")
    output_vol_file = "output.vol"

    # Create the output_oms_folder if it doesn't exist
    os.makedirs(output_oms_folder, exist_ok=True)

    # Run the OMS command and direct output to the specified folder
    oms_command = f'"{zeopp_exec}" -oms "{structure_file}" > "{output_oms_file}"'
    vol_command = f'"{zeopp_exec}" -ha -vol {probe_radius} {probe_radius} {num_samples} {output_vol_file} "{structure_file}"'

    subprocess.run(oms_command, shell=True, check=True)
    subprocess.run(vol_command, shell=True, check=True)

    if os.path.exists(output_oms_file):
        with open(output_oms_file, 'r') as file:
            oms_results = file.read()
            print(f"Open Metal Sites Results for {structure_name}:")
            print(oms_results)

        # Extract the number of open metal sites from the output
        num_oms = oms_results.count('Metal site')  # Assuming each OMS is denoted by 'Metal site' in the output

        # Append the number of OMS to the output file
        with open(output_oms_file, 'a') as file:
            file.write(f"\nNumber of open metal sites: {num_oms}\n")

        with open(output_oms_file, 'r') as file:
            updated_oms_results = file.read()
            print(updated_oms_results)

    if os.path.exists(output_vol_file):
        with open(output_vol_file, 'r') as file:
            vol_results = file.read()
            print(f"CO2 Adsorption Accessible Volume Results for {structure_name}:")
            print(vol_results)
