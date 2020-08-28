#Problem
"""
You are given a N X M integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.
"""

#Code
import numpy as np
n, m = map(int, input().split())
lis = []
for _ in range(n):
    lis.append((list(map(int, input().split()))))
arr = np.array(lis)
print(np.transpose(arr))
print(arr.flatten())
