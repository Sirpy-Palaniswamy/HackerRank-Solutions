#Problem
"""
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
"""

#Code
from itertools import permutations
S,K = input().split()
print(*[''.join(i) for i in permutations(sorted(S),int(K))],sep='\n')
