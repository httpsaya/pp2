import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)

    print(f"Path: {path}")
    print(f"Exists: {exists}")
    print(f"Readable: {readable}")
    print(f"Writable: {writable}")
    print(f"Executable: {executable}")

path = "/path/to/your/directory_or_file"
check_access(path)
