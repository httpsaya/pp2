def square_generator(N):
    for i in range(1, N+2):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
squares = square_generator(n)

for square in squares:
    print(square)