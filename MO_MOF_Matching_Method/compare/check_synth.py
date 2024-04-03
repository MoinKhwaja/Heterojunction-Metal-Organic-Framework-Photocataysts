import pandas as pd

# Read the CSV files
csv1 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/synthesized.csv')
csv2 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/CHOOH_compare.csv')

# Check if 'core' in csv1 matches 'Material ID' in csv2
csv2['core synthesized'] = csv2['Material ID'].isin(csv1['core']).map({True: 'yes', False: ''})

# Check if 'shell' in csv1 matches 'qmof_id' in csv2
csv2['mof synthesized'] = csv2['qmof_id'].isin(csv1['shell']).map({True: 'yes', False: ''})

# Add 'target' column if both 'core synthesized' and 'shell synthesized' are 'yes'
csv2['target'] = ''
csv2.loc[(csv2['core synthesized'] == 'yes') & (csv2['mof synthesized'] == 'yes'), 'target'] = 'yes'

# Save the updated CSV2
csv2.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/CHOOH_compare.csv', index=False)