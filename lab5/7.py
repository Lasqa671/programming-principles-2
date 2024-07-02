"""
Write a python program to convert snake case string 
to camel case string.
"""
import re
snake = input()
camel_str = snake.title().replace('_', '')
camel_str = camel_str[0].lower() + camel_str[1:]
print(camel_str)