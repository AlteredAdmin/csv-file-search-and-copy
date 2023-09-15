import os
import pandas as pd
import shutil

# Prompt for directory to search in
search_dir = input("Enter the directory to search in: ")

# Prompt for directory to copy to
copy_dir = input("Enter the directory to copy the files to: ")

# Prompt for location of the CSV file
csv_file_path = input("Enter the location of the CSV file: ")

# If the copy directory doesn't exist, create it
if not os.path.exists(copy_dir):
    os.makedirs(copy_dir)

# Read the CSV file
try:
    file_df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print("CSV file not found. Please check the file path and try again.")
    exit()

# Loop through the "File name" column
for file_name in file_df['File name']:
    # Use os.walk to search through the directory and its subdirectories
    for root, dirs, files in os.walk(search_dir):
        if file_name in files:
            # Construct full file path
            file_path = os.path.join(root, file_name)
            # Copy file to destination directory
            shutil.copy2(file_path, copy_dir)
            print(f'Copied file {file_name} to {copy_dir}')
