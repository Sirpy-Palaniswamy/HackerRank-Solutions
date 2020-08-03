#Problem
"""
You are given a string S.
Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.
"""

#Code
from itertools import combinations_with_replacement as cwr
S,K = input().split()
print(*[''.join(i) for i in cwr(sorted(S),int(K))],sep='\n')
