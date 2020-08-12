#Problem
"""
Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.
"""

#Code
import numpy as np
n,m = map(int,input().split())
np.set_printoptions(legacy='1.13')
print(np.eye(n,m, k = 0))
