import os
import subprocess
import glob

zeopp_exec = "/Users/moinkhwaja/zeo++-0.3/network"
probe_radius = 1.65
num_samples = 50000

structure_folder = "/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Adsoption/structures/test"
output_oms_folder = "/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Adsoption/OMS"

# Ensure the output directory exists
os.makedirs(output_oms_folder, exist_ok=True)

# Get all CIF files in the structure folder
structure_files = glob.glob(f"{structure_folder}/*.cif")

for structure_file in structure_files:
    structure_name = os.path.splitext(os.path.basename(structure_file))[0]
    output_oms_file = os.path.join(output_oms_folder, f"{structure_name}.oms")
    output_vol_file = "output.vol"
    
    # Run the OMS command and ensure output is redirected correctly
    oms_command = f'{zeopp_exec} -oms {structure_file}'
    vol_command = f'{zeopp_exec} -ha -vol {probe_radius} {probe_radius} {num_samples} {output_vol_file} {structure_file}'
    
    # Open the output file for writing and execute the command with stdout redirected
    with open(output_oms_file, 'w') as oms_output:
        subprocess.run(oms_command, shell=True, check=True, stdout=oms_output, stderr=subprocess.STDOUT)
    
    subprocess.run(vol_command, shell=True, check=True)

    if os.path.exists(output_oms_file):
        with open(output_oms_file, 'r') as file:
            oms_results = file.read()
            print(f"Open Metal Sites Results for {structure_name}:")
            print(oms_results)
        
        # Count the number of open metal sites from the output
        num_oms = oms_results.count('Metal site')  # Adjust based on actual output
        print(f"Number of Open Metal Sites: {num_oms}")
        
        # Append the number of OMS to the output file
        with open(output_oms_file, 'a') as file:
            file.write(f"\nNumber of open metal sites: {num_oms}\n")

    if os.path.exists(output_vol_file):
        with open(output_vol_file, 'r') as file:
            vol_results = file.read()
            print(f"CO2 Adsorption Accessible Volume Results for {structure_name}:")
            print(vol_results)
    else:
        print(f"Error: {output_vol_file} not found for {structure_name}")


