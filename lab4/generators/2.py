"""
Write a program using generator to print the 
even numbers between 0 and n in comma separated 
form where n is input from console.
"""
def even_nums_gen(n):
    return(i for i in range(0, n + 1, 2))

def main():
    try:
        n = int(input())
        even_nums = even_nums_gen(n)
        print(f"Even numbers between 0 and {n} in comma-separated form: {','.join(str(num) for num in even_nums)}")
    except ValueError:
        print("Please enter a valid inteher for n.")

if __name__ == "__main__":
    main()