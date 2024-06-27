"""
Write a Python program to drop microseconds 
from datetime.
"""
from datetime import datetime

current_datetime = datetime.now()

datetime_without_micros = current_datetime.replace(microsecond=0)

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_micros)