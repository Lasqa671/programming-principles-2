"""
Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the 
chickens and rabbits in a farm. 
How many rabbits and how many chickens do we
have? create function: 
solve(numheads, numlegs):
"""
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