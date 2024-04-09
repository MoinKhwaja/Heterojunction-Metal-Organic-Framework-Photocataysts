import pandas as pd

df1 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Predictions/Passing/CHOOH_pass_clean.csv')

df2 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/qmof_database/qmof_database/qmof.csv')

matched_rows = pd.DataFrame(columns=df2.columns)

for index, row in df1.iterrows():
    value_to_search = row[0]
    matched_row = df2[df2[df2.columns[0]] == value_to_search]
    if not matched_row.empty:
        matched_rows = matched_rows.append(matched_row)

matched_rows.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/CHOOH_match.csv', index=False)
