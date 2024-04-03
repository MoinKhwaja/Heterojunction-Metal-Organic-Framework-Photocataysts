import pandas as pd
import os

folder_path = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Descriptors/CO_Discript'

first_rows = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv') and not filename.startswith('.'):
        file_path = os.path.join(folder_path, filename)
        data = pd.read_csv(file_path, nrows=1)
        first_rows.append(data)

consolidated_data = pd.concat(first_rows, ignore_index=True)

script_dir = os.path.dirname(__file__)

output_file_path = os.path.join(script_dir, 'CO_consolidate.csv')

consolidated_data.to_csv(output_file_path, index=False)
