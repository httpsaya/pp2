import re
a = str(input("Enter a string: "))
print(re.findall(r'[a-z]_[a-z]', a))