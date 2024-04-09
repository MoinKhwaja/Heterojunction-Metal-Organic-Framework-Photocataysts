import pandas as pd

csv2 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/CO_compare.csv')

filtered_csv = csv2[csv2['target'] == 'yes']

filtered_csv.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/target/target_lists/CO_target.csv', index=False)
