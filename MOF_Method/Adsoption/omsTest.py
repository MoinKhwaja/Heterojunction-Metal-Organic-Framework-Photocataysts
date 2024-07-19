import os
import subprocess

# Define the paths to the Zeo++ executable and the structure file
zeopp_exec = "/Users/moinkhwaja/zeo++-0.3/network"
structure_file = "/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Adsoption/Nd2H48C39S3N14O19.cif"

# Output files
output_vol_file = "output.vol"
output_oms_file = "output.oms"

# Parameters for CO2 adsorption calculation
probe_radius = 1.65
num_samples = 50000

# Command to identify open metal sites
oms_command = f"{zeopp_exec} -oms {structure_file}"

# Command to calculate accessible volume for CO2 adsorption
vol_command = f"{zeopp_exec} -ha -vol {probe_radius} {probe_radius} {num_samples} {output_vol_file} {structure_file}"

# Execute the OMS command
subprocess.run(oms_command, shell=True, check=True)

# Execute the CO2 adsorption command
subprocess.run(vol_command, shell=True, check=True)

# Read and print the results
if os.path.exists(output_oms_file):
    with open(output_oms_file, 'r') as file:
        oms_results = file.read()
        print("Open Metal Sites Results:")
        print(oms_results)

if os.path.exists(output_vol_file):
    with open(output_vol_file, 'r') as file:
        vol_results = file.read()
        print("CO2 Adsorption Accessible Volume Results:")
        print(vol_results)
