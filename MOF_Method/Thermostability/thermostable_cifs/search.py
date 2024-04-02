import pandas as pd
import shutil
import os

df = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Thermostability/thermostable_cifs/CHOOH_therm_stable.csv')

filtered_df = df[df['StabilityScore'] > 0.5]

source_dir = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Thermostability/thermostable_cifs/CHOOH_cifs'
dest_dir = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Thermostability/thermostable_cifs/CHOOH_Stable'

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for filename in filtered_df['File']:
    source_file = os.path.join(source_dir, filename)
    dest_file = os.path.join(dest_dir, filename)
    
    if os.path.exists(source_file):
        shutil.copy(source_file, dest_file)
    else:
        print(f'File {source_file} not found.')

print('Files copied successfully.')
