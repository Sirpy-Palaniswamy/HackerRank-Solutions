#Problem
"""
You are given two integer arrays of size N X P and M X P (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
"""

#Code
import numpy as np
n, m, p = map(int, input().split())
pcol = []
prow = []
for _ in range(n):
    pcol.append(list(map(int, input().split())))
for _ in range(m):
    prow.append(list(map(int, input().split())))
carr = np.array(pcol)
crow = np.array(prow)
print(np.concatenate((carr, crow), axis  = 0))
