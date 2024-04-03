import pandas as pd

# Read CSV files into DataFrames
df1 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/passed_shell/CH4_cbm.csv')
df2 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/passed_core/CH4.csv')

# Create an empty DataFrame to store comparison results
comparison_df = pd.DataFrame(columns=['qmof_id', 'Material ID', 'CBM Comparison', 'VBM Comparison'])

# Iterate over each row in df1
for index, row in df1.iterrows():
    qmof_id = row['qmof_id']
    cbm1 = row['outputs.pbe.cbm']
    vbm1 = row['outputs.pbe.vbm']
    
    # Iterate over each row in df2 and compare cbm1 to CBM and vbm1 to VBM
    for index2, row2 in df2.iterrows():
        cbm2 = row2['CBM']
        vbm2 = row2['VBM']
        material_id = row2['Material ID']
        
        # Compare cbm1 to cbm2
        if cbm1 > cbm2:
            cbm_comparison = 'higher'
        elif cbm1 < cbm2:
            cbm_comparison = 'lower'
        else:
            cbm_comparison = 'equal'
        
        # Compare vbm1 to vbm2
        if vbm1 > vbm2:
            vbm_comparison = 'higher'
        elif vbm1 < vbm2:
            vbm_comparison = 'lower'
        else:
            vbm_comparison = 'equal'
        
        # Append comparison result to comparison_df
        comparison_df = comparison_df.append({'qmof_id': qmof_id, 'Material ID': material_id, 'CBM Comparison': cbm_comparison, 'VBM Comparison': vbm_comparison}, ignore_index=True)

# Write comparison_df to a new CSV file
comparison_df.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MO_MOF_Matching_Method/compare/CH4_compare.csv', index=False)
