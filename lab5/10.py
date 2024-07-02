"""
Write a Python program to convert a given camel 
case string to snake case.
"""
import re
camel = input()
snake = re.sub(r"([A-Z])", r" \1", camel)
snake = snake.lower()
snake = snake.strip()
snake = re.sub(r'\s', '_', snake)
print(snake)