import csv
import os
import shutil

input_csv = 'MOF_Method/CHOOH_MOF.csv'  # Path to your CSV file
source_folder = 'MOF_Method/qmof_database/qmof_database/scripts/relaxed_structures'  # Path to the folder containing .cif files
destination_folder = 'MOF_Method/CIF_Search/filtered_cifs/CH4_cifs'  # Path to the folder where you want to copy the files

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Read the CSV file and extract 'qmof_id' values
with open(input_csv, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        qmof_id = row['qmof_id']  # Use the correct column name here
        cif_file = f"{qmof_id.replace('_', '-')}.cif"  # Replace underscores with hyphens

        # Search for the .cif file in the source folder
        source_file_path = os.path.join(source_folder, cif_file)
        if os.path.exists(source_file_path):
            # Copy the file to the destination folder
            shutil.copy(source_file_path, destination_folder)