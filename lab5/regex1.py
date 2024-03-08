import re
a = str(input("Enter a string: "))
print(re.match(r'ab*', a))