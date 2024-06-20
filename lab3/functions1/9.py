"""
Write a function that computes the volume of
a sphere given its radius.
"""
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
