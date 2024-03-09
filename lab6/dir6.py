import string
import os


os.makedirs("files", exist_ok=True)

for letter in string.ascii_uppercase:
    file_path = os.path.join("files", f"{letter}.txt")
    with open(file_path, 'w') as file:
        pass  

print("Text files created successfully.")
