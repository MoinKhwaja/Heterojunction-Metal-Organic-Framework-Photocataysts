import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/CH4_match.csv')

# Select specific columns
selected_columns = df[['qmof_id', 'info.pld' ,'outputs.pbe.cbm' , 'outputs.pbe.vbm' , 'outputs.pbe.bandgap']]

# Save the selected columns to a new CSV file
selected_columns.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/cbm/CH4_cbm.csv', index=False)
