#Problem
"""
You are given a list of N lowercase English letters. 
For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""

#Code
from itertools import combinations
n = int(input())
l = input().split()
k = int(input())
C = list(combinations(l, k))
f = filter(lambda c: 'a' in c, C)
print("{0:.4}".format(len(list(f))/len(C)))
