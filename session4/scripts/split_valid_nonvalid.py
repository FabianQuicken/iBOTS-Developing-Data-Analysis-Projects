import sys
import pandas as pd

# Command-line inputs
input_csv_path = sys.argv[1]
output_valid_csv_path = sys.argv[2]
output_not_valid_csv_path = sys.argv[3]

# Load the csv file and extract active trials
df = pd.read_csv(input_csv_path)
df_valid = df[df.valid].copy()
df_not_valid = df[df.valid == False].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(output_valid_csv_path, index=False)
df_not_valid.to_csv(output_not_valid_csv_path, index=False)