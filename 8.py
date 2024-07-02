"""
Write a Python program to split a string at 
uppercase letters.
"""
import re
txt = input()
result = re.split(r'(?=[A-Z])', txt)
print(result)