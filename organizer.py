import os
import shutil

def organize_py_files():
    # 1. Get the current directory where this script is running
    current_dir = os.getcwd()
    
    # 2. Define the name of the new folder
    target_folder_name = "python_files_backup"
    target_folder_path = os.path.join(current_dir, target_folder_name)
    
    # Get the name of this specific script file to avoid moving itself
    current_script_name = os.path.basename(__file__)
    
    try:
        # 3. Create the new folder if it doesn't already exist
        if not os.path.exists(target_folder_path):
            os.makedirs(target_folder_path)
            print(f"Created new folder: {target_folder_name}")
        else:
            print(f"Folder '{target_folder_name}' already exists. Packing files into it...")

        # 4. List all files in the current directory
        all_files = os.listdir(current_dir)
        moved_count = 0

        # 5. Loop through and move the .py files
        for file in all_files:
            # Check if it's a file, ends with .py, and isn't this script itself
            if os.path.isfile(file) and file.endswith('.py') and file != current_script_name:
                source_file_path = os.path.join(current_dir, file)
                destination_file_path = os.path.join(target_folder_path, file)
                
                # Move the file
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved: {file}")
                moved_count += 1

        print(f"\nSuccess! Successfully moved {moved_count} Python file(s) into '{target_folder_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    organize_py_files()