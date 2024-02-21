def square_generator(N):
    for i in range(1, N+2):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
squares = square_generator(n)

for square in squares:
    print(square)