def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    reversed_string = ''.join(reversed(input_string))
    return input_string == reversed_string

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
