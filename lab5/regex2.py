import re
a = str(input("Enter a string: "))
print(re.match(r'ab{2,3}', a))