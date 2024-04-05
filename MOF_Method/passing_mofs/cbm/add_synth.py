import pandas as pd

# Read the CSV files
csv1 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/cbm/CHOOH_cbm.csv')
csv2 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/synthesized.csv')

# Check for items in csv1['qmof_id'] that are in csv2['shell']
csv1['synthesized'] = csv1['qmof_id'].isin(csv2['shell']).map({True: 'yes', False: ''})

# Save the updated CSV1 to a new file
csv1.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/cbm/CHOOH_cbm.csv', index=False)
