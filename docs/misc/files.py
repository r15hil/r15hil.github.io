import json
import os

# Specify the directory path
directory_path = "recipes_all"

# Get the list of all entries in the directory
entries = os.listdir(directory_path)

# Filter out directories, keeping only files
file_names = [
    entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))
]

# Convert the list to a JSON-formatted string with double quotes
file_names_json = json.dumps(file_names)

# Define the output string starting with 'const recipeFiles = '
output_string = f"const recipeFiles = {file_names_json};"

# Specify the output file path
output_file_path = "file.js"

# Write the output string to the file
with open(output_file_path, "w") as file:
    file.write(output_string)

print(f"File names have been written to {output_file_path}")
