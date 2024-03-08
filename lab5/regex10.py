import re

def insert_spaces(input_string):
    words = re.findall('[A-Z][a-z]*', input_string)
    result = re.sub('[A-Z][a-z]*', lambda x: '_' + x.group(0) if x.start() != 0 else x.group(0), input_string)
    return result
input_string = str(input("Enter a string: "))
result = insert_spaces(input_string)
print(result)
