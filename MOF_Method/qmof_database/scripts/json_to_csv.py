import os
import json
import pandas as pd

# Path to QMOF JSON file
qmof_json_path = "qmof.json"

# Read in QMOF JSON file
with open(qmof_json_path) as f:
    qmof = json.load(f)
qmof_df = pd.json_normalize(qmof).set_index("qmof_id")

# Write to CSV
qmof_df.to_csv("qmof.csv")
