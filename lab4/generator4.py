def square_generator(a,b):
    for i in range(a, b + 1):
        yield i**2

a = int(input("Enter a number: "))
n = int(input("Enter a number: "))
squares = square_generator(a, n)

for square in squares:
    print(square)