#Problem
"""
You are given a date. Your task is to find what the day is on that date.
"""

#Code
import calendar
m , d, y = map(int,input().split())
n = calendar.weekday(y, m, d)
dayname = calendar.day_name[n]
print(dayname.upper())
