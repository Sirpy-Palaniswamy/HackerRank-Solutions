#Problem
"""
You are given a 1-D array, A.
Your task is to print the Floor, Ceil and Rint of all the elements of A.
"""

#Code
import numpy as np
np.set_printoptions(sign=' ')
arr = np.array(input().split(),float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
