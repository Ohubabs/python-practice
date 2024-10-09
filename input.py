def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split() #this will convert the string inputs into an ordered list
    print(folder_paths)

    # Print elements in the list
    #for folder_path in folder_paths:
    #    print(folder_path)

if __name__ == "__main__":
    main()

---
# list files in folders
import os 

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()
