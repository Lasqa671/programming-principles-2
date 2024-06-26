"""
Create a generator that generates the squares 
of numbers up to some number N.
"""
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

N = int(input())
squares = square_generator(N)

for square in squares:
    print(square)