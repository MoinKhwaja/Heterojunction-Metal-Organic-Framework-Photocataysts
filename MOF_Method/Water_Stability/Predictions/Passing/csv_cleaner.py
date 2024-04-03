import pandas as pd

# Read the CSV file
df = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Predictions/Passing/CHOOH_pass.csv', header=None)

# Remove '_primitive' from the first column
df[0] = df[0].str.replace('_primitive', '')

# Save the modified data to a new CSV file
df.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Predictions/Passing/CHOOH_pass_clean.csv', index=False, header=False)
