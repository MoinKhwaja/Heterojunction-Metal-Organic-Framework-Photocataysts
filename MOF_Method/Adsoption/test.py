import os
import subprocess

# Define the paths to the Zeo++ executable and the structure file
zeopp_exec = "/Users/moinkhwaja/zeo++-0.3/network"  # Update this path
structure_file = "/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Adsoption/structure.cif"  # Update this path

# Define output files
output_sa_file = "output.sa"

# Define parameters
probe_radius = 1.2
num_samples = 2000

# Create a Zeo++ command to calculate accessible surface area directly from CIF
command = f"{zeopp_exec} -ha -sa {probe_radius} {probe_radius} {num_samples} {output_sa_file} {structure_file}"

# Execute the command using subprocess
result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

# Print the result of the command execution
print(result.stdout)

# Check if the output file exists
if os.path.exists(output_sa_file):
    # Read and print the contents of the output file
    with open(output_sa_file, 'r') as file:
        sa_results = file.read()
        print("Accessible Surface Area Results:")
        print(sa_results)
else:
    print("Output file not found.")


