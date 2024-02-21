def square_generator(N):
    for i in range(1, N+1):
        yield i**2

n = int(input("Enter a number: "))
squares = square_generator(n)

for square in squares:
    print(square)