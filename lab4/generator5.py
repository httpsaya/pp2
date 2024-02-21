def square_generator(b):
    while b >= 0:
        yield b
        b -= 1

n = int(input("Enter a number: "))
squares = square_generator(n)

for square in squares:
    print(square)