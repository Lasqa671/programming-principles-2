"""
Write a Python program that matches a string that 
has an 'a' followed by zero or more 'b''s.
"""
import re
txt = input()
match = re.search('a.*b', txt)
print(match)