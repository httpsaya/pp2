import os

def get_filename_and_directory(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Path: {path}")
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print("Path does not exist.")
path = os.getcwd()
get_filename_and_directory(path)
