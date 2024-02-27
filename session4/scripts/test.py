import sys
import pandas as pd

# Command-line inputs
input_csv_path = sys.argv[1]
output_valid_csv_path = sys.argv[2]
output_not_valid_csv_path = sys.argv[3]

# Load the csv file
df = pd.read_csv(input_csv_path)

# Assuming 'valid' column exists and contains boolean values
df_valid = df[df['valid']].copy()  # Filter valid rows
df_not_valid = df[~df['valid']].copy()  # Filter not valid rows

# Save the new dataframes as csv files
df_valid.to_csv(output_valid_csv_path, index=False)
df_not_valid.to_csv(output_not_valid_csv_path, index=False)