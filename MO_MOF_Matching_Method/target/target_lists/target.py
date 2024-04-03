import pandas as pd

# Read the CSV file
csv2 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/CO_compare.csv')

# Filter rows where 'target' is 'yes'
filtered_csv = csv2[csv2['target'] == 'yes']

# Save the filtered CSV to a new file
filtered_csv.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/target/target_lists/CO_target.csv', index=False)
