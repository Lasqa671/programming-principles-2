"""
Implement a generator called squares to yield 
the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of 
the yielded values.
"""
def squares_gen(a, b):
    for num in range(a, b + 1):
        yield num ** 2

def main():
    try:
        a = int(input())
        b = int(input())

        for square in squares_gen(a, b):
            print(square)
    except ValueError:
        print("Please enter valid integers for a and b.")

if __name__ == "__main__":
    main()