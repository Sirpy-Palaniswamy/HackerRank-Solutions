#Problem
"""
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
"""

#Code
from itertools import combinations
S,K = input().split()
for i in range(1,int(K)+1):
    print(*[''.join(j) for j in combinations(sorted(S),i)],sep='\n')
