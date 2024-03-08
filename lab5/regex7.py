def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_case = components[0] + ''.join(x.title() for x in components[1:])
    return camel_case

snake_case_str = str(input("Enter a string: "))
camel_case_str = snake_to_camel(snake_case_str)
print(camel_case_str)
