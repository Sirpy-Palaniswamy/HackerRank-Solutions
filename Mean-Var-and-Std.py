#Problem
"""
You are given a 2-D array of size N X M.
Your task is to find:
1. The mean along axis 1
2. The var along axis 0
3. The std along axis None
"""

#Code
import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
arr = np.array(l)
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.std(arr, axis = None))
