import os

def list_files_in_directory():
    # Get directory path from the environment variable
    dir_path = os.environ('DIRECTORY_PATH')
    
    if not dir_path:
        print("Environment variable 'DIRECTORY_PATH' is not set.")
        return

    if not os.path.exists(dir_path):
        print(f"The directory '{dir_path}' does not exist.")
        return
    
    # List files in the directory
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            print(file_name)

if __name__ == "__main__":
    list_files_in_directory()
