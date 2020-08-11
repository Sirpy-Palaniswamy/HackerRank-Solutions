#Problem
"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
"""

#Code
for i in range(int(input())):
    aele = int(input())
    a = set(list(map(int,input().split())))
    bele = int(input())
    b = set(list(map(int,input().split())))
    print(a.issubset(b))
    
