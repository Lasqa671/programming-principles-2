"""
Read in a Fahrenheit temperature. 
Calculate and display the equivalent 
centigrade temperature. The following formula 
is used for the conversion: 
C = (5 / 9) * (F – 32)
"""

def f_to_c(f):
    c = (5 / 9) * (f - 32)
    return c
f_temp = float(input())
c_temp = f_to_c(f_temp)
print(f_temp, "degrees Fahrenheit is equal to", c_temp, "degrees Celsius")