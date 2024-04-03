import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Predictions/full_predict/CHOOH_predict.csv')

# Filter rows where CH4_predict is above 0.50
filtered_df = df[df['CHOOH_predict'] > 0.50]

# Save the filtered data to a new CSV file
filtered_df.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Predictions/Passing/CHOOH_pass.csv', index=False)
