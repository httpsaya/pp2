import os

def list_directories_and_files(path):
    print("Directories:")
    for entry in os.scandir(path):
        if entry.is_dir():
            print(entry.name)

    print("\nFiles:")
    for entry in os.scandir(path):
        if entry.is_file():
            print(entry.name)

    print("\nAll directories and files:")
    for entry in os.walk(path):
        print(entry[0])
        for file in entry[2]:
            print(f"  {file}")
path = "/path/to/your/directory"
list_directories_and_files(path)
