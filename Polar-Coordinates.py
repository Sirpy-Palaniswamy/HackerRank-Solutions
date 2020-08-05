#Problem
"""
You are given a complex z. Your task is to convert it to polar coordinates.
"""

#Code
from cmath import *
z = complex(input())
print(abs(z))
print(phase(z))
