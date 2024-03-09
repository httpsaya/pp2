import os
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src_file:
            with open(destination_file, 'w') as dest_file:
                dest_file.write(src_file.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"One of the files '{source_file}' or '{destination_file}' not found.")
        
source_file = r"C:\Users\admin\Desktop\pp2\lab6\files\output.txt" 
destination_file = r"C:\Users\admin\Desktop\pp2\lab6\files2\output.txt" 
copy_file(source_file, destination_file)
