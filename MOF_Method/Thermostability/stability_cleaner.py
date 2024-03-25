import csv
import re

file_path = 'MOF_Method/Thermostability/ch4_therm_stability.csv'

# Read the data from the CSV file into memory
with open(file_path, 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    if len(header) < 3:
        header.append('Stability Score')
    data = [header] + [row for row in reader]

# Process each row in the data
for i, row in enumerate(data[1:], start=1):  # Skip the header row
    if 'Failed' in row[1]:
        row.append('0.0')
    else:
        match = re.search(r'(\d+\.\d+)', row[1])
        if match:
            row.append(match.group(1))
        else:
            row.append('')  # Append an empty string if no number is found

# Write the modified data back to the same CSV file
with open(file_path, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
