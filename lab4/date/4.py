"""
Write a Python program to calculate two date 
difference in seconds.
"""
from datetime import datetime

date_str1 = input("(YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("(YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

time_diff = date2 - date1

difference_in_sec = abs(time_diff.total_seconds())

print("Difference between the two dates in seconds:", difference_in_sec)