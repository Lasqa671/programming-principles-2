"""
You are given list of numbers 
separated by spaces. Write a function 
filter_prime which will take list of 
numbers as an agrument and returns only 
prime numbers from the list.
"""
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False  # other even numbers are not prime
    # Check for odd factors from 3 up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter with a lambda function to filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list :", numbers)
# Print the prime numbers
print("Prime numbers in the list:", prime_numbers)
