import os

def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

file_path = r"C:\Users\admin\Desktop\pp2\lab6\files\output.txt" 
data = [1, 2, 3, 4, 5]
write_list_to_file(file_path, data)
print(f"List written to {file_path}")
