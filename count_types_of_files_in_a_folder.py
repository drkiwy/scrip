import os
from collections import defaultdict

def count_files_by_extension(folder_path):
    # Dictionary to store the count of each file extension
    file_counts = defaultdict(int)
    
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"The path {folder_path} is not a valid directory.")
        return
    
    # Walk through the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (ignore subdirectories)
        if os.path.isfile(file_path):
            # Get the file extension and convert to lowercase for consistency
            extension = os.path.splitext(filename)[1].lower()
            file_counts[extension] += 1
    
    # Print the results
    if file_counts:
        print(f"File counts by extension in '{folder_path}':")
        for ext, count in file_counts.items():
            print(f"{ext or 'No extension'}: {count}")
    else:
        print("No files found in the directory.")

# Example usage
folder_path = 'D:\kits'  # Replace with the actual folder path
count_files_by_extension(folder_path)
