#Problem
"""
You are given a string S. 
Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.
"""

#Code
from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
