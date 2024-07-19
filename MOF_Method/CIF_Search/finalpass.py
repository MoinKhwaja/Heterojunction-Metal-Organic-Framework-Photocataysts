import os
import pandas as pd
import shutil

csv_path = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/CIF_Search/finalpass/CH4_match.csv'
cif_folder = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/CIF_Search/filtered_cifs/CH4_cifs'
destination_folder = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/CIF_Search/finalpass/CH4_pass'

df = pd.read_csv(csv_path)
qmof_ids = df['qmof_id'].tolist()
os.makedirs(destination_folder, exist_ok=True)

for qmof_id in qmof_ids:
    cif_filename = f"{qmof_id}.cif"
    cif_path = os.path.join(cif_folder, cif_filename)
    if os.path.isfile(cif_path):
        shutil.copy(cif_path, destination_folder)
        print(f"Copied: {cif_filename}")
    else:
        print(f"File not found: {cif_filename}")

print("Finished copying matching CIF files.")
