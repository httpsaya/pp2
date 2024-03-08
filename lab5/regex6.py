def replace_chars(input_string):
    chars_to_replace = [' ', ',', '.']
    for char in chars_to_replace:
        input_string = input_string.replace(char, ':')
    return input_string
input = str(input("Enter a string: "))
print(replace_chars(input))
