import os
import pandas as pd

# Directory containing the Excel files
input_directory = 'Data'
# Directory to save the CSV files
output_directory = 'Data_csv'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each file in the input directory
for file_name in os.listdir(input_directory):
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        # Construct file paths
        input_file_path = os.path.join(input_directory, file_name)
        output_file_path = os.path.join(output_directory, file_name.replace('.xlsx', '.csv').replace('.xls', '.csv'))
        
        # Read the Excel file
        df = pd.read_excel(input_file_path)
        
        # Save to CSV
        df.to_csv(output_file_path, index=False)
        print(f"Converted {file_name} to CSV")
