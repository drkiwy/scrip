import os

def count_files_in_folder(folder_path):
    try:
        # Get the list of files and directories in the specified folder
        files_and_dirs = os.listdir(folder_path)

        # Filter out directories and count the number of files
        file_count = sum(1 for item in files_and_dirs if os.path.isfile(os.path.join(folder_path, item)))

        return file_count
    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")
        return 0
    except PermissionError:
        print(f"Error: Permission denied to access the folder '{folder_path}'.")
        return 0


# Example usage:
folder_path = 'D:\kits'  # Replace with the actual folder path
file_count = count_files_in_folder(folder_path)
print(f"There are {file_count} files in the folder.")
