"""
Write a Python program to print yesterday, 
today, tomorrow.
"""
from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%y/%m/%d"))
print("Today:", today.strftime("%y/%m/%d"))
print("Tomorrow:", tomorrow.strftime("%y/%m/%d"))