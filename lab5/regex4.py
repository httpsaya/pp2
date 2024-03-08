import re
a = str(input("Enter a string: "))
print(re.findall(r'[A-Z][a-z]', a))