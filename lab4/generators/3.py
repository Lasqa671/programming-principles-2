"""
Define a function with a generator which can 
iterate the numbers, which are divisible by 3 
and 4, between a given range 0 and n.
"""
def div_by_three_and_four_gen(n):
    return(num for num in range(n + 1) if num % 3 == 0 and num % 4 == 0)

def main():
    try:
        n = int(input())
        div_nums = div_by_three_and_four_gen(n)
        print(f"numbers between 0 and {n} divisible by both 3 and 4: {', '.join(map(str, div_nums))}")
    except ValueError:
        print("Please enter a valid integer for n.")

if __name__ == "__main__":
    main()