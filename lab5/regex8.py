import re
def snake_to_camel(snake_str):
    components = re.findall(r'[A-Z][A-Z]*', snake_str)
    return components

snake_case_str = str(input("Enter a string: "))
camel_case_str = snake_to_camel(snake_case_str)
print(camel_case_str)
