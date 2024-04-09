import pandas as pd

comparison_df = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/CO_compare.csv')

comparison_df['type'] = comparison_df.apply(lambda row: 
    '2' if (row['CBM Comparison'] == 'higher' and row['VBM Comparison'] == 'higher') else
    '1' if (row['CBM Comparison'] == 'higher' and row['VBM Comparison'] == 'lower') else
    '2(low)', axis=1)

comparison_df.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/CO_compare.csv', index=False)
