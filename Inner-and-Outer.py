#Problem
"""
You are given two arrays: A and B.
Your task is to compute their inner and outer product.
"""

#Code
import numpy as np
a = np.array(list(map(int,input().split())))
b = np.array(list(map(int,input().split())))
print(np.inner(a,b))
print(np.outer(a,b))
