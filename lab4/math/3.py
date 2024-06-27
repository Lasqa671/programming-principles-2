"""
Write a Python program to calculate the area of 
regular polygon.
"""
import math

num_sides = int(input("Number of sides: "))
side_length = float(input("The length of a side: "))

area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

print(f"The area of the pokygon is: {area}")