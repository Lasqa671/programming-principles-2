"""
Implement a generator that returns all 
numbers from (n) down to 0.
"""
def countdown_gen(n):
    while n >= 0:
        yield n 
        n -= 1

def main():
    try:
        n = int(input())
        countdown = countdown_gen(n)
        print(f"Countdown from {n} to 0: {', '.join(map(str, countdown))}")
    except ValueError:
        print("Please enter a valid integer for n.")

if __name__ == "__main__":
    main()