#Problem
"""
You are given a space separated list of nine integers. 
Your task is to convert this list into a 3 X 3 NumPy array.
"""

#Code
import numpy as np
arr = np.array(list(map(int,input().split())))
arr.shape = (3, 3)
print(arr)
