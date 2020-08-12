#Problem
"""
You are given two arrays A and B. Both have dimensions of N X N.
Your task is to compute their matrix product.
"""

#Code
import numpy as np
n = int(input())
a = np.array([list(map(int,input().split()))for _ in range(n)])
b = np.array([list(map(int,input().split()))for _ in range(n)])
print(np.dot(a,b))
