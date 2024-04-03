import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/CO_match.csv')

# Add 0.425 to 'outputs.pbe.cbm' column
df['outputs.pbe.cbm'] = df['outputs.pbe.cbm'] + 0.425
df['outputs.pbe.vbm'] = df['outputs.pbe.vbm'] - 0.425
df['outputs.pbe.bandgap'] = df['outputs.pbe.bandgap'] + 0.85

# Save the modified DataFrame back to the same CSV file
df.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/passing_mofs/CO_match.csv', index=False)
