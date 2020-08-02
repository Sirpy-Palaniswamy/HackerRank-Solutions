#Problem
"""
You are given a 2-D array with dimensions N X M.
Your task is to perform the sum tool over axis 0 and then find the product of that result.
"""

#Code
import numpy as np
n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)],int)
print(np.prod(np.sum(a, axis = 0), axis = 0))
