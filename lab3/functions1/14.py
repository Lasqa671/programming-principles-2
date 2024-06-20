"""
Create a python file and import some of the 
functions from the above 13 tasks and try to 
use them.
"""
def f_to_c(f):
    c = (5 / 9) * (f - 32)
    return c
f_temp = float(input())
c_temp = f_to_c(f_temp)
print(f_temp, "degrees Fahrenheit is equal to", c_temp, "degrees Celsius")

def solve(numheads, numlegs):
    if numlegs % 2 != 0 or numheads <= 0:
        print("No solution exists.")
        return None
    num_rabbits = (numlegs - 2 * numheads) / 2
    num_chickens = numheads - num_rabbits

    if num_rabbits < 0 or num_chickens < 0 or num_rabbits !=(num_rabbits) or num_chickens != int(num_chickens):
        print("No solution exists")
        return None
    return int(num_chickens), int(num_rabbits)

num_heads = 42
num_legs = 100
result = solve(num_heads, num_legs)
if result:
    chickens, rabbits = result
    print("There are", chickens, "chickens and", rabbits, "rabbits on the farm")

from itertools import permutations

def print_permutations(input_string):
    for perm in permutations(input_string):
        print(''.join(perm))
user_input = input()
print_permutations(user_input)

import math
def sphere_vol(radius):
    if radius < 0:
        return "Radis must be non-negative"
    else:
        volume = (4/3) * math.pi * radius**3
        return volume

radius = float(input())
result = sphere_vol(radius)
print("The volume of the sphere with radius", radius, "is" , result, "cubic units")

def guess_the_number():
    print("Hello! Whst is your name?")
    name = input()

    print("Well, ",name," I am thinking of a number between 1 and 20")
    secret_number = random.randint(1, 20)

    guesses_taken = 0

    while True:
        print()
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print("Good job", name, "! You guessed my number in ", guesses_taken, "guesses!")
            break

guess_the_number()
import random