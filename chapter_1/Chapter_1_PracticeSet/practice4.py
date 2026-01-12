# python program to print the contents of a directory using the OS module using AI.

import os  # Importing the OS module to interact with the operating system

def print_directory_contents(path='.'):
    """
    Prints the files and sub-directories in the given directory path.
    Default is current directory ('.').
    """

    try:
        # os.listdir(path) returns a list of files & folders in the given directory
        entries = os.listdir(path)
    except FileNotFoundError:
        # This runs if the directory does not exist
        print(f"Error: The directory {path!r} does not exist.")
        return
    except PermissionError:
        # This runs if we do not have permission to open the directory
        print(f"Error: Permission denied to access {path!r}.")
        return
    except OSError as e:
        # Handles other OS related errors
        print(f"Error accessing {path!r}: {e}")
        return

    print(f"Contents of directory {path!r}:")
    
    # Loop through all files and folders and print their names
    for name in entries:
        print(name)

# Main program starts here
if __name__ == "__main__":
    # Ask user for path. If left blank, use current directory ('.')
    directory_path = input("Enter directory path (or leave blank for current): ").strip()
    
    if directory_path == '':
        directory_path = '.'  # Default to current directory
    
    # Call the function to print directory contents
    print_directory_contents(directory_path)
