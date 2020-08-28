#Problem
"""
You are given a 2-D array with dimensions N X M.
Your task is to perform the min function over axis 1 and then find the max of that.
"""

#Code
import numpy as np
n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
arr = np.array(l)
print(np.max(np.min(arr, axis = 1)))
