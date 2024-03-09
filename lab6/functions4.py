import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    return result

number = 25100
milliseconds = 2123
result = calculate_square_root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
