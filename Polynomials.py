#Problem
"""
You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.
"""

#Code
import numpy as np
P = list(map(float,input().split()))
x = int(input())
print(np.polyval(P,x))
