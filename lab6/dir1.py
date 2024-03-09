import os

def list_directories_files_all(path):
    print("Directories:")
    for entry in os.scandir(path):
        if entry.is_dir():
            print(entry.name)

    print("\nFiles:")
    for entry in os.scandir(path):
        if entry.is_file():
            print(entry.name)

    print("\nAll directories and files:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))
path = os.getcwd()
list_directories_files_all(path)
