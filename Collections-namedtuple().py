#Problem
"""
Dr. John Wesley has a spreadsheet containing a list of student's ID, marks, name and class.
Your task is to help Dr. Wesley calculate the average marks of the students.

            Sum Of the all Marks
  Average = --------------------
               Total Student         
"""

#Code
from collections import namedtuple
n = int(input())
sheet = namedtuple('sheet',input().split())
sum = 0
for i in range(n):
    excel = sheet(*(input().split()))
    sum += int(excel.MARKS)
print(sum/n)
