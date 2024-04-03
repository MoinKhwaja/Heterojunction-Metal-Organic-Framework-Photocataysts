import pandas as pd

# Read the first CSV file with header as first row
df1 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Predictions/Passing/CHOOH_pass_clean.csv')

# Read the second CSV file with header as first row
df2 = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/qmof_database/qmof_database/qmof.csv')

# Create an empty DataFrame to store the matched rows including headers
matched_rows = pd.DataFrame(columns=df2.columns)

# Iterate over the rows of the first DataFrame
for index, row in df1.iterrows():
    # Get the value from the first column of the first DataFrame
    value_to_search = row[0]
    
    # Search for the value in the first column of the second DataFrame
    matched_row = df2[df2[df2.columns[0]] == value_to_search]
    
    # If a match is found, append the matched row to the DataFrame
    if not matched_row.empty:
        matched_rows = matched_rows.append(matched_row)

# Save the matched rows to a new CSV file
matched_rows.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/CHOOH_match.csv', index=False)
