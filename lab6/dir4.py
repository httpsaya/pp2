import os

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

file_path = r"C:\Users\admin\Desktop\pp2\lab6\saya.txt"
line_count = count_lines(file_path)
if line_count is not None:
    print(f"Number of lines in '{file_path}': {line_count}")
