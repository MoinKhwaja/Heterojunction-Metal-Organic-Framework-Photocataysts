import pandas as pd

# Load the CSV files into dataframes
csv1 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/cbm/CHOOH_cbm.csv')
csv2 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Thermostability/thermostable_cifs/CHOOH_therm_stable.csv')

# Merge the dataframes based on the 'qmof_id' column
csv2['qmof_id'] = csv2['qmof_id'].str.replace('.cif', '')
merged = pd.merge(csv1, csv2[['qmof_id', 'StabilityScore']], on='qmof_id', how='left')

# Save the merged dataframe to a new CSV file
merged.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/cbm/CHOOH_cbm.csv', index=False)
