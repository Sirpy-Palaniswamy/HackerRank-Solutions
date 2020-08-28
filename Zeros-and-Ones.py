#Problem
"""
You are given the shape of the array in the form of space-separated integers, 
each integer representing the size of different dimensions, 
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.
"""

#Code
import numpy as np
l = tuple(map(int,input().split()))   
print(np.zeros((l), dtype = np.int))
print(np.ones((l), dtype = np.int))
