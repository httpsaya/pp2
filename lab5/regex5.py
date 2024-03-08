import re
a = str(input("Enter a string: "))
print(re.match(r'a.*b$', a))