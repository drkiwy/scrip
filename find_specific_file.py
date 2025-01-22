import os

def search_file_in_drive(drive_letter, filename, output_file):
    """
    Searches for a file in all directories of a given drive and saves results to a file.

    Parameters:
        drive_letter (str): The drive to search, e.g., "C".
        filename (str): The name or part of the filename to search for.
        output_file (str): The path of the output .txt file to save results.

    Returns:
        None
    """
    matched_files = []
    root_path = f"{drive_letter}:\\"

    print(f"Searching for '{filename}' in {root_path}...")

    try:
        # Walk through the directory tree
        for root, dir, files in os.walk(root_path, topdown=True):
            for file in files:
                if filename.lower() in file.lower():  # Case-insensitive search
                    matched_files.append(os.path.join(root, file))
    except PermissionError:
        print(f"Permission denied: Unable to access some directories in {root_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Write results to the output file
    with open(output_file, "w") as file:
        if matched_files:
            file.write(f"Search results for '{filename}' in {drive_letter}: drive:\n\n")
            file.write("\n".join(matched_files))
            print(f"\nFound {len(matched_files)} file(s). Results saved to '{output_file}'.")
        else:
            file.write(f"No files found with the name '{filename}' in {drive_letter}: drive.\n")
            print(f"\nNo files found with the name '{filename}' in {drive_letter}: drive. Results saved to '{output_file}'.")

if __name__ == "__main__":
    # Input: Drive letter and filename to search
    drive_letter = input("Enter the drive letter (e.g., C): ").strip().upper()
    filename = input("Enter the filename or part of the filename to search for: ").strip()
    output_file = "result_search.txt"  # Output file to save results

    # Check if the drive exists
    if not os.path.exists(f"{drive_letter}:\\"):
        print(f"The specified drive '{drive_letter}:' does not exist or is inaccessible. Please check and try again.")
    else:
        # Perform the search and save results
        search_file_in_drive(drive_letter, filename, output_file)
