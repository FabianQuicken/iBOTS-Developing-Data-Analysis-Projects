import sys
import pandas as pd

# Command-line inputs
input_csv_path = sys.argv[1]
output_csv_path = sys.argv[2]

# Load the csv file and extract active trials
df = pd.read_csv(input_csv_path)
df_correct_response = df[df.response==1]

# Save the new dataframe as a csv file
df_correct_response.to_csv(output_csv_path, index=False)