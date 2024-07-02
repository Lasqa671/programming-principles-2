"""
Write a Python program that matches a string that 
has an 'a' followed by two to three 'b'.
"""
import re
txt = input()
match = re.search( 'a(b{2,3})', txt)
if match:
    print("ok")
else:
    print("no")