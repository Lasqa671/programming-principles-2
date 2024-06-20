"""
Write a function that accepts string from 
user and print all permutations of that string.
"""
from itertools import permutations

def print_permutations(input_string):
    for perm in permutations(input_string):
        print(''.join(perm))
user_input = input()
print_permutations(user_input)