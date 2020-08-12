#Problem
"""
You are given a square matrix A with dimensions N X N.
Your task is to find the determinant. 
Note: Round the answer to 2 places after the decimal.
"""

#Code
import numpy as np
n = int(input())
a = np.array([list(map(float,input().split()))for _ in range(n)])
print("{:.2}".format(np.linalg.det(a)))
